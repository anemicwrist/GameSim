---
slug: veil-mode-ninetales-slot
mode: singles
season: Ranked Season M-6 / Regulation M-C (still applies in M-7 if the roster stays M-C)
status: proposed
confidence: calc-verified   # benchmarks from the Showdown calc's Champions mode; the claim that Veil mode wins more is theory only
priority: 3 × 3 ÷ 2 = 4.5
created: 2026-09-28
updated: 2026-09-28
---
<!-- Lab: copy to lab/hypotheses/<slug>.md. Method: .claude/agents/lab.md, "Research cycle". -->

# Veil mode: Alolan Ninetales in Z-Guard Balance's Garchomp slot

**What kind of hypothesis:** a targeted tech slot for `lab/hypotheses/z-guard-balance.md` (HYP-1). It swaps one
Pokémon, so run it after HYP-1's Phase A baseline.

**Priority score:**
- **Edge 3.** It uses the best-performing large archetype while screen removal is scarce (hole H4). The forecast (R1,
  R2) warns that window may close within weeks.
- **Trainer fit 3.** Veil halves incoming damage, which forgives mistakes. But it adds a second game plan and a frail lead.
- **Effort 2.** One new Pokémon plus Light Clay. The other five come from HYP-1.

## 1. Proposal

### The idea
- Replace Choice Scarf Garchomp in HYP-1 with **Alolan Ninetales @ Light Clay** (Snow Warning: Aurora Veil, Freeze-Dry,
  Moonblast, Encore).
- The team gains a second mode. Ninetales leads and sets 8 turns of Aurora Veil. Mega Lucario Z then uses Nasty Plot
  behind it.
- Snow Warning also replaces rain, HYP-1's weakest matchup.
- Everything else is HYP-1 unchanged.

### Why it should work now
1. **Veil is the best large archetype right now.**
   - Veil sides won **61.1%** (CI 50–72, n=72, 29 players) (brief §4.2, S4).
   - Veil teams Mega Evolve Lucario most often (15), then Baxcalibur (10) (S4). So Ninetales + Mega Lucario Z is the
     archetype's own main core.
   - Screen removal is scarce. The only common breakers in the top-30 move lists are Psychic Fangs (Metagross 76.7%) and
     Defog (Corviknight 12.5%) (brief H4, S1).
2. **Veil answers hole H2 from the defensive side.** Behind our Veil, the field's revenge killers stop OHKOing Lucario Z.
   Calc-verified damage to our Lucario Z behind Veil:

   | Attack | Damage behind Veil | Without Veil |
   |---|---|---|
   | Scarf Garchomp Earthquake | 77.5–91.8% | 155–184% |
   | Scarf Cinderace Pyro Ball | 86.3–102% (18.8% OHKO) | 173–204% |
   | Enemy Lucario Z Aura Sphere | 74.1–87.7% | 148–176% |
   | Baxcalibur Earthquake | 61.2–72.7% | 122–145% |
   | Hippowdon Earthquake | 57.1–67.3% | 114–135% |
   | Gholdengo Shadow Ball | 34.6–40.8% | 69–82% |

   Two things still kill through Veil: +1 Mega Salamence Earthquake (56% to OHKO) and Mega Charizard Y's Fire Blast in
   sun.
3. **A +2 Lucario Z then breaks the field.**
   - OHKOs: Garchomp (100.5–118.3%), bulky Calm Archaludon (155–183%), Mega Salamence (104–123%).
   - 2HKOs: Hippowdon (67–79%), Mega Golisopod (76–90%), Primarina (77–90%).
4. **Rain denial.**
   - Rain sides won 62.9% (S4), and rain is the worst archetype row in HYP-1.
   - Snow Warning replaces rain when Ninetales enters.
   - Freeze-Dry OHKOs Pelipper (139–168%) and has a 62.5% chance to OHKO Mega Swampert. Pelipper's Hurricane does only
     41–49% to Ninetales.
5. **Coverage for Dragons.** From 177 Speed, faster than Adamant Mega Salamence (172), Freeze-Dry OHKOs Mega Salamence
   (114.6–135.6%) and base Garchomp (110–132%).
