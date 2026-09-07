#!/usr/bin/env bash
# Thin wrapper so every step in the README is a shell script.
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$REPO_DIR/scripts/configure_flycast.py" "$@"
