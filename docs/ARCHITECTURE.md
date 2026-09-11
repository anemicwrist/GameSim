# Architecture

## The three pieces

**padserver** (`padserver/`) is an aiohttp server. It creates the virtual
gamepads at startup, serves the touch page to the phones, and applies each
WebSocket input message to a pad. It has five backends: `vigem` and `winkey`
for Windows, `uinput` and `xtest` for Linux, and `fake` for tests.

**The emulator** is Flycast, installed from Flathub, either standalone or as a
libretro core inside RetroArch. It is not modified;
`scripts/configure_flycast.py` and `scripts/configure_retroarch.py` merge a
handful of settings into its config, and `scripts/run.sh` launches it.

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

## Why there are two kinds of backend on each platform

The same split appears twice, for the same reason.

| | Virtual gamepads | Synthetic keys |
|---|---|---|
| Windows | `vigem` (ViGEmBus driver) | `winkey` (`SendInput`) |
| Linux | `uinput` (kernel devices) | `xtest` (X11) |

The gamepad backends are better: the emulator sees ordinary controllers and each
player is genuinely a separate device. They are used wherever possible.

Each has a privilege requirement that cannot always be met. `vigem` needs a
kernel-mode driver installed, which a managed or work-owned Windows machine
often forbids. `uinput` needs a real uinput driver in the kernel, and containers
usually have none: no `modprobe`, no `/lib/modules`, nothing to load. Cloud
desktops are containers.

So each platform has a fallback that asks for no privileges at all: `winkey`
sends key events through the Win32 `SendInput` API, and `xtest` injects them
into X11. Neither needs a driver, an install, or elevation.

The catch, in both cases, is that two players then share one keyboard, and
**standalone Flycast cannot bind one keyboard to two Dreamcast ports**
([flyinghead/flycast#68](https://github.com/flyinghead/flycast/issues/68)).
RetroArch can, through `input_player1_*` and `input_player2_*`, so the xtest
path runs the Flycast core inside RetroArch instead.

Both key backends read their assignments from
`padserver/keymap.py`: the backend presses those keys, and
`scripts/configure_retroarch.py` generates the emulator's bindings from the same
table. They cannot drift apart, and the tests assert the two players' keys never
overlap.

## Latency budget

Nothing here is free. Rough one-way numbers for the two arrangements.

**Local, the normal case.** The game runs on your own machine:

| Hop | Cost |
|---|---|
| touch to WebSocket send | 10-20 ms (one browser frame) |
| phone to PC over your own wifi | 1-5 ms |
| backend to emulator | under 2 ms |
| emulator frame | 16 ms |
| PC to TV, HDMI | ~0 |
| PC to TV, screen mirroring | 60-200 ms |

Wired, that is roughly 30-45 ms end to end, which is genuinely good. Mirroring
adds most of the remaining total, which is why a USB-C-to-HDMI adapter is the
best value improvement available to this setup.

Note where the mirroring cost falls: it is *display* lag, not *input* lag. The
emulator has already responded; the picture simply arrives late, and uniformly.
That is much easier to play around than input lag.

**In the cloud.** The emulator runs on a remote Linux box:

| Hop | Cost |
|---|---|
| touch to WebSocket send | 10-20 ms |
| phone to cloud VM over the internet | 10-60 ms, depending on ISP and region |
| backend to emulator | under 2 ms |
| emulator frame | 16 ms with a GPU; considerably more without one |
| VM framebuffer to VNC to the viewing PC | 40-120 ms, and well under 60 fps |
| viewing PC to the TV | 60-200 ms |

Roughly 150-400 ms, with no audio at all, since the VNC stream carries none.
Fine for casual play away from home; not a substitute for the local path.

The pad page shows its own round trip time in the top bar. That number covers
only the phone-to-server hop, which on the local path is the smallest term.

One caveat that dwarfs both tables: on a host with no GPU, every frame is drawn
by the CPU through llvmpipe, and the emulator frame stops being a 16 ms
constant. If the game manages only 25 fps, that row becomes 40 ms and it feels
wrong regardless of the network. `scripts/benchmark.sh` measures this.

## What the cloud box is still good for

Running the emulator remotely is the fallback, not the default: every latency
problem above comes from the emulator being somewhere else, and a cloud desktop
with no GPU renders in software besides. It still earns its place for:

- **Portability.** Away from the TV, the same repo and the same phones work
  against it with no reconfiguration.
- **Storage.** Persistent disk means the game dump can live there and be pulled
  down when wanted, rather than sitting permanently on a machine you do not own.
- **A Linux test bed** for the parts CI cannot cover.

What it is not good for is rendering, and routing video through it when the
local machine is right there only makes things worse.
