# trackvis: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.6.1`. Target: native Linux ARM64.

**Assessment: Binary distribution; no public source-build route found.**

The recipe's archive is explicitly x86_64. Upstream distributes TrackVis in binary form behind a registration-based download service; no public native source-build route was found in its product documentation. Its published file format is not source for the application.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/trackvis/build.yaml).
- Base image expression: `centos:7`.
- Declared download inputs: `TrackVis_v`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/171). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Product distribution documentation](https://trackvis.org/docs/?subsect=license).
- [Official download service](https://trackvis.org/download/).

## Plan and acceptance criteria

Revisit when the authors provide an authorized Linux ARM executable or source/build access. Preserve the visualization and tract-analysis features and test real tract data; do not substitute another viewer or emulate x86.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/trackvis/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A native upstream artifact or supported source/build route preserving the same application is required. Revisit when that concrete prerequisite changes. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
