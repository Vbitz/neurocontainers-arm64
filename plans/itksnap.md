# itksnap: ARM64 research plan

Researched: 2026-09-13. Recipe version: `4.4.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

ITK-SNAP publishes source and explicitly links build instructions. The recipe's prebuilt Linux executable is a packaging choice. Its ITK/VTK/Qt build and rendering dependencies require validation, but no fundamental ARM compiler failure is recorded.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/itksnap/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `downloaded_tar_file`, `MRI_crop_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/148). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pyushkevich/itksnap upstream documentation](https://github.com/pyushkevich/itksnap/blob/master/README.md).
- [pyushkevich/itksnap CMakeLists.txt](https://github.com/pyushkevich/itksnap/blob/master/CMakeLists.txt).
- [pyushkevich/itksnap release v4.4.0-beta2](https://github.com/pyushkevich/itksnap/releases/tag/v4.4.0-beta2).

## Plan and acceptance criteria

Use release-matched CMake/superbuild instructions and native ITK/VTK/Qt libraries, preserving all segmentation modules. Test volume loading, segmentation editing or scripted processing, and output image geometry on ARM.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/itksnap/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
