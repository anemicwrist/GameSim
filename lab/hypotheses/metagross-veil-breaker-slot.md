---
slug: metagross-veil-breaker-slot
mode: singles
season: Ranked Season M-6 / Regulation M-C (still applies in M-7 if the roster stays M-C)
status: proposed
confidence: calc-verified   # benchmarks from the Showdown calc's Champions mode; the claim that it improves the Veil and Salamence matchups is theory only
priority: 2 × 3 ÷ 2 = 3.0
created: 2026-09-28
updated: 2026-09-28
---
<!-- Lab: copy to lab/hypotheses/<slug>.md. Method: .claude/agents/lab.md, "Research cycle". -->

# Veil-breaker: Mega Metagross as a second Mega in Z-Guard Balance's Garchomp slot

**What kind of hypothesis:** a targeted tech slot for `lab/hypotheses/z-guard-balance.md` (HYP-1). It is the forecast's
counter-strategy C1 made concrete. It fills the same slot as HYP-2, so the two are alternatives. The test decides
between Scarf Garchomp (HYP-1), a Veil mode (HYP-2), and this Veil-breaker.

**Priority score:**
- **Edge 2.** Its tools line up with holes H3 and H4 and with forecast R1–R3. But Metagross fell from #10 to #22
  in-game for real reasons: Ground, Fire, Dark and Ghost weaknesses, and Rocky Helmet everywhere.
- **Trainer fit 3.** It's bulky and simple to click. But two Mega options add a decision at Team Preview.
- **Effort 2.** One new Pokémon plus a second 2,000 VP Mega Stone.

## 1. Proposal

### The idea
- Replace Choice Scarf Garchomp in HYP-1 with **Metagross @ Metagrossite**: Jolly, 2/32/0/0/0/32, Psychic Fangs, Ice
  Punch, Earthquake, Bullet Punch.
- The team then has two Mega options. Lucario Z stays the default. Metagross is the Mega into Aurora Veil teams and into
  double-Dragon Salamence teams.
- Never bring Lucario and Metagross in the same game. Only one of them could Mega Evolve.

### Why it should work now
1. **H4: Veil wins and removal is scarce.**
   - Veil sides won 61.1% (CI 50–72, n=72) (S4).
   - Psychic Fangs is the field's main screen-breaker, on 76.7% of Metagross. The only other common one is Corviknight's
     Defog at 12.5% (brief H4, S1). Psychic Fangs destroys Veil before dealing damage (S15).
2. **The Veil core's pieces are weak to Metagross.** Calc-verified:
   - Psychic Fangs removes the Veil and hits the common 2-HP Alolan Ninetales for 86.6–102.6%.
   - Next turn, priority Bullet Punch finishes Ninetales before it can Encore. Unboosted it does 162.6–194.6%; even
     through a Veil it does 81.3–97.3%.
   - Earthquake OHKOs Mega Lucario Z (112.9–133.3%).
   - Psychic Fangs has a 50% chance to OHKO Mega Venusaur.
   - Any two hits from Psychic Fangs (57–68%) and Bullet Punch (53–64%) KO Baxcalibur.
3. **H3: Salamence and Garchomp.**
   - Ice Punch OHKOs Mega Salamence at +0 (114.6–135.6%) and base Garchomp (136.2–162.1%). It 2HKOs Mega Garchomp Z
     (74.5–88.6%).
   - Before it Mega Evolves, Metagross has Clear Body, which blocks the Intimidate that Salamence and Gyarados carry
     (about 99% of each; S1). HazelGrayble: Metagross "ignores Intimidate with Clear Body, resists Double-Edge, then can
     Ice Punch in" (S11, Tier 3).
   - It resists Flying, Dragon, Fairy, Ice and Steel.
4. **Under-prepared for** (my read).
   - It fell from #10 to #22 in-game (S1/S2).
   - In M-B it was #8 on Showdown: Mega Metagross on 13.8% of teams at the 1500 cutoff (S5).
   - Fewer teams now carry answers built for it. Forecast R2 bets on its return. Playing it now is ahead of that curve.
5. **It takes the hits the meta throws at Steels.** Calc-verified, it survives:
   - an unboosted Lucario Z Dark Pulse (64.9–76.4%) and OHKOs back with Earthquake;
   - Mega Salamence Earthquake (61.1–72.6%);
   - Baxcalibur Earthquake (61.1–72.6%);
   - Hippowdon Earthquake (57.3–68.7%);
   - Garchomp Earthquake (77.7–92.9%);
   - Cinderace Pyro Ball (85.3–103.1%, 12.5% OHKO).

