# GameSim

Play Marvel vs Capcom 2 on a cloud Linux desktop, with two Android phones as the
controllers and your TV as the screen.

```
[Phone 1] ─┐   wifi → internet (Tailscale, or a Cloudflare tunnel)
[Phone 2] ─┴──────────────►  Orgo Linux computer
                               padserver  (this repo)
                                 └─ two virtual pads, or two sets of keys
                                      └─ Flycast  →  Marvel vs Capcom 2
                               desktop → VNC
                                            │
   [TV] ◄── cast ── [Windows PC: Orgo viewer in the browser] ◄┘
```

The phones load a web page. No app to install, nothing to pair. The page turns
touch input into two independent controllers that the emulator sees plugged
into Dreamcast ports A and B.

## Two ways in, picked automatically

How the phones' input reaches the emulator depends on what the host allows.
`scripts/uinput_check.py` decides, and the setup scripts follow its verdict.

| | **uinput** | **xtest** |
|---|---|---|
| What it makes | two virtual Xbox 360 gamepads | two disjoint sets of key presses |
| Needs | a real `uinput` driver in the kernel | an X display |
| Emulator | Flycast, standalone | Flycast core inside RetroArch |
| Where it works | a normal Linux desktop | anywhere, containers included |

Most cloud desktops, the Orgo one included, have no `uinput` driver, so **xtest
is the usual answer there**. Note that `/dev/uinput` existing proves nothing:
it is an ordinary character device that `mknod` will create with nothing behind
it, which is why the check opens it instead of looking for it. RetroArch is
needed for that path because standalone Flycast cannot split one keyboard
between two Dreamcast ports.

## You need to supply

- An Orgo Linux computer. Take the largest tier you can: the emulator is the
  hungry part. If a GPU is offered, take it. Without one everything is drawn by
  the CPU, and `scripts/benchmark.sh` will tell you whether that is fast enough
  before you build anything on top of it.
- **Your own Marvel vs Capcom 2 Dreamcast dump.** This repo contains no game
  data and will not fetch any. See [docs/GAME_FILES.md](docs/GAME_FILES.md).
- Two Android phones with Chrome, on any network.
- A Windows PC with Chrome or Edge to view the desktop and cast it to the TV.

## Setup, once

Run these on the Orgo computer (`orgo ssh <name>`, or its terminal app).

```bash
git clone https://github.com/anemicwrist/GameSim.git && cd GameSim
bash scripts/probe.sh              # what this machine can and cannot do
bash scripts/install_deps.sh       # python env, and picks the input backend
bash scripts/benchmark.sh          # can it render fast enough? see below
bash scripts/install_tailscale.sh  # private path from the phones (recommended)
```

`install_deps.sh` prints which backend this host will use. Then install the
emulator that goes with it:

```bash
bash scripts/install_flycast.sh    # if it said 'uinput'
bash scripts/install_retroarch.sh  # if it said 'xtest'
```

If it said `uinput`, log out and back in so your `input` group membership takes
effect. Either way, put your game file under `~/games/`.

## Will it actually run fast enough?

On a host with no GPU this is the question that decides everything, so answer it
before wiring up phones and a TV. `scripts/benchmark.sh` measures the machine,
and once you have the game file the frame counter is already switched on:

```bash
bash scripts/run.sh /path/to/mvc2.gdi
```

Marvel vs Capcom 2 runs at 60 fps natively. In a real match, 55-60 means the
plan works; 40-55 is playable but visibly slow; under 30 means run the emulator
on your own machine instead and use this repo's pad server against that.

## Every session

```bash
bash scripts/run.sh
```

It starts the pad server, waits for both virtual pads, applies the Flycast
settings and launches the game fullscreen. It prints the URL for the phones.
Open that URL in Chrome on each phone, tap **Tap to start**, and the badge shows
PLAYER 1 or PLAYER 2. Press START on both to get to character select.

On the Windows PC, open the Orgo desktop viewer fullscreen and cast the tab to
the TV. See [docs/CASTING.md](docs/CASTING.md).

## Controls

The right-hand buttons are the arcade layout.

| Touch | Dreamcast | Marvel vs Capcom 2 |
|---|---|---|
| LP | X | light punch |
| HP | Y | heavy punch |
| A1 | L trigger | assist 1 |
| LK | A | light kick |
| HK | B | heavy kick |
| A2 | R trigger | assist 2 |
| START | Start | start / pause |
| MENU | Back | opens the Flycast menu |

## Documentation

| File | What it covers |
|---|---|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | how the pieces fit, and the latency budget |
| [docs/ORGO_SETUP.md](docs/ORGO_SETUP.md) | provisioning and reaching the Orgo computer |
| [docs/GAME_FILES.md](docs/GAME_FILES.md) | which files you need and how to get them onto the VM |
| [docs/NETWORK.md](docs/NETWORK.md) | Tailscale, and the Cloudflare tunnel fallback |
| [docs/CASTING.md](docs/CASTING.md) | desktop to TV, and the audio caveat |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | when a pad, the video or the game does not show up |

## Scripts

| Script | What it does |
|---|---|
| `scripts/probe.sh` | reports what this machine can do; safe to re-run any time |
| `scripts/uinput_check.py` | decides which input backend is possible, by actually trying |
| `scripts/benchmark.sh` | measures whether the graphics are fast enough to bother |
| `scripts/install_deps.sh` | python environment, and installs for the backend it finds |
| `scripts/install_flycast.sh` | Flycast from Flathub (uinput path) |
| `scripts/install_retroarch.sh` | RetroArch and the Flycast core (xtest path) |
| `scripts/configure_retroarch.py` | generates two-player key bindings from `padserver/keymap.py` |
| `scripts/install_tailscale.sh` | private network path from the phones |
| `scripts/run.sh` | starts the server and launches the game |

## Development

```bash
pip install -e ".[dev]"
python -m pytest          # no kernel devices needed
python -m ruff check .
python -m padserver --backend fake --port 8080   # try the page on a desktop browser
python scripts/uinput_check.py                   # which backend does this host allow?
python scripts/configure_retroarch.py --dry-run  # the generated key bindings
```

`--backend fake` creates no devices, so the page and the protocol can be
exercised anywhere, including on a machine with no `/dev/uinput`. The tests
stub X11 and never touch a kernel device, so they run in CI unchanged.
