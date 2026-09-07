import json

import pytest
from aiohttp import WSServerHandshakeError
from aiohttp.test_utils import TestClient, TestServer

from padserver.app import create_app
from padserver.backends.fake import FakeBackend
from padserver.protocol import BUTTON_BITS


async def make_client(token=""):
    backend = FakeBackend()
    app = create_app(backend, players=2, access_token=token)
    client = TestClient(TestServer(app))
    await client.start_server()
    return client, backend


async def hello(ws, token="t1", name="phone"):
    await ws.send_str(json.dumps({"t": "hello", "token": token, "name": name}))
    return json.loads(await ws.receive_str())


@pytest.fixture
async def client():
    client, backend = await make_client()
    client.backend = backend
    yield client
    await client.close()


async def test_serves_the_controller_page(client):
    resp = await client.get("/")
    assert resp.status == 200
    assert "MvC2 Pad" in await resp.text()


async def test_health(client):
    resp = await client.get("/health")
    assert (await resp.json()) == {"ok": True}


async def test_hello_assigns_player_one(client):
    async with client.ws_connect("/ws") as ws:
        assert (await hello(ws))["player"] == 1


async def test_two_sockets_get_two_players_and_two_pads(client):
    async with client.ws_connect("/ws") as a, client.ws_connect("/ws") as b:
        assert (await hello(a, "t1"))["player"] == 1
        assert (await hello(b, "t2"))["player"] == 2
    assert len(client.backend.pads) == 2


async def test_third_phone_is_told_the_game_is_full(client):
    async with client.ws_connect("/ws") as a, client.ws_connect("/ws") as b:
        await hello(a, "t1")
        await hello(b, "t2")
        async with client.ws_connect("/ws") as c:
            reply = await hello(c, "t3")
            assert reply["t"] == "full"
            assert reply["capacity"] == 2


async def test_input_reaches_the_pad(client):
    async with client.ws_connect("/ws") as ws:
        await hello(ws)
        mask = (1 << BUTTON_BITS["LP"]) | (1 << BUTTON_BITS["A1"])
        await ws.send_str(json.dumps({"t": "in", "b": mask, "x": -1, "y": 0}))
        await ws.send_str(json.dumps({"t": "ping", "ts": 1}))  # round trip to order events
        assert json.loads(await ws.receive_str())["t"] == "pong"
        pad = client.backend.pads[0]
        assert (pad.buttons, pad.x, pad.y) == (mask, -1, 0)


async def test_disconnect_releases_the_slot_and_recenters(client):
    async with client.ws_connect("/ws") as ws:
        await hello(ws, "t1")
        await ws.send_str(json.dumps({"t": "in", "b": 0xFF, "x": 1, "y": 1}))
        await ws.send_str(json.dumps({"t": "ping", "ts": 1}))
        await ws.receive_str()
    async with client.ws_connect("/ws") as ws2:
        assert (await hello(ws2, "t9"))["player"] in (1, 2)
    assert client.backend.pads[0].history[-1] == (0, 0, 0)


async def test_input_before_hello_is_an_error(client):
    async with client.ws_connect("/ws") as ws:
        await ws.send_str(json.dumps({"t": "in", "b": 1}))
        reply = json.loads(await ws.receive_str())
        assert reply["t"] == "error"


async def test_malformed_message_does_not_drop_the_connection(client):
    async with client.ws_connect("/ws") as ws:
        await hello(ws)
        await ws.send_str("garbage")
        assert json.loads(await ws.receive_str())["t"] == "error"
        await ws.send_str(json.dumps({"t": "ping", "ts": 2}))
        assert json.loads(await ws.receive_str())["t"] == "pong"


async def test_ping_echoes_the_timestamp(client):
    async with client.ws_connect("/ws") as ws:
        await hello(ws)
        await ws.send_str(json.dumps({"t": "ping", "ts": 1234.5}))
        assert json.loads(await ws.receive_str())["ts"] == 1234.5


async def test_status_reports_players():
    client, backend = await make_client()
    try:
        async with client.ws_connect("/ws") as ws:
            await hello(ws, "t1", "Pixel")
            body = await (await client.get("/status")).json()
        assert body["players"][0]["connected"] is True
        assert body["players"][0]["name"] == "Pixel"
    finally:
        await client.close()


async def test_token_gates_the_page_and_the_socket():
    client, _ = await make_client(token="s3cret")
    try:
        assert (await client.get("/")).status == 403
        assert (await client.get("/?k=wrong")).status == 403
        assert (await client.get("/?k=s3cret")).status == 200
        with pytest.raises(WSServerHandshakeError):
            await client.ws_connect("/ws")
        async with client.ws_connect("/ws?k=s3cret") as ws:
            assert (await hello(ws))["player"] == 1
    finally:
        await client.close()
