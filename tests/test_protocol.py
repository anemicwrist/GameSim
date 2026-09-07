import json

import pytest

from padserver import protocol


def test_hello_round_trip():
    msg = protocol.parse(json.dumps({"t": "hello", "token": "abc", "name": "Pixel"}))
    assert isinstance(msg, protocol.Hello)
    assert msg.token == "abc"
    assert msg.name == "Pixel"


def test_hello_truncates_long_name():
    msg = protocol.parse(json.dumps({"t": "hello", "token": "abc", "name": "x" * 100}))
    assert len(msg.name) == 32


def test_input_masks_unknown_bits_and_clamps_axes():
    msg = protocol.parse(json.dumps({"t": "in", "b": 0xFFFF, "x": -7, "y": 4}))
    assert msg.buttons == protocol.BUTTON_MASK
    assert (msg.x, msg.y) == (-1, 1)


def test_input_pressed_names():
    msg = protocol.parse(json.dumps({"t": "in", "b": (1 << 0) | (1 << 5)}))
    assert msg.pressed() == ["LP", "A2"]


def test_input_defaults_to_neutral():
    msg = protocol.parse(json.dumps({"t": "in"}))
    assert (msg.buttons, msg.x, msg.y) == (0, 0, 0)


def test_ping():
    msg = protocol.parse(json.dumps({"t": "ping", "ts": 12.5}))
    assert msg.ts == 12.5


@pytest.mark.parametrize(
    "raw",
    [
        "not json",
        "[]",
        '{"t":"nope"}',
        '{"t":"hello"}',
        '{"t":"hello","token":""}',
        '{"t":"hello","token":123}',
        '{"t":"in","b":"3"}',
        '{"t":"in","b":true}',
        '{"t":"in","b":-1}',
        '{"t":"in","x":"left"}',
        '{"t":"ping","ts":"now"}',
    ],
)
def test_rejects_bad_messages(raw):
    with pytest.raises(protocol.ProtocolError):
        protocol.parse(raw)


def test_rejects_oversized_message():
    with pytest.raises(protocol.ProtocolError):
        protocol.parse("x" * (protocol.MAX_MESSAGE_BYTES + 1))


def test_bit_positions_are_unique_and_dense():
    bits = sorted(protocol.BUTTON_BITS.values())
    assert bits == list(range(len(protocol.BUTTON_ORDER)))


def test_pad_js_mirrors_the_bit_table():
    """The phone page hardcodes the same bit positions; keep them in sync."""
    import pathlib
    import re

    js = (pathlib.Path(protocol.__file__).parent / "static" / "pad.js").read_text()
    body = re.search(r"const BITS = \{(.*?)\};", js, re.S).group(1)
    found = dict((m.group(1), int(m.group(2))) for m in re.finditer(r"(\w+):\s*(\d+)", body))
    assert found == protocol.BUTTON_BITS
