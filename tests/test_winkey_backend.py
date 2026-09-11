"""The winkey backend runs on a machine that may be locked down and is the
hardest place to debug, so the mapping and event ordering are pinned here. The
sender is injected, so none of this needs Windows or a real keyboard."""

import pytest

from padserver.backends.winkey import WinkeyBackend, WinkeyPad, virtual_key_for
from padserver.keymap import MAX_PLAYERS, keys_for_player
from padserver.protocol import BUTTON_BITS


class StubSender:
    """Stands in for SendInput. Scan codes are the virtual key plus an offset so
    a test can tell the two apart and still trace one back to the other."""

    SCAN_OFFSET = 1000

    def __init__(self):
        self.batches = []

    def scancode_for(self, vk):
        return vk + self.SCAN_OFFSET

    def send(self, events):
        self.batches.append(list(events))

    @property
    def events(self):
        return [event for batch in self.batches for event in batch]


@pytest.fixture
def backend():
    return WinkeyBackend(sender=StubSender())


@pytest.fixture
def pad(backend):
    return backend.create_pad("player 1")


def bit(name):
    return 1 << BUTTON_BITS[name]


def test_letters_and_digits_map_to_virtual_keys():
    assert virtual_key_for("w") == (ord("W"), False)
    assert virtual_key_for("z") == (ord("Z"), False)
    assert virtual_key_for("1") == (ord("1"), False)


def test_arrows_are_flagged_extended():
    for name in ("Up", "Down", "Left", "Right"):
        _vk, extended = virtual_key_for(name)
        assert extended, f"{name} must be sent as an extended key"


def test_letters_are_not_extended():
    _vk, extended = virtual_key_for("w")
    assert not extended


def test_unknown_keysym_raises_rather_than_guessing():
    with pytest.raises(ValueError, match="no Windows virtual key"):
        virtual_key_for("Hyper_R")


def test_every_keymap_entry_can_be_translated():
    for index in range(MAX_PLAYERS):
        for keysym in keys_for_player(index).values():
            virtual_key_for(keysym)


def test_pressing_a_button_sends_one_keydown(pad, backend):
    pad.set_state(bit("LP"), 0, 0)
    assert len(backend._sender.events) == 1
    _scan, _ext, down = backend._sender.events[0]
    assert down is True


def test_holding_sends_nothing_further(pad, backend):
    pad.set_state(bit("LP"), 0, 0)
    backend._sender.batches.clear()
    pad.set_state(bit("LP"), 0, 0)
    pad.set_state(bit("LP"), 0, 0)
    assert backend._sender.batches == []


def test_releasing_sends_one_keyup(pad, backend):
    pad.set_state(bit("LP"), 0, 0)
    backend._sender.batches.clear()
    pad.set_state(0, 0, 0)
    assert [down for _s, _e, down in backend._sender.events] == [False]


def test_flicking_left_to_right_releases_before_pressing(pad, backend):
    pad.set_state(0, -1, 0)
    backend._sender.batches.clear()
    pad.set_state(0, 1, 0)
    downs = [down for _s, _e, down in backend._sender.events]
    # A press before the release would leave both directions held.
    assert downs == [False, True]


def test_a_whole_state_change_goes_out_in_one_batch(pad, backend):
    # One SendInput call means the direction and the button land together.
    pad.set_state(bit("LP") | bit("HP") | bit("A1"), -1, 1)
    assert len(backend._sender.batches) == 1
    assert len(backend._sender.batches[0]) == 5


def test_direction_signs_follow_the_hat_convention(pad, backend):
    # y = -1 is up, matching the Linux hat convention. Player 1's up is whatever
    # keymap.py says it is, so derive it rather than assuming.
    up_keysym = keys_for_player(0)["UP"]
    up_scan = backend._sender.scancode_for(virtual_key_for(up_keysym)[0])
    pad.set_state(0, 0, -1)
    assert backend._sender.events[0][0] == up_scan


def test_arrows_keep_the_extended_flag_through_to_the_sender(backend):
    backend.create_pad("player 1")
    second = backend.create_pad("player 2")
    assert keys_for_player(1)["UP"] == "Up", "this test assumes player 2 is on arrows"
    second.set_state(0, 0, -1)
    _scan, extended, down = backend._sender.events[-1]
    assert extended is True and down is True


def test_players_get_disjoint_scancodes(backend):
    first = backend.create_pad("p1")
    second = backend.create_pad("p2")
    assert set(first._keys.values()).isdisjoint(second._keys.values())


def test_reset_releases_everything(pad, backend):
    pad.set_state(bit("LP") | bit("HK"), 1, -1)
    backend._sender.batches.clear()
    pad.reset()
    assert len(backend._sender.events) == 4
    assert all(down is False for _s, _e, down in backend._sender.events)


def test_close_releases_then_ignores_further_input(pad, backend):
    pad.set_state(bit("LP"), 0, 0)
    backend._sender.batches.clear()
    pad.close()
    assert [down for _s, _e, down in backend._sender.events] == [False]
    backend._sender.batches.clear()
    pad.set_state(bit("HP"), 0, 0)
    assert backend._sender.batches == []


def test_describe_reports_what_is_held(pad):
    pad.set_state(bit("A2"), 0, -1)
    assert pad.describe() == {"name": "player 1", "held": ["A2", "UP"]}


def test_pad_is_usable_without_any_windows_api():
    # Constructed directly, the pad is pure logic: no ctypes, no user32.
    sender = StubSender()
    pad = WinkeyPad("solo", sender, {"LP": (30, False)})
    pad.set_state(bit("LP"), 0, 0)
    assert sender.events == [(30, False, True)]
