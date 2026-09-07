#!/usr/bin/env bash
# Fallback to Tailscale: exposes the pad server on a temporary public HTTPS URL
# via Cloudflare. Use PADSERVER_TOKEN so a stranger who guesses the URL cannot
# take a player slot.
set -euo pipefail
PORT="${PORT:-8080}"
SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

if ! command -v cloudflared >/dev/null 2>&1; then
  echo "==> installing cloudflared"
  ARCH="$(dpkg --print-architecture)"
  curl -fsSL -o /tmp/cloudflared.deb \
    "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-${ARCH}.deb"
  $SUDO dpkg -i /tmp/cloudflared.deb
fi

echo "==> opening a tunnel to http://localhost:$PORT"
echo "    Give the phones the https://<something>.trycloudflare.com URL below,"
echo "    with ?k=<your token> on the end if you started padserver with one."
exec cloudflared tunnel --url "http://localhost:$PORT"