6. **Trainer fit** (my read, to be tested). Veil halves every hit for 8 turns, so one misplay costs half the HP it would
   otherwise. That's a buffer for a player who is still calibrating. The plan is also scripted: Veil, Mega, Nasty Plot,
   attack.

### Target matchups
- Rain (4.4).
- Salamence / Garchomp / Primarina balance (4.1, 4.7). Veil halves Earthquake and Double-Edge.
- Offense that relies on Scarf or priority revenge kills.
- Hippowdon balance. Its Earthquake behind Veil no longer OHKOs Lucario.

### Expected weaknesses
- **Fast Steel, Fire or Rock attacks kill Ninetales before or right after it sets Veil.**
  - Lucario Z Flash Cannon (219–259%; 109–129% through Veil), Archaludon, Metagross Bullet Punch, Mega Golisopod Iron Head
    and Gholdengo's Make It Rain all OHKO it.
  - Cinderace Pyro Ball OHKOs it. Glimmora Power Gem has a 62.5% OHKO.
- **Screen removal:** Metagross Psychic Fangs, Corviknight Defog.
- **Encore on Ninetales after it sets Veil:** Primarina 50%, Indeedee 72%, Alolan Ninetales 70% (S1).
- **Phazing resets Nasty Plot:** Hippowdon Whirlwind 60%, Archaludon Roar 26% and Dragon Tail 25% (S1).
- **Losing Scarf Garchomp** removes HYP-1's 253 revenge killer and its only OHKO on Mega Charizard Y.

### Legality
- **Pokémon:** Ninetales (Alolan Form) is on the M-C eligible list (L3).
- **Ability:** Snow Warning is Alolan Ninetales's ability in Champions (L2; 99.8% in-game). PokéChamp DB's English page
  mislabels it "Blizzard" (threats.md).
- **Item:** Light Clay is in the item list (added in M-B; mechanics §8). It replaces Choice Scarf, so all six items stay
  different.

### Builds on
- **The archetype:** brief §4.2 and its example players ElPhilomeno (1492), Ghostofcolress (1439) and nightmare009 (1424,
  4-0) (S4).
- **The in-game set** (S1): Aurora Veil 97.3%, Freeze-Dry 72.2%, Encore 70.0%, Moonblast 55.0%, Light Clay 90.3%, spread
  2/0/0/32/0/32 at 23.4%.

### The slot

**Ninetales-Alola @ Light Clay**
- **Ability:** Snow Warning. **Stat Alignment:** Timid.
- **SP:** 2 / 0 / 0 / 32 / 0 / 32.
- **Stats:** 150 / 78 / 95 / 133 / 120 / 177.
- **Moves:** Aurora Veil, Freeze-Dry, Moonblast, Encore.
- **Speed benchmark.** 177 beats Adamant Mega Salamence (172), Garchomp (169), both Charizard Megas (167), Mimikyu (162),
  any Lucario before it Mega Evolves (156), Baxcalibur (152), Archaludon (150) and Gholdengo (149). So Veil goes up before
  any of these move.
- **Freeze-Dry:**
  - OHKOs Pelipper, Mega Salamence and base Garchomp.
  - 62.5% to OHKO Mega Swampert.
  - 37.5% to OHKO Impish Gyarados.
  - 58–68% to Basculegion.
- **Moonblast:**
  - 2HKOs Mega Garchomp Z (72–88%) and Baxcalibur (70–85%).
  - OHKOs Pawmot (122–144%, Focus Sash permitting).
- **What it survives:**
  - Scarf Garchomp Earthquake (73–86%).
  - Hippowdon Earthquake (53–63%).
  - Primarina Sparkling Aria (51–60%).
  - Rillaboom Grassy Glide in terrain (73–86%).
  - Baxcalibur Earthquake (57–68%).
  - Samurott-H Ceaseless Edge (34–40%).
  - Golisopod Sucker Punch (27–31%).

**Import:** replace the Garchomp block in HYP-1's import with this one (Stat Points on the `EVs:` line).
```
Ninetales-Alola @ Light Clay
Ability: Snow Warning
EVs: 2 HP / 32 SpA / 32 Spe
Timid Nature
- Aurora Veil
- Freeze-Dry
- Moonblast
- Encore
```

### Game plan
Two modes, chosen at Team Preview.

