# Doubles Threat List (VGC Reg M-C / Ranked Season M-6)

A living page. **Last updated:** 2026-09-28 by Scout. **Status:** PROVISIONAL. Built on one full-usage official M-C event (Baltimore) plus the Frankfurt and Brisbane top 8s. Refresh after the Recife and Louisville Regionals (Oct 3–4, Oct 10–11) and when Smogon's September stats land. Companion: `brief-2026-09-28.md`.

## How to read this page

- **Usage** figures:
  - **Baltimore share**, from Limitless (standings.limitlessvgc.com/0037/pokemon, acc. 2026-09-28, T2).
  - **Top-8s**, counted across 24 M-C Regional top-8 open team lists (Baltimore via Limitless T2; Frankfurt and Brisbane via RK9 rosters rk9.gg/roster/FR002-fiunEHp9wx4mh4 and rk9.gg/roster/BR002-IU5yO1W76UpdyA, T1).
  - **Tourn.** is the Pikalytics M-C tournament aggregate (pikalytics.com/pokedex/championstournaments/<Pokémon>, acc. 2026-09-28, T2).
- **Sets:** percentages are the share of that Pokémon's tournament open team lists (Pikalytics tournaments, T2). Named example sets come from open team lists (Limitless T2 or RK9 T1).
- **Mega typing, abilities and base stats** come from Showdown's public data (play.pokemonshowdown.com/data/pokedex.json, acc. 2026-09-28, T2). Not official Champions data, but consistent with the sets people run.
- **Spreads (as data shows):**
  - **M-B ladder:** most common Stat Point spread on the Showdown M-B ladder, August 2026 (smogon.com/stats/2026-08/moveset/gen9championsvgc2026regmb-1760.txt, pub. 2026-09-01, T2). M-B data; use it as a prior for M-C.
  - **WCS champion:** benchmarks from Takuma Yamazaki's team report (note.com/rapid_mint7926/n/nf439490f62a6, pub. 2026-09-06, T3; M-B context).
  - No public spread data exists yet for Pokémon new in M-C.
- **Speed**, Level 50, from Pikalytics' Champions speed tiers (pikalytics.com/speed-tiers, acc. 2026-09-28, T2), written as **max** (+Spe nature, 32 SP) / **neutral 32** / **neutral 0** / **min** (−Spe, 0 SP) / **Scarf max**.
  - Scout note: `stat = floor((base + 20 + SP) × nature)` reproduces every Pikalytics row I checked and the stat numbers in the champion's report (e.g. "A205 Kingambit", "S156 Jolly H-Arcanine"). This is an **inference**; confirm in `knowledge/mechanics.md`.
  - Tailwind doubles Speed for 4 turns and Trick Room lasts 5 turns (Showdown move data, play.pokemonshowdown.com/data/moves.json, T2; Scarlet/Violet baseline).
- **Answers** are **MY READ** (OPINION) unless marked otherwise. Any line that depends on a Scarlet/Violet mechanic says so; confirm those in `knowledge/mechanics.md`.

## Quick reference

