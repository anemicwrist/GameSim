"""Assign the two player slots to phones, and remember who had which."""

from __future__ import annotations

import time
from dataclasses import dataclass, field


@dataclass
class Slot:
    index: int  # 0-based; player number is index + 1
    pad: object
    token: str | None = None
    name: str = ""
    connected: bool = False
    last_seen: float = field(default_factory=time.monotonic)
    inputs: int = 0


class SlotManager:
    """Owns one pad per slot. Pads are created up front, before any phone
    connects, so that the emulator sees a stable set of devices with stable SDL
    joystick instance ids (which is what pins each pad to a Dreamcast port)."""

    def __init__(self, backend, players: int = 2, pad_name: str = "Microsoft X-Box 360 pad"):
        self.backend = backend
        self.slots = [Slot(index=i, pad=backend.create_pad(pad_name)) for i in range(players)]
        # Remembers the last slot a token held, so a phone that drops off wifi
        # for a moment gets its own player back rather than the other one.
        self._history: dict = {}

    @property
    def capacity(self) -> int:
        return len(self.slots)

    def claim(self, token: str, name: str = "") -> Slot | None:
        """Give this token a slot, preferring the one it had before."""
        preferred = self._history.get(token)
        candidates = []
        if preferred is not None:
            candidates.append(self.slots[preferred])
        candidates += self.slots

        for slot in candidates:
            if slot.connected and slot.token != token:
                continue
            slot.token = token
            slot.name = name
            slot.connected = True
            slot.last_seen = time.monotonic()
            slot.pad.reset()
            self._history[token] = slot.index
            return slot
        return None

    def release(self, slot: Slot) -> None:
        slot.connected = False
        slot.pad.reset()

    def apply(self, slot: Slot, buttons: int, x: int, y: int) -> None:
        slot.last_seen = time.monotonic()
        slot.inputs += 1
        slot.pad.set_state(buttons, x, y)

    def status(self) -> dict:
        now = time.monotonic()
        return {
            "capacity": self.capacity,
            "backend": getattr(self.backend, "name", "?"),
            "players": [
                {
                    "player": s.index + 1,
                    "connected": s.connected,
                    "name": s.name,
                    "inputs": s.inputs,
                    "idle_seconds": round(now - s.last_seen, 1),
                    "pad": getattr(s.pad, "describe", lambda: {})(),
                }
                for s in self.slots
            ],
        }

    def close(self) -> None:
        self.backend.close()
