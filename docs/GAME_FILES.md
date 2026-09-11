# Game files

**This repository contains no game data, and none of its scripts download any.**
You supply a dump of a copy of Marvel vs Capcom 2 that you own. Everything below
assumes that.

## What you need

**The game.** The Dreamcast release, in any format Flycast reads:

| Format | Notes |
|---|---|
| `.gdi` | a text index plus a set of numbered track files. Keep all of them together in one folder. |
| `.chd` | one compressed file, and the easiest to move around. Roughly 1 GB. |
| `.cdi` | a single-file image. Works, but `.gdi` and `.chd` are more faithful. |
| `.cue` + `.bin` | a text index plus numbered track files. Keep all of them together, with the exact names the `.cue` lists. |

## Checking a dump is complete

A Dreamcast GD-ROM has two areas, and this catches people out. The
**single-density** area is the small part an ordinary CD drive can read: a
warning track and some audio, a few megabytes in total. The **high-density**
area is the game, and it is around 1 GB.

A `.cue` from a GD-ROM rip usually lists three tracks and labels the areas:

```
REM SINGLE-DENSITY AREA
  TRACK 01 MODE1/2352      <- warning data, ~1 MB
  TRACK 02 AUDIO           <- audio, ~14 MB
REM HIGH-DENSITY AREA
  TRACK 03 MODE1/2352      <- THE GAME, ~1 GB
```

So before copying anything, open the `.cue` in a text editor and confirm that a
file exists for **every** `FILE` line it names, and that the high-density track
is the large one. A set that totals a few tens of megabytes contains no game at
all, however many files it has.

Two further rules for `.cue` and `.gdi` sets:

- **Keep the exact filenames.** The index looks for the names written inside it,
  spaces and punctuation included. Renaming a track, or letting a download
  rename it, breaks the set.
- **Keep every file in one folder**, alongside the index.

**The BIOS, optional.** `dc_boot.bin` and `dc_flash.bin`. Flycast has a built-in
high-level BIOS and boots Marvel vs Capcom 2 fine without them. Real BIOS files
give you the Dreamcast boot animation and the system menu, and are needed for
some other titles. They go in Flycast's data directory:

```
~/.var/app/org.flycast.Flycast/data/flycast/      # flatpak install
~/.local/share/flycast/                           # native build
```

## Getting a 1 GB file onto the Orgo computer

Orgo's file upload API caps at 10 MB, so upload is out. Pull it instead, from a
shell on the VM.

**From Google Drive.** Share the file with "anyone with the link", copy the file
id out of the URL, then:

```bash
pip install --user gdown
mkdir -p ~/games/mvc2 && cd ~/games/mvc2
gdown "https://drive.google.com/uc?id=<FILE_ID>"
```

**From any direct URL** (your own web server, an S3 pre-signed link, a Dropbox
link with `?dl=1` on the end):

```bash
mkdir -p ~/games/mvc2 && cd ~/games/mvc2
curl -L -o mvc2.chd "<URL>"
```

**Over Tailscale from your Windows PC.** Once both machines are on your
tailnet (see `docs/NETWORK.md`), serve the folder from Windows and fetch it:

```powershell
# on Windows, in the folder holding the dump
python -m http.server 8000
```
```bash
# on the Orgo computer
curl -O "http://<windows-tailscale-ip>:8000/mvc2.chd"
```

This is the fastest option and the file never leaves your own machines.

## Where to put it

Anywhere under `~/games`. `scripts/run.sh` picks the first `.gdi`, `.chd`,
`.cdi`, `.cue` or `.m3u` it finds there, or you can name the file:

```bash
bash scripts/run.sh ~/games/mvc2/mvc2.chd
```

For a `.gdi`, keep the index file and every track file in the same directory and
point `run.sh` at the `.gdi`.

## Checking it worked

```bash
ls -lh ~/games/mvc2/
```

A truncated download is the most common cause of "Flycast opens and immediately
shows an error". Compare the byte count against the source before blaming the
emulator.

`.gitignore` in this repo excludes `games/`, `*.chd`, `*.gdi`, `*.cdi` and
`*.bin`, so a stray copy inside the checkout will not be committed.
