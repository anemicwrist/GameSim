# GameSim

Play Marvel vs Capcom 2 with two friends, using two Android phones as the
controllers and your TV as the screen.

```
[Phone 1] ─┐  your own wifi
[Phone 2] ─┴──→  Windows PC
                   padserver  (this repo)
                     └─ two virtual pads, or two sets of keys
                          └─ Flycast  →  Marvel vs Capcom 2
                   └────────── HDMI or screen mirroring ──────────→ [TV]
```

The phones load a web page. No app to install, nothing to pair. The page turns
touch input into two independent controllers that the emulator sees plugged into
Dreamcast ports A and B.

Everything runs on your own machine and your own network, so inputs arrive in
single-digit milliseconds and the game has sound.

## You need to supply

- **A Windows PC.** Anything with Intel Iris Xe or better runs this at a locked
  60 fps. Integrated graphics are fine; a Dreamcast emulator is not demanding by
  modern standards.
- **Your own Marvel vs Capcom 2 Dreamcast dump.** This repo contains no game
  data and will not fetch any. See [docs/GAME_FILES.md](docs/GAME_FILES.md).
- **Two Android phones** with Chrome, on the same wifi.
- **A way to get the picture to the TV**: an HDMI cable, a USB-C-to-HDMI adapter,
  or wireless screen mirroring. See [docs/CASTING.md](docs/CASTING.md).

## Quick start

```powershell
git clone https://github.com/anemicwrist/GameSim.git
cd GameSim
powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1
```

That works out what your machine allows and tells you which emulator to install.
Put your game dump in the `games` folder, then:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run.ps1
```

It prints a URL. Open it in Chrome on each phone, tap **Tap to start**, and the
badge shows PLAYER 1 or PLAYER 2. Press START on both to reach character select.

Full walkthrough, including machines where you are not an administrator:
[docs/WINDOWS.md](docs/WINDOWS.md).

## Two ways in, picked automatically

How the phones' input reaches the emulator depends on what the host allows. The
setup scripts decide; you do not have to.

| | Virtual gamepads | Synthetic keys |
|---|---|---|
| Windows | `vigem`, needs the ViGEmBus driver and admin rights | `winkey`, needs nothing |
| Linux | `uinput`, needs a real uinput driver | `xtest`, needs an X display |
| Emulator | Flycast, standalone | RetroArch with the Flycast core |
| Each player is | a genuinely separate device | half of one shared keyboard |

The gamepad backends are better and are used wherever possible. The key-based
ones exist because a managed Windows machine may forbid installing a driver, and
because most Linux containers have no uinput driver at all. They need RetroArch
rather than standalone Flycast, which cannot bind one keyboard to two Dreamcast
ports.

The two players' key assignments live in `padserver/keymap.py`, and
`scripts/configure_retroarch.py` generates the emulator's bindings from that
same module, so they cannot drift apart.

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
| MENU | Back | opens the emulator menu |

## Running it in the cloud instead

The same repo runs on a Linux box, including a cloud desktop such as Orgo, with
the phones reaching it over Tailscale or a tunnel. That is the right choice when
you are away from the TV, and the wrong one when you are sitting in front of it:
a cloud desktop with no GPU renders in software, its VNC stream carries no
audio, and every input crosses the internet twice.

Treat it as the portable option, not the main one. See
[docs/ORGO_SETUP.md](docs/ORGO_SETUP.md), and run `scripts/benchmark.sh` there
before trusting it with an evening.

Orgo also earns its keep as **storage**: it has persistent disk, so your game
dump can live there and be pulled down when needed rather than sitting on a
work-owned laptop.

## Documentation

| File | What it covers |
|---|---|
| [docs/WINDOWS.md](docs/WINDOWS.md) | the main path, start to finish, admin rights or not |
| [docs/CASTING.md](docs/CASTING.md) | getting the picture to the TV, wired and wireless |
| [docs/GAME_FILES.md](docs/GAME_FILES.md) | which files you need and how to move them around |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | how the pieces fit, and the latency budget |
| [docs/NETWORK.md](docs/NETWORK.md) | Tailscale, and the Cloudflare tunnel fallback |
| [docs/ORGO_SETUP.md](docs/ORGO_SETUP.md) | the cloud option: provisioning and setup |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | when a pad, the video or the game does not show up |

## Scripts

**Windows**

| Script | What it does |
|---|---|
| `scripts/setup_windows.ps1` | venv, dependencies, firewall, and picks the backend |
| `scripts/run.ps1` | starts the server and launches the game |

**Linux / cloud**

| Script | What it does |
|---|---|
| `scripts/probe.sh` | reports what a machine can do; safe to re-run any time |
| `scripts/uinput_check.py` | decides which input backend is possible, by actually trying |
| `scripts/benchmark.sh` | measures whether the graphics are fast enough to bother |
| `scripts/install_deps.sh` | python environment, and installs for the backend it finds |
| `scripts/install_flycast.sh` | Flycast from Flathub (uinput path) |
| `scripts/install_retroarch.sh` | RetroArch and the Flycast core (xtest path) |
| `scripts/install_tailscale.sh` | private network path from the phones |
| `scripts/run.sh` | starts the server and launches the game |

**Either**

| Script | What it does |
|---|---|
| `scripts/configure_retroarch.py` | generates two-player key bindings from `padserver/keymap.py` |
| `scripts/configure_flycast.py` | merges settings into Flycast's `emu.cfg` |

## Development

```bash
pip install -e ".[dev]"
python -m pytest          # no kernel devices, no display, no Windows needed
python -m ruff check .
python -m padserver --backend fake --port 8080   # try the page in a browser
python scripts/configure_retroarch.py --dry-run  # the generated key bindings
```

`--backend fake` creates no devices, so the page and the protocol can be
exercised anywhere. The tests stub Xlib, `vgamepad` and the Win32 API, so all
four real backends are covered from Linux CI with no special hardware.
