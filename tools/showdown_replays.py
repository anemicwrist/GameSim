#!/usr/bin/env python3
"""Search, download and read Pokémon Showdown replays for Singles film study ([Gen 9 Champions] BSS).

Usage:
  python3 tools/showdown_replays.py search <format> [--sort rating] [--pages N]
  python3 tools/showdown_replays.py fetch <replay-id> [<replay-id> ...] [--dir replays] [--force]
  python3 tools/showdown_replays.py board <replay-id | path/to/replay.json> [--dir replays] [--turns 3,7-9]
                                          [--no-events]

Examples:
  python3 tools/showdown_replays.py search gen9championsbssregmc --sort rating --pages 2
  python3 tools/showdown_replays.py fetch gen9championsbssregmc-2688811994
  python3 tools/showdown_replays.py board gen9championsbssregmc-2688811994 --turns 7

search  Lists a format's public replays from replay.pokemonshowdown.com/search.json: id, rating, upload time (UTC)
        and players. Newest first by default; --sort rating lists the highest rated first. A page is ~50 replays.
fetch   Saves replay.pokemonshowdown.com/<id>.json as <dir>/<id>.json. The default dir is replays/, relative to
        where you run the tool (run it from the repo root; replays/ is git-ignored). Existing files are kept unless
        you pass --force. Replay URLs are accepted in place of ids.
board   Prints the players and pre-game Elo, replay rating, rules, Team Preview, picks and leads, Mega Evolutions,
        the result and rating changes. Then, for every turn, it prints the public board at the start of that turn:
        HP %, status, stat boosts and volatile effects of the active Pokémon, side conditions and weather/terrain
        with the turn they started, and every move, item and ability revealed so far. Each turn's events follow its
        board. Given a replay id, it reads <dir>/<id>.json and downloads the file first if it's missing.

Being gentle with the server: every HTTP request starts at least 1 s after the previous one, including requests
made by earlier runs (a timestamp file in the system temp folder is shared between runs), and each request sends a
descriptive User-Agent. Python 3 standard library only.

Reading the output:
- Everything comes from the replay log, which is the spectator view. HP is the log's percentage, and a turn's board
  shows only what both players could see at that moment. Nothing is inferred. Deductions such as "the screen lasted
  8 turns, so Light Clay" are left to the analyst.
- "T0" means before turn 1 (lead switch-ins). Showdown's replay rating has matched the lower of the two post-game
  Elos in every game checked so far.
- In Champions logs, effectiveness messages carry a doubling count. It's printed here as 2x/4x or 0.5x/0.25x.
- Showdown games are non-official: they aren't Pokémon Champions in-game ranked, and ladder players aren't pros.
"""
import argparse
import json
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    import fcntl  # POSIX only: lets concurrent runs queue for the shared request timestamp
except ImportError:
    fcntl = None

BASE = "https://replay.pokemonshowdown.com"
USER_AGENT = "GameSim-ShowdownReplays/1.0 (Pokemon Champions film-study tool; Python urllib; at most 1 request/s)"
MIN_INTERVAL = 1.0  # seconds between the end of one request and the start of the next
STAMP_FILE = Path(tempfile.gettempdir()) / "showdown_replays.last_request"
_last_request = 0.0

STAT = {"atk": "Atk", "def": "Def", "spa": "SpA", "spd": "SpD", "spe": "Spe", "accuracy": "Acc", "evasion": "Eva"}
STATUS = {"brn": "burned", "par": "paralyzed", "psn": "poisoned", "tox": "badly poisoned", "slp": "asleep",
          "frz": "frozen"}
WEATHER = {"RainDance": "Rain", "SunnyDay": "Sun", "Sandstorm": "Sand", "Snowscape": "Snow", "Snow": "Snow",
           "Hail": "Hail", "DesolateLand": "Harsh sun", "PrimordialSea": "Heavy rain", "DeltaStream": "Strong winds"}
