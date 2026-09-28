<!-- Copied from prompts/champions-coaching-team.md section 4. Update both together. -->

## 4. Film Room: Training on Five Years of Official Match Video

### 4.1 What "training" means here

Agents can't watch video the way a person does, and nothing here changes model weights. The team trains by turning
official matches into a structured library of turn logs, decisions, and lessons that every agent studies and cites.

The first pilot (`knowledge/film/pilot-report.md`) settled where that evidence can come from:
- **Official records and writing** (agents): results, open team lists, official coverage, and players' own team reports.
- **Watch-along notes** (the Trainer): YouTube's and Twitch's terms don't allow agents to download video or pull caption
  tracks. So turn-by-turn detail from official matches comes from the Trainer watching the official video normally,
  with a viewing guide the Coach prepares.
- **Exact replay logs** (agents): Pokémon Showdown replays, for the Singles supplement and any other games played there.

### 4.2 Scope and sources

- **Window:** five years back from today, rolling forward. Currently that's September 2021 to September 2026.
- **What counts:** official Pokémon video game matches (VGC). Not the TCG, Pokémon GO, or Pokémon UNITE.
- **Where the video is:** the Play! Pokémon "Pokémon VGC Championships" YouTube playlist, `twitch.tv/pokemon`, the
  Pokémon Broadcast Hub (`pokemon.com/broadcast`), official broadcasts in other languages, and Liquipedia event pages,
  which link match videos and results.
- **What to match each game with:** official results and team lists (RK9, Victory Road, Limitless, Pikalytics), official
  event coverage (worlds.pokemon.com also serves its coverage entries as JSON), and Liquipedia through its API (set scores,
  match start times, and which video holds each match).
- Access video only in ways the hosting platform's terms allow. Keep notes, not copies of footage, and never
  republish footage.

### 4.3 Eras and how much each counts

| Era | Window | Game and gimmick | Worlds | How to use it |
|---|---|---|---|---|
| Champions | Apr 2026 → now | Champions · Mega Evolution | 2026 San Francisco | Directly applicable. Highest weight. |
| Scarlet/Violet | 2023 → May 2026 | SV · Terastallization | 2023 Yokohama, 2024 Honolulu, 2025 Anaheim | Fundamentals, and Pokémon or sets that exist in Champions. Lines that depend on Tera don't transfer unless Champions has Tera. |
| Sword/Shield | Sep 2021 → late 2022 | SwSh · Dynamax | 2022 London | Fundamentals only. Lines built on Dynamax don't transfer. |

**Optional Mega-era archive.** VGC 2014–2016 and 2018–2019 are outside the window, but they're the only top-level
play with Mega Evolution before Champions. Pull a small, targeted set of those matches for Mega-specific lessons,
tagged `mega-archive`.

**The Singles gap.** Official VGC is Doubles only, and no official Singles circuit was found as of September 2026
(the Scout re-checks every season). The official video teaches Doubles directly, but for Singles it only teaches the
fundamentals that carry over. So the Scout also builds a **Singles supplement** from the best non-official material,
clearly labeled: high-rated Pokémon Showdown replays in the Champions Singles format (`gen9championsbssreg<set>`, for
example `gen9championsbssregmc`), Smogon BSS tournament replays and the Champions BSS thread, and videos from top Singles
ladder players in English and Japanese. Replays are the most accurate source here because they log every turn exactly.

### 4.4 Ingestion order and coverage targets

1. **Champions era:** every official featured match in the Masters division (Regionals, Internationals, Worlds
   2026). Target: finished before the Trainer switches to Doubles.
2. **Worlds 2022–2025:** Masters top cut.
3. **International Championships 2022–2026** (North America, Europe, Latin America, Oceania): Masters top cut.
4. **Other official events:** featured matches from Regionals and national championships such as the Pokémon Japan
   Championships.
5. **Long tail:** Swiss-round featured matches, other age divisions, and broadcasts in other languages.

Every game gets a text-first record in this order. The Trainer's watch-along time is the real bottleneck, so it goes to
Champions-era top-cut games first, and to games that written reports say contain an instructive moment.

The Singles supplement runs alongside these and takes priority while the Trainer is in the Singles phase.

Track each match's status in `catalog.csv` (`queued → draft-text → draft → verified`).

### 4.5 Pipeline (per game)

**Official matches**
1. **Catalog:** event, date, era, regulation or season, division, round, players, winner, the video link with a start
   timestamp, and links to results and team lists.
2. **Teams:** attach both players' published team lists. If none exist, rebuild the teams and mark them
   `[reconstructed]`, saying from what.
3. **Text harvest:** official coverage and recaps first, then players' own reports (read in the original language), then
   press for context. Tag every line `[report]` with its citation. Check again for new reports 2 and 4 weeks after the
   event. Result: `status: draft-text`.
