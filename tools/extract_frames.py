#!/usr/bin/env python3
"""Sample still frames from a game recording so the Coach can rebuild the turn log.

Usage: python3 tools/extract_frames.py <recording> [out_dir] [--fps 0.2] [--width 960]
Frames go to out_dir (default: frames/<recording name>/), which git ignores.
"""
import argparse
import pathlib
import subprocess
import sys


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "imageio-ffmpeg"], check=True)
        import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("recording")
    parser.add_argument("out_dir", nargs="?")
    parser.add_argument("--fps", type=float, default=0.2, help="frames per second to keep (default 0.2, one every 5s)")
    parser.add_argument("--width", type=int, default=960, help="output width in pixels (default 960)")
    args = parser.parse_args()

    src = pathlib.Path(args.recording)
    out = pathlib.Path(args.out_dir or f"frames/{src.stem}")
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [ffmpeg_exe(), "-loglevel", "error", "-i", str(src),
         "-vf", f"fps={args.fps},scale={args.width}:-2", str(out / "f_%04d.jpg"), "-y"],
        check=True,
    )
    print(f"{len(list(out.glob('f_*.jpg')))} frames -> {out}")


if __name__ == "__main__":
    main()
