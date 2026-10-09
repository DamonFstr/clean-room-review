# Prompt templates

Replace the angle-bracket fields. Paths are absolute.

## Architect

```
You are one of four architects designing, independently, how <product> should model <feature>.
Read <dir>/BRIEF.md fully first, then PRD.md beside it, then use requirements/ and the trunk
checkout as the brief describes. Obey the brief's "Off limits" section strictly.

YOUR LENS: <name>. <Two to four sentences: the push, what to borrow, what to optimise for.>

The other three architects take these lenses: <one phrase each>. Commit to your lens. Do not hedge
toward the middle. Where your lens leads somewhere costly or uncomfortable, say so and defend it, or
name the point where you would stop.

Read-only: do not edit any repo, commit, run migrations, start services or run tests. Write
exactly one file: <dir>/design-<lens>.md, in the format the brief specifies. Your final message:
the file path and a 5-line summary.
```

## Judge

```
You are the judge for an architecture exercise. Four architects designed, independently and
through deliberately different lenses, how <product> should model <feature>. Pick the target design.

Read in full: <dir>/BRIEF.md (obey its "Off limits" section yourself), <dir>/PRD.md, and
<dir>/design-*.md.

Verify the claims the decision turns on, read-only, in the trunk checkout <path>. Name the ones
you can already see: <list the load-bearing platform claims, with path:line>. Where a design
leans on a claim that is false, mark the design down. Do not edit anything.

Deliver <dir>/target.md, at most 3,500 words, with:
1. A scoring matrix: each design scored 1 to 5 on these criteria, with a one-line reason per cell:
   <6 to 8 criteria fitted to the problem; always include fit with the platform today, cost to
   build v1, operational risk, and reach beyond the first use case>.
2. Where the designs agree.
3. Where they disagree, and your ruling on each.
4. The recommended target. Synthesis is allowed, taking the best decision per axis, but it must
   be coherent, not a committee average. Cover the entities and where each lives, the source of
   truth versus derived state, the rules, the computation and its explanation, enforcement and
   concurrency, integrations, and failure detection.
5. The v1 cut and the order of the later phases.
6. Rejected alternatives, each with one line on why.
7. The claims you verified or refuted, with path:line.
8. Open decisions for product, <domain owner> and engineering.

Use exact numbers. Your final message: the file path and a 10-line summary.
```

Do not give the judge the existing build, the Phase 1 overview, or your own opinion of either.

## Adversarial check of an amendment

Use this when an amendment changes mechanics that no independent agent has reviewed.

```
Try to break this design change. Read <dir>/target.md, then <dir>/AMENDMENT-<topic>.md. The
amendment changes <what>. Using the trunk checkout <path>, read-only, find every way the amended
mechanics can fail: partial commits, lock ordering, retries, flag flips, paths that bypass the
hook, and load on shared paths. For each failure, give the trigger, the effect, how it would be
detected, and the cheapest fix. Cite path:line. Under 1,500 words.
```
