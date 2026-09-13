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

Candidate [`f36e931661901018af12f9d5bc945d9aa660be76`](https://github.com/Vbitz/neurocontainers/commit/f36e931661901018af12f9d5bc945d9aa660be76) is based on accepted pin `88e6776aeb27f16ef43e015acb426b7e87fe0d1c` and is pushed on [`arm64/pals-miniconda-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/pals-miniconda-arm). It declares ARM64 and selects the official pinned Python 3.10 Miniconda installer for each architecture, preserving the existing x86_64 checksum and installation path. The ARM64 installer URL was confirmed reachable and its SHA256 is pinned. Recipe validation and ARM64/x86_64 Dockerfile generation passed locally.

This is a native candidate, not a verification claim. Dispatch only when a runner slot opens; acceptance requires the ARM64 build, SIF conversion, deploy checks and the complete PALS runtime suite.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
