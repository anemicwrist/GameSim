#!/usr/bin/env python3
"""Merge flycast/emu.cfg.template into the live Flycast configuration.

Flycast rewrites emu.cfg whenever it exits, so this merges rather than
overwrites: keys in the template win, every other key already present is kept.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "flycast" / "emu.cfg.template"

CONFIG_DIRS = [
    Path.home() / ".var/app/org.flycast.Flycast/config/flycast",  # flatpak
    Path.home() / ".config/flycast",  # native build or AppImage
]


def parse_ini(text: str):
    """Ordered section -> {key: value}. Comments and blank lines are dropped."""
    sections = {}
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith((";", "#")):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            sections.setdefault(current, {})
            continue
        if "=" in line and current is not None:
            key, _, value = line.partition("=")
            sections[current][key.strip()] = value.strip()
    return sections


def render_ini(sections) -> str:
    out = []
    for name, entries in sections.items():
        out.append(f"[{name}]")
        for key, value in entries.items():
            out.append(f"{key} = {value}")
        out.append("")
    return "\n".join(out)


def pick_config_dir(explicit) -> Path:
    if explicit:
        return Path(explicit).expanduser()
    for candidate in CONFIG_DIRS:
        if candidate.exists():
            return candidate
    # Nothing yet: Flycast has never run. Prefer the flatpak location if the
    # flatpak app data directory exists, otherwise the native one.
    flatpak_root = Path.home() / ".var/app/org.flycast.Flycast"
    return CONFIG_DIRS[0] if flatpak_root.exists() else CONFIG_DIRS[1]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config-dir", help="Flycast config directory (autodetected)")
    ap.add_argument("--template", default=str(TEMPLATE))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    template = parse_ini(Path(args.template).read_text())
    config_dir = pick_config_dir(args.config_dir)
    config_dir.mkdir(parents=True, exist_ok=True)
    target = config_dir / "emu.cfg"

    existing = parse_ini(target.read_text()) if target.exists() else {}

    merged = {name: dict(entries) for name, entries in existing.items()}
    changes = []
    for name, entries in template.items():
        section = merged.setdefault(name, {})
        for key, value in entries.items():
            if section.get(key) != value:
                changes.append(f"[{name}] {key}: {section.get(key, '<unset>')} -> {value}")
            section[key] = value

    print(f"config file: {target}")
    if not changes:
        print("already up to date")
        return 0
    for change in changes:
        print("  " + change)
    if args.dry_run:
        print("(dry run, nothing written)")
        return 0

    if target.exists():
        backup = target.with_suffix(".cfg.bak")
        shutil.copy2(target, backup)
        print(f"backup: {backup}")
    target.write_text(render_ini(merged))
    print(f"wrote {len(changes)} change(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
