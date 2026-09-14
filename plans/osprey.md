# osprey: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.9.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

Osprey source is public and requires MATLAB/toolboxes for full functionality. The recipe uses compiled Ubuntu distributions with MATLAB Runtime. Linux ARM cannot use the available Intel standalone/runtime pair; macOS ARM support is a different OS target.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/osprey/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `matlabmcr 2023a`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/176). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [schorschinho/osprey upstream documentation](https://github.com/schorschinho/osprey/blob/develop/README.md).
- [schorschinho/osprey release v.2.9.0](https://github.com/schorschinho/osprey/releases/tag/v.2.9.0).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Track the Osprey/MCR pair and required SPM functionality. Revisit a supported native standalone route, then validate spectral fitting, voxel registration and GUI/CLI outputs using the same basis sets.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/osprey/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/176#issuecomment-5651354128).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
