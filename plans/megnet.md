# megnet: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.1.post1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The pinned environment chooses x86 PyQt5/PyQt5-sip wheels. PyQt5 5.15.11 has native linux-aarch64 Conda packages, so a missing PyPI wheel is not a fundamental Qt blocker. The MEG pipeline source is public; the remaining package set needs resolution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/megnet/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda py310_25.5.1-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/210). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [miao-cao/MEGNET_pipeline upstream documentation](https://github.com/miao-cao/MEGNET_pipeline/blob/main/README.md).
- [Conda-forge native Qt package metadata](https://api.anaconda.org/package/conda-forge/pyqt).

## Plan and acceptance criteria

Replace only architecture-specific wheel acquisition with a compatible native Qt binding and rebuild the same environment. Check shared-library discovery and MNE integration, then validate an electrophysiology operation and the deployed GUI behavior.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/megnet/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `1ce18a5642515bbb314ea48def4ac022c91264e8` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **6/6** fulltests in [run 34756122909](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756122909). The ARM route selects native conda-forge Qt bindings and preserves the existing MEGNET dependency/test contract and x86_64 path.
