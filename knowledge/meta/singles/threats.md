# Singles Threat List (living page)

| | |
|---|---|
| Mode | Singles: 3v3, register 6, pick 3 |
| Format | Regulation M-C, Ranked Season M-6 |
| Last updated | 2026-09-28 by Scout |
| Status | **PROVISIONAL**, as for the rest of the first M-C cycle |
| Companion brief | `brief-2026-09-28.md`. It has the full source list (§9) and the data limits (§1). |

**How to read each entry**
- **Sets** are in-game Ranked Singles percentages (S1: PokéChamp DB transcription of the in-game Battle Data, snapshot 2026-09-27 10:06 UTC).
- **Seen on Showdown** comes from Scout's sample of 299 M-C replays: 462 human sides, 281 unique teams, bots excluded (S4). Win % carries a 95% CI and its n. **Most n are small.**
- **What beats it** has three parts:
  - **Data:** who knocked it out in the sample (S4). It is small-n, and because 136 games were against one AI rain team (Archaludon, Meowscarada, Pelipper, Salamence, Sneasler, Swampert), those species are over-represented as attackers.
  - **Top players say:** attributed opinion.
  - **My read:** OPINION, built from verified typings, stats and speeds.
- **Typings and matchups** use Showdown's public pokedex.json and typechart.js. **Ability, move and item effects** use its moves.json, abilities.js and items.js (S15; Tier-2 implementation). Nothing on this page is verified against the game itself.
- SP spread order is HP/Atk/Def/SpA/SpD/Spe. "+Spe" means a Speed-raising nature (Jolly, Timid, Naive, Hasty). "32" means maximum Speed investment.

---

## 0. Stat system and speed benchmarks

**Formula (confidence: high, Tier 2)**
- Level 50. Stat Points (SP) cap at 32 per stat and total 66.
- **HP = Base + SP + 75.** **Other stats = ⌊(Base + SP + 20) × nature⌋**, where nature is ×1.1 or ×0.9.
- Choice Scarf is ×1.5. Unburden doubles Speed once the item is lost. Swift Swim doubles Speed in rain (S15). Stat stages are ×1.5 at +1 and ×2 at +2.

**How the formula was checked**
1. PokéChamp DB's public stat code computes non-HP max as ⌊1.1 × (B+52)⌋, neutral max as B+52, and uninvested as B+20. HP max is B+107 (S1, site JS bundle).
2. It reproduces **every value checked** in Smogon's Reg M-C speed-tier list (S13). Examples: Mega Z trio 223/203, Mega Salamence 189/172, +1 Mega Salamence 283/258, Golisopod-Mega 60/54.
3. Every in-game SP distribution sums to 66 with a cap of 32 (S1; also Game8, S10).
4. **Not checked against an in-game stat screen.**
5. **PENDING:** whether the new Speed applies on the turn a Pokémon Mega Evolves. The mechanics owner should confirm this.

**Speed benchmarks (the M-C field)**

| Speed | Pokémon / condition |
|---|---|
| 378 / 344 | Sneasler after Unburden triggers (+Spe / Adamant, 32 Spe) |
| 288 | Choice Scarf Meowscarada (Jolly) |
| 286 | Mega Blastoise +2 after Shell Smash (Timid 32) |
| 283 | Mega Salamence +1 after Dragon Dance (+Spe) |
| 282 | Choice Scarf Cinderace (Jolly) |
| 262 / 256 | Scarf Meowscarada (Adamant) / Scarf Cinderace (Adamant); Mega Blastoise +2 (Modest, 30 Spe) is also 256 |
| 258 | Mega Salamence +1 (neutral) |
| 253 / 231 | Choice Scarf Garchomp (Jolly / Adamant) |
| 241 | Choice Scarf Indeedee (Timid) |
| 228 / 208 | Mega Baxcalibur +1 (Jolly / Adamant) |
| **223** | **Mega Garchomp Z / Mega Lucario Z / Mega Absol Z (+Spe 32): the new ceiling** |
| 214 / 195 | Choice Scarf Basculegion (Jolly / Adamant): **slower than the +Spe Z-Megas** |
| 203 | Mega Z trio (neutral 32) |
| 192 / 175 | Meowscarada (Jolly / Adamant) |
| 189 / 172 | Mega Salamence (+Spe / neutral); Sneasler before Unburden (Jolly / Adamant) |
| 188 / 171 | Cinderace (Jolly / Adamant) |
| 177 | Alolan Ninetales (Timid) |
| 172 | Pawmot (Jolly) |
| 169 / 154 | Garchomp before Mega (Jolly / Adamant) |
| 167 / 152 | Charizard, Mega X and Mega Y alike (Timid / Modest) |
| 162 / 148 | Mimikyu (Jolly / Adamant) |
| 161 / 147 | Indeedee (Timid / Modest) |
| 156 | Lucario before Mega (Timid) |
| 152 / 139 | Baxcalibur, same before and after Mega (Jolly / Adamant) |
| 151 / 138 | Glimmora (Timid / Modest) |
| 150 / 137 / 105 | Archaludon (Timid / Modest / 0 SP) |
| 149 / 136 / 104 | Gholdengo (Timid / Modest / 0 SP) |
| 146 / 133 / 101 | Gyarados, same speed as Mega (Jolly / Adamant / Impish 0 SP) |
| 143 / 130 | Basculegion (Jolly / Adamant); Mega Blastoise (Timid) is also 143 |
| 128 | Mega Blastoise (Modest, 30 Spe; most common spread) |
| 107 | Rillaboom (Adamant, 2 Spe; most common spread) |
| 87 / 78 | Corviknight (0 SP neutral / Relaxed) |
| 80 / 72 | Primarina (0 SP); Aegislash (0 SP / Quiet 72) |
| 67 | Hippowdon (0 SP) |
| 60 / 54 | Mega Golisopod (0 SP neutral / Brave) |