4. **Watch-along (optional, human):** the Coach writes a viewing guide from `knowledge/film/_TEMPLATE-viewing-guide.md`.
   The Trainer watches the official video normally, pauses where the guide says, predicts, and logs what happened with
   the video time. The Coach merges the notes as `[watch]` lines (`[commentary]` for what the casters said) and turns the
   pause points into Decision Library positions. Result: `status: draft`.
5. **Quality check:** an agent re-opens every source and confirms every `[report]` line. A second human watch of at
   least 10% of `[watch]` actions must agree at least 95% of the time before a file becomes `verified`. Never invent
   turns the sources don't show.

**Replays (Singles supplement and other Showdown games)**
1. Find and fetch games with `tools/showdown_replays.py`, with at least 1 second between requests.
2. Write the match file from the exact log, and tag turn lines `[log]`. Label your analysis as analysis.
3. **Quality check:** a script confirms every turn line against the log. Then the file can be `verified`.

**Source-handling rules**
- The official record beats editorial text. When they conflict, keep both in a "Conflicts between sources" section.
- Read players' reports in the original language, and check every translated Pokémon name against the team list.
  Automatic summaries mistranslated names in the pilot.
- Search-engine answer summaries are not sources. In the pilot, they invented results.
- Don't work around pages that block automated access. List them for a human to read.
- For species, abilities, and moves in Showdown games, use Showdown's public data files
  (`play.pokemonshowdown.com/data/pokedex.json` and `moves.json`). They reflect Showdown's version of Champions, not the
  game client.

**Provenance tags**

| Tag | Meaning |
|---|---|
| `[log]` | From an exact replay log |
| `[watch]` | Seen by a human watcher in the official video (with the video time) |
| `[commentary]` | Said by the broadcast commentators, as noted by a human watcher |
| `[report]` | From writing: official coverage, a player's own report, or press. Always cited. |
| `[inferred]` | A deduction. State the basis. |
| `[reconstructed]` | Rebuilt without an official team list. Say from what. |

**Match file schema** (`knowledge/film/matches/<event>-<division>-<round>-<p1>-vs-<p2>-g<n>.md`):

```markdown
---
event: <official event name>
date: YYYY-MM-DD
era: champions             # champions | sv | swsh | mega-archive | singles-supplement
format: <regulation set or ranked season>
mode: doubles              # singles | doubles
division: masters          # ladder, for replays
round: <e.g. Top 8, game 1 of 3>
players: [<player (country)>, <player (country)>]
winner: <player, or "Not available from permitted sources">
game_winner_basis: record  # record | report | inferred-from-set-score | unknown
series_score: <e.g. "A 2-1 B">
video: <link with start timestamp, or the replay link>
video_kind: standalone-set-upload   # standalone-set-upload | day-stream | replay
team_lists: <link>
official: true             # false for replays and other non-official games; add rating: for ladder games
status: draft-text         # draft-text | draft | verified
---
## Team Preview       both 6; what each side actually brought and led (known / inferred / not available);
                      any planned selection from a player's report, kept separate; known spreads and speeds
## Turn Log           T1: … [tag]. Moments without a known turn number go in a list: M1, M2 …
## Key Decisions      the choice, the alternatives, and the player's or commentators' reasoning
## Turning Points
## Set-level Facts    facts about the set when the game isn't known
## Conflicts Between Sources
## Lessons            each tagged: era, mode (singles-transferable | doubles-only), topic,
                      basis (observed | player-plan | set-level)
## Open Items         what a watch-along should confirm
```

**Decision Library position** (`knowledge/film/positions/`): the source match and turn, the mode tag, a difficulty
rating, the board state (only what the deciding player could see: Pokémon, HP, known sets, field conditions, what each
side has revealed), and the question "what would you click?" The answer is kept in its own section and shown only after
the Trainer answers: the player's play, their or the commentators' reasoning, and what happened.

### 4.6 What each agent learns from the film

| Agent | Studies | Produces |
|---|---|---|
| Scout | Every match file | Player habits with counts in the dossiers, event summaries, `meta-cycles.md` |
| Coach | Key decisions and turning points | `lessons.md`, the Decision Library, viewing guides, film study matched to the Trainer's weaknesses |
| Lab | Meta changes over time, upsets, forgotten tech | `upsets.md`, forecasts, hypotheses built on ideas that worked before |

Each entry in `lessons.md` needs at least two supporting matches, and at least one of them must have basis `observed`,
so a player's plan never counts as evidence on its own.

Set aside 10% of positions in `positions-heldout/`, with the answer key in a separate file. They're never used in
lessons or drills. They exist only to test whether the film study is working (Phase 8).

### 4.7 Keeping it current

After each official event, the Scout catalogs its videos within 7 days and writes text-first records in priority order.
It checks again for players' reports 2 and 4 weeks after the event. As the window moves forward, matches older than five
years move to an archive with lower weight. They aren't deleted.