TRAPS = {"Bind", "Wrap", "Fire Spin", "Whirlpool", "Sand Tomb", "Clamp", "Magma Storm", "Infestation", "Snap Trap",
         "Thunder Cage"}


# ---------------------------------------------------------------- HTTP

def http_get_json(url):
    """GET url and parse the JSON, starting at least MIN_INTERVAL seconds after this tool's previous request."""
    global _last_request
    stamp, last = None, _last_request
    try:
        stamp = open(STAMP_FILE, "a+")
        if fcntl:
            fcntl.flock(stamp, fcntl.LOCK_EX)
        stamp.seek(0)
        last = max(last, float(stamp.read().strip() or 0))
    except (OSError, ValueError):
        pass  # no shared timestamp available: fall back to this run's own clock
    try:
        wait = last + MIN_INTERVAL - time.time()
        if wait > 0:
            time.sleep(wait)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    finally:
        _last_request = time.time()
        if stamp:
            try:
                stamp.seek(0)
                stamp.truncate()
                stamp.write(f"{_last_request:.3f}")
            except OSError:
                pass
            stamp.close()  # also releases the lock
    return json.loads(body[1:] if body.startswith("]") else body)


def utc(timestamp):
    return datetime.fromtimestamp(int(timestamp), timezone.utc).strftime("%Y-%m-%d %H:%M") if timestamp else "?"


def replay_id(text):
    """Accept an id or a replay URL; return the id."""
    rid = re.sub(r"^https?://replay\.pokemonshowdown\.com/", "", text.strip()).split("?")[0]
    rid = re.sub(r"\.(json|log)$", "", rid)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", rid):
        sys.exit(f"error: not a replay id or replay URL: {text!r}")
    return rid


def fetch(rid, folder, force=False):
    """Download <rid>.json into folder unless it's already there. Returns (path, downloaded)."""
    path = Path(folder) / f"{rid}.json"
    if path.exists() and not force:
        return path, False
    data = http_get_json(f"{BASE}/{rid}.json")
    if "log" not in data:
        sys.exit(f"error: {rid}: the response has no battle log")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return path, True


# ---------------------------------------------------------------- commands

def cmd_search(args):
    rows, seen, before, more = [], set(), None, False
    for page in range(1, args.pages + 1):
        params = {"format": args.format}
        if args.sort == "rating":
            params.update(sort="rating", page=page)
        elif before:
            params["before"] = before
        batch = http_get_json(f"{BASE}/search.json?{urllib.parse.urlencode(params)}")
        fresh = [r for r in batch if r["id"] not in seen]
        seen.update(r["id"] for r in fresh)
        rows += fresh
        more = len(batch) > 50  # the server sends a 51st result when another page exists
        if not more or not fresh:
            break
        # 'before' is exclusive, so +1 re-reads replays sharing the last timestamp; the duplicates are dropped above
        before = min(r["uploadtime"] for r in batch) + 1
    if not rows:
        print(f"no public replays found for format {args.format!r}")
        return
    width = max(len(r["id"]) for r in rows)
    print(f"{'id':<{width}}  {'rating':>6}  {'uploaded (UTC)':<16}  players")
    for r in rows:
        players = " vs ".join(r.get("players") or [])
        print(f"{r['id']:<{width}}  {r.get('rating') or '-'!s:>6}  {utc(r.get('uploadtime')):<16}  {players}")
    print(f"{len(rows)} replays" + (f"; more available (try --pages {args.pages + 1})" if more else ""))


def cmd_fetch(args):
    failed = 0
    for text in args.ids:
        rid = replay_id(text)
        try:
            path, downloaded = fetch(rid, args.dir, args.force)
        except urllib.error.HTTPError as err:
            failed += 1
            print(f"error: {rid}: HTTP {err.code}{' (no such public replay)' if err.code == 404 else ''}",
                  file=sys.stderr)
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        print(f"{'saved' if downloaded else 'already had'} {path}  "
              f"({' vs '.join(data.get('players') or [])}, rating {data.get('rating') or '-'})")
    if failed:
        sys.exit(1)


