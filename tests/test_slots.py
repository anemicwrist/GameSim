from padserver.backends.fake import FakeBackend
from padserver.protocol import BUTTON_BITS
from padserver.slots import SlotManager


def manager(players=2):
    return SlotManager(FakeBackend(), players=players)


def test_pads_exist_before_anyone_connects():
    m = manager()
    assert len(m.backend.pads) == 2
    assert all(not s.connected for s in m.slots)


def test_two_phones_get_distinct_slots_and_a_third_is_refused():
    m = manager()
    assert m.claim("a").index == 0
    assert m.claim("b").index == 1
    assert m.claim("c") is None


def test_reconnect_keeps_the_same_player_number():
    m = manager()
    first = m.claim("a")
    m.claim("b")
    m.release(first)
    assert m.claim("a").index == first.index


def test_reconnect_prefers_previous_slot_even_when_another_is_free():
    m = manager()
    m.claim("a")
    second = m.claim("b")
    m.release(second)
    assert m.claim("b").index == 1


def test_same_token_reconnecting_while_still_marked_connected_reuses_its_slot():
    m = manager()
    slot = m.claim("a")
    assert m.claim("a").index == slot.index


def test_apply_reaches_the_pad():
    m = manager()
    slot = m.claim("a")
    m.apply(slot, 1 << BUTTON_BITS["HK"], -1, 1)
    assert slot.pad.pressed() == ["HK"]
    assert (slot.pad.x, slot.pad.y) == (-1, 1)


def test_release_recenters_the_pad():
    m = manager()
    slot = m.claim("a")
    m.apply(slot, 0xFF, 1, 1)
    m.release(slot)
    assert slot.pad.pressed() == []
    assert (slot.pad.x, slot.pad.y) == (0, 0)
    assert not slot.connected


def test_status_shape():
    m = manager()
    m.claim("a", "Pixel")
    status = m.status()
    assert status["capacity"] == 2
    assert status["backend"] == "fake"
    assert status["players"][0]["connected"] is True
    assert status["players"][1]["connected"] is False
