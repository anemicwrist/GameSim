---
slug: z-guard-balance
mode: singles
season: Ranked Season M-6 / Regulation M-C (still applies in M-7 if the roster stays M-C)
status: proposed
confidence: calc-verified   # damage and speed benchmarks from the Showdown calc's Champions mode; the matchup verdicts are theory only until tested
priority: 3 × 4 ÷ 3 = 4.0
created: 2026-09-28
updated: 2026-09-28
---
<!-- Lab: copy to lab/hypotheses/<slug>.md. Method: .claude/agents/lab.md, "Research cycle". -->

# Z-Guard Balance: Mega Lucario Z + Rocky Helmet Gyarados + Choice Scarf Garchomp

**Priority score:**
- **Edge 3.** The team is built from three strong performers in the Scout's sample plus fixes for holes H1–H3. It has
  no surprise factor.
- **Trainer fit 4.** One fast Mega that outspeeds nearly everything, a default pick of three, bulky pivots, and few
  50/50 guesses.
- **Effort 3.** All six have to be built from scratch: one 2,000 VP Mega Stone, five other items, and training.
- HYP-2 (`veil-mode-ninetales-slot`) and HYP-3 (`metagross-veil-breaker-slot`) each swap one slot of this team.

## 1. Proposal

### The idea
A balance team for climbing Ranked Singles in the meta the forecast expects for mid-to-late October:
- **The core** is three strong performers from the Scout's M-C sample. Defensive Gyarados is one of only two Pokémon
  brought 10+ times whose win-rate interval sits entirely above 50%. Archaludon and Mega Lucario Z have the two best win
  rates in the usage top 10.
- **Two answers to the brief's holes** complete it: Choice Scarf Garchomp (253 Speed, non-contact Earthquake) above the
  223 Z-Mega ceiling, and Primarina for Dragons and Encore.
- **Rotom-Heat** covers Mega Golisopod and Grassy Terrain.
- There is **one Mega**. The default pick is Lucario Z + Gyarados + Archaludon, with clear swap rules at Team Preview.

### Why it should work now
1. **The core is built from the sample's winners.**
   - Win rate when brought: Gyarados **69%** (CI 51–83, n=29), Archaludon **60%** (47–72, n=55), Mega Lucario Z **57%**
     (42–70, n=44) (brief §3, S4).
   - Gyarados is one of only two Pokémon brought 10+ times whose whole CI sits above 50% (the other is Umbreon, 82%,
     n=11). Archaludon and Lucario have the two best win rates in the usage top 10.
   - The samples are small (see §3, red team). The team doesn't rely on those rates. It relies on the calcs in §2.
2. **H1: Aura Guard against a contact-priority meta.**
   - Aura Guard halves damage from contact moves. The field's common priority moves all make contact (brief §6 H1; S1,
     S15).
   - Calc-verified damage to our Lucario Z:

     | Priority move | Damage |
     |---|---|
     | Life Orb Mimikyu Shadow Sneak | 18–21% |
     | Mega Golisopod Sucker Punch | 14–17% |
     | Kingambit Sucker Punch | 15–18% |
     | Scarf Basculegion Aqua Jet | 19–23% |
     | Pawmot Mach Punch | 35–41% |
     | Baxcalibur Ice Shard (the common non-contact option) | 18–22% |
3. **H2: the 223 speed ceiling.**
   - Choice Scarf Jolly Garchomp reaches 253. Earthquake is non-contact, so Aura Guard doesn't apply.
   - Earthquake OHKOs Mega Lucario Z (155–184%) and Outrage OHKOs Mega Garchomp Z (128–150%). Calc-verified.
4. **H3: Mega Salamence is over-picked.**
   - It is on 33.8% of teams but won 40% when brought. 8 of its 48 faints were its own recoil, and Rocky Helmet use has
     surged (brief H3; S1, S4).
   - Gyarados (Intimidate + Rocky Helmet + Avalanche) and Archaludon (resists its Flying-type Double-Edge) each beat it
     one-on-one (§2).
5. **Forecast fit** (`lab/forecast-singles-2026-09-28.md`).
   - R3 and R4 predict Gyarados and Archaludon rise: this team fields both.
   - R5 predicts more Scarf users: this team already sits at 253.
   - F1 says Salamence stays on about a third of teams: this team's punishers keep meeting it.

### Target matchups
- The two most common shells: Salamence + Hippowdon balance (brief §4.1) and standard Salamence goodstuffs (§4.7).
- Grassy offense (§4.5) and Revival Blessing (§4.6).
- Mega Lucario Z, Mega Golisopod, Gholdengo, Archaludon, Rillaboom.

### Expected weaknesses
- An enemy Lucario Z behind Aurora Veil.
- Rain.
- Pawmot.
- Mega Charizard Y.
- +2 Mega Blastoise in Psychic Terrain.
- A +1 Mega Salamence (258/283 Speed) outruns everything on the team.

### Legality
- **Pokémon.** All six species are on the official Regulation M-C eligible list: Lucario, Gyarados, Garchomp, Primarina,
  Archaludon, and Rotom (Heat Rotom) (L3). Heat Rotom counts as Rotom for Species Clause, and there is only one Rotom.
