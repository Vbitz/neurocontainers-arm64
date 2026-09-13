# spm12bi: ARM64 research plan

Researched: 2026-09-13. Recipe version: `latest`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The BI standalone archive is compiled SPM12 for Linux R2019b and runs through MATLAB Runtime. Source availability for ordinary SPM12 does not establish that the exact BI distribution can be rebuilt or run on Linux ARM.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/spm12bi/build.yaml).
- Base image expression: `ubuntu:16.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`, `miniconda py310_25.5.1-0`.
- Declared download inputs: `standalone`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/174). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [spm/spm12 upstream documentation](https://github.com/spm/spm12/blob/main/README.md).
- [spm/spm12 release r7771](https://github.com/spm/spm12/releases/tag/r7771).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Identify the BI source revision and runtime pairing, then require a supported native standalone route. Preserve the BI-specific functionality and tests; do not replace it with standard SPM12 merely because that source is easier to obtain.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/spm12bi/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
