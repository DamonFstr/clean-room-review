# Phase 3: the delta

The delta answers the question the reviewer actually has: which parts of this build survive the target, which change, which go, and what is missing.

## Count by area

Group the existing build's paths into the areas the target talks about, then count the added lines with the script:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/diff_by_area.py \
  --repo <worktree> --base <merge-base> --head HEAD \
  --area "domain rules=/domain/" \
  --area "rule data=registry/|/config\.py$" \
  --area "jobs and infra=close_job|\.tf$|scripts/" \
  --area "schema=versions/|models/"
```

`${CLAUDE_SKILL_DIR}` resolves to this skill's folder, whether it was installed as a plugin or copied to `~/.claude/skills`. The first matching area wins. Anything unmatched lands in `other`, and the output totals must equal the diff total. Run the script once per repo, then quote the source lines (not tests) in the document. The test lines follow their area and are worth one sentence, so the default test pattern (any path containing `test` or `spec`) is deliberately loose. Save the exact `--area` patterns you ran in the working folder, so the numbers can be reproduced.

## Verdicts

Use one closed set, as a dropdown column if the document tool supports one:

| Verdict | Meaning |
|---|---|
| Keep | Carries into the target as is, or with renames only |
| Rework | The idea or data survives, but the mechanics change |
| Throwaway | The target has no equivalent, or builds it differently enough that none of the code carries |
| Missing | The target or the spec needs it, and the build has nothing |

## The table

One row per area, with these columns: area (and its source lines), what the existing build does, what the target does, and the verdict. Below the table, add one sentence on how the tests split.

The lead paragraph gives the arithmetic: how many source lines carry over, how many need rework, how many are throwaway, and how many fall in other. Those buckets must add up to the total.

## Finding what is missing

For each item in the PRD's scope and each failure-detection mechanism in the target, search the build for it, for example: `git grep -n -i "<term>"` and `git diff --name-only <base> HEAD | grep -i <area>`. Report an item as missing only after the search comes back empty. Say "not in the stack" unless you also searched the author's plan.

## Tone

The delta is about a colleague's work, and they will probably read it. Describe what the code does. Give credit where the target and the build converged independently, because that is evidence the build was on the right track. Leave motives out.
