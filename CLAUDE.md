# GameSim: Pokémon Champions Coaching Team

This repo runs a three-agent coaching team for one player (the "Trainer"). The master prompt is
`prompts/champions-coaching-team.md`; read it before doing coaching work.

- Agents: `.claude/agents/scout.md`, `coach.md`, `lab.md`.
- Shared state: `knowledge/` (sources, rules, mechanics, meta briefs, Film Room, players, events), `trainer/` (profile,
  games, drills, film study), `lab/` (hypotheses, playbook).
- The Trainer's current mode and goals are in `trainer/profile.md`. Check it first.
- Cite sources as described in `knowledge/sources.md`. Keep video files out of git.
- To sample frames from a Trainer's game recording: `python3 tools/extract_frames.py <recording>` (frames land in the
  git-ignored `frames/` folder).
- To find and read Showdown replays for the Singles supplement: `python3 tools/showdown_replays.py search|fetch|board …`
  (downloads land in the git-ignored `replays/` folder).
