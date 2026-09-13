# diffusiontoolkit: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.6.4.1`. Target: native Linux ARM64.

**Assessment: Binary distribution; no public source-build route found.**

The current archive is x86_64. The upstream product documentation describes the distributed Toolkit in binary form and provides a registration-based download service; no public source-build route for this product was found. A different tractography toolkit is not an acceptable replacement.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/diffusiontoolkit/build.yaml).
- Base image expression: `centos:7`.
- Declared download inputs: `archive`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/138). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Toolkit product documentation](https://trackvis.org/dtk/).
- [Product distribution documentation](https://trackvis.org/docs/?subsect=license).
- [Official download service](https://trackvis.org/download/).

## Plan and acceptance criteria

Revisit when the authors supply an authorized Linux ARM binary or source/build access for this exact Toolkit. Preserve reconstruction and tractography tests; architecture declarations alone cannot make the current executable run natively.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/diffusiontoolkit/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A native upstream artifact or supported source/build route preserving the same application is required. Revisit when that concrete prerequisite changes. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
