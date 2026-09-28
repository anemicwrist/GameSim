---
event: "Pokémon Showdown ladder: [Gen 9 Champions] BSS Reg M-C (non-official)"
date: 2026-09-18
era: singles-supplement
format: "Champions BSS Reg M-C (Pokémon Showdown ladder)"
mode: singles
division: ladder
round: "rated ladder game (one game, not a set)"
players: [Dragalge THL, mk7juju]
winner: Dragalge THL
rating: 1428   # Showdown replay rating (= the lower of the two post-game Elos). Pre-game Elo [log]: Dragalge THL 1417, mk7juju 1450
video: https://replay.pokemonshowdown.com/gen9championsbssregmc-2683599297
team_lists: "none published; both 6s come from the log's Team Preview; sets only as revealed in play"
official: false
status: draft   # extracted from the exact text log; awaiting the second-agent QC in README 4.5 step 6
---

> **NON-OFFICIAL.** This is a Pokémon Showdown ladder game. It is not Pokémon Champions in-game ranked and not a
> Play! Pokémon event. Both players are ladder players, not pros, so "what the high-rated player did" is not
> automatically the best play.
> `[log]` = taken from the replay's battle log. `[inferred]` = a deduction the log supports but doesn't state.
> **My read** = Scout analysis.
> Source: the battle log — (Pokémon Showdown replay, https://replay.pokemonshowdown.com/gen9championsbssregmc-2683599297.json,
> accessed 2026-09-28, Tier 2). Typings, abilities and base stats — (Pokémon Showdown source, github.com/smogon/pokemon-showdown
> `data/pokedex.ts` and `data/mods/champions/`, accessed 2026-09-28, Tier 2; Showdown's implementation of Champions,
> not checked against the game client).
> Rules [log]: Level 50, Species Clause, Item Clause, register 6 / bring 3. 26 turns, 5 min 35 s, played 14:58 UTC.
> Data quirk: the log's T22 burn line reads `20/100y brn` (a stray character). The HP is read as 20%.

## Team Preview

| | Dragalge THL (p1, 1417 pre-game) | mk7juju (p2, 1450 pre-game) |
|---|---|---|
| Registered 6 [log] | Sableye, Sylveon, Samurott-Hisui, Dragalge, Gholdengo, Toxapex | Grimmsnarl, Empoleon, Golisopod, Salamence, Volcarona, Gholdengo |
| Brought 3 [log] | Sableye, Toxapex, Samurott-Hisui | Grimmsnarl, Gholdengo, Golisopod |
| Lead [log] | Sableye | Grimmsnarl |
| Mega Evolution [log] | none | Golisopod → Mega Golisopod (T9) |

**Sets revealed in play** [log], with items or abilities marked [inferred] where the log only implies them:
- **Sableye:** Reflect, Light Screen, Will-O-Wisp. Its screens lasted 8 turns each time (Reflect T1–T8 and T11–T18,
  Light Screen T2–T9 and T13–T20) → Light Clay [inferred]. The log never names its ability.
- **Toxapex:** Regenerator; Haze, Recover, Infestation.
- **Samurott-Hisui:** Leftovers; Swords Dance, Razor Shell, Ceaseless Edge.
- **Grimmsnarl:** Reflect, Light Screen, Foul Play. Its screens lasted 8 turns → Light Clay [inferred]. The log never
  names its ability.
- **Gholdengo:** Nasty Plot. It never used an attacking move.
- **Golisopod:** Golisopite; Leech Life, Drill Run, Swords Dance. Mega Golisopod is Bug/Steel with Tough Claws
  (Showdown data).

**Likely win conditions (my read):**
- **Dragalge THL, stall/balance:** Sableye's screens and Will-O-Wisp cripple physical attackers. Toxapex (Haze, Recover,
  Regenerator) erases setup. Samurott-Hisui (Swords Dance, Leftovers) is the cleaner, and its Dark STAB hits Gholdengo
  super effectively.
- **mk7juju, screens setup offense:** Grimmsnarl sets both screens, then Gholdengo (Nasty Plot) or Mega Golisopod
  (Swords Dance) sets up behind them and sweeps.

