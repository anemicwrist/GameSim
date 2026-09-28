# Pokémon Champions: verified mechanics and differences from Scarlet/Violet

As of **2026-09-28** (game v1.2.0 plus server maintenance on 2026-09-11 and 2026-09-16; Regulation Set M-C / Ranked Season M-6).
Owner: Scout. Citation format and tiers: `knowledge/sources.md`. Lines marked `UNVERIFIED` or `OPINION` are not facts.
`[derived]` = arithmetic on a cited formula.

> **Re-test warning.** "Text strings and classifications are just client-side window dressing … battle calculations happen
> server-side … Do not assume knowledge from previous games matches this game, or even knowledge from before the last server
> maintenance. RE-TEST OFTEN" — (Smogon "Champions Battle Mechanics Research" OP,
> https://www.smogon.com/forums/threads/champions-battle-mechanics-research.3780372/, OP 2026-04-07 (edited since), accessed
> 2026-09-28, Tier 2). Below, **"Smogon OP"** means this post, and "Smogon p.N" means page N of the same thread.

---

## 0. The differences that matter most (details and citations in the linked sections)

1. **No Terastallization, Dynamax or Z-Moves.** Mega Evolution is the only battle gimmick, **once per battle** (§3, §4).
2. **Stat Points replace EVs:** 66 total, max 32 per stat, +1 stat per point at Lv 50. **No IVs** (all maxed). Natures are
   now **"Stat Alignment"** (±10%) and can be changed in the menu (§2).
3. **Smaller item pool.** No Choice Band/Specs, Assault Vest, Heavy-Duty Boots, Safety Goggles, Covert Cloak, Booster
   Energy, Eviolite, Toxic/Flame Orb, Weakness Policy… (§8).
4. **Status nerfs:** paralysis full-para 12.5%; sleep is at most 2 turns; freeze thaws by the 3rd turn (§5).
5. **PP rework:** every move is at max PP, nothing above 20. Protect and most recovery moves have **8 PP** (§6).
6. **Dozens of move changes** (BP, accuracy, secondary chances, types, flags) and trimmed learnsets (e.g., Incineroar has no
   Knock Off or U-turn) (§6).
7. **Unseen Fist and Piercing Drill** hit through Protect for only **¼** damage. **Fake Out** can't be clicked after turn 1 out (§6, §7).
8. **Ranked/Casual time-outs are draws**, not wins on count/HP. Running out of "Your Time" is a loss (§10).
9. **Champions-exclusive Megas and abilities** (Mega Garchomp Z, Mega Lucario Z, Mega Starmie with Huge Power, Mega Meganium
   with Mega Sol, …) (§3).
10. **Team Preview shows shinies.** v1.2.0 added **View Log** (current battle only) and **Selection Support** (§11).

---

## 1. Game basics that affect competitive play

