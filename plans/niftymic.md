# niftymic: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.9`. Target: native Linux ARM64.

**Assessment: Native dependency or legacy environment needs a supported build route.**

NiftyMIC documents native installation requiring ITK_NiftyMIC and SimpleReg dependencies. That specialized ITK environment is the substantive work behind the amd64 image. Public source exists; no specific ARM failure is demonstrated by the prior manifest assessment.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/niftymic/build.yaml).
- Base image expression: `renbem/niftymic:v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/110). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `renbem/niftymic:v0.9`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [gift-surg/NiftyMIC upstream documentation](https://github.com/gift-surg/NiftyMIC/blob/master/README.md).
- [gift-surg/NiftyMIC requirements.txt](https://github.com/gift-surg/NiftyMIC/blob/master/requirements.txt).
- [gift-surg/NiftyMIC setup.py](https://github.com/gift-surg/NiftyMIC/blob/master/setup.py).
- [gift-surg/NiftyMIC release v0.6](https://github.com/gift-surg/NiftyMIC/releases/tag/v0.6).
- [Registry manifest inspected](https://registry-1.docker.io/v2/renbem/niftymic/manifests/v0.9).

## Plan and acceptance criteria

Follow the release-matched native install instructions, resolve ITK_NiftyMIC and registration dependencies, and validate slice-to-volume reconstruction with preserved masks and geometry. Stop only at a concrete unsupported native dependency.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/niftymic/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/110#issuecomment-5651282200).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Implementation disposition — 2026-09-14

- A fresh source-route audit found no supported ARM64 candidate for the pinned NiftyMIC 0.9 stack. The upstream installation instructions require NSoL, SimpleReg, PySiTK and ITK_NiftyMIC and document development/testing against Python 2.7, 3.5 and 3.6 on Ubuntu 16.04/18.04.
- The required repositories are legacy dependency components with no maintained ARM64 build or package route. Their current upstream metadata reports last pushes of 2022-02-15 for NiftyMIC, 2021-01-31 for NSoL, 2019-12-07 for ITK_NiftyMIC, 2019-08-11 for PySiTK and 2019-07-26 for SimpleReg. The pinned Docker image remains linux/amd64-only.
- Outcome: **blocked-prerequisite**. No ARM64 build was dispatched because replacing the image requires porting the complete legacy ITK_NiftyMIC/WrapITK and registration stack. Revisit only when the upstream stack publishes a maintained ARM64 build, multi-architecture image or documented current Python/ITK source route.
- Durable evidence is recorded in [issue #110](https://github.com/Vbitz/neurocontainers-arm64/issues/110#issuecomment-5661388675). The recipe remains unverified.
