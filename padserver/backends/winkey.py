"""Windows backend: synthetic key events through the Win32 SendInput API.

The counterpart to the uinput/vigem split on Linux. `vigem` is the better
Windows backend, but it needs the ViGEmBus kernel-mode driver, and installing a
driver requires administrator rights that a managed or work-owned machine often
withholds. This backend needs no driver, no elevation and no install beyond
Python itself, so it works where `vigem` cannot.

It is the exact Windows analogue of `xtest.py`: both players share one keyboard,
both take their key assignments from padserver/keymap.py, and the emulator side
is RetroArch with the Flycast core, configured by scripts/configure_retroarch.py
from that same module. Standalone Flycast cannot bind one keyboard to two
Dreamcast ports, which is why this path uses RetroArch.

Scan codes rather than virtual key codes are sent, because emulators commonly
read the keyboard through DirectInput or Raw Input, which look at the scan code
and ignore the virtual key. All of a frame's changes go out in a single
SendInput call, so a move and the button that goes with it land together rather
than in separate batches.
"""

from __future__ import annotations

import sys

from padserver.keymap import keys_for_player
from padserver.protocol import BUTTON_BITS, BUTTON_ORDER

# Virtual key codes for the keysym names used in keymap.py, with a flag for the
# "extended" keys. The arrow keys live on the extended part of the keyboard and
# are rejected or misread if that flag is not set.
_ARROW_VKS = {
    "Up": (0x26, True),
    "Down": (0x28, True),
    "Left": (0x25, True),
    "Right": (0x27, True),
}

INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008
MAPVK_VK_TO_VSC = 0

try:  # pragma: no cover - Windows only
    import ctypes
    from ctypes import wintypes

    class _MOUSEINPUT(ctypes.Structure):
        _fields_ = [
            ("dx", wintypes.LONG),
            ("dy", wintypes.LONG),
            ("mouseData", wintypes.DWORD),
            ("dwFlags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
        ]

    class _KEYBDINPUT(ctypes.Structure):
        _fields_ = [
            ("wVk", wintypes.WORD),
            ("wScan", wintypes.WORD),
            ("dwFlags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
        ]

    class _HARDWAREINPUT(ctypes.Structure):
        _fields_ = [
            ("uMsg", wintypes.DWORD),
            ("wParamL", wintypes.WORD),
            ("wParamH", wintypes.WORD),
        ]

    class _INPUTUNION(ctypes.Union):
        _fields_ = [("mi", _MOUSEINPUT), ("ki", _KEYBDINPUT), ("hi", _HARDWAREINPUT)]

    class _INPUT(ctypes.Structure):
        _fields_ = [("type", wintypes.DWORD), ("u", _INPUTUNION)]

    WINKEY_IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover - not Windows
    ctypes = None  # type: ignore[assignment]
    WINKEY_IMPORT_ERROR = exc


class SendInputSender:  # pragma: no cover - Windows only
    """Sends batches of key transitions through SendInput."""

    def __init__(self):
        self._user32 = ctypes.WinDLL("user32", use_last_error=True)

    def scancode_for(self, vk: int) -> int:
        return self._user32.MapVirtualKeyW(vk, MAPVK_VK_TO_VSC)

    def send(self, events) -> None:
        """events: iterable of (scancode, extended, down)."""
        events = list(events)
        if not events:
            return
        array = (_INPUT * len(events))()
        for index, (scancode, extended, down) in enumerate(events):
            flags = KEYEVENTF_SCANCODE
            if extended:
                flags |= KEYEVENTF_EXTENDEDKEY
            if not down:
                flags |= KEYEVENTF_KEYUP
            array[index].type = INPUT_KEYBOARD
            array[index].u.ki = _KEYBDINPUT(
                wVk=0, wScan=scancode, dwFlags=flags, time=0, dwExtraInfo=None
            )
        sent = self._user32.SendInput(len(events), array, ctypes.sizeof(_INPUT))
        if sent != len(events):
            raise OSError(ctypes.get_last_error(), "SendInput was blocked or failed")


class WinkeyPad:
    """One player's share of the keyboard."""

    def __init__(self, name: str, sender, keys: dict[str, tuple[int, bool]]):
        self.name = name
        self._sender = sender
        self._keys = keys
        self._down: set[str] = set()
        self.closed = False

    def _controls_for(self, buttons: int, x: int, y: int) -> set[str]:
        active = {n for n in BUTTON_ORDER if buttons & (1 << BUTTON_BITS[n])}
        if x < 0:
            active.add("LEFT")
        elif x > 0:
            active.add("RIGHT")
        if y < 0:
            active.add("UP")
        elif y > 0:
            active.add("DOWN")
        return active

    def set_state(self, buttons: int, x: int, y: int) -> None:
        if self.closed:
            return
        wanted = self._controls_for(buttons, x, y)
        if wanted == self._down:
            return

        events = []
        # Release before press, so flicking from left to right never has both
        # held at once, even for a single frame.
        for control in sorted(self._down - wanted):
            scancode, extended = self._keys[control]
            events.append((scancode, extended, False))
        for control in sorted(wanted - self._down):
            scancode, extended = self._keys[control]
            events.append((scancode, extended, True))

        self._down = wanted
        self._sender.send(events)

    def reset(self) -> None:
        self.set_state(0, 0, 0)

    def close(self) -> None:
        if not self.closed:
            self.reset()
            self.closed = True

    def describe(self) -> dict:
        return {"name": self.name, "held": sorted(self._down)}


def virtual_key_for(keysym: str) -> tuple[int, bool]:
    """Map a keymap.py keysym name onto (virtual key code, is_extended)."""
    if keysym in _ARROW_VKS:
        return _ARROW_VKS[keysym]
    if len(keysym) == 1 and keysym.isalpha():
        return ord(keysym.upper()), False
    if len(keysym) == 1 and keysym.isdigit():
        return ord(keysym), False
    raise ValueError(
        f"no Windows virtual key known for the keysym {keysym!r}; "
        "add it to _ARROW_VKS in padserver/backends/winkey.py"
    )


class WinkeyBackend:
    name = "winkey"

    def __init__(self, sender=None):
        if sender is None:  # pragma: no cover - Windows only
            if sys.platform != "win32":
                raise RuntimeError(
                    "the winkey backend is Windows-only; use --backend xtest on Linux"
                )
            if WINKEY_IMPORT_ERROR is not None:
                raise RuntimeError(f"could not load the Win32 API: {WINKEY_IMPORT_ERROR}")
            sender = SendInputSender()
        self._sender = sender
        self._pads: list[WinkeyPad] = []

    def _resolve(self, index: int) -> dict[str, tuple[int, bool]]:
        keys = {}
        for control, keysym in keys_for_player(index).items():
            vk, extended = virtual_key_for(keysym)
            keys[control] = (self._sender.scancode_for(vk), extended)
        return keys

    def create_pad(self, name: str) -> WinkeyPad:
        index = len(self._pads)
        pad = WinkeyPad(name, self._sender, self._resolve(index))
        self._pads.append(pad)
        return pad

    def close(self) -> None:
        for pad in self._pads:
            pad.close()
