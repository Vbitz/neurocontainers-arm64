# qsiprep: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

QSIPrep provides source and its image build, but reconstructing the exact diffusion-preprocessing stack requires native FSL/ANTs/FreeSurfer and Python dependencies. Newer upstream releases have different environments and CUDA requirements; those are not proof about pinned 1.0.1.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/qsiprep/build.yaml).
- Base image expression: `pennlinc/qsiprep:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/113). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `pennlinc/qsiprep:1.0.1`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pennlinc/qsiprep upstream documentation](https://github.com/PennLINC/qsiprep/blob/main/README.rst).
- [pennlinc/qsiprep Dockerfile](https://github.com/PennLINC/qsiprep/blob/main/Dockerfile).
- [pennlinc/qsiprep pyproject.toml](https://github.com/PennLINC/qsiprep/blob/main/pyproject.toml).
- [pennlinc/qsiprep release 26.0.0](https://github.com/PennLINC/qsiprep/releases/tag/26.0.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/pennlinc/qsiprep/manifests/1.0.1).

## Plan and acceptance criteria

Inspect the 1.0.1 staged Dockerfile and lock, inventory required executables and supported CPU modes, then resolve prerequisites. Validate a small DWI BIDS workflow and corrected data/reports without omitting essential preprocessing stages.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/qsiprep/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
