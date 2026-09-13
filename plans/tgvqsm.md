# tgvqsm: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recipe actually builds the supplied Python/Cython TGVQSM source, but installs an Intel Miniconda2 runtime and very old SciPy 0.17.1/nibabel 2.1.0. CMake has ARM options; the harder issue is the legacy Python 2 scientific environment. A newer Julia implementation is a different implementation and is not a drop-in port.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/tgvqsm/build.yaml).
- Base image expression: `ubuntu:16.04`.
- Declared download inputs: `cmake`, `dcm2niix_source`, `source`, `bet2`, `miniconda`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/169). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Original TGV QSM project and source](https://www.neuroimaging.at/pages/qsm.php).
- [Pinned recipe source archive](https://www.neuroimaging.at/media/qsm/TGVQSM-plus.zip).

## Plan and acceptance criteria

Inspect the original source and documented Python support, resolve a native same-version runtime if feasible, and build its Cython extension without algorithm changes. Validate susceptibility maps with original numerical checks. Stop if this requires maintaining a private legacy numerical-library port.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/tgvqsm/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
