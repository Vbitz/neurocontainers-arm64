# startrack: ARM64 research plan

Researched: 2026-09-13. Recipe version: `20250920`. Target: native Linux ARM64.

**Assessment: Required vendor runtime/standalone execution path unavailable.**

The pinned ST_Linux_x86 archive and launcher explicitly require MATLAB Runtime glnxa64. The official download page confirms Linux x86 and MATLAB Runtime 2023b; its Apple ARM build is for macOS. A Python successor is announced as in preparation, not a released replacement for this recipe.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/startrack/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Builder templates: `matlabmcr {{ context.matlab_runtime_version }}`.
- Declared download inputs: `startrack_linux_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/179). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [Official application downloads and runtime requirements](https://nbl-research.github.io/startrack.html).
- [MathWorks Linux system requirements](https://www.mathworks.com/support/requirements/matlab-linux.html).
- [MathWorks Runtime platform/release downloads](https://www.mathworks.com/products/compiler/matlab-runtime.html).

## Plan and acceptance criteria

Obtain authoritative source/build information without bypassing access controls, and require a native Linux ARM runtime/application pair. Preserve StarTrack's tractography behavior; a different tractography implementation is not an acceptable port.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/startrack/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

The missing compatible runtime/standalone path blocks the current full deployment. Revisit on upstream native support or a documented execution route that preserves the complete feature contract. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Blocked prerequisite**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/179#issuecomment-5651354657).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
