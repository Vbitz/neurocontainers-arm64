# afni: ARM64 research plan

Researched: 2026-09-13. Recipe version: `26.0.07`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

No fundamental ARM64 blocker established. The recipe chooses an x86 Linux tarball, but AFNI publishes source and a documented local build. Its precompiled R library bundle is a separate architecture-specific input.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/afni/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `freesurfer 7.4.1`.
- Declared download inputs: `update_afni_binaries`, `linux_ubuntu_24_R_4_3_libs_tgz`, `afni_binary`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/118). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [afni/afni upstream documentation](https://github.com/afni/afni/blob/master/README.rst).
- [afni/afni CMakeLists.txt](https://github.com/afni/afni/blob/master/CMakeLists.txt).
- [AFNI source-build documentation](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/download_links.html).

## Plan and acceptance criteria

Build the pinned AFNI source with its supported build tooling and ARM system libraries; rebuild the R packages rather than reuse the binary bundle. Validate AFNI and SUMA, a small image calculation, and an R-based analysis.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/afni/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
