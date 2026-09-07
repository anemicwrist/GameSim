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

if [ ! -w /dev/uinput ]; then
  echo "error: /dev/uinput is not writable by $(id -un). Run scripts/install_deps.sh"
  echo "       then log out and back in. See docs/TROUBLESHOOTING.md."
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
PAD_ARGS=(--backend uinput --port "$PORT" --players "$PLAYERS" --pad-name "$PAD_NAME")
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

echo "==> applying Flycast settings"
"$PYTHON" "$REPO_DIR/scripts/configure_flycast.py" || true

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

echo "==> launching Flycast: $GAME"
if flatpak info org.flycast.Flycast >/dev/null 2>&1; then
  flatpak run org.flycast.Flycast "$GAME"
elif command -v flycast >/dev/null 2>&1; then
  flycast "$GAME"
else
  echo "error: Flycast is not installed. Run scripts/install_flycast.sh"
  exit 1
fi
