"""The RetroArch bindings are generated, not hand-written, so the generator is
the thing worth testing. A wrong key name produces a binding that silently does
nothing, which is miserable to debug with a phone in each hand."""

import importlib.util
import pathlib

import pytest

from padserver.keymap import CONTROLS, MAX_PLAYERS, keys_for_player

SPEC = importlib.util.spec_from_file_location(
    "configure_retroarch",
    pathlib.Path(__file__).parent.parent / "scripts" / "configure_retroarch.py",
)
cr = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cr)


@pytest.mark.parametrize(
    "keysym, expected",
    [
        ("w", "w"),
        ("z", "z"),
        ("Up", "up"),
        ("Down", "down"),
        ("Left", "left"),
        ("Right", "right"),
        ("1", "num1"),
        ("4", "num4"),
        ("Return", "enter"),
    ],
)
def test_keysym_translation(keysym, expected):
    assert cr.retroarch_key(keysym) == expected


def test_unknown_keysym_raises_rather_than_guessing():
    with pytest.raises(ValueError, match="no RetroArch key name"):
        cr.retroarch_key("Hyper_R")


def test_every_control_is_bound_for_every_player():
    for index in range(MAX_PLAYERS):
        bindings = cr.player_bindings(index)
        assert len(bindings) == len(CONTROLS)
        for control in CONTROLS:
            key = f"input_player{index + 1}_{cr.CONTROL_TO_RETROPAD[control]}"
            assert key in bindings


def test_retropad_letters_are_positional_not_literal():
    # The Flycast core maps RetroPad onto the Dreamcast diamond by position, so
    # light punch (Dreamcast X) must land on RetroPad Y, not RetroPad X.
    assert cr.CONTROL_TO_RETROPAD["LP"] == "y"
    assert cr.CONTROL_TO_RETROPAD["HP"] == "x"
    assert cr.CONTROL_TO_RETROPAD["LK"] == "b"
    assert cr.CONTROL_TO_RETROPAD["HK"] == "a"


def test_bindings_match_the_keymap_the_backend_presses():
    for index in range(MAX_PLAYERS):
        mapping = keys_for_player(index)
        bindings = cr.player_bindings(index)
        for control, keysym in mapping.items():
            key = f"input_player{index + 1}_{cr.CONTROL_TO_RETROPAD[control]}"
            assert bindings[key] == cr.retroarch_key(keysym)


def test_players_never_share_a_bound_key():
    first = set(cr.player_bindings(0).values())
    second = set(cr.player_bindings(1).values())
    assert first.isdisjoint(second)


def test_settings_enable_both_players():
    settings = cr.build_settings()
    assert settings["input_max_users"] == "2"
    assert settings["video_fullscreen"] == "true"
    assert settings["fps_show"] == "true"


def test_menu_toggle_is_player_ones_select():
    settings = cr.build_settings()
    expected = cr.retroarch_key(keys_for_player(0)["SELECT"])
    assert settings["input_menu_toggle"] == expected


def test_cfg_roundtrip():
    entries = {"video_fullscreen": "true", "input_player1_a": "k"}
    assert cr.parse_cfg(cr.render_cfg(entries)) == entries


def test_parse_ignores_comments_and_blanks():
    text = '# a comment\n\nvideo_fullscreen = "true"\n'
    assert cr.parse_cfg(text) == {"video_fullscreen": "true"}


def test_merge_keeps_unrelated_settings(tmp_path):
    cfg = tmp_path / "retroarch.cfg"
    cfg.write_text('savefile_directory = "/home/someone/saves"\ninput_player1_a = "wrong"\n')
    assert cr.main(["--config-dir", str(tmp_path)]) == 0
    result = cr.parse_cfg(cfg.read_text())
    assert result["savefile_directory"] == "/home/someone/saves"
    assert result["input_player1_a"] == "k"


def test_rerunning_is_a_no_op(tmp_path, capsys):
    cr.main(["--config-dir", str(tmp_path)])
    capsys.readouterr()
    cr.main(["--config-dir", str(tmp_path)])
    assert "already correct" in capsys.readouterr().out


def test_existing_config_is_backed_up(tmp_path):
    cfg = tmp_path / "retroarch.cfg"
    cfg.write_text('input_player1_a = "wrong"\n')
    cr.main(["--config-dir", str(tmp_path)])
    assert (tmp_path / "retroarch.cfg.bak").exists()
