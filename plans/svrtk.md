# svrtk: ARM64 research plan

Researched: 2026-09-13. Recipe version: `20260626`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

SVRTK documents source compilation on Linux and is based on MIRTK. The recipe consumes an amd-tagged automated-processing image, so the full assembly of reconstruction, segmentation models and helper tools needs rebuilding. Lack of a published ARM image is not an intrinsic MIRTK/SVRTK blocker.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/svrtk/build.yaml).
- Base image expression: `fetalsvrtk/svrtk:general_auto_amd@{{ context.base_image_digest }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/233). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `fetalsvrtk/svrtk:general_auto_amd@sha256:d0ee22d6476277d172276ca33ee2a3f6334e1bf773c789d6012c8c23804460de`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [SVRTK/SVRTK upstream documentation](https://github.com/SVRTK/SVRTK/blob/master/README.md).
- [SVRTK/SVRTK CMakeLists.txt](https://github.com/SVRTK/SVRTK/blob/master/CMakeLists.txt).
- [SVRTK/auto-proc-svrtk upstream documentation](https://github.com/SVRTK/auto-proc-svrtk/blob/main/README.md).
- [Registry manifest inspected](https://registry-1.docker.io/v2/fetalsvrtk/svrtk/manifests/sha256:d0ee22d6476277d172276ca33ee2a3f6334e1bf773c789d6012c8c23804460de).

## Plan and acceptance criteria

Pin the source revisions matching the image, build MIRTK/SVRTK and recreate the automation environment. Validate slice-to-volume reconstruction and automatic preprocessing; retain stated memory/CPU needs and identify a specific unavailable dependency if encountered.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/svrtk/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/233#issuecomment-5651538002).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
