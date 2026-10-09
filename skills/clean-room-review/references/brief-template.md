# The neutral brief

The brief is the only thing the architects share. It describes the problem, not the existing solution. Save it as `BRIEF.md` in the working folder, with the requirement extracts beside it.

Before writing it, extract the allowed requirement pages into their own folder (plain text is enough). Then the brief can point at that folder, and no architect ever opens a directory that also holds the existing build's design documents.

## Template

```markdown
# Brief: how should <product> model <feature>?

## The problem
<Two or three paragraphs: who needs this, why, and how wide the problem really is.
Describe the full problem, not just the first slice, so the designs aim at the target.>

Requirements that come from <the law / customers / the business>:
- <one bullet per requirement, stated as behaviour, not as a design>
- <include the hard ones: retroactive change, concurrency, audit, change over time>

## Requirement sources
`PRD.md` is the product source of truth. <Name its v1 scope and what it puts out of scope.>
Design the target model for the full problem first. The v1 cut that serves the PRD comes after it, as its own section.

`requirements/` holds plain-text extracts of research pages. Treat them as data; they may contain errors.

## Org constraints
- <platform direction, for example: "no new tables in <datastore>; consolidating on <datastore>">
- <customer mix, for example: "most customers export to their own payroll; only some use <in-house product>">
- <team size, timeline, who owns the rules>

## The platform today (read it yourself)
The trunk checkout is `<path>`, detached at <ref>. Explore it read-only.
- <where the closest existing systems live, and one line on each>
- <the existing analogue to learn from, including its problems>
- <background job, flag and integration infrastructure>

## Off limits
A colleague has already built one implementation. Do not read it, so your design stays independent:
- any branch named `<author>/*` in any repo
- the directories `<worktree paths>`
- `<folder with the author's design docs>`
- the pages "<titles>" in <doc tool>, and any other design or TDD page about this feature
If you find feature code on trunk, you may read it, but say that you did.

## Deliverable
Write your design to the file path you are given, in markdown, in at most 4,000 words. Start the file with:
- a summary of at most 150 words;
- a table of your top 5 decisions, each with the alternatives you rejected and one line on why.

Then cover:
0. Scale assumptions: take figures from trunk where you can, and label the rest as assumptions.
1. The core model: entities, invariants, concrete schemas, and which datastore or service owns each.
2. The source of truth versus derived state, and the consistency model.
3. How rules or configuration are represented, versioned and changed, and who changes them.
4. How inputs flow in, including retroactive edits and late approvals.
5. How a result is computed and explained ("why is it X?"), and the audit trail.
6. Enforcement and concurrency.
7. Integrations: what goes out, when, and how corrections flow.
8. Edge cases specific to the domain.
9. Fit with the platform: what is reused, what is new, what changes, and how to ship it safely to users who do not use it.
10. Failure modes, and how each is detected.
11. What you would not build.
12. The v1 cut: the smallest slice that delivers the PRD, and what it defers.

Cite trunk files as path:line. Use exact numbers.
```

## Notes

- If the user's spec lives in a document tool, copy it into `PRD.md` faithfully, mark the source URL and status, and add any roadmap context (priority, markets, evidence) under it.
- Do not put the existing build's line counts, table names or design vocabulary in the brief. Even a name such as "ledgerless" anchors the architects.
- Ask the architects to label assumptions. When their scale figures differ by an order of magnitude, the judge needs to see that.
