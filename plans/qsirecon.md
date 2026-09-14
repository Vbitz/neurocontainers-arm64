# qsirecon: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

QSIRecon source is public. Its amd64 image bundles multiple reconstruction backends; their native package availability must be assessed individually. A pure-Python wrapper installation cannot verify the full reconstruction suite, but no fundamental wrapper ARM limitation is established.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/qsirecon/build.yaml).
- Base image expression: `pennlinc/qsirecon:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/114). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `pennlinc/qsirecon:1.1.0`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pennlinc/qsirecon upstream documentation](https://github.com/PennLINC/qsirecon/blob/main/README.rst).
- [pennlinc/qsirecon Dockerfile](https://github.com/PennLINC/qsirecon/blob/main/Dockerfile).
- [pennlinc/qsirecon pyproject.toml](https://github.com/PennLINC/qsirecon/blob/main/pyproject.toml).
- [pennlinc/qsirecon release 26.0.0](https://github.com/PennLINC/qsirecon/releases/tag/26.0.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/pennlinc/qsirecon/manifests/1.1.0).

## Plan and acceptance criteria

Map each promised reconstruction workflow in 1.1.0 to exact executables and model data. Build the supported dependencies natively and validate representative reconstruction/connectome outputs; record a per-backend blocker if source/configuration is unavailable.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/qsirecon/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/114#issuecomment-5651282939).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
