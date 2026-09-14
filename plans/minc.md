# minc: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.9.18`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

MINC has a public CMake source build with documented dependencies. The recipe installs an Ubuntu x86_64 toolkit bundle. The full toolkit's ITK/NetCDF/HDF5 and auxiliary modules must be matched; source availability makes a blanket binary-only claim incorrect.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/minc/build.yaml).
- Base image expression: `ubuntu:18.04`.
- Declared download inputs: `archive`, `volgenmodel`, `beast`, `mni_09a`, `mni_09c`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/154). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BIC-MNI/minc-toolkit upstream documentation](https://github.com/BIC-MNI/minc-toolkit/blob/master/README.md).
- [BIC-MNI/minc-toolkit CMakeLists.txt](https://github.com/BIC-MNI/minc-toolkit/blob/master/CMakeLists.txt).
- [BIC-MNI/minc-toolkit release release-1.0.09](https://github.com/BIC-MNI/minc-toolkit/releases/tag/release-1.0.09).
- [CAIsr/volgenmodel-nipype upstream documentation](https://github.com/CAIsr/volgenmodel-nipype/blob/master/README.md).

## Plan and acceptance criteria

Identify the source tag/superbuild corresponding to toolkit 1.9.18 and retain all deployed modules. Build natively and test image conversion, resampling and model-building utilities. Avoid substituting a minimal subset that would lose toolkit functionality.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/minc/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/154#issuecomment-5651349902).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
