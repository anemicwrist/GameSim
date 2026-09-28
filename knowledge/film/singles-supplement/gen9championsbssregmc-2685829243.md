---
event: "Pokémon Showdown ladder: [Gen 9 Champions] BSS Reg M-C (non-official)"
date: 2026-09-22
era: singles-supplement
format: "Champions BSS Reg M-C (Pokémon Showdown ladder)"
mode: singles
division: ladder
round: "rated ladder game (one game, not a set)"
players: [qhzht, LGPESWEEPER]
winner: LGPESWEEPER
rating: 1369   # Showdown replay rating (= the lower of the two post-game Elos). Pre-game Elo [log]: qhzht 1438, LGPESWEEPER 1344
video: https://replay.pokemonshowdown.com/gen9championsbssregmc-2685829243
team_lists: "none published; both 6s come from the log's Team Preview; sets only as revealed in play"
official: false
status: verified   # turn log checked against the replay log by tools/showdown_replays.py on 2026-09-28 (README 4.5, replays step 3)
---

> **NON-OFFICIAL.** This is a Pokémon Showdown ladder game. It is not Pokémon Champions in-game ranked and not a
> Play! Pokémon event. Both players are ladder players, not pros, so "what the high-rated player did" is not
> automatically the best play.
> `[log]` = taken from the replay's battle log. `[inferred]` = a deduction the log supports but doesn't state.
> **My read** = Scout analysis.
> Source: the battle log — (Pokémon Showdown replay, https://replay.pokemonshowdown.com/gen9championsbssregmc-2685829243.json,
> accessed 2026-09-28, Tier 2). Typings, abilities and base stats — (Pokémon Showdown public data,
> https://play.pokemonshowdown.com/data/pokedex.json, accessed 2026-09-28, Tier 2). Move data — (Pokémon Showdown public
> data, https://play.pokemonshowdown.com/data/moves.json, accessed 2026-09-28, Tier 2). This is Showdown's data, not
> checked against the Champions game client.
> Rules [log]: Level 50, Species Clause, Item Clause, register 6 / bring 3. 8 turns, 2 min 15 s, played 14:58 UTC.

## Team Preview

| | qhzht (p1, 1438 pre-game) | LGPESWEEPER (p2, 1344 pre-game) |
|---|---|---|
| Registered 6 [log] | Primarina, Salamence, Glimmora, Blaziken, Rillaboom, Baxcalibur | Salamence, Gyarados, Mimikyu, Meowscarada, Mamoswine, Lucario |
| Brought 3 [log] | Glimmora, Blaziken, Baxcalibur | Gyarados, Lucario, Mimikyu |
| Lead [log] | Glimmora | Gyarados |
| Mega Evolution [log] | Blaziken → Mega Blaziken (T4) | Lucario → Mega Lucario Z (T2) |

**Sets revealed in play** [log]:
- **Glimmora:** Focus Sash; Stealth Rock, Mud Shot. The log never names its ability (Showdown data: Toxic Debris or
  Corrosion).
- **Blaziken:** Blazikenite; Speed Boost; Flare Blitz, Thunder Punch. Mega Blaziken is Fire/Fighting (Showdown data).
- **Baxcalibur:** fainted before acting, so nothing was revealed.
- **Gyarados:** Intimidate; Leftovers. None of its moves appeared.
- **Lucario:** Lucarionite Z; Flash Cannon, Vacuum Wave. Mega Lucario Z is Fighting/Steel with base Speed 151
  (Showdown data).
- **Mimikyu:** Disguise; Life Orb; Play Rough, Shadow Sneak.

**Likely win conditions (my read):**
- **qhzht, hazard lead into a Speed Boost sweep:** a Focus Sash Glimmora guarantees Stealth Rock, then Mega Blaziken
  (Speed Boost, Thunder Punch for Water types) sweeps a chipped team. Baxcalibur is the second physical attacker.
- **LGPESWEEPER, fast Mega plus priority cleanup:** Gyarados (Intimidate) softens physical attackers, Mega Lucario Z
  (base 151 Speed, Vacuum Wave) removes frail or Sash leads, and Mimikyu (Disguise, Life Orb, Shadow Sneak) cleans up
  late.

## Turn Log
- Lead: Glimmora vs Gyarados; Intimidate → Glimmora −1 Atk. [log]
- T1: LGPESWEEPER switches Gyarados → Lucario. Glimmora Stealth Rock. [log]
- T2: Lucario Mega Evolves and moves first: Flash Cannon (2x) → Glimmora hangs on at 1% with Focus Sash. Glimmora Mud Shot (2x) → Lucario 45%, −1 Spe. [log]
- T3: Lucario Vacuum Wave (priority) → Glimmora KO. Blaziken comes in. [log]
- T4: LGPESWEEPER switches Lucario → Gyarados; Stealth Rock → 75%; Intimidate → Blaziken −1 Atk. Blaziken Mega Evolves; Flare Blitz (resisted) → Gyarados 53%, then 59% after Leftovers; recoil → Blaziken 91%; Speed Boost +1 Spe. [log]
- T5: Mega Blaziken (first) Thunder Punch (4x) → Gyarados KO; Speed Boost → +2. Mimikyu comes in; Stealth Rock → 87%. [log]
- T6: qhzht switches Mega Blaziken → Baxcalibur. Mimikyu Play Rough (2x) → Baxcalibur KO from 100%; Life Orb → Mimikyu 78%. Mega Blaziken comes back in at 91%. [log]
- T7: Mega Blaziken (first) Flare Blitz → Disguise absorbs it (no damage, so no recoil); busting costs Mimikyu 1/8 → 65%. Mimikyu Play Rough → Blaziken 22%; Life Orb → Mimikyu 56%. Speed Boost +1. [log]
- T8: Mimikyu Shadow Sneak (priority) → Blaziken KO; Life Orb → Mimikyu 46%. **LGPESWEEPER wins** with Mega Lucario Z 45% and Mimikyu 46%. Elo: qhzht 1438 → 1413, LGPESWEEPER 1344 → 1369. [log]

## Key Decisions
1. **T1: LGPESWEEPER answers the Glimmora lead with Lucario.** My read: sound. A Sash Glimmora gets Stealth Rock up
   whatever you do, so the question is how cheaply you remove it. Mega Lucario Z did it with a special STAB (Flash
   Cannon, 2x) plus priority (Vacuum Wave) to finish through the Sash. Special attacks also avoid Toxic Debris, which
   lays Toxic Spikes when Glimmora is hit by a physical move (its first ability per Showdown data; not revealed here).
   The cost was real: Mud Shot took Lucario to 45% and −1 Speed, and Stealth Rock stayed up for the rest of the game.
2. **T4: LGPESWEEPER switches the 45% Lucario out to Gyarados.** This one is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2685829243-t4.md`. My read: a bet that Mega Blaziken had no
   Electric coverage. Gyarados paid 25% to Stealth Rock just to enter and was slower than Blaziken after one Speed
   Boost, so it died the next turn without moving.
3. **T4: qhzht Mega Evolves and uses Flare Blitz.** It was resisted by the incoming Gyarados. The alternative was
   Thunder Punch, which would have been 4x on Gyarados and neutral on a Lucario that stayed in. My read: close. Flare
   Blitz was the sure KO if Lucario stayed (2x on Steel), and Speed Boost made up the lost turn anyway.
4. **T6: qhzht switches Mega Blaziken out to Baxcalibur against a fresh Mimikyu.** This one is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2685829243-t6.md`. My read: the losing move. Baxcalibur
   (Dragon/Ice) is weak to Mimikyu's Fairy STAB and was OHKO'd from 100%.
5. **T7–T8: Mimikyu's Disguise plus Shadow Sneak finishes the game.** Disguise took the Flare Blitz (and denied its
   recoil), Play Rough did 69%, and Shadow Sneak picked off the 22% Blaziken before Speed Boost could matter.

