"""X11 backend: drives the emulator with synthetic key events through XTEST.

Used where /dev/uinput exists but has no driver behind it, which is the normal
state of affairs inside a container. XTEST needs no kernel device and no
elevated privileges beyond access to the X display, so it works where the
uinput backend cannot.

The cost is that both players share one keyboard, so the emulator has to bind
keys per port. padserver/keymap.py holds the two disjoint key sets, and
scripts/configure_flycast.py generates matching emulator bindings from that
same module, so the two halves cannot drift apart.

Events are sent as presses and releases on transitions only. Holding a
direction sends one KeyPress and nothing further until it is let go, which is
what an emulator expects; re-sending presses would look like key repeat.
"""

from __future__ import annotations

import os

from padserver.keymap import DIRECTIONS, keys_for_player
from padserver.protocol import BUTTON_BITS, BUTTON_ORDER

try:  # pragma: no cover - exercised only on a machine with X11 and python-xlib
    from Xlib import XK, X, display
    from Xlib.ext import xtest

    XLIB_IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    X = XK = display = xtest = None  # type: ignore[assignment]
    XLIB_IMPORT_ERROR = exc


def _install_hint() -> str:
    return (
        "the xtest backend needs python-xlib and an X display.\n"
        "  apt-get install -y python3-xlib   (or: pip install python-xlib)\n"
        f"  DISPLAY is currently {os.environ.get('DISPLAY') or '<unset>'}"
    )


class XtestPad:
    """One player's share of the keyboard."""

    def __init__(self, name: str, disp, keycodes: dict[str, int]):
        self.name = name
        self._display = disp
        self._keycodes = keycodes
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

        # Release first: a stick flicked straight from left to right should not
        # have both directions held at once, even for one event.
        for control in sorted(self._down - wanted):
            xtest.fake_input(self._display, X.KeyRelease, self._keycodes[control])
        for control in sorted(wanted - self._down):
            xtest.fake_input(self._display, X.KeyPress, self._keycodes[control])

        self._down = wanted
        self._display.sync()

    def reset(self) -> None:
        self.set_state(0, 0, 0)

    def close(self) -> None:
        if not self.closed:
            self.reset()
            self.closed = True

    def describe(self) -> dict:
        return {"name": self.name, "held": sorted(self._down)}


class XtestBackend:
    name = "xtest"

    def __init__(self, display_name: str | None = None):
        if XLIB_IMPORT_ERROR is not None:
            raise RuntimeError(f"{_install_hint()}\n  import failed: {XLIB_IMPORT_ERROR}")
        try:
            self._display = display.Display(display_name)
        except Exception as exc:
            raise RuntimeError(f"cannot open the X display.\n  {_install_hint()}") from exc
        if not self._display.query_extension("XTEST"):
            raise RuntimeError("this X server has no XTEST extension, so keys cannot be injected")
        self._pads: list[XtestPad] = []

    def _resolve(self, index: int) -> dict[str, int]:
        """Turn keysym names into keycodes for the server's current layout."""
        mapping = keys_for_player(index)
        keycodes: dict[str, int] = {}
        for control, keysym_name in mapping.items():
            keysym = XK.string_to_keysym(keysym_name)
            if keysym == 0:
                raise RuntimeError(f"X does not know the keysym {keysym_name!r} ({control})")
            keycode = self._display.keysym_to_keycode(keysym)
            if not keycode:
                raise RuntimeError(
                    f"the current keyboard layout has no key for {keysym_name!r} "
                    f"({control}); padserver/keymap.py needs a different assignment"
                )
            keycodes[control] = keycode
        return keycodes

    def create_pad(self, name: str) -> XtestPad:
        index = len(self._pads)
        pad = XtestPad(name, self._display, self._resolve(index))
        self._pads.append(pad)
        return pad

    def close(self) -> None:
        for pad in self._pads:
            pad.close()
        try:
            self._display.close()
        except Exception:  # pragma: no cover - display already gone
            pass


__all__ = ["XtestBackend", "XtestPad", "DIRECTIONS"]
