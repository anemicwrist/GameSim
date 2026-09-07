#!/usr/bin/env python3
"""Decide whether kernel-level virtual gamepads are possible on this machine.

Existence of /dev/uinput proves nothing. The node is an ordinary character
special file, so `mknod /dev/uinput c 10 223` creates one on any system whether
or not the kernel has the uinput driver behind it. Containers routinely have no
driver, no `modprobe`, and no /lib/modules at all. The only honest test is to
open the node and create a device.

This script does that and reports one of four verdicts, so the setup scripts and
the docs can stop guessing:

    ok        a real device was created; use the uinput backend
    nodriver  node opens to nothing; the kernel lacks uinput; use the xtest backend
    denied    driver is there but this user or container may not use it
    nonode    no node, and it could not be created

Exit codes match: 0 ok, 2 nodriver, 3 denied, 4 nonode.
"""

from __future__ import annotations

import argparse
import errno
import os
import stat
import subprocess
import sys

DEV = "/dev/uinput"
UINPUT_MAJOR = 10
UINPUT_MINOR = 223

OK, NODRIVER, DENIED, NONODE = "ok", "nodriver", "denied", "nonode"
EXIT_CODES = {OK: 0, NODRIVER: 2, DENIED: 3, NONODE: 4}

ADVICE = {
    OK: "Virtual gamepads work here. Use the uinput backend (the default).",
    NODRIVER: (
        "The node exists but has no driver behind it, so no gamepad can ever be\n"
        "created. This is normal in a container. Run padserver with\n"
        "--backend xtest, which needs no kernel device."
    ),
    DENIED: (
        "The driver is present but access was refused. If you are not root, run\n"
        "scripts/install_deps.sh to join the 'input' group, then log back in.\n"
        "If you are root, the container's device cgroup is blocking it; use\n"
        "--backend xtest instead."
    ),
    NONODE: (
        "No /dev/uinput and it could not be created. Re-run this as root to let\n"
        "it try mknod, or use --backend xtest."
    ),
}


def classify(exc: OSError) -> str:
    """Map an errno from opening /dev/uinput onto a verdict.

    ENODEV and ENXIO both mean 'no driver behind this node', which is what a
    hand-made node in a driverless container gives you.
    """
    if exc.errno in (errno.ENODEV, errno.ENXIO):
        return NODRIVER
    if exc.errno in (errno.EACCES, errno.EPERM):
        return DENIED
    if exc.errno == errno.ENOENT:
        return NONODE
    return NODRIVER


def node_exists() -> bool:
    try:
        return stat.S_ISCHR(os.stat(DEV).st_mode)
    except OSError:
        return False


def try_mknod() -> bool:
    """Create the node. Only possible as root, and only helps if a driver exists."""
    if os.geteuid() != 0:
        return False
    try:
        subprocess.run(
            ["mknod", DEV, "c", str(UINPUT_MAJOR), str(UINPUT_MINOR)],
            check=True,
            capture_output=True,
        )
        os.chmod(DEV, 0o660)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


def probe(create: bool = True) -> tuple[str, str]:
    """Return (verdict, detail). Creates the node first if asked and needed."""
    created = False
    if not node_exists():
        if not create or not try_mknod():
            return NONODE, f"{DEV} does not exist"
        created = True

    note = " (node created by this script)" if created else ""

    try:
        fd = os.open(DEV, os.O_WRONLY | os.O_NONBLOCK)
    except OSError as exc:
        return classify(exc), f"open({DEV}) failed: {exc.strerror}{note}"
    os.close(fd)

    # Opening can succeed where creating a device still fails, so go all the way.
    try:
        from evdev import UInput
    except Exception:
        return OK, f"{DEV} opened{note}; python evdev not installed, device not created"

    try:
        device = UInput(name="padserver-probe")
    except OSError as exc:
        return classify(exc), f"UI_DEV_CREATE failed: {exc.strerror}{note}"
    except Exception as exc:  # evdev wraps some failures
        return NODRIVER, f"UI_DEV_CREATE failed: {exc}{note}"
    path = device.device.path if device.device else "?"
    device.close()
    return OK, f"created and destroyed a real device at {path}{note}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--no-create",
        action="store_true",
        help="report only; do not try to mknod a missing node",
    )
    parser.add_argument(
        "--quiet", action="store_true", help="print the verdict word and nothing else"
    )
    args = parser.parse_args(argv)

    verdict, detail = probe(create=not args.no_create)

    if args.quiet:
        print(verdict)
    else:
        print(f"uinput: {verdict}")
        print(f"  {detail}")
        print()
        for paragraph in ADVICE[verdict].split("\n"):
            print(f"  {paragraph}")
    return EXIT_CODES[verdict]


if __name__ == "__main__":
    sys.exit(main())
