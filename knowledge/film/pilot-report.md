# Film Room Pilot Report: 5 Champions-era games

Scout, 2026-09-28. Roadmap Phase 3, step 3. Status: complete for the text-only pipeline. No game has been checked against
video.

## TL;DR
- **Games:** five games from the 2026 World Championships Masters top cut, Regulation M-B: all three games of the final,
  plus one game from each semifinal. Files are in `knowledge/film/matches/`, all `status: draft`.
- **What's easy:** metadata, both open team lists, set results and VOD links fill at about 86–95% from permitted sources.
- **What's hard:** game content (brings, leads, turns, decisions, turning points) fills at only **20–40%**. It exists only
  where somebody wrote about that exact game, which means the official recap and the two finalists' own team reports.
  Not one turn could be placed on a turn number.
- **What can't be done by agents:** README 4.5 steps 3 (caption tracks), 4 (frame sampling) and 6 (QC against video) all
  conflict with YouTube's and Twitch's terms. Under those terms, turn-level data for official matches can come only from
  (a) writing or (b) a human watching the official VOD normally. Section 6 proposes a pipeline v2 built on that.

## 1. Games chosen and how complete each file is

| File | Game | Why chosen | Overall | Metadata + teams | Game content |
|---|---|---|---|---|---|
| `worlds2026-masters-final-onishi-vs-yamazaki-g1.md` | Final G1 | Highest priority; official recap and both players' reports | 60% | 88% | 23% |
| `worlds2026-masters-final-onishi-vs-yamazaki-g2.md` | Final G2 | Official recap names a G2 moment (Kingambit at 1%) | 59% | 86% | 23% |
| `worlds2026-masters-final-onishi-vs-yamazaki-g3.md` | Final G3 | Official set-winning play; Onishi names "Game 3" | **71%** | 93% | **40%** |
| `worlds2026-masters-semifinal-onishi-vs-leite-g2.md` | SF1 G2 | Onishi's report describes this game (a comeback from a losing team preview) | 64% | 95% | 20% |
| `worlds2026-masters-semifinal-yamazaki-vs-weed-g3.md` | SF2 G3 | Yamazaki's report gives his plan for this matchup; G3 winner can be deduced | 66% | 95% | 25% |

How these percentages are scored: 24 schema fields per game. 14 are metadata and teams (the frontmatter plus both sixes);
10 are game content (brings ×2, leads ×2, win conditions ×2, turn log, key decisions, turning points, lessons). Each field
scores 1 if sourced for that game, 0.5 if partial or if the game number is inferred, 0.25 if only inferred from a general
plan (or a hint for finding it in the VOD), and 0 if not available. The per-field matrix is in the appendix. Some fields are
filled only with inferences, so "game content" overstates what we actually know about the games.

