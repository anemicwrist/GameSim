"""Linux backend: creates kernel-level virtual gamepads with uinput.

The devices deliberately impersonate a wired Xbox 360 controller (vendor
0x045e, product 0x028e, version 0x0110, name "Microsoft X-Box 360 pad"), and
declare exactly the same buttons and axes in the same order as the kernel's
xpad driver. SDL2 therefore computes the GUID 030000005e0400008e02000010010000,
finds that entry in its built-in controller database, and exposes the pad
through the SDL_GameController API. Flycast's built-in default mapping
(core/sdl/sdl_gamepad.cpp) then binds it to the Dreamcast pad with no mapping
file needed:

    SDL A/B/X/Y  -> Dreamcast A/B/X/Y
    SDL LT / RT  -> Dreamcast L / R triggers
    SDL start    -> Dreamcast start
    SDL back     -> Flycast menu
    SDL dpad     -> Dreamcast dpad

Which lands the MvC2 layout on the six touch buttons:
    LP=X  HP=Y  LK=A  HK=B  A1=L  A2=R
"""

from __future__ import annotations

from padserver.protocol import BUTTON_BITS

try:  # pragma: no cover - exercised only on Linux with evdev installed
    from evdev import AbsInfo, UInput
    from evdev import ecodes as e

    EVDEV_IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    UInput = None  # type: ignore[assignment]
    AbsInfo = None  # type: ignore[assignment]
    e = None  # type: ignore[assignment]
    EVDEV_IMPORT_ERROR = exc

PAD_NAME = "Microsoft X-Box 360 pad"
PAD_VENDOR = 0x045E
PAD_PRODUCT = 0x028E
PAD_VERSION = 0x0110
PAD_BUSTYPE = 0x03  # BUS_USB

STICK_MAX = 32767
TRIGGER_MAX = 255


def _capabilities():
    """Button and axis set of the kernel xpad driver, in event-code order."""
    return {
        e.EV_KEY: [
            e.BTN_SOUTH,  # A      -> joystick button 0
            e.BTN_EAST,  # B      -> 1
            e.BTN_NORTH,  # X      -> 2
            e.BTN_WEST,  # Y      -> 3
            e.BTN_TL,  # LB     -> 4
            e.BTN_TR,  # RB     -> 5
            e.BTN_SELECT,  # back   -> 6
            e.BTN_START,  # start  -> 7
            e.BTN_MODE,  # guide  -> 8
            e.BTN_THUMBL,  # LS     -> 9
            e.BTN_THUMBR,  # RS     -> 10
        ],
        e.EV_ABS: [
            (e.ABS_X, AbsInfo(0, -STICK_MAX - 1, STICK_MAX, 16, 128, 0)),
            (e.ABS_Y, AbsInfo(0, -STICK_MAX - 1, STICK_MAX, 16, 128, 0)),
            (e.ABS_Z, AbsInfo(0, 0, TRIGGER_MAX, 0, 0, 0)),
            (e.ABS_RX, AbsInfo(0, -STICK_MAX - 1, STICK_MAX, 16, 128, 0)),
            (e.ABS_RY, AbsInfo(0, -STICK_MAX - 1, STICK_MAX, 16, 128, 0)),
            (e.ABS_RZ, AbsInfo(0, 0, TRIGGER_MAX, 0, 0, 0)),
            (e.ABS_HAT0X, AbsInfo(0, -1, 1, 0, 0, 0)),
            (e.ABS_HAT0Y, AbsInfo(0, -1, 1, 0, 0, 0)),
        ],
    }


def _key_map():
    return {
        "LP": e.BTN_NORTH,
        "HP": e.BTN_WEST,
        "LK": e.BTN_SOUTH,
        "HK": e.BTN_EAST,
        "START": e.BTN_START,
        "SELECT": e.BTN_SELECT,
    }


def _trigger_map():
    return {"A1": e.ABS_Z, "A2": e.ABS_RZ}


class UinputPad:
    def __init__(self, name: str, mirror_analog: bool = True):
        self.name = name
        self.mirror_analog = mirror_analog
        self._keys = _key_map()
        self._triggers = _trigger_map()
        self._ui = UInput(
            _capabilities(),
            name=name,
            vendor=PAD_VENDOR,
            product=PAD_PRODUCT,
            version=PAD_VERSION,
            bustype=PAD_BUSTYPE,
        )
        self._state = {}
        self.reset()

    @property
    def device_path(self) -> str:
        return self._ui.device.path

    def set_state(self, buttons: int, x: int, y: int) -> None:
        ui = self._ui
        changed = False

        for logical, code in self._keys.items():
            value = 1 if buttons & (1 << BUTTON_BITS[logical]) else 0
            if self._state.get(("key", code)) != value:
                self._state[("key", code)] = value
                ui.write(e.EV_KEY, code, value)
                changed = True

        for logical, code in self._triggers.items():
            value = TRIGGER_MAX if buttons & (1 << BUTTON_BITS[logical]) else 0
            if self._state.get(("abs", code)) != value:
                self._state[("abs", code)] = value
                ui.write(e.EV_ABS, code, value)
                changed = True

        axes = [(e.ABS_HAT0X, x), (e.ABS_HAT0Y, y)]
        if self.mirror_analog:
            axes += [(e.ABS_X, x * STICK_MAX), (e.ABS_Y, y * STICK_MAX)]
        for code, value in axes:
            if self._state.get(("abs", code)) != value:
                self._state[("abs", code)] = value
                ui.write(e.EV_ABS, code, value)
                changed = True

        if changed:
            ui.syn()

    def reset(self) -> None:
        self._state = {}
        self.set_state(0, 0, 0)

    def close(self) -> None:
        try:
            self.reset()
        finally:
            self._ui.close()


class UinputBackend:
    name = "uinput"

    def __init__(self, mirror_analog: bool = True):
        if UInput is None:
            raise RuntimeError(
                "the uinput backend needs python-evdev: pip install evdev "
                f"(import failed: {EVDEV_IMPORT_ERROR})"
            )
        self.mirror_analog = mirror_analog
        self.pads: list = []

    def create_pad(self, name: str) -> UinputPad:
        try:
            pad = UinputPad(name, mirror_analog=self.mirror_analog)
        except (PermissionError, FileNotFoundError) as exc:
            raise RuntimeError(
                "cannot open /dev/uinput. Run scripts/install_deps.sh, which loads "
                "the uinput module and installs a udev rule, then log out and back "
                "in. As a last resort run the server with sudo. "
                f"(original error: {exc})"
            ) from exc
        self.pads.append(pad)
        return pad

    def close(self) -> None:
        for pad in self.pads:
            try:
                pad.close()
            except Exception:
                pass