def cmd_board(args):
    path = Path(args.replay)
    if not path.is_file():
        if args.replay.endswith(".json") and not args.replay.startswith("http"):
            sys.exit(f"error: no such file: {args.replay}")
        path, downloaded = fetch(replay_id(args.replay), args.dir)
        if downloaded:
            print(f"(downloaded {path})", file=sys.stderr)
    battle = Battle(json.loads(path.read_text(encoding="utf-8"))).run()
    print(battle.report(args.turns, not args.no_events))


# ---------------------------------------------------------------- battle-log state tracker

def split_tags(args):
    """Separate positional protocol arguments from [tag] arguments such as '[from] item: Life Orb'."""
    plain, tags = [], {}
    for arg in args:
        match = re.match(r"\[(\w+)\]\s*(.*)$", arg)
        if match:
            tags[match.group(1)] = match.group(2)
        else:
            plain.append(arg)
    return plain, tags


def parse_hp(text):
    """'58/100' -> (58, ''), '93/100 brn' -> (93, 'brn'), '0 fnt' -> (0, 'fnt'). Ignores stray characters."""
    value, _, status = text.strip().partition(" ")
    if "/" in value:
        num, den = (int(re.sub(r"\D", "", part) or 0) for part in value.split("/", 1))
        return (round(100 * num / den) if den else 0), status
    return int(re.sub(r"\D", "", value) or 0), status


def same_species(preview, species):
    return preview == species or (preview.endswith("-*") and species.startswith(preview[:-1]))


class Mon:
    def __init__(self, species):
        self.species = self.forme = species
        self.hp, self.status, self.fainted = 100, "", False
        self.item = self.item_note = self.ability = None
        self.moves = []


class Side:
    def __init__(self, sid):
        self.sid, self.name, self.elo, self.teamsize = sid, sid, None, None
        self.preview, self.mons, self.active = [], {}, None  # mons: nickname -> Mon, in order of appearance
        self.boosts, self.volatiles, self.conditions = {}, {}, {}  # conditions: name -> [turn set, layers]
        self.mega = None  # (species, Mega forme, stone, turn)