- Platforms: Nintendo Switch and iOS/Android, with **cross-platform play** ("mobile device users can battle against Trainers
  playing on Nintendo Switch or Nintendo Switch 2") — (Official site, https://champions.pokemon.com/en-us/, accessed 2026-09-28,
  Tier 1). Mobile launched 2026-06-17. The game is free-to-play with optional purchases, needs an internet connection, and
  shares save data via Nintendo Account — (TPCi press release,
  https://press.pokemon.com/en/releases/Pokemon-Champions-Launches-June-17-on-iOS-and-Android-Devices-The-Poke, 2026-06-03, Tier 1).
- Modes: **Ranked, Casual, Private**, each in **Single or Double** Battles. VP (Victory Points) are earned in battle and
  "cannot be purchased directly" (VPを直接購入することはできません) — (Official site バトルについて,
  https://www.pokemonchampions.jp/ja/battle/, accessed 2026-09-28, Tier 1).
- Getting Pokémon: in-game **Scout/Recruit** (Trial = time-limited, Regular = permanent) or visits from **Pokémon HOME**. Only
  species that exist in Champions can visit. A visiting Pokémon's moves that aren't usable in Champions must be changed in
  Training. Pokémon scouted in Champions can't be deposited to HOME — (Official site ポケモンについて,
  https://www.pokemonchampions.jp/ja/pokemon/, accessed 2026-09-28, Tier 1).
- **Trial-scouted Pokémon can't be trained** (トライアルスカウト中のポケモンをトレーニングすることはできません) — (Official site
  育成について, https://www.pokemonchampions.jp/ja/training/, accessed 2026-09-28, Tier 1).
- **Mobile at official events:** allowed at Open Play, VGC Cups and Challenges and Celebration Events; "not supported at
  Regional Championships and above" — (VGC Tournament Handbook §3.2.1,
  https://www.pokemon.com/static-assets/content-assets/cms2/pdf/play-pokemon/rules/play-pokemon-vgc-tournament-handbook-en.pdf,
  rev. 2026-09-01, Tier 1).
- **Level:** everything battles at Lv 50 in ranked — (Serebii "Season M-6",
  https://www.serebii.net/pokemonchampions/rankedbattle/seasonm-6.shtml, accessed 2026-09-28, Tier 2) — and at official
  events, "auto-leveled to Lv. 50" (Handbook §2.3, Tier 1).

## 2. How stats are invested

- **Stat Points (SP) replace EVs:** "66 Stat Points that you can allocate … with a cap of 32 Stat Points per stat" (vs 510 EVs /
  252 per stat) — (Game8 "What Are Stat Points?", https://game8.co/games/Pokemon-Champions/archives/538683, updated 2026-04-23,
  Tier 3). The Showdown calc's Champions mode limits SP entry to 0–32 per stat — (calc.pokemonshowdown.com `js/shared_controls.js`,
  accessed 2026-09-28, Tier 2).
- **Stat formulas** (credited to the Anubis data dump): "HP = BaseHP + StatPoints + 75;
  Atk/Def/SpA/SpD/Spe = Nature * (BaseStat + StatPoints + 20), where Nature is 0.9, 1.0, or 1.1" — (Smogon OP, Tier 2).
  The Showdown calc's Champions mode uses the same formula, flooring the result — (calc.pokemonshowdown.com `calc/stats.js`,
  accessed 2026-09-28, Tier 2).
  - [derived] 1 SP = +1 to the stat before the nature multiplier.
  - [derived] 32 SP gives the same stat as 252 EVs at Lv 50 with 31 IVs (e.g., Jolly Garchomp, base 102 Spe:
    ⌊1.1 × (102+32+20)⌋ = 169, same as SV's 252+ Spe Garchomp at Lv 50). In SV, 510 EVs are worth 65 stat points at Lv 50.
    Champions gives 66.
  - [derived] **Minimum Speed** = ⌊0.9 × (Base + 20)⌋ (0 SP, −Spe alignment). You **can't** drop below this with IVs.
    OPINION: this matters for Trick Room speed tiers and Gyro Ball.
- **No IVs:** "All Pokemon in the game have maximum IVs." HOME transfers gain max IVs and revert when sent back — (Game8
  "Are There IVs?", https://game8.co/games/Pokemon-Champions/archives/593716, updated 2026-04-09, Tier 3). Serebii: "there seems
  to be no IV adjustment" — (Serebii "Training", https://www.serebii.net/pokemonchampions/training.shtml, accessed 2026-09-28,
  Tier 2). The developer (Hoshino, via GameSpot) described removing IVs to lower the barrier to entry — (Nintendo Everything,
  https://nintendoeverything.com/pokemon-champions-wont-have-ivs-developer-explains-why/, 2026-03-26, Tier 3).
  - Identical-stat mirrors are pure 50/50 Speed ties — (Game8 "Are There IVs?", Tier 3).
- **Stat Alignment = Nature** (+10% / −10%). The VGC team list calls it "Stat alignment" (Handbook §2.4.1, Tier 1). The
  multiplier is in the Smogon formula above.
- **Training menu:** stats, moves, Ability and alignment can all be changed with VP, or for free with a Training Ticket — (Official
  site 育成について, Tier 1). Hidden Abilities are usable at official events (Handbook §2.3, Tier 1).
  - VP costs **conflict**: Serebii lists 2 VP per SP, 100 VP per move, 200 VP per nature and 400 VP per Ability — (Serebii
    "Training", Tier 2). Game8 says 5 VP per SP (330 VP for 66) and that removing SP is free — (Game8 SP page, Tier 3).
    UNVERIFIED which is current. Prices may have changed after launch.

## 3. Mega Evolution

- **Rules:** "Certain Pokémon can Mega Evolve if they're holding a Mega Stone. You can use Mega Evolution only one time per
  battle." — (Official in-game news "Regulation Set M-C", https://news.pokemon-home.com/en/page/816.html, accessed 2026-09-28,
  Tier 1). The same wording appears in M-A (#751) and M-B (#776). You may hold several different Mega Stones, since only duplicate
  items are banned (#816).
- **The Omni Ring** (ゼンブイリング) is the player's Key Stone equivalent for Mega Evolution — (Official site バトルについて,
  https://www.pokemonchampions.jp/ja/battle/, Tier 1). The English name "Omni Ring" comes from Bulbapedia's page title in the
  search index (Bulbapedia is Tier 2 but bot-walled, so not read).
- **Mega Stones** cost 2,000 VP each in the shop — (Game8 "List of New Items", https://game8.co/games/Pokemon-Champions/archives/605519,
  updated 2026-09-09, Tier 3). Some are also Battle Pass rewards, e.g., Golisopite and Lucarionite Z on the M-6 premium track —
  (Game8 "Ranked Battles Season M-6", https://game8.co/games/Pokemon-Champions/archives/620414, updated 2026-09-17, Tier 3).
- **81 Megas are legal in M-C** (59 from M-A, +16 in M-B, +6 in M-C) — [derived] from official notices #751/#776/#816 (Tier 1).
- **Speed on the turn a Pokémon Mega Evolves:** **UNVERIFIED.** Background: in Gen 6, Mega Evolution did not change turn order
  on the turn it happened — (Bulbapedia "Mega Evolution", https://bulbapedia.bulbagarden.net/wiki/Mega_Evolution, seen only as a
  search-index excerpt because the page is bot-walled, accessed 2026-09-28, Tier 2). One uncited guide says Gen 7 re-rolls
  Speed after Mega Evolution, and that Champions uses the Gen 7 rule (post-Mega Speed that turn) — (pokekipe "Mega
  Evolution, Deep-Dive Reference", https://pokekipe.com/guides/mechanics/mega-evolution-deep-dive, "Updated April 2026",
  Tier 3 low-trust). An official known issue at launch said "When both players' Pokémon Mega Evolve simultaneously under
  certain conditions, the turn order may behave incorrectly" — (Official in-game news "Regarding Current Issues",
  https://news.pokemon-home.com/en/page/758.html, 2026-04-09, Tier 1). That implies Mega Evolution affects turn order, but
  isn't proof. **Test it** (Lab/Trainer, Private Battle): a slower-base Mega that becomes faster than the opponent's lead.
- **Mega Evolution order** (which Mega happens first) was bugged at launch, and the developers acknowledged it. After a fix on
  2026-04-09, "a setup tested yesterday resulted in expected Speed order" — (Smogon OP "Acknowledged Bugs". Smogon p.3,
  DaWoblefet stream #3, 2026-04-09, Tier 2).
- Mega Evolution **keeps a Speed Swap–modified Speed** (it doesn't overwrite it) — (Smogon OP. Smogon p.7, DaWoblefet stream #6,
  2026-04-15, Tier 2). **Revival Blessing** revives a Mega as a Mega (e.g., Mega Staraptor) — (Smogon p.10, DaWoblefet,
  2026-09-09, Tier 2). **Poltergeist** now works on Mega Stones — (Game8 list of changes,
  https://game8.co/games/Pokemon-Champions/archives/593893, updated 2026-09-18, Tier 3).

### Champions-specific Megas and abilities

Game8 says "Mega Evolutions from Pokemon Legends: Z-A have been added … including Z Mega Evolutions" — (Game8 list of changes,
https://game8.co/games/Pokemon-Champions/archives/593893, updated 2026-09-18, Tier 3). Champions gives these Megas the following
Abilities — (Serebii "Mega Evolution Abilities", https://www.serebii.net/pokemonchampions/megaabilities.shtml, accessed
2026-09-28, Tier 2):

Mega Raichu X – Electric Surge · Mega Raichu Y – No Guard · Mega Clefable – Magic Bounce · Mega Victreebel – Innards Out ·
Mega Starmie – **Huge Power** · Mega Dragonite – Multiscale · Mega Meganium – **Mega Sol** · Mega Feraligatr – **Dragonize** ·
Mega Skarmory – Stalwart · Mega Chimecho – Levitate · Mega Absol Z – Sharpness · Mega Staraptor – Contrary · Mega Garchomp Z –
Levitate · Mega Lucario Z – **Aura Guard** · Mega Froslass – Snow Warning · Mega Emboar – Mold Breaker · Mega Excadrill –
**Piercing Drill** · Mega Scolipede – Shell Armor · Mega Scrafty – Intimidate · Mega Eelektross – **Eelevate** · Mega Chandelure –
Infiltrator · Mega Golurk – Unseen Fist · Mega Chesnaught – Bulletproof · Mega Delphox – Levitate · Mega Greninja – Protean ·
Mega Pyroar – **Fire Mane** · Mega Floette – Fairy Aura · Mega Meowstic – Trace · Mega Malamar – Contrary · Mega Barbaracle –
Tough Claws · Mega Dragalge – Regenerator · Mega Hawlucha – No Guard · Mega Crabominable – Iron Fist · Mega Golisopod – Tough
Claws · Mega Drampa – Berserk · Mega Falinks – Defiant · Mega Scovillain – **Spicy Spray** · Mega Glimmora – Adaptability ·
Mega Baxcalibur – Thermal Exchange.

New in M-C, with Showdown's data and Game8 agreeing on every value — (Showdown public data pokedex.json,
https://play.pokemonshowdown.com/data/pokedex.json, accessed 2026-09-28, Tier 2. Game8 list of changes, Tier 3):

| Mega | Type | HP-Atk-Def-SpA-SpD-Spe (BST) | Ability |
|---|---|---|---|
| Mega Garchomp Z | **Dragon** (loses Ground) | 108-130-85-141-85-151 (700) | Levitate |
| Mega Lucario Z | Fighting/Steel | 70-100-70-164-70-151 (625) | Aura Guard |
| Mega Absol Z | **Dark/Ghost** | 65-154-60-75-60-151 (565) | Sharpness |
| Mega Baxcalibur | Dragon/Ice | 115-175-117-105-101-87 (700) | Thermal Exchange |
| Mega Golisopod | Bug/Steel | 75-150-175-70-120-40 (630) | Tough Claws |
| Mega Salamence | Dragon/Flying | 95-145-130-120-90-120 (700) | Aerilate |

New ability texts — (Serebii "New Abilities", https://www.serebii.net/pokemonchampions/newabilities.shtml, accessed 2026-09-28, Tier 2):
- **Piercing Drill:** contact moves hit targets that are protecting for ¼ damage. Everything except the protection's own
  effects still triggers.
- **Dragonize:** Normal-type moves become Dragon-type with 1.2× power.
- **Eelevate:** immune to Ground moves, Spikes, Toxic Spikes and Sticky Web. +1 to its highest stat after KOing with an attack.
- **Mega Sol:** "the Pokémon can use its moves as if the weather were harsh sunlight."
- **Fire Mane:** Fire moves ×1.5.
- **Spicy Spray:** burns the attacker when this Pokémon takes damage from a move.
- **Aura Guard:** halves damage from contact moves.

**Mega Sol details** — (Smogon OP and Smogon p.8, dhelmise and Hydrametr0nice, 2026-04-18, Tier 2):
- The user's Water moves are weakened, and the user ignores the target's sand/snow defensive bonus.
- It does **not** trigger other Pokémon's sun Abilities (Chlorophyll, Solar Power, Dry Skin, Harvest, Forecast, Leaf Guard),
  and Solar Beam doesn't skip its charge when targeting a Mega Sol Pokémon.
- The Mega Sol + Growth bug is fixed: Growth now gives +2 Atk and +2 SpA — (Smogon p.10, Hydrametr0nice, 2026-09-07, Tier 2).

## 4. Terastallization, Dynamax, Z-Moves

- **None of them is in Champions as of 2026-09-28.** Evidence:
  - The official regulation notices' "Mechanics" sections list only Mega Evolution (#751, #776, #816, Tier 1).
  - The official VGC team list has **no Tera Type field**. It covers species, Ability, item, moves, stats and Stat alignment
    (Handbook §2.4.1, Tier 1).
  - Tera Blast, Dynamax Cannon and Hidden Power aren't in Serebii's usable-moves list — (Serebii "Useable Moves",
    https://www.serebii.net/pokemonchampions/moves.shtml, accessed 2026-09-28, Tier 2).
- **Future:** the official site says more special features will be added to the Omni Ring
  (今後、ゼンブイリングの機能に他の特別な要素も追加されるようです) — (Official site バトルについて, Tier 1). No mechanic or date is
  named. Guide-site claims that Tera, Z-Moves or Dynamax are coming are **UNVERIFIED speculation**. One guide site (ChampsDex)
  wrongly says Tera is already in the game.

## 5. Status conditions

| Status | Scarlet/Violet | Champions | Source |
|---|---|---|---|
| Paralysis | 25% full para, Speed halved | **12.5%** full para, Speed halved | Smogon OP (Tier 2); Serebii "Changed Status Conditions", https://www.serebii.net/pokemonchampions/statusconditions.shtml (Tier 2) |
| Sleep | 1–3 turns asleep | Turn 1 asleep; turn 2: 1/3 chance to wake; **turn 3: always wakes** | Smogon OP; Serebii status page (Tier 2) |
| Rest | 2 turns asleep (Game8's "previous effect") | **Unchanged**: "Rest works as it did before" (Smogon p.2, Hydrametr0nice, 2026-04-09, Tier 2). **Conflict:** Game8 says Rest now sleeps 3 turns (Game8 list of changes, https://game8.co/games/Pokemon-Champions/archives/593893, Tier 3). Smogon's research thread is the more trusted source, but UNVERIFIED until tested | Smogon p.2; Game8 |
| Freeze | 20% thaw per turn, no limit | 25% thaw when it tries to move; **thaws on the 3rd turn** at the latest | Smogon OP; Serebii status page |
| Salt Cure | 1/8 per turn (1/4 Water/Steel) | **1/16** (1/8 Water/Steel) | Smogon OP; Serebii "Updated Attacks" (Tier 2) |
| Leech Seed | 1/8 | 1/8 (the in-game text saying 1/16 was wrong and has been fixed) | Official #758, https://news.pokemon-home.com/en/page/758.html, 2026-04-09 (Tier 1) |

No source reports changes to burn or poison damage (as of 2026-09-28).

## 6. Moves

**PP:** "All moves have max PP, and no moves have more than 20 base or max PP. maxPP = 4 * (basePP / 5 + 1) So, 5 -> 8,
10 -> 12, 15 -> 16, 20 -> 20" — (Smogon OP, Tier 2). Examples as of 2026-09-28 — (Serebii "Useable Moves",
https://www.serebii.net/pokemonchampions/moves.shtml, Tier 2):
- **8 PP:** Protect, Detect, Recover, Roost, Slack Off, Moonlight, Synthesis, Morning Sun, Milk Drink, Wish, Strength Sap,
  Encore, Destiny Bond, Trick Room, Sucker Punch, Extreme Speed, Close Combat, Draco Meteor, the OHKO moves.
- **12 PP:** Toxic, Substitute, Leech Seed, Earthquake, Fake Out, Yawn, Belly Drum.
- **16 PP:** Will-O-Wisp, Tailwind, Defog, Sleep Powder, Shell Smash.
- **20 PP:** Stealth Rock, Spikes, Toxic Spikes, Sticky Web, Knock Off, U-turn, Volt Switch, Flip Turn, Thunder Wave, Taunt,
  Rapid Spin, Swords Dance, Calm Mind, Nasty Plot, Dragon Dance.
- [derived] Protect has 8 PP, but the formula on SV's base 10 (Showdown moves.json, SV data,
  https://play.pokemonshowdown.com/data/moves.json, Tier 2) would give 12, so Protect's base PP was cut as well.
  v1.2.0 cut Wish and Strength Sap from 12 to 8 — (Official in-game news #817, https://news.pokemon-home.com/en/page/817.html,
  accessed 2026-09-28, Tier 1).

**Power, accuracy and effect changes** (SV → Champions). Table source: (Serebii "Updated Attacks",
https://www.serebii.net/pokemonchampions/updatedattacks.shtml, accessed 2026-09-28, Tier 2) and (Smogon OP, Tier 2). M-C rows
are also in (Official #817, Tier 1) and (Game8 list of changes, Tier 3).

| Move | Change |
|---|---|
| Apple Acid, Grav Apple, Fire Lash | 80 → 90 BP |
| Beak Blast | 100 → 120 BP |
| Bone Rush | 25 → 30 BP |
| First Impression | 90 → 100 BP (and can't be selected after the first turn out) |
| Infernal Parade | 60 → 65 BP |
| Mountain Gale | 100 → 120 BP |
| Night Daze | 85 → 90 BP |
| Psyshield Bash | 70 → 90 BP |
| Spirit Shackle | 80 → 90 BP |
| Trop Kick | 70 → 85 BP |
| Crabhammer | accuracy 90 → 95 |
| Syrup Bomb | accuracy 85 → 90 |
| Dire Claw | status chance 50% → 30% (also now a slicing move) |
| Iron Head | flinch 30% → 20% |
| Moonblast | SpA drop chance 30% → 10% |
| Freeze-Dry | can no longer freeze |
| Growth | Normal → **Grass** type |
| Snap Trap | Grass → **Steel** type |
| Toxic Thread | Speed −1 → **−2** |
| Make It Rain | accuracy 100 → 95; SpA drop −1 → **−2** |
| Rage Fist | power bonus **resets on switch-out** (Serebii notes it is still capped at 350 BP) |
| Crush Claw, Shadow Claw, Dragon Claw | now slicing moves (Sharpness) |
| Dragon Cheer | now a sound move (Soundproof allies are immune) |
| **M-C:** Slash | usable again; 70 → 80 BP |
| **M-C:** Snipe Shot | 80 → 85 BP |
| **M-C:** Meteor Assault | 150 → 170 BP |
| **M-C:** Double Shock | now a punching move (Iron Fist) |
| **M-C:** Milk Drink | can target an ally, and heals through Protect (Smogon p.10, DaWoblefet, 2026-09-09) |

**Selection and priority rules** — (Smogon OP, Tier 2):
- **Fake Out** and **First Impression** can't be selected or used after the user's first turn out.
- Belch can be selected without having eaten a Berry. Stuff Cheeks can be selected with no Berry held. Spit Up can't be
  selected with no Stockpile. Burn Up can't be selected by a non-Fire user. Last Resort can't be selected until the user's
  other moves have been used.
- **Encore:** a target Encored before it moves that turn uses the **Encored move's priority**, not the priority of the move it
  selected. Since M-C, Ability-based priority (Prankster, Grassy Glide in terrain) also updates after Encore, so a
  Prankster user Encored into an attack gets priority 0 and Dark types aren't immune — (Smogon p.10, Hydrametr0nice,
  2026-09-19, Tier 2).

**Resolution changes:**
- Knock Off still removes the item, Rapid Spin still clears hazards, and Thief still steals, even if the user faints to Rough
  Skin — (Smogon OP, Tier 2). Ceaseless Edge also sets Spikes in that case now — (Smogon p.10, Hydrametr0nice, 2026-09-07, Tier 2).
- Eject Button no longer blocks the switch from U-turn/Volt Switch. All eligible Pokémon switch out — (Smogon p.10, oopsgtg
  2026-09-09 and Hydrametr0nice 2026-09-19, Tier 2).

**Learnsets differ from SV.** Examples verified in Serebii's Champions Pokédex (accessed 2026-09-28, Tier 2):
- **Incineroar** has **no Knock Off and no U-turn** but keeps Fake Out, Parting Shot and Will-O-Wisp
  (https://www.serebii.net/pokedex-champions/incineroar/).
- **Archaludon** has **no Body Press, Mirror Coat or Metal Burst**, and keeps Draco Meteor, Flash Cannon and Electro Shot
  (https://www.serebii.net/pokedex-champions/archaludon/).
- Other Game8-reported changes (Tier 3, unverified individually): Gengar without Encore or Shadow Sneak; Greninja without
  Nasty Plot; Milotic without Calm Mind; Sableye without Parting Shot; Charizard regains Roost; Dragonite and Tyranitar regain
  Superpower; Mega Lopunny gains Close Combat, U-turn, Triple Axel and Mach Punch; Swampert gains Wave Crash; Sceptile gains
  Earth Power — (Game8 list of changes, Tier 3).
- M-C (v1.2.0): Politoed loses Pound. Archaludon loses Mirror Coat and Metal Burst — (Official #817, Tier 1).
- Not usable at all (not in Serebii's usable-moves list): Tera Blast, Hidden Power, Spore, Shore Up, Soft-Boiled, Teleport,
  Victory Dance — (Serebii "Useable Moves", Tier 2).

## 7. Abilities

- **Unseen Fist:** contact moves hit through protection for **¼ damage**, not full damage. Phantom Force still deals normal
  damage — (Smogon OP, Tier 2. Game8 list of changes, Tier 3). Mega Excadrill's Piercing Drill works the same way (§3).
- **Healer:** in-game text indicates a **50%** chance to cure an ally's status (SV: 30%) — (Smogon p.4, Talpr0ne, 2026-04-10,
  Tier 2). UNVERIFIED by testing.
- **Run Away:** now lets the Pokémon **switch out while trapped** (tested vs Shadow Tag), working like Shed Shell — (Smogon p.10,
  DaWoblefet footage, 2026-09-09, Tier 2).
- **Regenerator:** no mechanical change, but the opponent sees the healed HP in the party menu after the switch — (Smogon OP.
  Smogon p.8, Hydrametr0nice, 2026-05-17, Tier 2).
- A Sheer Force–boosted move **no longer prevents Berserk or Pickpocket**, but still prevents Shell Bell — (Smogon OP. Smogon p.7,
  Tier 2).
- Lightning Rod may fail to redirect an Encored Electric move: an acknowledged issue at launch, current status UNVERIFIED —
  (Official #758, Tier 1).
- Mega-only Abilities: §3.

## 8. Items

Pool as of 2026-09-28: **57 held items, 28 Berries, 81 Mega Stones** — (Serebii "Items",
https://www.serebii.net/pokemonchampions/items.shtml, accessed 2026-09-28, Tier 2). All 12 held items added in M-C are sold in
the shop for VP — (Game8 "List of New Items", https://game8.co/games/Pokemon-Champions/archives/605519, updated 2026-09-09, Tier 3).
Serebii lists every held item as "Shop" (700–1,000 VP) or "Beginning".

**Held items in the game (57):** Air Balloon, Big Root, Binding Band, Black Belt, Black Glasses, Bright Powder, Charcoal,
**Choice Scarf**, Damp Rock, Dragon Fang, Eject Button, Electric Seed, Expert Belt, Fairy Feather, Focus Band, **Focus Sash**,
Grassy Seed, Hard Stone, Heat Rock, Icy Rock, Iron Ball, King's Rock, Leek, **Leftovers**, **Life Orb**, Light Ball, Light Clay,
Magnet, Mental Herb, Metal Coat, Metronome, Miracle Seed, Misty Seed, Muscle Band, Mystic Water, Never-Melt Ice, Normal Gem,
Poison Barb, Psychic Seed, Quick Claw, Red Card, **Rocky Helmet**, Scope Lens, Sharp Beak, Shed Shell, Shell Bell, Silk Scarf,
Silver Powder, Smooth Rock, Soft Sand, Spell Tag, Terrain Extender, Twisted Spoon, White Herb, Wide Lens, Wise Glasses, Zoom Lens.

**Berries (28):** the 18 type-resist Berries, plus Aspear, Cheri, Chesto, Pecha, Persim, Rawst, Lum, Leppa, Oran and **Sitrus**.
No pinch Berries (e.g., Salac, Liechi, Figy).

**Not in the game (as of 2026-09-28; absent from Serebii's list):** Choice Band, Choice Specs, Assault Vest, **Heavy-Duty Boots**,
Eviolite, Black Sludge, Flame Orb, Toxic Orb, Weakness Policy, Booster Energy, Covert Cloak, Clear Amulet, Safety Goggles,
Throat Spray, Loaded Dice, Mirror Herb, Power Herb, Ability Shield, Blunder Policy, Eject Pack, Room Service, Utility Umbrella,
Protective Pads, Punching Glove. Game8 separately notes Flame Orb and Toxic Orb are "not yet in the game", which weakens Marvel
Scale and Poison Heal — (Game8 list of changes, Tier 3).

Added per regulation: **M-B (+15):** Muscle Band, Wise Glasses, Expert Belt, Life Orb, Metronome, Big Root, Light Clay, Heat Rock,
Icy Rock, Smooth Rock, Damp Rock, Wide Lens, Zoom Lens, Iron Ball, Shed Shell. **M-C (+12):** Air Balloon, Binding Band, Eject
Button, Electric Seed, Grassy Seed, Leek, Misty Seed, Normal Gem, Psychic Seed, Red Card, Rocky Helmet, Terrain Extender —
(Game8 list of changes and new-items pages, Tier 3). Serebii's list is consistent.

Item behavior notes:
- **Item Clause:** "Duplicate held items are not allowed." — (Official #816, Tier 1).
- Life Orb recoil happens **before** Make It Rain's SpA drop, unlike the usual order — (Smogon p.9, Hydrametr0nice, 2026-06-20, Tier 2).
- Knock Off gets its boost and removes a Mega Stone held by a Pokémon that can't use it — (Smogon p.9, Marty, 2026-06-19, Tier 2).
- Item descriptions: trust the in-game text Serebii shows ("If the holder is damaged by an attack…" for Eject Button) over
  Game8's paraphrases, which wrongly limit Eject Button and Red Card to contact or physical hits.

## 9. Battle engine and other differences

- **Damage formula** "generally seems to be the same as SV". The lowest damage roll went missing briefly after launch and "is
  back as of 2026/04/23" — (Smogon OP, Tier 2).
- **Trick Room Speed overflow** (>1809) is gone — (Smogon OP. Smogon p.3, DaWoblefet stream #3, 2026-04-09, Tier 2).
- **Switch-in order:** v1.0.3 fixed "The changes in speed caused by held items are not reflected in the order in which abilities
  activate" (e.g., Choice Scarf) — (Nintendo Support update history,
  https://www.nintendo.com/en-gb/Support/Purchases-Subscriptions/Games/How-to-Update-Pokemon-Champions-3079895.html, accessed
  2026-09-28, Tier 1). Hazard damage now resolves as a separate step **before** entry Abilities. In Trick Room: Torkoal took
  Stealth Rock, then Typhlosion took Stealth Rock, then Drought, then Frisk — (Smogon p.7, DaWoblefet stream #6, 2026-04-15, Tier 2).
- **Grassy Terrain** end-of-turn healing reportedly goes by slot (P1 left, P1 right, P2 left, P2 right) — (Smogon p.9, Linathan,
  2026-06-28, Tier 2; one report).
- **Idle rule:** no actions for 3 turns from the start of battle loses ("You have been idle for too long!") — (Smogon p.7,
  DaWoblefet stream #6, 2026-04-15, Tier 2).
- **Frisk** reveals both items in Doubles, same as SV — (Smogon p.3, DaWoblefet stream #3, 2026-04-09, Tier 2).

## 10. Timers and time-outs

| Setting | Timers | When the game clock runs out | Source |
|---|---|---|---|
| **Ranked and Casual** (Singles and Doubles) | Total 20 min · Player 7 min · Turn 45 s · Preview 90 s | **Draw.** No VP, no rank change | Timers: Official #816 (Tier 1). Draw: Game8 timers, https://game8.co/games/Pokemon-Champions/archives/596247, updated 2026-04-23 (Tier 3); Automaton, https://automaton-media.com/en/news/pokemon-champions-new-rules-eliminate-timer-stall-wins-but-possible-exploits-raise-concerns/, 2026-04-08 (Tier 3); GamesRadar+, 2026-04-10 (Tier 3) |
| **Online Competitions** (MCS, Global Challenge) | per competition | "result will be determined by the number of remaining Pokémon and their HP" | Official #824 / #825, https://news.pokemon-home.com/en/page/824.html (Tier 1) |
| **Private Battles / official VGC** | Team Preview 90 s · move 45 s · Your Time 7 min · game 20 min | Reported: old rule (more Pokémon, then more HP). **UNVERIFIED.** Official events then apply Bo3 tie tables and sudden death | Handbook §4.3.1, §4.4.2–4.4.4 (Tier 1); Automaton (Tier 3) |

- **"Your Time"** running out ends the battle as a **loss** for that player. The **move timer** running out uses "the move on the
  top of the list" — (Game8 timers, Tier 3).
- SV contrast: in earlier games a time-out was won by the side with more Pokémon, then more HP — (Automaton, Tier 3). In
  Champions ranked, stalling out the clock never wins.

## 11. Information: Team Preview, Open Team List, logs, replays, usage data

- **Ranked Team Preview:** shows all 6 species and forms and **which are Shiny** — (Smogon OP, Tier 2). **Held items at Team
  Preview: UNVERIFIED.** Only one uncited guide claims items and Mega Stones are visible — (ChampDex,
  https://champdex.com/guides/team-preview, Tier 3 low-trust). Showdown's simulation shows no items. Full table:
  `regulations/ranked-singles-m-6.md` §8.
- **Selection Support** (v1.2.0): "displays indicators on the Pokémon selection screen to assist in choosing Pokémon to send
  into battle" — (Official #817, Tier 1). Serebii describes a Summary showing advantage or disadvantage against the opponent's
  team "with data pulled from prior Ranked data" — (Serebii news 2026-09-09,
  https://www.serebii.net/news/2026/09-September-2026.shtml, Tier 2).
- **Open Team List (official VGC):** the opponent sees species/form, Ability, item, all moves and **Stat Alignment**, but not
  stats — [derived] from Handbook §2.4–2.4.1 (Tier 1). Details: `regulations/vgc-reg-m-c.md` §3.
- **View Log** (v1.2.0): "displays a history of all actions taken during the course of the current battle" — (Official #817,
  Tier 1). **No saved-replay feature** is mentioned in any patch note through v1.2.0 or in the official news feed — (Nintendo
  Support update history, Tier 1. news.pokemon-home.com list, checked 2026-09-28, Tier 1). The Trainer still has to
  screen-record.
- **In-game Battle Data:** Battle → Battle Data → Ranked Battles or Online Competitions shows usage rankings for Singles and
  Doubles, and per-Pokémon moves, items, teammates and stats — (Operation Sports,
  https://www.operationsports.com/pokemon-champions-how-to-check-battle-data/, 2026-04-22, Tier 3). This is **official usage
  data** the Trainer can screenshot for the Scout.

## 12. Clauses at a glance

| Rule | Ranked Singles | Ranked Doubles | Official VGC |
|---|---|---|---|
| Bring / pick | 6 / 3 | 6 / 4 | 6 / 4 |
| Level | 50 | 50 | 50 |
| Species Clause (by Dex no.) | Yes | Yes | Yes (Handbook §2.3) |
| Item Clause | Yes | Yes | Yes |
| Mega Evolutions per battle | 1 | 1 | 1 |
| Sleep / OHKO / Evasion clauses | None listed | None listed | None listed |
| Team sheets | Closed | Closed | **Open** |
| Games per match | 1 | 1 | Bo1 or Bo3 Swiss; Bo3 top cut |

Sources: `regulations/ranked-singles-m-6.md` §2, `regulations/ranked-doubles-m-6.md` §2, `regulations/vgc-reg-m-c.md` §2–3
(each line cited there).

---

## 13. Unverified / open questions

1. **Speed on the Mega Evolution turn:** Gen 7 rule (post-Mega Speed) or not? Needs a Private Battle test with footage.
2. **Does a Mega's new Ability activate when it Mega Evolves** (e.g., Mega Scrafty's Intimidate, Mega Froslass's Snow Warning,
   Mega Raichu X's Electric Surge)? Asked on Smogon (p.9, 2026-06-17) and unanswered there.
3. **Are held items or Mega Stones shown at ranked Team Preview?** One uncited claim says yes. Trainer screenshot needed.
4. **Rest sleep duration** (Smogon: unchanged; Game8: 3 turns).
5. **Healer at 50%:** from in-game text, not yet tested.
6. **Private Battle time-out result** (reported: count, then HP) and how official events rule a clock time-out.
7. **Training VP costs** (Serebii and Game8 disagree).
8. **Doubles spread-move modifier:** assumed 0.75× as in SV. No Champions test found.
9. Is **Battle Bond** usable in ranked? (It's banned at official events, Handbook §2.3.)
10. Do **Mega Evolution and switching** share a priority step (a lead seen on a guide site), or do switches still resolve
    before Mega Evolution? No reliable source found.
11. Future gimmicks through the Omni Ring: which ones, and when? The official site only says "other special elements" will be added.
12. The server can change mechanics without a version bump. Re-check the Smogon research thread OP before relying on any line above,
    and note the date.
