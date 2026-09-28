# Sources: vetted list for the Champions coaching team

Owner: Scout. Last full check: **2026-09-28**. Re-check every source at least monthly, and at once when a
source fails, moves, or contradicts a higher tier.

---

## 1. Source hierarchy (cite in this order of trust)

Copied from `prompts/champions-coaching-team.md` §2.2 so this file stands alone.

**Tier 1: Official and primary (authoritative for rules and results)**
- Play! Pokémon / Pokémon Championships: `championships.pokemon.com`, `pokemon.com/play-pokemon`, and the VGC Tournament
  Handbook and Rules & Formats PDFs.
- Official in-game announcements and patch notes for Pokémon Champions, plus official social accounts.
- Official tournament pairings, standings, and team lists (RK9 Labs pages for official events).
- **Official match broadcasts:** the Play! Pokémon "Pokémon VGC Championships" YouTube playlist
  (`youtube.com/playlist?list=PL1ZXmduPrAdmRKbTx60G3eQwoJLQb5UDh`), `twitch.tv/pokemon`, and the Pokémon Broadcast Hub.
  What happens on screen is primary evidence. What the commentators say about it is expert opinion (Tier 3).

**Tier 2: Specialist data and community-standard reference (authoritative for usage and team trends)**
- **Pikalytics**: Champions usage by regulation and tournament results (`pikalytics.com/tournaments`).
- **Pokémon Zone**: Champions ranked usage for Singles and Doubles, by season (`pokemon-zone.com/champions/ranked-seasons/singles/`).
- **Victory Road** (`victoryroad.pro`): regulation pages, team reports, tournament team lists and analysis.
- **Limitless VGC**: tournament results and team lists, including grassroots and online events.
- **Liquipedia Pokémon**: event brackets, standings, player histories, and links to match videos.
- **Smogon Battle Stadium Singles (BSS)** forum, including its Pokémon Champions BSS discussion thread and BSS tournament
  replays. BSS uses the same 6-pick-3, Level 50 singles structure as Champions Singles.
- **Pokémon Showdown**: replays (exact turn-by-turn logs) and the damage calculator, *only where they support Champions
  mechanics*. Check this before relying on them.
- Champions-specific damage calculators and team builders. The Scout keeps a list of which ones are accurate for Champions (§7).

