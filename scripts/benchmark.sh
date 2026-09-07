#!/usr/bin/env bash
# Measures whether this host can render the game fast enough to be worth playing.
#
# This is the go/no-go check. On a machine with no GPU, everything is drawn by
# the CPU through llvmpipe, and Marvel vs Capcom 2 is not a light 2D game: it
# runs on Dreamcast/NAOMI hardware and pushes a lot of sprites and a 3D
# background. Rather than build the whole system and discover at the TV that it
# runs at 12 fps, measure first.
#
#   bash scripts/benchmark.sh            # graphics proxy, needs no game file
#   bash scripts/benchmark.sh --help     # how to run the real test
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
  sed -n '2,14p' "$0" | sed 's/^# \{0,1\}//'
  exit 0
fi

if [ -z "${DISPLAY:-}" ]; then
  echo "error: no DISPLAY. Run this from the desktop session's terminal."
  exit 1
fi

echo "=== what is drawing the pixels ==="
if command -v glxinfo >/dev/null 2>&1; then
  glxinfo -B 2>/dev/null | grep -Ei "device|renderer|opengl version" | head -4
else
  echo "glxinfo not installed; run scripts/install_deps.sh first"
fi

RENDERER="$(glxinfo -B 2>/dev/null | grep -i 'device' | head -1 || true)"
case "$RENDERER" in
  *llvmpipe*|*softpipe*|*swrast*)
    echo
    echo ">> Software rendering. There is no GPU here, so the CPU draws every"
    echo ">> frame. Expect this to be the limiting factor."
    ;;
esac

echo
echo "=== OpenGL throughput (glmark2) ==="
if ! command -v glmark2 >/dev/null 2>&1; then
  echo "installing glmark2..."
  $SUDO apt-get update -qq
  $SUDO apt-get install -y --no-install-recommends glmark2 >/dev/null 2>&1 || {
    echo "could not install glmark2; skipping the proxy benchmark"
    exit 0
  }
fi

# A small, fixed subset at the resolution we actually play at. The absolute
# number matters less than its order of magnitude.
glmark2 --size 1280x720 \
  -b build -b texture -b shading -b bump -b effect2d \
  2>/dev/null | tee /tmp/glmark2.out | tail -20

SCORE="$(grep -i '^glmark2 Score' /tmp/glmark2.out | grep -oE '[0-9]+' | head -1 || true)"

echo
echo "=== what that means ==="
if [ -z "$SCORE" ]; then
  echo "No score was produced. Read the output above for errors."
  exit 0
fi
echo "glmark2 score: $SCORE"
echo
if [ "$SCORE" -lt 100 ]; then
  echo ">> Very low. A Dreamcast emulator is unlikely to be playable here."
  echo ">> Expect to fall back to running the emulator on your own machine."
elif [ "$SCORE" -lt 300 ]; then
  echo ">> Low. Marvel vs Capcom 2 may run, but probably below 60 fps."
  echo ">> Worth measuring for real before building anything else on it."
else
  echo ">> Reasonable for software rendering. Worth measuring for real."
fi

cat <<'EOF'

=== the real test ===
glmark2 only says how fast this machine draws triangles. The number that
decides the project is the frame rate of an actual match, so measure that as
soon as you have the game file:

  bash scripts/run.sh /path/to/mvc2.gdi

The frame counter is already switched on in the generated config. Start a
versus match with two characters on screen, let a few seconds of real fighting
happen, and read the counter.

  55-60 fps   full speed; the plan works as written
  40-55 fps   noticeably slow but playable for casual matches
  30-40 fps   sluggish; fighting-game timing will feel wrong
  under 30    not worth playing; run the emulator on your own machine instead

Marvel vs Capcom 2 runs at 60 fps natively, so anything under that is the
emulator failing to keep up, not the game being designed that way.
EOF
