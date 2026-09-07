"""Key assignments used by the xtest backend and by the emulator config.

Design B drives the emulator with synthetic keyboard events instead of virtual
gamepads, for hosts where /dev/uinput has no driver behind it (most containers,
including the Orgo desktop). Two players therefore share one keyboard, so each
player needs a disjoint set of keys and the emulator must bind them per port.

Nobody types these keys, so their physical layout is irrelevant. The only
properties that matter are that every control is covered and that no keysym is
used twice. ``validate()`` enforces exactly that, and the tests run it.

This module deliberately has no X11 dependency: the config generator imports it
on machines with no display, and the tests import it everywhere.
"""

from __future__ import annotations

from padserver.protocol import BUTTON_ORDER

DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
CONTROLS = DIRECTIONS + BUTTON_ORDER

# X11 keysym names, as understood by XStringToKeysym.
PLAYER_KEYS: list[dict[str, str]] = [
    {
        "UP": "w",
        "DOWN": "s",
        "LEFT": "a",
        "RIGHT": "d",
        "LP": "u",
        "HP": "i",
        "LK": "j",
        "HK": "k",
        "A1": "o",
        "A2": "l",
        "START": "1",
        "SELECT": "2",
    },
    {
        "UP": "Up",
        "DOWN": "Down",
        "LEFT": "Left",
        "RIGHT": "Right",
        "LP": "z",
        "HP": "x",
        "LK": "c",
        "HK": "v",
        "A1": "b",
        "A2": "n",
        "START": "3",
        "SELECT": "4",
    },
]

MAX_PLAYERS = len(PLAYER_KEYS)


def keys_for_player(index: int) -> dict[str, str]:
    """Key map for a zero-based player index."""
    if not 0 <= index < MAX_PLAYERS:
        raise ValueError(
            f"no key map for player index {index}; "
            f"the xtest backend supports {MAX_PLAYERS} players"
        )
    return dict(PLAYER_KEYS[index])


def validate() -> None:
    """Raise if the maps are incomplete or overlap. Called by the tests."""
    seen: dict[str, str] = {}
    for index, mapping in enumerate(PLAYER_KEYS):
        missing = [c for c in CONTROLS if c not in mapping]
        if missing:
            raise ValueError(f"player {index + 1} key map is missing {missing}")
        extra = [c for c in mapping if c not in CONTROLS]
        if extra:
            raise ValueError(f"player {index + 1} key map has unknown controls {extra}")
        for control, keysym in mapping.items():
            if keysym in seen:
                raise ValueError(
                    f"keysym {keysym!r} is used twice: "
                    f"{seen[keysym]} and player {index + 1} {control}"
                )
            seen[keysym] = f"player {index + 1} {control}"
