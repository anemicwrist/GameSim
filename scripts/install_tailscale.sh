#!/usr/bin/env bash
# Puts this machine on your private Tailscale network so the phones can reach
# it directly, without exposing anything to the public internet.
set -euo pipefail
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

if ! command -v tailscale >/dev/null 2>&1; then
  echo "==> installing tailscale"
  curl -fsSL https://tailscale.com/install.sh | $SUDO sh
fi

echo "==> bringing tailscale up"
echo "    A login URL will be printed. Open it, sign in, and approve this machine."
$SUDO tailscale up --hostname=gamesim

echo
echo "This machine's tailscale address:"
tailscale ip -4
echo
echo "Install the Tailscale app on both phones, sign in with the same account,"
echo "then open  http://<the address above>:8080/  in Chrome."
