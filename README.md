# GameSim

Play Marvel vs Capcom 2 on a cloud Linux desktop, with two Android phones as the
controllers and your TV as the screen.

```
[Phone 1] ─┐   wifi → internet (Tailscale, or a Cloudflare tunnel)
[Phone 2] ─┴──────────────►  Orgo Linux computer
                               padserver  (this repo)
                                 └─ two virtual Xbox 360 pads via /dev/uinput
                                      └─ Flycast  →  Marvel vs Capcom 2
                               desktop → VNC
                                            │
   [TV] ◄── cast ── [Windows PC: Orgo viewer in the browser] ◄┘
```

The phones load a web page. No app to install, nothing to pair. The page turns
touch input into two kernel-level gamepads, which the emulator sees as ordinary
Xbox 360 controllers plugged into Dreamcast ports A and B.

## You need to supply

- An Orgo Linux computer. The 4 vCPU tier with a GPU is the one to pick.
- **Your own Marvel vs Capcom 2 Dreamcast dump.** This repo contains no game
  data and will not fetch any. See [docs/GAME_FILES.md](docs/GAME_FILES.md).
- Two Android phones with Chrome, on any network.
- A Windows PC with Chrome or Edge to view the desktop and cast it to the TV.

## Setup, once

Run these on the Orgo computer (`orgo ssh <name>`, or its terminal app).

```bash
git clone https://github.com/anemicwrist/GameSim.git && cd GameSim
bash scripts/probe.sh              # check this machine can do the job
bash scripts/install_deps.sh       # python env + /dev/uinput access
bash scripts/install_flycast.sh    # Flycast from Flathub
bash scripts/install_tailscale.sh  # private path from the phones (recommended)
```

Log out and back in after `install_deps.sh` so your `input` group membership
takes effect, then put your game file under `~/games/`.

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

## Development

```bash
pip install -e ".[dev]"
python -m pytest          # no kernel devices needed
python -m ruff check .
python -m padserver --backend fake --port 8080   # try the page on a desktop browser
```

`--backend fake` creates no devices, so the page and the protocol can be
exercised anywhere, including on a machine with no `/dev/uinput`.