- **Mega.** Mega Lucario Z is allowed from M-C (official notice #816, L4). One Mega per battle (regulations §2).
- **Items.** Lucarionite Z, Rocky Helmet, Choice Scarf, Sitrus Berry, Leftovers and White Herb are six different items
  (Item Clause). All are in the Champions item list (mechanics §8): Rocky Helmet, Choice Scarf, Leftovers and White Herb
  are held items, Sitrus is a Berry, and Lucarionite Z is one of the 81 Mega Stones.
- **Moves and abilities.** Every move and ability below is in that Pokémon's Champions learnset on Serebii's Champions
  Pokédex (L2).

### Builds on
- **Every set is close to the in-game consensus** (brief §3, S1; Rotom-Heat from its S1 page).
  - Lucario Z: Nasty Plot, Dark Pulse, Flash Cannon, Aura Sphere, Timid 2/0/0/32/0/32 (52.5%).
  - Gyarados: Rocky Helmet, Impish 32/2/32, Avalanche, Earthquake, Taunt, Temper Flare.
  - Scarf Garchomp.
  - Primarina: Moonblast, Sparkling Aria, Encore, Aqua Jet.
  - Archaludon: Draco Meteor, Flash Cannon, Thunderbolt, Stealth Rock.
  - Rotom-Heat: Overheat 97.8%, Volt Switch 90.5%, Will-O-Wisp 77.5%, Pain Split 33.1%, Bold 43.5%.
  - The Lab's changes are the combination, the Speed-creep points, the item assignment, and the game plan.
- **Credits:**
  - Magcargo, on Lucario Z as a "trade demon" with the top Speed.
  - HazelGrayble: "contact moves at all look bad into Lucario" (S11, S12).
  - JoeyJoestar, on Rotom-Heat as anti-Golisopod and anti-Salamence (S12).
  - The Scout's holes H1–H3 (brief §6).

### The team

SP order is HP/Atk/Def/SpA/SpD/Spe. Stats are at Level 50: HP = Base + SP + 75, others = ⌊(Base + SP + 20) × nature⌋
(mechanics §2). Every benchmark is calc-verified (method in §2).

**1. Lucario → Mega Lucario Z @ Lucarionite Z**
- **Ability:** Inner Focus, then Aura Guard after Mega Evolution.
- **Stat Alignment:** Timid.
- **SP:** 2 / 0 / 0 / 32 / 0 / 32.
- **Stats:** Mega 147 / 108 / 90 / 216 / 90 / **223**. Before Mega: Speed 156.
- **Moves:** Nasty Plot, Flash Cannon, Aura Sphere, Dark Pulse.
- **Benchmarks this spread hits:**
  - 223 Speed ties the +Spe Z-Megas, and beats Scarf Basculegion (214), Meowscarada (192) and Mega Salamence (189).
  - Flash Cannon OHKOs the common 2-HP Alolan Ninetales **through Aurora Veil** (109–129%).
  - Aura Sphere OHKOs offensive Archaludon (138–163%), Hisuian Samurott and Meowscarada.
  - Dark Pulse OHKOs Aegislash once it's in Blade Forme (after it attacks; 110–131%) and 2HKOs Gholdengo (72–85%).
    Against Shield Forme it does 49–59%.

**2. Gyarados @ Rocky Helmet**
- **Ability:** Intimidate. **Stat Alignment:** Impish.
- **SP:** 32 / 2 / 32 / 0 / 0 / 0.
- **Stats:** 202 / 147 / 144 / 72 / 120 / 101.
- **Moves:** Avalanche, Earthquake, Taunt, Temper Flare.
- **Benchmarks this spread hits:**
  - Takes Mega Salamence's Double-Edge at +0 (a +1 Salamence after Intimidate) for 61–72%. Then Avalanche, doubled
    because Gyarados was hit first, OHKOs it (105–124%).
  - Takes +2 Lucario Z Flash Cannon for 40–48%.
  - Earthquake 2HKOs Lucario Z (84–99%).
  - Temper Flare does 48–57% to Mega Golisopod (81% to 2HKO).

**3. Garchomp @ Choice Scarf**
- **Ability:** Rough Skin. **Stat Alignment:** Jolly.
- **SP:** 2 / 32 / 0 / 0 / 0 / 32.
- **Stats:** 185 / 182 / 115 / 90 / 105 / 169, which is **253** Speed with the Scarf.
- **Moves:** Earthquake, Outrage, Stone Edge, Fire Fang.
- **Benchmarks this spread hits:**
  - 253 Speed is above the 223 tier, Scarf Indeedee (241) and +1 Jolly Baxcalibur (228).
  - Earthquake OHKOs Mega Lucario Z (155–184%), Cinderace, Pawmot (Focus Sash permitting) and Glimmora. It hits
    Indeedee for 99–118% (94% to OHKO).
  - Outrage OHKOs Mega Garchomp Z (128–150%) and non-Sash Baxcalibur.
  - Stone Edge OHKOs Mega Charizard Y (181–214%).

**4. Primarina @ Sitrus Berry**
- **Ability:** Torrent. **Stat Alignment:** Modest.
- **SP:** 32 / 0 / 0 / 32 / 0 / 2.
- **Stats:** 187 / 84 / 94 / 195 / 136 / 82.
- **Moves:** Moonblast, Sparkling Aria, Encore, Aqua Jet.
- **Benchmarks this spread hits:**
  - Moonblast OHKOs Mega Salamence (112–133%), both Garchomp forms (108–128%) and non-Sash Baxcalibur (104–123%).
  - Sparkling Aria OHKOs Cinderace and Glimmora.
  - 82 Speed beats uninvested Primarina and Aegislash (80), so it moves first in the mirror.

**5. Archaludon @ Leftovers**
- **Ability:** Stamina. **Stat Alignment:** Modest.
- **SP:** 32 / 0 / 0 / 32 / 0 / 2.
- **Stats:** 197 / 112 / 150 / 194 / 85 / 107.
- **Moves:** Draco Meteor, Flash Cannon, Thunderbolt, Stealth Rock.
- **Benchmarks this spread hits:**
  - Draco Meteor OHKOs Mega Salamence (151–179%) and Mega Garchomp Z.
  - Thunderbolt OHKOs Impish Gyarados (111–131%) and Pelipper.
  - Flash Cannon has an 87.5% chance to OHKO 2-HP Alolan Ninetales through Veil.
  - 107 Speed beats uninvested Archaludon (105) and Gholdengo (104).

**6. Rotom-Heat @ White Herb**
- **Ability:** Levitate. **Stat Alignment:** Bold.
- **SP:** 32 / 0 / 30 / 2 / 0 / 2.
- **Stats:** 157 / 76 / 172 / 127 / 127 / 108.
- **Moves:** Overheat, Volt Switch, Will-O-Wisp, Pain Split.
- **Benchmarks this spread hits:**
  - Overheat OHKOs Mega Golisopod (147–174%), Gholdengo (102–122%) and Mega Lucario Z (140–167%). It hits Rillaboom for
    100–119% (94% to OHKO).
  - Takes Golisopod's Sucker Punch for 29–34% and Close Combat for 48–57%, and Mega Salamence's Double-Edge for 32–38%.
  - 108 Speed beats Rillaboom (107).
  - White Herb resets the first Overheat's Sp. Atk drop, so Rotom gets two full-power Overheats.

**Showdown import.** In Champions formats, Showdown's teambuilder uses Points (32 cap, 66 total), and the export writes
them on the `EVs:` line (L5, inferred from the client code; check that the teambuilder shows "Points" after import).

```
Lucario @ Lucarionite Z
Ability: Inner Focus
EVs: 2 HP / 32 SpA / 32 Spe
Timid Nature
- Nasty Plot
- Flash Cannon
- Aura Sphere
- Dark Pulse

Gyarados @ Rocky Helmet
Ability: Intimidate
EVs: 32 HP / 2 Atk / 32 Def
Impish Nature
- Avalanche
- Earthquake
- Taunt
- Temper Flare

Garchomp @ Choice Scarf
Ability: Rough Skin
EVs: 2 HP / 32 Atk / 32 Spe
Jolly Nature
- Earthquake
- Outrage
- Stone Edge
- Fire Fang

Primarina @ Sitrus Berry
Ability: Torrent
EVs: 32 HP / 32 SpA / 2 Spe
Modest Nature
- Moonblast
- Sparkling Aria
- Encore
- Aqua Jet

Archaludon @ Leftovers
Ability: Stamina
EVs: 32 HP / 32 SpA / 2 Spe
Modest Nature
- Draco Meteor
- Flash Cannon
- Thunderbolt
- Stealth Rock

Rotom-Heat @ White Herb
Ability: Levitate
EVs: 32 HP / 30 Def / 2 SpA / 2 Spe
Bold Nature
- Overheat
- Volt Switch
- Will-O-Wisp
- Pain Split
```

### Game plan

**Win conditions:**
1. Mega Lucario Z at 223 cleans up once its checks are removed or chipped. Its checks are Ground and Fire attackers,
   Gyarados and Primarina.
2. Gyarados and Archaludon absorb the physical Dragons and chip them with Rocky Helmet and recoil. Primarina and
   Garchomp then revenge-kill.

**Default pick: Lucario Z + Gyarados + Archaludon.** It covers both of the most common shells (brief §4.1 and §4.7).
Swap by the preview cues below.

| Opponent's 6 looks like (brief §4) | Bring | Lead | Plan in one line |
|---|---|---|---|
| Salamence + Hippowdon balance (4.1) | Gyarados, Archaludon, Lucario Z | Gyarados | Taunt Hippowdon on turn 1 (no Stealth Rock or Yawn). Intimidate Salamence. Archaludon takes Double-Edge and fires Draco Meteor. Lucario Z Dark Pulses Gholdengo or Aegislash |
| Standard Salamence goodstuffs (4.7) | Gyarados, Archaludon, Lucario Z (Primarina for Lucario if they show 3 Dragons) | Archaludon | Stealth Rock on turn 1, then Draco Meteor or Thunderbolt. Gyarados takes Salamence. Lucario cleans |
| Aurora Veil + setup (4.2) | Lucario Z, Gyarados, Primarina | Lucario Z | Mega and Flash Cannon the Ninetales on turn 1. Gyarados walls their Lucario Z. Primarina Encores Baxcalibur or Samurott setup |
| Rain (4.4) | Archaludon, Garchomp, Primarina | Archaludon | Thunderbolt the Pelipper. Garchomp is immune to Electro Shot and revenge-kills. Primarina resists Water. No Mega this game |
| Psychic Terrain (4.3) | Lucario Z, Primarina, Rotom-Heat | Lucario Z | Dark Pulse Indeedee. Primarina Encores Shell Smash. Rotom Volt Switches into Blastoise and burns Sneasler |
| Grassy offense (4.5) | Rotom-Heat, Gyarados, Lucario Z | Rotom-Heat | Rotom walls and Overheats Rillaboom. Gyarados takes Salamence. Lucario at +2 handles Primarina |
| Revival Blessing / Last Respects (4.6) | Lucario Z, Garchomp, Archaludon | Lucario Z | Dark Pulse Basculegion or Banette. Garchomp Earthquakes Pawmot (twice if the Sash holds) |
| Anything else | Default pick | Archaludon; Gyarados if they show Cinderace, Charizard, Golisopod or Garchomp | Stealth Rock, then trade into the Lucario Z cleanup |

**Seven rules for the 45-second turn timer:**
1. **Mega Evolve Lucario the first turn it's in.** At 223 it moves first against everything except Choice Scarf users,
   boosted sweepers, and other +Spe Z-Megas, which speed-tie it.
2. **Don't Nasty Plot in front of Primarina, Alolan Ninetales or Indeedee.** They carry Encore on 50%, 70% and 72% of
   sets (S1). Don't try to set up through Gyarados either: +2 Flash Cannon does only 40–48%. Switch out instead.
3. **Gyarados comes in on Salamence, Garchomp, Golisopod, Lucario Z and Hippowdon.** Against a Salamence that just used
   Dragon Dance, switch to Gyarados, then click Avalanche. It goes last on purpose and doubles in power.
4. **Scarf Garchomp comes in after a faint to revenge-kill.** Never switch it into an attack. The default click is
   Earthquake. Use Outrage into Dragons and Stone Edge into Charizard or Ninetales.
5. **Primarina clicks Encore the turn after the opponent sets up or uses a status move.** Otherwise it Moonblasts Dragons
   and uses Sparkling Aria on the rest.
6. **Archaludon sets Stealth Rock on turn 1 unless it would be OHKO'd.** Then it uses Draco Meteor on Dragons,
   Thunderbolt on Water and Flying types, and Flash Cannon on Fairy and Ice types.
7. **Rotom-Heat Volt Switches when a switch is likely.** It burns physical attackers, but never Baxcalibur (Thermal
   Exchange blocks burns and Fire boosts it). Overheat finishes things.

## 2. Theory check

**Damage calcs:**
- **Tool.** Pokémon Showdown's damage calculator in Champions mode. Its library files, including
  `calc/mechanics/champions.js`, were fetched from calc.pokemonshowdown.com on 2026-09-28 and run in Node 22 with
  gen 0 = Champions (L1).
- **Why it's trusted.** The Scout verified that this calc models Champions: the SP stat formula, the Champions move
  changes, and Aura Guard (`knowledge/sources.md` §7). The stats it printed match the mechanics.md formula.
- **Label.** **calc-verified**, meaning Showdown's model of Champions, not checked against the game client.
- **Opponent sets.** The most common in-game M-6 spread and nature from brief §3 (S1). Examples: Mega Salamence Adamant
  1/32/1/0/0/32; Lucario Z Timid 2/0/0/32/0/32; Primarina Modest 32/0/20/14/0/0; Hippowdon Impish 32/0/32/0/2/0 or
  Careful 32/0/2/0/32/0; Baxcalibur Adamant 1/32/1/0/0/32 with Focus Sash; Gyarados Impish 32/2/32/0/0/0 with Rocky
  Helmet; Alolan Ninetales Timid 2/0/0/32/0/32 (S1, 23.4%).
- **Not modeled.** Critical hits, Stealth Rock and weather chip, Stamina boosts, Leftovers and Sitrus timing, Helmet and
  recoil damage.
- **Notation.** In the calc's output, "32+" means 32 SP with a boosting Stat Alignment, and "0-" means a lowering one.

Key results (copied from the calc output):
- **Lucario Z (offense)**
  - 32 SpA Mega Lucario Z Flash Cannon vs. 2 HP / 0 SpD Ninetales-Alola with Aurora Veil: **109.3–129.3%, guaranteed
    OHKO**. Against 32 HP / 0 SpD it's 91.1–107.7%, 50% to OHKO.
  - Aura Sphere vs. 2 HP / 0 SpD Archaludon: 137.7–162.8% (OHKO). vs. 32 HP / 32+ SpD Archaludon: 77.1–92.3%.
  - Dark Pulse vs. 2 HP / 0 SpD Gholdengo: 71.9–85.3% (2HKO). vs. 32 HP / 1 SpD Aegislash-Blade: 110.1–130.5% (OHKO).
    vs. Aegislash-Shield: 49.1–58.6%.
  - Flash Cannon vs. 1 HP / 0 SpD Baxcalibur: 97.3–114.1% (81.3% to OHKO, but Focus Sash).
  - +2 Flash Cannon vs. 32 HP Primarina: 77.0–90.3%. +2 vs. 32 HP / 32+ Def Gyarados: 40.0–47.5%.
- **Contact priority into Lucario Z (H1)**
  - Life Orb Mimikyu Shadow Sneak: 17.6–21%.
  - Mega Golisopod Sucker Punch: 14.2–17%.
  - Kingambit Sucker Punch: 14.9–18.3%.
  - Pawmot Mach Punch: 34.6–41.4%.
  - Primarina Aqua Jet: 7.4–8.8%.
- **What does kill Lucario Z (the answers the field will move to)**
  - Scarf Garchomp Earthquake: 155.1–183.6%.
  - Hippowdon Earthquake: 114.2–134.6%.
  - Mega Salamence Earthquake: 122.4–145.5%.
  - Baxcalibur Earthquake: 122.4–145.5%.
  - Cinderace Pyro Ball: 172.7–204%.
  - Mega Charizard Y Fire Blast in sun: 326–385%.
  - Mega Garchomp Z Earth Power: 99.3–117%, 87.5% to OHKO.
- **Gyarados**
  - Takes Mega Salamence Double-Edge (Aerilate) at +0: 60.8–71.7%. At +1 with no Intimidate: 90.5–106.9%.
  - Avalanche at 120 BP vs. Mega Salamence: 105.2–123.9%, OHKO. vs. Garchomp: 125.4–149.1%.
  - Earthquake vs. Lucario Z: 84.3–99.3%. Temper Flare vs. 32 HP Mega Golisopod: 48.3–57.1%.
  - Takes -1 Mega Golisopod Sucker Punch: 17.8–21.2%.
- **Scarf Garchomp**
  - Earthquake vs. Lucario Z: 155–184%. With Aurora Veil it drops to 77.5–91.8%.
  - Outrage vs. Mega Garchomp Z: 127.5–150.2%. vs. Mega Salamence: 95.9–113.4% at +0 and 64.3–77.1% at -1.
  - Stone Edge vs. Mega Charizard Y: 180.6–214.1%. vs. Ninetales-Alola: 97.3–114.6%.
- **Primarina**
  - Moonblast vs. Mega Salamence: 112.2–133.3%. vs. Garchomp or Mega Garchomp Z: 108.1–127.5%. vs. non-Sash
    Baxcalibur: 103.6–122.5%.
  - Sparkling Aria vs. Careful Hippowdon: 67.9–80.9%.
  - Takes Mega Garchomp Z Earth Power: 26.2–31%. Takes +0 Baxcalibur Earthquake: 46.5–55%.
  - Is OHKO'd by: Mega Salamence Double-Edge (99.4–117.6%), Rillaboom Grassy Glide in terrain (116.5–139%), Pawmot
    Double Shock (154–183%), Sneasler Dire Claw (102.6–121.9%).
- **Archaludon**
  - Draco Meteor vs. Mega Salamence: 150.8–178.9%. Thunderbolt vs. Impish Gyarados: 110.8–130.6%. Thunderbolt vs.
    Primarina: 52.4–62%.
  - Takes +1 Mega Salamence Double-Edge: 44.1–52.2%. Takes +1 Earthquake: 83.2–98.4%.
  - Takes Mega Garchomp Z Earth Power: 78.1–92.3%.
- **Rotom-Heat**
  - Overheat vs. Mega Golisopod: 147.2–173.6%. vs. Gholdengo: 102.4–121.9%. vs. Lucario Z: 140.1–167.3%. vs. Lucario Z
    behind Veil: 70–83.6%.
  - Takes Golisopod Close Combat: 48.4–57.3%. Takes Primarina Sparkling Aria: 89.1–107%.

**Speed benchmarks** (ours in bold; field values from threats.md §0):

| Speed | Pokémon |
|---|---|
| 288 / 282 | Scarf Meowscarada / Scarf Cinderace (Jolly) |
| 283 / 258 | Mega Salamence after one Dragon Dance (Jolly / Adamant): outruns everything we have |
| **253** | **Scarf Garchomp** (a Jolly Scarf Garchomp mirror is a speed tie) |
| 241 / 228 | Scarf Indeedee / +1 Jolly Baxcalibur |
| **223** | **Mega Lucario Z**: ties Mega Garchomp Z, Mega Lucario Z and Mega Absol Z with +Spe |
| 214 | Scarf Basculegion |
| 189 / 172 | Mega Salamence (Jolly / Adamant) |
| 177 | Alolan Ninetales (Timid) |
| 156 | Our Lucario before Mega. Matters on the Mega turn if Champions doesn't apply Mega Speed that turn (FACT_CHECK) |
| 150 / 149 | Archaludon / Gholdengo (max Speed) |
| **108** | **Rotom-Heat**: beats Rillaboom (107), uninvested Archaludon (105) and Gholdengo (104) |
| **107** | **Archaludon** |
| **101** | **Gyarados**: beats Hippowdon (67), so Taunt lands first |
| **82** | **Primarina**: beats uninvested Primarina and Aegislash (80) |

**Matchups against the top 10 threats (in-game M-6 order) and the four main archetypes:**

| Top threat / archetype | Verdict | Why | Main answer |
|---|---|---|---|
| Mega Salamence (33.8% of teams) | **Favored** | Gyarados takes its Double-Edge at +0 for 61–72%. Each Double-Edge also costs Salamence 1/6 from Rocky Helmet and 1/3 of the damage in recoil. Avalanche then OHKOs (105–124%). Archaludon takes a +1 Double-Edge for 44–52% and OHKOs with Draco Meteor, but a +1 Earthquake does 83–98% to it. Primarina OHKOs Salamence but is OHKO'd by Double-Edge (94%), so it only comes in after a faint | Gyarados, Archaludon |
| Garchomp / Mega Garchomp Z (31.0%) | **Favored** | Primarina OHKOs both forms, is immune to Dragon moves, and takes special Mega Z's Earth Power for 26–31%. Gyarados is immune to Earthquake, and Avalanche OHKOs base Garchomp. Archaludon's Draco Meteor OHKOs Mega Z. Risk: Scarf Garchomp OHKOs Lucario Z, and special Mega Z has an 87.5% OHKO on it | Primarina, Gyarados |
| Primarina (28.5%) | **Even** | Archaludon (107 Speed vs 80) Thunderbolts for 52–62% and takes 56–67% back from Moonblast. With Sitrus or Leftovers it's a close 2HKO race. +2 Lucario hits 77–90%, but Primarina's Encore punishes Nasty Plot. Rotom-Heat loses: Volt Switch does 40–48%, and Sparkling Aria does 89–107% back | Archaludon; Lucario Z once Primarina is chipped |
| Hippowdon (13.2%) | **Favored** | Gyarados (101) Taunts first, which blocks Stealth Rock, Yawn, Whirlwind and Slack Off. Hippowdon's only attack, Earthquake, can't touch Gyarados. Primarina's Sparkling Aria does 68–81%. Risk: its Earthquake OHKOs Lucario Z (114–135%) | Gyarados, Primarina |
| Baxcalibur (16.7%; Focus Sash on 46.9%) | **Even** (favored with Stealth Rock up) | Lucario's Flash Cannon has an 81% OHKO chance, but the Sash holds and Baxcalibur's Earthquake then OHKOs Lucario. Stealth Rock breaks the Sash (25% on entry). Primarina is immune to Glaive Rush, takes a +0 Earthquake for 47–55%, OHKOs a Baxcalibur without its Sash, and Encores its setup. Ice Shard has a 56% OHKO on Garchomp. A +2 Glaive Rush OHKOs Gyarados | Primarina + Stealth Rock |
| Mega Golisopod (21.7%) | **Favored** | Rotom-Heat OHKOs with Overheat, takes Sucker Punch for 29–34% and Close Combat for 48–57%, is immune to Drill Run, and resists Bug moves. Gyarados resists Bug moves, is immune to Drill Run, carries Intimidate, and Temper Flare does 48–57%. Risk: Close Combat has a 25% OHKO on Archaludon | Rotom-Heat, Gyarados |
| Mega Lucario Z (14.9%) | **Favored** (not behind Veil) | Gyarados takes Flash Cannon for 20–24% (40–48% at +2) and Earthquakes back for 84–99%. Rotom-Heat OHKOs it and takes Dark Pulse for 32–39%. Scarf Garchomp outspeeds and OHKOs. Primarina resists Dark and Fighting. In the Lucario mirror, both are at 223 and both Aura Spheres OHKO, so avoid it | Gyarados, Rotom-Heat, Garchomp |
| Archaludon (23.5%) | **Favored** | Lucario Z's Aura Sphere OHKOs the offensive spread and does 77–92% to the bulky one. Lucario resists Archaludon's Draco Meteor and Flash Cannon and takes Thunderbolt for 50–59%. Risk: its Thunderbolt OHKOs Gyarados and its Draco Meteor OHKOs Garchomp | Lucario Z |
| Gholdengo (18.5%; Air Balloon 72.9%) | **Favored** | Lucario (223 vs 136–149) Dark Pulses twice for 72–85% each and survives one Shadow Ball (69–82%). It loses only if Gholdengo already has Nasty Plot up. Rotom-Heat OHKOs with Overheat and takes Shadow Ball for 46–55% | Lucario Z, Rotom-Heat |
| Rillaboom (13.2%) | **Favored** | Rotom-Heat outspeeds it (108 vs 107), has a 94% OHKO with Overheat, takes Grass moves at ×¼, is immune to High Horsepower, and takes Knock Off for 35–41%. Gyarados, after Intimidate, takes Grassy Glide for 24–29%. Risk: Grassy Glide OHKOs Primarina | Rotom-Heat, Gyarados |
| Aurora Veil + setup (4.2; 61% win rate) | **Even** | Lucario Z OHKOs the common Ninetales even through Veil, and Archaludon has an 87.5% chance to. But an enemy Lucario Z **behind Veil** survives our Garchomp's Earthquake (78–92%), Rotom's Overheat (70–84%) and our Lucario's Aura Sphere (74–88%). Gyarados has to wall it instead. A +2 Baxcalibur Glaive Rush OHKOs Gyarados, so Primarina (immune) Encores it. The game turns on whether Veil goes up before Ninetales falls (FACT_CHECK 1) | Lucario Z lead, Gyarados, Primarina |
| Rain (4.4; 62.9%) | **Even to unfavored** | Archaludon's Thunderbolt OHKOs Pelipper. Garchomp is immune to Electro Shot and outruns Adamant Mega Swampert in rain (244). Primarina resists Water. But Gyarados (×4 Electric), Rotom-Heat (Water) and Lucario Z (Swampert's Earthquake) are liabilities | Archaludon, Garchomp, Primarina |
| Psychic Terrain (4.3; 52.2%) | **Even** | Lucario's Dark Pulse does 83–99% to Indeedee, and Garchomp's Earthquake has a 94% OHKO on it. Primarina (82 Speed) Encores Shell Smash after it's used. But a +2 Mega Blastoise's Terrain Pulse OHKOs Primarina, Gyarados and Lucario. Rotom's Volt Switch does 47–57% to an unboosted Blastoise | Lucario Z, Primarina, Rotom-Heat |
| Revival Blessing / Last Respects (4.6; 39.5%) | **Favored** | Lucario (223) outspeeds Scarf Basculegion (214) and Dark Pulses it (70–83%). Garchomp's Earthquake and Primarina's Moonblast both OHKO Pawmot, though its Focus Sash (90.9%) holds once. Risk: Pawmot's Double Shock OHKOs Gyarados and Primarina. Rotom-Heat resists Double Shock | Lucario Z, Garchomp, Archaludon |

