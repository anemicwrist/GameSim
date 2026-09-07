"""scripts/uinput_check.py decides which backend the host can support, so its
errno classification is load-bearing: getting it wrong sends the user down the
wrong setup path. The filesystem is never touched here."""

import errno
import importlib.util
import pathlib

import pytest

SPEC = importlib.util.spec_from_file_location(
    "uinput_check", pathlib.Path(__file__).parent.parent / "scripts" / "uinput_check.py"
)
uinput_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(uinput_check)


@pytest.mark.parametrize(
    "code, expected",
    [
        # A node made by mknod in a container with no driver behind it.
        (errno.ENODEV, uinput_check.NODRIVER),
        (errno.ENXIO, uinput_check.NODRIVER),
        # Driver present, but this user or container cgroup may not use it.
        (errno.EACCES, uinput_check.DENIED),
        (errno.EPERM, uinput_check.DENIED),
        (errno.ENOENT, uinput_check.NONODE),
    ],
)
def test_errno_maps_to_the_right_verdict(code, expected):
    assert uinput_check.classify(OSError(code, "boom")) == expected


def test_unknown_errno_is_treated_as_no_driver():
    # Better to send the user to the backend that always works than to claim
    # a gamepad will appear when we cannot show that it will.
    assert uinput_check.classify(OSError(errno.EIO, "boom")) == uinput_check.NODRIVER


def test_every_verdict_has_an_exit_code_and_advice():
    verdicts = {
        uinput_check.OK,
        uinput_check.NODRIVER,
        uinput_check.DENIED,
        uinput_check.NONODE,
    }
    assert set(uinput_check.EXIT_CODES) == verdicts
    assert set(uinput_check.ADVICE) == verdicts


def test_only_success_exits_zero():
    zero = [v for v, code in uinput_check.EXIT_CODES.items() if code == 0]
    assert zero == [uinput_check.OK]


def test_no_create_does_not_invent_a_node(monkeypatch):
    monkeypatch.setattr(uinput_check, "node_exists", lambda: False)
    monkeypatch.setattr(
        uinput_check, "try_mknod", lambda: pytest.fail("must not mknod with --no-create")
    )
    verdict, detail = uinput_check.probe(create=False)
    assert verdict == uinput_check.NONODE
    assert "does not exist" in detail


def test_nodriver_is_reported_when_the_node_will_not_open(monkeypatch):
    monkeypatch.setattr(uinput_check, "node_exists", lambda: True)

    def refuse(*_args, **_kwargs):
        raise OSError(errno.ENODEV, "No such device")

    monkeypatch.setattr(uinput_check.os, "open", refuse)
    verdict, detail = uinput_check.probe()
    assert verdict == uinput_check.NODRIVER
    assert "No such device" in detail
