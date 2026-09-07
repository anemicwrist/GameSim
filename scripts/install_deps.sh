#!/usr/bin/env bash
# Installs what padserver needs, and works out how input can reach the emulator
# on this host.
#
# There are two ways in. Virtual gamepads through /dev/uinput are the better
# one, but they need a real uinput driver in the kernel, which containers
# usually do not have. Where that is missing we fall back to synthetic keyboard
# events through X11, which needs no kernel device at all. This script finds out
# which applies and installs accordingly, rather than assuming.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

echo "==> installing system packages"
$SUDO apt-get update -qq
$SUDO apt-get install -y --no-install-recommends \
  python3 python3-venv python3-pip \
  evtest mesa-utils x11-utils curl ca-certificates

echo "==> creating the python environment"
python3 -m venv "$REPO_DIR/.venv"
PYTHON="$REPO_DIR/.venv/bin/python"
"$REPO_DIR/.venv/bin/pip" install --quiet --upgrade pip
"$REPO_DIR/.venv/bin/pip" install --quiet -e "$REPO_DIR"

echo
echo "==> can this host create virtual gamepads?"
# Try to make the node first: it is an ordinary character device, so root can
# create one even where there is no `modprobe` and no /lib/modules. That alone
# proves nothing, which is why uinput_check.py goes on to open it.
set +e
"$PYTHON" "$REPO_DIR/scripts/uinput_check.py"
VERDICT_CODE=$?
set -e

# 3 means the driver is there but access was refused, which group membership
# often fixes. Worth one attempt before falling back.
if [ "$VERDICT_CODE" -eq 3 ]; then
  echo
  echo "==> access was refused; granting this user access to /dev/uinput"
  $SUDO groupadd -f input
  $SUDO usermod -aG input "$(id -un)"
  printf 'KERNEL=="uinput", MODE="0660", GROUP="input", OPTIONS+="static_node=uinput"\n' \
    | $SUDO tee /etc/udev/rules.d/99-padserver-uinput.rules >/dev/null
  $SUDO udevadm control --reload-rules 2>/dev/null || true
  $SUDO udevadm trigger --name-match=uinput 2>/dev/null || true
  $SUDO chgrp input /dev/uinput 2>/dev/null || true
  $SUDO chmod 660 /dev/uinput 2>/dev/null || true
  echo "    (a new login may be needed before the group takes effect)"
fi

if [ "$VERDICT_CODE" -eq 0 ]; then
  BACKEND=uinput
else
  BACKEND=xtest
fi

echo
echo "==> installing the '$BACKEND' backend's dependencies"
if [ "$BACKEND" = uinput ]; then
  # evdev builds a C extension, so it needs headers and a compiler.
  $SUDO apt-get install -y --no-install-recommends build-essential python3-dev
  "$REPO_DIR/.venv/bin/pip" install --quiet -e "$REPO_DIR[uinput]"
  echo uinput | $SUDO tee /etc/modules-load.d/uinput.conf >/dev/null
else
  "$REPO_DIR/.venv/bin/pip" install --quiet -e "$REPO_DIR[xtest]"
fi

echo
echo "done. This host will use the '$BACKEND' backend."
if [ "$BACKEND" = uinput ]; then
  echo "Two virtual Xbox 360 pads will appear when you start the server."
  if [ ! -w /dev/uinput ]; then
    echo
    echo "Note: /dev/uinput is not writable by this shell yet. Log out and back"
    echo "in (or run 'newgrp input'), then check:  test -w /dev/uinput && echo ok"
  fi
else
  echo "Both players share one keyboard, and the emulator gets per-player key"
  echo "bindings generated from padserver/keymap.py. This needs the graphical"
  echo "session, so run scripts/run.sh from the desktop's terminal."
fi
echo "Next: scripts/install_flycast.sh"