### Target matchups
- Aurora Veil + setup (4.2).
- Salamence-heavy shells (4.1, 4.7).
- Revival Blessing (4.6): Psychic Fangs OHKOs Pawmot, Focus Sash permitting.
- Sneasler: Psychic Fangs OHKOs it (392–466%).

### Expected weaknesses
- **Ground.** Earthquake is on 97.1% of Hippowdon, 91.4% of Baxcalibur, 73.0% of Salamence and 67.3% of Garchomp (S1).
  Mega Swampert's rain Earthquake has a 68.8% OHKO.
- **Fire.** Mega Charizard Y's sun Fire Blast OHKOs. Cinderace. Mega Garchomp Z's Flamethrower does 65–76%.
- **Dark.** A +2 Lucario Z Dark Pulse OHKOs. Mega Golisopod's Sucker Punch does 57–69%. Knock Off.
- **Ghost.** Gholdengo's Shadow Ball has a 37.5% OHKO. Basculegion's Last Respects after one faint has a 62.5% OHKO.
- **Contact punishment.** Rocky Helmet (Corviknight 62.8%, Gyarados 54.2%) and Rough Skin tax three of its four moves.
  Earthquake is the only non-contact one.
- **Hisuian Samurott**, a Veil partner, is immune to Psychic Fangs and resists Bullet Punch. Its Ceaseless Edge does
  74–88%.
- **Psychic Terrain** blocks Bullet Punch against grounded targets (S15).

