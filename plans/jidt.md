# jidt: ARM64 research plan

Researched: 2026-09-13. Recipe version: `1.6`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

JIDT is a portable Java library and upstream distributes source/classes. The recipe also deploys an old amd64 RStudio desktop package; Java itself is not the blocker. R/JPype/rJava native dependencies and the promised IDE need compatible builds.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/jidt/build.yaml).
- Base image expression: `ubuntu:22.04`.
- Declared download inputs: `jidt_zip`, `rstudio_deb`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/149). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [jlizier/jidt upstream documentation](https://github.com/jlizier/jidt/blob/master/README.md).
- [jlizier/jidt release v1.6.1](https://github.com/jlizier/jidt/releases/tag/v1.6.1).

## Plan and acceptance criteria

Keep the JIDT jar, select native JVM and Python/R bindings, and establish an ARM build of the included RStudio version. Test the transfer-entropy examples and RStudio launch. Removing the IDE would change this container's declared functionality.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/jidt/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **➖ Not run**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-prerequisite**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/149#issuecomment-5651348926).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
