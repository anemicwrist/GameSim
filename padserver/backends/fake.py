"""In-memory backend. Used by the tests and for trying the phone page without a
kernel device (``python -m padserver --backend fake``)."""

from __future__ import annotations

from padserver.protocol import BUTTON_BITS, BUTTON_ORDER


class FakePad:
    def __init__(self, name: str):
        self.name = name
        self.buttons = 0
        self.x = 0
        self.y = 0
        self.history: list = []
        self.closed = False

    def set_state(self, buttons: int, x: int, y: int) -> None:
        self.buttons, self.x, self.y = buttons, x, y
        self.history.append((buttons, x, y))

    def reset(self) -> None:
        self.set_state(0, 0, 0)

    def close(self) -> None:
        self.closed = True

    def pressed(self) -> list:
        return [n for n in BUTTON_ORDER if self.buttons & (1 << BUTTON_BITS[n])]

    def describe(self) -> dict:
        return {"name": self.name, "buttons": self.pressed(), "x": self.x, "y": self.y}


class FakeBackend:
    name = "fake"

    def __init__(self):
        self.pads: list = []

    def create_pad(self, name: str) -> FakePad:
        pad = FakePad(name)
        self.pads.append(pad)
        return pad

    def close(self) -> None:
        for pad in self.pads:
            pad.close()