**Veil mode: Ninetales (lead) + Lucario Z + Gyarados** (Archaludon instead of Gyarados into Primarina-heavy teams).
1. Turn 1: Ninetales uses Aurora Veil.
2. After that, Ninetales clicks Encore if the opponent just set up or used a status move. Otherwise it uses Freeze-Dry on
   Water, Flying and Dragon types and Moonblast on the rest.
3. When Ninetales is low, let it faint so Lucario Z comes in for free. Don't spend a switch to save it.
4. Lucario Z: Mega Evolve. Nasty Plot **once**, only when nothing in front of it has Encore or can OHKO it through Veil.
   Then attack.
5. Veil lasts 8 turns counting the turn it goes up: set on turn 2, it's gone after turn 9 (Showdown shows the end
   message). Finish the sweep by then, or bring Gyarados in to stall the last turns.

**Rain variant of Veil mode: Ninetales (lead) + Archaludon + Primarina.** Snow Warning removes the rain and Veil still
goes up. There's no Mega that game.

**Standard mode:** HYP-1's pick table with Garchomp removed. Garchomp's two rows change:
- Rain uses the rain variant above.
- Revival Blessing becomes Lucario Z + Primarina + Archaludon. Moonblast replaces Garchomp's Earthquake on Pawmot.

**Choosing the mode:**
- **Veil mode is the default** into balance and offense.
- **Standard mode** when the opponent's 6 shows Metagross or Corviknight (screen removal).
- **If their 6 shows Cinderace** (it leads 32% of the time it's registered; S4), lead Gyarados instead. Bring Ninetales
  in after the first faint: Snow Warning re-sets the snow on entry, so Veil can still go up mid-game (FACT_CHECK 3).

## 2. Theory check

**Damage calcs:** same method and opponent sets as HYP-1 §2. The tool is the Showdown calc in Champions mode, run
locally from the calc.pokemonshowdown.com code on 2026-09-28 (L1). Every number here is calc-verified. Critical hits,
chip damage and Stamina are not modeled. Key additions beyond HYP-1:
- **Ninetales offense** (32 SpA Timid):
  - Freeze-Dry vs. 32 HP Pelipper: 138.9–167.6%.
  - Freeze-Dry vs. Mega Salamence: 114.6–135.6%.
  - Freeze-Dry vs. Garchomp: 110.2–131.8%.
  - Freeze-Dry vs. Mega Swampert: 94.9–110.7% (62.5% to OHKO).
  - Freeze-Dry vs. 32 HP Gyarados: 89.1–106.9%.
  - Moonblast vs. Mega Garchomp Z: 72.4–87.5%.
  - Moonblast vs. Baxcalibur: 70.1–84.8%.
  - Moonblast vs. Pawmot: 122.4–144.2%.
  - Freeze-Dry vs. Mega Blastoise: 50.6–60.7%.
- **Into Ninetales:**
  - Mega Lucario Z Flash Cannon: 218.6–258.6%; through Veil 109.3–129.3%.
  - Archaludon Flash Cannon: 194.6–232%; through Veil 97.3–116%.
  - Mega Salamence Double-Edge: 124–146%.
  - Cinderace Pyro Ball: 160–189%.
  - Mega Metagross Bullet Punch: 162.6–194.6%.
  - Glimmora Power Gem: 92–109.3%; through Veil 46–54.6%.
  - Scarf Garchomp Earthquake: 72.6–86%.
  - Pawmot Double Shock: 96–112.6% (75% to OHKO).
  - Pelipper Hurricane: 40.6–48.6%.
- **Our Lucario Z behind Veil:** the table in §1, item 2.
- **Our +2 Lucario Z:** §1, item 3.

**Speed benchmarks:** HYP-1's table, with Ninetales at **177** in place of Garchomp's 253. What's lost:
- Nothing on the team outspeeds a +Spe Z-Mega any more. Our Lucario Z only speed-ties it at 223.
- Scarf users (241–288) now outrun the whole team. Veil is the answer to them instead of speed.
- **Mega-turn caveat (FACT_CHECK 1):** if Champions doesn't use Mega Speed on the Mega turn, an enemy Lucario Z (156
  before Mega) moves after our Ninetales on turn 1. Then Veil goes up before it dies.

**Matchups in Veil-mode games** (the change from HYP-1 in brackets):

