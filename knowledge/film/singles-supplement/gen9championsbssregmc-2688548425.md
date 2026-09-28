---
event: "Pokémon Showdown ladder: [Gen 9 Champions] BSS Reg M-C (non-official)"
date: 2026-09-27
era: singles-supplement
format: "Champions BSS Reg M-C (Pokémon Showdown ladder)"
mode: singles
division: ladder
round: "rated ladder game (one game, not a set)"
players: [sky2132, Ghostofcolress]
winner: Ghostofcolress
rating: 1460   # Showdown replay rating (= the lower of the two post-game Elos). Pre-game Elo [log]: sky2132 1483, Ghostofcolress 1439
video: https://replay.pokemonshowdown.com/gen9championsbssregmc-2688548425
team_lists: "none published; both 6s come from the log's Team Preview; sets only as revealed in play"
official: false
status: draft   # extracted from the exact text log; awaiting the second-agent QC in README 4.5 step 6
---

> **NON-OFFICIAL.** This is a Pokémon Showdown ladder game. It is not Pokémon Champions in-game ranked and not a
> Play! Pokémon event. Both players are ladder players, not pros, so "what the high-rated player did" is not
> automatically the best play.
> `[log]` = taken from the replay's battle log. `[inferred]` = a deduction the log supports but doesn't state.
> **My read** = Scout analysis.
> Source: the battle log — (Pokémon Showdown replay, https://replay.pokemonshowdown.com/gen9championsbssregmc-2688548425.json,
> accessed 2026-09-28, Tier 2). Typings, abilities and base stats — (Pokémon Showdown public data,
> https://play.pokemonshowdown.com/data/pokedex.json, accessed 2026-09-28, Tier 2). Move data — (Pokémon Showdown public
> data, https://play.pokemonshowdown.com/data/moves.json, accessed 2026-09-28, Tier 2). This is Showdown's data, not
> checked against the Champions game client.
> Rules [log]: Level 50, Species Clause, Item Clause, register 6 / bring 3. 11 turns, 3 min 28 s, played 05:55 UTC.

## Team Preview

| | sky2132 (p1, 1483 pre-game) | Ghostofcolress (p2, 1439 pre-game) |
|---|---|---|
| Registered 6 [log] | Golisopod, Pelipper, Swampert, Archaludon, Cinderace, Garchomp | Samurott-Hisui, Aegislash, Ninetales-Alola, Baxcalibur, Venusaur, Cinderace |
| Brought 3 [log] | Pelipper, Archaludon, Golisopod | Cinderace, Ninetales-Alola, Samurott-Hisui |
| Lead [log] | Pelipper | Cinderace |
| Mega Evolution [log] | Golisopod → Mega Golisopod (T6) | none |

**Sets revealed in play** [log], with items or abilities marked [inferred] where the log only implies them:
- **Pelipper:** Drizzle; Hurricane. The rain it set on T4 was still up at the end of T10, so it lasted 8 turns → Damp Rock [inferred].
- **Archaludon:** Flash Cannon, Electro Shot. It got no Defense boost when hit on T10, so its ability isn't Stamina (it's Sturdy or Stalwart) [inferred].
- **Golisopod:** Golisopite; Leech Life, Drill Run, Sucker Punch. Mega Golisopod is Bug/Steel with Tough Claws (Showdown data), which is why Pyro Ball was 4x [log].
- **Cinderace:** Libero; Life Orb; High Jump Kick, Pyro Ball.
- **Ninetales-Alola:** Snow Warning; Aurora Veil. The Veil lasted T2–T9 (8 turns) → Light Clay [inferred].
- **Samurott-Hisui:** Focus Sash; Ceaseless Edge, Sacred Sword, Aqua Jet.

**Likely win conditions (my read):**
- **sky2132, rain offense:** Pelipper's Drizzle lets Archaludon fire Electro Shot without a charge turn (+1 SpA each use)
  and powers Water moves. Mega Golisopod is the physical wallbreaker, with Sucker Punch as priority.
- **Ghostofcolress, weather denial plus hazards:** Ninetales-Alola's Snow Warning overrides rain and enables Aurora Veil.
  Samurott-Hisui lays a layer of Spikes with every Ceaseless Edge and closes with Focus Sash plus Aqua Jet. Cinderace
  (Libero, Life Orb) is the fast cleaner.

## Turn Log
- Lead: Pelipper (Drizzle → rain) vs Cinderace. [log]
- T1: Ghostofcolress switches Cinderace → Ninetales-Alola; Snow Warning replaces rain with snow. Pelipper's Hurricane → Ninetales 58%, confused. [log]
- T2: sky2132 switches Pelipper → Archaludon. Ninetales (confused, but acts) sets Aurora Veil. [log]
- T3: Archaludon Flash Cannon (4x) → Ninetales KO through the Veil (58% → 0). Samurott-Hisui comes in. [log]
- T4: sky2132 switches Archaludon → Pelipper, and rain returns. Samurott-H Ceaseless Edge (critical hit) → Pelipper 40%; Spikes ×1 on sky2132's side. [log]
- T5: Samurott-H moves first: Ceaseless Edge → Pelipper KO; Spikes ×2. Golisopod comes in at 83% after Spikes. [log]
- T6: Ghostofcolress switches Samurott-H → Cinderace. Golisopod Mega Evolves and uses Leech Life (resisted) → Cinderace 75%; Golisopod drains 83% → 95%. [log]
- T7: Cinderace moves first: High Jump Kick → Golisopod 45%. Libero makes Cinderace Fighting-type; Life Orb → Cinderace 65%. Golisopod Drill Run → Cinderace 33%. [log]
- T8: sky2132's turn timer drops to 30 s. Golisopod Sucker Punch (resisted by the Fighting-type Cinderace) → 19%. Cinderace Pyro Ball (4x) → Golisopod KO; Life Orb → Cinderace 9%. Archaludon comes in at 83% after Spikes. [log]
- T9: Archaludon Electro Shot (fires the same turn in rain; +1 SpA) → Cinderace KO. Aurora Veil ends. Samurott-H comes in at 100%. [log]
- T10: Archaludon moves first: Electro Shot (+2 SpA) → Samurott-H hangs on at 1% with Focus Sash. Samurott-H Sacred Sword (2x) → Archaludon 10%. [log]
- T11: Samurott-H Aqua Jet (priority, resisted) → Archaludon KO. **Ghostofcolress wins** with Samurott-H at 1%. Elo: sky2132 1483 → 1460, Ghostofcolress 1439 → 1462. [log]