---

## 1. Mega Salamence: in-game #1 (NEW) · 33.8% of sample teams
- **Profile** (S15): Salamence (Dragon/Flying, 95/135/80/110/80/100, Intimidate) becomes **Mega: Dragon/Flying, 95/145/130/120/90/120, Aerilate** (Normal moves become Flying with 1.2× power).
  - Weak: **Ice ×4**, Dragon, Fairy, Rock. Resists: Grass ×¼, Bug, Fighting, Fire, Water. Immune: Ground.
- **Sets** (S1): Salamencite 97.4%. Intimidate 99.1% (it activates on the pre-Mega switch-in).
  - **Physical Dragon Dance:** Double-Edge 77.8, Earthquake 73.0, Dragon Dance 69.6, Roost 59.9. Natures: Adamant 46.8 / Jolly 16.3 / Naive 15.8. Spreads: 1/32/1/0/0/32 (14.1), 2/32/0/0/0/32 (12.3).
  - **Special minority:** Draco Meteor 30.7, Fire Blast 21.1, Flamethrower 14.7, Hyper Voice 13.6. Spread 1/0/1/32/0/32 (5.1).
- **Seen on Showdown** (S4): brought 38% when registered. It Mega Evolves in about 88% of games where it is brought. Lead 5%. **Won 40% when brought (CI 29–53, n=60).** Moves seen: Double-Edge 29, Dragon Dance 17, Earthquake 15, Draco Meteor 9, Roost 8.
- **Speed:** Mega 189 (+Spe) / 172 (neutral). +1: 283 / 258. Before Mega: 167 / 152.
- **Partners:** in-game, Primarina, Hippowdon, Gholdengo, Garchomp, Lucario, Archaludon (S1). Sample cores: Primarina (36 teams), Gholdengo (28, lift 1.6), Hippowdon (25, lift 2.0), Aegislash (18, lift 1.9) (S4).
- **What beats it**
  - **Data** (S4): 48 human-side faints. **Its own Double-Edge recoil caused 8.** Archaludon 7, Charizard 3, and Swampert, Gyarados, Mimikyu and Gholdengo 2 each.
  - **Top players say:**
    - Magcargo says the main draw of Baxcalibur is that it checks Mega Salamence with Ice Shard (S12, 2026-09-12; paraphrase).
    - "Offence as the best defence against Mega Salamence" (deepseazapdos, S12, 2026-09-11).
    - Rotom-Heat is "anti golisopod and anti mence if it doesnt run facade" (JoeyJoestar, S12, 2026-09-15).
    - Metagross "ignores Intimidate with Clear Body, resists Double-Edge, then can Ice Punch in" (HazelGrayble, S11, 2026-09-27).
  - **My read:**
    - Revenge it with **Ice Shard Baxcalibur** (4×, non-contact priority) or **Scarf Jolly Meowscarada Triple Axel** (288 outspeeds even +1 Salamence at 283).
    - Wall its main attack with **Steel types that resist Flying**, ideally holding **Rocky Helmet** (Double-Edge makes contact): Corviknight, Archaludon, Aegislash, Metagross.
    - Moonblast and Power Gem hit it super-effectively. Do not rely on Ninetales (177), which is slower than Mega Salamence.

## 2. Garchomp / Mega Garchomp Z: in-game #2 (M-5 #1) · 31.0%
- **Profile** (S15):
  - Base: **Dragon/Ground, 108/130/95/80/85/102, Rough Skin**. Weak Ice ×4, Dragon, Fairy. Immune Electric.
  - **Mega Z: pure Dragon, 108/130/85/141/85/151, Levitate.** Weak Dragon, Fairy, Ice (only ×2). Resists Electric, Fire, Grass, Water. Levitate makes it immune to Ground.
  - Replays show Earthquake failing into Levitate and Electric and Grass moves being resisted (S4). This confirms Showdown's implementation, not the game.
- **Sets** (S1), four distinct builds:
  - **Garchompite Z 34.9%**, either physical (Jolly 25.4 / Adamant 19.8; 2/32/0/0/0/32 at 26.8) or **special** (Timid 20.1; 2/0/0/32/0/32 at 23.0; Draco Meteor 30.0, Earth Power 24.3, Flamethrower 27.7, Power Gem 18.7).
  - **Choice Scarf 17.8%.**
  - **Focus Sash 16.0%** lead with Stealth Rock (40.8% overall).
  - **Bulky**: Rocky Helmet 12.3 or Sitrus 11.0, Impish 17.1, Dragon Tail 27.7.
  - Earthquake fell from 99.2% (M-5) to 67.3% (S1/S2).
