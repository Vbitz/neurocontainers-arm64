# voreen: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.3.0`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

Voreen source and Linux build instructions exist. The recorded native attempts failed in the bundled Boost finder requesting obsolete math_c99l/math_tr1l components. That is a concrete build-system/dependency compatibility failure, not evidence that volume rendering inherently requires x86.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/voreen/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `voreen_src`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/117). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34739991537); use the issue for exact candidate SHA and failure context.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Upstream Linux build guide](https://www.uni-muenster.de/Voreen/documentation/linux.html).

## Plan and acceptance criteria

Preserve the failed-run record and require an applicable released upstream Boost/CMake compatibility fix or documented configuration before retrying. Validate rendering and required modules on ARM; do not patch third-party internals or remove tested features to obtain a build.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/voreen/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Keep the recorded failure as the current blocker for that candidate. A released upstream fix or documented configuration addressing its first error is the condition for a justified retry. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/117#issuecomment-5651386281).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
