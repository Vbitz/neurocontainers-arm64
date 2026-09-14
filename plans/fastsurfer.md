# fastsurfer: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.5.4`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

Upstream provides CPU operation and even a macOS ARM installer, but that is not a Linux ARM container. Its surface reconstruction still calls FreeSurfer binaries and requires a FreeSurfer license. The Python network and complete surface pipeline have different portability requirements.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/fastsurfer/build.yaml).
- Base image expression: `deepmi/fastsurfer:cpu-v{{ context.version }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/196). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Fresh registry inspection of `deepmi/fastsurfer:cpu-v2.5.4`: `linux/amd64`. This describes the published image only; source rebuild feasibility is assessed separately.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Deep-MI/FastSurfer upstream documentation](https://github.com/Deep-MI/FastSurfer/blob/dev/README.md).
- [Deep-MI/FastSurfer pyproject.toml](https://github.com/Deep-MI/FastSurfer/blob/dev/pyproject.toml).
- [Deep-MI/FastSurfer requirements.txt](https://github.com/Deep-MI/FastSurfer/blob/dev/requirements.txt).
- [Deep-MI/FastSurfer release v2.5.4](https://github.com/Deep-MI/FastSurfer/releases/tag/v2.5.4).
- [Registry manifest inspected](https://registry-1.docker.io/v2/deepmi/fastsurfer/manifests/cpu-v2.5.4).

## Plan and acceptance criteria

Rebuild the release's CPU environment and supply compatible ARM FreeSurfer commands. Preserve segmentation, surfaces and the recipe's deployment contract; verify label maps and cortical outputs with the same model files.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/fastsurfer/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/196#issuecomment-5651530860).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.

## Implementation disposition — 2026-09-14

A follow-up audit of the official FreeSurfer downloads found ARM64 artifacts for
macOS but only x86_64/amd64 Linux artifacts; no Linux ARM64 FreeSurfer payload is
listed in the [official development index](https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/dev_20260102/)
or [release download documentation](https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads).
Because the full FastSurfer recipe requires FreeSurfer commands for its surface
pipeline, rebuilding only its Python components would not preserve the tested
functionality. The exact blocker is recorded in
[issue #196](https://github.com/Vbitz/neurocontainers-arm64/issues/196#issuecomment-5660576119).
Revisit when a supported Linux ARM64 FreeSurfer payload or complete FastSurfer
surface route is released.
