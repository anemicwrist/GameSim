# Film Room catalog: build notes

Scout, 2026-09-28. Covers `knowledge/film/catalog.csv` for the window 2021-09-28 → 2026-09-28. Every row is
`status: queued`. Nothing has been extracted or verified against video yet.

## 1. What's in the catalog

**340 rows: 119 event rows and 221 match rows.**

| Era | Event rows | Match rows | Total |
|---|---|---|---|
| champions | 14 | 221 | 235 |
| sv (Scarlet/Violet) | 94 | 0 | 94 |
| swsh (Sword/Shield) | 11 | 0 | 11 |
| **Total** | **119** | **221** | **340** |

| Priority (README 4.4) | Event rows | Match rows | What it is |
|---|---|---|---|
| 1 | 14 | 221 | Champions era: every Champions-format official event found, plus its featured Masters matches |
| 2 | 4 | 0 | Worlds 2022–2025 |
| 3 | 13 | 0 | International Championships 2022–2026 (EUIC 22–26, NAIC 22–25, OCIC 23, LAIC 24–26) |
| 4 | 88 | 0 | Regionals, Special Events, national championships (JCS, Korea PTC, Asia Master Ball Leagues), the 2021 Global Exhibition |
| 5 | 0 | 0 | No separate rows. The long tail (Jr/Sr divisions, other-language streams, pre-Champions Swiss features) sits inside the VODs listed on event rows |

Event rows by season (the official season name; for example, "2026 LAIC" was played in Nov 2025): 2022: 11 · 2023: 20 · 2024: 27 ·
2025: 25 · 2026: 32 · 2027 (so far): 4.

Broadcast type of event rows: **109 official** (Play! Pokémon or a regional Pokémon Company channel), **5 partner**
(Victory Road streams of the 2023 European Regionals and Special Events), **5 community** (OCE Pokémon VGC or OceaniaVGC,
Oceania Regionals). The brief asked for events "that had an official broadcast". The 10 partner and community rows are
extra and flagged in `notes` (`broadcast=partner|community`). Filter them out if you need the strict set. I kept them
because 2027 Brisbane is one of only three M-C events so far.

### Champions-era events (priority 1)

| Event row id | VGC dates | Format | Swiss featured | Top cut | Stream known | Official per-match uploads | VOD |
|---|---|---|---|---|---|---|---|
| 2026-malaysia | 05-09 → 05-10 | M-A | 0 | 1 (final) | 1/1 | 0 | Day 1 + Day 2 |
| 2026-thailand | 05-16 → 05-17 | M-A | 0 | 1 (final) | 1/1 | 0 | none located |
| 2026-singapore | 05-23 → 05-24 | M-A | 0 | 1 (final) | 1/1 | 0 | Day 2 |
| 2026-korea (PTC) | 05-24 → 05-25 | M-A | 0 | 1 (final) | 1/1 | 0 | Masters broadcast |
| 2026-indianapolis | 05-30 → 05-31 | M-A | 12 | 15 | 15/27 | 4 | Day 1 + Day 2 |
| 2026-japan (JCS) | 06-06 → 06-07 | M-A | 0 | 1 (final) | 1/1 | 0 | Day 1 + Day 2 |
| 2026-turin | 06-06 → 06-07 | M-A | 10 | 15 | 13/25 | 3 | Day 1 + Day 2 |
| 2026-naic | 06-12 → 06-14 | M-A | 39 | 12 | 41/51 | 3 | 3 days + 6 Victory Road side streams |
| 2026-taiwan | 06-13 → 06-14 | M-A | 0 | 1 (final) | 1/1 | 0 | Day 2 |
| 2026-worlds | 08-28 → 08-30 | M-B | 34 | 12 | 43/46 | 2 | 3 days on 2 channels + 4 Victory Road side streams |
| 2027-baltimore | 09-19 → 09-20 | M-C | 11 | 12 | 14/23 | 3 | Day 1 + Day 2 |
| 2027-indonesia-pbl | 09-19 → 09-20 | M-B | 0 | 1 (final) | 1/1 | 0 | none located |
| 2027-frankfurt | 09-26 → 09-27 | M-C | 11 | 11 | 12/22 | 0 (not posted yet) | Day 1 + Day 2 |
| 2027-brisbane | 09-26 → 09-27 | M-C | 10 | 10 | 10/20 | 0 | community Twitch, no VOD |

**The most complete are Worlds 2026 and NAIC 2026.** For those two, Liquipedia names the stream that carried each
featured Swiss match. For Worlds it also gives the exact VOD ID. They are followed by Baltimore 2027 and Indianapolis
2026, which have official per-match uploads for both semifinals and the final.

