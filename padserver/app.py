"""aiohttp application: serves the phone controller page and applies its input."""

from __future__ import annotations

import logging
from pathlib import Path

from aiohttp import WSMsgType, web

from padserver import protocol
from padserver.slots import SlotManager

log = logging.getLogger("padserver")

STATIC_DIR = Path(__file__).parent / "static"

SLOTS = web.AppKey("slots", SlotManager)
ACCESS_TOKEN = web.AppKey("access_token", str)


def _authorized(request: web.Request) -> bool:
    expected = request.app[ACCESS_TOKEN]
    if not expected:
        return True
    return request.query.get("k") == expected


async def index(request: web.Request) -> web.StreamResponse:
    if not _authorized(request):
        raise web.HTTPForbidden(text="bad or missing access token (?k=...)")
    return web.FileResponse(STATIC_DIR / "index.html")


async def health(request: web.Request) -> web.Response:
    return web.json_response({"ok": True})


async def status(request: web.Request) -> web.Response:
    if not _authorized(request):
        raise web.HTTPForbidden(text="bad or missing access token (?k=...)")
    return web.json_response(request.app[SLOTS].status())


async def websocket(request: web.Request) -> web.WebSocketResponse:
    if not _authorized(request):
        raise web.HTTPForbidden(text="bad or missing access token (?k=...)")

    ws = web.WebSocketResponse(heartbeat=5.0, max_msg_size=4096)
    await ws.prepare(request)

    slots: SlotManager = request.app[SLOTS]
    slot = None
    peer = request.remote

    try:
        async for msg in ws:
            if msg.type is not WSMsgType.TEXT:
                continue
            try:
                message = protocol.parse(msg.data)
            except protocol.ProtocolError as exc:
                await ws.send_str(protocol.error_message(str(exc)))
                continue

            if isinstance(message, protocol.Hello):
                if slot is not None:
                    slots.release(slot)
                slot = slots.claim(message.token, message.name)
                if slot is None:
                    await ws.send_str(protocol.full_message(slots.capacity))
                    await ws.close()
                    break
                log.info("player %d claimed by %s (%s)", slot.index + 1, peer, message.name or "?")
                await ws.send_str(protocol.slot_message(slot.index + 1))

            elif isinstance(message, protocol.Input):
                if slot is None:
                    await ws.send_str(protocol.error_message("send hello first"))
                    continue
                slots.apply(slot, message.buttons, message.x, message.y)

            elif isinstance(message, protocol.Ping):
                await ws.send_str(protocol.pong_message(message.ts))
    finally:
        if slot is not None:
            log.info("player %d released by %s", slot.index + 1, peer)
            slots.release(slot)

    return ws


def create_app(
    backend,
    players: int = 2,
    access_token: str = "",
    pad_name: str = "Microsoft X-Box 360 pad",
) -> web.Application:
    app = web.Application()
    app[SLOTS] = SlotManager(backend, players=players, pad_name=pad_name)
    app[ACCESS_TOKEN] = access_token
    app.router.add_get("/", index)
    app.router.add_get("/health", health)
    app.router.add_get("/status", status)
    app.router.add_get("/ws", websocket)
    app.router.add_static("/static/", STATIC_DIR, name="static")

    async def _cleanup(app: web.Application):
        app[SLOTS].close()

    app.on_cleanup.append(_cleanup)
    return app