**Tier 3: Expert opinion (valuable, but it's opinion)**
- Team reports, articles, VODs, and streams from players with *documented* top results: Worlds, International Championship,
  and Regional top cuts for Doubles, and top ranked-season finishes and BSS tournament results for Singles.
- Commentary from official broadcasts.
- Streams and videos from top Singles ladder players, in English and Japanese. Japan has the deepest Singles scene, so
  translate transcripts.
- Game guide sites (such as Game8) are fine for ranked-system details once checked against Tier 1. Their tier lists are opinion.
- Established content creators and coaches. Weigh them by their competitive record, not their follower count.

**Tier 4: Signals only (never cite as fact)**
- Reddit, Discord, social media posts, and unverified leaks. Use them only as leads the Scout confirms from a higher tier.

## 2. Citation format (use everywhere)

`[claim] — (Source name, URL or event name, date accessed/published, tier)`

Any claim with no citation must be labeled `UNVERIFIED` or `OPINION`.

House conventions:
- Dates are ISO (`YYYY-MM-DD`). Give the page's published/updated date when it shows one, plus `accessed YYYY-MM-DD`.
- Cite the **original** Tier 1 page, not a mirror (cite `news.pokemon-home.com`, not PocketMonsters.Net).
- When one source backs every row of a table, one citation line under the table is enough.
- Derived numbers (math on a cited formula) are marked `[derived]` and name the formula's source.

## 3. Freshness rules (copied from §2.3)

- Every meta claim has an **as-of date**. Treat usage and "what's good" as **stale after 14 days**, and immediately after any
  ranked season change, regulation change, balance patch, or major event.
- When a new season or regulation set starts, every agent marks its meta knowledge for that mode as *provisional* until the
  Scout publishes a new Meta Brief.
- If an agent's training knowledge disagrees with a fresh Tier 1 or Tier 2 source, **the source wins**.
- Film Room lessons keep the era they came from. A lesson from the Scarlet/Violet or Sword/Shield era counts as a
  fundamental only if it doesn't depend on Tera or Dynamax.

## 4. Status legend

- **Live**: result of a check on 2026-09-28 (curl HTTP status, WebFetch, or API call). **Bot wall** means the site
  returns 403 to automated clients (Cloudflare / Incapsula). A human browser works, but agents can't read it.
- **Champions today**: `Y` = covers Pokémon Champions under the current rules (Reg M-C / Season M-6); `partial` = some
  Champions coverage, but stale or limited; `N` = no Champions coverage (or superseded).

## 5. Quick table

| Source | Tier | Live (2026-09-28) | Champions today | Best use |
|---|---|---|---|---|
| Official in-game news (news.pokemon-home.com) | 1 | Yes (HTML + JSON list) | Y | Season/regulation dates, timers, Mega rules, patch and maintenance notes |
| Official eligible-Pokémon lists (web-view.app.pokemonchampions.jp) | 1 | Yes | Y | Exact legal list per regulation |
| VGC Tournament Handbook PDF | 1 | Yes (via WebFetch; curl bot wall) | Y (rev. 2026-09-01) | Official-event rules, OTS, timers, tiebreaks |
| championships.pokemon.com | 1 | JS shell only; curl bot wall | Y (not machine-readable) | Human check of season changes, events, Broadcast Hub |
| pokemon.com/play-pokemon (+ Rules & Resources) | 1 | Yes (WebFetch); curl bot wall | Y | Links to the current rules PDFs, 2027 season news |
| "VG Rules, Formats & Penalty Guidelines" PDF | 1 | Yes | **N (stale, 2025-07-01)** | Superseded; don't use for Champions |
| pokemon.com news articles | 1 | Yes (WebFetch) | Y | Regulation announcements (e.g., M-C, 2026-09-02) |
| Nintendo Support update history | 1 | Yes (WebFetch) | Y | Patch notes by version |
| Official sites: champions.pokemon.com / pokemonchampions.jp | 1 | EN: WebFetch OK; JA: yes; EN .jp: 403 | Y | Modes, training, HOME rules, platform facts |
| press.pokemon.com | 1 | Yes | Y | Press releases (mobile launch, events) |
| Official social accounts | 1 | Not checked | — | Leads for announcements; confirm on the in-game news |
| RK9 Labs (rk9.gg) | 1 | Yes | Y | Official pairings, standings, team lists |
| Play! Pokémon YouTube / twitch.tv/pokemon | 1 | Not auto-checked (platform ToS) | Y (per official article) | Match video (Film Room) |
| Broadcast Hub | 1 | JS shell; `pokemon.com/broadcast` is **404** | Y | Live streams |
| In-game Battle Data (Battle → Battle Data) | 1 | In-game only | Y | Official ranked usage: moves, items, teammates, stats |
| Pikalytics | 2 | Yes | Y | Tournament usage/teams (Reg M-C), calc |
| Pokémon Zone | 2 | **Bot wall** (403 curl + WebFetch) | Y per search index; content unverified | Ranked usage by season (human check) |
| Victory Road | 2 | Yes | Y | Regulation summaries, 2027 calendar (OTS/regulation per event) |
| Limitless VGC | 2 | Yes | Y | Results and team lists (official + grassroots) |
| Liquipedia Pokémon | 2 | HTML bot wall; **API OK** | Y | Brackets, standings, event dates |
| Smogon BSS forum + Champions BSS thread | 2 | Yes | Y | Singles meta discussion, viability, rules summary |
| Smogon "Champions Battle Mechanics Research" thread | 2 | Yes (10 pages, last post 2026-09-26) | Y | **Best mechanics source after Tier 1** |
| Smogon "Pokémon Champions News and Changes Directory" | 2 | Yes | Y | Index of Smogon Champions resources |
| Showdown replay API | 2 | Yes (M-C replays from today) | Y | Exact turn logs, Singles supplement |
| Showdown damage calculator (Champions mode) | 2 | Yes | Y (M-C data) | Damage calcs (see §7) |
| Showdown public data files (play.pokemonshowdown.com/data) | 2 | Yes | partial | Species, types, abilities, Mega stats; **moves.json carries SV values** |
| Smogon usage stats | 2 | Yes | partial (M-B only; no M-C folder yet) | Showdown ladder usage, movesets, chaos JSON |
| Serebii | 2 | Yes | Y | Item, move, ability tables; patch log; season dates |
| Bulbapedia | 2 | Bot wall | unknown | Human check only |
| Pokémon Battle Database JP (champs.pokedb.tokyo) | 2 | Bot wall | Y per search index; unverified | JP ranked data (human check) |
| Game8 | 3 | Yes (curl; WebFetch returns blank) | Y (with errors, see §8) | Ranked-system details, change lists, rewards |
| Press/guide outlets (GamesRadar+, Automaton, Vandal, Operation Sports, Nintendo Everything) | 3 | Yes | Y | Corroboration of ranked/timer/UI facts |
| Low-trust guide sites (ChampDex, ChampsDex, games.gg, pokekipe, etc.) | 3 (low) | Mixed | Mixed | Leads only; several confirmed errors |
| Reddit / Discord / X | 4 | Not checked | — | Leads only |

## 6. Source notes

### Tier 1

**Official in-game news (Pokémon HOME / Champions news feed)**
- URL: https://news.pokemon-home.com/en/list (article list JSON: https://news.pokemon-home.com/en/json/list.json;
  pages: `https://news.pokemon-home.com/en/page/<id>.html`)
