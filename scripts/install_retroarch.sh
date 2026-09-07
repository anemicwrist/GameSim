#!/usr/bin/env bash
# Installs RetroArch and the Flycast core.
#
# This is the emulator for the xtest backend. Standalone Flycast cannot split
# one keyboard between two Dreamcast ports (flyinghead/flycast#68), so on hosts
# with no uinput driver we run the same emulator as a libretro core inside
# RetroArch, which does bind keys per player.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GAMES_DIR="${GAMES_DIR:-$HOME/games}"
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

CORE_URL="https://buildbot.libretro.com/nightly/linux/x86_64/latest/flycast_libretro.so.zip"

if ! command -v flatpak >/dev/null 2>&1; then
  echo "==> installing flatpak"
  $SUDO apt-get update -qq
  $SUDO apt-get install -y --no-install-recommends flatpak
fi
if ! command -v unzip >/dev/null 2>&1; then
  $SUDO apt-get install -y --no-install-recommends unzip
fi

echo "==> adding flathub"
flatpak remote-add --if-not-exists --user \
  flathub https://dl.flathub.org/repo/flathub.flatpakrepo

echo "==> installing RetroArch"
flatpak install --user -y flathub org.libretro.RetroArch

echo "==> granting filesystem access"
mkdir -p "$GAMES_DIR"
flatpak override --user --filesystem="$GAMES_DIR" org.libretro.RetroArch
flatpak override --user --share=network org.libretro.RetroArch

CONFIG_DIR="$HOME/.var/app/org.libretro.RetroArch/config/retroarch"
CORE_DIR="$CONFIG_DIR/cores"
mkdir -p "$CORE_DIR"

if [ -f "$CORE_DIR/flycast_libretro.so" ]; then
  echo "==> Flycast core already present"
else
  echo "==> downloading the Flycast core"
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  if curl -fsSL "$CORE_URL" -o "$TMP/core.zip"; then
    unzip -o -q "$TMP/core.zip" -d "$CORE_DIR"
    echo "    installed to $CORE_DIR/flycast_libretro.so"
  else
    echo "!! could not download the core from:"
    echo "!!   $CORE_URL"
    echo "!! Install it from RetroArch instead:"
    echo "!!   Main Menu > Online Updater > Core Downloader > Sega Dreamcast (Flycast)"
  fi
fi

echo
echo "==> writing two-player key bindings"
"$REPO_DIR/scripts/configure_retroarch.py" || \
  python3 "$REPO_DIR/scripts/configure_retroarch.py"

echo
echo "done."
echo "RetroArch config:  $CONFIG_DIR/retroarch.cfg"
echo "Cores:             $CORE_DIR"
echo "BIOS (optional):   $CONFIG_DIR/system/    (dc_boot.bin, dc_flash.bin)"
echo "Next: put your game dump in $GAMES_DIR and run scripts/run.sh"