| # | Threat | Baltimore share / top-8s | Why it matters | Speed max (neutral 32) | First answers to check (MY READ) |
|---|---|---|---|---|---|
| 1 | Rillaboom | 54.8% / 14 | Fake Out + Grassy Glide priority on Grassy Terrain; on most teams | 150 (137) | Fire/Flying/Poison hits, Intimidate, overwrite the terrain |
| 2 | Sneasler | 46.8% / 14 | Unburden speed after its Seed or White Herb triggers; Fake Out; Dire Claw status | 189 (172) | Psychic damage (4×), Intimidate, Wide/Quick Guard, Protect on turn 1 |
| 3 | Mega Salamence | 37.3% / 4 | Intimidate, then Aerilate Hyper Voice spread + Tailwind | 189 (172) | Ice (4×), Rock Slide, Fairy spread, Defiant/Competitive |
| 4 | Incineroar | 29.4% / 12 | Fake Out, Intimidate, Parting Shot cycling | 123 (112) | Defiant/Competitive, Water/Ground/Fighting |
| 5 | Gholdengo | 31.1% / 5 | Nasty Plot + Make It Rain spread; Good as Gold | 149 (136) | Kingambit, Fire/Ground/Dark/Ghost, Wide Guard |
| 6 | Kingambit | 25.9% / 7 | Defiant punishes Intimidate; Sucker Punch; late-game cleaner | 112 (102) | Fighting (4×), Fire, Ground; don't Intimidate it |
| 7 | Mega Raichu Y | 22.1% / 4 | No Guard Zap Cannon = sure paralysis at 200 Speed; Fake Out | 200 (182) | Ground types, Mega Garchomp Z / Scarf outspeed |
| 8 | Hisuian Arcanine | 24.4% / 3 | Sash, Head Smash, Extreme Speed (+2) | 156 (142) | Water/Ground spread, chip the Sash, Psychic Terrain (SV) |
| 9 | Indeedee-F / Indeedee-M | 20.0% + 5.5% / 4 | Psychic Terrain, Follow Me, Trick Room; Scarf Expanding Force (M) | F 150 / M 161 | Dark attacks, Imprison or Taunt vs Trick Room, terrain overwrite |
| 10 | Basculegion | 17.5% / 3 | Last Respects snowball; Aqua Jet; Scarf or Life Orb | 143 (130); Scarf 214 | Grass/Electric/Dark, Intimidate, don't feed KOs |
| 11 | Mega Floette | 11.9% / 8 | Fairy Aura Dazzling Gleam + Calm Mind; most top-8s of any Mega | 169 (154) | Steel/Poison, Gholdengo, Kingambit Iron Head |
| 12 | Mega Garchomp Z | Garchomp 14.7% total / 4 Z | Special Dragon at base Speed 151; won 2 of 3 M-C Regionals | 223 (203) | Fairy/Ice/Dragon hits, Scarf Garchomp 253, Pixilate Quick Attack |
| 13 | Archaludon (rain core) | 12.3% / 6 | Stamina tank; Electro Shot without a charge turn in rain; screens | 150 (137) | Fighting/Ground special, remove Pelipper or Politoed, break screens |
| 14 | Mega Charizard Y (sun) | 13.3% / 5 | Drought Heat Wave/Weather Ball; best Baltimore win rate in the top 20 (54.4%) | 167 (152) | Rock (4×) spread, Water/Electric, Wide Guard, weather control |
| 15 | Milotic | 15.6% / 2 | Competitive (punishes Intimidate), Coil + Hypnosis, Icy Wind | 146 (133) | Grass/Electric, don't Intimidate it, Taunt |

## Threat detail

