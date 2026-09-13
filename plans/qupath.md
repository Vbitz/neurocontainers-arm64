# qupath: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.7.0`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

QuPath documents building from source. Its 0.7.0 Linux package is not an ARM-specific asset, but the Java application is not binary-only. JavaFX, OpenSlide/OpenCV/native image readers, and bundled Cellpose extensions all need matching ARM support.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/qupath/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `qupath_archive`, `cellpose_extension_archive`, `cellpose_cyto3_model`, `cellpose_cyto3_size_model`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/229). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `v0.7.0` lists: `QuPath-v0.7.0-Linux.tar.xz`, `QuPath-v0.7.0-Mac-arm64.pkg`. This release metadata establishes asset availability, not a passed native test.

Release `v0.12.1` lists: . This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [qupath/qupath upstream documentation](https://github.com/qupath/qupath/blob/main/README.md).
- [qupath/qupath build.gradle.kts](https://github.com/qupath/qupath/blob/main/build.gradle.kts).
- [qupath/qupath release v0.7.0](https://github.com/qupath/qupath/releases/tag/v0.7.0).
- [BIOP/qupath-extension-cellpose upstream documentation](https://github.com/BIOP/qupath-extension-cellpose/blob/main/README.md).
- [BIOP/qupath-extension-cellpose build.gradle.kts](https://github.com/BIOP/qupath-extension-cellpose/blob/main/build.gradle.kts).
- [BIOP/qupath-extension-cellpose release v0.12.1](https://github.com/BIOP/qupath-extension-cellpose/releases/tag/v0.12.1).

## Plan and acceptance criteria

Build the same release with a native JDK and Gradle, inspect platform classifiers for all native libraries, then preserve the included extension environment. Validate whole-slide loading, image analysis and a small Cellpose operation plus GUI launch.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/qupath/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation candidate — 2026-09-14

Candidate [`386964db1c454c002ebd562d06bd1cdcbedcdb99`](https://github.com/Vbitz/neurocontainers/commit/386964db1c454c002ebd562d06bd1cdcbedcdb99)
is pushed on [`arm64/qupath-source-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/qupath-source-arm), based on accepted pin `8bcc3e3d`. It declares ARM64 and builds QuPath v0.7.0 from the upstream Gradle source project with `jpackage`, retaining the released x86_64 archive path. It also installs Cellpose with the official ARM64 CPU PyTorch 2.6.0 wheel while preserving the x86_64 CUDA route and the existing extension/model tests. Local validation and both architecture generations pass.

The candidate is queued behind four active native jobs. Acceptance requires the exact native ARM64 build, SIF conversion, deploy checks, QuPath CLI behavior and the Cellpose extension test suite. A build failure will identify whether one of the upstream native classifiers is still missing for ARM64.