## 2. How it was built

1. **Event universe.** I used the Victory Road season calendars for 2022–2027 (dates, game, regulation per event;
   https://victoryroad.pro/2022-season-events/ , /2023-season-events/ , /2024-season-calendar/ , /2025-season-calendar/ ,
   /2026-season-calendar/ , /2027-season-calendar/ , accessed 2026-09-28, Tier 2), cross-checked against Serebii's 2022,
   2023 and 2026 series pages and Limitless's official-event index (https://standings.limitlessvgc.com/). Victory Road's
   season pages also gave me verified event-page URLs.
2. **Broadcast evidence.** I ran YouTube-restricted web searches for the official title patterns ("VG Day 2 | 2024
   Pokémon <City> Regional Championships", "VGC Day 1 | 2026 …", "Championship Sunday | …", "<P1> vs <P2> - Pokémon VGC
   Masters Finals | …"). **Every video ID in the CSV was confirmed with YouTube's oEmbed endpoint** (title plus channel).
   314 lookups were made, at 1 per second: 304 returned 200, 9 returned 404 and 1 returned 403. None of the 404 or 403
   IDs is used as a `video_url`: the 404s are removed 2021 Global Exhibition uploads, and the 403 is the Worlds 2024
   Sunday VOD, which is named only in `notes`. Fan re-uploads (Abnaze, ThePokeKing, "Moe Pokemon VGC Archival Process",
   and others) were identified by channel and excluded. An event goes in only if a VOD (or, for four rows, a broadcast
   channel) is documented.
3. **Champions-era matches.**
   - *Featured-match lists and top-cut brackets:* from Liquipedia's MediaWiki API, in 2 calls: the NAIC 2026 page, then
     one batched call for Worlds 2026, Indianapolis, Turin, Baltimore, Frankfurt and Brisbane. These give the Swiss
     "Streamed Matches" (round, players, game score, local start time, and which stream carried the match) and the
     top-cut brackets with game scores.
   - *Cross-check:* each of the 214 matches was matched against Limitless's per-round pairings (a mirror of RK9), about
     150 page loads at ≥2.5 s. The pairing, the round and the winner agree for all 214: 211 matched automatically and 3
     by hand, because of spelling variants (Nelson Fonkua/Fonkoua; Chanmin Lee/이 찬민; Tommy/Thomas Cooleen).
   - *Finals for events without a Liquipedia or RK9 bracket* (JCS 2026, Korea PTC 2026, the Malaysia, Thailand,
     Singapore and Taiwan Master Ball Leagues, Indonesia PBL): the final is derived as 1st vs 2nd from Victory Road's
     standings table. I read the raw page myself, because a WebFetch summary had swapped Taiwan's 1st and 2nd and
     invented impossible semifinal pairings.
4. **Access rules followed.**
   - YouTube and Twitch: oEmbed only. No page fetches, no captions, no downloads.
   - Liquipedia: one HTML page (Worlds 2026) loaded. The next four HTML requests, spaced 6 s apart, and one WebFetch got
     a bot challenge or 429, so I stopped fetching HTML. I then made two API calls, as the pilot and orchestrator
     advised. A third API call (a check of which pages exist) returned **429**, and I then stopped all Liquipedia
     access. Other Liquipedia URLs were confirmed only from search-engine results. **Wait before the next Liquipedia
     request.**
   - pokemon.com, championships.pokemon.com and the Broadcast Hub are bot-protected (Incapsula), so I didn't use them.

## 3. Column conventions

- `id`: events use Victory Road's slug style `<season>-<event>`, for example `2026-worlds` or `2027-baltimore`. Matches use
  `<event-id>-masters-<round>-<player1>-vs-<player2>`, with rounds written `r1`…`r13`, `top-16`, `quarterfinal`,
  `semifinal`, `final`. The Worlds 2026 pilot files use a different stem (`worlds2026-masters-final-onishi-vs-yamazaki-g1.md`).
  The matching catalog rows point to them in `notes`.
- `round`: `R<n>` (the Swiss round, identical to RK9/Limitless numbering), `Top 16` (the first playoff round, including
  cuts of 11–13 players with byes), `Quarterfinal`, `Semifinal` or `Final`.
- `player1`/`player2`: in Liquipedia's order, with Liquipedia spelling (so `Marco Silva`, where Limitless has "Marco
  Hemantha Kaludura Silva"). The derived finals list the champion first. `winner` is the winner of the set.
- `video_url`:
  - An official per-match upload if one exists.
  - Otherwise the VOD that Liquipedia names (Worlds).
  - Otherwise the day-stream VOD matched by date. Victory Road side-stream matches get the side-stream VOD matched by
    day and language.
  - When there's no VOD at all, it holds a channel page (4 event rows, 22 match rows), stated in `notes`.
- `timestamp`: **empty everywhere.** No permitted page publishes VOD offsets, and I didn't read YouTube pages or
  chapters. `notes` has `start_local=` (Liquipedia's local start time) for most Champions-era matches. That, plus the
  stream's start time, locates the match in a day VOD.
- `results_url`: Limitless standings for 2026/2027-season events. Match rows point to the exact Limitless round page.
  Older events use the Victory Road event page.
- `teamlist_url`: the RK9 roster (official open team lists) for 2026/2027-season events; otherwise the Victory Road
  event page. Match rows also list both players' Limitless team-list pages in `notes`.
- `liquipedia_url`: filled for 80 of 119 events, only where the page was confirmed. Empty means not confirmed this
  session, not that no page exists.
- `notes` keys on match rows: `stream=`, `start_local=`, `series=` (game score, p1-p2), `vod_kind=`, `teamlists:`,
  `src:`. Event rows have `broadcast=`, `vods:` (every VOD with its channel), `sources:`, and caveats.
- Channel legend:
  - Play Pokémon (@PlayPokemon) hosts the official "Pokémon VGC Championships" playlist
    (https://www.youtube.com/playlist?list=PL1ZXmduPrAdmRKbTx60G3eQwoJLQb5UDh).
  - Official Pokémon (@pokemon) mirrors most of the same streams (listed as "mirror").
  - Regional official channels: Pokémon JP official, Pokémon Korea official, Pokémon Asia ENG, Pokémon ZH official,
    Pokémon Indonesia.
  - Victory Road: its side streams at NAIC and Worlds 2026 feature different tables from the main stream, and
    Liquipedia lists them as "Community" streams.

## 4. VOD types: full-stream vs per-match

- **Full-stream day VODs** (3–10 hours each) are the default: 136 match rows point to a main-stream day VOD, and 48 to a
  Victory Road side-stream day VOD (EN or ES). Every event row points to a day VOD, normally the one containing the top
  cut.
- **Official per-match uploads** (a single set, starting at the set) are used in 15 match rows:
  - Worlds 2026 final (GHNLQjVj1Xc), and the Worlds 2026 Top 16 Joshi–Onishi set (a Victory Road upload).
  - NAIC 2026: final, the Glick–Dion quarterfinal, and the R4 Underhill–Glick set.
  - Indianapolis 2026: both semifinals, the final, and the R8 Gillespie–Glick set.
  - Turin 2026: both semifinals and the final.
  - Baltimore 2027: both semifinals and the final.
- More per-match uploads are listed in event-row `notes` for pre-Champions events: the Masters finals of Worlds
  2022/23/24/25, NAIC 2022, EUIC 2026, LAIC 2026, Las Vegas 2026, Stuttgart 2026 and Seville 2026; the Worlds 2023
  Harada–Kimura top 4; and the top 4 sets of Seville and Utrecht 2026.
- Two more uploads were matched only by inference from their titles, so they sit in `notes`, not in `video_url`:
  NAIC R6 Lybbert–Weed (T1xdxAo3VZU) and Indianapolis R7 Lara–Heier (ReeDgu2RUpQ).
- **Victory Road playlists** (4 event rows, the 2023 EU events) hold several videos. Use the playlist to find the day.

## 5. Known gaps and caveats

1. **No timestamps.** See section 3. This is the biggest gap for ingestion. The pilot's human watch-along plan fills it.
2. **Top-cut stream status is unconfirmed for 66 match rows.** Liquipedia doesn't mark streams on most regional top-cut
   matches. Those rows point to the relevant day VOD with `stream=not listed …`. The match may not be on the main stream.
3. **Thin Champions-era events:**
   - JCS 2026, PTC 2026, the four Master Ball Leagues and Indonesia PBL have only the final, derived from standings, with
     no series score and no featured Swiss list. Their brackets exist only as images on the Victory Road pages and the
     PACS portal.
   - No VOD located for the Thailand MBL or Indonesia PBL (official channels noted), or for Brisbane 2027 (community
     Twitch only).
   - Frankfurt 2027 ended yesterday, and its official per-match uploads aren't posted yet.
4. **The baseline conflicts with the sources.** The baseline says the first Champions-only event was Indianapolis
   (May 29–31).
   - The Malaysia MBL (2026-05-09/10) was played on Pokémon Champions M-A — (Victory Road 2026 calendar,
     https://victoryroad.pro/2026-season-calendar/, accessed 2026-09-28, Tier 2).
   - Victory Road called it "the first official live event in #PokemonChampions" —
     (https://x.com/VGCVictoryRoad/status/2052742820289474933, Tier 4 lead).
   - Thailand, Singapore and Korea (all before May 29) were also on M-A. The online Global Challenge (May 1–4) was M-A
     too, but I found no broadcast for it.

   I tagged these events `era=champions`, `priority=1`, because the README defines priority by era, and flagged
   "predates the 2026-05-29 cut-off" in `notes`. **My read:** Indianapolis was the first Champions *Regional* in the
   TPCi circuit, not the first Champions event overall.
5. **Date nuance.** The Indianapolis event weekend was May 29–31 (Limitless). The VGC days were May 30–31 (Liquipedia,
   Victory Road). The CSV uses the VGC days.
6. **Excluded because no official broadcast VOD was found** (the searches returned only community uploads, or nothing):
   - Latin American Regionals and Special Events 2023–2026.
   - Oceania Regionals other than the 5 community rows kept.
   - South Africa (MESA) Special Championships 2025–26.
   - San Juan / Caguas Special Events, and the London Open 2022.
   - The 2022 European, Latin American and Oceanian Regionals (Liverpool, Bilbao, Lille, Bremen, Milan, Santiago,
     Brisbane, Perth, Melbourne).
   - Hong Kong MBL 2026.
   - Online Global and Grand Challenges.
   - Two lists were **not searched** at all: Asia-Pacific national events 2022–2025, and the 2023 Paldea Prologue.
   - The 2023 LAIC had no VGC event per Victory Road's 2023 list.
7. **Missing day VODs** (the event row notes each one): the Day 1 of 2022 Vancouver; the Day 2 of 2022 Milwaukee, 2023
   San Diego and 2023 Hartford; the Championship Sunday of EUIC 2023/24/25 and LAIC 2025; and others.
8. **Unverified VODs.** The Worlds 2024 Championship Sunday VOD (M-tQC1AFomU) returned 403 on oEmbed, so it stays in
   `notes` only. The 2021 Global Exhibition per-match uploads now return 404.
9. **Data oddities to check while watching:**
   - Indianapolis R4 has three main-stream matches listed at 12:10, 13:40 and 14:45 EDT. Limitless confirms all three
     pairings are Round 4, so the times are the odd part.
   - Liquipedia labels the Baltimore 2027 times "PST".
   - Liquipedia's Worlds 2026 format text says there were 4 Day 2 Swiss rounds, but its match list and Limitless show 11
     Swiss rounds in total (R9–R11 on Day 2).

## 6. Recommended ingestion order for the next sessions

Keep the pilot's pipeline v2 (text harvest first, then a human watch-along; see `pilot-report.md` section 6). The order:

1. **Worlds 2026 top cut (12 sets).** The pilot has 3 of 12 as draft files. The rest are on the Day 2 main stream
   (SPiMHL6SfzA), with Liquipedia start times.
2. **M-C, the current regulation:**
   - Baltimore 2027 top cut: the semifinals and final have per-match uploads.
   - Frankfurt 2027 top cut: re-check for per-match uploads around 2026-10-01.
   - Brisbane 2027: find a VOD first.
3. **NAIC 2026 top cut, then its 13 main-stream Swiss features.** After that, the 26 Victory Road side-stream features
   (EN first).
4. **Worlds 2026 Swiss features (34):** main stream (12), then Victory Road EN (11), then Victory Road ES (11).
5. **Indianapolis 2026 and Turin 2026:** top cut first, then the Swiss features.
6. **The Asia-Pacific, JCS and PTC finals:** Pokémon Asia ENG ones first (English commentary). JCS, PTC and Taiwan need
   JP/KR/ZH name maps.
7. **Then priority 2.** Catalog the Worlds 2022–2025 top-cut sets as match rows. Limitless doesn't cover them, so use
   RK9 pairings per round, or the Liquipedia API after a cooldown, with batched titles and at most one request per
   30 s for `parse`. Then priority 3 (the 13 ICs), then 4.

Housekeeping for the next session:
- Add October 2026 events within 7 days of each: Recife 10-03/04, Louisville 10-10/11, Nice 10-17/18, Puebla
  10-24/25, and Gdańsk 10-31→11-01.
- Re-search the Thailand MBL and Indonesia PBL VODs and the Worlds 2024 Sunday VOD.
- Fill the 39 empty `liquipedia_url` cells in one batched API call once the block has lifted.
- Search the Asia-Pacific national events for 2022–2025.
