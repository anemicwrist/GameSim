"""Backend interface: something that turns button state into OS-level gamepad events."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Pad(Protocol):
    """One virtual gamepad."""

    def set_state(self, buttons: int, x: int, y: int) -> None:
        """Apply a full input state. ``buttons`` is the protocol bitmask,
        ``x``/``y`` are the d-pad direction, each in {-1, 0, 1}."""

    def reset(self) -> None:
        """Release everything (used when a player disconnects)."""

    def close(self) -> None:
        """Destroy the underlying device."""


@runtime_checkable
class Backend(Protocol):
    name: str

    def create_pad(self, name: str) -> Pad: ...

    def close(self) -> None: ...


def make_backend(kind: str):
    """Instantiate a backend by name. Imports lazily so that a missing optional
    dependency only matters when that backend is actually requested."""
    if kind == "fake":
        from padserver.backends.fake import FakeBackend

        return FakeBackend()
    if kind == "uinput":
        from padserver.backends.uinput import UinputBackend

        return UinputBackend()
    if kind == "vigem":
        from padserver.backends.vigem import VigemBackend

        return VigemBackend()
    raise ValueError(f"unknown backend: {kind!r} (expected fake, uinput or vigem)")
