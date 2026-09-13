# bidsapphcppipelines: ARM64 research plan

Researched: 2026-09-13. Recipe version: `4.3.0`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The upstream Dockerfile pins Intel FreeSurfer and MATLAB Runtime; its README lists MCR among the pipeline dependencies. Workbench and FSL also need ARM builds. Public shell scripts do not remove the compiled runtime requirement of the packaged pipeline.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsapphcppipelines/build.yaml).
- Base image expression: `bids/hcppipelines:{{ context.base_image_tag }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/184). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `bids/hcppipelines:v4.3.0-3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/HCPPipelines upstream documentation](https://github.com/bids-apps/HCPPipelines/blob/master/README.md).
- [bids-apps/HCPPipelines Dockerfile](https://github.com/bids-apps/HCPPipelines/blob/master/Dockerfile).
- [bids-apps/HCPPipelines release v4.3.0-3](https://github.com/bids-apps/HCPPipelines/releases/tag/v4.3.0-3).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/bids/hcppipelines/manifests/v4.3.0-3).

## Plan and acceptance criteria

Map the required HCP stages to MCR executables and exact FreeSurfer/FSL versions. Revisit full support when those prerequisites exist natively; do not silently omit MATLAB-dependent stages to produce a green container.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsapphcppipelines/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
