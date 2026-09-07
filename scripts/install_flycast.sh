#!/usr/bin/env bash
# Installs Flycast from Flathub and gives it access to the virtual gamepads.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GAMES_DIR="${GAMES_DIR:-$HOME/games}"
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

if ! command -v flatpak >/dev/null 2>&1; then
  echo "==> installing flatpak"
  $SUDO apt-get update -qq
  $SUDO apt-get install -y --no-install-recommends flatpak
fi

echo "==> adding flathub"
flatpak remote-add --if-not-exists --user \
  flathub https://dl.flathub.org/repo/flathub.flatpakrepo

echo "==> installing Flycast"
flatpak install --user -y flathub org.flycast.Flycast

echo "==> granting device and filesystem access"
mkdir -p "$GAMES_DIR"
# --device=all lets the sandbox read /dev/input/event*, which is where the
# virtual pads appear. Without it Flycast sees no controllers at all.
flatpak override --user --device=all org.flycast.Flycast
flatpak override --user --filesystem="$GAMES_DIR" org.flycast.Flycast
flatpak override --user --share=network org.flycast.Flycast

echo
echo "done. Flycast config lives in:"
echo "  $HOME/.var/app/org.flycast.Flycast/config/flycast/"
echo "Dreamcast BIOS files (optional) go in:"
echo "  $HOME/.var/app/org.flycast.Flycast/data/flycast/"
echo "Next: put your game dump in $GAMES_DIR and run scripts/configure_flycast.sh"
echo "(repo: $REPO_DIR)"
