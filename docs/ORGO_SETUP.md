# The Orgo computer

Orgo (orgo.ai) rents cloud Linux desktops. A few properties of that platform
shape this project.

| Property | Consequence here |
|---|---|
| No public inbound hostname or open ports | the phones cannot reach the VM directly; see `docs/NETWORK.md` |
| Desktop is streamed as VNC over websockify, 1280x720 by default | the TV shows a VNC view, not a native display |
| No audio in the desktop stream | game sound does not reach the TV; see `docs/CASTING.md` |
| Disk persists across stop and start | install once, play many times |
| File upload API caps at 10 MB | the game dump has to be pulled in from a URL |
| 1-4 vCPU, optional 2 GB or 4 GB vGPU on Linux | pick the largest tier you can |

## Provisioning

Pick a Linux computer, the 4 vCPU tier, with a GPU if the plan offers one.
Flycast runs Marvel vs Capcom 2 on software rendering, but a GPU is the
difference between a steady 60 fps and a variable one, and it leaves CPU free
for the video encode.

## Getting a shell

Either works:

- `orgo ssh <name>` from your Windows machine, which opens an interactive shell
  over a WebSocket.
- The terminal application inside the desktop itself, which you reach from the
  Orgo web viewer.

Use the desktop's own terminal for `scripts/run.sh`, because Flycast needs the
graphical session. If you start it over `orgo ssh` you may have to set
`DISPLAY=:0` first; `run.sh` warns when `DISPLAY` is unset.

## Order of operations

```bash
git clone https://github.com/anemicwrist/GameSim.git && cd GameSim
bash scripts/probe.sh
```

Read the probe output before installing anything. Two lines decide whether this
plan works at all:

- **`/dev/uinput`** must exist, or be creatable with `sudo modprobe uinput`.
  Without it there are no virtual gamepads, and the only route left is Plan B in
  `docs/ARCHITECTURE.md`.
- **the OpenGL renderer** tells you whether you got a GPU or `llvmpipe`
  software rendering. Software rendering still works; keep
  `rend.Resolution = 480` in that case and do not raise it.

Then:

```bash
bash scripts/install_deps.sh      # then log out and back in
bash scripts/install_flycast.sh
bash scripts/install_tailscale.sh
```

## Keeping the desktop alive

The Orgo viewer disconnects after about 30 minutes with no input (WebSocket
close code 4008). That closes your *view* of the machine, not the machine. The
game keeps running; reopen the viewer. The phones' input path is independent of
the viewer entirely.
