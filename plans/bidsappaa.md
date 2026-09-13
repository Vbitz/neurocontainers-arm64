# bidsappaa: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.2.0.post2`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The upstream app is unmaintained and its source Dockerfile assembles a MATLAB-based Automatic Analysis environment with FreeSurfer and FSL. Source availability for AA does not provide the proprietary Linux ARM MATLAB runtime needed by its compiled entry point.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsappaa/build.yaml).
- Base image expression: `bids/aa:{{ context.image_tag }}`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/127). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Registry inspection was inconclusive ('config'); no new platform-availability claim is derived from that request.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [bids-apps/aa upstream documentation](https://github.com/bids-apps/aa/blob/master/README.md).
- [bids-apps/aa Dockerfile](https://github.com/bids-apps/aa/blob/master/Dockerfile).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Retain the blocker for the compiled AA deployment until a matching native runtime/application is available. Record the exact AA/MCR pairing and dependencies. Switching to reproa, the suggested successor, would be a different application and must not be presented as this port.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsappaa/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