## Turn Log
- Lead: Sableye vs Grimmsnarl. [log]
- T1: Grimmsnarl (first) Reflect; Sableye Reflect. Both sides now have Reflect. [log]
- T2: Grimmsnarl Light Screen; Sableye Light Screen. [log]
- T3: Double switch: mk7juju Grimmsnarl → Gholdengo; Dragalge THL Sableye → Toxapex. [log]
- T4: Dragalge THL switches Toxapex → Samurott-Hisui. Gholdengo Nasty Plot (+2 SpA). [log]
- T5: mk7juju switches Gholdengo → Grimmsnarl. Samurott-H Swords Dance (+2 Atk). [log]
- T6: Samurott-H (first) Swords Dance (+4). Grimmsnarl Foul Play (resisted) → Samurott-H 58%, then 64% after Leftovers. [log]
- T7: Samurott-H Razor Shell → Grimmsnarl 14%. Grimmsnarl Foul Play → Samurott-H 21%, then 27% after Leftovers. [log]
- T8: Samurott-H Razor Shell → Grimmsnarl KO; Leftovers → 34%. Both Reflects end. Golisopod comes in. [log]
- T9: Dragalge THL switches Samurott-H → Toxapex. Golisopod Mega Evolves and uses Leech Life (resisted) → Toxapex 80%. Both Light Screens end. [log]
- T10: Dragalge THL switches Toxapex (Regenerator → 100%) → Sableye. Golisopod Drill Run → Sableye 58%. [log]
- T11: Sableye Reflect. Golisopod Swords Dance (+2). [log]
- T12: Sableye Will-O-Wisp → Golisopod burned. Golisopod Swords Dance (+4); burn → 93%. [log]
- T13: Sableye Light Screen. Golisopod Swords Dance (+6); burn → 87%. [log]
- T14: Dragalge THL switches Sableye → Toxapex. Golisopod (+6) Leech Life (resisted, burned, into Reflect) → Toxapex 78%; Golisopod drains to 97%, then burn → 91%. [log]
- T15: Golisopod (first) Drill Run (2x) → Toxapex 23%. Toxapex Haze clears all boosts. Burn → 85%. [log]
- T16: Golisopod Drill Run → Toxapex 9%. Toxapex Recover → 59%. Burn → 79%. [log]
- T17: Golisopod Swords Dance (+2). Toxapex Infestation (resisted) → Golisopod 78% and trapped. Burn plus Infestation → 59%. [log]
- T18: Golisopod Drill Run → Toxapex 31%. Toxapex Haze. Burn plus Infestation → 41%. Sableye's Reflect ends. [log]
- T19: Golisopod Swords Dance; Toxapex Haze. Burn plus Infestation → 23%. [log]
- T20: Dragalge THL switches Toxapex (Regenerator → 64%) → Sableye (58%). Golisopod Drill Run → Sableye 37%. Burn → 17%; Infestation ends. Sableye's Light Screen ends. [log]
- T21: Sableye Light Screen. Golisopod Leech Life → Sableye 3%; Golisopod drains to 32%, then burn → 26%. [log]
- T22: Sableye Reflect. Golisopod Swords Dance (+2); burn → 20%. [log]
- T23: Sableye Will-O-Wisp fails (Golisopod is already burned). Golisopod Leech Life → Sableye KO; drain → 21%, burn → 15%. Samurott-H comes in at 34%. [log]
- T24: Samurott-H Razor Shell → Golisopod KO; Leftovers → 40%. Gholdengo comes in. [log]
- T25: Samurott-H (first) Ceaseless Edge (2x) → Gholdengo 28%; Spikes on mk7juju's side. Gholdengo Nasty Plot (+2). Leftovers: Samurott-H 46%, Gholdengo 35%. [log]
- T26: Samurott-H (first) Ceaseless Edge → Gholdengo KO. **Dragalge THL wins** with Toxapex 64% and Samurott-H 46%. Elo: Dragalge THL 1417 → 1439, mk7juju 1450 → 1428. [log]

## Key Decisions
1. **T1–T2: the screens mirror.** Both leads set Reflect, then Light Screen. My read: by matching screens, Sableye made
   mk7juju's future sweepers attack into halved damage, while Dragalge THL's own Samurott-H set up behind its own
   screens. The mirror cancelled the reason mk7juju led with Grimmsnarl.
