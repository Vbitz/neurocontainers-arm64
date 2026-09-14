# lesymap: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.0.9222.post1`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

LESYMAP is an R source package with documented installation of ANTsR dependencies. Its published image is amd64-only, but no fundamental R/ARM limitation follows from that. The matching ANTsR/ITK native build and bundled RStudio are unresolved.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/lesymap/build.yaml).
- Base image expression: `dorianps/lesymap:{{ context.base_image_tag }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/206). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `dorianps/lesymap:20220701`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [dorianps/LESYMAP upstream documentation](https://github.com/dorianps/LESYMAP/blob/master/README.md).
- [dorianps/LESYMAP release v0.0.0.9222](https://github.com/dorianps/LESYMAP/releases/tag/v0.0.0.9222).
- [dorianps/docker upstream documentation](https://github.com/dorianps/docker/blob/master/README.md).
- [Registry manifest inspected](https://registry-1.docker.io/v2/dorianps/lesymap/manifests/20220701).

## Plan and acceptance criteria

Reconstruct the pinned R environment and build ANTsR through its documented procedure, then supply native RStudio if required by deployment. Test lesion-to-symptom maps and statistical results. Record an actual dependency failure before declaring an upstream port necessary.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/lesymap/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/206#issuecomment-5651532962).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