## 3. Red team

**How a top player beats it after seeing it at Team Preview:**
1. **Brings Veil with its own Lucario Z.** Behind their Veil, none of our Lucario answers OHKO (see the Veil row). Their
   Lucario, at +2 behind Veil, then breaks everything except Gyarados. This is the team's worst common matchup, and the
   reason HYP-2 and HYP-3 exist.
2. **Brings Electric, Ground and Fire together.**
   - Pawmot's Double Shock OHKOs Gyarados (186–222%) and Primarina (154–183%), and its Focus Sash survives our OHKOs once.
   - Mega Charizard Y's Fire Blast in sun OHKOs Lucario Z and Archaludon. Only Garchomp's Stone Edge OHKOs it back.
   - Special Mega Garchomp Z has an 87.5% OHKO on Lucario Z with Earth Power or Flamethrower.
   - When they show two of these three, the default pick is wrong. The pick table must steer away from it (log it).
3. **Keeps a +1 Mega Salamence alive.** After one Dragon Dance it has 258–283 Speed, faster than anything we have, and a
   +1 Earthquake does 83–98% to Archaludon. Gyarados has to come in before the second attack. A misread here loses the
   game.
4. **Encores our Nasty Plot** with Primarina, Ninetales or Indeedee. Rule 2 exists for this.
5. **Uses Knock Off** (Meowscarada 69.2%, Rillaboom 63.1%; S1). It strips Garchomp's Scarf (Garchomp drops to 169 Speed)
   and Gyarados's Helmet.

