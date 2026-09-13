# fieldtrip: ARM64 research plan

Researched: 2026-09-13. Recipe version: `20220617.post1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

FieldTrip is source-available MATLAB code, but this container runs a compiled 2020b package. The Linux MATLAB Runtime target is glnxa64. Public scripts and recompilable MEX helpers do not supply the missing proprietary ARM runtime.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fieldtrip/build.yaml).
- Base image expression: `ubuntu:18.04`.
- Builder templates: `matlabmcr {{ context.matlab_version }}`.
- Declared download inputs: `fieldtrip_1`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/145). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [fieldtrip/fieldtrip upstream documentation](https://github.com/fieldtrip/fieldtrip/blob/master/README.md).
- [fieldtrip/fieldtrip release 20251218](https://github.com/fieldtrip/fieldtrip/releases/tag/20251218).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Track the exact standalone/MCR pair. Any alternative interpreter requires explicit upstream support and full functional equivalence; otherwise revisit on a native Linux ARM standalone release. Preserve signal-processing and source-analysis tests.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fieldtrip/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