Why Worlds rather than the alternatives: I also checked NAIC 2026 (M-A) and Indianapolis 2026 (the first Champions-only
Regional). Both have results, team lists and official VODs. For NAIC, the written game-level coverage I could reach was thinner. The
championships.pokemon.com event page renders by JavaScript and gave WebFetch no content (I didn't try its JSON). The NAIC
Quick Attack article was bot-blocked when I fetched it. The fan-blog recap had nothing per game. For Indianapolis, I
confirmed only the final (Arsal Puri 2-0 Wolfe Glick) and didn't search for team reports in the time box, so it's
unexplored rather than thin — (Liquipedia Indianapolis 2026 VGC page via API, accessed 2026-09-28, Tier 2); (Victory Road
NAIC and Indianapolis pages, https://victoryroad.pro/2026-naic/ , https://victoryroad.pro/2026-indianapolis/, accessed
2026-09-28, Tier 2).

## 2. What each source type gave

| Source type (tier) | Examples used | Fields it filled | Fields it couldn't fill | Access notes (2026-09-28) |
|---|---|---|---|---|
| **Official results and team lists** (T1) | RK9 pairings (top-cut rounds 12–15), roster (in-game names), public team lists; the worlds.pokemon.com standings feed; pokemon.com results | event, division, round, players, **set** winner, table numbers, both sixes (ability, item, nature ["Stat Alignment"], moves), in-game names | Game scores, game winners, stat points, brings, leads, turns | RK9 loads pairings through per-round fragments (`?pod=2&rnd=N`); fine at a gentle rate. pokemon.com blocks `curl` (Incapsula 403). WebFetch worked for the Worlds Quick Attack article and was blocked on the NAIC one. |
| **Official editorial coverage** (T1, editorial) | worlds.pokemon.com "Standings and Coverage" entries (daily; the page content is also served as JSON); pokemon.com "Quick Attack"; the official Sunday preview | Set score (2-1), 2 game-level moments (G2: Kingambit at 1%; the set-winning Feint + Aqua Jet on Mega Charizard Y), player quotes, archetype framing | Turn numbers; the game number for the Quick Attack moment; anything about the semifinals; brings and leads | It contained **one factual error**: the preview says both finalists use Tailwind, and Yamazaki's RK9 list has none. Treat editorial text as a recap, not a record. |
| **Community reference** (T2) | Liquipedia (MediaWiki API), Victory Road event page, Limitless, VRPastes, MetaVGC, Top Cut Explorer | **Game scores per set** (2-0 / 2-1), match start times (PDT), which VOD holds each match (day stream vs standalone upload), mirrors of the team lists | Game winners, brings, leads, turns | Liquipedia's page returned 429 through WebFetch but worked through its API with a descriptive User-Agent and one request per page. Pikalytics' Worlds page didn't list the Worlds top-cut teams (snapshot 2026-09-09). |
| **Players' own team reports** (T3) | Yamazaki (note.com, 2026-09-06), Onishi (note.com, 2026-09-13), both in Japanese | **The only game-numbered details outside the official recap**: "決勝のGame3" (final, game 3), "Top4… Game1 / Game2"; planned brings and leads per matchup (including the exact QF, SF and final opponents); win conditions; stat-point benchmarks; exact Speed (Basculegion S123); self-assessed mistakes | Turn logs; confirmation that a planned bring was used in a given game | No reports from Weed or Leite were found. **WebFetch's summarizer mistranslated the Japanese names** (Sneasler → "Weavile", Basculegion → "Palafin", Kingambit → "Kommo-o", Floette → "Florges"), so I read the raw text myself instead. |
| **Press** (T3) | Kotaku, The Big Lead, GAME Watch, Sportskeeda, Deltia's Gaming | Archetype descriptions, "full set" (3 games) confirmation, set tables | Anything game-level | Sportskeeda (403), Deltia's (405), Pokémon Zone (403) and Bulbagarden (403) refused automated fetches. |
| **Official video** (T1 on-screen) | YouTube: standalone final upload `GHNLQjVj1Xc`; stream VODs `SPiMHL6SfzA` (Day 2), `cqXdwdtjzuA` (Sunday) | Video links, titles and channel (oEmbed) | **Everything visual**: captions, frames, and per-game timestamps (none published on any permitted page) | Metadata only. No downloads, no caption tracks, no scraping. |
| **Social** (T4) | Victory Road's and Play! Pokémon's X posts (game-by-game updates probably exist) | Nothing | Everything | x.com returns HTTP 402 to fetches. It's Tier 4 anyway. |
| **Search-engine answer summaries** | WebSearch answer text | Pointers to pages only | Nothing (not a source) | **They fabricated facts** during this pilot: "Onishi… won the 2026 World Championship", "Leite winning 2-1" against Onishi, and garbled species names. Never cite them. |
| **Showdown replays** | None | Nothing | Nothing | Official matches are played on the Champions client, so no Showdown replays exist. They're relevant only to the Singles supplement and to practice formats, if Showdown supports Champions (still to verify). |

## 3. Effort

Agent effort, approximate (OPINION, from this session's work log):
- **Event-level discovery** (shared by all 5 games): about 70 tool calls, roughly 2 hours. About 20 pages were useful; about
  12 were blocked or empty. Most of the time went to finding the few pages with game-level text, and to reading two
  Japanese reports in the original.
- **Per game**, once sources are in hand: about 15–25 minutes to write and cite a text-first file.
- **Marginal cost** of another game at an already-researched event: about 15 minutes. A new event costs about 1.5–2.5 hours
  of discovery. Almost all of the cost is per event, not per game.

Projected human effort for watch-along (OPINION): the Trainer needs about 25–40 minutes per game (watching with pauses,
plus writing notes). The Coach needs about 15–20 minutes per game to prepare a viewing guide from the text-first file.

## 4. Problems found

1. **The pipeline conflicts with platform terms.** README 4.1 ("caption tracks… frames sampled from the video") and 4.5
   steps 3, 4 and 6 can't be run by agents. The QC rule ("re-check ≥10% of turns against the video… ≥95% agreement") can't
   be met without a human watching.
2. **Game winners are usually missing.** Sources give set scores. A game winner can be deduced only for the last game of a
   2-1 set or for both games of a 2-0. The G1 and G2 winners of the final are unknown.
3. **Written moments rarely carry turn numbers, and sometimes not even game numbers.** Quick Attack says "to set the win",
   not "game 3".
4. **Planned is not played.** The richest material, players' selection plans, describes intentions, not what was clicked
   in a given game. The schema needs to keep them apart.
5. **An error in official editorial text** (the Tailwind claim) shows that we need a "Conflicts" section and a rule that the
   RK9 list beats editorial text.
6. **Language.** The two most useful sources are Japanese. Automatic summaries corrupted species names, so we need raw
   text plus a name map built from the legal list.
7. **Bot walls.** Several relevant pages refuse automated fetches (listed in section 2). We must not work around them.
   They go on a list for humans to read instead.

## 5. Schema fixes (proposed; README not edited, pending the Coach and Lab)

1. **Provenance tags.** Add `[report]`: the line comes from writing (an official recap, press, or a player's own report),
   with a mandatory citation. Add `[watch]`: a human watch-along note, with the watcher and a VOD timestamp. Keep
   `[inferred]`, and require the basis. Keep `[video]` and `[commentary]` only for human-verified lines.
2. **Game-number confidence.** When a source doesn't number the game, write `[report]` plus a note: "game number
   `[inferred]` from …".
3. **Frontmatter additions:** `series_score`, `game_winner_basis` (record | report | inferred-from-set-score | unknown),
   `video_kind` (standalone-set-upload | day-stream), `video_alt`, `match_start_local`, `in_game_names`,
   `provenance_tags_used`. `winner:` may be "Not available from permitted sources". (All five pilot files use these under a
   "pilot extensions" comment.)
4. **Team Preview:** split it into *Brought (actual)*, *Leads (actual)* and *Planned selection (player report)*. Each
   actual field is `known [source]`, `inferred`, or "Not available from permitted sources". Add *Known spreads and speeds*,
   because open team lists have no stat points and reports fill that gap.
5. **Turn Log:** allow "Moments with no known turn number (M1, M2…)" when the turn is unknown.
6. **New sections:** "Set-level facts (game not specified)", "Conflicts between sources", and "Open items for
   watch-along".
7. **Status ladder:** `draft-text` (text-only; agent QC = citation audit, re-opening every source) → `draft` (after
   watch-along) → `verified` (a second human pass on ≥10% of logged actions, with ≥95% agreement).
8. **Lessons:** add `basis: observed | player-plan | set-level`. `lessons.md` should require at least one `observed` match
   of the two it needs, so that plans don't masquerade as evidence.
9. **catalog.csv** (for the agent that owns it; I didn't touch it): consider columns for `match_start_local`,
   `video_kind`, `in_game_names`, `series_score`, `coverage_page` and `report_links`.

## 6. Recommended pipeline v2 (within platform terms)

**Stage 1: Catalog (agent, automated, gentle rates).** Use RK9 (pairings per round, roster, team lists), the official
event coverage page (Worlds serves its entries as JSON), Liquipedia via its API (set scores, start times and VOD IDs;
follow Liquipedia's API terms on User-Agent and rate limits), the Victory Road event page (which VOD holds each match),
and YouTube oEmbed for titles. Output: catalog rows plus text-first file skeletons. About 15–30 minutes per event.

**Stage 2: Text harvest (agent).** In order of yield: (1) the official coverage page and Quick Attack-style articles;
(2) players' own reports (note.com, Victory Road team reports, personal blogs), read in the original language with a
JP→EN name map, re-checking every translated species against the team list; (3) press, for context only. Tag everything
`[report]`. Re-check for reports 2 and 4 weeks after the event (Onishi's came 14 days after the final). Output:
`status: draft-text`.

**Stage 3: Watch-along (human, the only route to turn logs for official matches).** The Trainer watches the official VOD
normally on YouTube or Twitch (no downloads) and follows a viewing guide the Coach prepares:
```
VIEWING GUIDE — <match file>                      prepared by Coach, <date>
Open: <official URL> (standalone set, or day stream + clock time from Liquipedia)
2-min brief: both sixes (items and key moves), known speeds/spreads from reports, each side's plan (from reports)
PAUSE A — Team Preview (before picks are revealed): predict both sides' 4 and their leads. Write them down.
PAUSE B — After turn 1 is chosen: what would you click for each side? Then watch. Log what happened.
Every turn: log "T<n>: <mon> <move> → <target> (<result>)" plus the VOD time. Note switches, Mega, Protect, field effects.
HOOKS from reports (spoiler-free phrasing): "watch the Basculegion speed contest", "a Kingambit ends at very low HP"
PAUSE C–E — decision points the Coach flags, e.g. the turn before a KO on a Mega: "what would you click?"
AFTER: fill in the brings, leads, winner and 1–3 key decisions; compare your predictions with the pro's plays.
```
The Coach turns each PAUSE into a Decision Library position (board state from the Trainer's log plus the list sets and
report spreads, with the answer kept hidden) and merges the log into the match file as `[watch]` lines, with VOD
timestamps. The Trainer's notes are notes, not footage, so they're allowed.

**Stage 4: QC.** Agents do a citation audit: re-open every source and confirm every `[report]` line. Humans do a second
watch of at least 10% of `[watch]` actions, and must reach ≥95% agreement before a file becomes `verified`.

**Stage 5: Official APIs, metadata only (optional).** With a YouTube Data API key, `videos.list` metadata such as
`liveStreamingDetails.actualStartTime` gives the start time of a day stream. Combined with Liquipedia's match times, that
yields approximate seek offsets for the viewing guide. Never download captions (the API allows that only to the video's
owner). For Twitch, use VOD metadata only.

**Stage 6: Singles supplement.** Where exact logs exist (Smogon BSS tournament replays, Showdown replays of Champions
formats, if and where Showdown supports them), parse the text logs at a gentle rate. They give exact turns and need no
video.

**What honestly can't be done:** automated turn logs, HP reads or commentary transcripts for official matches; game
winners that nobody wrote down; the old README's "95% against video" check without a human. The Trainer's time is the
bottleneck. Five years of VODs can't all be watched, so watch-along should target the Champions-era top cut first and
games that have report hooks.

## 7. Leads to follow up (not facts)
- Onishi says he posted a WCS explanation on his YouTube channel (`@cona5757`). A human could watch it for his own account
  of each game — (Onishi report, https://note.com/cona_5757/n/n0b5081073f01, 2026-09-13, Tier 3)
- Third-party breakdowns of the final exist; titles and channels come from oEmbed, and their content is Tier 3 opinion:
  アルカナ/alcana (`OGl247l6FGw`), CloverBells (`3HCaQhfXo1k`), Pokeaim+ (`SvH3iZQGxkw`).
- Tier 4 lead to check in watch-along: "Feint broke Charizard's Protect" in the deciding game. This came from a search
  summary and from Deltia's Gaming, whose page is blocked to automated fetches.
- Weed and Leite team reports: re-check around 2026-10-12.

## Appendix: field matrix (1 / 0.5 / 0.25 / 0)
| Field | F-G1 | F-G2 | F-G3 | SF1-G2 | SF2-G3 |
|---|---|---|---|---|---|
| event, date, era, format, mode, division, round, players (8) | 1 each | 1 each | 1 each | 1 each | 1 each |
| game winner | 0 | 0 | 1 | 1 | 1 |
| video link | 1 | 1 | 1 | 1 | 1 |
| game start timestamp | 0.25 | 0 | 0 | 0.25 | 0.25 |
| team_lists | 1 | 1 | 1 | 1 | 1 |
| P1 six / P2 six | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| P1 / P2 brought | 0 / 0.25 | 0 / 0.25 | 0.25 / 0.5 | 0 / 0 | 0.25 / 0 |
| P1 / P2 leads | 0 / 0.25 | 0 / 0 | 0 / 0 | 0 / 0 | 0.25 / 0 |
| P1 / P2 win condition | 0.5 / 0.5 | 0.5 / 0.5 | 0.5 / 0.5 | 0.5 / 0.25 | 1 / 0.25 |
| turn log | 0 | 0.25 | 0.25 | 0 | 0 |
| key decisions | 0.25 | 0 | 0.5 | 0.25 | 0.25 |
| turning points | 0 | 0.25 | 0.5 | 0.5 | 0 |
| lessons | 0.5 | 0.5 | 1 | 0.5 | 0.5 |
