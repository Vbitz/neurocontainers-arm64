# itksnap: ARM64 research plan

Researched: 2026-09-13. Recipe version: `4.4.0`. Target: native Linux ARM64.

**Assessment: Plausible recipe-level port; no fundamental blocker established.**

ITK-SNAP publishes source and explicitly links build instructions. The recipe's prebuilt Linux executable is a packaging choice. Its ITK/VTK/Qt build and rendering dependencies require validation, but no fundamental ARM compiler failure is recorded.

This is a research assessment, not a successful build or a claim that all source-build routes have been exhausted.

## Pinned recipe and existing evidence

- [Recipe at accepted source `457c5a31b983`](https://github.com/Vbitz/neurocontainers/blob/457c5a31b9830587801a06e7d6f81f18293135e8/recipes/itksnap/build.yaml).
- Base image expression: `ubuntu:24.04`.
- Declared download inputs: `downloaded_tar_file`, `MRI_crop_zip`.
- [Previous issue and investigation comments](https://github.com/Vbitz/neurocontainers-arm64/issues/148). Earlier labels are historical claims, not independent proof of a fundamental blocker.

## Upstream findings

The assessment above is based on the recipe and these upstream sources inspected during this pass. Current upstream documentation may describe a newer release; the plan explicitly retains the pinned-version compatibility question.

- [pyushkevich/itksnap upstream documentation](https://github.com/pyushkevich/itksnap/blob/master/README.md).
- [pyushkevich/itksnap CMakeLists.txt](https://github.com/pyushkevich/itksnap/blob/master/CMakeLists.txt).
- [pyushkevich/itksnap release v4.4.0-beta2](https://github.com/pyushkevich/itksnap/releases/tag/v4.4.0-beta2).

## Plan and acceptance criteria

Use release-matched CMake/superbuild instructions and native ITK/VTK/Qt libraries, preserving all segmentation modules. Test volume loading, segmentation editing or scripted processing, and output image geometry on ARM.

Preserve the assertions in [the existing fulltest](../neurocontainers/recipes/itksnap/fulltest.yaml) and the deployment checks. Any future acceptance requires a newly built native ARM64 image, architecture verification, SIF conversion and meaningful runtime tests. Configuration generation alone is insufficient.

## Decision boundary

Proceed to a bounded recipe-level experiment after resolving the exact inputs above. There is presently insufficient evidence to label this recipe fundamentally blocked. Do not introduce emulation, replace scientific implementations, omit essential tests or maintain private library/compiler ports.

## Implementation outcome — 2026-09-14

- Candidate `7ceabea5d97151a98cf6655055729804870b33ee` on
  `arm64/itksnap-root` built ITK 5.4.3 and VTK 9.3.1 natively, including the
  required `RenderingExternal` module, but its final ITK-SNAP configure failed
  before compiling the application. The first actionable errors were the
  source archive's missing Git metadata (`get_git_commit_date`) and the pinned
  source's Qt 6.7 style translation/deployment API on Ubuntu Qt 6.4.2
  (`qt_generate_deploy_script` was unknown; the newer translation signature
  also produced a bad qrc input path). This is recorded in
  [run 34769119103](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769119103).
- A targeted recipe-level retry `905404b1facd8697ba2e0d3e641d0ab60c351a98`
  adds an empty archive Git commit, maps the translation call to Qt 6.4's
  `qt6_add_translations`, omits only the unavailable optional deployment helper
  so system Qt plugins are used, and corrects the installed main executable
  path. Local validation and ARM64/x86_64 generation pass.
- The exact native retry is [run 34771393155](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34771393155),
  currently in progress. Its accepted-base replay is prepared as
  `f4a84c7150db1e9a35cb9f26014304a7ed0b3804` on `arm64/itksnap-integrated`.
  Do not advance the top-level pin until the integrated candidate is also
  rebuilt and passes all gates.

The exact retry `34771393155` then reached application compilation and failed
on narrow Qt 6.4 source compatibility errors: three `QDebug` insertions passed
`std::string` without an unambiguous overload, and `SNAPQtCommon.cxx` used
`QTimeZone` without including its definition. ITK and VTK compiled successfully.

## Implementation outcome — 2026-09-14 (continued)

- Candidate `15fb3f7a0699f337fcbe30b7dd1844968f49b173` adds the three
  `QString::fromStdString` conversions and the missing `QTimeZone` include.
  Recipe validation and ARM64/x86_64 Dockerfile generation pass.
- The complete ITK-SNAP change set was replayed onto accepted PyDeface pin
  `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` as integrated candidate
  `701e4cd9f3d0bb8dc65b65bb655975b20ba19cfe` on
  `arm64/itksnap-integrated-80a`.
- Exact native verification is dispatched as
  [run 34773851298](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773851298),
  attempt 4/6. The top-level pin remains unchanged until this exact SHA
  passes build, SIF, deploy and fulltest.

Run [34773851298](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773851298) reached application compilation and failed on one additional `QDebug`/`std::string` conversion and a missing `QDialogButtonBox` include in `DeepLearningServerPanel.cxx`. Candidate `258f746afb80f90077beb6fb63d0a336745fbb1e` adds those narrow Qt 6.4 source fixes, passes local validation and both architecture generations, and is dispatched as the final bounded retry in [run 34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451).

Run 34776098451 compiled 740/751 targets and then exposed three missed
`QDebug << std::string` expressions in the bundled `SSHTunnelTest/main.cxx`.
Candidate [`c14b22703394ab8ed56510580ef8c381605fb9ec`](https://github.com/Vbitz/neurocontainers/commit/c14b22703394ab8ed56510580ef8c381605fb9ec)
replays the complete source-build route onto accepted pin `8bcc3e3d` and adds
the same explicit `QString::fromStdString` conversion to that test source.
Validation and both architecture generations pass. Exact retry [run
34778923438](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778923438)
was a recipe command quoting failure before the source build: the Python
lambda's `pair: value` was parsed as a YAML mapping and generated an invalid
shell command. Candidate [`817d0c540376842f9b63304be53f7c7b0f1538a4`](https://github.com/Vbitz/neurocontainers/commit/817d0c540376842f9b63304be53f7c7b0f1538a4)
replaces that expression with explicit string replacements, passes validation
and both architecture generations, and is dispatched in exact retry [run
34779151809](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779151809),
attempt 3/6. Stop if the next failure is a dependency port rather than a
localized Qt compatibility issue.