**Common tech that shuts it down:**
- **Taunt** (Gyarados 51.6%) blocks our Stealth Rock, Encore, Will-O-Wisp and Pain Split.
- **Intimidate** (Salamence and Gyarados, both about 99%) weakens our Garchomp and Gyarados.
- **A +2 Mega Blastoise in Psychic Terrain** OHKOs every member.
- **Rocky Helmet and Rough Skin** tax Gyarados's Avalanche and Temper Flare, and Garchomp's Outrage and Fire Fang (all
  contact).
- **Sand, snow and rain chip** Gyarados, Primarina and Rotom-Heat.

**Honest doubts:**
- The core's win rates come from small, self-selected Showdown samples (n = 29–55, brief §1 C). Gyarados's 69% could
  regress.
- Every set is the in-game consensus, so opponents know what we run. The edge is in the combination and the plan, not in
  surprise.
- In-game Selection Support may flag our strong matchups for the opponent (mechanics §11). The effect is UNVERIFIED.
- In rain and Veil games the team plays without its Mega or without its best answers. Those rows cap the win rate.

## 4. Test plan

**Games**
- **Phase A:** 20 games on the Pokémon Showdown ladder, format `[Gen 9 Champions] BSS Reg M-C` (`gen9championsbssregmc`),
  with the exact import above. Play with the timer on and treat 45 seconds as the turn limit.
