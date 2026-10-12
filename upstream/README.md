# Upstream ARM64 retesting

The 2026-10-12 assignment covers the exact **129 recipe/variants** that had fully
passing native ARM64 evidence at the historical accepted source
`e74050df0e4881833ae5d8d82b4e0ef287a14179`.

The user subsequently excluded ARM64 work for all OpenRecon recipes. Upstream's
`uses_openrecon` classification identifies **17 exclusions**, leaving **112
containers in the active goal**, each requiring its own upstream PR. The frozen
129-entry inventory is retained for auditability; exclusions are recorded as
`excluded-by-user` and do not count as verified or merged.

[queue.json](queue.json) freezes that inventory and records each container's
historical source/run/counts, current upstream review, candidate branch/SHA,
investigation deadline, attempts, native run, upstream PR, CI result and merge.
Historical success does not count as a retest of current upstream.

The fork's `main` was fast-forwarded to upstream
`6720f24a5d1b9137e5e7082e3c12bd521656fed7`. Existing accepted port branches and the
top-level accepted gitlink are preserved while focused candidates are tested.
There are 80 recipes with fork changes and 49 without fork recipe changes.
Of those 49, upstream removed ARM64 declarations from five OpenRecon recipes;
those five are excluded by the user's scope correction. The other 44 still
declare ARM64.
All 129 current recipe paths exist. Of the 80 port patches, 45 apply directly,
21 more merge automatically against current upstream, and 14 require manual
reconciliation. These counts describe preparation, not verified builds.

Each in-scope container progresses through recipe review, local validation, native ARM64
Docker/SIF/deploy/fulltest verification, its own upstream PR,
upstream candidate tests for every declared variant, and merge. Review recipes
without fork changes for individually justified fixes or test improvements;
do not manufacture empty PRs or mark their upstream testing complete without
evidence. The user explicitly requires one PR per container; never combine
containers in a PR.

Upstream classifies fulltest-only PRs as source-only and does not build image
candidates for them. Those PRs need separate upstream container verification of
their actual candidate before merge. A successful Code quality check alone does
not satisfy runtime verification.

The user explicitly authorized upstream PRs and merges for this assignment.
Fork Actions remains disabled. The upstream `Container release gate` and
`Code quality` checks must pass, and actual container reports must have positive
test counts, zero failures and zero skips before merging. Do not invoke release
promotion or edit generated release metadata.

Keep at most four builds active, accounting for the upstream PR matrix as well
as local repository Actions. Never dispatch concurrent duplicates. Resume from
the recorded run/PR before starting another attempt. Per-recipe budgets remain
six total container build attempts and twelve hours, including the root ARM64
build and both architecture jobs in each upstream matrix. Upstream retries and
integration attempts also consume that budget; separate architecture counters
do not enlarge it.

Durable investigation notes belong in each linked `arm64-container` issue's
comments. `PLAN.md` records checkpoints. Coverage issue #2 continues to report
its own accepted architecture inventory and latest build evidence; its historic
129 total is separate from completion of this upstream submission queue.

Local checkout protection: upstream instruction files differ from the historical
checkout. They were read from git without changing any on-disk `AGENTS.md`.
The submodule index marks both instruction paths skip-worktree; preserve those
protections. Do not stage the working candidate gitlink as an accepted update.
