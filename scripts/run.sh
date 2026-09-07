#!/usr/bin/env bash
# Starts the pad server, waits for both virtual gamepads to exist, then launches
# Flycast with the game. Order matters: the pads must be present before Flycast
# opens SDL, otherwise the joystick instance ids that pin each pad to a
# Dreamcast port come out differently.
#
#   scripts/run.sh                      # first game file found under ~/games
#   scripts/run.sh ~/games/mvc2/mvc2.gdi
#   PORT=9000 PADSERVER_TOKEN=hunter2 scripts/run.sh
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GAMES_DIR="${GAMES_DIR:-$HOME/games}"
PORT="${PORT:-8080}"
TOKEN="${PADSERVER_TOKEN:-}"
PAD_NAME="${PAD_NAME:-Microsoft X-Box 360 pad}"
PLAYERS="${PLAYERS:-2}"

PYTHON="$REPO_DIR/.venv/bin/python"
[ -x "$PYTHON" ] || PYTHON="$(command -v python3)"

GAME="${1:-${GAME:-}}"
if [ -z "$GAME" ]; then
  GAME="$(find "$GAMES_DIR" -maxdepth 3 -type f \
    \( -iname '*.gdi' -o -iname '*.chd' -o -iname '*.cdi' -o -iname '*.cue' -o -iname '*.m3u' \) \
    2>/dev/null | sort | head -1)"
fi
if [ -z "$GAME" ] || [ ! -f "$GAME" ]; then
  echo "No game file found. Put your own Marvel vs Capcom 2 dump (.gdi/.chd/.cdi)"
  echo "under $GAMES_DIR, or pass the path: scripts/run.sh /path/to/mvc2.gdi"
  echo "See docs/GAME_FILES.md."
  exit 1
fi

if [ -z "${DISPLAY:-}${WAYLAND_DISPLAY:-}" ]; then
  echo "warning: no DISPLAY set. Flycast needs the graphical desktop session."
  echo "         On Orgo, run this from the desktop's terminal, or export DISPLAY=:0"
fi

# Which way input reaches the emulator. Virtual gamepads are the better option,
# but they need a real uinput driver, which most containers do not have. The
# check opens the device rather than trusting that the node exists, because
# `mknod` will happily create a node with nothing behind it.
BACKEND="${PADSERVER_BACKEND:-auto}"
if [ "$BACKEND" = auto ]; then
  VERDICT="$("$PYTHON" "$REPO_DIR/scripts/uinput_check.py" --quiet 2>/dev/null || true)"
  case "$VERDICT" in
    ok) BACKEND=uinput ;;
    *)  BACKEND=xtest ;;
  esac
  echo "==> input backend: $BACKEND (uinput probe said: ${VERDICT:-unavailable})"
else
  echo "==> input backend: $BACKEND (forced by PADSERVER_BACKEND)"
fi

if [ "$BACKEND" = xtest ] && [ -z "${DISPLAY:-}" ]; then
  echo "error: the xtest backend needs an X display, but DISPLAY is unset."
  echo "       Run this from the desktop session, or export DISPLAY=:0"
  exit 1
fi

PAD_PID=""
cleanup() {
  if [ -n "$PAD_PID" ] && kill -0 "$PAD_PID" 2>/dev/null; then
    kill "$PAD_PID" 2>/dev/null || true
    wait "$PAD_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM

echo "==> starting padserver on port $PORT"
PAD_ARGS=(--backend "$BACKEND" --port "$PORT" --players "$PLAYERS" --pad-name "$PAD_NAME")
[ -n "$TOKEN" ] && PAD_ARGS+=(--token "$TOKEN")
"$PYTHON" -m padserver "${PAD_ARGS[@]}" &
PAD_PID=$!

for _ in $(seq 1 50); do
  curl -sf "http://127.0.0.1:$PORT/health" >/dev/null 2>&1 && break
  sleep 0.2
done
if ! curl -sf "http://127.0.0.1:$PORT/health" >/dev/null 2>&1; then
  echo "error: padserver did not come up on port $PORT"
  exit 1
fi

if [ "$BACKEND" = uinput ]; then
  echo "==> waiting for $PLAYERS virtual pads named '$PAD_NAME'"
  for _ in $(seq 1 50); do
    found=$(grep -lx "$PAD_NAME" /sys/class/input/input*/name 2>/dev/null | wc -l)
    [ "$found" -ge "$PLAYERS" ] && break
    sleep 0.2
  done
  found=$(grep -lx "$PAD_NAME" /sys/class/input/input*/name 2>/dev/null | wc -l)
  if [ "$found" -lt "$PLAYERS" ]; then
    echo "error: only $found of $PLAYERS pads appeared under /sys/class/input"
    exit 1
  fi
  echo "    $found pads ready"
fi

if [ "$BACKEND" = uinput ]; then
  echo "==> applying Flycast settings"
  "$PYTHON" "$REPO_DIR/scripts/configure_flycast.py" || true
else
  echo "==> applying RetroArch settings and two-player key bindings"
  "$PYTHON" "$REPO_DIR/scripts/configure_retroarch.py" || true
fi

echo
echo "Phones open:"
SUFFIX=""
[ -n "$TOKEN" ] && SUFFIX="?k=$TOKEN"
if command -v tailscale >/dev/null 2>&1; then
  tailscale ip -4 2>/dev/null | sed "s|^|  http://|; s|\$|:$PORT/$SUFFIX|"
fi
ip -4 addr show scope global 2>/dev/null | grep -oP '(?<=inet )[\d.]+' \
  | sed "s|^|  http://|; s|\$|:$PORT/$SUFFIX|"
echo

if [ "$BACKEND" = uinput ]; then
  echo "==> launching Flycast: $GAME"
  if flatpak info org.flycast.Flycast >/dev/null 2>&1; then
    flatpak run org.flycast.Flycast "$GAME"
  elif command -v flycast >/dev/null 2>&1; then
    flycast "$GAME"
  else
    echo "error: Flycast is not installed. Run scripts/install_flycast.sh"
    exit 1
  fi
else
  # The Flycast core inside RetroArch, because it can bind two players to one
  # keyboard where standalone Flycast cannot.
  CORE="${CORE:-}"
  if [ -z "$CORE" ]; then
    for candidate in \
      "$HOME/.var/app/org.libretro.RetroArch/config/retroarch/cores/flycast_libretro.so" \
      "$HOME/.config/retroarch/cores/flycast_libretro.so" \
      /usr/lib/libretro/flycast_libretro.so; do
      [ -f "$candidate" ] && CORE="$candidate" && break
    done
  fi
  if [ -z "$CORE" ]; then
    echo "error: the Flycast core was not found. Run scripts/install_retroarch.sh"
    exit 1
  fi

  echo "==> launching RetroArch with the Flycast core"
  echo "    core: $CORE"
  echo "    game: $GAME"
  if flatpak info org.libretro.RetroArch >/dev/null 2>&1; then
    flatpak run org.libretro.RetroArch -L "$CORE" -f "$GAME"
  elif command -v retroarch >/dev/null 2>&1; then
    retroarch -L "$CORE" -f "$GAME"
  else
    echo "error: RetroArch is not installed. Run scripts/install_retroarch.sh"
    exit 1
  fi
fi
