"""Windows backend (Plan B): virtual Xbox 360 pads through the ViGEmBus driver.

Requires the ViGEmBus driver (https://github.com/nefarius/ViGEmBus) and
``pip install vgamepad``. Buttons land on the same Xbox layout as the Linux
backend, so Flycast's default mapping produces the same Dreamcast bindings.
"""

from __future__ import annotations

from padserver.protocol import BUTTON_BITS

try:  # pragma: no cover - Windows only
    import vgamepad as vg

    VGAMEPAD_IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    vg = None  # type: ignore[assignment]
    VGAMEPAD_IMPORT_ERROR = exc


class VigemPad:  # pragma: no cover - Windows only
    def __init__(self, name: str):
        self.name = name
        self._pad = vg.VX360Gamepad()
        self._map = {
            "LP": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
            "HP": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
            "LK": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
            "HK": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
            "START": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
            "SELECT": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
        }
        self._dpad = {
            (0, -1): vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
            (0, 1): vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
            (-1, 0): vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
            (1, 0): vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
        }

    def set_state(self, buttons: int, x: int, y: int) -> None:
        pad = self._pad
        pad.reset()
        for logical, code in self._map.items():
            if buttons & (1 << BUTTON_BITS[logical]):
                pad.press_button(code)
        for (dx, dy), code in self._dpad.items():
            if (dx and dx == x) or (dy and dy == y):
                pad.press_button(code)
        pad.left_trigger(value=255 if buttons & (1 << BUTTON_BITS["A1"]) else 0)
        pad.right_trigger(value=255 if buttons & (1 << BUTTON_BITS["A2"]) else 0)
        pad.left_joystick(x_value=x * 32767, y_value=-y * 32767)
        pad.update()

    def reset(self) -> None:
        self._pad.reset()
        self._pad.update()

    def close(self) -> None:
        self.reset()


class VigemBackend:  # pragma: no cover - Windows only
    name = "vigem"

    def __init__(self):
        if vg is None:
            raise RuntimeError(
                "the vigem backend needs the ViGEmBus driver and 'pip install "
                f"vgamepad' (import failed: {VGAMEPAD_IMPORT_ERROR})"
            )
        self.pads: list = []

    def create_pad(self, name: str) -> VigemPad:
        pad = VigemPad(name)
        self.pads.append(pad)
        return pad

    def close(self) -> None:
        for pad in self.pads:
            try:
                pad.close()
            except Exception:
                pass
