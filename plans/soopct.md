# soopct: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.0`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The pipeline publishes Python source, but registration needs antspyx and some normalization paths require SynthSR. Screened antspyx releases provide source but no ARM wheel. Upstream explicitly identifies the additional SynthSR dependency, so conversion-only success would not verify the full workflow.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/soopct/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda py313_25.5.1-0`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/232). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `antspyx-0.5.4`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `antspyx-0.6.1`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [rordenlab/soop-ct upstream documentation](https://github.com/rordenlab/soop-ct/blob/main/README.md).
- [rordenlab/soop-ct requirements.txt](https://github.com/rordenlab/soop-ct/blob/main/requirements.txt).
- [antspyx-0.5.4 published package metadata](https://pypi.org/pypi/antspyx/0.5.4/json).
- [antspyx-0.6.1 published package metadata](https://pypi.org/pypi/antspyx/0.6.1/json).

## Plan and acceptance criteria

Resolve the exact ANTsPy source build and native SynthSR environment without changing implementations. Test DICOM-to-BIDS conversion plus registration/normalization outputs; use existing BrainLesion evidence to avoid repeating a known unmodified failing build.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/soopct/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