- **Seen on Showdown** (S4): brought 51%, lead 16%, Mega Evolved in 20% of registrations (33 Garchompite Z, 1 Garchompite). **Won 49% (CI 39–59, n=88).** Moves seen: Earthquake 38, **Earth Power 22, Draco Meteor 17**, Stealth Rock 9, Dragon Tail 8.
- **Speed:** Mega Z 223 / 203. Base 169 / 154. Scarf 253 / 231.
- **Partners** (S1): Primarina, Golisopod, Salamence, Baxcalibur, Gholdengo, Lucario.
- **What beats it**
  - **Data** (S4): 56 faints. Archaludon 9, Salamence 8, Garchomp 6, Swampert 4, Cinderace 4.
  - **My read:**
    - **Fairy and Ice hit both forms.** Primarina Moonblast, Mimikyu Play Rough (Disguise absorbs the first hit), Ice Shard, and Scarf Meowscarada Triple Axel.
    - Mega Z **resists Electric and Water**, so do not count on them. Steel types resist Draco Meteor but take Flamethrower or Earth Power from the special Mega Z.
    - Items are hidden at Team Preview. Tells: Rough Skin damage means base form (Sash, Scarf or Helmet); Levitate appears after it Mega Evolves.

## 3. Primarina: #3 (M-5 #2) · 28.5%
- **Profile** (S15): **Water/Fairy, 80/74/74/126/116/60.** Weak Electric, Grass, Poison. Immune Dragon. Resists Bug, Dark, Fighting, Fire, Ice, Water.
- **Sets** (S1): Moonblast 98.0, Sparkling Aria 90.0, Aqua Jet 67.5, Encore 50.3, Calm Mind 35.8, Flip Turn 14.9. Items: Sitrus 41.0, Leftovers 32.1, Chesto 8.3 (Rest). Modest 71.0. Spread 32/0/20/14/0/0 (11.1), which is bulky with 0 Spe.
- **Seen on Showdown** (S4): brought 42%, **lead 25%**. Won 47% (34–60, n=51). Items seen: Sitrus 17, Leftovers 8.
- **Speed:** 80 with 0 SP. Everything relevant outspeeds it, so it relies on Aqua Jet (contact, which Mega Lucario Z halves).
- **Partners** (S1): Salamence, Garchomp, Hippowdon, Golisopod, Gholdengo, Baxcalibur.
- **What beats it**
  - **Data** (S4): 37 faints. Swampert 6, then Blastoise, Gholdengo and Meowscarada 3 each.
  - **My read:**
    - Grass: Rillaboom's Grassy Glide, with priority in its terrain.
    - Poison: Sneasler's Dire Claw, Glimmora's Sludge Wave.
    - Electric: Archaludon Thunderbolt (it also resists Water), Pawmot, Rotom-Wash.
    - Steel: Gholdengo (resists Fairy, hits back with super-effective Make It Rain) and Mega Lucario Z's Flash Cannon.
    - Encore (50%) punishes setting up in front of it. Taunt or fast attackers beat Calm Mind.

## 4. Hippowdon: #4 (M-5 #6) · 13.2%
- **Profile** (S15): **Ground, 108/112/118/68/72/47, Sand Stream.** Weak Grass, Ice, Water. Immune Electric.
- **Sets** (S1): Earthquake 97.1, Yawn 95.9, Stealth Rock 89.5, Whirlwind 60.0, Slack Off 38.6. Items: Sitrus 63.8, **Rocky Helmet 18.6 (new)**, Leftovers 15.9. Natures: Impish 59.2 / Careful 30.6. Spreads: 32/0/2/0/32/0 (28.3), 32/0/32/0/2/0 (17.6).
- **Seen on Showdown** (S4): brought 45%, lead 16%. Won 48% (31–66, n=29). **It KO'd only 4 Pokémon in 29 appearances**, so its job is support.
- **Speed:** 67 with 0 SP.
- **Partners** (S1): Salamence, Primarina, Lucario, Gholdengo, Baxcalibur, Aegislash.
- **What beats it**
  - **Top players say:** "the premier tank right now … lack of versatility is what truly holds it back" (Photon, S12, 2026-08-22, M-B context).
  - **My read:**
    - **Taunt** (Gyarados 51.6%) stops Yawn, Stealth Rock, Whirlwind and Slack Off.
    - **Good as Gold** Gholdengo is immune to Yawn and Whirlwind, and Air Balloon makes it immune to Earthquake, Hippowdon's only attack.
    - Water, Grass and Ice hit it super-effectively: Primarina, Basculegion, Rillaboom, Baxcalibur, Ninetales, Mega Blastoise.

## 5. Baxcalibur / Mega Baxcalibur: #5 (NEW) · 16.7%
- **Profile** (S15):
  - Base: **Dragon/Ice, 115/145/92/75/86/87.**
  - **Mega: 115/175/117/105/101/87.** Both have **Thermal Exchange**: Fire moves raise its Attack by 1 and it cannot be burned.
  - Weak Dragon, Fairy, Fighting, Rock, Steel. Resists Electric, Grass, Water.
- **Sets** (S1): **Focus Sash 46.9% (not Mega Evolving) vs Baxcalibrite 35.6%.**
  - Moves: Ice Shard 91.9, Earthquake 91.4, Glaive Rush 83.4, Icicle Crash 52.4, Swords Dance 29.3, Dragon Dance 24.7.
  - Adamant 73.8 / Jolly 23.8. Spread 1/32/1/0/0/32 (32.4).