- Good for: the exact text of in-game announcements: regulation sets (M-A #751, M-B #776, M-C #816), ranked seasons
  (M-1 #746 … M-6 #822), online competitions (#824 MCS Sep 2026, #825 Global Challenge I), maintenance/patch notes
  (#817 v1.2.0, #855, #857), known issues (#758).
- Trust notes: this is the in-game notice text. Champions items are `infoTab: 5` in the JSON. PocketMonsters.Net mirrors these
  verbatim; cite the original.
- Live: yes (HTML and JSON). Champions: **Y**. Last checked: 2026-09-28.

**Official eligible-Pokémon lists**
- URLs: M-C https://web-view.app.pokemonchampions.jp/battle/pages/events/rs178713870219xeaaio/en/pokemon.html ·
  M-B …/rs178066986988lmoqpm/en/pokemon.html · M-A …/rs177501629259kmzbny/en/pokemon.html (linked from the regulation notices)
- Good for: the authoritative legal list (the page embeds a JSON array of dex number, form, and name).
- Trust notes: the list covers species and forms, not Mega Evolutions (those are listed in the regulation notice).
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Play! Pokémon VGC Tournament Handbook (PDF)**
- URL: https://www.pokemon.com/static-assets/content-assets/cms2/pdf/play-pokemon/rules/play-pokemon-vgc-tournament-handbook-en.pdf
- Good for: official-event rules: team construction, Open Team List contents, mobile eligibility, timers, Bo1/Bo3,
  tiebreaks, sudden death, disconnections.
- Trust notes: "LAST REVISION: September 1, 2026". §2.4 still says "The 2026 Pokémon VGC season will utilize an open team
  list format" even though it was revised in the 2027 season. Victory Road's calendar marks every listed 2027-season event
  OTS. curl gets an Incapsula 403; WebFetch downloads the PDF.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**championships.pokemon.com (Pokémon Championship Series)**
- URLs: https://championships.pokemon.com/en-us · season changes: https://championships.pokemon.com/en-us/about/2027-season-changes
  · Broadcast Hub: https://championships.pokemon.com/en-us/broadcasts/vg
- Good for: season changes, event list, Broadcast Hub.
- Trust notes: pages render client-side. WebFetch returns only the title; curl returns an Incapsula 403. **A human must read
  these pages.** The 2026 season-changes page (the prompt's starting point) shows only its title to agents.
- Live: yes (shell). Champions: Y (not machine-readable). Last checked: 2026-09-28.

**pokemon.com/play-pokemon and Rules & Resources**
- URLs: https://www.pokemon.com/us/play-pokemon · https://www.pokemon.com/us/play-pokemon/about/tournaments-rules-and-resources
- Good for: current links to the Tournament Rules Handbook, Standards of Conduct, Penalty Guidelines, VGC Tournament
  Handbook, and VG Team List PDF. The hub links 2027 Championship Series news and LAIC registration.
- Trust notes: curl gets a 403; WebFetch works. The general-rules PDFs were listed but not opened this pass.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**"Video Game Rules, Formats, & Penalty Guidelines" (PDF), STALE**
- URL: https://www.pokemon.com/static-assets/content-assets/cms2/pdf/play-pokemon/rules/play-pokemon-vg-rules-formats-and-penalty-guidelines-en.pdf
- Trust notes: "Date of last revision: July 1, 2025" (Scarlet/Violet era). It's no longer linked from Rules & Resources
  (checked 2026-09-28). **Do not use for Champions rules**; use the VGC Tournament Handbook.
- Live: yes. Champions: **N**. Last checked: 2026-09-28.

**pokemon.com news**
- Example: "Get Ready for Regulation Set M‑C in Pokémon Champions", https://www.pokemon.com/us/news/get-ready-for-regulation-set-m-c-in-pokemon-champions (published 2026-09-02)
- Good for: regulation announcements with local (PDT/PST) times; broadcast info (e.g., the 2026 NAIC article, 2026-06-12,
  lists the Broadcast Hub, Twitch.tv/Pokemon and YouTube @PlayPokemon as official channels).
- Live: yes (WebFetch). Champions: **Y**. Last checked: 2026-09-28.

**Nintendo Support: Pokémon Champions update history**
- URL: https://www.nintendo.com/en-gb/Support/Purchases-Subscriptions/Games/How-to-Update-Pokemon-Champions-3079895.html
- Good for: official patch notes per version (1.0.3 → 1.2.0).
- Live: yes (WebFetch). Champions: **Y**. Last checked: 2026-09-28.

**Official game sites**
- URLs: https://champions.pokemon.com/en-us/ (EN) · https://www.pokemonchampions.jp/ja/ (JA: battle, training and Pokémon pages)
- Good for: official descriptions of modes, training, HOME rules, cross-play, and the Omni Ring.
- Trust notes: the EN site is promotional and light on detail. The JA site has more (e.g., the Omni Ring note about future
  features). `pokemonchampions.jp/en/` returns 403 (S3 AccessDenied).
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**press.pokemon.com (TPCi press site)**
- URL: https://press.pokemon.com/en/releases/Pokemon-Champions-Launches-June-17-on-iOS-and-Android-Devices-The-Poke (2026-06-03)
- Good for: launch facts (mobile date, cross-play, F2P).
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Official social accounts**
- Not checked this pass (no automated access). Treat posts as leads and confirm them in the in-game news feed above.
- Live: not checked. Champions: —. Last checked: 2026-09-28 (skipped).

**RK9 Labs**
- URL: https://rk9.gg/events/pokemon
- Good for: official pairings, standings, team lists (OTS lists).
- Trust notes: the events page lists 2027-season Regionals (Brisbane and Frankfurt Sep 26–27, Recife, Louisville, Nice,
  Puebla, Gdańsk…).
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Official broadcasts: Play! Pokémon YouTube playlist, twitch.tv/pokemon, Broadcast Hub**
- URLs: https://www.youtube.com/playlist?list=PL1ZXmduPrAdmRKbTx60G3eQwoJLQb5UDh · https://twitch.tv/pokemon ·
  Broadcast Hub: https://championships.pokemon.com/en-us/broadcasts/vg (the official article gives "Pokemon.com/Broadcasts")
- Trust notes: YouTube and Twitch were **not auto-checked** (platform terms: no scraping, no caption or video downloads).
  The prompt's `pokemon.com/broadcast` (singular) returns **404**; use the URLs above. The official NAIC 2026 article
  (https://www.pokemon.com/us/pokemon-news/watch-the-2026-north-america-international-championships-live, 2026-06-12) names
  Twitch.tv/Pokemon (VGC) and YouTube @PlayPokemon as official channels.
- Champions: Y. Last checked: 2026-09-28.

**In-game Battle Data**
- Where: in-game Battle → Battle Data → Ranked Battles or Online Competitions; press X to switch Singles/Doubles. Per-Pokémon
  view shows its most popular moves, items, teammates and stats — (Operation Sports, https://www.operationsports.com/pokemon-champions-how-to-check-battle-data/, published 2026-04-22, Tier 3).
- Trust notes: official data, but only the Trainer can read it (screenshots). Update frequency is UNVERIFIED.
- Live: in-game only (not machine-checkable). Champions: **Y**. Last checked: 2026-09-28 (via the Operation Sports description).

### Tier 2

**Pikalytics**
- URLs: https://www.pikalytics.com/tournaments · calc: https://www.pikalytics.com/damage-calculator
- Good for: Reg M-C tournament teams and usage. The page says it tracks events run on Limitless, RK9 and Victory Road.
- Trust notes: the live tournament list is mostly grassroots (Limitless) events, so weigh by event size. The calc is covered in §7.
- Live: yes. Champions: **Y** (Reg M-C events on 2026-09-27/28). Last checked: 2026-09-28.

**Pokémon Zone**
- URLs: https://www.pokemon-zone.com/champions/ranked-seasons/singles/ · https://www.pokemon-zone.com/champions/regulations/
- Good for: ranked usage by season for Singles and Doubles.
- Trust notes: **bot wall** (Cloudflare challenge; 403 to curl and to WebFetch). The search index shows the Singles page
  titled "Season 6 — Singles Usage Stats", so it probably tracks M-6, but **its content was not verified**. A human should
  open it and paste the data, or screenshot it, for the Scout. Don't try to get around the bot wall.
- Live: bot wall. Champions: Y per search index (unverified). Last checked: 2026-09-28.

**Victory Road**
- URLs: https://victoryroad.pro/champions-regulations/ · https://victoryroad.pro/2027-season-calendar/ · https://victoryroad.pro/2027-season-structure/
- Good for: regulation summaries and dates, the official battle and team rules restated, an event calendar with regulation
  and OTS/CTS per event, and winners.
- Trust notes: accurate on everything cross-checked this pass. Its legal-Pokémon lists are images, so use the official
  eligible lists for exact legality. Calendar last updated 2026-09-23.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Limitless VGC**
- URL: https://limitlessvgc.com/
- Good for: results and team lists. On 2026-09-28 the homepage showed "Regulation Set M-C", the Baltimore Regional
  (19 Sep 2026, 1081 players), Worlds 2026 and NAIC 2026.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Liquipedia Pokémon**
- URL: https://liquipedia.net/pokemon/ (API: https://liquipedia.net/pokemon/api.php)
- Good for: event dates, brackets, standings, video links.
- Trust notes: HTML pages return 403 to curl and WebFetch. The **MediaWiki API works** with a descriptive User-Agent
  (siteinfo OK; "Pokemon Championships/Worlds/2026/VGC" exists, last touched 2026-09-23). Follow Liquipedia's API terms:
  only a few requests, spaced out, and parse actions rarely.
- Live: yes (API). Champions: **Y**. Last checked: 2026-09-28.

**Smogon BSS forum and Champions BSS threads**
- URLs: https://www.smogon.com/forums/forums/battle-stadium-singles.532/ ·
  https://www.smogon.com/forums/threads/pokemon-champions-bss-discussion-thread.3785396/ (OP 2026-07-17) ·
  viability: https://www.smogon.com/forums/threads/pokemon-champions-bss-viability-rankings.3780943/
- Good for: the Singles metagame, sets, and a rules restatement (L50, pick 3 of 6, Species and Item Clause).
- Trust notes: viability rankings are Tier 3-style opinion. Rules statements match the other sources.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Smogon "Champions Battle Mechanics Research" thread** (discovered)
- URL: https://www.smogon.com/forums/threads/champions-battle-mechanics-research.3780372/ (OP by Marty 2026-04-07,
  continually edited; page 10 has posts through 2026-09-26)
- Good for: tested mechanics with footage (DaWoblefet streams and others) and data-dump findings (credited to Kaphotics and
  Anubis): stat formula, PP formula, status changes, Unseen Fist, idle rule, Mega interactions, M-C-era changes.
- Trust notes: the OP itself warns that battle logic is server-side and can change without a version bump: "RE-TEST OFTEN".
  Prefer OP summary lines, and cite the individual post (author, date) for later findings.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Smogon "Pokémon Champions News and Changes Directory"** (discovered)
- URL: https://www.smogon.com/forums/threads/pok%C3%A9mon-champions-news-and-changes-directory.3780387/
- Good for: an index of Smogon's Champions resources (legal lists, mechanics changes, Mega abilities, speed tiers).
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Pokémon Showdown replay search API** (discovered)
- URLs: `https://replay.pokemonshowdown.com/search.json?format=<formatid>` · a replay: `https://replay.pokemonshowdown.com/<id>.json`
- Current Champions format IDs: `gen9championsbssregmc` (Singles, BSS Reg M-C) and `gen9championsvgc2026regmc` (Doubles).
  Older: `gen9championsbssregmb`, `gen9championsvgc2026regmb`. Search results include `rating` and `uploadtime`.
- Good for: exact turn logs for the Singles supplement and habit counts. The log's `|rule|` lines show the ladder's clauses
  (Species and Item Clause). `|teampreview|3` for BSS, `|teampreview|4` for VGC.
- Trust notes: this is Showdown's **simulation** of Champions, not the game client. Known reported discrepancies: Steel Beam
  self-KO order in 1v1 endgames (Smogon mechanics thread, Tyrant • Lucifer, 2026-09-26) and Sitrus Berry vs Dragon Tail
  timing (qrChar, 2026-09-23). Showdown's Team Preview shows species, level, gender and shiny, never items.
- Live: yes (M-C replays uploaded 2026-09-28). Champions: **Y**. Last checked: 2026-09-28.

**Pokémon Showdown damage calculator** (see §7)
- URL: https://calc.pokemonshowdown.com/ (select the **"Champions"** mode button)
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Pokémon Showdown public data files**
- URLs: https://play.pokemonshowdown.com/data/pokedex.json · https://play.pokemonshowdown.com/data/moves.json
- Good for: species base stats, types and abilities, including Champions/Z-A Megas (Mega Garchomp Z, Mega Lucario Z, etc.).
- Trust notes: these reflect Showdown's main (SV) data. **`moves.json` has SV values, not Champions values**: on
  2026-09-28 it listed Trop Kick at 70 BP and Moonblast with a 30% SpA drop, while Champions has 85 BP and 10%. Use
  Serebii's "Updated Attacks" or the calc's Champions mode for move data. The `isNonstandard` flags refer to SV formats,
  not Champions legality.
- Live: yes. Champions: **partial**. Last checked: 2026-09-28.

**Smogon usage stats** (discovered)
- URL: https://www.smogon.com/stats/ (folders `YYYY-MM/`, with `moveset/` and `chaos/` subfolders)
- Good for: Showdown ladder usage, movesets and teammates by rating cutoff (0/1500/1630/1760).
- Trust notes: the latest folder is **2026-08** (`gen9championsbssregmb-*`, `gen9championsvgc2026regmb-*`, `…bo3-*`, plus
  Smogon's own Champions OU/UU). That is **Reg M-B only**. `2026-09/` returned 404 on 2026-09-28, so there are no M-C
  stats until early October. This is Showdown ladder data, not in-game data.
- Live: yes. Champions: **partial**. Last checked: 2026-09-28.

**Serebii** (discovered)
- URLs: https://www.serebii.net/pokemonchampions/ (sub-pages: `rankedbattle.shtml`, `rankedbattle/seasonm-6.shtml`,
  `items.shtml`, `moves.shtml`, `updatedattacks.shtml`, `megaabilities.shtml`, `newabilities.shtml`,
  `statusconditions.shtml`, `training.shtml`, `patch.shtml`)
- Good for: item pool, usable moves with PP, move changes, Mega abilities, patch log, season dates, rewards.
- Trust notes: data tables matched other sources. Errors found: the 2026-09-09 news post said the September Monthly
  Challenge Series used Reg M-B, but the official notice says M-C; the patch page misspells "Mega Lucairo Z". The site is
  latin-1 encoded, so decode carefully.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Bulbapedia**
- URL: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Champions
- Trust notes: 403 to curl and WebFetch (bot wall). The search index shows useful pages ("Omni Ring", "Regulation Sets in
  Pokémon Champions"). Human check only.
- Live: bot wall. Champions: unknown. Last checked: 2026-09-28.

**Pokémon Battle Database JP (ポケモンバトルデータベース)**
- URL: https://champs.pokedb.tokyo/
- Trust notes: 403 to curl and WebFetch. The search index describes ranked data, usage rates and team-report collections for
  Champions. This is a lead for the JP Singles scene. Human check only.
- Live: bot wall. Champions: Y per search index (unverified). Last checked: 2026-09-28.

### Tier 3

**Game8 (Pokémon Champions wiki)**
- Key URLs: ranked guide https://game8.co/games/Pokemon-Champions/archives/588870 · formats …/588873 · Season M-6 …/620414 ·
  list of changes …/593893 · timers …/596247 · Stat Points …/538683 · IVs …/593716 · new items (M-C) …/605519
- Good for: ranked-system details, rewards tables, change lists per regulation, timer behavior.
- Trust notes: useful but **error-prone; check against Tier 1** (see §8). WebFetch returns a blank page for Game8, so use
  curl with a browser User-Agent. Tier lists are opinion.
- Live: yes. Champions: **Y**. Last checked: 2026-09-28.

**Press and guide outlets**
- GamesRadar+ ranks guide (https://www.gamesradar.com/games/pokemon/pokemon-champions-ranked-tiers/, updated 2026-06-17);
  GamesRadar+ timer-draw article (…/pokemon-champions-matches-end-in-draws-when-the-timer-runs-out-and-no-one-can-decide-if-thats-a-good-thing/,
  2026-04-10); Automaton (https://automaton-media.com/en/news/pokemon-champions-new-rules-eliminate-timer-stall-wins-but-possible-exploits-raise-concerns/,
  2026-04-08); Vandal ranks guide (https://vandal.elespanol.com/en/pokemon-champions/pokemon-champions-ranks.html, 2026-07-08,
  gzip-encoded); Operation Sports (Battle Data, 2026-04-22); Nintendo Everything (IVs and developer interview, 2026-03-26).
- Good for: corroborating ranked, timer and UI facts. They aren't competitive authorities.
- Live: yes. Champions: Y. Last checked: 2026-09-28.

**PocketMonsters.Net**
- URL: https://pocketmonsters.net/news/9511 (M-6), /9508 (v1.2.0)
- Trust notes: republishes official notices verbatim and links the original (news.pokemon-home.com). Cite the original.
- Live: yes. Champions: Y. Last checked: 2026-09-28.

**Top-player content, broadcast commentary, JP Singles streamers, coaches**
- Not surveyed in this pass. Add entries with each creator's documented results when the dossiers (knowledge/players/) are built.
- Live: n/a. Champions: n/a. Last checked: 2026-09-28 (not yet surveyed).

**Low-trust guide and tool sites** (ChampDex champdex.com, ChampsDex champsdex.com, games.gg, pokekipe.com, PokéChamps,
theclick.gg, op.gg, NeonLightsMedia, etc.)
- Trust notes: often uncited. Errors confirmed this pass: ChampsDex says "Terastallization and Mega Evolution are the two
  headline mechanics", but Tera isn't in Champions (see mechanics.md). games.gg says Throat Spray and Booster Energy are
  available, but neither is in Serebii's item list. ChampDex's claim that **held items show at Team Preview** has no
  corroboration. Use these as leads only.
- Live: mixed (games.gg bot wall; ChampDex and pokekipe readable via WebFetch). Champions: mixed. Last checked: 2026-09-28.

### Tier 4

**Reddit, Discord, X/Twitter, YouTube comments**: not checked. Leads only. Smogon threads often link X posts with footage.
Cite the Smogon post that analyzes the footage (Tier 2), not the X post. Live: not checked. Last checked: 2026-09-28 (skipped).

## 7. Damage calculators and team builders: Champions accuracy

Why it matters: Champions stats aren't SV stats. The formulas are HP = Base + StatPoints + 75 and
other stats = Nature × (Base + StatPoints + 20), with all IVs maxed. Many moves also changed. — (Smogon Champions Battle
Mechanics Research OP, https://www.smogon.com/forums/threads/champions-battle-mechanics-research.3780372/, accessed 2026-09-28, Tier 2)

| Tool | Verdict | Evidence (checked 2026-09-28) |
|---|---|---|
| **Pokémon Showdown calc, "Champions" mode** (https://calc.pokemonshowdown.com/) | **Use this. Verified by inspecting the site's code** | The stat function uses `base + sp + 75` for HP and `floor(nature × (base + sp + 20))` for other stats, matching the Smogon formula. SP entry is capped at 0–32 per stat. The Champions move patch covers the M-A→M-C changes (e.g., Trop Kick 85, Slash 80, Snipe Shot 85, Meteor Assault 170, Double Shock = punch, Dragon Cheer = sound, Freeze-Dry without freeze). It implements Aura Guard (halves contact damage), Mega Sol, Dragonize, Eelevate, Fire Mane, and Unseen Fist/Piercing Drill vs Protect, and includes the M-C Megas. When importing SV sets, it converts EVs to SP as 4 → 1 and otherwise `ceil(EV/8)`. — (calc.pokemonshowdown.com `calc/stats.js`, `calc/data/moves.js`, `calc/mechanics/gen789.js`, `js/shared_controls.js`, accessed 2026-09-28, Tier 2) |
| Pikalytics calc (https://www.pikalytics.com/damage-calculator) | Usable for quick checks; confirm key calcs on Showdown | It has a Champions mode with Stat Points and a Champions set dex, but the UI still shows a "Teratype" field (irrelevant in Champions; leave it blank). Formula not audited. |
| Game8 calc, op.gg calc, ChampDex calc, Porygon Labs, canolabs.dev, RotomPicks, PokéChampions Coach | UNVERIFIED | Not audited. Before trusting one, compare 3 calcs against the Showdown Champions calc. |
| taylorsmithgg.github.io/pokemonchampions ("Champions Calc") | **Don't use without an audit** | Its search-result description advertises "Terastallization" support, which Champions doesn't have. That's a red flag for its mechanics model. (Site not opened.) |
| Showdown teambuilder / validator (play.pokemonshowdown.com, `gen9championsbssregmc` / `gen9championsvgc2026regmc`) | Good for legality checks | Ladder replays show Species and Item Clause, and L50. It's Showdown's model, so the official eligible list still decides legality. |
| Game8 Team Builder | UNVERIFIED | Not audited. |

## 8. Known errors and stale pages (found 2026-09-28)

| Page | Problem | Trust instead |
|---|---|---|
| Game8 ranked guide (588870, updated 2026-09-09) | Header still reads "currently Season M-5 … Regulation M-B will last until September 02, 2026". | Official M-B notice: extended to **2026-09-09 01:59 UTC** (announced 2026-08-05). |
| Game8 M-6 page (620414) | Weekday typo ("September 9 (Thu)"; Sep 9 was a Wednesday); end time "05:59 UTC"; boilerplate "Season M-6 … has ended". | Official M-6 notice: **Wed 2026-10-07 01:59 UTC** end. |
| Game8 list of changes (593893) | Says Annihilape lost Pound in M-C. | Official 1.2.0 notes: **Politoed** lost Pound. |
| Game8 list of changes (593893) | Says Rest's sleep went from 2 to 3 turns. | Smogon research thread: "no change to Rest" (Hydrametr0nice, 2026-04-09). Rest is UNVERIFIED, so test it. |
| Game8 formats (588873) | Lists Electroweb as an entry hazard. | Electroweb isn't a hazard in SV, and no source says Champions changed it (Serebii's usable-moves list gives no hazard effect). |
| Game8 M-6 page (620414) | "cannot contain two Pokémon with the same Species other than Regional Forms" (ambiguous). | Handbook §2.3 and Victory Road: same National Pokédex number banned (Rotom forms and regional forms included). |
| Serebii news 2026-09-09 | Says the September Monthly Challenge Series used Reg M-B. | Official notice #824: **Regulation Set M-C**, Single Battles. |
| ChampsDex | Says Tera is a headline Champions mechanic. | Official regulation notices list only Mega Evolution. |
| games.gg | Lists Throat Spray and Booster Energy as available. | Serebii item list (not present). |
| VG Rules, Formats & Penalty Guidelines PDF | Revision 2025-07-01 (SV era). | VGC Tournament Handbook (rev. 2026-09-01). |
| Prompt URL `pokemon.com/broadcast` | 404. | championships.pokemon.com/en-us/broadcasts/vg ("Pokemon.com/Broadcasts"). |

## 9. Access notes for agents

- **Bot walls** (don't try to get around them): championships.pokemon.com and pokemon.com (curl 403, but WebFetch works on
  most pokemon.com pages and PDFs), Pokémon Zone, Bulbapedia, champs.pokedb.tokyo, games.gg, Liquipedia HTML. Ask the
  Trainer or a human to open these when they matter.
- **Rate limits:** wait at least 1 s between automated requests (use 2–3 s on forums). Liquipedia: API only, a few calls, spaced out.
- **YouTube and Twitch:** no scraping, no video or caption downloads. Keep notes, not copies.
- **GitHub** isn't used as a source in this project's sessions. Use play.pokemonshowdown.com data, the calc site, and the
  replay API instead.
- Game8 needs curl with a browser User-Agent (WebFetch returns blank). Serebii is latin-1. Vandal returns gzip.
