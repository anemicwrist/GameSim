"""The vigem backend had no coverage at all: it is Windows-only and was marked
pragma: no cover, so its button mapping had never been asserted anywhere. A
wrong mapping means punches come out as kicks, which is confusing rather than
obviously broken. vgamepad is stubbed, so this runs on any platform."""

import sys
import types

import pytest

from padserver.protocol import BUTTON_BITS

BUTTON_NAMES = [
    "XUSB_GAMEPAD_A",
    "XUSB_GAMEPAD_B",
    "XUSB_GAMEPAD_X",
    "XUSB_GAMEPAD_Y",
    "XUSB_GAMEPAD_START",
    "XUSB_GAMEPAD_BACK",
    "XUSB_GAMEPAD_DPAD_UP",
    "XUSB_GAMEPAD_DPAD_DOWN",
    "XUSB_GAMEPAD_DPAD_LEFT",
    "XUSB_GAMEPAD_DPAD_RIGHT",
]


class StubGamepad:
    def __init__(self):
        self.pressed = set()
        self.left = 0
        self.right = 0
        self.stick = (0, 0)
        self.updates = 0
        self.resets = 0

    def reset(self):
        self.pressed.clear()
        self.left = self.right = 0
        self.stick = (0, 0)
        self.resets += 1

    def press_button(self, button):
        self.pressed.add(button)

    def left_trigger(self, value):
        self.left = value

    def right_trigger(self, value):
        self.right = value

    def left_joystick(self, x_value, y_value):
        self.stick = (x_value, y_value)

    def update(self):
        self.updates += 1


@pytest.fixture
def vigem(monkeypatch):
    """Install a stub vgamepad, then import the backend against it."""
    stub = types.ModuleType("vgamepad")
    stub.XUSB_BUTTON = types.SimpleNamespace(**{name: name for name in BUTTON_NAMES})
    stub.VX360Gamepad = StubGamepad
    monkeypatch.setitem(sys.modules, "vgamepad", stub)

    for name in list(sys.modules):
        if name == "padserver.backends.vigem":
            monkeypatch.delitem(sys.modules, name)
    import padserver.backends.vigem as module

    monkeypatch.setattr(module, "vg", stub)
    monkeypatch.setattr(module, "VGAMEPAD_IMPORT_ERROR", None)
    return module


@pytest.fixture
def pad(vigem):
    return vigem.VigemBackend().create_pad("player 1")


def bit(name):
    return 1 << BUTTON_BITS[name]


@pytest.mark.parametrize(
    "control, expected",
    [
        # Dreamcast layout: light punch is X, heavy punch is Y, kicks are A/B.
        ("LP", "XUSB_GAMEPAD_X"),
        ("HP", "XUSB_GAMEPAD_Y"),
        ("LK", "XUSB_GAMEPAD_A"),
        ("HK", "XUSB_GAMEPAD_B"),
        ("START", "XUSB_GAMEPAD_START"),
        ("SELECT", "XUSB_GAMEPAD_BACK"),
    ],
)
def test_button_mapping(pad, control, expected):
    pad.set_state(bit(control), 0, 0)
    assert expected in pad._pad.pressed


def test_assists_are_triggers_not_buttons(pad):
    pad.set_state(bit("A1"), 0, 0)
    assert pad._pad.left == 255 and pad._pad.right == 0
    pad.set_state(bit("A2"), 0, 0)
    assert pad._pad.right == 255 and pad._pad.left == 0


def test_triggers_release(pad):
    pad.set_state(bit("A1") | bit("A2"), 0, 0)
    pad.set_state(0, 0, 0)
    assert pad._pad.left == 0 and pad._pad.right == 0


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (0, -1, "XUSB_GAMEPAD_DPAD_UP"),
        (0, 1, "XUSB_GAMEPAD_DPAD_DOWN"),
        (-1, 0, "XUSB_GAMEPAD_DPAD_LEFT"),
        (1, 0, "XUSB_GAMEPAD_DPAD_RIGHT"),
    ],
)
def test_dpad_directions(pad, x, y, expected):
    pad.set_state(0, x, y)
    assert expected in pad._pad.pressed


def test_diagonals_press_both_directions(pad):
    pad.set_state(0, -1, 1)  # down-back, the blocking direction
    assert "XUSB_GAMEPAD_DPAD_LEFT" in pad._pad.pressed
    assert "XUSB_GAMEPAD_DPAD_DOWN" in pad._pad.pressed


def test_neutral_presses_no_direction(pad):
    pad.set_state(0, 0, 0)
    assert not any("DPAD" in button for button in pad._pad.pressed)


def test_stick_y_is_inverted_for_xinput(pad):
    # XInput has +Y as up, while the protocol has y = -1 as up.
    pad.set_state(0, 0, -1)
    assert pad._pad.stick == (0, 32767)
    pad.set_state(0, 0, 1)
    assert pad._pad.stick == (0, -32767)


def test_stick_x_is_not_inverted(pad):
    pad.set_state(0, 1, 0)
    assert pad._pad.stick[0] == 32767


def test_each_state_is_sent_once(pad):
    pad.set_state(bit("LP"), 0, 0)
    pad.set_state(bit("HP"), 0, 0)
    assert pad._pad.updates == 2


def test_state_is_rebuilt_each_time_so_buttons_release(pad):
    # ViGEm takes a whole state, so the previous frame must not linger.
    pad.set_state(bit("LP"), 0, 0)
    pad.set_state(bit("HP"), 0, 0)
    assert "XUSB_GAMEPAD_X" not in pad._pad.pressed
    assert "XUSB_GAMEPAD_Y" in pad._pad.pressed


def test_a_super_holds_several_buttons_at_once(pad):
    pad.set_state(bit("LP") | bit("HP") | bit("A1"), 0, 0)
    assert {"XUSB_GAMEPAD_X", "XUSB_GAMEPAD_Y"} <= pad._pad.pressed
    assert pad._pad.left == 255


def test_backend_reports_a_clear_error_without_the_driver(vigem, monkeypatch):
    monkeypatch.setattr(vigem, "vg", None)
    with pytest.raises(RuntimeError, match="ViGEmBus"):
        vigem.VigemBackend()