- **Phase B:** only if Phase A passes and the Coach schedules it. 20 in-game Ranked Singles games, screen-recorded with
  narration (`trainer/README.md`).

**Log per game.** Add these lines under the standard game log in `trainer/README.md`:
```
LAB:            z-guard-balance · phase A/B · rating or rank before the game
OPP ARCHETYPE:  brief §4 tag (4.1–4.7) or "other"
MY PICKS/LEAD:  followed the pick table? Y/N (if N, why)
MEGA:           used? which turn?
DECIDED BY:     decision / matchup / information / variance
PLAN WORKED:    Y/N + one line
H1:             contact priority into Lucario Z: count, and did Aura Guard keep it alive? (Y/N)
H2:             Garchomp revenge attempts on 223+ Pokémon: attempts / KOs
H3:             vs Salamence: who handled it? Did it lose ≥1/3 HP to Helmet or recoil?
H4:             vs Veil: did Veil go up before Ninetales fell?
                Phase B only: on Lucario's Mega turn vs a faster-base Pokémon, who moved first?
                (field evidence for FACT_CHECK 1)
TIMER:          any turn over 35 s? Any "Your Time" warning?
```

**Success criteria**
- **Phase A.**
  - *Promising* means all three: at least 11 wins (55%); the pick table followed in at least 15 games; and no top-10
    threat with 3 or more losses in 4 or fewer appearances.
  - *Rework* means 7 wins or fewer (35%).
  - 8–10 wins means extend to 30 games before deciding.
  - 20 games give about a ±22-point 95% interval, so Phase A can only screen out a bad idea.