- **Seen on Showdown** (S4): brought 46%, Mega Evolved in 14% of registrations. Won 56% (41–70, n=43).
- **Speed:** 152 / 139, the same as its Mega. +1 is 228 / 208.
- **Partners** (S1): Garchomp, Primarina, Salamence, Lucario, Hippowdon, Golisopod. Sample: Ninetales + Baxcalibur (13 teams, lift 2.1) (S4).
- **What beats it**
  - **Data** (S4): 28 faints. Metagross 3, **Stealth Rock 3**, Swampert 3.
  - **Top players say:** Magcargo lists its weaknesses as not OHKOing Hippowdon, being weak to rocks, and having common checks in Mega Lucario, Golisopod, Scizor, Primarina and Alolan Ninetales (S12; paraphrase). HazelGrayble adds that Dragonite "could 1v1 Focus Sash Baxcalibur" with Extreme Speed (S11).
  - **My read:**
    - **Stealth Rock breaks its Sash** (25% chip).
    - After **Glaive Rush** it takes 2× damage until its next turn (S15), which is a free revenge window.
    - Revenge options: Metagross Bullet Punch, Lucario Z Vacuum Wave or Aura Sphere, Pawmot Mach Punch.
    - Do not rely on burn or Fire: Will-O-Wisp fails, and Fire attacks (neutral damage) raise its Attack (Thermal Exchange).

## 6. Mega Golisopod: #6 (NEW) · 21.7%
- **Profile** (S15):
  - Base: Bug/Water, Emergency Exit.
  - **Mega: Bug/Steel, 75/150/175/70/120/40, Tough Claws** (contact moves 1.3×).
  - **Only weakness: Fire ×4.** Resists 7 types and Grass ×¼. Immune Poison.
- **Sets** (S1): Golisopite 97.9. Iron Head 73.3, Sucker Punch 63.5, First Impression 62.5, Leech Life 43.2, U-turn 35.0, Drill Run 30.7, Swords Dance 26.5, Close Combat 20.1, Aqua Jet 16.6. Adamant 82.6 / Brave 12.3. Spread 32/32/0/0/2/0 (26.0).
- **Trend:** First Impression is falling while Sucker Punch, Aqua Jet, Swords Dance and Drill Run are rising (forum observation, S11, 2026-09-25).
- **Seen on Showdown** (S4): brought 45%, Mega Evolved in 42% of registrations, lead 15%. Won 46% (32–61, n=41). Moves seen: Leech Life 19, Sucker Punch 12, Bulk Up 11, Drill Run 11, Aqua Jet 10, Swords Dance 9.
- **Speed:** 60 (54 with Brave). It relies on priority: First Impression +2, Sucker Punch +1, Aqua Jet +1, all contact.
- **Partners** (S1): Garchomp, Primarina, Salamence, Baxcalibur, Hippowdon, Gholdengo.
- **What beats it**
  - **Data** (S4): 25 faints. Salamence 4, Pelipper 3, Swampert 3.
  - **Top players say:** "more like an answer to whatever your mega is weak to rather than a main mega" (JoeyJoestar, S12). Aegislash "has little ground to stand on into Golisopod" (HazelGrayble, S11).
  - **My read:**
    - **Fire.** The field is full of it: Cinderace Pyro Ball 99%, Charizard, Rotom-Heat (Levitate), Volcarona, Indeedee Mystical Fire 92%, Dragonite Flamethrower 53%, Garchomp Flamethrower 28%, Gyarados Temper Flare 38%.
    - Intimidate and Will-O-Wisp (Rotom-Wash 82%) blunt it.
    - **Psychic Terrain blocks all its priority** against grounded targets. Aura Guard halves its contact moves.

## 7. Mega Lucario Z: #7 (M-5 #29) · 14.9%
- **Profile** (S15): **Mega Z: Fighting/Steel, 70/100/70/164/70/151, Aura Guard** (takes ½ damage from contact moves).
  - Weak Fighting, Fire, Ground. Resists Dark, Dragon, Grass, Ice, Normal, Steel, plus Bug and Rock ×¼. Immune Poison.
- **Sets** (S1): **Lucarionite Z 91.0** (regular Lucarionite 8.2). Dark Pulse 78.6, **Nasty Plot 76.8**, Flash Cannon 72.4, Aura Sphere 72.2, Vacuum Wave 38.7, Steel Beam 22.4. Timid 66.1 / Modest 26.5. Spread 2/0/0/32/0/32 (52.5).
  - This replaced last season's physical Mega Lucario (Close Combat, Swords Dance, Meteor Mash, Extreme Speed) (S2).
- **Seen on Showdown** (S4): brought 49%, Mega Evolved in 47% of registrations (38 Z-Megas, 4 regular). **Won 57% (42–70, n=44).**
- **Speed:** **223** (Timid) / 203 (Modest). Before Mega (Timid): 156.
- **Partners** (S1): Salamence, Primarina, Hippowdon, Garchomp, Baxcalibur, Rillaboom.
- **What beats it**
  - **Data** (S4): 25 faints. Garchomp 4, Swampert 4, Indeedee 2, Metagross 2, Basculegion 2.
  - **Top players say:** "This Pokemon is a trade demon. Having the highest speed in the metagame …"; "Steel Beam also gives it nuclear Power"; "it does get annoyed by Earthquake and a few Pokemon such as Toxapex" (Magcargo, S12, 2026-09-12). "Contact moves at all look bad into Lucario" (HazelGrayble, S11).
  - **My read:**
    - **Faster Ground or Fire hits:** Scarf Garchomp Earthquake (253/231 > 223), Scarf Cinderace Pyro Ball (non-contact, 282).
    - Slower bulky Ground types (Hippowdon, Swampert) must survive a hit first. Test this in the Lab.
    - Gholdengo is immune to Aura Sphere and Vacuum Wave and resists Flash Cannon, but **Dark Pulse (79%) hits it super-effectively**, so it is not a safe answer.
    - **Most priority makes contact and is halved** by Aura Guard (brief H1).

