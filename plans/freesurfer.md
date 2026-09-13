# freesurfer: ARM64 research plan

Researched: 2026-09-13. Recipe version: `8.2.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

FreeSurfer publishes substantial C/C++ source, so it is not binary-only. This particular full recipe additionally installs MATLAB runtimes and an explicitly linux_x86_64 segmentNuclei payload. The complete packaged capability set therefore has a vendor-runtime/binary obstacle beyond compiling the open-source core.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/freesurfer/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `matlabmcr 2014a`, `matlabmcr 2019b`.
- Declared download inputs: `segmentNuclei_1`, `freesurfer_deb`, `workbench_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/200). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [freesurfer/freesurfer upstream documentation](https://github.com/freesurfer/freesurfer/blob/dev/README.md).
- [freesurfer/freesurfer CMakeLists.txt](https://github.com/freesurfer/freesurfer/blob/dev/CMakeLists.txt).
- [freesurfer/freesurfer Dockerfile](https://github.com/freesurfer/freesurfer/blob/dev/Dockerfile).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Separate source-buildable commands from MCR and packaged executable requirements. Use the release-matched BuildGuide for core investigation, but retain a blocker for full support until every required standalone component has a native route. Preserve all segmentation, surface and specialized tests.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/freesurfer/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