- **Phase B.** *Promising* means at least 11 wins in 20 plus a net rank gain.
- **Validated** (moves to the playbook) means all of these:
  - at least 56% over 50 or more in-game ranked games;
  - every "Favored" row wins at least 60% where n ≥ 5;
  - no "Your Time" losses;
  - Team Preview decided within 90 seconds in at least 95% of games.

**Scheduled by the Coach for:** Coach decides. The Lab suggests running this before HYP-2 and HYP-3, since both swap one
slot of this team.

**Dependencies:**
- **FACT_CHECK for the Scout:**
  1. Mega-turn Speed (mechanics §13 Q1).
  2. Can Lucarionite Z be bought for VP in the shop, or does it only come from the M-6 premium pass (regulations §7)?
     Does that still hold after M-6 ends?
  3. Do Avalanche (doubles if hit first) and Temper Flare work as in SV in Champions?
  4. Does Showdown's Champions teambuilder read the `EVs:` line as Stat Points?
- **CONSULT for the Coach:**
  1. Can the Trainer recruit these six, and what VP budget do they have (Mega Stone 2,000 VP; items 700–1,000 VP each;
     training)?
  2. Do they have a Showdown account for Phase A?
  3. After calibration: does their style suit balance, or would they rather play offense?

## 5. Verdict
- **Result:** not tested yet. 0–0 over 0 games.
- **Verdict:** pending.
- **What we learned:** none yet.