class Battle:
    def __init__(self, replay):
        self.replay = replay
        self.sides = {"p1": Side("p1"), "p2": Side("p2")}
        self.turn, self.weather, self.field = 0, None, {}
        self.tier, self.gametype = replay.get("format", "?"), "singles"
        self.rules, self.times, self.notes, self.ratings = [], [], [], []
        self.winner, self.frames, self.final = None, [], ""

    def run(self):
        frame = [0, "", []]  # [turn, board at the start of the turn, events during the turn]
        self.frames.append(frame)
        for line in self.replay.get("log", "").split("\n"):
            parts = line.split("|")
            if len(parts) < 2 or not parts[1]:
                continue
            if parts[1] == "turn":
                self.turn = int(parts[2])
                frame = [self.turn, self.render(), []]
                self.frames.append(frame)
                continue
            event = self.apply(parts[1], parts[2:])
            if event:
                frame[2].append(event)
        self.final = self.render()
        return self

    def ident(self, text):
        """'p1a: Nick' -> (Side, Mon or None). Also accepts 'p1: Name' (a side)."""
        sid, _, nick = text.partition(": ")
        side = self.sides.get(sid[:2])
        return side, (side.mons.get(nick) if side else None)

    def label(self, text):
        side, mon = self.ident(text)
        return f"{side.sid} {mon.forme}" if mon else text

    def reveal(self, target, tags):
        """Record the item or ability named in '[from] item: X' / '[from] ability: X'. The holder is [of] if given."""
        source = tags.get("from", "")
        if not source.startswith(("item: ", "ability: ")):
            return
        holder = self.ident(tags["of"])[1] if tags.get("of") else target
        if holder is None:
            return
        if source.startswith("item: "):
            holder.item = source[len("item: "):]
        else:
            holder.ability = source[len("ability: "):]

    def switch(self, kind, plain):
        side_id, _, nick = plain[0].partition(": ")
        side = self.sides[side_id[:2]]
        species = plain[1].split(",")[0]
        mon = side.mons.setdefault(nick, Mon(species))
        mon.forme = species
        if len(plain) > 2:
            mon.hp, status = parse_hp(plain[2])
            mon.status = "" if status == "fnt" else status
        side.active = nick
        if kind == "replace":  # an Illusion broke: the active Pokémon is really this one
            return f"{side.sid} {species} was hidden by Illusion"
        side.boosts, side.volatiles = {}, {}
        return f"{side.sid} {'dragged in' if kind == 'drag' else 'in'}: {species} {mon.hp}%"

    def apply(self, kind, args):
        """Update the state for one protocol line. Returns a short event description, or None."""
        plain, tags = split_tags(args)
        if kind == "player" and len(plain) > 1 and plain[1]:
            side = self.sides[plain[0]]
            side.name = plain[1]
            if len(plain) > 3 and plain[3]:
                side.elo = plain[3]
        elif kind == "poke":
            self.sides[plain[0]].preview.append(plain[1].split(",")[0])
        elif kind == "teamsize":
            self.sides[plain[0]].teamsize = int(plain[1])
        elif kind == "rule":
            self.rules.append(plain[0].split(":")[0])
        elif kind == "tier":
            self.tier = plain[0]
        elif kind == "gametype":
            self.gametype = plain[0]
        elif kind == "t:":
            self.times.append(int(plain[0]))
        elif kind in ("switch", "drag", "replace"):
            return self.switch(kind, plain)
        elif kind in ("detailschange", "-formechange"):
            _, mon = self.ident(plain[0])
            if mon:
                mon.forme = plain[1].split(",")[0]
        elif kind == "-mega":
            side, mon = self.ident(plain[0])
            if mon is None:
                return None
            if len(plain) > 2:
                mon.item, mon.item_note = plain[2], None
            side.mega = (mon.species, mon.forme, mon.item, self.turn)
            return f"{side.sid} {mon.species} Mega Evolves into {mon.forme} ({mon.item})"
        elif kind == "move":
            side, mon = self.ident(plain[0])
            if mon is None:
                return None
            if "from" not in tags and plain[1] not in mon.moves:
                mon.moves.append(plain[1])
            target = self.ident(plain[2])[1] if len(plain) > 2 and plain[2] else None
            text = f"{side.sid} {mon.forme}: {plain[1]}"
            if target and target is not mon:
                text += f" -> {target.forme}"
            if "miss" in tags:
                text += " (missed)"
            if tags.get("from"):
                text += f" [via {tags['from']}]"
            return text
        elif kind in ("-damage", "-heal", "-sethp"):
            _, mon = self.ident(plain[0])
            if mon is None:
                return None
            mon.hp, status = parse_hp(plain[1])
            mon.status = "" if status == "fnt" else status
            self.reveal(mon, tags)
            source = tags.get("from", "")
            return f"{self.label(plain[0])} {'0% (fainting)' if status == 'fnt' else f'{mon.hp}%'}" + \
                (f" [{source}]" if source else "")
        elif kind == "-status":
            _, mon = self.ident(plain[0])
            if mon is None:
                return None
            mon.status = plain[1]
            self.reveal(mon, tags)
            return f"{self.label(plain[0])} {STATUS.get(plain[1], plain[1])}"
        elif kind == "-curestatus":
            _, mon = self.ident(plain[0])
            if mon:
                mon.status = ""
            return f"{self.label(plain[0])} cured of {STATUS.get(plain[1], plain[1])}"
        elif kind == "-cureteam":
            side, _ = self.ident(plain[0])
            for mon in side.mons.values():
                mon.status = ""
            return f"{side.sid} team cured"
        elif kind in ("-boost", "-unboost"):
            side, _ = self.ident(plain[0])
            change = int(plain[2]) * (1 if kind == "-boost" else -1)
            side.boosts[plain[1]] = max(-6, min(6, side.boosts.get(plain[1], 0) + change))
            return f"{self.label(plain[0])} {STAT.get(plain[1], plain[1])} {change:+d}"
        elif kind == "-setboost":
            side, _ = self.ident(plain[0])
            side.boosts[plain[1]] = int(plain[2])
            return f"{self.label(plain[0])} {STAT.get(plain[1], plain[1])} set to {int(plain[2]):+d}"
        elif kind == "-clearallboost":
            for side in self.sides.values():
                side.boosts = {}
            return "all stat changes cleared"
        elif kind in ("-clearboost", "-clearnegativeboost", "-clearpositiveboost", "-invertboost"):
            side, _ = self.ident(plain[0])
            keep = {"-clearboost": lambda v: False, "-clearnegativeboost": lambda v: v > 0,
                    "-clearpositiveboost": lambda v: v < 0, "-invertboost": lambda v: True}[kind]
            sign = -1 if kind == "-invertboost" else 1
            side.boosts = {stat: sign * v for stat, v in side.boosts.items() if keep(v)}
            return f"{self.label(plain[0])}: {kind[1:]}"
        elif kind == "-copyboost":  # plain[0] copies plain[1]'s stat changes (Psych Up)
            user, _ = self.ident(plain[0])
            user.boosts = dict(self.ident(plain[1])[0].boosts)
            return f"{self.label(plain[0])} copied {self.label(plain[1])}'s stat changes"
        elif kind == "-swapboost":
            one, _ = self.ident(plain[0])
            two, _ = self.ident(plain[1])
            for stat in (plain[2].split(", ") if len(plain) > 2 and plain[2] else list(STAT)):
                one.boosts[stat], two.boosts[stat] = two.boosts.get(stat, 0), one.boosts.get(stat, 0)
            return f"{self.label(plain[0])} and {self.label(plain[1])} swapped stat changes"
        elif kind in ("-sidestart", "-sideend"):
            side = self.sides[plain[0][:2]]
            condition = plain[1].replace("move: ", "")
            if kind == "-sidestart":
                side.conditions.setdefault(condition, [self.turn, 0])[1] += 1
                self.reveal(None, tags)
            else:
                side.conditions.pop(condition, None)
            return f"{side.sid} side {'+' if kind == '-sidestart' else '-'}{condition}"
        elif kind == "-swapsideconditions":
            one, two = self.sides["p1"], self.sides["p2"]
            one.conditions, two.conditions = two.conditions, one.conditions
            return "side conditions swapped"
        elif kind == "-weather":
            if "upkeep" in tags:
                return None
            if plain[0] == "none":
                self.weather = None
                return "weather ended"
            self.reveal(None, tags)
            source = tags.get("from", "").replace("ability: ", "")
            self.weather = (WEATHER.get(plain[0], plain[0]), self.turn, source)
            return f"weather: {self.weather[0]}" + (f" [{source}]" if source else "")
        elif kind in ("-fieldstart", "-fieldend"):
            name = plain[0].replace("move: ", "")
            if kind == "-fieldend":
                self.field.pop(name, None)
                return f"field -{name}"
            if name.endswith("Terrain"):  # a new terrain replaces the old one
                self.field = {k: v for k, v in self.field.items() if not k.endswith("Terrain")}
            self.field[name] = self.turn
            self.reveal(None, tags)
            return f"field +{name}"
        elif kind == "-item":
            _, mon = self.ident(plain[0])
            if mon is None:
                return None
            mon.item, mon.item_note = plain[1], None
            self.reveal(None, tags)
            return f"{self.label(plain[0])} holds {plain[1]}" + (f" [{tags['from']}]" if tags.get("from") else "")
        elif kind == "-enditem":
            _, mon = self.ident(plain[0])
            if mon is None:
                return None
            source = tags.get("from", "")
            if "weaken" in tags and mon.item_note:
                return None  # second line of a resist berry that was already eaten
            if "eat" in tags:
                note = "eaten"
            elif "Knock Off" in source:
                note = "knocked off"
            elif source == "stealeat" or "Bug Bite" in source or "Pluck" in source:
                note = "eaten by the opponent"
            elif "Thief" in source or "Covet" in source:
                note = "stolen"
            else:
                note = "used"
            mon.item, mon.item_note = plain[1], note
            return f"{self.label(plain[0])}'s {plain[1]} {note}"
        elif kind == "-ability":
            _, mon = self.ident(plain[0])
            if mon:
                mon.ability = plain[1]
            return f"{self.label(plain[0])}'s {plain[1]}"
        elif kind == "-activate":
            side, mon = self.ident(plain[0])
            what = plain[1] if len(plain) > 1 else ""
            if mon:
                if what.startswith("ability: "):
                    mon.ability = what[len("ability: "):]
                elif what.startswith("item: "):
                    mon.item = what[len("item: "):]
                elif what.replace("move: ", "") in TRAPS:
                    side.volatiles[what.replace("move: ", "")] = "trapped"
            return f"{self.label(plain[0])}: {what}"
        elif kind in ("-start", "-end"):
            side, mon = self.ident(plain[0])
            effect = plain[1].replace("move: ", "").replace("ability: ", "") if len(plain) > 1 else ""
            detail = plain[2] if len(plain) > 2 else ""
            if mon and nick_of(side, mon) == side.active:
                if kind == "-start":
                    side.volatiles[effect] = detail
                else:
                    side.volatiles.pop(effect, None)
            self.reveal(mon, tags)
            if "silent" in tags:
                return None
            sign = "+" if kind == "-start" else "-"
            return f"{self.label(plain[0])} {sign}{effect}" + (f" {detail}" if detail else "")
        elif kind == "faint":
            side, mon = self.ident(plain[0])
            if mon is None:
                return None
            mon.fainted, mon.hp = True, 0
            return f"{side.sid} {mon.forme} fainted"
        elif kind == "cant":
            return f"{self.label(plain[0])} can't move ({plain[1] if len(plain) > 1 else '?'})"
        elif kind in ("-supereffective", "-resisted"):
            count = int(plain[1]) if len(plain) > 1 and plain[1].isdigit() else 0
            if kind == "-supereffective":
                return "super effective" + (f" ({2 ** count}x)" if count else "")
            return "resisted" + (f" ({0.5 ** count:g}x)" if count else "")
        elif kind == "-immune":
            _, mon = self.ident(plain[0])
            self.reveal(mon, tags)
            return f"{self.label(plain[0])} is immune" + (f" [{tags['from']}]" if tags.get("from") else "")
        elif kind == "-crit":
            return "critical hit"
        elif kind == "-miss":
            return "missed"
        elif kind == "-fail":
            return f"{self.label(plain[0])}: it failed" + (f" ({plain[1]})" if len(plain) > 1 and plain[1] else "")
        elif kind == "-block":
            return f"{self.label(plain[0])} blocked it ({plain[1] if len(plain) > 1 else '?'})"
        elif kind == "-hitcount":
            return f"hit {plain[1]} times"
        elif kind == "-prepare":
            return f"{self.label(plain[0])} charges {plain[1]}"
        elif kind == "-singleturn":
            return f"{self.label(plain[0])}: {plain[1].replace('move: ', '')}"
        elif kind == "-transform":
            return f"{self.label(plain[0])} transformed into {self.label(plain[1])}"
        elif kind == "-terastallize":
            return f"{self.label(plain[0])} Terastallized ({plain[1]})"
        elif kind == "-message":
            self.notes.append(plain[0])
            return plain[0]
        elif kind == "inactive":
            text = plain[0] if plain else ""
            left = re.search(r"has (\d+) seconds left", text)
            if left and int(left.group(1)) <= 30:
                return f"[timer] {text}"
            if re.search(r"lost|disconnected|forfeit", text):
                self.notes.append(text)
                return text
        elif kind == "raw":
            text = re.sub(r"<[^>]+>", "", plain[0]).replace("&rarr;", "->") if plain else ""
            if "rating:" in text:
                self.ratings.append(re.sub(r"\s*\(", " (", text))
        elif kind == "win":
            self.winner = plain[0]
            return f"{plain[0]} wins"
        elif kind == "tie":
            self.winner = "tie"
            return "tie"
        return None

    # ------------------------------------------------------------ output

    def render(self):
        """The public board right now."""
        if self.weather:
            name, turn, source = self.weather
            weather = f"{name} (since T{turn}" + (f", {source})" if source else ")")
        else:
            weather = "none"
        field = ", ".join(f"{name} (since T{turn})" for name, turn in self.field.items()) or "none"
        lines = [f"  weather: {weather}; terrain/rooms: {field}"]
        for side in self.sides.values():
            conditions = ", ".join(f"{name}{f' x{layers}' if layers > 1 else ''} (since T{turn})"
                                   for name, (turn, layers) in side.conditions.items()) or "none"
            mega = f"used ({side.mega[0]}, T{side.mega[3]})" if side.mega else "not used"
            lines.append(f"  {side.sid} {side.name} | Mega: {mega} | side conditions: {conditions}")
            for nick, mon in side.mons.items():
                active = nick == side.active and not mon.fainted
                cells = [f"{'>' if active else ' '} {mon.forme:<18} {'FNT' if mon.fainted else f'{mon.hp}%':>4}"]
                if mon.status:
                    cells.append(mon.status.upper())
                if active:
                    boosts = " ".join(f"{STAT.get(k, k)} {v:+d}" for k, v in side.boosts.items() if v)
                    effects = ", ".join(f"{k} {v}".strip() for k, v in side.volatiles.items())
                    cells += [f"[{boosts}]"] if boosts else []
                    cells += [f"{{{effects}}}"] if effects else []
                item = (mon.item or "?") + (f" ({mon.item_note})" if mon.item_note else "")
                cells.append(f"item: {item} | ability: {mon.ability or '?'} | moves: {', '.join(mon.moves) or '-'}")
                lines.append("    " + "  ".join(cells))
            unseen = [p for p in side.preview if not any(same_species(p, m.species) for m in side.mons.values())]
            missing = side.teamsize - len(side.mons) if side.teamsize else len(unseen)
            if missing > 0 and unseen:
                lines.append(f"      not seen yet: {missing} of {', '.join(unseen)}")
        return "\n".join(lines)

    def report(self, turns=None, events=True):
        rid = self.replay.get("id", "?")
        out = [f"{rid} (Pokémon Showdown replay, non-official)", f"  {BASE}/{rid}",
               f"  format: {self.tier}" + (f"; rules: {', '.join(self.rules)}" if self.rules else "")]
        if self.gametype != "singles":
            out.append(f"  warning: this is a {self.gametype} game; the board is built for singles")
        played = utc(self.times[0]) if self.times else "?"
        length = self.times[-1] - self.times[0] if len(self.times) > 1 else None
        out.append(f"  played {played} UTC" + (f" ({length // 60} min {length % 60:02d} s)" if length else "") +
                   f"; uploaded {utc(self.replay.get('uploadtime'))} UTC; replay rating "
                   f"{self.replay.get('rating') or '-'}")
        for side in self.sides.values():
            out.append(f"  {side.sid}: {side.name}" + (f" (pre-game Elo {side.elo})" if side.elo else ""))

        out.append("\nTEAM PREVIEW")
        for side in self.sides.values():
            out.append(f"  {side.sid} {side.name}: {', '.join(side.preview) or '(no Team Preview in this log)'}")
        out.append("PICKS (in order of appearance) AND LEADS")
        for side in self.sides.values():
            picks = [m.species for m in side.mons.values()]
            text = ", ".join(f"{name} (lead)" if i == 0 else name for i, name in enumerate(picks)) or "-"
            if side.teamsize and side.teamsize > len(picks):
                text += f", + {side.teamsize - len(picks)} never shown"
            out.append(f"  {side.sid} {side.name}: {text}")
        out.append("MEGA EVOLUTION")
        for side in self.sides.values():
            mega = side.mega
            out.append(f"  {side.sid} {side.name}: " +
                       (f"{mega[0]} -> {mega[1]} ({mega[2]}) on T{mega[3]}" if mega else "none"))
        out.append("RESULT")
        if self.winner:
            out.append(f"  {'tie' if self.winner == 'tie' else self.winner + ' won'} after {self.turn} turns")
        else:
            out.append(f"  no winner in the log (it stops at turn {self.turn})")
        out += [f"  {note}" for note in self.notes]
        out += [f"  {rating}" for rating in self.ratings]

        for turn, board, happened in self.frames:
            if turns and turn not in turns:
                continue
            if turn == 0:
                if events:
                    out.append(f"\nLEADS (T0): {'; '.join(happened)}")
                continue
            out.append(f"\n=== T{turn}: board at the start of turn {turn} ===\n{board}")
            if events:
                out.append(f"  events T{turn}: {'; '.join(happened) or '-'}")
        if not turns:
            out.append(f"\n=== END: board after the last turn ===\n{self.final}")
        return "\n".join(out)


