# clinicadl: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.6.1`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

ClinicaDL source is available with PyTorch-based inference/training. The recipe adds Clinica and native imaging tools; the older pinned Python environment may add package constraints. No fundamental ARM prohibition in the model framework has been demonstrated.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/clinicadl/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `miniconda py310_25.5.1-0`, `fsl 6.0.7.16`, `spm12 r7771`, `freesurfer 7.4.1`, `ants 2.4.3`, `mrtrix3 3.0.4`, `dcm2niix latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/190). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [aramis-lab/clinicadl upstream documentation](https://github.com/aramis-lab/clinicadl/blob/dev/README.md).
- [aramis-lab/clinicadl environment.yml](https://github.com/aramis-lab/clinicadl/blob/dev/environment.yml).
- [aramis-lab/clinicadl pyproject.toml](https://github.com/aramis-lab/clinicadl/blob/dev/pyproject.toml).
- [aramis-lab/clinicadl release v2.0.0](https://github.com/aramis-lab/clinicadl/releases/tag/v2.0.0).

## Plan and acceptance criteria

Resolve the pinned ClinicaDL Python/torch environment on ARM and separately establish preprocessing dependencies. Compare predictions from the same weights and validate the included Clinica workflows before claiming complete support.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/clinicadl/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/190#issuecomment-5651529525).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
