# romeo: ARM64 research plan

Researched: 2026-09-13. Recipe version: `3.2.8`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

ROMEO.jl publishes source and a documented Julia execution path. The recipe downloads a precompiled application bundle, which needs a native equivalent. Julia ARM support makes a source/JIT route plausible; compiled app version 3.2.8 must be mapped to its actual Julia package version.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/romeo/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `romeo_linux_3_2_8_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/164). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [korbinian90/ROMEO.jl upstream documentation](https://github.com/korbinian90/ROMEO.jl/blob/master/README.md).
- [korbinian90/ROMEO.jl Project.toml](https://github.com/korbinian90/ROMEO.jl/blob/master/Project.toml).
- [korbinian90/ROMEO.jl release v1.6.0](https://github.com/korbinian90/ROMEO.jl/releases/tag/v1.6.0).
- [korbinian90/ROMEO upstream documentation](https://github.com/korbinian90/ROMEO/blob/master/README.md).
- [korbinian90/ROMEO release newReleases](https://github.com/korbinian90/ROMEO/releases/tag/newReleases).

## Plan and acceptance criteria

Recover the release project/manifest and use the same algorithm and CLI through the supported Julia source or app build. Validate phase unwrapping and coil combination, preserving output conventions and numerical checks.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/romeo/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **✅**, fulltest **❌**; plan assessment: **Plausible**.
- Investigation outcome: **failed-runtime**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5653761465).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
