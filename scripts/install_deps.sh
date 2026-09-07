#!/usr/bin/env bash
# Installs what padserver needs and makes /dev/uinput usable without sudo.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

echo "==> installing system packages"
$SUDO apt-get update -qq
$SUDO apt-get install -y --no-install-recommends \
  python3 python3-venv python3-pip \
  evtest mesa-utils curl ca-certificates

echo "==> loading the uinput kernel module"
$SUDO modprobe uinput || true
echo uinput | $SUDO tee /etc/modules-load.d/uinput.conf >/dev/null

if [ ! -e /dev/uinput ]; then
  echo
  echo "!! /dev/uinput does not exist on this kernel."
  echo "!! The virtual gamepads cannot be created here. See docs/TROUBLESHOOTING.md"
  echo "!! ('no /dev/uinput') before going further."
  exit 1
fi

echo "==> granting access to /dev/uinput"
$SUDO groupadd -f input
$SUDO usermod -aG input "$(id -un)"
printf 'KERNEL=="uinput", MODE="0660", GROUP="input", OPTIONS+="static_node=uinput"\n' \
  | $SUDO tee /etc/udev/rules.d/99-padserver-uinput.rules >/dev/null
$SUDO udevadm control --reload-rules 2>/dev/null || true
$SUDO udevadm trigger --name-match=uinput 2>/dev/null || true
$SUDO chgrp input /dev/uinput 2>/dev/null || true
$SUDO chmod 660 /dev/uinput 2>/dev/null || true

echo "==> creating the python environment"
python3 -m venv "$REPO_DIR/.venv"
"$REPO_DIR/.venv/bin/pip" install --quiet --upgrade pip
"$REPO_DIR/.venv/bin/pip" install --quiet -e "$REPO_DIR[uinput]"

echo
echo "done."
if [ -w /dev/uinput ]; then
  echo "/dev/uinput is writable now. Next: scripts/install_flycast.sh"
else
  echo "You were added to the 'input' group but this shell predates it."
  echo "Log out and back in (or run 'newgrp input'), then check:  test -w /dev/uinput && echo ok"
fi