## 8. Archaludon: #8 (M-5 #4) · 23.5%
- **Profile** (S15): **Steel/Dragon, 90/105/130/125/65/85. Stamina** (+1 Defense when hit) or **Sturdy.**
  - Weak Fighting, Ground. Resists 8 types (including Flying, so Salamence's Double-Edge) and Grass ×¼. Immune Poison.
- **Sets** (S1): Draco Meteor 70.9, Flash Cannon 64.2, Thunderbolt 63.0, Stealth Rock 62.4, Roar 26.4, Dragon Tail 24.6, Electro Shot 15.0.
  - Items: Sitrus 37.5, Leftovers 23.3, Scarf 9.2, White Herb 9.0.
  - Natures: Modest 30.4 / Bold 29.6 / Calm 19.6. Offensive 2/0/0/32/0/32 (15.7) and bulky 32/0/2/0/32/0 (11.8) spreads are both common.
- **Seen on Showdown** (S4): brought 56%, lead 29%. **Won 60% (47–72, n=55), the best of the top 10.** Moves seen: Stealth Rock 23, Flash Cannon 20, Draco Meteor 20, Electro Shot 7.
- **Speed:** 150 / 137 / 105 (0 SP).
- **Partners** (S1): Salamence, Primarina, Garchomp, Golisopod, Lucario, Rillaboom. In rain, Electro Shot needs no charge turn (S15).
- **What beats it**
  - **Data** (S4): 44 faints. Swampert 6, Salamence 4.
  - **My read:**
    - **Ground:** Earthquake or Earth Power from Garchomp, Hippowdon, Baxcalibur (91% run Earthquake), Swampert.
    - **Fighting:** Lucario Z Aura Sphere, Sneasler, Cinderace High Jump Kick, Pawmot.
    - Avoid multi-hit physical moves into Stamina.

## 9. Gholdengo: #9 (M-5 #24) · 18.5%
- **Profile** (S15): **Steel/Ghost, 87/60/95/133/91/84. Good as Gold** (immune to status moves).
  - Weak Dark, Fire, Ghost, Ground. Immune Fighting, Normal, Poison.
- **Sets** (S1): Shadow Ball 98.6, Make It Rain 93.3, **Nasty Plot 84.1**, Recover 64.2, Thunderbolt 28.9. **Air Balloon 72.9 (new)**, Scarf 9.3, Leftovers 8.2. Modest 67.0 / Timid 16.7.
- **Seen on Showdown** (S4): brought 43%. **Won 37% (24–52, n=43).** Air Balloon was seen 22 times.
- **Speed:** 149 / 136 / 104.
- **Partners** (S1): Salamence, Primarina, Hippowdon, Garchomp, Baxcalibur, Lucario.
- **What beats it**
  - **Data** (S4): 27 faints. Swampert 5, Salamence 3.
  - **My read:**
    - Dark: Meowscarada Knock Off 69% or Sucker Punch, Lucario Z Dark Pulse 79%, Kingambit.
    - Ghost: Aegislash, Basculegion Last Respects, Mimikyu Shadow Claw.
    - Fire: Cinderace, Charizard.
    - Ground only after the Balloon pops. Any hit pops it (S15), so chip it first.

## 10. Rillaboom: #10 (NEW) · 13.2%
- **Profile** (S15): **Grass, 100/125/90/60/70/85, Grassy Surge.** Grassy Glide gets +1 priority in Grassy Terrain, and the terrain heals 1/16 per turn.
  - Weak Bug, Fire, Flying, Ice, Poison.
- **Sets** (S1): Grassy Glide 97.1, U-turn 71.8, Knock Off 63.1, High Horsepower 50.0, Drum Beating 49.0. Items: Life Orb 23.3, Miracle Seed 22.2, Terrain Extender 17.9, Grassy Seed 11.0. Adamant 87.3. Spread 32/32/0/0/0/2 (36.9).
- **Seen on Showdown** (S4): brought 41%, lead 20%. Won 36% (n=22).
- **Speed:** 107 (Grassy Glide is its speed control).
- **Partners** (S1): Salamence, Primarina, Lucario, Garchomp, Baxcalibur, Hippowdon.
- **What beats it** (my read): Pokémon that take Grass at ×¼ and hit back super-effectively: Mega Salamence (Flying Double-Edge), Mega Golisopod (Bug STAB), Corviknight (Brave Bird). Archaludon also takes Grass at ×¼ but has no super-effective move. Also Fire (Charizard, Cinderace) and Poison (Sneasler).

## 11. Mimikyu: #11 (M-5 #5) · 16.0%
- **Profile** (S15): **Ghost/Fairy, 55/90/80/50/105/96, Disguise** (blocks the first hit, takes 1/8 instead).
  - Weak Ghost, Steel. Immune Dragon, Fighting, Normal.
- **Sets** (S1): Play Rough 96.7, Shadow Sneak 95.1, Swords Dance 81.1, Shadow Claw 62.8, Curse 16.3. **Life Orb 80.6.** Adamant 77.2 / Jolly 17.6.
- **Seen on Showdown** (S4): brought 34%. **Won 34.5% (20–53, n=29).** Trick Room was seen 4 times.
- **Speed:** 162 / 148.
- **Partners** (S1): Garchomp, Salamence, Lucario, Primarina, Baxcalibur, Charizard.
- **What beats it**
  - **Data** (S4): 24 faints. Archaludon 7, **Life Orb recoil 3**.
  - **My read:**
    - Steel types hit it super-effectively and resist Play Rough: Archaludon, Metagross (Bullet Punch), Golisopod, Gholdengo (but Gholdengo takes super-effective Ghost damage), Lucario Z (Aura Guard halves Play Rough and Shadow Claw).
    - Multi-hit moves break Disguise.
    - Psychic Terrain blocks Shadow Sneak against grounded targets.

## 12. Meowscarada: #12 (M-5 #3) · 10.0%
- **Profile** (S15): **Grass/Dark, 76/110/70/81/70/123, Protean** (once per switch-in).
  - Weak **Bug ×4**, Fairy, Fighting, Fire, Flying, Ice, Poison. Immune Psychic.
- **Sets** (S1): Flower Trick 97.3, Triple Axel 91.4, Knock Off 69.2, U-turn 64.6, Sucker Punch 21.9. **Scarf 61.1** / Sash 22.9 / Life Orb 9.3. Jolly 62.7.
- **Seen on Showdown** (S4): brought 40%. Won 44% (n=25).
- **Speed:** 192 / 175. **Scarf: 288 / 262, the fastest common revenge killer.**
- **Partners** (S1): Primarina, Garchomp, Salamence, Hippowdon, Lucario, Golisopod.
- **What beats it** (my read):
  - **Mega Lucario Z** resists both STABs, outspeeds non-Scarf sets, and hits with super-effective Aura Sphere.
  - **Mega Golisopod** hits with ×4 Bug moves.
  - Primarina resists Dark and hits with Moonblast. Cinderace uses Pyro Ball.

## 13. Charizard (Mega Y / Mega X): #13 (M-5 #11) · 7.8%
- **Profile** (S15):
  - **Mega Y: Fire/Flying, 78/104/78/159/115/100, Drought.** Weak **Rock ×4**, Electric, Water.
  - **Mega X: Fire/Dragon, 78/130/111/130/85/100, Tough Claws.** Weak Dragon, Ground, Rock.
- **Sets** (S1): Charizardite Y 74.5 / X 24.1.
  - Mega Y: Solar Beam 72.8, Flamethrower 54.3, **Dragon Pulse 37.8**, Air Slash 34.2, Roost 31.0. Modest 51.8 / Timid 21.4.
  - Mega X: Flare Blitz 22.9 and Dragon Dance 16.4 overall.
- **Seen on Showdown** (S4): brought 66%, lead 24%, Mega Evolved 61% of registrations (19 Y, 4 X). Won 48% (n=25).
- **Speed:** 167 / 152 for both Megas.
- **Partners** (S1): Garchomp, Primarina, Baxcalibur, Mimikyu, Hippowdon, Archaludon.
- **What beats it** (my read):
  - **Stealth Rock** takes 50% from Mega Y. It is common: Hippowdon 90%, Glimmora 69%, Archaludon 62%, Garchomp 41%.
  - Rock attacks: Glimmora Power Gem 81%.
  - Against Mega Y only, Water or Electric: Primarina, Basculegion, Archaludon Thunderbolt, Rotom-Wash. Mega X takes Water neutrally and resists Electric.
  - You cannot tell X from Y at Team Preview.

## 14. Gyarados: #14 (M-5 #7) · 7.1%
- **Profile** (S15):
  - Base: **Water/Flying, 95/125/79/60/100/81, Intimidate.** Weak **Electric ×4**, Rock.
  - Mega: Water/Dark, 95/155/109/70/130/81, Mold Breaker. Weak Bug, Electric, Fairy, Fighting, Grass.
- **Sets** (S1): **Rocky Helmet 54.2** / Gyaradosite 22.2 (M-5: 74.1) / Leftovers 12.7.
  - Moves: Power Whip 67.5, Avalanche 56.7, Waterfall 55.5, **Taunt 51.6**, Earthquake 46.1, Temper Flare 38.0, Dragon Dance 31.0.
  - **Impish 45.2** / Adamant 34.0. Spread 32/2/32/0/0/0 (9.4).
- **Seen on Showdown** (S4): brought 66%. **Won 69% (51–83, n=29), the highest among frequently brought Pokémon.** Rocky Helmet was seen 10 times.
- **Speed:** 101 (Impish, 0 SP) / 133 / 146.
- **Partners** (S1): Garchomp, Lucario, Baxcalibur, Salamence, Hippowdon, Mimikyu.
- **What beats it**
  - **Data** (S4): 19 faints. Archaludon 5 (Thunderbolt or Electro Shot).
  - **My read:**
    - Electric: Archaludon (63% run Thunderbolt), Rotom-Wash, Pawmot Double Shock.
    - Special attackers ignore Intimidate and avoid Rocky Helmet.
    - Its Taunt shuts down Hippowdon and other setup and support Pokémon.

## 15. Sneasler: #15 (M-5 #48) · 5.0%
- **Profile** (S15): **Fighting/Poison, 80/130/60/40/80/120, Unburden.**
  - Weak **Psychic ×4**, Flying, Ground.
- **Sets** (S1): Close Combat 97.9, Dire Claw 96.5, Swords Dance 49.5, Throat Chop 47.5, Fake Out 40.3, Acrobatics 19.4. Items: **Psychic Seed 44.8, Normal Gem 31.8**, Grassy Seed 6.5. Adamant 85.2.
- **Seen on Showdown** (S4): Psychic Seed seen 7 times. Won 45% (n=11).
- **Speed:** 189 / 172. **After Unburden: 378 / 344.**
- **Partners** (S1): **Indeedee, Blastoise**, Salamence, Garchomp, Baxcalibur, Primarina. Indeedee + Sneasler lift 7.4 (S4).
- **What beats it**
  - **Data** (S4): 8 faints. Salamence 4, Gholdengo 2.
  - **My read:**
    - **Gholdengo and Aegislash are immune to both of its STABs** (Fighting and Poison). Throat Chop (48%) hits them super-effectively, though.
    - Corviknight is immune to Poison and takes Close Combat only neutrally.
    - Mega Salamence resists Fighting and hits with super-effective Flying.
    - Psychic moves hit it ×4. The most common Psychic attacker, Indeedee, is usually on Sneasler's own team, so look to opposing Metagross Psychic Fangs.

## 16. Cinderace: #16 (NEW) · 5.0%
- **Profile** (S15): **Fire, 80/116/75/65/75/119, Libero** (becomes the type of the move it uses, once per switch-in).
  - As a Fire type it is weak to Ground, Rock, Water.
- **Sets** (S1): Pyro Ball 99.3, High Jump Kick 91.2, Gunk Shot 86.1, Sucker Punch 46.2, U-turn 42.4. Items: Sash 27.2, **Scarf 26.5**, **Wide Lens 23.3**, Life Orb 17.8. Adamant 53.1 / Jolly 44.3.
- **Seen on Showdown** (S4): brought 63%, lead 32%. Won 58% (n=12).
- **Speed:** 188 / 171. Scarf 282 / 256.
- **Partners** (S1): Salamence, Primarina, Garchomp, Baxcalibur, Golisopod, Hippowdon.
- **What beats it** (my read): bulky Water types (Primarina, Basculegion with Aqua Jet, Gyarados), Ground types (Garchomp, Hippowdon). Beware that Libero changes its typing after the first move.

## 17. Glimmora: #17 (M-5 #18) · 11.4%
- **Profile** (S15): **Rock/Poison, 83/55/90/130/81/86, Toxic Debris** (a physical hit on it sets Toxic Spikes). Mega: Adaptability.
  - Weak **Ground ×4**, Psychic, Steel, Water.
- **Sets** (S1): Power Gem 81.1, Stealth Rock 69.1, Earth Power 62.0, Sludge Wave 51.9, Mortal Spin 27.9. Items: **Focus Sash 60.5**, Air Balloon 14.6, Glimmoranite 11.2, Red Card 8.6. Timid 49.5 / Modest 34.5.
- **Seen on Showdown** (S4): **lead 36%**, a hazard-setting lead. Won 36% (n=28). Moves seen: Stealth Rock 13, Earth Power 8, Mud Shot 8.
- **Speed:** 151 / 138.
- **Partners** (S1): Salamence, Primarina, Garchomp, Lucario, Gholdengo, Hippowdon.
- **What beats it** (my read):
  - Ground (×4), with a multi-hit or chip to break the Sash first.
  - Steel types (Archaludon, Gholdengo, Metagross). Water types.
  - Special attacks avoid triggering Toxic Debris.

## 18. Aegislash: #18 (M-5 #23) · 10.0%
- **Profile** (S15): **Steel/Ghost, Shield Forme 60/50/140/50/140/60, Blade Forme 60/140/50/140/50/60, Stance Change.**
  - Weak Dark, Fire, Ghost, Ground. Immune Fighting, Normal, Poison.
- **Sets** (S1): Shadow Sneak 95.8, King's Shield 83.3, Poltergeist 58.1, Shadow Ball 37.8, Sacred Sword 36.0, Swords Dance 27.6. Items: Leftovers 45.5, Spell Tag 23.2, Life Orb 12.5. Adamant 47.3 / Quiet 29.5.
- **Seen on Showdown** (S4): brought 24% when registered, the lowest bring rate in the top 20. n=11.
- **Speed:** 80 (72 with Quiet).
- **Partners** (S1): Salamence, Hippowdon, Primarina, Garchomp, Golisopod, Lucario.
- **What beats it**
  - **Top players say:** it "has not looked quite as dominant … contact moves at all look bad into Lucario … little ground to stand on into Golisopod. … I'd look at Gholdengo first" (HazelGrayble, S11).
  - **My read:** Dark (Lucario Z Dark Pulse, Meowscarada, Kingambit), Fire, Ground.

## 19. Corviknight: #19 (M-5 #14) · 7.8%
- **Profile** (S15): **Flying/Steel, 98/87/105/53/85/67. Pressure or Mirror Armor** (reflects stat drops such as Intimidate).
  - Weak Electric, Fire. Immune Ground, Poison.
- **Sets** (S1): Roost 98.9, U-turn 64.1, Body Press 59.8, Iron Defense 56.7, Iron Head 30.3, Brave Bird 26.8, Bulk Up 22.7, Defog 12.5. Items: **Rocky Helmet 62.8** (M-5: Leftovers 56.8), Leftovers 26.7. Impish 62.8. Spread 32/0/32/0/2/0 (41.2).
- **Speed:** 87 (78 with Relaxed).
- **Partners** (S1): Garchomp, Primarina, Salamence, Baxcalibur, Charizard, Hippowdon.
- **What beats it** (my read):
  - Fire and Electric special attacks: Charizard Y, Rotom-Heat or Wash, Archaludon Thunderbolt, Pawmot.
  - Taunt stops Iron Defense and Roost.
  - It is one of the few common Defog users that can remove Aurora Veil (brief H4).

## 20. Basculegion: #20 (M-5 #12) · 11.7%
- **Profile** (S15): **Water/Ghost, 120/112/65/80/75/78, Adaptability** (STAB is 2×).
  - Weak Dark, Electric, Ghost, Grass. Immune Fighting, Normal.
- **Sets** (S1): Last Respects 99.8, Wave Crash 95.3, Aqua Jet 88.2, Flip Turn 76.1. Items: **Scarf 70.7**, Life Orb 9.5, Mystic Water 7.4. Jolly 60.7 / Adamant 36.0.
- **Seen on Showdown** (S4): won 26% when brought (n=19).
- **Speed:** 143 / 130. **Scarf 214 / 195, which does NOT outspeed the +Spe Z-Megas at 223.**
- **Partners** (S1): **Pawmot**, Garchomp, Salamence, Golisopod, Banette, Archaludon. Basculegion + Pawmot lift 5.2 (S4).
- **What beats it**
  - **Data** (S4): 13 faints. Golisopod 3 (Sucker Punch).
  - **My read:** Dark priority (Golisopod or Meowscarada Sucker Punch), Grassy Glide, Electric attackers.
  - Last Respects gains power for every fainted ally (S15), so the longer the game goes the more dangerous it gets; remove it before trading down.

---

## Archetype enablers (ranks 21–30, compact)

- **Alolan Ninetales, #25 (M-5 #33)**
  - Ice/Fairy, weak **Steel ×4**, Fire, Poison, Rock (S15).
  - Set: Aurora Veil 97.3, Freeze-Dry 72.2, Encore 70.0, Blizzard 64.4, Moonblast 55.0. **Light Clay 90.3** (8-turn Veil). Snow Warning 99.8. Timid 85.0 (177 Speed) (S1).
    - PokéChamp DB's English page mislabels the ability as "Blizzard" because its own dictionary maps the Japanese name ゆきふらし to both entries. Snow Warning is correct.
  - Veil teams won 61% of sides (n=72) (S4).
  - Beats it: Steel attacks (Metagross Bullet Punch, Archaludon, Lucario Z), Taunt leads, screen removal (brief H4).
- **Indeedee (M), #21 (NEW)**
  - Psychic/Normal, weak Bug, Dark; immune Ghost (S15).
  - Set: Expanding Force 99.5, Mystical Fire 91.9, Encore 71.9, Dazzling Gleam 66.7, Healing Wish 18.5. **Terrain Extender 60.8** / Scarf 21.6 / Sash 12.5. Timid 161 / Scarf 241 Speed (S1).
  - **The highest lead rate of any Pokémon on 20 or more sample teams (46% of registrations).** Won 57% (n=30) (S4).
  - Beats it: Dark and Bug attacks without priority (priority fails against grounded targets in its terrain), such as Knock Off and U-turn.
- **Mega Blastoise, #24 (M-5 #43)**
  - Water, 79/103/120/135/115/78, **Mega Launcher** (pulse moves 1.5×) (S15).
  - Set: Blastoisinite 96.6. **Shell Smash 91.3, Aura Sphere 86.5, Dark Pulse 82.2, Terrain Pulse 74.6.** Modest 80.4 (S1).
  - Speed: +2 is 256 (Modest, 30 Spe) or 286 (Timid 32).
  - Beats it: Electric or Grass attacks before it sets up. Pawmot KO'd it 3 times out of 11 in the sample (S4). It is hard to revenge-kill under Psychic Terrain (brief H5).
- **Pawmot, #26 (NEW)**
  - Electric/Fighting, weak Fairy, Ground, Psychic (S15).
  - Set: Double Shock 93.9, **Revival Blessing 87.6**, Ice Punch 68.2, Close Combat 59.0, Mach Punch 53.9. **Focus Sash 90.9.** Iron Fist 94.2. Jolly 172 Speed (S1).
  - **Brought in 74% of games where it is registered**, the highest of the 45 most-registered Pokémon in the sample. Won 50% (n=32) (S4).
  - Beats it: Ground (Garchomp KO'd it 5 times in the sample), chip damage that breaks the Sash before its Revival Blessing turn.

## Watch list (next update)
- **Empoleon (#30, M-5 #74):** Stealth Rock, Yawn, Ice Beam; Shuca Berry or Air Balloon (S1). Unverified claim that it reached #1 (S12).
- **Mega Absol Z (#50, M-5 #162):** Dark/Ghost, Sharpness, 151 Speed (S15). Won a BSSCL II set (S4).
- **Rotom-Heat (#36):** Levitate Fire type that answers Golisopod.
- **Ditto (#51):** Imposter copies set-up Mega sweepers (S15).
- **Mega Dragalge + Sableye stall:** one high-rated player (S4).
- **Mega Metagross (#22):** Ice Punch 73.9, Psychic Fangs 76.7 (a screen breaker) (S1).

## Sources
Same keys as `brief-2026-09-28.md` §9. The main ones:
- **S1** PokéChamp DB, in-game M-6 Singles data: https://pokechamdb.com/en (snapshot 2026-09-27; T2)
- **S2** PokéChamp DB M-5 data (2026-09-06; T2)
- **S4** Scout's Showdown replay sample: https://replay.pokemonshowdown.com/search.json?format=gen9championsbssregmc (2026-09-11 → 09-28; T2)
- **S10** Game8 Battle Data page (T3)
- **S11** Smogon Champions Usage Ranking Changelog (2026-09-23 → 09-27; T2/T3)
- **S12** Smogon Champions BSS Viability Rankings thread (T2/T3)
- **S13** Smogon Champions Speed Tiers [Reg M-C] (edited 2026-09-12; T2)
- **S15** Showdown public data: https://play.pokemonshowdown.com/data/pokedex.json, moves.json, abilities.js, items.js, typechart.js (accessed 2026-09-28; T2)
