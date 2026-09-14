# networkcorrespondancetoolkit: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.3.3.post2`. Target: native Linux ARM64.

**Assessment: Concrete prior build failure; not a general architecture prohibition.**

The previous native runs exposed an ARM VTK/Qt dependency solve conflict with pinned Wayland/OpenSSL constraints. The toolkit is Python source and Qt has ARM packages; the failure is the exact lock, not a fundamental inability to perform network correspondence on ARM.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/networkcorrespondancetoolkit/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `nct_data`, `environment.yml`, `miniconda.sh`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/99). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34745548264); use the issue for exact candidate SHA and failure context.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34745756464); use the issue for exact candidate SHA and failure context.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34745899127); use the issue for exact candidate SHA and failure context.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34739158124); use the issue for exact candidate SHA and failure context.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [rubykong/cbig_network_correspondence upstream documentation](https://github.com/rubykong/cbig_network_correspondence/blob/master/README.md).
- [rubykong/cbig_network_correspondence pyproject.toml](https://github.com/rubykong/cbig_network_correspondence/blob/master/pyproject.toml).
- [rubykong/cbig_network_correspondence release 0.3.3](https://github.com/rubykong/cbig_network_correspondence/releases/tag/0.3.3).

## Plan and acceptance criteria

Retain run evidence and identify a compatible released upstream environment before another attempt. Avoid arbitrary dependency-version changes. Validate atlas correspondence statistics and visualizations with all original numerical assertions.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/networkcorrespondancetoolkit/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Keep the recorded failure as the current blocker for that candidate. A released upstream fix or documented configuration addressing its first error is the condition for a justified retry. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Tracker disposition — 2026-09-14

- Coverage status: build **❌**, fulltest **➖ Not run**; plan assessment: **Unresolved**.
- Investigation outcome: **blocked-upstream**. The exact candidate, native evidence, first actionable blocker, and revisit condition are recorded in [the linked issue outcome](https://github.com/Vbitz/neurocontainers-arm64/issues/99#issuecomment-5652030082).
- This recipe remains unverified. Do not dispatch another attempt unless the linked revisit condition changes or a released upstream fix becomes available.
