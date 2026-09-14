# ospreybids: ARM64 research plan

Researched: 2026-09-13. Recipe version: `4.2.1`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The BIDS wrapper has Python source but delegates MRS analysis to Osprey's MATLAB-based implementation. The pinned container is amd64-only; rebuilding just its Python layer does not supply native compiled Osprey and its runtime.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/ospreybids/build.yaml).
- Base image expression: `dcanumn/osprey-bids:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/111). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `dcanumn/osprey-bids:v4.2.1`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [DCAN-Labs/OSPREY_BIDS upstream documentation](https://github.com/DCAN-Labs/OSPREY_BIDS/blob/main/README.md).
- [DCAN-Labs/OSPREY_BIDS Dockerfile](https://github.com/DCAN-Labs/OSPREY_BIDS/blob/main/Dockerfile).
- [DCAN-Labs/OSPREY_BIDS pyproject.toml](https://github.com/DCAN-Labs/OSPREY_BIDS/blob/main/pyproject.toml).
- [DCAN-Labs/OSPREY_BIDS release v4.2.1-testing](https://github.com/DCAN-Labs/OSPREY_BIDS/releases/tag/v4.2.1-testing).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/dcanumn/osprey-bids/manifests/v4.2.1).

## Plan and acceptance criteria

Inspect the exact v4.2.1 Dockerfile's Osprey/MCR payload and ANTsPy dependencies. Retain the runtime prerequisite for complete processing; validate BIDS MRS fitting and localizer registration when a native route exists.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/ospreybids/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/111#issuecomment-5651282363).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
