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
