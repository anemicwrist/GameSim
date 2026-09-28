<!-- Copied from prompts/champions-coaching-team.md section 4. Update both together. -->

## 4. Film Room: Training on Five Years of Official Match Video

### 4.1 What "training" means here

Agents can't watch video the way a person does, and nothing here changes model weights. The team trains by turning
official match video into a structured library of turn logs, decisions, and lessons that every agent studies and
cites. The evidence comes from three places: caption tracks (the commentary), frames sampled from the video, and
official team lists and results.

### 4.2 Scope and sources

- **Window:** five years back from today, rolling forward. Currently that's September 2021 to September 2026.
- **What counts:** official Pokémon video game matches (VGC). Not the TCG, Pokémon GO, or Pokémon UNITE.
- **Where the video is:** the Play! Pokémon "Pokémon VGC Championships" YouTube playlist, `twitch.tv/pokemon`, the
  Pokémon Broadcast Hub (`pokemon.com/broadcast`), official broadcasts in other languages, and Liquipedia event pages,
  which link match videos and results.
- **What to match each game with:** official results and team lists from RK9, Victory Road, Limitless, and Pikalytics.
- Access video only in ways the hosting platform's terms allow. Keep notes, not copies of footage, and never
  republish footage.

### 4.3 Eras and how much each counts

| Era | Window | Game and gimmick | Worlds | How to use it |
|---|---|---|---|---|
| Champions | May 2026 → now | Champions · Mega Evolution | 2026 San Francisco | Directly applicable. Highest weight. |
| Scarlet/Violet | 2023 → May 2026 | SV · Terastallization | 2023 Yokohama, 2024 Honolulu, 2025 Anaheim | Fundamentals, and Pokémon or sets that exist in Champions. Lines that depend on Tera don't transfer unless Champions has Tera. |
| Sword/Shield | Sep 2021 → late 2022 | SwSh · Dynamax | 2022 London | Fundamentals only. Lines built on Dynamax don't transfer. |

**Optional Mega-era archive.** VGC 2014–2016 and 2018–2019 are outside the window, but they're the only top-level
play with Mega Evolution before Champions. Pull a small, targeted set of those matches for Mega-specific lessons,
tagged `mega-archive`.

**The Singles gap.** Official VGC is Doubles only, and no official Singles circuit was found as of September 2026
(the Scout re-checks every season). The official video teaches Doubles directly, but for Singles it only teaches the
fundamentals that carry over. So the Scout also builds a **Singles supplement** from the best non-official material,
clearly labeled: Smogon BSS tournament replays and the Champions BSS thread, Showdown replays of Champions singles
formats, and videos from top Singles ladder players in English and Japanese. Text replays are the most accurate
source here because they log every turn exactly.

### 4.4 Ingestion order and coverage targets

1. **Champions era:** every official featured match in the Masters division (Regionals, Internationals, Worlds
   2026). Target: finished before the Trainer switches to Doubles.
2. **Worlds 2022–2025:** Masters top cut.
3. **International Championships 2022–2026** (North America, Europe, Latin America, Oceania): Masters top cut.
4. **Other official events:** featured matches from Regionals and national championships such as the Pokémon Japan
   Championships.
5. **Long tail:** Swiss-round featured matches, other age divisions, and broadcasts in other languages.

The Singles supplement runs alongside these and takes priority while the Trainer is in the Singles phase.

Five years of broadcasts is thousands of hours. Work in priority order, use helper sub-agents in parallel, and track
each match's status in `catalog.csv` (`queued → extracted → verified`).

### 4.5 Pipeline (per game)

1. **Catalog:** event, date, era, regulation or season, division, round, players, winner, the video link with a start
   timestamp, and links to results and team lists.
2. **Teams:** attach both players' published team lists. If none exist, rebuild the teams from the video and mark them
   `[reconstructed]`.
3. **Commentary:** get the caption track, fix garbled Pokémon and move names against the legal list, and line it up
   with the turns.
4. **Visuals** (priority 1–2 matches): sample frames at each turn and read the battle screen (moves, HP, switches,
   field effects) with a vision-capable model.
5. **Write the match file** (schema below). Tag every turn line with where it came from: `[video]`,
   `[commentary]`, or `[inferred]`.
6. **Quality check:** a second agent re-checks at least 10% of turns against the video. Mark the file `verified`
   only when at least 95% of actions agree. Otherwise, fix it and check again. Never invent turns the sources don't
   show.

**Match file schema** (`knowledge/film/matches/<event>-<division>-<round>-<p1>-vs-<p2>-g<n>.md`):

```markdown
---
event: <official event name>
date: YYYY-MM-DD
era: champions            # champions | sv | swsh | mega-archive | singles-supplement
format: <regulation set or ranked season>
mode: doubles             # singles | doubles
division: masters
round: <e.g. Top 8, game 1 of 3>
players: [<player (country)>, <player (country)>]
winner: <player>
video: <link with start timestamp>
team_lists: <link>
status: draft             # draft | verified
---
## Team Preview    both 6, what each side picked, leads, each side's likely win condition
## Turn Log        T1: … [video] / [commentary] / [inferred]
## Key Decisions   the choice, the alternatives, and the commentators' reasoning
## Turning Points
## Lessons         each tagged: era, mode (singles-transferable | doubles-only), topic
```

**Decision Library position** (`knowledge/film/positions/`): the source match and turn, the mode tag, a difficulty
rating, the board state (Pokémon, HP, known sets, field conditions, what each side has revealed), and the question
"what would you click?" The answer is kept in its own section and shown only after the Trainer answers: the pro's
play, the commentators' reasoning, and what happened.

### 4.6 What each agent learns from the film

| Agent | Studies | Produces |
|---|---|---|
| Scout | Every verified match | Player habits with counts in the dossiers, event summaries, `meta-cycles.md` |
| Coach | Key decisions and turning points | `lessons.md`, the Decision Library, film study matched to the Trainer's weaknesses |
| Lab | Meta changes over time, upsets, forgotten tech | `upsets.md`, forecasts, hypotheses built on ideas that worked before |

Each entry in `lessons.md` needs at least two supporting matches and tags for era, mode, and topic.

Set aside 10% of positions in `positions-heldout/`, with the answer key in a separate file. They're never used in
lessons or drills. They exist only to test whether the film study is working (Phase 8).

### 4.7 Keeping it current

After each official event, the Scout catalogs its videos within 7 days and ingestion follows the priority order.
As the window moves forward, matches older than five years move to an archive with lower weight. They aren't
deleted.
