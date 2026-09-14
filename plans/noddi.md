# noddi: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The public repository contains a compiled ss_noddi MATLAB application and launcher. The recipe invokes it through MATLAB Runtime. Source availability for NODDI algorithms does not supply a Linux ARM runtime for this deployed standalone binary.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/noddi/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `noddi_source`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/160). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [CyclotronResearchCentre/NODDI_singularity upstream documentation](https://github.com/CyclotronResearchCentre/NODDI_singularity/blob/main/README.md).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Record the exact application/MCR pairing. Revisit an upstream native build or a documented equivalent execution route, retaining fitted parameter maps and model behavior. Substituting another NODDI implementation would not port this recipe.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/noddi/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/160#issuecomment-5651351090).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
