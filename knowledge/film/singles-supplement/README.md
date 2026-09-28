# Singles supplement: Champions BSS on Pokémon Showdown (batch 1, 2026-09-28)

> **NON-OFFICIAL MATERIAL.** Every game here is **Pokémon Showdown ladder play** in the `[Gen 9 Champions] BSS Reg M-C`
> format. It is **not** Pokémon Champions in-game ranked, and **not** a Play! Pokémon event. The players are ladder
> players, not pros: the files describe what the high-rated player did, and say so when another play looks better.
> This supplement exists because official VGC video is Doubles only (Film Room README 4.3, "The Singles gap").

## Contents

| Output | Files |
|---|---|
| 5 match files | `gen9championsbssregmc-<id>.md` in this folder |
| 8 Decision Library positions | `knowledge/film/positions/ss-gen9championsbssregmc-<id>-t<turn>.md` |
| 2 held-out positions | `knowledge/film/positions-heldout/ss-…-t<turn>.md`, answers in `positions-heldout/answer-key.md` |

## Index of games

Replay rating is Showdown's value for the game, which equals the lower of the two post-game Elos (true for all 5, from
the `|raw|` rating lines). Pre-game Elo comes from the `|player|` lines [log]. Ladder rank is from the Showdown ladder
snapshot of 2026-09-28 (Pokémon Showdown ladder, https://pokemonshowdown.com/ladder/gen9championsbssregmc.json,
accessed 2026-09-28, Tier 2).

