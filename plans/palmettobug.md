# palmettobug: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.2.11`. Target: native Linux ARM64.

**Assessment: Complete dependency stack unresolved.**

PyPI supplies a platform-independent wheel for 0.2.11 and upstream source is public, contradicting any core binary-only interpretation. Upstream warns that its many dependencies require a tightly controlled Python environment; the recipe uses Python 3.11 while current README guidance specifies 3.10.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/palmettobug/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `miniconda latest`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/98). Earlier labels are historical claims, not independent proof of a fundamental blocker.
- [Existing native attempt](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34738541920); use the issue for exact candidate SHA and failure context.

## Upstream findings

Package `palmettobug-0.2.11`: 0 Linux ARM wheel filenames, 1 source archives, 1 universal wheel filenames in the inspected release metadata. A wheel must also match the Python ABI and resolve its dependencies.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [BenCaiello/Palmettobug upstream documentation](https://github.com/BenCaiello/PalmettoBUG/blob/main/README.md).
- [BenCaiello/Palmettobug pyproject.toml](https://github.com/BenCaiello/PalmettoBUG/blob/main/pyproject.toml).
- [BenCaiello/Palmettobug release 0.2.11](https://github.com/BenCaiello/PalmettoBUG/releases/tag/0.2.11).
- [palmettobug-0.2.11 published package metadata](https://pypi.org/pypi/palmettobug/0.2.11/json).

## Plan and acceptance criteria

Read the exact 0.2.11 metadata, resolve its pinned native imaging/GUI packages on ARM, and reconcile Python version against the existing tested environment. Test cytometry preprocessing/analysis and GUI operation. Record any exact missing dependency; do not infer one from Miniconda alone.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/palmettobug/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

A dependency/source-build investigation remains, rather than an established universal ARM incompatibility. Revisit when the exact native package set or documented source configuration is available; record any first actionable failure. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.
