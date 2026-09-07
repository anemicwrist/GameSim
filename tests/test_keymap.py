"""The key maps are shared by the xtest backend and the generated emulator
config, so a mistake here silently breaks player 2 in a way that is painful to
debug at the TV. These tests are cheap insurance."""

import pytest

from padserver import keymap
from padserver.protocol import BUTTON_ORDER


def test_maps_are_complete_and_disjoint():
    keymap.validate()


def test_every_player_covers_every_control():
    for index in range(keymap.MAX_PLAYERS):
        mapping = keymap.keys_for_player(index)
        assert set(mapping) == set(keymap.CONTROLS)


def test_buttons_match_the_protocol():
    for name in BUTTON_ORDER:
        assert name in keymap.CONTROLS


def test_no_keysym_is_shared_between_players():
    first = set(keymap.keys_for_player(0).values())
    second = set(keymap.keys_for_player(1).values())
    assert first.isdisjoint(second)


def test_keys_for_player_rejects_out_of_range():
    with pytest.raises(ValueError, match="no key map"):
        keymap.keys_for_player(keymap.MAX_PLAYERS)


def test_keys_for_player_returns_a_copy():
    mapping = keymap.keys_for_player(0)
    mapping["UP"] = "clobbered"
    assert keymap.keys_for_player(0)["UP"] != "clobbered"


def test_validate_catches_a_duplicate(monkeypatch):
    clashing = [dict(keymap.PLAYER_KEYS[0]), dict(keymap.PLAYER_KEYS[1])]
    clashing[1]["LP"] = clashing[0]["LP"]
    monkeypatch.setattr(keymap, "PLAYER_KEYS", clashing)
    with pytest.raises(ValueError, match="used twice"):
        keymap.validate()


def test_validate_catches_a_missing_control(monkeypatch):
    short = [dict(keymap.PLAYER_KEYS[0]), dict(keymap.PLAYER_KEYS[1])]
    del short[0]["A2"]
    monkeypatch.setattr(keymap, "PLAYER_KEYS", short)
    with pytest.raises(ValueError, match="missing"):
        keymap.validate()
