# brainager: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.1.0.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The brainageR model is R source, but upstream uses SPM12/MATLAB for segmentation and normalization. This recipe supplies compiled SPM/MCR Intel binaries. ARM R and kernlab alone cannot reproduce its preprocessing stage.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/brainager/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `matlabmcr 2017b`.
- Declared download inputs: `spm12_r7219_Linux_R2017b_zip`, `brainager_neurodesk_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/123). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [james-cole/brainageR upstream documentation](https://github.com/james-cole/brainageR/blob/master/README.md).
- [james-cole/brainageR release 2.1](https://github.com/james-cole/brainageR/releases/tag/2.1).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Record the SPM/MCR dependency separately from the R model. Revisit complete support when that runtime has a native route. Validate tissue segmentation, PCA projection and predicted age together; do not substitute a different segmentation algorithm.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/brainager/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
