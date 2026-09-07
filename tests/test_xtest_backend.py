"""XtestPad drives the emulator by pressing and releasing real keys, so the
event stream has to be exactly right: transitions only, and never two opposite
directions held at once. Xlib is stubbed so this runs with no X server."""

import pytest

from padserver.backends import xtest as xtest_backend
from padserver.protocol import BUTTON_BITS

PRESS, RELEASE = 2, 3


class StubX:
    KeyPress = PRESS
    KeyRelease = RELEASE


class StubXtest:
    def __init__(self):
        self.events = []

    def fake_input(self, _display, kind, keycode):
        self.events.append((kind, keycode))


class StubDisplay:
    def __init__(self):
        self.syncs = 0

    def sync(self):
        self.syncs += 1


# Keycodes are arbitrary but distinct, so events can be traced back to controls.
KEYCODES = {
    "UP": 10,
    "DOWN": 11,
    "LEFT": 12,
    "RIGHT": 13,
    "LP": 14,
    "HP": 15,
    "LK": 16,
    "HK": 17,
    "A1": 18,
    "A2": 19,
    "START": 20,
    "SELECT": 21,
}
BY_KEYCODE = {v: k for k, v in KEYCODES.items()}


@pytest.fixture
def pad(monkeypatch):
    stub = StubXtest()
    monkeypatch.setattr(xtest_backend, "X", StubX)
    monkeypatch.setattr(xtest_backend, "xtest", stub)
    display = StubDisplay()
    pad = xtest_backend.XtestPad("test pad", display, KEYCODES)
    pad.stub = stub
    pad.display = display
    return pad


def readable(events):
    return [("press" if k == PRESS else "release", BY_KEYCODE[c]) for k, c in events]


def bit(name):
    return 1 << BUTTON_BITS[name]


def test_pressing_a_button_emits_one_press(pad):
    pad.set_state(bit("LP"), 0, 0)
    assert readable(pad.stub.events) == [("press", "LP")]


def test_holding_the_same_state_emits_nothing_further(pad):
    pad.set_state(bit("LP"), 0, 0)
    pad.stub.events.clear()
    pad.set_state(bit("LP"), 0, 0)
    pad.set_state(bit("LP"), 0, 0)
    assert pad.stub.events == []


def test_releasing_a_button_emits_one_release(pad):
    pad.set_state(bit("LP"), 0, 0)
    pad.stub.events.clear()
    pad.set_state(0, 0, 0)
    assert readable(pad.stub.events) == [("release", "LP")]


def test_direction_signs_follow_the_hat_convention(pad):
    pad.set_state(0, 0, -1)
    assert readable(pad.stub.events) == [("press", "UP")]
    pad.stub.events.clear()
    pad.set_state(0, 0, 1)
    assert readable(pad.stub.events) == [("release", "UP"), ("press", "DOWN")]


def test_flicking_left_to_right_never_holds_both(pad):
    pad.set_state(0, -1, 0)
    pad.stub.events.clear()
    pad.set_state(0, 1, 0)
    # The release must come first, or the emulator sees left+right together.
    assert readable(pad.stub.events) == [("release", "LEFT"), ("press", "RIGHT")]


def test_a_super_combination_presses_everything_once(pad):
    pad.set_state(bit("LP") | bit("HP") | bit("A1"), -1, 1)
    assert sorted(readable(pad.stub.events)) == sorted(
        [
            ("press", "LP"),
            ("press", "HP"),
            ("press", "A1"),
            ("press", "LEFT"),
            ("press", "DOWN"),
        ]
    )


def test_one_sync_per_state_change(pad):
    pad.set_state(bit("LP"), 0, 0)
    pad.set_state(bit("HP"), 1, 0)
    assert pad.display.syncs == 2


def test_no_sync_when_nothing_changed(pad):
    pad.set_state(bit("LP"), 0, 0)
    before = pad.display.syncs
    pad.set_state(bit("LP"), 0, 0)
    assert pad.display.syncs == before


def test_reset_releases_everything(pad):
    pad.set_state(bit("LP") | bit("HK"), 1, -1)
    pad.stub.events.clear()
    pad.reset()
    assert sorted(readable(pad.stub.events)) == sorted(
        [("release", "LP"), ("release", "HK"), ("release", "RIGHT"), ("release", "UP")]
    )


def test_close_releases_then_ignores_further_input(pad):
    pad.set_state(bit("LP"), 0, 0)
    pad.stub.events.clear()
    pad.close()
    assert readable(pad.stub.events) == [("release", "LP")]
    pad.stub.events.clear()
    pad.set_state(bit("HP"), 0, 0)
    assert pad.stub.events == []


def test_describe_reports_what_is_held(pad):
    pad.set_state(bit("A2"), 0, -1)
    assert pad.describe() == {"name": "test pad", "held": ["A2", "UP"]}
