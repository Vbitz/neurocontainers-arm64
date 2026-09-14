# spinalcordtoolbox: ARM64 research plan

Researched: 2026-09-13. Recipe version: `7.3.3`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

The previous native attempt stopped during PyQt5 source metadata generation with exit 143. This is not an unsupported-instruction error. PyQt5 5.15.11 is available as a Conda ARM package, but SCT's exact bundled Qt/Python pins and other native binaries remain constraints.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/spinalcordtoolbox/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `downloaded_tar_file`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/74). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699323574); use the issue for exact candidate SHA and failure context.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699607997); use the issue for exact candidate SHA and failure context.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [spinalcordtoolbox/spinalcordtoolbox upstream documentation](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/README.rst).
- [spinalcordtoolbox/spinalcordtoolbox Dockerfile](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/Dockerfile).
- [spinalcordtoolbox/spinalcordtoolbox requirements.txt](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/requirements.txt).
- [spinalcordtoolbox/spinalcordtoolbox setup.py](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/master/setup.py).
- [spinalcordtoolbox/spinalcordtoolbox release 7.3](https://github.com/spinalcordtoolbox/spinalcordtoolbox/releases/tag/7.3).
- [Conda-forge native Qt package metadata](https://api.anaconda.org/package/conda-forge/pyqt).

## Plan and acceptance criteria

Inspect the pinned installer and dependency freeze for a documented native Qt route; use an applicable upstream configuration fix before retrying. Preserve SCT segmentation, registration and viewer functionality, and record runtime scientific results rather than treating installer completion as success.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/spinalcordtoolbox/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Keep the recorded failure as the current blocker for that candidate. A released upstream fix or documented configuration addressing its first error is the condition for a justified retry. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/74#issuecomment-5646623032).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
