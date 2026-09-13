# modsort: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.0.2`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The exact upstream v0.0.2 release includes modsort-Linux-arm64-0.0.2.AppImage. The current recipe selects the x86_64 AppImage, so the earlier unavailable-asset blocker is contradicted by direct release evidence.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/modsort/build.yaml).
- Base image expression: `ubuntu:24.04`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/155). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `v0.0.2` lists: `modsort-Linux-arm64-0.0.2.AppImage`, `modsort-Linux-x86_64-0.0.2.AppImage`, `modsort-Mac-arm64-0.0.2-Installer.dmg`, `modsort-Windows-arm64-0.0.2-Setup.exe`. This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BrainLesion/modsort upstream documentation](https://github.com/BrainLesion/modsort/blob/main/README.md).
- [BrainLesion/modsort release v0.0.2](https://github.com/BrainLesion/modsort/releases/tag/v0.0.2).

## Plan and acceptance criteria

Select and pin the published ARM AppImage conditionally, retain x86 support, and inspect its extracted executable/dependencies. Test the GUI and a real sequence sorting/copying operation with output assertions; AppImage availability alone is not runtime verification.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/modsort/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
