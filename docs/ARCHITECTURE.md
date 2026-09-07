# Architecture

## The three pieces

**padserver** (`padserver/`) is an aiohttp server. It creates the virtual
gamepads at startup, serves the touch page to the phones, and applies each
WebSocket input message to a pad. It has three backends: `uinput` for Linux,
`vigem` for Windows, and `fake` for tests.

**Flycast** is the Dreamcast emulator, installed from Flathub. It is not
modified. `scripts/configure_flycast.py` merges a handful of settings into its
`emu.cfg`, and `scripts/run.sh` launches it.

**Docs and scripts** cover everything that is a one-time human step:
provisioning, network, casting.

## Why the pads pretend to be Xbox 360 controllers

The uinput devices declare the same name, vendor, product, version and
capability set as the kernel's `xpad` driver: `Microsoft X-Box 360 pad`,
`045e:028e`, version `0110`, buttons and axes in the same event-code order.

SDL2 therefore computes the GUID `030000005e0400008e02000010010000`, finds that
entry in its built-in controller database, and exposes each pad through the
`SDL_GameController` API. Flycast's built-in default mapping
(`core/sdl/sdl_gamepad.cpp`) then binds a recognised game controller to the
Dreamcast pad with no mapping file:

```
SDL A / B / X / Y   -> Dreamcast A / B / X / Y
SDL LT / RT axes    -> Dreamcast L / R triggers
SDL start / back    -> Dreamcast start / Flycast menu
SDL dpad            -> Dreamcast dpad
```

which lands the arcade six-button layout on the touch buttons. This is why the
assist buttons drive the analog trigger axes `ABS_Z` and `ABS_RZ` rather than
the shoulder buttons: Flycast binds the triggers to L and R first and only falls
back to the shoulders when a pad has no trigger axes.

## Why both pads are created before anyone connects

Flycast identifies a pad as `sdl_joystick_<instance id>`, and SDL hands out
instance ids in the order joysticks are opened. `emu.cfg` pins
`maple_sdl_joystick_0` to port A and `maple_sdl_joystick_1` to port B. So the
pads must exist, in a stable order, before Flycast starts. `scripts/run.sh`
enforces that: pad server first, wait for both device nodes, then the emulator.

A phone connecting later just claims a slot that already owns a pad.

## Latency budget

Nothing here is free. Rough one-way numbers for the Orgo layout:

| Hop | Cost |
|---|---|
| touch to WebSocket send | 10-20 ms (one browser frame) |
| phone to cloud VM over the internet | 10-60 ms, depends on your ISP and the VM region |
| uinput to SDL to Flycast | under 2 ms |
| emulator frame | 16 ms |
| VM framebuffer to VNC to the Windows PC | 40-120 ms, and well under 60 fps |
| Windows PC casting to the TV | 60-200 ms depending on the cast method |

Expect roughly 150-400 ms from pressing a button to seeing it on the TV. That is
fine for casual matches and no good for competitive play. Two things move the
needle most, in order: replacing VNC with Moonlight (see
`docs/TROUBLESHOOTING.md`), and casting with a wired HDMI stick rather than
screen mirroring.

The pad page shows its own round trip time in the top bar. That number covers
only the phone-to-server hop, which is usually the smallest term.

## Plan B: run it all on the Windows PC

Every latency problem above comes from the emulator being in the cloud. The same
repo runs on a Windows machine on your own wifi: install the ViGEmBus driver and
`pip install vgamepad`, run `python -m padserver --backend vigem`, use Flycast
for Windows, and connect the PC to the TV with HDMI. The phones then reach the
PC over the LAN with single-digit millisecond latency, at 60 fps, with sound.
