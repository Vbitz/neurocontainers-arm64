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
