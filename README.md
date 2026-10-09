# clean-room-review

A Claude Code skill for reviewing a large existing implementation at the architecture level instead of line by line. It suits a stack of branches, a spike or a rewrite.

It runs in three phases. Each can be run on its own.

1. **Map.** Parallel research agents write an architecture overview of the existing build. The orchestrator checks every claim the overview rests on before writing it down.
2. **Redesign.** Four architects design from the spec alone, each pushed into a different lens: record-keeping, generic engine, platform fit and delegate. None of them can see the existing build. A judge that has not seen it either scores the designs, verifies their claims against trunk, and picks one target.
3. **Delta.** The existing build is compared with the target area by area. Each area gets a verdict (Keep, Rework, Throwaway or Missing), and the added lines are counted per area.

If a constraint comes up after the judge has ruled, it is recorded as a named amendment, and the ruling is left as it was.

## Install

As a plugin:

```
/plugin marketplace add DamonFstr/clean-room-review
/plugin install clean-room-review@clean-room-review
```

If the repo is private, you need read access. Claude Code clones it with your existing git credentials, for example through `gh auth login`.

To install only the skill, copy `skills/clean-room-review/` to `~/.claude/skills/clean-room-review/`.

## Use

Ask Claude to review a large stack or spike, to produce an architecture overview of someone's branches, or to design the feature properly and then compare it with what was built.

Phase 2 launches five agents that each read code for a while, so expect it to cost a good number of tokens.

## Layout

```
skills/clean-room-review/
  SKILL.md                    workflow
  references/overview.md      phase 1 agent split and document structure
  references/brief-template.md
  references/lenses.md
  references/prompts.md       architect, judge and adversarial prompts
  references/delta.md
  scripts/diff_by_area.py     lines added per area, split into source and tests
```
