# linda: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.5.1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

LINDA publishes R source and explicitly requires ANTsR. Its pinned image hides that native dependency stack. Image unavailability is a packaging barrier, while same-version ANTsR/ITK and model compatibility are the source-build questions.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/linda/build.yaml).
- Base image expression: `dorianps/linda:latest@{{ context.base_image_digest }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/245). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `dorianps/linda:latest@sha256:abe94d551bf6f7f2937f04a2bb5a1b3b7cd25a0f6e2cf684602ea9fa397c78a3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [dorianps/LINDA upstream documentation](https://github.com/dorianps/LINDA/blob/master/README.md).
- [dorianps/LINDA release 0.5.1](https://github.com/dorianps/LINDA/releases/tag/0.5.1).
- [Registry manifest inspected](https://registry-1.docker.io/v2/dorianps/linda/manifests/sha256:abe94d551bf6f7f2937f04a2bb5a1b3b7cd25a0f6e2cf684602ea9fa397c78a3).

## Plan and acceptance criteria

Build the pinned R package and ANTsR dependencies natively with the original model data. Test lesion segmentation and registered outputs. Reuse a valid ANTsR result if available; do not infer ANTsR failure merely from the separate antspyx build.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/linda/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/245#issuecomment-5651544904).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
