"""Wire protocol between the phone page and the pad server.

Messages are small JSON objects. The button bitmask defined here is the single
source of truth; ``padserver/static/pad.js`` mirrors these bit positions.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

# Bit positions in the "b" field of an input message. MvC2 uses six attack
# buttons plus start/select. Keep these in sync with BITS in pad.js.
BUTTON_BITS = {
    "LP": 0,  # light punch   -> Dreamcast X
    "HP": 1,  # heavy punch   -> Dreamcast Y
    "LK": 2,  # light kick    -> Dreamcast A
    "HK": 3,  # heavy kick    -> Dreamcast B
    "A1": 4,  # assist 1      -> Dreamcast L trigger
    "A2": 5,  # assist 2      -> Dreamcast R trigger
    "START": 6,
    "SELECT": 7,
}

BUTTON_ORDER = ["LP", "HP", "LK", "HK", "A1", "A2", "START", "SELECT"]
BUTTON_MASK = (1 << len(BUTTON_ORDER)) - 1

MAX_MESSAGE_BYTES = 512


class ProtocolError(ValueError):
    """Raised when a client sends something that is not a valid message."""


@dataclass(frozen=True)
class Hello:
    token: str
    name: str


@dataclass(frozen=True)
class Input:
    buttons: int
    x: int
    y: int

    def pressed(self) -> list:
        return [n for n in BUTTON_ORDER if self.buttons & (1 << BUTTON_BITS[n])]


@dataclass(frozen=True)
class Ping:
    ts: float


Message = Any  # Hello | Input | Ping


def _clamp_axis(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ProtocolError(f"{field} must be a number")
    v = int(value)
    if v < -1:
        return -1
    if v > 1:
        return 1
    return v


def parse(raw: str) -> Message:
    """Parse one client message. Raises ProtocolError on anything unexpected."""
    if len(raw) > MAX_MESSAGE_BYTES:
        raise ProtocolError("message too large")
    try:
        obj = json.loads(raw)
    except (ValueError, TypeError) as exc:
        raise ProtocolError("not valid json") from exc
    if not isinstance(obj, dict):
        raise ProtocolError("message must be an object")

    kind = obj.get("t")
    if kind == "hello":
        token = obj.get("token")
        if not isinstance(token, str) or not (1 <= len(token) <= 64):
            raise ProtocolError("hello needs a token of 1-64 chars")
        name = obj.get("name", "")
        if not isinstance(name, str):
            raise ProtocolError("name must be a string")
        return Hello(token=token, name=name[:32])

    if kind == "in":
        buttons = obj.get("b", 0)
        if isinstance(buttons, bool) or not isinstance(buttons, int):
            raise ProtocolError("b must be an integer")
        if buttons < 0:
            raise ProtocolError("b must not be negative")
        return Input(
            buttons=buttons & BUTTON_MASK,
            x=_clamp_axis(obj.get("x", 0), "x"),
            y=_clamp_axis(obj.get("y", 0), "y"),
        )

    if kind == "ping":
        ts = obj.get("ts", 0)
        if isinstance(ts, bool) or not isinstance(ts, (int, float)):
            raise ProtocolError("ts must be a number")
        return Ping(ts=float(ts))

    raise ProtocolError(f"unknown message type: {kind!r}")


def slot_message(player: int, buttons: list | None = None) -> str:
    return json.dumps({"t": "slot", "player": player, "buttons": buttons or BUTTON_ORDER})


def full_message(capacity: int) -> str:
    return json.dumps({"t": "full", "capacity": capacity})


def pong_message(ts: float) -> str:
    return json.dumps({"t": "pong", "ts": ts})


def error_message(reason: str) -> str:
    return json.dumps({"t": "error", "reason": reason})
