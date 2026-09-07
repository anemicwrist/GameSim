#!/usr/bin/env bash
# Reports whether this machine can host the emulator and the virtual gamepads.
# Run it on the Orgo computer and paste the whole output back.
set -u

line() { printf '\n=== %s ===\n' "$1"; }
have() { command -v "$1" >/dev/null 2>&1; }

line "os"
uname -a
[ -r /etc/os-release ] && (. /etc/os-release && echo "distro: $PRETTY_NAME")

line "cpu / memory / disk"
echo "cpus: $(nproc 2>/dev/null || echo '?')"
free -h 2>/dev/null | sed -n '1,2p'
df -h / 2>/dev/null | sed -n '1,2p'

line "display server"
echo "DISPLAY=${DISPLAY:-<unset>}  WAYLAND_DISPLAY=${WAYLAND_DISPLAY:-<unset>}  XDG_SESSION_TYPE=${XDG_SESSION_TYPE:-<unset>}"
have xrandr && xrandr 2>/dev/null | sed -n '1,4p'

line "input backend"
# Whether /dev/uinput exists says nothing useful: it is an ordinary character
# device that `mknod` can create anywhere, driver or not. The only real test is
# to open it and create a device, which is what this does. It reports "nodriver"
# on hosts that then need the xtest backend instead.
[ -e /dev/uinput ] && ls -l /dev/uinput || echo "/dev/uinput: absent"
if [ -x "$(dirname "$0")/uinput_check.py" ] || [ -f "$(dirname "$0")/uinput_check.py" ]; then
  python3 "$(dirname "$0")/uinput_check.py" --no-create || true
else
  echo "uinput_check.py not found next to this script"
fi
echo "groups: $(id -nG)"

line "opengl (needed by the emulator)"
if have glxinfo; then
  glxinfo -B 2>/dev/null | grep -Ei "vendor|renderer|version|device" | head -8
else
  echo "glxinfo not installed (apt-get install -y mesa-utils)"
fi
if [ -e /dev/dri ]; then ls -l /dev/dri; else echo "no /dev/dri (software rendering only)"; fi

line "audio"
if have pactl; then pactl info 2>/dev/null | sed -n '1,4p'; else echo "pulseaudio/pipewire client tools not installed"; fi

line "toolchain"
for c in python3 pip3 flatpak curl git; do
  if have "$c"; then
    printf '%-8s %s\n' "$c" "$("$c" --version 2>&1 | head -1)"
  else
    printf '%-8s MISSING\n' "$c"
  fi
done
python3 -c "import evdev; print('python evdev:', evdev.__version__)" 2>/dev/null || echo "python evdev: not installed"
python3 -c "import aiohttp; print('python aiohttp:', aiohttp.__version__)" 2>/dev/null || echo "python aiohttp: not installed"

line "network"
ip -4 addr show scope global 2>/dev/null | grep -oP '(?<=inet )[\d.]+' | sed 's/^/local ip: /'
if have tailscale; then tailscale ip -4 2>/dev/null | sed 's/^/tailscale ip: /'; else echo "tailscale: not installed"; fi

printf '\nprobe done\n'
