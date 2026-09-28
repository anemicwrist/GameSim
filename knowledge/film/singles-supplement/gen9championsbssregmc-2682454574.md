---
event: "Pokémon Showdown ladder: [Gen 9 Champions] BSS Reg M-C (non-official)"
date: 2026-09-16
era: singles-supplement
format: "Champions BSS Reg M-C (Pokémon Showdown ladder)"
mode: singles
division: ladder
round: "rated ladder game (one game, not a set)"
players: [hengcaiji, Gosaimasu]
winner: Gosaimasu
rating: 1377   # Showdown replay rating (= the lower of the two post-game Elos). Pre-game Elo [log]: hengcaiji 1394, Gosaimasu 1438
video: https://replay.pokemonshowdown.com/gen9championsbssregmc-2682454574
team_lists: "none published; both 6s come from the log's Team Preview; sets only as revealed in play"
official: false
status: verified   # turn log checked against the replay log by tools/showdown_replays.py on 2026-09-28 (README 4.5, replays step 3)
---

> **NON-OFFICIAL.** This is a Pokémon Showdown ladder game. It is not Pokémon Champions in-game ranked and not a
> Play! Pokémon event. Both players are ladder players, not pros, so "what the high-rated player did" is not
> automatically the best play.
> `[log]` = taken from the replay's battle log. `[inferred]` = a deduction the log supports but doesn't state.
> **My read** = Scout analysis.
> Source: the battle log — (Pokémon Showdown replay, https://replay.pokemonshowdown.com/gen9championsbssregmc-2682454574.json,
> accessed 2026-09-28, Tier 2). Typings, abilities and base stats — (Pokémon Showdown public data,
> https://play.pokemonshowdown.com/data/pokedex.json, accessed 2026-09-28, Tier 2). Move data — (Pokémon Showdown public
> data, https://play.pokemonshowdown.com/data/moves.json, accessed 2026-09-28, Tier 2). This is Showdown's data, not
> checked against the Champions game client.
> Rules [log]: Level 50, Species Clause, Item Clause, register 6 / bring 3. 10 turns, 2 min 01 s, played 17:54 UTC.
> Gosaimasu was #3 on the Showdown Reg M-C ladder (Elo 1534) in the 2026-09-28 snapshot
> (Pokémon Showdown ladder, https://pokemonshowdown.com/ladder/gen9championsbssregmc.json, accessed 2026-09-28, Tier 2).

## Team Preview

| | hengcaiji (p1, 1394 pre-game) | Gosaimasu (p2, 1438 pre-game) |
|---|---|---|
| Registered 6 [log] | Raichu, Garchomp, Greninja, Salamence, Corviknight, Primarina | Grimmsnarl, Gholdengo, Golisopod, Hippowdon, Ceruledge, Salamence |
| Brought 3 [log] | Primarina, Greninja, Corviknight | Grimmsnarl, Gholdengo, and a third Pokémon that never appeared |
| Lead [log] | Primarina | Grimmsnarl |
| Mega Evolution [log] | Greninja → Mega Greninja (T7) | none |

**Sets revealed in play** [log], with items or abilities marked [inferred] where the log only implies them:
- **Primarina:** Calm Mind, Moonblast, Sparkling Aria.
- **Greninja:** Greninjite; Protean; Dark Pulse. Mega Greninja is Water/Dark with Protean (Showdown data).
- **Corviknight:** Mirror Armor; Leftovers; Bulk Up, Brave Bird.
- **Grimmsnarl:** Light Screen, Spirit Break, Parting Shot. The Light Screen lasted T1–T8 (8 turns) → Light Clay
  [inferred]. The log never names the ability, but its status moves went first both times (T1, T4) even though it
  looks speed-tied with Primarina. That fits Prankster, its standard ability [inferred].
- **Gholdengo:** Leftovers; Nasty Plot, Shadow Ball, Make It Rain. Make It Rain lowered its SpA by **2** stages
  [log]. The public Showdown move data (base Gen 9) says 1 stage, and the same −2 appears in all 3 Make It Rain uses in
  the 51 replays pulled for this batch. That points to a Champions-format change as Showdown runs it. It isn't verified
  against the game client and needs an entry in knowledge/mechanics.md.

**Likely win conditions (my read):**
- **hengcaiji, special offense plus a physical wall:** Primarina sets up Calm Mind and sweeps; Mega Greninja (Protean)
  is the fast special cleaner; Corviknight (Bulk Up, Mirror Armor) handles physical attackers.
- **Gosaimasu, screens into a Nasty Plot sweep:** Grimmsnarl sets screens, chips with Spirit Break (which lowers SpA),
  and Parting Shots into Gholdengo, whose Good as Gold blocks status moves. Gholdengo sets up behind the Light Screen.

## Turn Log
- Lead: Primarina vs Grimmsnarl. [log]
- T1: Grimmsnarl (first) Light Screen. Primarina Calm Mind (+1 SpA, +1 SpD). [log]
- T2: Grimmsnarl (first) Spirit Break → Primarina 62%, −1 SpA. Primarina Calm Mind (net +1 SpA, +2 SpD). [log]
- T3: Primarina moves first this time: Moonblast (2x) → Grimmsnarl 32%. Grimmsnarl Spirit Break → Primarina 27%, −1 SpA (net +0). [log]
- T4: Grimmsnarl (first) Parting Shot → Primarina −1 Atk, −1 SpA; Gosaimasu brings in Gholdengo. Primarina Moonblast (resisted) → Gholdengo 91%, then 96% after Leftovers. [log]
- T5: Gholdengo (first) Nasty Plot (+2 SpA). Primarina Sparkling Aria → Gholdengo 73%, then 79% after Leftovers. [log]
- T6: Gholdengo Shadow Ball → Primarina KO; Leftovers → 85%. Greninja comes in. [log]
- T7: Greninja Mega Evolves and moves first: Dark Pulse (Protean → Dark-type; 2x) → Gholdengo 40%. Gholdengo Make It Rain → Mega Greninja KO; Gholdengo −2 SpA; Leftovers → 46%. Corviknight comes in. [log]
- T8: Gholdengo Nasty Plot (+2 SpA). Corviknight Bulk Up (+1 Atk, +1 Def). Leftovers → 52%. Gosaimasu's Light Screen ends. [log]
- T9: Gholdengo (first) Shadow Ball → Corviknight 25%; Mirror Armor bounces the SpD drop back onto Gholdengo (−1 SpD). Corviknight Brave Bird (resisted) → Gholdengo 28%; recoil → Corviknight 18%. Leftovers: Gholdengo 34%, Corviknight 23%. [log]
- T10: Gholdengo Shadow Ball → Corviknight KO. **Gosaimasu wins** with Grimmsnarl 32%, Gholdengo 34% and an unseen third Pokémon. Elo: hengcaiji 1394 → 1377, Gosaimasu 1438 → 1455. [log]

## Key Decisions
1. **T1–T2: hengcaiji uses Calm Mind twice into Grimmsnarl.** The second one is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2682454574-t2.md`. My read: the Calm Mind plan can't beat
   Spirit Break. Each hit removes the SpA boost Calm Mind just added and takes about 35–38%, and Light Screen was
   already halving Primarina's special attacks. Moonblast on T2 (which did 68% at the same +1 on T3) would have
   pressured Grimmsnarl a full turn earlier.
2. **T3: Primarina Moonblasts at +1 SpA.** It did 68%. My read: correct once Spirit Break was revealed.
3. **T4: Gosaimasu's Parting Shot into Gholdengo.** This one is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2682454574-t4.md`. My read: the best play of the game. Attacking
   would have been a speed-tie coin flip (Primarina KOs Grimmsnarl or Spirit Break KOs Primarina). Prankster Parting
   Shot went first for certain, dropped Primarina to −1 SpA, and let Gholdengo take a resisted Moonblast (9%).
4. **T5: hengcaiji chips with a −1 SpA Primarina (27%).** Sparkling Aria did 23% before Primarina fell, and Greninja
   got a free switch-in after the KO. My read: fine. Primarina was sack fodder at that point, and a switch would have
   given Gholdengo a free Nasty Plot anyway.
5. **T7: Make It Rain, not Shadow Ball, into Mega Greninja.** My read: correct. Greninja is Water/Dark, which resists
   both of Gholdengo's STABs, but Protean turns it pure Dark when it uses Dark Pulse, so Steel became neutral while
   Ghost stayed resisted. Light Screen was still up on T7 (the 7th turn of a Light Clay screen) and halved the Dark
   Pulse to 45%. Without it, the same hit would have been about 90% against Gholdengo's 85%, so probably a KO (no calc
   done).
6. **T8: Corviknight uses Bulk Up against a special attacker.** Gholdengo took a free Nasty Plot. My read: Bulk Up's
   Defense boost does nothing against Shadow Ball, and Corviknight had no real answer anyway. Brave Bird is resisted
   by Steel and Body Press can't touch a Ghost type (Corviknight never showed it). The game was decided on T4–T7.

## Turning Points
1. **T2–T3:** Spirit Break's SpA drops cancelled both Calm Minds' SpA gains. By the end of T3 Primarina was back to
   +0 SpA (with +2 SpD) and down to 27%, having landed one +1 Moonblast.
2. **T4:** Parting Shot brought Gholdengo in for free on a resisted hit, with the Light Screen still up.
3. **T7:** Gholdengo survived a super-effective Mega Greninja Dark Pulse at 40%, with Light Screen (Light Clay)
   halving the hit, and KO'd it with Make It Rain.

## Lessons
- **Calm Mind loses to Spirit Break.** Spirit Break always lowers SpA by 1, so each hit cancels one Calm Mind while
  dealing damage. Against a Grimmsnarl lead, attack immediately. `[era: singles-supplement | mode: singles | topic: setup]`
- **A Prankster Parting Shot is a guaranteed safe pivot.** It goes first, weakens the attacker, and brings your sweeper
  in on a hit it resists. Use it when your active Pokémon would otherwise have to win a speed tie.
  `[era: singles-supplement | mode: singles | topic: pivoting]`
- **Light Clay screens last 8 turns.** Count from the turn they go up (T1 → through T8 here), and don't plan a special
  attack around the screen ending after 5. `[era: singles-supplement | mode: singles | topic: screens]`
- **Protean and Libero change type before the hit lands.** A Greninja using Dark Pulse becomes pure Dark and loses the
  Water typing that resisted Steel. `[era: singles-supplement | mode: singles | topic: abilities-type-change]`
- **Make It Rain costs 2 SpA stages in Showdown's Champions format** [log] (1 in Scarlet/Violet). After one Make It
  Rain, Gholdengo needs Nasty Plot or a switch to threaten again, so that's a window to attack it.
  `[era: singles-supplement | mode: singles | topic: mechanics]`
