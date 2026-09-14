# civet: ARM64 research plan

Researched: 2026-09-13. Recipe version: `2.1.1`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The recipe already builds CIVET from source. Linux-x86_64 is also a directory name copied from upstream's build layout; its spelling alone does not prove CPU-specific code. The old Netpbm/MINC build stack and generated environment scripts need inspection.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/civet/build.yaml).
- Base image expression: `ubuntu:18.04`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/130). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [aces/CIVET_Full_Project upstream documentation](https://github.com/aces/CIVET_Full_Project/blob/master/README.md).
- [aces/CIVET_Full_Project Dockerfile](https://github.com/aces/CIVET_Full_Project/blob/master/Dockerfile).
- [aces/CIVET_Full_Project release CIVET_2_1_1](https://github.com/aces/CIVET_Full_Project/releases/tag/CIVET_2_1_1).

## Plan and acceptance criteria

Follow CIVET's source build using native compilers, inspect architecture detection and bundled source archives, and adjust only ordinary paths/configuration. Test cortical processing and thickness output. Stop at a real unsupported dependency rather than assuming the directory name is one.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/civet/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **✅**, fulltest **❌**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653806029).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
