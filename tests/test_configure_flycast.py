"""The Flycast config merger must never lose settings Flycast wrote itself."""

import importlib.util
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "configure_flycast", REPO / "scripts" / "configure_flycast.py"
)
cf = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cf)


def test_parses_sections_keys_and_comments():
    parsed = cf.parse_ini("# note\n[a]\nx = 1\n\n; other\n[b]\ny=2\n")
    assert parsed == {"a": {"x": "1"}, "b": {"y": "2"}}


def test_render_round_trips():
    sections = {"a": {"x": "1"}, "b": {"y": "2"}}
    assert cf.parse_ini(cf.render_ini(sections)) == sections


def test_merge_keeps_unknown_keys_and_overrides_known_ones(tmp_path):
    target = tmp_path / "emu.cfg"
    target.write_text("[config]\nDreamcast.Region = 0\nrend.MaxThreads = 3\n")
    assert cf.main(["--config-dir", str(tmp_path)]) == 0
    merged = cf.parse_ini(target.read_text())
    assert merged["config"]["rend.MaxThreads"] == "3"  # untouched
    assert merged["config"]["Dreamcast.Region"] == "1"  # overridden
    assert merged["input"]["device2"] == "0"  # player 2 controller added
    assert merged["input"]["maple_sdl_joystick_1"] == "1"  # pad 2 -> port B
    assert (tmp_path / "emu.cfg.bak").exists()


def test_creates_the_file_when_flycast_has_never_run(tmp_path):
    target = tmp_path / "sub" / "emu.cfg"
    assert cf.main(["--config-dir", str(tmp_path / "sub")]) == 0
    assert cf.parse_ini(target.read_text())["window"]["fullscreen"] == "yes"


def test_dry_run_writes_nothing(tmp_path):
    assert cf.main(["--config-dir", str(tmp_path), "--dry-run"]) == 0
    assert not (tmp_path / "emu.cfg").exists()


def test_second_run_is_a_no_op(tmp_path, capsys):
    cf.main(["--config-dir", str(tmp_path)])
    capsys.readouterr()
    cf.main(["--config-dir", str(tmp_path)])
    assert "already up to date" in capsys.readouterr().out


@pytest.mark.parametrize(
    "section,key,value",
    [
        ("input", "device1", "0"),  # port A controller
        ("input", "device2", "0"),  # port B controller
        ("input", "maple_sdl_joystick_0", "0"),
        ("window", "fullscreen", "yes"),
    ],
)
def test_template_pins_the_settings_the_two_player_setup_depends_on(section, key, value):
    template = cf.parse_ini(cf.TEMPLATE.read_text())
    assert template[section][key] == value
