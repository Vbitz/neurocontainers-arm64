# eeglab: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2020.0.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The recipe's compiled 2020a standalone depends on MATLAB Runtime for Intel Linux. Upstream also documents source operation in Octave, but only command-line support there. That is a real alternative to investigate, not proof that the existing GUI standalone can be preserved.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/eeglab/build.yaml).
- Base image expression: `ubuntu:18.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `eeglab2020_0_mcr2020a_tar_gz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/144). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [sccn/eeglab upstream documentation](https://github.com/sccn/eeglab/blob/develop/README.md).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Record the missing runtime for the current GUI package. Evaluate Octave only against the complete deployed feature/test contract; if it loses the GUI or required plugins it is a separate reduced variant. Validate EEG processing and ICA output before any equivalence claim.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/eeglab/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/144#issuecomment-5651347930).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
