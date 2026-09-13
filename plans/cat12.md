# cat12: ARM64 research plan

Researched: 2026-09-13. Recipe version: `26.0.rc3.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

CAT source and Apple Silicon standalone assets exist, but the Linux standalone build uses MATLAB Runtime glnxa64. Mac ARM binaries cannot satisfy a Linux ARM container. The required runtime is the fundamental blocker for this recipe.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/cat12/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`, `miniconda latest`.
- Declared download inputs: `cat12.zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/129). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `26.0.rc4` lists: `cat-standalone-Linux.zip`, `cat-standalone-Mac_arm64.zip`. This release metadata establishes asset availability, not a passed native test.

Release `v0.1.0` lists: . This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [ChristianGaser/cat12 upstream documentation](https://github.com/ChristianGaser/cat12/blob/main/README.md).
- [ChristianGaser/cat12 release 26.0.rc4](https://github.com/ChristianGaser/cat12/releases/tag/26.0.rc4).
- [m-wierzba/cat-container upstream documentation](https://github.com/m-wierzba/cat-container/blob/master/README.md).
- [m-wierzba/cat-container release v0.1.0](https://github.com/m-wierzba/cat-container/releases/tag/v0.1.0).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Track the exact CAT/MCR pair and wait for a Linux ARM standalone route. Rebuilding isolated CAT helpers is insufficient; eventual validation must include segmentation and surface morphometry with the existing assertions.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/cat12/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
