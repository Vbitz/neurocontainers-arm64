# aslprep: ARM64 research plan

Researched: 2026-09-13. Recipe version: `26.0.3`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The recipe wraps a published image. ASLPrep source and its Dockerfile are public, so an amd64-only image is a packaging barrier. Full functionality depends on a matched neuroimaging environment; rebuilding only the Python frontend would not supply registration, segmentation and perfusion tools.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/aslprep/build.yaml).
- Base image expression: `pennlinc/aslprep:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/100). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `pennlinc/aslprep:26.0.3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pennlinc/aslprep upstream documentation](https://github.com/PennLINC/aslprep/blob/main/README.rst).
- [pennlinc/aslprep Dockerfile](https://github.com/PennLINC/aslprep/blob/main/Dockerfile).
- [pennlinc/aslprep pyproject.toml](https://github.com/PennLINC/aslprep/blob/main/pyproject.toml).
- [pennlinc/aslprep release 26.0.3](https://github.com/PennLINC/aslprep/releases/tag/26.0.3).
- [Registry manifest inspected](https://registry-1.docker.io/v2/pennlinc/aslprep/manifests/26.0.3).

## Plan and acceptance criteria

Use the pinned release Dockerfile and dependency lock to enumerate native dependencies; resolve each for ARM64 before recreating the image. Validate a small ASL BIDS workflow and its CBF outputs, not merely the CLI.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/aslprep/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/100#issuecomment-5651280215).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
