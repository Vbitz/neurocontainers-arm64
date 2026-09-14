# mricrogl: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.2.20211006`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

MRIcroGL documents Linux source compilation with Lazarus/FreePascal and system libqt5pas. The recipe's amd64 QtPas package is replaceable. Optional accelerated compression/build settings need inspection, but no fundamental source blocker is established.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/mricrogl/build.yaml).
- Base image expression: `ubuntu:20.04`.
- Declared download inputs: `v`, `libqt5pas1_2_9_0_amd64_deb`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/97). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [rordenlab/MRIcroGL upstream documentation](https://github.com/rordenlab/MRIcroGL/blob/master/README.md).
- [rordenlab/MRIcroGL release v1.2.20220720](https://github.com/rordenlab/MRIcroGL/releases/tag/v1.2.20220720).
- [davidbannon/libqt5pas upstream documentation](https://github.com/davidbannon/libqt5pas/blob/master/README.md).
- [davidbannon/libqt5pas release v1.2.16](https://github.com/davidbannon/libqt5pas/releases/tag/v1.2.16).

## Plan and acceptance criteria

Build the pinned source with native Lazarus/QtPas and documented portable settings. Test NIfTI/DICOM loading, scripting and rendered image output. Preserve required capabilities while avoiding x86-specific optional compression binaries.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/mricrogl/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Plausible**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/97#issuecomment-5654319586).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