| Top threat / archetype | Verdict | Why |
|---|---|---|
| Mega Salamence | **Favored** [same] | Ninetales outspeeds Adamant Salamence (177 vs 172) and OHKOs it with Freeze-Dry. A Jolly or Naive Salamence (189) outspeeds and OHKOs Ninetales with Double-Edge. Veil halves Salamence's hits on Gyarados and Archaludon |
| Garchomp / Mega Garchomp Z | **Favored** [same] | Freeze-Dry OHKOs base Garchomp, and Ninetales survives a Scarf Earthquake (73–86%). Primarina and Archaludon still handle Mega Z. We lose Garchomp's Outrage |
| Primarina | **Even** [same] | Freeze-Dry does 43–51%, and Sparkling Aria does 51–60% back. Veil lets Archaludon win its 2HKO race |
| Hippowdon | **Favored** [same] | Behind Veil its Earthquake does 57–67% to Lucario. A Lucario that is **already** +2 2HKOs it through Sitrus (67–79% per Aura Sphere) and survives one Earthquake. Using Nasty Plot in front of it costs too much HP: Lucario would take two Earthquakes. Its Whirlwind (60%) also resets boosts, so Gyarados's Taunt is still the cleanest line |
| Baxcalibur | **Even** [same] | Ninetales outspeeds it (177 vs 152). Moonblast does 70–85% (the Sash holds). Ninetales is immune to Glaive Rush and resists Icicle Crash. Encore its Swords Dance or Dragon Dance |
| Mega Golisopod | **Favored** [same, through Rotom-Heat] | Ninetales can't face it: Iron Head OHKOs, though Sucker Punch does only 27–31% |
| Mega Lucario Z | **Favored** [slightly worse] | Gyarados and Rotom-Heat still answer it. Garchomp's OHKO is gone. Their Lucario OHKOs Ninetales |
| Archaludon | **Favored** [same] | Our +2 Lucario behind Veil OHKOs even bulky Archaludon (155–183%) |
| Gholdengo | **Favored** [same] | Lucario Z and Rotom-Heat, as in HYP-1. Behind Veil, Shadow Ball does 35–41% to Lucario |
| Rillaboom | **Favored** [same] | Rotom-Heat, as in HYP-1. Ninetales survives Grassy Glide (73–86%) |
| Aurora Veil (mirror) | **Even** [same] | Our Lucario Z OHKOs their Ninetales through Veil. Their Veil still covers their sweeper. Snow is shared |
| Rain | **Even to favored** [up from even/unfavored, the main gain] | Snow Warning removes rain on entry, which turns off Swift Swim and makes Electro Shot charge again. Freeze-Dry OHKOs Pelipper, and Hurricane does only 41–49% back. Their Archaludon and Mega Golisopod still OHKO Ninetales |
| Psychic Terrain | **Even** [same] | Indeedee's Mystical Fire does 51–60% to Ninetales, and Moonblast does 46–55% back. Ninetales (177) outspeeds Blastoise (128–143), so it can Encore a Shell Smash **the next turn**. But a +2 Aura Sphere OHKOs Ninetales |
| Revival Blessing | **Even** [down from favored] | Moonblast OHKOs Pawmot (Sash permitting), but Double Shock has a 75% OHKO on Ninetales. Freeze-Dry does 58–68% to Basculegion. Garchomp's Earthquake is gone |

## 3. Red team

**How a top player beats it after seeing it at Team Preview:**
- **Leads something that kills Ninetales before Veil** (Cinderace, Jolly Mega Salamence, or Lucario Z if Mega Speed
  applies on the Mega turn). Or leads Glimmora: Power Gem has a 62.5% OHKO, and Glimmora sets Stealth Rock anyway.
- **Keeps its own screen remover.** Metagross Psychic Fangs is on 76.7% of Metagross (S1), and the forecast (R2) expects
  more of it.
- **Encores Ninetales right after Veil** (Primarina, Indeedee or its own Ninetales). Ninetales is then locked into a
  Veil that fails, wasting three turns or forcing a switch.
- **Phazes the +2 Lucario:** Hippowdon Whirlwind 60%, Archaludon Roar and Dragon Tail.
- **Stalls out the 8 Veil turns** with Protect, switches and Gyarados. That's hard in 3v3 but possible against a slow
  sweep.
