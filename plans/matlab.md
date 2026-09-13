# matlab: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2025b`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The recipe requires proprietary MATLAB R2025b, glnxa64 mpm and additional products. The vendor Linux processor requirements specify Intel/AMD x86-64. Available Apple ARM support does not provide a Linux ARM MATLAB distribution.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/matlab/build.yaml).
- Base image expression: `mathworks/matlab:R{{ context.version }}`.
- Declared download inputs: `mpm`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/208). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `mathworks/matlab:R2025b`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [mathworks-ref-arch/matlab-dockerfile upstream documentation](https://github.com/mathworks-ref-arch/matlab-dockerfile/blob/main/README.md).
- [mathworks-ref-arch/matlab-dockerfile Dockerfile](https://github.com/mathworks-ref-arch/matlab-dockerfile/blob/main/Dockerfile).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/mathworks/matlab/manifests/R2025b).

## Plan and acceptance criteria

Revisit only when MathWorks supplies an appropriate native Linux ARM release and the required products/licensing are available. Validate actual MATLAB/toolbox computations; changing to Octave or a remote service would not port this container.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/matlab/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