## 6. Playbook
- Not validated. Nothing goes into `lab/playbook.md` yet.

## Sources
The brief's keys (S1, S4, S11, S12, S13, S15) expand as in `knowledge/meta/singles/brief-2026-09-28.md` §9. Lab keys:
- **L1:** [every damage range and stat above] — (Pokémon Showdown damage calculator, Champions mode,
  https://calc.pokemonshowdown.com/; library `calc/*.js` including `calc/mechanics/champions.js`, fetched 2026-09-28 and
  run in Node 22 with gen 0; accessed 2026-09-28, Tier 2; Champions accuracy verified in `knowledge/sources.md` §7).
- **L2:** [each set's moves and abilities are in its Champions learnset: Lucario (Nasty Plot, Flash Cannon, Aura Sphere,
  Dark Pulse; Inner Focus; Mega Z Aura Guard), Gyarados (Avalanche, Earthquake, Taunt, Temper Flare), Garchomp
  (Earthquake, Outrage, Stone Edge, Fire Fang), Primarina (Moonblast, Sparkling Aria, Encore, Aqua Jet), Archaludon
  (Draco Meteor, Flash Cannon, Thunderbolt, Stealth Rock), Rotom (Overheat, Volt Switch, Will-O-Wisp, Pain Split)] —
  (Serebii Pokédex Champions, https://www.serebii.net/pokedex-champions/<name>/, accessed 2026-09-28, Tier 2).
- **L3:** [all six species are M-C eligible (262 entries)] — (Official eligible-Pokémon list,
  https://web-view.app.pokemonchampions.jp/battle/pages/events/rs178713870219xeaaio/en/pokemon.html, accessed
  2026-09-28, Tier 1).
- **L4:** [Mega Lucario Z newly allowed in M-C] — (Official in-game news "Regulation Set M-C (Updated on September 9)",
  https://news.pokemon-home.com/en/page/816.html, accessed 2026-09-28, Tier 1).
- **L5:** [Champions formats on Showdown use "Points" (32 per stat, 66 total), and the export writes them on the `EVs:`
  line] — (Pokémon Showdown client, https://play.pokemonshowdown.com/js/oldclient/client-teambuilder.js and storage.js,
  accessed 2026-09-28, Tier 2; inferred from code).
- **S1 Rotom-Heat page:** [Overheat 97.8%, Volt Switch 90.5%, Will-O-Wisp 77.5%, Pain Split 33.1%, Bold 43.5%] —
  (PokéChamp DB, https://pokechamdb.com/snapshots/pokemon/rotom-heat.json, M-6 Singles snapshot 2026-09-27, accessed
  2026-09-28, Tier 2).