- **Blocks Veil with Prankster Taunt** before it's used (Grimmsnarl #48 in-game, Sableye, Whimsicott). Ninetales is not
  Dark, so Prankster works on it.

**Common tech that shuts it down:**
- Psychic Fangs or Brick Break; Defog.
- Always-crit moves ignore Veil (Meowscarada's Flower Trick).
- Stealth Rock takes 25% from Ninetales, since it's weak to Rock.
- Sand or sun replaces the snow. Veil persists once set, but can't be re-set without snow.

**Honest doubts:**
- The sample's Veil winners mostly paired Ninetales with Hisuian Samurott, Aegislash, Baxcalibur and Mega Venusaur (brief
  §4.2), not with this team's partners. Their 61% may not transfer.
- The forecast expects anti-Veil tech to rise (R2), so this slot may have a short shelf life.
- Losing the 253 Scarf answer weakens HYP-1's speed plan (hole H2) and its only OHKO on Mega Charizard Y.

## 4. Test plan

**Games:**
- After HYP-1's Phase A (20 games, the baseline), play **20 Showdown games** (`gen9championsbssregmc`) with Ninetales in
  Garchomp's slot. Same timer rule: 45 seconds per turn.
- If promising, play 20 in-game Ranked Singles games when the Coach schedules them.

**Log per game:** HYP-1's lines, plus:
```
LAB:          veil-mode-ninetales-slot
MODE:         Veil / standard, and why
VEIL:         set on turn __ / never. If never: KO'd first / Taunted / Encored / no snow
BEHIND VEIL:  Lucario Nasty Plots used __. Hits it survived only thanks to Veil (name them)
RAIN:         did Snow Warning remove the rain? Y/N / not a rain game
NINETALES:    KO'd before acting? Y/N
FEEL:         how hard was this game to pilot? 1–5
```

**Success criteria:**
- **Promising** means all four:
  - Veil goes up in at least 75% of games where Ninetales is picked.
  - Veil-mode games (expect 8 or more of the 20) win at least 60%.
  - The overall win rate is no worse than HYP-1's Phase A minus 5 points.
  - Average FEEL is at or below HYP-1's.
- **Reject** if either:
  - Ninetales is KO'd before setting Veil in at least 40% of its leads, or
  - the overall win rate is 15 or more points below the HYP-1 baseline.
- Rain games will be few in 20. Report them, but don't decide on them.
- **Validated** follows the same bar as HYP-1: at least 56% over 50 or more in-game games, and Veil mode at least 60%
  where n ≥ 10.

**Scheduled by the Coach for:** Coach decides. The Lab suggests running it after HYP-1 Phase A and before HYP-3. It's
the cheaper swap, and it tests whether the Trainer benefits from the Veil buffer.

**Dependencies (FACT_CHECK for the Scout):**
1. Mega-turn Speed (mechanics §13 Q1).
2. Does Light Clay give 8 turns of Veil in-game? On Showdown it's inferred from replays: the Veil lasted turns 2–9 in
   replay 2688548425 (Singles supplement G1).
3. Does Snow Warning re-set the snow when Ninetales switches in mid-game?

## 5. Verdict
- **Result:** not tested yet. 0–0 over 0 games.
- **Verdict:** pending.
- **What we learned:** none yet.

## 6. Playbook
- Not validated.

## Sources
The brief's keys (S1, S4, S15) expand as in `knowledge/meta/singles/brief-2026-09-28.md` §9. L1–L5 are as in
`lab/hypotheses/z-guard-balance.md`:
- **L1:** Showdown calc, Champions mode (all numbers above).
- **L2:** Serebii Champions Pokédex. Ninetales (Alolan) has Aurora Veil, Freeze-Dry, Moonblast, Encore and Snow Warning.
- **L3:** Official M-C eligible list, including "Ninetales (Alolan Form)".
- **L5:** Showdown teambuilder Stat Points.

Plus:
- [Alolan Ninetales set and spread] — (PokéChamp DB, https://pokechamdb.com/snapshots/pokemon/ninetales-alola.json, M-6
  Singles snapshot 2026-09-27, accessed 2026-09-28, Tier 2).
