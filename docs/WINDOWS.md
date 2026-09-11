# Running it on Windows

This is the main path. The game runs on your own machine, the phones reach it
over your own wifi, and the TV shows the result. Nothing depends on the cloud.

## Which backend you will use

The phones' input has to become input the emulator understands, and there are
two ways to do that on Windows.

| | **vigem** | **winkey** |
|---|---|---|
| What it makes | two virtual Xbox 360 pads | two disjoint sets of key presses |
| Needs | the ViGEmBus driver | nothing beyond Python |
| Administrator rights | **yes**, to install the driver | **no** |
| Emulator | Flycast, standalone | RetroArch with the Flycast core |
| Each player is | a genuinely separate device | half of one shared keyboard |

`vigem` is the better of the two. But installing a kernel-mode driver needs
administrator rights, which a work-owned or managed machine often withholds, so
`winkey` exists to work anywhere. `scripts\setup_windows.ps1` detects which
applies and sets up accordingly; you do not have to choose.

`winkey` needs RetroArch rather than standalone Flycast because two players are
sharing one keyboard, and standalone Flycast cannot bind one keyboard to two
Dreamcast ports.

## Setup

### 1. Python

Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/)
or the Microsoft Store. **The Store version needs no administrator rights**,
which is the easier route on a managed machine.

### 2. This repository

```powershell
git clone https://github.com/anemicwrist/GameSim.git
cd GameSim
powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1
```

`-ExecutionPolicy Bypass` applies to that one command only. It does not change
any machine setting.

The script creates a virtual environment **inside the repository folder**,
installs into it, works out which backend this machine allows, and tells you
which emulator to install. It prints that at the end.

### 3. The emulator

Whichever the setup script named:

- **Flycast** (if it said `vigem`): from [flycast.org](https://flycast.org/)
- **RetroArch** (if it said `winkey`): from [retroarch.com](https://retroarch.com/),
  then in RetroArch go to **Online Updater → Core Downloader → Sega Dreamcast
  (Flycast)**

**Without administrator rights, take the portable build.** RetroArch offers a
`.7z` archive on its download page that you unpack anywhere and run in place,
with no installer and no elevation; Flycast ships as a plain `.exe`. Unpack it
somewhere you can write, such as your user folder or next to this repository.
`run.ps1` searches common locations, and you can always point it straight at the
executable:

```powershell
scripts\run.ps1 -Emulator C:\Users\you\retroarch\retroarch.exe
```

### 4. ViGEmBus, only if you want the better backend

If you have administrator rights and want `vigem`, install
[ViGEmBus](https://github.com/nefarius/ViGEmBus/releases), then re-run
`scripts\setup_windows.ps1`. It will detect the driver and switch over.

### 5. Your game

Put your own Marvel vs Capcom 2 dump in the `games` folder inside the
repository. See [GAME_FILES.md](GAME_FILES.md) for the formats and where to get
one from your own disc.

## Playing

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run.ps1
```

It starts the pad server, prints the URL for the phones, and launches the game.
Open that URL in Chrome on each phone and tap to start. The badge shows PLAYER 1
or PLAYER 2. Press START on both to reach character select.

Closing the emulator stops the pad server.

Useful options:

```powershell
scripts\run.ps1 -Game C:\dumps\mvc2.gdi      # a specific game
scripts\run.ps1 -Tunnel                       # when the firewall blocks the phones
scripts\run.ps1 -Port 9000                    # a different port
scripts\run.ps1 -Token hunter2                # require ?k=hunter2 in the URL
scripts\run.ps1 -Backend winkey               # force a backend
scripts\run.ps1 -Emulator C:\apps\retroarch\retroarch.exe
```

Then get the picture to the TV: see [CASTING.md](CASTING.md). Check whether your
USB-C port does video out before settling for wireless — it is a large
improvement for about ten dollars.

## When the firewall is locked down

The phones need to reach port 8080 on the tablet. Adding a firewall rule needs
administrator rights, and `setup_windows.ps1` will say so if it could not.

Try it first anyway. Windows often prompts to allow Python the first time it
listens, and on a network marked Private it frequently works with no rule.

`setup_windows.ps1` inspects the firewall and tells you whether it expects the
phones to be refused. It cannot test this by connecting to the machine itself,
because a connection from the machine to its own address is not filtered the way
one from a phone is, so it reads the firewall's configuration instead.

If the phones genuinely cannot connect, use the tunnel:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run.ps1 -Tunnel
```

This dials **outbound** from the tablet, so no inbound rule and no administrator
rights are needed. It fetches `cloudflared.exe` into the repository folder on
first use: a single file, nothing installed, removed when you delete the folder.

It prints an HTTPS address the phones can open, and because that address is
public it also generates a secret and requires it in the URL. The address stops
working when you close the game.

The cost is latency: input now travels out to Cloudflare and back rather than
straight across your wifi. Use it only when the direct route is blocked.

## Removing it cleanly

Relevant if this is a work machine. Almost everything lives in the repository
folder, so deleting it removes almost all of it. In full:

1. **Delete the repository folder.** This removes the code, the virtual
   environment, the Python packages, `cloudflared.exe` if you used the tunnel,
   and your game files in one go.
2. **Remove the firewall rule**, if one was added:
   ```powershell
   Remove-NetFirewallRule -DisplayName "GameSim padserver"
   ```
3. **Uninstall the emulator**, if you used an installer rather than a portable
   build. RetroArch also keeps configuration in `%APPDATA%\RetroArch`.
4. **Uninstall ViGEmBus**, if you installed it, from Apps & features.

Nothing else is written: no registry keys of ours, no services, no scheduled
tasks, no system-wide Python packages.

## When something is wrong

**The phones show the page but no player number.** Two players are already
connected. Check `http://localhost:8080/status` on the tablet.

**The phones cannot load the page at all.** Firewall; see above. Confirm the
tablet's address with `ipconfig` and that both phones are on the same network
and not on a guest VLAN.

**The page works but the game ignores it.** With `winkey`, the key presses go to
whichever window has focus, so the emulator window must be focused. With
`vigem`, check the pads exist: press `Win`+`R`, run `joy.cpl`, and you should
see two Xbox 360 controllers.

**RetroArch ignores player 2.** Re-run `scripts\configure_retroarch.py` **while
RetroArch is closed**. It rewrites its configuration on exit and will discard
changes made while it is running.

**The game runs slowly.** Unlikely on Iris Xe, but: plug the tablet in, since
Windows throttles the GPU on battery, and close anything else using it.