## Key Decisions
1. **T1: Ghostofcolress answers the rain lead with Ninetales-Alola.** The alternative was to stay in with Cinderace,
   but Pyro Ball is halved in rain and High Jump Kick is resisted by Pelipper's Flying type. My read: correct. Snow
   Warning cancels rain at once: no rain-boosted Water hits, Electro Shot needs its charge turn again, and Hurricane
   drops to 70% accuracy (it hit anyway). Ninetales took 42% plus confusion and still set Aurora Veil the next turn.
2. **T2–T3: sky2132 brings Archaludon in on Ninetales-Alola.** Steel resists both of Ninetales' STAB types (Ice and
   Fairy) and hits it 4x, and the Veil didn't save it. My read: sky2132's best sequence of the game. It removed
   Ghostofcolress's weather and Veil setter without losing anything.
3. **T4: sky2132 goes back to Pelipper to restore rain against Samurott-Hisui.** The alternative was to keep
   Archaludon in, but Flash Cannon is resisted by Samurott-H's Water typing and Electro Shot needs a charge turn in
   snow, which gives Samurott a free hit. My read: reasonable, because Archaludon's plan depends on rain. The cost was
   Pelipper taking the hit that lays Spikes. The critical hit (60% instead of about 40%) turned a Pelipper that could
   have pivoted again into a sack. That's variance, not a decision error.
4. **T5: Pelipper (40%) stays in and is KO'd before it moves.** That gave Golisopod a free entry, at 83% because of
   Spikes ×2. My read: fine. Rain was already up for 8 turns (Damp Rock), and a switch would still have let Ceaseless
   Edge land on the incoming Pokémon and add the second layer.
5. **T8: sky2132 clicks Sucker Punch with Mega Golisopod (45%) against Cinderace (33%).** This one is quizzed in
   `knowledge/film/positions/ss-gen9championsbssregmc-2688548425-t8.md`. In short (my read): after High Jump Kick,
   Libero left Cinderace Fighting-type, so Sucker Punch was resisted and couldn't KO. The alternative was switching to
   Archaludon to take a rain-weakened, non-STAB Pyro Ball and keep Golisopod's priority for the Samurott-H endgame.
6. **T10–T11: the Focus Sash plus Aqua Jet endgame.** Archaludon (83%, +1 SpA) faced a 100% Samurott-H with its Sash
   intact. Any single hit leaves it at 1%, and Sacred Sword (2x) followed by Aqua Jet finishes Archaludon. My read: by
   T9, sky2132 had no answer left to Sash plus priority. It had no multi-hit move and no residual damage: rain doesn't
   hurt Samurott-H, and both Spikes layers were on sky2132's own side.

## Turning Points
1. **T4–T5:** Samurott-Hisui's two Ceaseless Edges removed Pelipper and left Spikes ×2, so every later sky2132
   switch-in lost 1/6 of its HP.
2. **T8:** Sucker Punch was resisted by the Libero-Fighting Cinderace. Golisopod died without removing Cinderace, and
   Archaludon had to spend T9 finishing it.
3. **T10–T11:** Focus Sash plus Aqua Jet. Samurott-Hisui survived Electro Shot at 1% and won the 1-on-1.

## Lessons
- **Weather wars: switch your own weather setter in first.** Snow Warning on the switch turned rain off before
  Pelipper's Hurricane landed (70% accuracy instead of 100%) and made Archaludon's Electro Shot a two-turn move again.
  `[era: singles-supplement | mode: singles | topic: weather]`
- **Libero and Protean change the user's type once per switch-in** (the Gen 9 rule; the log shows no second type
  change on T8). A Cinderace that has used High Jump Kick stays Fighting-type: Dark priority is resisted and its Fire
  moves lose STAB. Check the type indicator before choosing your move.
  `[era: singles-supplement | mode: singles | topic: abilities-type-change]`
- **Focus Sash plus priority wins 1-on-1 endgames.** Break the Sash with chip damage before the last exchange (hazards
  on their side, multi-hit moves, weather damage), or keep a priority user of your own healthy.
  `[era: singles-supplement | mode: singles | topic: endgame]`
- **Ceaseless Edge sets Spikes while it attacks.** Two hits made two layers (1/6 HP per switch-in). Against
  Samurott-Hisui, switch as little as possible or remove it early.
  `[era: singles-supplement | mode: singles | topic: hazards]`
- **Aurora Veil with Light Clay lasts 8 turns** (T2–T9 here). Count Veil and screen turns from the turn they go up.
  `[era: singles-supplement | mode: singles | topic: screens]`
