# tractseg: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.9.post2`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

The recipe pins torch 1.6.0+cpu, whose inspected release lacks an ARM wheel, and also includes FSL/MRtrix. Current upstream TractSeg is source available and documents broader Python support, so the old environment pin is not proof of an intrinsic model limitation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/tractseg/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Builder templates: `mrtrix3 3.0.4`, `miniconda py37_23.1.0-1`, `fsl 6.0.7.16`.
- Declared download inputs: `pretrained_weights_tract_segmentation_xtract_v1.npz`, `pretrained_weights_tract_segmentation_v3.npz`, `pretrained_weights_endings_segmentation_v4.npz`, `pretrained_weights_dm_regression_xtract_v1.npz`, `pretrained_weights_dm_regression_v2.npz`, `pretrained_weights_peak_regression_part1_v2.npz`, `pretrained_weights_peak_regression_part2_v2.npz`, `pretrained_weights_peak_regression_part3_v2.npz`, `pretrained_weights_peak_regression_part4_v2.npz`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/238). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `torch-1.6.0`: 0 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MIC-DKFZ/TractSeg upstream documentation](https://github.com/MIC-DKFZ/TractSeg/blob/master/Readme.md).
- [MIC-DKFZ/TractSeg setup.py](https://github.com/MIC-DKFZ/TractSeg/blob/master/setup.py).
- [torch-1.6.0 published package metadata](https://pypi.org/pypi/torch/1.6.0/json).

## Plan and acceptance criteria

Check the exact TractSeg 2.9 requirements and model compatibility for a documented newer torch CPU version. Resolve native FSL/MRtrix and preserve bundle segmentation/tracking outputs. A framework change requires scientific comparison, not just a successful import.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/tractseg/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation attempt — 2026-09-13

The first implementation candidate is pushed as [`a6bd2f46399657df8b56cfc12ce48f147796d1fc`](https://github.com/Vbitz/neurocontainers/commit/a6bd2f46399657df8b56cfc12ce48f147796d1fc) on [`arm64/tractseg-modern-arm`](https://github.com/Vbitz/neurocontainers/tree/arm64/tractseg-modern-arm), based on accepted submodule pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`. It keeps the existing x86_64 binary and Python 3.7/torch 1.6 route. The ARM64 path uses the pinned MRtrix3 3.0.4 source template and Miniconda py311 with the native `torch==2.4.1` wheel. This is an ordinary upstream source build and does not change the scientific toolchain.

Recipe validation and ARM64/x86_64 Dockerfile generation passed locally. Native verification is pending; the candidate must pass the existing MRtrix, FSL, TractSeg, Tractometry and deployment fulltest assertions before acceptance. Investigation window: `2026-09-13T19:06:28Z` through `2026-09-14T07:06:28Z`, attempt 1/6. Issue checkpoint: [#238 comment](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5655429034).
