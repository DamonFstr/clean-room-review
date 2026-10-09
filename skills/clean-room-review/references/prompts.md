# Prompt templates

The plugin's agents carry the fixed parts of each role: the ground rules, the output format and the stance. A prompt only supplies what changes per run. Replace the angle-bracket fields, and use absolute paths.

## Researcher (`clean-room-review:researcher`, Phase 1)

```
Map <area> of the existing build for an architecture overview.
Worktree: <path>, detached at <sha>. Diff range: `git merge-base HEAD <trunk>`..HEAD.
Commits in scope, bottom to top: <list>.
Answer:
1. <question specific to this area>
2. <...>
Report in prose and tables, under <1,000 to 1,200> words.
```

For the author's design docs, add the folder path, which pages to prioritise, and where helper scripts may be written.

## Architect (`clean-room-review:architect`, Phase 2)

```
Brief: <dir>/BRIEF.md. Write your design to <dir>/design-<lens>.md.

YOUR LENS: <name>. <Two to four sentences: the push, what to borrow, what to optimise for.>

The other architects take these lenses: <one phrase each>.
```

Launch all four in one message, so they run in parallel.

## Judge (`clean-room-review:judge`, Phase 2)

```
Brief: <dir>/BRIEF.md and <dir>/PRD.md. Designs: <dir>/design-*.md.
Trunk checkout: <path>. Write your ruling to <dir>/target.md.

Score on these criteria: <6 to 8 fitted to the problem; always include fit with the platform today,
cost to build v1, operational risk, and reach beyond the first use case>.

Claims to verify that I can already see: <load-bearing platform claims, with path:line>.
Open-decision owners: product, <domain owner>, engineering.
```

Do not give the judge the existing build, the Phase 1 overview, or your own opinion of either.

## Adversarial check of an amendment (`general-purpose`)

```
Try to break this design change. Read <dir>/target.md, then <dir>/AMENDMENT-<topic>.md. The
amendment changes <what>. Using the trunk checkout <path>, read-only, find every way the amended
mechanics can fail: partial commits, lock ordering, retries, flag flips, paths that bypass the
hook, and load on shared paths. For each failure, give the trigger, the effect, how it would be
detected, and the cheapest fix. Cite path:line. Under 1,500 words.
```
