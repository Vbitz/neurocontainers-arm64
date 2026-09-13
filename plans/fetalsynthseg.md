# fetalsynthseg: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

FetalSynthSeg publishes Python source and a pinned PyTorch 2.1.2 environment. PyPI has ARM wheels for that torch version. The current image is the immediate packaging barrier; no fundamental ARM failure has been demonstrated.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fetalsynthseg/build.yaml).
- Base image expression: `vzalevskyi/fetalsynthseg:latest@{{ context.base_image_digest }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/199). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `torch-2.1.2`: 4 Linux ARM wheel filenames, 0 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Fresh registry inspection of `vzalevskyi/fetalsynthseg:latest@sha256:380b4ce81cb13f67ce8a09391e557f964eb6b1befbdbb405dd8e08dc474c620f`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Medical-Image-Analysis-Laboratory/FetalSynthSeg upstream documentation](https://github.com/Medical-Image-Analysis-Laboratory/FetalSynthSeg/blob/main/README.md).
- [Medical-Image-Analysis-Laboratory/FetalSynthSeg requirements.txt](https://github.com/Medical-Image-Analysis-Laboratory/FetalSynthSeg/blob/main/requirements.txt).
- [torch-2.1.2 published package metadata](https://pypi.org/pypi/torch/2.1.2/json).
- [Registry manifest inspected](https://registry-1.docker.io/v2/vzalevskyi/fetalsynthseg/manifests/sha256:380b4ce81cb13f67ce8a09391e557f964eb6b1befbdbb405dd8e08dc474c620f).

## Plan and acceptance criteria

Recreate the pinned requirements on a native Python base and check device selection for supported CPU inference. Preserve preprocessing, model weights and outputs. Test a small fetal MRI segmentation; record a GPU prerequisite only if the actual code requires it.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fetalsynthseg/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