### 1. Rillaboom
**Usage.** Baltimore 54.8% (591 teams, 49.6% win), top-8s 14/24, Tourn. 54.10% (#1). Showdown M-C ladder #1 (37.18%) (Pikalytics M-C Showdown, dateModified 2026-09-23, T2).

**Profile.** Grass. Base 100/125/90/60/70/85 (Pikalytics, T2). Grassy Surge 99%.

**Sets.** Fake Out 98%, Grassy Glide 98%, Wood Hammer 88%, U-turn 49%, High Horsepower 47%. Items: Miracle Seed 62%, Sitrus 11%, Life Orb 8%, Occa 5%. Grassy Glide gets +1 priority when the user is on Grassy Terrain (Showdown move data, T2).
- Rios (Frankfurt 1st): Miracle Seed, Adamant; Grassy Glide / Wood Hammer / Fake Out / U-turn (RK9, T1).
- Brady Smith (Baltimore 3rd): Eject Button, Careful; Fake Out / Grassy Glide / U-turn / Protect (Limitless, T2).

**Spreads.** No public M-C data yet (new in M-C).

**Speed.** 150 / 137 / 105 / 94; Scarf 225.

**Partners.** Sneasler 46%, Incineroar 44%, Mega Salamence 43%, Gholdengo 32%, Kingambit 25% (Pikalytics tournaments, T2).

**Answers (MY READ).**
- Mega Salamence's Aerilate Hyper Voice (Flying spread), Flare Blitz users, Dire Claw.
- Replacing Grassy Terrain removes Glide's priority: Indeedee's Psychic Surge, or Mega Metagross's Steel Roller, which ends terrain (Showdown move data, T2).
- Intimidate blunts Wood Hammer.

### 2. Sneasler
**Usage.** Baltimore 46.8% (505, 49.0% win), top-8s 14/24, Tourn. 44.54%. Baltimore Phase 2 conversion 0.83 (Scout calc from Limitless, T2).

**Profile.** Fighting/Poison. Base 80/130/60/40/80/120.

**Sets.** Close Combat 100%, Dire Claw 92%, Protect 75%, Fake Out 52%, Rock Slide 26%, Coaching 12%, Throat Chop 8%.
- Items: Grassy Seed 39%, Psychic Seed 26%, White Herb 21%, Focus Sash 11%. Unburden 91%, Poison Touch 8%.
- Dire Claw has a 50% chance to sleep, poison or paralyze (Showdown move data, T2).
- Poison Touch Sash sets exist, with Feint (Yamazaki, WCS 1st) or Quick Guard (Basham, Tang at Baltimore) (Limitless, T2).

**Spreads.** M-B ladder: Jolly 2/32/0/0/0/32 (47%), Adamant 2/32/0/0/0/32 (9%) (Smogon, T2). WCS champion: max Attack and Speed on the Sash set (note, T3).

**Speed.** 189 / 172 / 140 / 126; Scarf 283. Under Unburden, Speed doubles once the item is consumed (Scarlet/Violet behavior; confirm in Champions). A Psychic or Grassy Seed triggers on terrain activation; White Herb triggers after Close Combat's drops.

**Partners.** Rillaboom 56%, Mega Salamence 49%, Incineroar 33%, Kingambit 33%, Basculegion 27%.

**Answers (MY READ).**
- Psychic-type spread hits it 4× (Expanding Force Mega Gardevoir / Indeedee-M; Psychic from Farigiraf / Indeedee-F).
- Intimidate on the lead.
- Protect on turn 1 to waste Fake Out and the Seed's timing.
- Mega Staraptor and Mega Salamence Flying hits.

### 3. Mega Salamence
**Usage.** Baltimore 37.3% (402, 48.8% win); Mega Salamence on 37.3% of Phase 1 teams (Victory Road Baltimore page, victoryroad.pro/2027-baltimore/, T2). Top-8s 4/24. Tourn. 33.99% (#3). Phase 2 conversion 0.85.

**Profile.** Dragon/Flying. Base 95/145/130/120/90/120. Mega ability Aerilate; base ability Intimidate 95% (Showdown data, T2; Pikalytics, T2).

**Sets.** Protect 98%, Hyper Voice 92%, Tailwind 74%, Draco Meteor 57%, Double-Edge 31%, Flamethrower 18%.
- Ugarte (Baltimore 1st): Timid; Hyper Voice / Draco Meteor / Flamethrower / Protect (Limitless, T2).
- Daniel Walker (Brisbane 6th), support set: Careful; Double-Edge / Tailwind / Roost / Rain Dance (RK9, T1).

**Spreads.** No public M-C data yet.

**Speed.** 189 / 172 / 140 / 126; Scarf 283. Base Salamence before Mega Evolving is Speed 100: 167 max.

**Partners.** Rillaboom 69%, Sneasler 64%, Kingambit 34%, Gholdengo 31%, Incineroar 28%.

**Answers (MY READ).**
- Ice hits it 4× (Milotic's Ice Beam 58% / Icy Wind 48%, Mega Froslass's Blizzard).
- Rock Slide (Mega Tyranitar, Excadrill, Garchomp), Fairy spread (Mega Floette, Sylveon, Mega Gardevoir).
- Defiant Kingambit and Competitive Milotic punish its Intimidate.
- Wide Guard blocks Hyper Voice (Pelipper runs it 65%).

### 4. Incineroar
**Usage.** Baltimore 29.4% (317, 50.1% win), top-8s 12/24, Tourn. 32.53%.

**Profile.** Fire/Dark. Base 95/115/90/80/90/60. Intimidate 99%.

**Sets.** Fake Out 99%, Parting Shot 95%, Flare Blitz 94%, Throat Chop 51%, Darkest Lariat 28%. Items: Sitrus 67%, Chople 9%, Rocky Helmet 9%, Passho 8%.

**Spreads.** M-B ladder: very spread out; top is Impish 32/0/20/0/12/2 at 6% (Smogon, T2).

**Speed.** 123 / 112 / 80 / 72.

**Partners.** Rillaboom 73%, Sneasler 46%, Mega Salamence 29%, Mega Floette 29%, Gholdengo 24%.

**Answers (MY READ).**
- Defiant Kingambit and Competitive Milotic.
- Water / Fighting / Ground damage (Basculegion, Sneasler, Mega Swampert).
- Good as Gold Gholdengo ignores Parting Shot. It's a status move, and Good as Gold blocks opposing status moves in Scarlet/Violet; confirm in Champions.

### 5. Gholdengo
**Usage.** Baltimore 31.1% (335, 51.7% win), top-8s 5/24, Tourn. 21.51%. Phase 2 conversion 1.23. Worlds (M-B) was only 5.8%.

**Profile.** Steel/Ghost. Base 87/60/95/133/91/84. Good as Gold.

**Sets.** Make It Rain 100%, Shadow Ball 100%, Protect 96%, Nasty Plot 90%. Life Orb 81%.
- Make It Rain hits both foes and lowers the user's Sp. Atk (Showdown move data, T2).

**Spreads.** M-B ladder: Timid 2/0/0/32/0/32 (13%), Modest 2/0/0/32/0/32 (11%) (Smogon, T2).

**Speed.** 149 / 136 / 104 / 93; Scarf 223.

**Partners.** Rillaboom 81%, Mega Salamence 49%, Sneasler 47%, Mega Raichu Y 41%, Incineroar 36%.

**Answers (MY READ).**
- Kingambit (Dark; Sucker Punch before a Nasty Plot follow-up).
- Fire / Ground / Ghost / Dark hits.
- Wide Guard vs Make It Rain.
- Fake Out plus a double-target on the Nasty Plot turn.

### 6. Kingambit
**Usage.** Baltimore 25.9% (279, 52.2% win), top-8s 7/24, Tourn. 25.38%. Phase 2 conversion 1.32. On 7 of 8 Worlds M-B top-8 teams (Limitless Worlds, T2).

**Profile.** Dark/Steel. Base 100/135/120/60/85/50. Defiant 99%.

**Sets.** Kowtow Cleave 99%, Sucker Punch 97%, Iron Head 73%, Protect 59%, Low Kick 49%, Swords Dance 19%. Items: Chople 42%, Life Orb 21%, Black Glasses 17%, Sash 16%.

**Spreads.** M-B ladder: Adamant 32/32/0/0/1/1 (18%) (Smogon, T2). WCS champion: no Speed investment, heavy Sp. Def to survive Timid Mega Floette's (207 SpA) Light of Ruin 15/16 of the time. Chople Berry and Low Kick were for the Kingambit mirror; no Protect (note, T3).

**Speed.** 112 / 102 / 70 / 63. Slow enough to move first under Trick Room at minimum Speed.

**Partners.** Sneasler 57%, Rillaboom 54%, Mega Salamence 46%, Basculegion 29%, Incineroar 21%.

**Answers (MY READ).**
- Fighting hits it 4× (Close Combat from Sneasler / Mega Staraptor; Focus Blast from Mega Raichu Y; Low Kick). Chople Berry (42%) halves the first one.
- Fire and Ground hits.
- Never Intimidate or Parting Shot into it (Defiant).
- Protect on the turn it's expected to Sucker Punch.

### 7. Mega Raichu Y
**Usage.** Baltimore 22.1% (238, 52.0% win); Mega Raichu Y on 21.6% of Phase 1 teams and 27.7% of Phase 2 (VR Baltimore, T2). Top-8s 4/24. Tourn. 13.52%. Phase 2 conversion 1.26.

**Profile.** Electric. Base 60/100/55/160/80/130. Mega ability **No Guard** (Showdown data, T2).
- Zap Cannon is 50% accurate with a 100% paralysis chance (Showdown move data, T2), so under No Guard it's a guaranteed paralysis every turn.

**Sets.** Zap Cannon 100%, Focus Blast 99%, Protect 99%, Fake Out 75%, Encore 20%. Base ability on open team lists: Lightning Rod 95%.

**Spreads.** M-B ladder: Timid 30/0/13/0/0/23 (11%), Timid 32/0/0/2/0/32 (11%), Timid 2/0/0/32/0/32 (10%) (Smogon, T2). Many players trade Speed and power for bulk.

**Speed.** 200 / 182 / 150 / 135. Before Mega Evolving, Raichu is base 110: 178 max.

**Partners.** Rillaboom 85%, Gholdengo 66%, H-Arcanine 49%, Sneasler 37%, Sylveon 32%.

**Answers (MY READ).**
- Ground types (Garchomp; Excadrill; Mega Swampert).
- Faster threats: Mega Garchomp Z at 223, Scarf users.
- Priority: Extreme Speed, Grassy Glide, Aqua Jet. It has 55 base Defense.
- Electric types can't be paralyzed (Scarlet/Violet).

### 8. Hisuian Arcanine
**Usage.** Baltimore 24.4% (263, 51.5% win), top-8s 3/24, Tourn. 15.68%.

**Profile.** Fire/Rock. Base 95/115/80/95/80/90. Rock Head 96% (no recoil on Head Smash in Scarlet/Violet).

**Sets.** Flare Blitz 100%, Protect 98%, Head Smash 96%, Extreme Speed 93%. Focus Sash 96%. Extreme Speed is +2 priority (Showdown move data, T2).

**Spreads.** M-B ladder: Jolly 2/32/0/0/0/32 (45%) (Smogon, T2).

**Speed.** 156 / 142 / 110 / 99. The WCS champion made his Mega Floette Timid specifically to outspeed Jolly H-Arcanine (156) and survive its Head Smash (note, T3).

**Partners.** Rillaboom 81%, Mega Salamence 57%, Sneasler 50%, Gholdengo 46%, Mega Raichu Y 43%.

**Answers (MY READ).**
- Water and Ground hit it 4× (Muddy Water, Earthquake, Aqua Jet).
- Break the Sash with Fake Out chip or spread damage.
- Psychic Terrain stops Extreme Speed hitting grounded targets (Scarlet/Violet; confirm).

### 9. Indeedee-F / Indeedee-M (Psychic Terrain and Trick Room)
**Usage.** Baltimore: Indeedee-F 20.0% (49.2% win), Indeedee-M 5.5% (53.8% win). Top-8s 4/24 combined. Showdown ladder: Indeedee-F #6 (21.78%).

**Profile.** Psychic/Normal. Base F 70/55/65/95/105/85, M 60/65/55/105/95/95. Psychic Surge.

**Sets.**
- **F:** Follow Me 99%, Trick Room 89%, Helping Hand 83%, Psychic 66%. Items: Colbur 37%, Rocky Helmet 26%, Psychic Seed 20%.
- **M** (Pikalytics' "Indeedee" page appears to mix forms): Choice Scarf with Expanding Force / Mystical Fire / Trick (Ugarte, Baltimore 1st), or Scarf with Trick Room / Imprison (Blaik Thompson, Baltimore 4th) (Limitless, T2).
- Expanding Force hits both foes at 1.5× power on Psychic Terrain (Showdown move data, T2).

**Spreads.** No public M-C data yet.

**Speed.** F 150 / 137 / 105 / 94. M 161 / 147 / 115 / 103; Scarf 241.

**Partners.** Sneasler (66% for M, 48% for F), Mega Gardevoir, Mega Salamence, Excadrill / Mega Tyranitar (M), Armarouge (F).

**Answers (MY READ).**
- Dark attacks: Kowtow Cleave, Throat Chop, Knock Off. Sucker Punch and Fake Out won't hit grounded targets under Psychic Terrain in Scarlet/Violet; confirm.
- Taunt or Imprison vs Trick Room. Imprison already appears on Farigiraf (10%) and Indeedee-F (8%).
- Re-set Grassy Terrain (Rillaboom) or end it with Steel Roller.

### 10. Basculegion
**Usage.** Baltimore 17.5% (189, 47.0% win), top-8s 3/24, Tourn. 21.28%. Phase 2 conversion 0.55, the worst in the top 20. On 6 of 8 Worlds top-8 teams (M-B).

**Profile.** Water/Ghost. Base 120/112/65/80/75/78. Adaptability 96%.

**Sets.** Last Respects 100%, Wave Crash 95%, Aqua Jet 93%, Protect 60%, Flip Turn 40%. Items: Choice Scarf 39%, Life Orb 39%, Mystic Water 14%. Last Respects gains +50 power per fainted party member (Showdown move data, T2).

**Spreads.** M-B ladder: Jolly 2/32/0/0/0/32 (13%) (Smogon, T2). WCS champion: Life Orb, Sp. Def-heavy to survive a 212-SpA Mega Gengar Shadow Ball 13/16 of the time and a 205-Atk Kingambit Sucker Punch 9/16. Speed invested for the Basculegion mirror (note, T3).

**Speed.** 143 / 130 / 98 / 88; Scarf 214.

**Partners.** Sneasler 56%, Rillaboom 49%, Mega Salamence 40%, Kingambit 35%, Incineroar 27%.

**Answers (MY READ).**
- Grassy Glide (priority, super-effective), Zap Cannon, Kowtow Cleave / Sucker Punch.
- Intimidate.
- Avoid feeding early KOs when it is in the back.

### 11. Mega Floette (Floette-Eternal)
**Usage.** Baltimore 11.9% (128, 50.2% win), but top-8s 8/24, the most of any Mega Stone. Tourn. 13.19%. Phase 2 conversion 1.31.

**Profile.** Fairy. Mega base 74/85/87/155/148/102. Mega ability Fairy Aura (Showdown data, T2); base ability Flower Veil 94%.

**Sets.** Protect 100%, Dazzling Gleam 96%, Calm Mind 75%, Moonblast 73%, Draining Kiss 28%, Light of Ruin 27%. Light of Ruin is 140 BP with 1/2 recoil (Showdown move data, T2).

**Spreads.** M-B ladder: Timid 2/0/0/32/0/32 (17%) (Smogon, T2). WCS champion: Timid to outspeed Jolly H-Arcanine and survive its Head Smash (note, T3).

**Speed.** 169 / 154 / 122 / 109; Scarf 253. Before Mega Evolving, Floette-Eternal is base 92: 158 max.

**Partners.** Rillaboom 78%, Sneasler 71%, Incineroar 71%, Mega Salamence 45%, Gholdengo 36%.

**Answers (MY READ).**
- Steel and Poison attacks: Make It Rain, Iron Head, Dire Claw / Gunk Shot, Mega Metagross.
- Taunt or double-target on the Calm Mind turn.
- Good as Gold Gholdengo walls its Fairy damage and hits back.

### 12. Mega Garchomp Z (and Garchomp)
**Usage.** Garchomp species at Baltimore 14.7% (159, 52.9% win; includes Scarf, Life Orb and Mega forms). Mega Garchomp Z: Tourn. ~6% (#24).
- Top-8s: Frankfurt 1st (Rios) and 2nd (Liu Li), Brisbane 1st (Singh) and 7th (Tanizawa) (RK9, T1).
- Not in Baltimore's top-8 Mega list (VR, T2).

**Profile.** **Pure Dragon**, Mega ability **Levitate**. Base 108/130/85/141/85/151 (Showdown data, T2). The regular Mega Garchomp is Dragon/Ground with Sand Force and base Speed 92 (Showdown data, T2).

**Sets (Mega Z).** Protect 98%, Power Gem 81%, Draco Meteor 67%, Flamethrower 63%, Earth Power 41%, Dragon Pulse 35%. Natures are Modest in all four top-8 lists (RK9, T1).

**Sets (base Garchomp).** Dragon Claw 91%, Rock Slide 82%, Stomping Tantrum 65%, Earthquake 63%. Items: Life Orb 49%, Choice Scarf 31%.

**Spreads.** None public for Mega Z. Base Garchomp, M-B ladder: Jolly 2/32/0/0/0/32 (21%) (Smogon, T2). The WCS champion's Scarf Garchomp trimmed Atk and Spe for Defense, to survive a +2 Kingambit Sucker Punch 13/16 of the time while still outspeeding Mega Aerodactyl with Scarf (note, T3).

**Speed.** Mega Z: 223 / 203 / 171 / 153. Base Garchomp: 169 / 154 / 122 / 109; Scarf 253.

**Partners (Mega Z).** Rillaboom 68%, Incineroar 56%, Sneasler 44%, Farigiraf 25%, Kingambit 22%, Volcarona 21%.

**Answers (MY READ).**
- Fairy (Pixilate Quick Attack is Fairy-type priority), Ice (Icy Wind, Ice Beam, Blizzard) and Dragon hits.
- Scarf Garchomp (253) outspeeds it.
- Trick Room reverses its speed advantage.
- Levitate means Earthquake misses it.
- Details in the brief's §5.1.

### 13. Archaludon and the rain core (Pelipper / Politoed)
**Usage.** Baltimore: Archaludon 12.3% (52.3% win), Pelipper 12.4%, Politoed 4.3%. Top-8s: Archaludon 6/24, including Brisbane 1st and Baltimore 2nd.

**Profile.** Archaludon is Steel/Dragon, base 90/105/130/125/65/85, Stamina 97%.
- Electro Shot charges instantly in rain (Showdown move data, T2).
- Version 1.2.0 removed Archaludon's Mirror Coat and Metal Burst (Pokémon HOME news 817, T1).

**Sets.**
- **Archaludon:** Electro Shot 99%, Protect 98%, Dragon Pulse 85%, Flash Cannon 82%. Leftovers 90%.
- **Pelipper:** Hurricane 98%, Weather Ball 95%, Tailwind 85%, Wide Guard 65%. Focus Sash 48% / Sitrus 38%.
- **Politoed:** Weather Ball 95%, Perish Song 59%, Encore 45%.
- **Grimmsnarl screens:** Light Clay 94%, with Reflect and Light Screen 97% each (Pikalytics tournaments, T2).

**Spreads.** M-B ladder:
- Archaludon: Bold 32/0/1/1/29/3 (6%), Timid 2/0/0/32/0/32 (4%)
- Pelipper: Timid 2/0/0/32/0/32 (12%)
- Politoed: Calm 31/0/23/0/12/0 (27%) (Smogon, T2)

**Speed.** Archaludon 150 / 137 / 105 / 94. Pelipper 128 / 117. Politoed 134 / 122. Rain partners Mega Swampert (Swift Swim per Showdown data) and Mega Golisopod (base Speed 40, 101 max) are slow outside rain or Trick Room.

**Partners.** Pelipper 71%, Mega Golisopod 46%, Rillaboom 45%, Incineroar 29%, Grimmsnarl 28% (for Archaludon).

**Answers (MY READ).**
- Ground and Fighting damage into Archaludon (Earth Power, High Horsepower, Close Combat, Focus Blast).
- Remove or out-weather the drizzle setter (Mega Charizard Y's Drought, Mega Tyranitar's sand).
- A screen breaker. Rare in the field; see brief §5.3.

### 14. Mega Charizard Y (and Venusaur sun)
**Usage.** Baltimore 13.3% (143), **54.4% win**, the best in the top 20. Top-8s 5/24. Tourn. 9.97%. At Worlds (M-B) it was on 45.3% of teams.

**Profile.** Fire/Flying. Mega base 78/104/78/159/115/100, Mega ability Drought (Showdown data, T2).

**Sets.** Heat Wave 100%, Protect 99%, Weather Ball 92%, Solar Beam 44% / Ancient Power 43%, Hurricane 13%. Partner Venusaur varies:
- Focus Sash + Sleep Powder: Sánchez (Worlds 5th), Kiran Singh (Brisbane 1st), Daniel Quek (Brisbane 8th).
- Life Orb with Leaf Storm / Sludge Bomb / Earth Power and no Sleep Powder: Odriozola (Frankfurt 6th).
(Limitless, T2; RK9, T1)

**Spreads.** M-B ladder: Modest 32/0/2/32/0/0 (5%), Modest 22/0/20/11/0/13 (5%) (Smogon, T2). Very spread out.

**Speed.** 167 / 152 / 120 / 108.

**Partners.** Sneasler 34%, Rillaboom 34%, Kingambit 33%, Garchomp 33%, Sylveon 28%, Venusaur 27%.

**Answers (MY READ).**
- Rock hits it 4× (Rock Slide, Head Smash, Power Gem; Mega Garchomp Z carries Power Gem 81%).
- Rain resets the sun.
- Wide Guard vs Heat Wave.
- Grass types don't fear Sleep Powder in Scarlet/Violet; confirm.

### 15. Milotic
**Usage.** Baltimore 15.6% (168, 48.9% win), top-8s 2/24, Tourn. 11.60%. Worlds (M-B) 4.6%.

**Profile.** Water. Base 95/60/79/100/125/81. Competitive 99%.

**Sets.** Protect 80%, Scald 67%, Ice Beam 58%, Icy Wind 48%, Muddy Water 34%, Coil 31%, Hypnosis 30%, Recover 26%. Leftovers 60%, Sitrus 29%. Coil boosts accuracy, which is relevant to Hypnosis (60% base) (Showdown move data, T2).

**Spreads.** M-B ladder: Calm 32/0/27/0/5/2 (9%) (Smogon, T2).

**Speed.** 146 / 133 / 101 / 90. Icy Wind drops both foes' Speed by 1 stage.

**Partners.** Rillaboom 57%, Mega Salamence 47%, Sneasler 38%, Gholdengo 33%, Excadrill and Mega Tyranitar in sand (Pikalytics tournaments, T2).

**Answers (MY READ).**
- Grass and Electric hits (Grassy Glide, Zap Cannon).
- Never Intimidate or Parting Shot into it (Competitive).
- Taunt against the Coil / Recover / Hypnosis sets.

## Watch list (16–25)

| Pokémon | Why it's here (DATA) | Speed max (neutral 32) |
|---|---|---|
| Mega Golisopod | Baltimore 14.1%, 45.9% win (lowest in the top 20); ladder #8; Trick Room / rain attacker. Mega ability Tough Claws, base Speed 40 (Showdown data) | 101 (92) |
| Farigiraf | Baltimore 13.1%; Trick Room 97%, Armor Tail blocks priority in Scarlet/Violet; Frankfurt 2nd | 123 (112) |
| Sylveon | Baltimore 11.8%, 53.0% win, conversion 1.37; Pixilate Hyper Voice / Hyper Beam / Quick Attack | 123 (112) |
| Mega Gardevoir | Baltimore 10.5% but 47.9% win and conversion 0.68; Pixilate Hyper Voice + Expanding Force with Indeedee | 167 (152) |
| Mega Staraptor | Baltimore 9.9%, conversion 1.43; Mega ability Contrary (Close Combat raises its defenses), Tailwind 73% | 178 (162) |
| Mega Tyranitar + Excadrill (sand) | Baltimore winner (Ugarte). Excadrill has Sand Rush and a Sash; Mega Tyranitar has Rock Slide, Knock Off, Low Kick | Tyranitar-Mega 135 (123); Excadrill 154 (140) |
| Mega Gengar (Perish trap) | 4.5% usage, 55.0% win; on 3 of the 24 M-C top-8 teams (two Perish builds); Shadow Tag (Showdown data) | 200 (182) |
| Kommo-o | Baltimore conversion 1.74, 54.2% win; Clangorous Soul in Frankfurt 3rd and 5th | 150 (137) |
| Volcarona | Rage Powder / Tailwind support in Frankfurt 1st and Brisbane 7th; Quiver Dance in Frankfurt 7th | 167 (152) |
| Mega Froslass | Worlds 3rd, 4th and Juniors champion (M-B); M-C: Baltimore 6th, Frankfurt 7th; Snow Warning + Aurora Veil + Blizzard | 189 (172) |

Watch-list sources: Limitless and VR (T2), RK9 (T1), Pikalytics tournaments and speed tiers (T2), Showdown pokedex data (T2).

## Change log
- 2026-09-28: page created (first M-C version).