2. **T3–T5: the switch war.** On T3 both players switched (Gholdengo in, Toxapex in). On T4 Dragalge THL sent
   Samurott-Hisui into Gholdengo, which used Nasty Plot. On T5 mk7juju pulled Gholdengo back to Grimmsnarl, and
   Samurott-H got a free Swords Dance. My read: the T4 Samurott-H switch was the key read. Its Dark STAB is 2x on
   Gholdengo, and both of Gholdengo's usual STAB types are resisted by Water/Dark (Steel by Water, Ghost by Dark), so
   Gholdengo's +2 was wasted. Retreating on T5 was understandable for mk7juju, but it cost a free boost.
3. **T6–T7: Grimmsnarl stays in against a +2, then +4, Samurott-Hisui.** If Grimmsnarl has Prankster (standard for it;
   not shown in the log), its Prankster status moves fail against Dark types under the Gen 7+ rule. That left Foul Play,
   which is resisted but scales with the target's boosts: it did 42% and 43%. Samurott-H's +4 Razor Shell did 86%.
   My read: Grimmsnarl traded itself for two-thirds of Samurott-H's HP (100% → 34% after Leftovers), which is
   acceptable, since mk7juju had no safe switch-in to a +4 Samurott-H.
4. **T9: Samurott-Hisui (34%, +4) retreats to Toxapex.** This one is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2683599297-t9.md`. My read: correct. It preserved the one
   Pokémon that threatens Gholdengo.
5. **T11–T13: Mega Golisopod sets up into Sableye.** It used Swords Dance three times while Sableye set Reflect, burned
   it with Will-O-Wisp (T12), and set Light Screen. My read: setting up a physical attacker in front of a likely
   Will-O-Wisp user invites the burn. At +6 (×4) with a burn (×½) into Reflect (×½), Golisopod hit like an unboosted,
   unburned attacker with no screen in the way. Three Swords Dances only cancelled the burn and the Reflect.
6. **T14–T20: Toxapex's Haze loop.** Golisopod reached +6 (T13), +2 (T17) and +2 (T19), and Haze cleared it on T15,
   T18 and T19. Recover and Regenerator switches (T10, T20) kept Toxapex healthy, and Infestation (T17) trapped
   Golisopod for three turns of extra chip damage. The T17 choice is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2683599297-t17.md`.
7. **T25: Gholdengo uses Nasty Plot against a 40% Samurott-Hisui.** Samurott-H moved first on both turns, and Ceaseless
   Edge (2x) did 72%. My read: Nasty Plot only works if Gholdengo moves first or survives two hits, and neither was true.
   Attacking at once was the only chance, and a slim one, because both of Gholdengo's usual STAB types are resisted by
   Water/Dark (its other moves never appeared).

## Turning Points
1. **T4–T8:** Samurott-Hisui's free Swords Dances behind Sableye's screens removed Grimmsnarl, mk7juju's screens setter.
2. **T12:** Will-O-Wisp burned Mega Golisopod, mk7juju's main physical threat.
3. **T15, T18, T19:** Haze erased every Golisopod boost, so its setup turns produced nothing.
4. **T23–T26:** Samurott-Hisui, held back at 34% since T9, KO'd Golisopod and then Gholdengo.

## Lessons
- **Don't set up into a revealed Haze.** Once Toxapex had shown Haze (T15), each Swords Dance was a free turn for
  Recover or Infestation while the burn ticked. `[era: singles-supplement | mode: singles | topic: setup-vs-stall]`
- **Burn plus screens flatten boosts.** +6 Attack (×4) under burn (×½) into Reflect (×½) hits like a clean, unboosted
  attacker. Once a physical sweeper is burned, its job changes. `[era: singles-supplement | mode: singles | topic: status]`
- **Burn only damages the Pokémon while it's on the field.** Switching a burned attacker out stops the 1/16-per-turn
  clock and escapes trapping moves before they land. `[era: singles-supplement | mode: singles | topic: status]`
- **Keep the Pokémon that beats their last one.** Samurott-Hisui at 34% was Dragalge THL's only real threat to
  Gholdengo. It sat out from T9 to T23 and then won the game.
  `[era: singles-supplement | mode: singles | topic: win-condition]`
- **Prankster status moves fail against Dark types** (the Gen 7+ rule; Showdown's Champions mod leaves Prankster
  unchanged). A Prankster Grimmsnarl or Sableye can't Thunder Wave, Will-O-Wisp or Parting Shot a Samurott-Hisui.
  `[era: singles-supplement | mode: singles | topic: mechanics]`
- **Screens with Light Clay last 8 turns** (both setters here). Count them.
  `[era: singles-supplement | mode: singles | topic: screens]`
