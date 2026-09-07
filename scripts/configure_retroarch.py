#!/usr/bin/env python3
"""Generate RetroArch key bindings for two players from padserver/keymap.py.

Used with the xtest backend. Standalone Flycast cannot split one keyboard
between two Dreamcast ports (flyinghead/flycast#68), so on hosts with no uinput
driver we run the Flycast *core* inside RetroArch instead, which binds keys per
player.

Bindings are derived from padserver.keymap, the same module the xtest backend
presses keys from, so the emulator and the pad server cannot disagree about
which key means what.

RetroArch rewrites retroarch.cfg on exit, so this merges rather than
overwrites: the keys below win, everything else already present is kept.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from padserver.keymap import MAX_PLAYERS, keys_for_player  # noqa: E402

CONFIG_DIRS = [
    Path.home() / ".var/app/org.libretro.RetroArch/config/retroarch",  # flatpak
    Path.home() / ".config/retroarch",  # native
]

# RetroPad is laid out like a SNES pad and the Flycast core maps it onto the
# Dreamcast diamond by position, not by letter (docs.libretro.com/library/flycast):
#
#     RetroPad          Dreamcast
#        X                  Y
#      Y   A     ->       X   B
#        B                  A
#
# So the Dreamcast button we want decides which RetroPad button to bind, and the
# letters deliberately do not match.
CONTROL_TO_RETROPAD = {
    "LP": "y",  # light punch -> Dreamcast X
    "HP": "x",  # heavy punch -> Dreamcast Y
    "LK": "b",  # light kick  -> Dreamcast A
    "HK": "a",  # heavy kick  -> Dreamcast B
    "A1": "l",  # assist 1    -> L trigger
    "A2": "r",  # assist 2    -> R trigger
    "START": "start",
    "SELECT": "select",
    "UP": "up",
    "DOWN": "down",
    "LEFT": "left",
    "RIGHT": "right",
}

# X11 keysym names -> RetroArch key names (docs.libretro.com/guides/input-and-controls).
_ARROWS = {"Up": "up", "Down": "down", "Left": "left", "Right": "right"}
_NAMED = {
    "Return": "enter",
    "space": "space",
    "BackSpace": "backspace",
    "Tab": "tab",
    "Escape": "escape",
}


def retroarch_key(keysym: str) -> str:
    """Translate one X11 keysym name into RetroArch's name for the same key.

    Raises on anything unrecognised: a silently wrong name produces a binding
    that does nothing, which is painful to diagnose with a phone in each hand.
    """
    if keysym in _ARROWS:
        return _ARROWS[keysym]
    if keysym in _NAMED:
        return _NAMED[keysym]
    if len(keysym) == 1 and keysym.isalpha():
        return keysym.lower()
    if len(keysym) == 1 and keysym.isdigit():
        return f"num{keysym}"
    raise ValueError(
        f"no RetroArch key name known for the keysym {keysym!r}; "
        "add it to _NAMED in scripts/configure_retroarch.py"
    )


def player_bindings(index: int) -> dict[str, str]:
    """input_playerN_* bindings for a zero-based player index."""
    player = index + 1
    out = {}
    for control, keysym in keys_for_player(index).items():
        out[f"input_player{player}_{CONTROL_TO_RETROPAD[control]}"] = retroarch_key(keysym)
    return out


def build_settings(players: int = MAX_PLAYERS) -> dict[str, str]:
    settings: dict[str, str] = {
        # Both ports hold a controller, so player 2 exists as soon as it boots.
        "input_max_users": str(players),
        "video_fullscreen": "true",
        "video_windowed_fullscreen": "true",
        # Software rendering: never wait on a vblank we cannot hit anyway, and
        # do not let RetroArch drop to a slower path trying to keep in step.
        "video_vsync": "false",
        "video_threaded": "true",
        "audio_sync": "false",
        # A frame counter is the whole point of the performance gate.
        "fps_show": "true",
        "video_font_enable": "true",
    }
    for index in range(players):
        settings.update(player_bindings(index))

    # Player 1's MENU button opens the RetroArch menu, matching what the phone
    # page labels it. Escape still quits.
    menu_key = retroarch_key(keys_for_player(0)["SELECT"])
    settings["input_menu_toggle"] = menu_key
    return settings


def parse_cfg(text: str) -> dict[str, str]:
    """RetroArch's config is flat `key = "value"` lines."""
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if not sep:
            continue
        out[key.strip()] = value.strip().strip('"')
    return out


def render_cfg(entries: dict[str, str]) -> str:
    return "\n".join(f'{key} = "{value}"' for key, value in sorted(entries.items())) + "\n"


def pick_config_dir(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser()
    for candidate in CONFIG_DIRS:
        if candidate.exists():
            return candidate
    flatpak_root = Path.home() / ".var/app/org.libretro.RetroArch"
    return CONFIG_DIRS[0] if flatpak_root.exists() else CONFIG_DIRS[1]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--config-dir", help="RetroArch config directory (autodetected)")
    ap.add_argument("--players", type=int, default=MAX_PLAYERS)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    wanted = build_settings(args.players)

    if args.dry_run:
        print(render_cfg(wanted), end="")
        return 0

    config_dir = pick_config_dir(args.config_dir)
    config_dir.mkdir(parents=True, exist_ok=True)
    target = config_dir / "retroarch.cfg"

    existing = parse_cfg(target.read_text()) if target.exists() else {}
    changes = [k for k, v in wanted.items() if existing.get(k) != v]

    if not changes:
        print(f"retroarch.cfg already correct ({target})")
        return 0

    if target.exists():
        shutil.copy2(target, target.with_suffix(".cfg.bak"))

    merged = dict(existing)
    merged.update(wanted)
    target.write_text(render_cfg(merged))

    print(f"updated {target} ({len(changes)} settings)")
    for key in sorted(changes):
        print(f"  {key} = {wanted[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
