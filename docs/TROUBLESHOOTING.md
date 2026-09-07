# Troubleshooting

Work down from the input side. `http://127.0.0.1:8080/status` on the VM answers
most questions on its own: it shows each slot, whether a phone is connected, how
many input messages it has sent, and the live button state of its pad.

## The phone shows "connecting" or "reconnecting" forever

The phone cannot reach the server.

- On Tailscale: is the VPN switch on in the Tailscale app? Does
  `tailscale status` on the VM list the phone?
- Is the pad server actually running? `curl -sf http://127.0.0.1:8080/health`
  on the VM should print `{"ok": true}`.
- Using a token? The URL needs `?k=<token>` and the page returns 403 without it.
- On a Cloudflare tunnel: the URL changes every time `tunnel.sh` restarts.

## The phone says "game full"

Both slots are held. A phone that lost its connection frees its slot as soon as
the socket closes, which can take a few seconds. `status` shows who holds what.
Reloading on the original phone reclaims its own slot, because the page
remembers a token in `localStorage` and the server hands a returning token back
its previous player number.

## no /dev/uinput

```bash
sudo modprobe uinput
ls -l /dev/uinput
```

If the module loads, `scripts/install_deps.sh` makes it permanently available
and writable by the `input` group. You must log out and back in for the group to
apply; `newgrp input` works in the current shell.

If `modprobe` fails and `scripts/probe.sh` reports no `uinput.ko` in the
kernel's modules, this kernel cannot create virtual input devices at all. The
approach does not work on that machine. Plan B in `docs/ARCHITECTURE.md` runs
the same server on your Windows PC instead.

## The pads exist but Flycast shows no controllers

```bash
grep -l "X-Box" /sys/class/input/input*/name    # should list two
sudo evtest                                     # should offer both by name
```

If they are there and Flycast still sees nothing, it is the flatpak sandbox.
`scripts/install_flycast.sh` grants `--device=all`, which is what lets Flycast
read `/dev/input/event*`. Check it stuck:

```bash
flatpak override --user --show org.flycast.Flycast
```

## Buttons work but they are the wrong buttons

The automatic mapping depends on SDL recognising the pad as an Xbox 360
controller. If something in that chain differs on your machine, remap once by
hand: Flycast's Settings, then Controls, then Map on the pad. Flycast saves the
result to

```
~/.var/app/org.flycast.Flycast/config/flycast/mappings/
```

and reuses it from then on. The layout you want for Marvel vs Capcom 2:

```
X = LP    Y = HP    L = A1
A = LK    B = HK    R = A2
```

## Player 2 does not exist in the game

The second Dreamcast port has to hold a controller before the game boots.
`scripts/configure_flycast.py` sets `device2 = 0` for that. Flycast rewrites
`emu.cfg` when it exits, so if you changed settings in the Flycast menu, run the
script again and restart. Check the live file:

```bash
grep -A4 '\[input\]' ~/.var/app/org.flycast.Flycast/config/flycast/emu.cfg
```

## Both phones control the same character

Both pads landed on the same Dreamcast port. The port assignment keys off SDL
joystick instance ids, which are only predictable if both pads exist before
Flycast starts. Always launch through `scripts/run.sh`, which waits for both
device nodes first. If you started Flycast by hand, quit it and use the script.

## The game runs slowly on the VM

Check what `scripts/probe.sh` said about OpenGL. `llvmpipe` means software
rendering on the CPU.

- Keep `rend.Resolution = 480` in `flycast/emu.cfg.template`. Raising it
  multiplies the pixel cost.
- Keep `rend.ThreadedRendering = yes`.
- `aica.DSPEnabled = no` is already set; the DSP is expensive and this game does
  not need it.
- Move to a larger Orgo tier, ideally one with a GPU.

Distinguish a slow emulator from a slow picture: if the audio-free game feels
sluggish in its own timing (the character select timer counts down slowly), the
emulator is slow. If the game is at speed but the image is jerky, that is VNC.

## The video is too choppy

VNC is the bottleneck, not the emulator. The real fix is a video stream built
for games. On the VM install Sunshine, on the Windows PC install Moonlight, and
connect them over Tailscale at 720p60. That carries audio too, which VNC does
not.

It costs CPU on the VM for the H.264 encode, which competes with Flycast. On a
4 vCPU box without a GPU it can make things worse rather than better. Try it
only if you have the GPU tier, and keep the bitrate modest.

## Latency feels bad

Read the budget in `docs/ARCHITECTURE.md`. The two largest terms are almost
always VNC and the cast to the TV, not the phones. Before blaming the input
path, check the number in the phone's top bar: that is the full round trip from
phone to server and back, and if it reads 40 ms then the input is not your
problem.

Ordered by how much they help:

1. Wire the Windows PC to the TV with HDMI instead of casting.
2. Replace VNC with Moonlight.
3. Make sure Tailscale reports `direct` and not `relay`.
4. Run the whole thing on the Windows PC instead (Plan B).
