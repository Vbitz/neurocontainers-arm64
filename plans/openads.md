# openads: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.0.0`. Target: native Linux ARM64.

**Assessment: GPU capability or supported CPU-mode prerequisite.**

This recipe is specifically the GPU image. OpenADS also documents a CPU/source mode, represented separately by openadscpu. Its pinned GPU image lacks native ARM packaging and full GPU execution cannot be verified on the CPU runner; antspyx is an additional dependency build issue.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/openads/build.yaml).
- Base image expression: `docker.io/sljhlab/openads:gpu@{{ context.base_image_digest }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/241). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Package `antspyx-0.5.4`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Package `antspyx-0.6.1`: 0 Linux ARM wheel filenames, 1 source archives, 0 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

Fresh registry inspection of `docker.io/sljhlab/openads:gpu@sha256:bd3508a0278538bbf10b7b0a090085b7b584860cef7f3c1fed6183707fc6223d`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [farialab/OpenADS upstream documentation](https://github.com/farialab/OpenADS/blob/main/README.md).
- [farialab/OpenADS setup.py](https://github.com/farialab/OpenADS/blob/main/setup.py).
- [antspyx-0.5.4 published package metadata](https://pypi.org/pypi/antspyx/0.5.4/json).
- [antspyx-0.6.1 published package metadata](https://pypi.org/pypi/antspyx/0.6.1/json).
- [Registry manifest inspected](https://registry-1.docker.io/v2/sljhlab/openads/manifests/sha256:bd3508a0278538bbf10b7b0a090085b7b584860cef7f3c1fed6183707fc6223d).

## Plan and acceptance criteria

Retain GPU scope and require native ARM GPU infrastructure plus matching CUDA/torch/antspyx. Use the separate CPU recipe for CPU investigation. Validate the stroke-analysis workflow and generated reports when the required hardware is available.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/openads/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The existing GPU capability needs compatible native hardware and dependencies, or a demonstrably upstream-supported CPU mode preserving the intended scope. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Conditional**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/241#issuecomment-5651543991).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
