# gouhfi: ARM64 research plan

Researched: 2026-09-15. Recipe version: `0.0.1.post3`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The recipe declares ARM64, uses the native Miniconda base and has a CPU execution option in its documented interface. The two native attempts reached a completed Docker image but failed during Docker-to-SIF export because the runner had no disk space. This does not establish an application or architecture blocker.

## Pinned recipe and evidence

- [Recipe at accepted source `04970417e995`](https://github.com/Vbitz/neurocontainers/blob/04970417e995232706f4ce85ddf4db23c79d4f25/recipes/gouhfi/build.yaml).
- [GOUHFI upstream](https://github.com/mafortin/GOUHFI).
- First native export failure [run 34691452949](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691452949).
- Permitted unchanged retry [run 34694039302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694039302).

## Blocker and next action

Both attempts report `no space left on device` during `docker save`; neither produced a SIF or ran deploy/fulltest. The unchanged infrastructure retry budget is exhausted. Revisit after runner storage/export infrastructure is repaired, then dispatch the exact ARM64 candidate and require all native build, SIF, deploy and runtime gates. Do not change the recipe or weaken tests to work around storage exhaustion.

## Reopened infrastructure retry — 2026-09-15

Subsequent native ARM64 runs, including neurocommand run
[34928959233](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34928959233),
completed Docker build, SIF conversion and fulltest on the same runner class.
That changed infrastructure evidence justifies one fresh unchanged retry of the
already ARM64-declared recipe at accepted source
`e74050df0e4881833ae5d8d82b4e0ef287a14179`. Investigation starts
`2026-09-15T04:43:14Z` with a `2026-09-15T16:43:14Z` deadline. Require the
complete native build/SIF/deploy/fulltest path; stop immediately if storage
exhaustion recurs or if a real application blocker appears.