## Turning Points
1. **T2–T3:** Mega Lucario Z beat Glimmora's Focus Sash with Flash Cannon plus Vacuum Wave, but only after Stealth
   Rock was up and Lucario had taken 55%.
2. **T5:** Mega Blaziken's Thunder Punch (4x) KO'd Gyarados. qhzht was then ahead: Blaziken 91% at +2 Spe and
   Baxcalibur 100%, against Lucario 45% and Mimikyu 87%.
3. **T6:** Baxcalibur switched into Play Rough and was OHKO'd, leaving one against two.
4. **T7–T8:** Disguise absorbed a hit, and Play Rough plus Shadow Sneak finished Blaziken.

## Lessons
- **Team Preview: count what your pick is weak to on their side.** Baxcalibur is weak to Fairy (Mimikyu) and to Steel
  and Fighting (Lucario), and LGPESWEEPER's 6 showed both. qhzht's Rillaboom would have taken neutral damage from all
  four of those STAB types. My read: Baxcalibur was probably picked because its Ice STAB threatens Salamence (4x) and
  Meowscarada (2x), which makes it a bet on which three the opponent brings.
  `[era: singles-supplement | mode: singles | topic: team-preview]`
- **Mimikyu gets two actions.** Disguise absorbs the first hit, and Shadow Sneak (priority) finishes weakened targets.
  Count Shadow Sneak into your endgame HP. `[era: singles-supplement | mode: singles | topic: priority]`
- **Stealth Rock punishes Flying-type switch-ins.** Gyarados lost 25% just entering on T4 (Rock is 2x on Flying).
  `[era: singles-supplement | mode: singles | topic: hazards]`
- **A Focus Sash hazard lead will get its hazard up.** Remove it efficiently, with a STAB hit plus priority to get
  through the Sash, and prefer special attacks against Glimmora (Toxic Debris triggers on physical hits).
  `[era: singles-supplement | mode: singles | topic: leads]`
- **Speed Boost Blaziken gets faster every turn it stays in.** Keep a priority user (Shadow Sneak, Vacuum Wave) for
  it, and don't count on outspeeding it one turn later. `[era: singles-supplement | mode: singles | topic: speed-control]`
