# jamovi: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.7.4`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Jamovi source is public. The current recipe consumes an amd64 container; the application comprises a GUI/server and an R analysis environment with compiled modules. Recreating that full environment is required, not simply changing the base manifest.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/jamovi/build.yaml).
- Base image expression: `jamovi/jamovi:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/203). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `jamovi/jamovi:2.7.4`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [jamovi/jamovi upstream documentation](https://github.com/jamovi/jamovi/blob/main/README.md).
- [jamovi/jamovi pyproject.toml](https://github.com/jamovi/jamovi/blob/main/pyproject.toml).
- [jamovi/jamovi release v2.7.30](https://github.com/jamovi/jamovi/releases/tag/v2.7.30).
- [Registry manifest inspected](https://registry-1.docker.io/v2/jamovi/jamovi/manifests/2.7.4).

## Plan and acceptance criteria

Use the 2.7.4 source/build instructions and pin the R/module versions. Verify every bundled module on ARM and test a small statistical analysis through the application with expected numerical results.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/jamovi/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/203#issuecomment-5651532363).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
