# cartool: ARM64 research plan

Researched: 2026-09-13. Recipe version: `5.06.04`. Target: native Linux ARM64.

**Assessment: Different operating-system application port required.**

Cartool publishes source and build instructions, so it is not binary-only. The distributed installer is a Windows executable, and the supported build targets Windows tooling. Running it through Wine does not turn x86 Windows code into native Linux ARM code.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/cartool/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `cartool_installer`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/188). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [DenisBrunet/Cartool upstream documentation](https://github.com/DenisBrunet/Cartool/blob/main/README.md).
- [DenisBrunet/Cartool release 5.06.05](https://github.com/DenisBrunet/Cartool/releases/tag/5.06.05).
- [Upstream build requirements](https://github.com/DenisBrunet/Cartool/blob/main/BUILDING.md).

## Plan and acceptance criteria

Review the Windows-specific application/framework dependencies in BUILDING.md. A Linux application port is beyond recipe configuration; revisit when upstream offers a Linux build or a genuinely native supported route. Preserve EEG analysis and visualization behavior.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/cartool/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A native upstream artifact or supported source/build route preserving the same application is required. Revisit when that concrete prerequisite changes. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Outside scope**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/188#issuecomment-5651529073).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