### Legality
- **Pokémon:** Metagross is on the M-C eligible list (L3).
- **Mega:** Mega Metagross has been allowed since M-B (official notice #776, L4). Metagrossite is on 94.8% of in-game
  Metagross (S1).
- **Two stones:** a team may register two Mega Stones. Only one Mega Evolution per battle (regulations §2; brief §1).
- **Items:** Metagrossite replaces Choice Scarf, so all six items stay different.
- **Moves and ability:** in Metagross's Champions learnset (L2).

### Builds on
- **The in-game Metagross set** (S1): Bullet Punch 89%, Psychic Fangs 76.7%, Ice Punch 73.9%, Earthquake 57.1%; Jolly
  31.6%; 2/32/0/0/0/32 on 26.5%.
- **HazelGrayble's** Salamence analysis (S11).
- **Brief H3 and H4.**

### The slot

**Metagross → Mega Metagross @ Metagrossite**
- **Ability:** Clear Body, then Tough Claws after Mega Evolution. **Stat Alignment:** Jolly.
- **SP:** 2 / 32 / 0 / 0 / 0 / 32.
- **Stats:** Mega 157 / 197 / 170 / 112 / 130 / 178. Before Mega: Speed 134.
- **Moves:** Psychic Fangs, Ice Punch, Earthquake, Bullet Punch.
- **Speed benchmark.** 178 beats Timid Alolan Ninetales (177), Adamant Mega Salamence (172), Garchomp (169) and the
  Charizard Megas (167). This holds on the Mega turn only if Champions applies Mega Speed that turn (FACT_CHECK 1).
  Otherwise Metagross moves at 134 that turn.
- **Damage benchmarks:**
  - Ice Punch OHKOs Mega Salamence at +0 and Garchomp.
  - Earthquake OHKOs Mega Lucario Z, Aegislash-Blade and Glimmora.
  - Psychic Fangs breaks Veil and OHKOs Sneasler and Pawmot.
  - Bullet Punch OHKOs a 2-HP Ninetales once its Veil is gone.
- **Why Jolly and not the in-game favorite Adamant (58.3%):** the Ninetales and Salamence benchmarks above need the 178
  Speed.

**Import:** replace the Garchomp block in HYP-1's import with this one (Stat Points on the `EVs:` line).
```
Metagross @ Metagrossite
Ability: Clear Body
EVs: 2 HP / 32 Atk / 32 Spe
Jolly Nature
- Psychic Fangs
- Ice Punch
- Earthquake
- Bullet Punch
```

### Game plan

**Choosing the Mega at Team Preview (one rule):**
- Bring Metagross as the Mega when the opponent's 6 shows Alolan Ninetales, **or** at least two of Salamence, Garchomp
  and Baxcalibur with no Charizard, Cinderace or Gholdengo.
- Otherwise play HYP-1's plan with Lucario Z.

**Picks:**
- **Into Veil: Metagross + Gyarados + Primarina. Lead Metagross.**
  1. Turn 1: Mega Evolve and use Psychic Fangs on Ninetales (breaks the Veil).
  2. Turn 2: Bullet Punch Ninetales before it can Encore.
  3. Gyarados walls their Lucario Z. Primarina handles Baxcalibur or Samurott setup (Encore, Moonblast).
- **Into double-Dragon Salamence balance: Metagross + Gyarados + Archaludon.**
  - Lead Archaludon (Stealth Rock), or lead Metagross if they show no Hippowdon.
  - Ice Punch the Dragons. Gyarados Taunts Hippowdon.

**Click rules:**
- **Ice Punch** into Dragons.
- **Psychic Fangs** into screens and into Poison or Fighting types.
- **Earthquake** into Lucario Z, Archaludon, Aegislash, Glimmora and Fire types.
- **Bullet Punch** to finish anything below about 40% that would outspeed Metagross. It doesn't work inside Psychic
  Terrain against grounded targets.
- Don't click contact moves into Rocky Helmet Corviknight or Gyarados unless the move KOs.

## 2. Theory check

**Damage calcs:** same tool, method and opponent sets as HYP-1 §2 (L1). Every number here is calc-verified. Critical
hits, chip damage and Helmet recoil are not modeled.
- **Metagross offense** (32 Atk Jolly, Tough Claws on contact moves):
  - Psychic Fangs vs. 2 HP Ninetales-Alola: 86.6–102.6% (Veil removed first).
  - Bullet Punch vs. Ninetales: 162.6–194.6%; through Veil 81.3–97.3%.
  - Ice Punch vs. Mega Salamence: 114.6–135.6% at +0; 77.1–91.2% at -1.
  - Ice Punch vs. Garchomp: 136.2–162.1%. vs. Mega Garchomp Z: 74.5–88.6%.
  - Earthquake vs. Mega Lucario Z: 112.9–133.3%. vs. 32 HP Archaludon: 50.7–59.8%.
  - Psychic Fangs vs. Pawmot: 185–220%. vs. Sneasler: 392–466%. vs. Mega Venusaur: 90.9–109%.
  - Psychic Fangs vs. Baxcalibur: 57–68%. Bullet Punch vs. Baxcalibur: 53.4–63.8%.
  - Psychic Fangs vs. Primarina: 58.2–68.9%. vs. Mega Blastoise: 55.6–66.4%.
  - Ice Punch vs. Hippowdon: 36.2–43.7% (Impish 32/0/32/0/2/0) or 48.3–57.6% (Careful 32/0/2/0/32/0). vs. Rillaboom:
    64.7–76.3%.
  - Earthquake vs. Hisuian Samurott: 44.3–52.6%.
  - Psychic Fangs vs. Impish Gyarados: 42–50.4%.
- **Into Metagross** (2 HP / 0 Def / 0 SpD):
  - Lucario Z Dark Pulse: 64.9–76.4% at +0; 127.3–150.3% at +2.
  - Mega Salamence Earthquake: 61.1–72.6% at +0; 91.7–108.2% at +1.
  - Garchomp Earthquake: 77.7–92.9%. Hippowdon Earthquake: 57.3–68.7%. Baxcalibur Earthquake: 61.1–72.6%.
  - Mega Swampert rain Earthquake: 95.5–112.1%.
  - Gholdengo Shadow Ball: 89.1–107%. Basculegion Last Respects after one faint: 94.2–112.1%.
  - Mega Golisopod Sucker Punch: 57.3–68.7%. Hisuian Samurott Ceaseless Edge: 73.8–87.8%.
  - Cinderace Pyro Ball: 85.3–103.1%. Mega Charizard Y sun Fire Blast: 214–252%. Mega Garchomp Z Flamethrower:
    64.9–76.4%.
  - Primarina Sparkling Aria: 43.9–52.2%. Rillaboom (Life Orb) High Horsepower: 68.1–80.8%. Rillaboom Knock Off:
    46.4–56%.
  - +2 Mega Blastoise Aura Sphere: 90.4–107%.

**Speed:** HYP-1's table, with **178** (Mega Metagross, Jolly 32) in place of Garchomp's 253.
- 178 sits just above Timid Ninetales (177) and Adamant Mega Salamence (172).
- It is below Jolly or Naive Mega Salamence (189), the Z-Megas (223), Meowscarada (192) and Cinderace (188).

**Matchups in games where Metagross is the Mega** (the change from HYP-1 in brackets):

| Top threat / archetype | Verdict | Why |
|---|---|---|
| Mega Salamence | **Favored** [better] | Ice Punch OHKOs at +0 and outspeeds Adamant sets. If Metagross is already Mega'd when Salamence comes in, Intimidate lands and Ice Punch does 77–91%. Salamence's Earthquake does 61–73% at +0 and has a 50% OHKO at +1 |
| Garchomp / Mega Garchomp Z | **Favored** [same] | Ice Punch OHKOs base Garchomp and 2HKOs Mega Z. Its Earthquake does 78–93% and Mega Z's Flamethrower 65–76%, so don't let it hit first twice |
| Primarina | **Even** [same] | Metagross moves first. Two Psychic Fangs (58–69% each) usually beat Primarina's Sparkling Aria (44–52% each), but Sitrus makes it close on low rolls |
| Hippowdon | **Unfavored for Metagross 1v1** [same overall, through Gyarados] | Ice Punch does only 36–44% into the common Impish spread (48–58% into Careful), and Hippowdon's Earthquake does 57–69% back, so Metagross loses the 1v1. Gyarados's Taunt stays the line |
| Baxcalibur | **Even** [same] | Metagross outspeeds it (178 vs 152) and 2HKOs it with Psychic Fangs then Bullet Punch. It takes Earthquake for 61–73% at +0, but a +2 Earthquake OHKOs |
| Mega Golisopod | **Unfavored for Metagross** [same overall, through Rotom-Heat] | Earthquake does 23–27%, and its Sucker Punch does 57–69% |
| Mega Lucario Z | **Favored** [same] | Survives an unboosted Dark Pulse and Earthquakes for the OHKO. Loses to a +2 Lucario |
| Archaludon | **Favored** [same] | Earthquake does 51–60%. Metagross resists Draco Meteor and Flash Cannon |
| Gholdengo | **Unfavored for Metagross** [same overall, through Lucario Z or Rotom-Heat] | Shadow Ball has a 37.5% OHKO, and Air Balloon blocks Earthquake |
| Rillaboom | **Even** [same overall, through Rotom-Heat] | Ice Punch does 65–76%. High Horsepower does 68–81% and Knock Off 46–56% back |
| Aurora Veil + setup | **Favored** [up from even; the reason for this slot] | Psychic Fangs breaks Veil, then Bullet Punch removes Ninetales before it can Encore. Earthquake OHKOs their Lucario Z. Risk: Samurott-H (immune to Psychic Fangs, Ceaseless Edge 74–88%) and whether Veil goes up first (FACT_CHECK 1) |
| Rain | **Even to unfavored** [same] | Mega Swampert's rain Earthquake has a 69% OHKO, and Ice Punch does only 26–31% to Pelipper. Pick HYP-1's rain trio instead |
| Psychic Terrain | **Even** [same] | Psychic Fangs OHKOs Sneasler, but Bullet Punch fails in terrain. A +2 Blastoise Aura Sphere has a 44% OHKO. Mystical Fire does 43–52% |
| Revival Blessing | **Favored** [same] | Psychic Fangs OHKOs Pawmot (Sash permitting). Risk: Basculegion's Last Respects after one faint has a 62.5% OHKO |

## 3. Red team

**How a top player beats it after seeing it at Team Preview:**
- **Brings Ground, Fire or Ghost.** Earthquake users are everywhere, and Gholdengo or Basculegion (Last Respects) or
  Charizard Y all punish it. The preview rule tries to avoid Fire and Gholdengo, but Ground can't be avoided.
- **Brings Hisuian Samurott into the Veil** instead of Lucario Z. It is immune to Psychic Fangs and resists Bullet Punch.
- **Keeps a Rocky Helmet Corviknight or Gyarados** in front of it. Three of its four moves make contact.
- **Reads the second Mega.** At Team Preview both Lucario and Metagross show. The opponent doesn't know which will Mega
  Evolve (UNVERIFIED whether preview shows items; regulations §8), which is a small upside. It also doesn't cost them
  much to prepare for both.

**Common tech that shuts it down:**
- Earthquake (the #1 move on the #2 and #4 Pokémon).
- Air Balloon Gholdengo (72.9%).
- Rocky Helmet.
- Psychic Terrain (it turns off Bullet Punch).
- Taunt doesn't hurt it: Metagross runs no status moves.

**Honest doubts:**
- Metagross's in-game fall from #10 to #22 suggests the field has already found its answers.
- It adds another Ground weakness to a team that already has two (Lucario, Archaludon). Games where Metagross is the Mega
  lean hard on Gyarados.
- The benefit rests on the Veil and Salamence rows. Those are about 13% and 34% of teams, so in 20 games we might see
  only 3–4 Veil teams. The test has to be read row by row, not only overall.

## 4. Test plan

**Games:**
- After HYP-1's Phase A baseline, play **20 Showdown games** (`gen9championsbssregmc`) with Metagross in Garchomp's slot.
  Same timer rule.
- Ladder opponents can't be chosen. If fewer than 4 Veil teams show up in the 20 games, keep the slot for up to 10 more
  games and add only the Veil games from those to the Veil row.
- If promising, play 20 in-game Ranked Singles games when the Coach schedules them.

**Log per game:** HYP-1's lines, plus:
```
LAB:        metagross-veil-breaker-slot
MEGA PICK:  Lucario Z / Metagross, and why (did the one-line rule decide it? Y/N)
PREVIEW:    seconds to decide the picks (the 90 s limit matters with two Megas)
VEIL:       Psychic Fangs used? Veil removed Y/N · Ninetales KO'd before Encoring? Y/N
SALAMENCE:  Ice Punch KO? Intimidate blocked by Clear Body? Y/N
METAGROSS:  KO'd by Ground / Fire / Dark / Ghost / other · contact damage taken from Helmet or Rough Skin
```

**Success criteria:**
- **Promising** means all four:
  - Veil and double-Dragon games combined (expect about 8 of 20) win at least 60%, and beat HYP-1's rate in the same
    games.
  - Veil removed, or Ninetales KO'd before the enemy sweeper sets up, in at least 75% of Veil games.
  - The overall win rate is no worse than HYP-1's Phase A minus 5 points.
  - Team Preview decided within 90 seconds in 100% of games.
- **Reject** if either:
  - Metagross is picked in fewer than 25% of games (it isn't earning the slot), or
  - it dies before acting in more than a third of the games where it's brought.
- **Validated** follows HYP-1's bar: at least 56% over 50 or more in-game games, with the Veil row at least 60% once
  n ≥ 8.

**Scheduled by the Coach for:** Coach decides. The Lab suggests running it after HYP-2 unless the Trainer's first 20
games show Veil or Salamence as the main source of losses. In that case, run it first.

**Dependencies (FACT_CHECK for the Scout):**
1. Mega-turn Speed (mechanics §13 Q1). It decides the Ninetales turn-1 race.
2. Do Psychic Fangs and Brick Break remove Aurora Veil in-game in Champions?
3. Is Metagrossite sold for VP (2,000 VP per Game8), and can the Trainer afford two stones?

## 5. Verdict
- **Result:** not tested yet. 0–0 over 0 games.
- **Verdict:** pending.
- **What we learned:** none yet.

## 6. Playbook
- Not validated.

## Sources
The brief's keys (S1, S2, S4, S5, S11, S15) expand as in `knowledge/meta/singles/brief-2026-09-28.md` §9. L1–L5 are as
in `lab/hypotheses/z-guard-balance.md`:
- **L1:** Showdown calc, Champions mode (every number above).
- **L2:** Serebii Champions Pokédex. Metagross has Psychic Fangs, Ice Punch, Earthquake, Bullet Punch and Clear Body.
  Mega Metagross has Tough Claws.
- **L3:** Official M-C eligible list.
- **L4:** Mega Metagross is in the M-B additions (official in-game news #776, https://news.pokemon-home.com/en/page/776.html,
  accessed 2026-09-28, Tier 1).

Plus:
- [in-game Metagross set; ranks #10 in M-5 and #22 in M-6] — (PokéChamp DB,
  https://pokechamdb.com/snapshots/pokemon/metagross.json and /snapshots/rankings/M-6/single.json, snapshots 2026-09-27
  and 2026-09-06, accessed 2026-09-28, Tier 2).
- [Mega Metagross on 13.8% of teams, #8, at the 1500 cutoff in M-B] — (Smogon usage stats,
  https://www.smogon.com/stats/2026-08/gen9championsbssregmb-1500.txt, published September 2026, accessed 2026-09-28,
  Tier 2; the brief's S5).
