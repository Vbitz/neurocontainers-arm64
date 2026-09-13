# pals: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.0.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

PALS publishes native Python installation instructions and requires ANTs and FSL. Both have source, and FSL now publishes ARM package metadata. The full same-version dependency path remains untested; there is no demonstrated intrinsic PALS ARM limitation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/pals/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `ants 2.4.3`.
- Declared download inputs: `miniconda.sh`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/226). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [npnl/PALS upstream documentation](https://github.com/npnl/PALS/blob/main/README.md).
- [npnl/PALS requirements.txt](https://github.com/npnl/PALS/blob/main/requirements.txt).
- [npnl/PALS release v1.1.0](https://github.com/npnl/PALS/releases/tag/v1.1.0).

## Plan and acceptance criteria

Resolve the actual ANTs/FSL commands and versions in this recipe, build or install native equivalents of those same tools, then validate lesion analysis and registered outputs with the existing fixture.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/pals/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Implementation candidate — 2026-09-14

Candidate [`5fa9705a7ff388e51330bbbfa00e1298b37abf23`](https://github.com/Vbitz/neurocontainers/commit/5fa9705a7ff388e51330bbbfa00e1298b37abf23) is based on accepted pin `88e6776aeb27f16ef43e015acb426b7e87fe0d1c` and is pushed on [`arm64/pals-miniconda-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/pals-miniconda-arm). It declares ARM64 and selects the official pinned Python 3.10 Miniconda installer for each architecture, preserving the existing x86_64 checksum and installation path. The ARM64 installer URL was confirmed reachable and its SHA256 is pinned. Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. The fulltest now performs a real MNI-space lesion overlap against the bundled atlas and asserts a positive output volume and ROI overlap.

This is a native candidate, not a verification claim. Dispatch only when a runner slot opens; acceptance requires the ARM64 build, SIF conversion, deploy checks and the complete PALS runtime suite.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

The exact native run [34782446828](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782446828) built the ARM64 image and SIF and passed the source revision and FSL launcher checks. The new lesion-overlap fulltest initially failed because its configured output directory did not exist; PALS then raised `NameError: name 'add_to_log' is not defined` while reporting that missing path.

Candidate [`ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`](https://github.com/Vbitz/neurocontainers/commit/ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006) creates the output directory in the test fixture before invoking PALS. Recipe code and x86_64 behavior are unchanged. Local validation and both architecture generations pass. The corrected exact retry is [run 34782946174](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782946174), attempt 2/6.