| # | Replay | Date (UTC) | p1 (pre-game Elo) | p2 (pre-game Elo) | Replay rating | Archetypes, p1 vs p2 (brought 3) | Winner | Turns | Positions |
|---|---|---|---|---|---|---|---|---|---|
| G1 | [2688548425](https://replay.pokemonshowdown.com/gen9championsbssregmc-2688548425) | 2026-09-27 | sky2132 (1483) | Ghostofcolress (1439) | **1460** | Rain offense (Pelipper, Archaludon, Mega Golisopod) vs weather denial plus hazards (Cinderace, Ninetales-Alola with Veil, Samurott-Hisui with Sash) | Ghostofcolress | 11 | t8; t6 held out |
| G2 | [2683599297](https://replay.pokemonshowdown.com/gen9championsbssregmc-2683599297) | 2026-09-18 | Dragalge THL (1417) | mk7juju (1450) | **1428** | Screens stall (Sableye, Toxapex, Samurott-Hisui) vs screens setup offense (Grimmsnarl, Gholdengo, Mega Golisopod) | Dragalge THL | 26 | t9, t17 |
| G3 | [2688811994](https://replay.pokemonshowdown.com/gen9championsbssregmc-2688811994) | 2026-09-27 | Ch3t1x (1368) | Ghostofcolress (1453) | **1393** | Sash lead into Dragon Dance (Alakazam, Mega Gyarados, Garchomp) vs Samurott-H hazards into Mega Charizard X (Samurott-Hisui, Ninetales-Alola, Mega Charizard X) | Ch3t1x | 8 | t7; t3 held out |
| G4 | [2682454574](https://replay.pokemonshowdown.com/gen9championsbssregmc-2682454574) | 2026-09-16 | hengcaiji (1394) | Gosaimasu (1438) | **1377** | Special offense (Primarina, Mega Greninja, Corviknight) vs screens into Nasty Plot (Grimmsnarl, Gholdengo, third never shown) | Gosaimasu | 10 | t2, t4 |
| G5 | [2685829243](https://replay.pokemonshowdown.com/gen9championsbssregmc-2685829243) | 2026-09-22 | qhzht (1438) | LGPESWEEPER (1344) | **1369** | Hazard lead into Speed Boost (Glimmora, Mega Blaziken, Baxcalibur) vs fast Mega plus priority (Gyarados, Mega Lucario Z, Mimikyu) | LGPESWEEPER | 8 | t4, t6 |

**Ladder snapshot, 2026-09-28:**

| Player | Rank | Elo |
|---|---|---|
| Gosaimasu | #3 | 1534 |
| sky2132 | #14 | 1485 |
| Ghostofcolress | #39 | 1434 |
| Ch3t1x | #63 | 1415 |
| qhzht | #120 | 1364 |
| mk7juju | #125 | 1362 |
| LGPESWEEPER | #177 | 1332 |
| Dragalge THL | #426 | 1248 (after a drop from 1439) |
| hengcaiji | outside the top 500 | — |

The lower-rated player won 4 of the 5 games (all except G4).

## Method

1. **Search:** Showdown replay search, `https://replay.pokemonshowdown.com/search.json?format=gen9championsbssregmc`
   (51 results per page), both newest-first and `&sort=rating`. At least 1 s between all requests (1.2 s used).
2. **Fetch:** the full replay JSON for every one of the 51 top-rated results
   (`https://replay.pokemonshowdown.com/<id>.json`). Fields used: `players`, `rating`, `uploadtime`, and `log`, the
   full battle protocol.
3. **Parse:** a state tracker replayed each `log` and dumped the public board at the start of every turn: HP %,
   boosts, status, side conditions with their start turn, weather, Mega usage, and every move, item and ability
   revealed so far, in log order. It also read Team Preview (`|poke|`), picks and leads (`|switch|`/`|drag|`), Megas
   (`|detailschange|` + `|-mega|`), the result (`|win|`) and rating changes (`|raw|`). Nicknames are mapped to species
   through the details field (for example, "Inevitible" is a Sableye in replay 2679875458). The scripts ran in the
   Scout's scratchpad and are **not** in the repo, because this task allowed writing only the listed files.
   Committing them (for example as `tools/showdown_replays.py`) is the next step toward scale.
4. **Deductions** are marked `[inferred]`: Light Clay and Damp Rock from 8-turn screens or rain, and a ruled-out
   Stamina from a missing Defense boost. Other deductions and all opinions are labeled "my read".
5. **Mechanics checks:** typings, base stats and abilities come from (Pokémon Showdown public data,
   https://play.pokemonshowdown.com/data/pokedex.json, accessed 2026-09-28, Tier 2). Move data comes from
   (…/data/moves.json, same date, Tier 2), and ability and item effect texts from (…/data/abilities.js and
   …/data/items.js, same date, Tier 2). These describe how Showdown implements Champions. They are **not** verified
   against the game client.
6. **Write:** a match file per game following the README 4.5 schema, with `era: singles-supplement`, `mode: singles`,
   `division: ladder`, a `rating` field, the replay URL as `video`, and `status: draft`. Each game gets 2 Decision
   Library positions. The board state in a position is only what the deciding player could see: the opponent's info
   as revealed by that turn, plus the player's own set, which they know (taken from the full log).
7. **Held-out positions:** 2 of the 10 (one from G1, one from G3; 20% of this batch, against the 10% target) go in
   `positions-heldout/` with no answer section. Their answers are only in `answer-key.md`. To limit leakage, the G1 and
   G3 match files record those turns as `[log]` lines but don't analyze them in Key Decisions, Turning Points or
   Lessons.

### Selection criteria and funnel
- **Format:** Reg M-C, the current Champions BSS format on Showdown, live since about 2026-09-09. The fallback
  `gen9championsbssregmb` was checked and **not used**. It has only 3 replays at 1500+ (1526, 1520, 1518), two of them
  the same pairing (curryPanMan vs paurutan), and M-B is the previous regulation, so it can't stand for the current
  meta. Those 3 are candidates for a clearly labeled archive batch.
- **Rating:** 1500+ was preferred, but **no M-C replay reaches 1500**. The highest is 1460, and the live ladder has
  only 9 accounts at 1500+ Elo (77 at 1400+; ladder snapshot above). So the rule became "highest available". The 5
  picks are the top eligible games, rated 1369–1460.
- **Exclusions:** forfeits, inactivity or disconnect losses, games under 5 turns, and accounts whose names suggest bots
  or test accounts (PokachampFP5/7/9, PokaLadMcts, watapokebotwPW, Liotest1/2, yoyotakatest, testingtoba). The
  bot/test call is **my read from the names alone** (UNVERIFIED).
- **Funnel:** 51 top-rated M-C replays (ratings 1293–1460). 16 ended in a forfeit, 1 in an inactivity loss, 2 ran
  under 5 turns, and 12 involved bot or test-named accounts (these groups overlap), leaving **25 eligible**. Only
  **2 of the 6 replays at 1400+** were eligible (1460 and 1428); the other four were forfeits.
- **Diversity:** among the top 6 eligible games, 2679875458 (1393) was dropped because it repeated both a player
  (Dragalge THL) and an archetype (rain) already in the set. Two archetypes still appear twice, on purpose. In the 51
  top-rated replays, the Samurott-Hisui + Ninetales-Alola core appears on 7 team-sides (Ghostofcolress, ElPhilomeno),
  and the Grimmsnarl + Gholdengo screens core on 6 (Gosaimasu, lemme get a, mk7juju). Each is shown once winning and
  once losing (G1/G3 and G4/G2). These are sample counts from a small, upload-biased set, not usage statistics.

## Conventions
- `[log]`: taken from the battle log. HP is the log's percentage, not exact HP.
- The number after `-supereffective` or `-resisted` in the log counts doublings: `|1` = 2x (or 0.5x), `|2` = 4x
  (or 0.25x). This is my read of the protocol, and it matched the type chart everywhere it was checked across the 5
  games.
- "My read" means Scout analysis and opinion. No damage calculator was used, so damage estimates are scaled from HP
  changes in the log and say so.

## Problems with the data
1. **No 1500+ games in the current format.** See the selection criteria above. All 5 picks are 1369–1460.
2. **High forfeit rate at the top.** 4 of the 6 replays at 1400+ were forfeits.
3. **The very top of the ladder is missing.** The #1, #2 and #4 accounts (King-Yoo, 2shiaii, Might miss moves) have
   **zero** public M-C replays (user search on 2026-09-28). Uploads are opt-in, so the sample is biased.
4. **Bot-like accounts are common** in the top-rated list: 12 of 51 replays, mostly with the same rain team. Excluded.
5. **Mechanics caveat.** Showdown's Champions format can differ from base Gen 9 data. Make It Rain lowered SpA by
   **2** in all 3 uses in these replays [log], but Showdown's public move data (base Gen 9) says 1. Treat Showdown as a
   simulation of Champions until it's checked against the game client; knowledge/mechanics.md should record this.
6. **Partial sets.** There are no team sheets: only moves actually used are known, and there are no EVs or stat points.
   Some Pokémon never moved (Garchomp and Ninetales in G3, Baxcalibur in G5, Gosaimasu's third pick in G4).
7. **Log quirks.** One malformed HP string (`20/100y brn` in G2, T22), and nicknames in place of species (handled).
8. **Ratings move.** Dragalge THL dropped from 1439 after G2 to 1248 on the 2026-09-28 ladder. Replay rating shows how
   strong a game was, not how good a player is now.
9. **Verification.** All files are `status: draft`. The turn lines are exact by construction, but README 4.5 step 6
   needs a second agent to re-check them.

## What this pipeline could scale to (my read, measured on this batch)
- **The `[log]` layer can be fully automated:** Team Preview, turn-log draft, revealed sets, inferred items and rating
  lines. It's rate-limited to roughly 1–1.5 s per request, about **2,400–3,600 replays per hour** of fetch-and-parse on
  one worker. Parsing itself is effectively instant.
- **Annotated games are the real cost.** This first batch, including exploring the API, building the tracker and
  checking mechanics, took about 45 minutes of wall-clock for 5 match files, 10 positions and this README. With the
  tooling in place, I'd expect about **8–10 fully annotated games (2 positions each) per agent-hour**. Five helper
  sub-agents in parallel would give about 40–50 per hour.
- **QC can be 100% instead of 10%.** Because the log is exact, a script can diff every `[log]` line against the parsed
  protocol.
- **Supply, not processing, is the bottleneck.** About 25 eligible games rated 1290+ exist across roughly 19 days of
  M-C, about 1–2 new ones per day. To grow the base:
  1. Poll the rating-sorted search daily.
  2. Search by the usernames of top-ladder players (`search.json?user=<id>&format=…`).
  3. Add Smogon BSS tournament replays (`smogtours-gen9championsbssregmc-*`, visible in the same search but with no
     rating, so select them by tournament stage).
  4. Build a labeled Reg M-B archive batch (the 3 games at 1500+).