def nick_of(side, mon):
    return next((nick for nick, m in side.mons.items() if m is mon), None)


def parse_turns(text):
    """'3,7-9' -> {3, 7, 8, 9}"""
    turns = set()
    for chunk in text.split(","):
        start, _, end = chunk.strip().partition("-")
        turns.update(range(int(start), int(end or start) + 1))
    return turns


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search", help="list public replays of a format")
    search.add_argument("format", help="format id, e.g. gen9championsbssregmc")
    search.add_argument("--sort", choices=["date", "rating"], default="date", help="default: newest first")
    search.add_argument("--pages", type=int, default=1, help="pages of about 50 replays to read (default 1)")
    fetch_cmd = commands.add_parser("fetch", help="download replay JSON files")
    fetch_cmd.add_argument("ids", nargs="+", metavar="replay-id", help="replay id or replay URL")
    fetch_cmd.add_argument("--dir", default="replays", help="folder to save into (default: replays/)")
    fetch_cmd.add_argument("--force", action="store_true", help="download again even if the file exists")
    board = commands.add_parser("board", help="Team Preview, picks, Megas, result and the board at every turn")
    board.add_argument("replay", metavar="replay-id-or-json-path")
    board.add_argument("--dir", default="replays", help="where replay files are read and saved (default: replays/)")
    board.add_argument("--turns", type=parse_turns, help="only show these turns, e.g. 3,7-9")
    board.add_argument("--no-events", action="store_true", help="leave out each turn's events")
    args = parser.parse_args()
    if args.command == "search" and args.pages < 1:
        parser.error("--pages must be at least 1")
    try:
        {"search": cmd_search, "fetch": cmd_fetch, "board": cmd_board}[args.command](args)
    except urllib.error.HTTPError as err:
        sys.exit(f"error: HTTP {err.code} for {err.url}")
    except urllib.error.URLError as err:
        sys.exit(f"error: could not reach {BASE}: {err.reason}")


if __name__ == "__main__":
    main()
