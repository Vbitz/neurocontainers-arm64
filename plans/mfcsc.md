# mfcsc: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.1.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

MFCSC source is public MATLAB code, but the current container launches a precompiled binary with MATLAB Runtime 2020a. That runtime lacks a documented Linux ARM distribution; changing the launcher cannot fix the binary architecture.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mfcsc/build.yaml).
- Base image expression: `ubuntu:18.04`.
- Builder templates: `matlabmcr 2020a`.
- Declared download inputs: `mfcsc_binary`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/152). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [civier/mfcsc upstream documentation](https://github.com/civier/mfcsc/blob/main/README.md).
- [civier/mfcsc release 1.1](https://github.com/civier/mfcsc/releases/tag/1.1).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Track the compiled artifact and runtime pair, and revisit upon a supported native execution route. Retain the functional-versus-structural connectivity calculation and expected numerical assertions.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mfcsc/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/152#issuecomment-5651349517).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
