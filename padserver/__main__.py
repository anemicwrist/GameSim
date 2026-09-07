from __future__ import annotations

import argparse
import logging
import socket
import sys

from aiohttp import web

from padserver.app import create_app
from padserver.backends import make_backend


def local_addresses() -> list:
    addrs = set()
    try:
        hostname = socket.gethostname()
        for info in socket.getaddrinfo(hostname, None, socket.AF_INET):
            addrs.add(info[4][0])
    except OSError:
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.0.2.1", 1))  # TEST-NET-1, no packets are sent
        addrs.add(s.getsockname()[0])
        s.close()
    except OSError:
        pass
    return sorted(a for a in addrs if not a.startswith("127."))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="padserver",
        description="Serve a touch gamepad page and feed it to virtual gamepads.",
    )
    p.add_argument("--host", default="0.0.0.0", help="listen address (default: all)")
    p.add_argument("--port", type=int, default=8080, help="listen port (default: 8080)")
    p.add_argument(
        "--backend",
        default="uinput",
        choices=["uinput", "xtest", "vigem", "fake"],
        help=(
            "how to deliver input (default: uinput). Use xtest on hosts where "
            "/dev/uinput has no driver behind it, such as most containers; run "
            "scripts/uinput_check.py to find out which applies"
        ),
    )
    p.add_argument("--players", type=int, default=2, help="number of pads (default: 2)")
    p.add_argument(
        "--token",
        default="",
        help="shared secret; clients must pass ?k=<token>. Use with a public tunnel.",
    )
    p.add_argument(
        "--pad-name",
        default="Microsoft X-Box 360 pad",
        help="name reported by the virtual devices (default matches the kernel xpad driver)",
    )
    p.add_argument(
        "--no-analog",
        action="store_true",
        help="drive only the d-pad, leaving the analog stick centred (uinput only)",
    )
    p.add_argument("--verbose", action="store_true")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    if args.backend == "uinput":
        from padserver.backends.uinput import UinputBackend

        backend = UinputBackend(mirror_analog=not args.no_analog)
    else:
        backend = make_backend(args.backend)

    app = create_app(
        backend,
        players=args.players,
        access_token=args.token,
        pad_name=args.pad_name,
    )

    suffix = f"?k={args.token}" if args.token else ""
    print(f"padserver: {args.players} pads on the '{args.backend}' backend", file=sys.stderr)
    for addr in local_addresses():
        print(f"  phones open:  http://{addr}:{args.port}/{suffix}", file=sys.stderr)
    print(f"  status page:  http://127.0.0.1:{args.port}/status{suffix}", file=sys.stderr)

    web.run_app(app, host=args.host, port=args.port, print=None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
