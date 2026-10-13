# afni: ARM64 research plan

Researched: 2026-09-13. Recipe version: `26.0.07`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

No fundamental ARM64 blocker established. The recipe chooses an x86 Linux tarball, but AFNI publishes source and a documented local build. Its precompiled R library bundle is a separate architecture-specific input.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/afni/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Builder templates: `freesurfer 7.4.1`.
- Declared download inputs: `update_afni_binaries`, `linux_ubuntu_24_R_4_3_libs_tgz`, `afni_binary`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/118). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [afni/afni upstream documentation](https://github.com/afni/afni/blob/master/README.rst).
- [afni/afni CMakeLists.txt](https://github.com/afni/afni/blob/master/CMakeLists.txt).
- [AFNI source-build documentation](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/download_links.html).

## Plan and acceptance criteria

Build the pinned AFNI source with its supported build tooling and ARM system libraries; rebuild the R packages rather than reuse the binary bundle. Validate AFNI and SUMA, a small image calculation, and an R-based analysis.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/afni/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Accepted implementation — 2026-09-14

Candidate `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` passed native ARM64 Docker build, SIF conversion, deploy checks, and all **114/114** fulltests in [run 34765634289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765634289). The ARM route builds AFNI and its R bundle from the published ARM inputs while preserving the x86_64 route.

## Current upstream preflight — 2026-10-13

Outcome: blocked-prerequisite (preflight; no build/PR)

AFNI26.3.02 core has an official native Ubuntu24 ARM build, but the full current recipe unconditionally installs FreeSurfer7.4.1 from freesurfer-linux-centos7_x86_64-7.4.1.tar.gz through the shared template. Official7.4.1 distribution lists Linux x86_64/amd64 and macOS x86_64 only. AFNI @SUMA_Make_Spec_FS explicitly requires mris_convert, so this is a scientific workflow dependency, not an unused cosmetic file. No native Linux ARM7.4.1 packaged replacement is published. An ordinary documented supported native source configuration for that version was not established; this is a blocker for the existing packaged route, not a claim that every source build is impossible. Do not retain x86 binaries as ARM functionality, remove the dependency, upgrade the scientific dependency silently or introduce emulation/private ports.

At current baseline `9545cba27a176c0c9af44c03fe23c9962e71e531`, official ARM AFNI_version.txt reports `AFNI_26.3.02`, `linux_ubuntu_24_ARM`, `Oct09 2026`, `official`. Thus the main AFNI binary route itself is feasible. Historical114/114 AFNI reports do not cover execution/architecture of bundled FreeSurfer; they remain limited evidence. No private fork, dependency deletion, weaker test or emulation attempted. Start `2026-10-13T02:11:06.877059+00:00`, deadline `2026-10-13T14:11:06.877059+00:00`, attempts0/6. Revisit: Revisit with a compatible released native Linux ARM64 FreeSurfer7.4.1 package or documented supported source configuration preserving its complete required workflow; then test native mris_convert alongside AFNI/SUMA/R scientific operations.

Official sources: - https://afni.nimh.nih.gov/pub/dist/bin/linux_ubuntu_24_ARM/AFNI_version.txt
- https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/
- https://afni.nimh.nih.gov/pub/dist/doc/program_help/@SUMA_Make_Spec_FS.html
- https://github.com/freesurfer/freesurfer/blob/v7.4.1/README.md

Durable outcome: https://github.com/Vbitz/neurocontainers-arm64/issues/118#issuecomment-6136742703
