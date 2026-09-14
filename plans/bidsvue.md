# bidsvue: ARM64 research plan

Researched: 2026-09-13. Recipe version: `0.1.20260704`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

The exact release offers a Linux amd64 package and an Apple ARM package, not an interchangeable Linux ARM binary. However the project documents a Rust/Tauri source build. The desktop shell and its bundled dcm2niix/niimath sidecars need architecture-correct builds.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/bidsvue/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `bidsvue_deb`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/121). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

Release `v0.1.20260704` lists: `BIDSvue_0.1.20260704_aarch64.dmg`, `BIDSvue_0.1.20260715_aarch64.dmg`. This release metadata establishes asset availability, not a passed native test.

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [niivue/BIDSvue upstream documentation](https://github.com/niivue/BIDSvue/blob/main/README.md).
- [niivue/BIDSvue package.json](https://github.com/niivue/BIDSvue/blob/main/package.json).
- [niivue/BIDSvue release v0.1.20260704](https://github.com/niivue/BIDSvue/releases/tag/v0.1.20260704).

## Plan and acceptance criteria

Build the pinned source with Rust, Bun and Linux WebKitGTK/Tauri prerequisites. Inspect sidecar acquisition and compile the same tools natively. Test importing DICOM, BIDS validation and de-identification, plus GUI startup.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/bidsvue/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **5/5** fulltests in [run 34768724186](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768724186). The ARM route builds the Rust/Tauri application and installs its launcher at the existing deployment path while preserving x86_64 packaging.
