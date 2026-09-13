# micapipe: ARM64 research plan

Researched: 2026-09-13. Recipe version: `v0.2.3`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The public Dockerfile includes glnxa64 MCR plus FSL, FreeSurfer and C3D. Upstream says FIX can use MATLAB Runtime, MATLAB or Octave, so the existing MCR packaging is blocked but alternative upstream-supported configurations deserve evaluation.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/micapipe/build.yaml).
- Base image expression: `micalab/micapipe:{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/108). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `micalab/micapipe:v0.2.3`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [MICA-MNI/micapipe upstream documentation](https://github.com/MICA-MNI/micapipe/blob/master/readme.md).
- [MICA-MNI/micapipe Dockerfile](https://github.com/MICA-MNI/micapipe/blob/master/Dockerfile).
- [MICA-MNI/micapipe release v0.2.3](https://github.com/MICA-MNI/micapipe/releases/tag/v0.2.3).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).
- [Registry manifest inspected](https://registry-1.docker.io/v2/micalab/micapipe/manifests/v0.2.3).

## Plan and acceptance criteria

Map every MCR invocation, not only FIX, before considering Octave. Resolve the native imaging stack and validate all promised processing modules. If any required compiled MATLAB application remains, retain the vendor-runtime blocker for full support.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/micapipe/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
