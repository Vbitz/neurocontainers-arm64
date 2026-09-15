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

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/169#issuecomment-5651352825).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Prerequisite refresh — 2026-09-15

The exact pinned Miniconda2 installer URL still returns HTTP 404 for
`Miniconda2-4.6.14-Linux-aarch64.sh`. CMake 3.31.12 does publish a native
Linux AArch64 archive, so CMake is no longer the blocker; the pinned Python 2
runtime remains unavailable. No supported ARM64 Python 2 replacement is
available in this recipe, and changing the runtime to Python 3 would be a
scientific environment change rather than a recipe-level architecture fix.

The prerequisite blocker remains: revisit when TGVQSM documents a supported
ARM64 Python/runtime dependency set or publishes a native package. No native
dispatch is justified for the current pinned recipe.
