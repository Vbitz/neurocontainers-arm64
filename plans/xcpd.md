# xcpd: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.10.7`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

The recipe inherits an amd64 image and manually installs an amd64 libpng12 package into an x86 library directory. XCP-D source and its dependency build are public; libpng's binary packaging alone is not a fundamental limitation. The full native postprocessing toolchain must be reconstructed.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/xcpd/build.yaml).
- Base image expression: `pennlinc/xcp_d:{{ context.version }}`.
- Declared download inputs: `libpng12_deb`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/172). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `pennlinc/xcp_d:0.10.7`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [PennLINC/xcp_d upstream documentation](https://github.com/PennLINC/xcp_d/blob/main/README.rst).
- [PennLINC/xcp_d Dockerfile](https://github.com/PennLINC/xcp_d/blob/main/Dockerfile).
- [PennLINC/xcp_d pyproject.toml](https://github.com/PennLINC/xcp_d/blob/main/pyproject.toml).
- [PennLINC/xcp_d release 26.2.0](https://github.com/PennLINC/xcp_d/releases/tag/26.2.0).
- [Registry manifest inspected](https://registry-1.docker.io/v2/pennlinc/xcp_d/manifests/0.10.7).

## Plan and acceptance criteria

Inspect the 0.10.7 image's actual need for libpng12 and rebuild the same dependent tool/library natively or use an upstream-supported release fix. Resolve Workbench/AFNI and Python dependencies, then validate denoising, connectivity and reports.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/xcpd/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/172#issuecomment-5651353388).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
