# ARM64 porting checkpoint

Updated: 2026-09-13 (Australia/Brisbane)

## Current state

- Top-level branch: `main`
- Top-level commit: `116eb6e` (wfTFI accepted)
- Pinned submodule: `neurocontainers@9a383b0d951f71725f2a2dade16a12e372bd6253` (wfTFI accepted in this checkpoint)
- Submodule checkout: `arm64/blochsiegertb1mapping`, candidate `93a11a16885aec3a548584bb9f3f332fe726df1b` from accepted source `9a383b0d951f71725f2a2dade16a12e372bd6253`; origin `Vbitz/neurocontainers`
- Fork Actions: disabled (`enabled: false`)
- Existing verified pipeline check: `workshopdemo` / `arm64`, run [34692323241](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692323241), 4 passed, source `c6d782cd`
- Coverage snapshot: 84 of 247 declarations, refreshed from accepted source `9a383b0d`; issue [#2](https://github.com/Vbitz/neurocontainers-arm64/issues/2)

## Latest checkpoint

MipView candidate `d7de67d4647d4bfb50eb14f799afd34fd57d3c34` passed exact native
ARM64 run `34704666186` with 4 passed, 0 failed, and 0 skipped. Issue
[#83](https://github.com/Vbitz/neurocontainers-arm64/issues/83) records the
run, report artifact, and acceptance at top-level commit `18d0fba`.

qMRLab candidate `8fdfbd5a814d113d895a8c75a0ad95ca1d7b2873`, based on the
accepted MipView pin, passed exact run `34705439660` with 51 passed, 0 failed,
and 0 skipped. The unchanged recipe commit was applied to the current accepted
ancestry as `0e0f6329f18d4ff60628dfe2fedf16a8a6f6871b`; local validation and
both architecture generations passed, so no duplicate run was dispatched after
the independent Sodiumgridding and Sodiumnufft acceptances. Earlier qMRLab
candidates also passed, but are retained as prior evidence because their base
pins were older.

SynthStrip candidate `d166adbd7ef00e723a322f03e8232b1de4d2cf57` passed exact
native ARM64 run `34698395635` with 70 passed, 0 failed, and 0 skipped. The
same one line recipe commit was applied to the current accepted ancestry as
`e90ee1a49ec687dd8582d10e7fb68546a008ecd4`; local validation and both
architecture generations passed, so no duplicate run was dispatched. Stale
integration run `34703210392` also completed successfully with 70 passed, 0
failed, and 0 skipped; it is bookkeeping only because its source `8533a146`
is not the accepted pin.

Sodiumgridding investigation started at `2026-09-13T02:24:10Z` on attempt 1
from accepted source `d7de67d4647d4bfb50eb14f799afd34fd57d3c34`. Candidate
`cd7950c00e93503648e96270f58104fae11f5718` on branch `arm64/sodiumgridding`
adds only `aarch64`. The OpenRecon source build is already covered by the
accepted OpenRecon I2I result, and the pinned numba, pyFFTW, and SimpleITK
releases publish Linux ARM64 wheels. Validation and both architecture
generations passed. The first dispatch `34705129164` failed before checkout
because of an incorrect ref string and produced no recipe evidence. Corrected
exact candidate run `34705231419` passed with 7 passed, 0 failed, and 0 skipped.
The candidate is accepted at the top-level submodule pointer after this
checkpoint commit.

Sodiumnufft investigation started at `2026-09-13T02:25:40Z` on attempt 1 from
accepted source `d7de67d4647d4bfb50eb14f799afd34fd57d3c34`. Candidate
`444e18aea84dbd67c7e939cba1eccbeab52007bb` on branch `arm64/sodiumnufft`
adds only `aarch64`; its pinned sigpy dependency is a pure Python wheel and it
uses the same ARM64-tested OpenRecon source build. Validation and both
architecture generations passed. Run `34705192559` was dispatched with an
incorrect ref string and failed during source checkout; no recipe evidence was
produced. Corrected exact candidate run `34705290732` was dispatched with
`upload_image=false` and passed with 5 passed, 0 failed, and 0 skipped. The
recipe commit is accepted at the top-level submodule pointer after this
checkpoint commit.

Epirecon investigation started at `2026-09-13T02:36:57Z` on attempt 1 from
accepted source `9602df1a290918704615776c8c52916c374fd0c4`. Candidate
`313f47d4958cd5f69d718edd05656f9f41526d28` on branch `arm64/epirecon` adds
only `aarch64`. It reuses the accepted OpenRecon source build and the pinned
portable `twixtools` dependency; its fulltest includes a synthetic Cartesian
FFT point-source reconstruction assertion. Validation and both architecture
generations passed. Exact run `34705779719` was dispatched with
`upload_image=false` and passed with 7 passed, 0 failed, and 0 skipped. The
same recipe commit is prepared on the qMRLab accepted ancestry as
`89d8112a80230f1d8052dcd2b269b0a1296b41de`; local validation and both
architecture generations passed.

Sodiumgriddingptpi investigation started at `2026-09-13T02:38:23Z` on attempt
1 from accepted source `9602df1a290918704615776c8c52916c374fd0c4`. Candidate
`8cd40433b186f4a71ea98dd04815ecf6fcd3385c` on branch
`arm64/sodiumgriddingptpi` adds only `aarch64`. Its pinned Python dependencies
publish Linux ARM64 wheels, and the existing fulltest exercises the source
gridding CLI. Validation and both architecture generations passed. Exact run
`34705851195` was dispatched with `upload_image=false` and passed with 7
passed, 0 failed, and 0 skipped. The recipe commit was applied by ancestry
after Epirecon as `15a0dd8efbaf96fe820c8f09658aea41629f805b`; local validation
and both architecture generations passed, so no duplicate run was dispatched.

PALM investigation started at `2026-09-12T16:53:27Z` on attempt 1 from
accepted source `e90ee1a49ec687dd8582d10e7fb68546a008ecd4`; deadline
`2026-09-13T04:53:27Z`. Candidate `57b11078062dbf7735fe0e76afd513db17f3b5f1`
on branch `arm64/palm` adds only `aarch64`. The upstream payload is
architecture independent Octave/MATLAB code, and the existing fulltest runs
real PALM permutation analyses against generated NIfTI data. Validation and
both architecture generations passed. Exact run `34706614272` was dispatched
with `upload_image=false` and passed with 56 passed, 0 failed, and 0 skipped.
The unchanged one line recipe commit was applied onto the current accepted
ancestry as `6fe8f9f21abbb8ad7058b6bc26eef81b9b39db85`; local validation and both
architecture generations passed, so no duplicate run was dispatched. Attempt
budget used: 1/6.

wfTFI candidate `9a383b0d951f71725f2a2dade16a12e372bd6253` passed exact native
ARM64 run `34707462294` with 21 passed, 0 failed, and 0 skipped. The candidate
adds `aarch64` and changes the base from Ubuntu 16.04 to Ubuntu 18.04 after the
first exact build showed that the ARM64 Miniconda installer requires GLIBC
2.25. The candidate is a direct descendant of the accepted PALM pin, so it is
accepted here without a duplicate native run; local validation and both
architecture generations passed. Issue [#89](https://github.com/Vbitz/neurocontainers-arm64/issues/89)
contains the durable result and artifact link. Attempt budget used: 3/6,
including one metadata-only short-ref dispatch.

`openreconexample` investigation started at `2026-09-12T17:23:50Z` from
accepted source `9a383b0d951f71725f2a2dade16a12e372bd6253`; deadline
`2026-09-13T05:23:50Z`. Candidate
`2eaed2732a85fa475cb823a336c62f682b8df90b` on branch
`arm64/openreconexample` adds only `aarch64`. It reuses the OpenRecon source
build and FSL-BET2 build already exercised by the accepted OpenRecon I2I
recipe. Validation and both architecture generations passed. An invalid
short-ref dispatch `34708172513` was cancelled during source checkout before
recipe work; corrected exact run `34708194854` is in progress. Attempt budget:
2/6 including the cancelled metadata-only dispatch.

`blochsiegertb1mapping` investigation started at `2026-09-12T17:23:50Z` from
accepted source `9a383b0d951f71725f2a2dade16a12e372bd6253`; deadline
`2026-09-13T05:23:50Z`. Candidate `93a11a16885aec3a548584bb9f3f332fe726df1b`
on branch
`arm64/blochsiegertb1mapping` adds only `aarch64`. It reuses the same accepted
OpenRecon source build, and its fulltest performs numerical Bloch-Siegert map
assertions over synthetic ISMRMRD images. Validation and both architecture
generations passed; exact run `34708203749` is queued. Attempt budget: 1/6.

ANTs investigation started at `2026-09-12T16:57:23Z` on attempt 1 from
accepted source `e90ee1a49ec687dd8582d10e7fb68546a008ecd4`; deadline
`2026-09-13T04:57:23Z`. Candidate `f48620a9503c3f532fa16c1b1e9ccc96778a86c6`
on branch `arm64/ants` adds `aarch64` and makes the existing source-build
compiler flags conditional: the x86_64 path retains its generic x86 flags,
while ARM64 uses the compiler defaults. Upstream ANTs source is built by the
existing Neurodocker template, and the fulltest runs version checks, image
conversion, denoising, thresholding, and smoothing operations. Validation and
both architecture generations passed. Exact run `34706765954` was dispatched
with `upload_image=false` and is still building; attempt budget is 1/6.

wfTFI investigation started at `2026-09-12T17:07:17Z` from accepted source
`6fe8f9f21abbb8ad7058b6bc26eef81b9b39db85`; the 12-hour deadline is
`2026-09-13T05:07:17Z`. Candidate `aad7a88be81b47665b319d1fa6cffbf66b6a8aa3`
on branch `arm64/wftfi` adds only `aarch64`. The build uses the existing
architecture-aware Miniconda template, which generated the ARM64 installer
URL, and its conda-forge environment contains portable Python numerical
dependencies plus the upstream cbviewer source. Local validation and both
architecture generations passed. An initial dispatch `34707269633` used a
short, invalid source ref and is metadata-only; corrected exact run
`34707282986` uses the full candidate SHA, with `upload_image=false`, and
failed during the ARM64 Docker build. The first actionable error was
`GLIBC_2.25 not found` from the ARM64 Miniconda installer; no SIF or runtime
tests were produced. Count the malformed dispatch as attempt 1 and this exact
run as attempt 2/6; it produced no recipe evidence beyond the configuration
failure.

wfTFI retry hypothesis: candidate `9a383b0d951f71725f2a2dade16a12e372bd6253`
on `arm64/wftfi` changes only the base image from Ubuntu 16.04 to Ubuntu 18.04,
which supplies the required glibc while preserving the conda environment and
both x86_64 and ARM64 paths. Validation and both architecture generations
passed. Exact retry `34707462294` was dispatched with `upload_image=false`;
attempt budget is 3/6. The exact retry passed all build, SIF, deploy, and
fulltest gates; issue [#89](https://github.com/Vbitz/neurocontainers-arm64/issues/89)
records 21 passed, 0 failed, and 0 skipped. The candidate is accepted by
ancestry in this checkpoint.

## Queue

Initial verification batch, using the current accepted pin and no recipe edits:

- `dcm2niix` — source build on ARM64, focused DICOM conversion CLI tests
- `niimath` — pinned upstream source build, NIfTI math CLI tests
- `niftyreg` — declared ARM64 build, registration CLI tests
- `vina` — declared ARM64 build, command line smoke tests

After reviewing each result, refill up to four available slots with the next
eligible declared recipe, then assess practical undeclared recipes. Keep one
issue per recipe/variant and record durable evidence in comments.

Integrated port: `dicomtools` branch `arm64/dicomtools`, candidate
`e430edb9d9a595878a619cb4bb00a68056665daf`. The only recipe change is
declaring `aarch64`; validation and ARM64 and x86_64 Dockerfile generation
passed. Run `34687413104` passed all gates and the current accepted checkout
now points to this tested commit.

Prepared and dispatched `rapidtide` from branch `arm64/rapidtide`, candidate
`5c3a60d0e9e906b24441bc8279f2766c7795887e`, as run `34687554873`. Its only
recipe change is declaring `aarch64`; validation and both architecture
Dockerfile generations passed.

Prepared and dispatched `radtract` from branch `arm64/radtract`, candidate
`df8153f509a2f9d838b3e1715ca14492a070a701`, as run `34687615746`. Its only
recipe change is declaring `aarch64`; validation and both architecture
Dockerfile generations passed.

The radtract recipe commit was cherry-picked onto the current accepted pin as
`031ff4750b9097aa0a552eb2efcccef00ab38a3b`; validation and both architecture
Dockerfile generations passed. Its exact integrated recheck is run
`34687953581`.

The rapidtide recipe commit was cherry-picked onto the current accepted pin as
`7e6a7a4072bcad0644b06bb7a7b8433c22a38c7c`; validation and both architecture
Dockerfile generations passed. Its exact integrated recheck is run
`34688020789`.

The lqt accepted-pin recheck against `e430edb9d9a595878a619cb4bb00a68056665daf`
is run `34687969649`.

The declared `segmentator` verification against accepted pin
`e430edb9d9a595878a619cb4bb00a68056665daf` is run `34688060966`. Its suite
includes CLI help, imports, and a synthetic NIfTI histogram output assertion.

The declared `spant` verification against accepted pin `031ff4750b9097aa0a552eb2efcccef00ab38a3b`
is run `34688352312`; the declared `condaenvs` verification is run
`34688353976`.

## Active attempts

Initial verification started at `2026-09-12T09:09:37Z`; each recipe is on
attempt 1 with a 12-hour deadline of `2026-09-12T21:09:37Z`.

The `bidstools`, `dicompare`, and `eharmonize` baseline runs started at
`2026-09-12T09:36:08Z`; each passed on attempt 1. Their accepted-pin rechecks
started at `2026-09-12T09:44:07Z` and use the full accepted source SHA
`7bd4f9ee9734c4dd3a449290c39955f009f081d3`.

The `afib1` current-pin verification started at `2026-09-12T09:46:06Z` on
attempt 1 with a deadline of `2026-09-12T21:46:06Z`.

The `b0map` current-pin verification started at `2026-09-12T09:52:16Z` on
attempt 1 with a deadline of `2026-09-12T21:52:16Z`. The `arfiproc` run started
at `2026-09-12T09:49:34Z` and passed on attempt 1. The `bidsmanager` and
`cbsb0stats` runs started at `2026-09-12T09:55:01Z` and
`2026-09-12T09:55:03Z`, respectively, on attempt 1.

The lqt verification started at `2026-09-12T09:57:17Z`; dicomtools started at
`2026-09-12T10:02:51Z` and passed on attempt 1. The rapidtide port started at
`2026-09-12T10:06:07Z` on attempt 1 with a deadline of `2026-09-12T22:06:07Z`.
The radtract port started at `2026-09-12T10:07:29Z` on attempt 1 with a
deadline of `2026-09-12T22:07:29Z`.
The radtract current-pin recheck started at `2026-09-12T10:15:12Z`; the lqt
current-pin recheck started at `2026-09-12T10:15:30Z`; and the rapidtide
current-pin recheck started at `2026-09-12T10:16:41Z`.
The segmentator verification started at `2026-09-12T10:17:38Z`.
The spant verification started at `2026-09-12T10:24:13Z`; condaenvs started at
`2026-09-12T10:24:15Z`.
The rapidtide recheck on the radtract-advanced accepted pin started at
`2026-09-12T10:26:37Z`.
The final lqt recheck on accepted source `031ff4750b9097aa0a552eb2efcccef00ab38a3b`
started at `2026-09-12T10:31:43Z` as run `34688683840`.

DeepDisco investigation started at `2026-09-12T13:20:10Z` on attempt 1 with a
12-hour deadline of `2026-09-13T01:20:10Z`, from accepted source
`31091ade121699a43a8745a2633e325f47c99061`. The evidence-supported hypothesis
is that the recipe needs only an `aarch64` declaration because its pinned CPU
PyTorch and PySide6 dependencies publish Linux ARM64 wheels and the fulltest
loads a bundled model checkpoint.

DeepDisco candidate `fbce330df22a4152be2a2be2e67ae5e959f8148c` was validated,
generated for both architectures, pushed to `arm64/deepdisco`, and dispatched
as run `34696205436` at `2026-09-12T13:21:29Z`. It passed 2 tests and was
accepted serially as the current pinned source; issue [#67](https://github.com/Vbitz/neurocontainers-arm64/issues/67) has the run and evidence links.

FLAMeS investigation started at `2026-09-12T13:22:48Z` on attempt 1 with a
12-hour deadline of `2026-09-13T01:22:48Z`, from accepted source
`31091ade121699a43a8745a2633e325f47c99061`. The proposed change is an
architecture-conditional Miniforge installer while retaining the existing CPU
PyTorch and runtime fulltest.

FLAMeS candidate `9614409505d9d6102528c33f972290572e655bf4` was validated,
generated for both architectures, pushed to `arm64/flames`, and dispatched as
run `34696329756` at `2026-09-12T13:24:11Z`; it passed 9 tests, but was based
on the older accepted source `31091ade`. The recipe commit was replayed onto
the current accepted pin as integrated candidate
`1c6bd96c84cd75dc52aae6598cf363e24e7a37aa` on
`arm64/integrate-flames-deepdisco`; validation and both architecture
generations passed. Exact serial recheck `34696992986` was dispatched at
`2026-09-12T13:38:38Z`; issue [#69](https://github.com/Vbitz/neurocontainers-arm64/issues/69)
records both runs and the integration checkpoint.

QSMxT investigation started at `2026-09-12T13:29:02Z` on attempt 1 with a
12-hour deadline of `2026-09-13T01:29:02Z`, from accepted source
`fbce330df22a4152be2a2be2e67ae5e959f8148c`. The existing recipe already
selects the official upstream `aarch64` release archive for architecture
conditional builds, and the pinned v9.17.0 release contains that asset.

QSMxT candidate `b7c54813713c74d6c707b800d8e26c622bcbb3f1` was validated,
generated for both architectures, pushed to `arm64/qsmxt`, and dispatched as
run `34696583728` at `2026-09-12T13:29:51Z`; the official ARM64 archive was
missing the bundled `dcm2niix` path and the build stopped before SIF conversion.
The targeted recipe fix builds the documented dcm2niix source for ARM64 at the
expected path. Candidate `a0c486f70e96e3a9e6e2d91ffe3e2947ca2c7cde` passed
validation and both architecture generations, was pushed to `arm64/qsmxt`, and
was dispatched as retry `34696916528` at `2026-09-12T13:36:55Z`; issue
[#68](https://github.com/Vbitz/neurocontainers-arm64/issues/68) records the
first error, hypothesis, retry, and successful 9-test result; the candidate is
pending replay onto the accepted FLAMeS pin and exact serial integration
recheck.

QSMxT was replayed onto the accepted FLAMeS pin as integrated candidate
`56253af124371ff19dd7c82cf97e82a60e10fcaf` on branch
`arm64/integrate-qsmxt-flames`; validation and both architecture generations
passed. Exact serial recheck `34697632034` passed all 9 tests and is now the
accepted pin; issue [#68](https://github.com/Vbitz/neurocontainers-arm64/issues/68)
records the integrated source and verification.

MNE investigation started at `2026-09-12T13:30:58Z` on attempt 1 with a
12-hour deadline of `2026-09-13T01:30:58Z`, from accepted source
`fbce330df22a4152be2a2be2e67ae5e959f8148c`. The proposed change selects the
official ARM64 VS Code Debian package on `aarch64` while preserving the x86_64
download and the existing conda-based MNE runtime tests.

MNE candidate `953c23b9731267e08b816e48f4f88c0be314768f` was validated,
generated for both architectures, pushed to `arm64/mne`, and dispatched as run
`34696735862` at `2026-09-12T13:33:00Z`; it passed 6 tests and issue
[#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70) records the
verification. Its recipe commit was replayed onto the accepted QSMxT pin as
integrated candidate `f8a66f994161507e1399826980f78c90fcec6e19` on branch
`arm64/integrate-mne-qsmxt`; validation and both architecture generations
passed. Exact serial recheck `34698033237` was dispatched at
`2026-09-12T14:00:56Z` and is currently in progress.

MNEextended investigation started at `2026-09-12T13:49:38Z` on attempt 1 with
a 12-hour deadline of `2026-09-13T01:49:38Z`, from accepted source
`fbce330df22a4152be2a2be2e67ae5e959f8148c`. Candidate
`108f2d4a624f28188e31b950fb7220376b7bc27e` on branch `arm64/mneextended`
passed validation and both architecture generations, and was dispatched as run
`34697506684`; the build stopped before SIF conversion because conda-forge has
no `pyedflib` package for `linux-aarch64`. A targeted fix installs the official
PyPI `pyedflib==0.1.42` ARM64 wheel after conda environment creation while
preserving the existing tests. Retry candidate
`f31fde3e10df1161043f0dc92cdfafea731bc32d` passed validation and ARM64
generation and was dispatched as run `34697784145` at `2026-09-12T13:55:43Z`;
it installed the ARM64 wheel but failed `pip check` on the existing
`trame-vtk`/`trame-client` constraint. Attempt 3 candidate
`91ac9396f876ee9835d13cb72903ad17a8f95d5a` adds the direct `trame-client<4`
conda constraint and passed validation and ARM64 generation. An abbreviated
ref dispatch failed before checkout as run `34698178019`; the corrected exact
full-SHA run `34698395577` was dispatched at `2026-09-12T14:08:16Z` and failed
with the next trame dependency conflict. Issue
[#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70) records the
failure, correction, hypothesis, and blocked-upstream decision.

SynthStrip investigation started at `2026-09-12T14:07:36Z` on attempt 1 with
a 12-hour deadline of `2026-09-13T02:07:36Z`, from accepted source
`56253af124371ff19dd7c82cf97e82a60e10fcaf`. The recipe adds only `aarch64`;
the pinned CPU-only PyTorch 2.2.2 index publishes Linux ARM64 wheels, and the
existing fulltest performs real SynthStrip output and image-shape assertions.
Candidate `d166adbd7ef00e723a322f03e8232b1de4d2cf57` passed validation and both
architecture generations. Its abbreviated-ref dispatch failed before checkout
as run `34698365483`; corrected exact full-SHA run `34698395635` was dispatched
at `2026-09-12T14:08:16Z`.

SynthStroke investigation started at `2026-09-12T14:17:50Z` on attempt 1 with
a 12-hour deadline of `2026-09-13T02:17:50Z`, from accepted source
`f8a66f994161507e1399826980f78c90fcec6e19`. Candidate
`9e66780db53cae25e95c28e55fc79b78905dff19` declares `aarch64`, passes
validation and both architecture generations, selects the architecture-matched
official Miniconda installer, and adds a bundled baseline inference assertion.
Its abbreviated-ref dispatch failed before checkout as run `34698867860`;
corrected exact full-SHA run `34698887077` built and converted successfully but
the added assertion used an undefined output variable. Retry candidate
`bb3f660d9c3ec0718df2f558cd15450eaffd8260` corrects that path, passed
validation and both architecture generations, and was dispatched as exact run
`34699377187` at `2026-09-12T14:28:16Z`. Issue
[#73](https://github.com/Vbitz/neurocontainers-arm64/issues/73) records the
failure, hypothesis, and retry.
The exact candidate descended directly from the accepted pin, so serial
integration branch `arm64/integrate-synthstroke` points to the same SHA.
Serial recheck `34699910413` was dispatched at `2026-09-12T14:39:12Z` before
advancing the top-level pointer.
It passed all gates with 4 tests passed, 0 failed, and 0 skipped; the tested
candidate is accepted at top-level submodule pin
`bb3f660d9c3ec0718df2f558cd15450eaffd8260`.

Spinal Cord Toolbox investigation started at `2026-09-12T14:27:11Z` on attempt
1 with a 12-hour deadline of `2026-09-13T02:27:11Z`, from accepted source
`f8a66f994161507e1399826980f78c90fcec6e19`. Candidate
`2e72afcc66bab2d8076e7fb48cffaf9119cef2be` declares `aarch64` and conditionally
rewrites the pinned upstream installer to use the official Miniforge Linux
ARM64 asset, while preserving x86_64 and the GPU-only variant. Validation and
both architecture generations passed. Exact run `34699323574` was dispatched
at `2026-09-12T14:27:11Z` and failed during the pinned PyQt5 5.15.11 source
metadata build because qmake was unavailable. The targeted fix added Ubuntu
`qtbase5-dev`; validation and both architecture generations passed. Retry
candidate `3dac0979b1d71e7f4a5d2a9e8d5c8dc08e9a5b0` was dispatched as exact run
`34699607997` at `2026-09-12T14:32:56Z`. Issue
[#74](https://github.com/Vbitz/neurocontainers-arm64/issues/74) records the
first error, hypothesis, and retry.
The retry installed qmake and resolved the ARM64 dependency set, but the pinned
PyQt5 5.15.11 source distribution stayed in `Preparing metadata` for about 13
minutes before the build process ended with exit 143. No SIF or fulltest ran;
this is blocked-upstream pending a supported PyQt5 ARM64 wheel or documented
ARM64 source-build path.

CLEARSWI investigation started at `2026-09-12T14:38:25Z` on attempt 1 with a
12-hour deadline of `2026-09-13T02:38:25Z`, from accepted source
`f8a66f994161507e1399826980f78c90fcec6e19`. Candidate
`86c62b327f7ddc784df2eb114f7bdd3f7f8ae091` on `arm64/clearswi` selects the
official Julia Linux ARM64 archive while preserving the x86_64 archive. It
passed validation and both architecture generations. Exact run
`34699875754` installed and precompiled the Julia dependencies, then failed
during PackageCompiler sysimage generation with Julia LLVM instruction
selection error `i64 = vscale Constant:i64<1>` in
`HostCPUFeatures/src/cpu_info_aarch64.jl`, followed by signal 6. No SIF or
fulltest ran; this is blocked-upstream pending an upstream Julia/LLVM/
PackageCompiler ARM64 fix or documented generic sysimage path. Issue
[#75](https://github.com/Vbitz/neurocontainers-arm64/issues/75) records the
first error and revisit condition.

QSMbly investigation started at `2026-09-12T15:01:01Z` on attempt 1 with a
12-hour deadline of `2026-09-13T03:01:01Z`, from accepted source
`bb3f660d9c3ec0718df2f558cd15450eaffd8260`. Candidate
`fb92480d3132c936de1c3cd4b88cb9e6cc61cb11` on `arm64/qsmbly` declares
`aarch64` and adds a launcher output assertion to the existing WebAssembly
asset test while preserving x86_64. Validation and both architecture
generations passed. The first dispatch used an invalid source ref and failed
before checkout as run `34700948284`; corrected exact run `34701138583` is now
queued with `upload_image=false`. Issue creation is pending the workflow
report.

The corrected run built and converted successfully and passed deploy checks and
fulltest with 2 passed, 0 failed, and 0 skipped. Issue
[#76](https://github.com/Vbitz/neurocontainers-arm64/issues/76) records the
verified candidate and the required serial integration recheck.
The serial integration branch points to the same candidate because it descends
directly from the accepted pin. Revalidation passed and serial exact run
`34701432576` was dispatched at `2026-09-12T15:10:39Z`.
Serial run `34701432576` passed with 2 passed, 0 failed, and 0 skipped, and
the top-level submodule pointer now accepts
`fb92480d3132c936de1c3cd4b88cb9e6cc61cb11`.

VertexWiseR investigation started at `2026-09-12T15:04:18Z` on attempt 1 with
a 12-hour deadline of `2026-09-13T03:04:18Z`, from accepted source
`bb3f660d9c3ec0718df2f558cd15450eaffd8260`. Candidate
`881380dbc85bbf7460e8071c1334c9d8ac6c51c5` on `arm64/vertexwiser` declares
`aarch64` and updates the pinned VTK dependency from 9.3.1, which has no Linux
ARM64 wheel, to official VTK 9.7.0, which publishes Linux ARM64 and x86_64
wheels. Validation and both architecture generations passed. Exact run
`34701117134` built and converted successfully and passed deploy checks and
fulltest with 10 passed, 0 failed, and 0 skipped. Issue
[#77](https://github.com/Vbitz/neurocontainers-arm64/issues/77) records the
candidate and the required serial integration recheck.
The integration branch cherry-picked the recipe commit onto accepted source
`fb92480d3132c936de1c3cd4b88cb9e6cc61cb11`; revalidation passed and serial
exact run `34701810565` was dispatched at `2026-09-12T15:18:04Z`.

Deep Quality Estimation investigation started at `2026-09-12T15:24:14Z` on
attempt 2 with a 12-hour deadline of `2026-09-13T03:24:14Z`, from accepted
source `fb92480d3132c936de1c3cd4b88cb9e6cc61cb11`. Candidate
`891296e99840fb0ba9117cb7481676a8385c8bf3` on
`arm64/deep-quality-estimation` declares `aarch64` and selects the official
PyTorch CPU 2.5.1 aarch64 wheel on ARM64 while preserving the existing CUDA
installation on x86_64. Validation and both architecture generations passed.
Attempt 1 candidate `74dd8ca66dba65499c9751b805b0dd46be1011fd` failed before
deploy in run `34702124198` because a multiline shell conditional was expanded
with invalid `&&` separators. The conditional was folded into one shell
command and the corrected exact run `34702315565` was dispatched at
`2026-09-12T15:28:03Z` with `upload_image=false`. Issue
[#78](https://github.com/Vbitz/neurocontainers-arm64/issues/78) records the
failure and correction.

Template (DataLad) investigation started at `2026-09-12T15:30:43Z` on attempt
1 with a 12-hour deadline of `2026-09-13T03:30:43Z`. Candidate
`626fcf8705eb46228251f7b41b63b6c3e949acb7` on `arm64/template` declares
`aarch64` and adds a version-output assertion to the existing DataLad fulltest.
The pinned NeuroDebian Bookworm image is a multi-architecture manifest with a
native Linux ARM64 image. Validation and both architecture generations passed;
candidate run `34702446198` passed with 2 passed, 0 failed, and 0 skipped.
The first serial run `34702657955` also passed with 2 passed, 0 failed, and 0
skipped, but its branch descended from stale pre-Vertex accepted source
`fb92480d`, so it is retained as recipe evidence and not accepted integration
evidence. Corrected integrated candidate `0d53a8c8cdebd167e6eff657f7e1ef3ed636a24d`
replays the recipe commit onto current accepted source `5534389f`; validation
and both architecture generations passed. Corrected serial exact run
`34703023438` was dispatched at `2026-09-12T15:42:11Z` with `upload_image=false`
and passed. After DQE was accepted, corrected integrated candidate
`ffe5f289da8da47c006835876a86dcd07138b208` replayed the recipe commit onto the
new accepted source; validation and both architecture generations passed, and
serial run `34703327433` was dispatched at `2026-09-12T15:48:19Z` with
`upload_image=false`. It passed with 2 passed, 0 failed, and 0 skipped. The
candidate is accepted at the top-level pin as `ffe5f289da8da47c006835876a86dcd07138b208`;
issue [#79](https://github.com/Vbitz/neurocontainers-arm64/issues/79) records
the exact run, reports, and acceptance evidence.

GingerALE investigation started at `2026-09-12T15:33:56Z` on attempt 1 with a
12-hour deadline of `2026-09-13T03:33:56Z`, from accepted source
`5534389f33c579fc39cb307c43fbf7d30b980478`. Candidate
`aee640961d9c5abab1b9a7257310a75c32b3def8` on `arm64/gingerale` declares
`aarch64`; the recipe runs a portable Java JAR with Ubuntu OpenJDK. Validation
and both architecture generations passed. Exact run `34702611171` was
dispatched at `2026-09-12T15:33:56Z` with `upload_image=false`; it passed with
51 passed, 0 failed, and 0 skipped. The integrated branch
`arm64/integrate-gingerale` replays the recipe commit onto prior accepted source
`5534389f`; serial run `34703078533` passed with the same counts. After DQE was
accepted, corrected integrated candidate
`448b1de188704f7270a16b9217ad28ad38c33f1b` replayed the recipe commit onto the
DQE accepted source; its exact serial run `34703452146` passed with 51 passed,
0 failed, and 0 skipped, but became stale when Template advanced the accepted
pin. Final integrated candidate `7592907bb1caf8c3da996156e87f765a727c8719`
replays the recipe commit onto accepted Template source `ffe5f289`; validation
and both architecture generations passed. Exact serial run `34703768813` was
dispatched at `2026-09-12T15:57:20Z` with `upload_image=false` and is in
progress.

qMRLab investigation started at `2026-09-13T01:58:46Z` on attempt 1 from
accepted source `ffe5f289da8da47c006835876a86dcd07138b208`. Candidate
`bb0992471ae46822b94e8fc8200793f20efd64bf` on `arm64/qmrlab` adds `aarch64`
to the source-based qMRLab 2.4.2 recipe. The Ubuntu 24.04 base installs
Octave and the existing fulltest exercises model listing and instantiation,
synthetic signal simulations, and NIfTI data I/O. Validation and both
architecture generations passed. Candidate `8fdfbd5a814d113d895a8c75a0ad95ca1d7b2873`
on `arm64/integrate-qmrlab-mipview` was based on accepted MipView source and
passed exact native ARM64 run `34705439660` with 51 passed, 0 failed, and 0
skipped. The same one line recipe change was cherry-picked onto the accepted
Sodiumnufft source as `0e0f6329f18d4ff60628dfe2fedf16a8a6f6871b`; local
validation and both architecture generations passed. It is accepted without
another workflow run because the independent recipe result already passed.

MipView investigation started at `2026-09-13T02:15:21Z` on attempt 1 from
accepted source `fd60cfea817a54dd286f386fef251b07d41dc192`. Candidate
`d7de67d4647d4bfb50eb14f799afd34fd57d3c34` on `arm64/mipview` adds `aarch64`
to the source Python/Qt recipe and extends the fulltest with a package import
and synthetic NIfTI construction assertion. Validation and both architecture
generations passed. Exact serial run `34704666186` was dispatched with
`upload_image=false` and is queued.

OpenRecon I2I investigation is prepared from accepted source
`7592907bb1caf8c3da996156e87f765a727c8719`. Final candidate
`fd60cfea817a54dd286f386fef251b07d41dc192` on
`arm64/integrate-openreconi2iexample-gingerale` replays the ARM64 declaration
onto the accepted GingerALE pin. Its pinned Ubuntu 22.04 digest is a native
multi-architecture manifest; validation and both architecture generations
passed. The candidate is pushed. Exact serial run `34704212512` was dispatched
at `2026-09-13T02:06:14Z` with `upload_image=false` and is queued.
The segmentator current-pin recheck on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T10:37:36Z`
as run `34688945692`.
The fitlins verification on accepted source `c6d782cd73cf88ccc44b837f705967b810519086`
started at `2026-09-12T10:40:18Z` as run `34689060946`.
The spmpython verification on accepted source `c6d782cd73cf88ccc44b837f705967b810519086`
started at `2026-09-12T10:44:34Z` as run `34689239216`.
The cosmomvpa verification on accepted source `c6d782cd73cf88ccc44b837f705967b810519086`
started at `2026-09-12T10:48:44Z` as run `34689424126`; irkernel started at
`2026-09-12T10:48:46Z` as run `34689425438`.
The hdbet verification on accepted source `c6d782cd73cf88ccc44b837f705967b810519086`
started at `2026-09-12T10:50:52Z` as run `34689514789`.
The totalsegmentator verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T10:52:07Z`
as run `34689567635`.
The MIPAV verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T10:54:52Z`
as run `34689681947`.
The AMICO verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T10:59:51Z`
as run `34689875666`.
The GLMsingle verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:00:32Z`
as run `34689909788`.
The batchheudiconv verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:03:01Z`
as run `34690023102`.
The BIDSme verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:05:15Z`
as run `34690122795`.
The BLAST-CT verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:08:13Z`
as run `34690252022`.
The Nighres verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:10:34Z`
as run `34690354693`.
The XNAT verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:13:15Z`
as run `34690473020`.
The DAFNE verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:14:17Z`
as run `34690518800`; its native headless GUI startup returned exit 139 after
the other checks passed, and the issue records it as blocked upstream.
The HNN-core verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:18:17Z`
as run `34690701313` and passed 73 tests.
The VesselVio verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:19:45Z`
as run `34690762333` and passed 96 fulltest tests.
The Topaz verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:23:41Z`
as run `34690938300` and passed 126 tests.
The MEDE verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:30:54Z`
as run `34691245302`.
The Builder verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:32:14Z`
as run `34691302636`.
The BIDScoin verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:32:16Z`
as run `34691304372` and passed 96 tests.
The GOUHFI verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:35:39Z`
as run `34691452949`.
The Neurodesktop-lite verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:35:41Z`
as run `34691454730`.
The ProstateFiducialSeg verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:44:19Z`
as run `34691824091`.
The next exact accepted-pin rechecks are `workshopdemo` and `vina`, both using
source `c6d782cd73cf88ccc44b837f705967b810519086`; dispatch them after this
checkpoint commit. `workshopdemo` started at `2026-09-12T11:56:11Z` as run
`34692323241`; `vina` started at `2026-09-12T11:56:13Z` as run `34692325207`.
The next available slot is assigned to the exact `dcm2niix` recheck on the
same source; dispatch it after this checkpoint and record its run ID here.
`dcm2niix` started at `2026-09-12T11:58:00Z` as run `34692396408`.
The next two slots are assigned to exact accepted-pin rechecks for `niimath`
and `niftyreg`; dispatch them after this checkpoint and record their run IDs
here. `niimath` was dispatched at `2026-09-12T11:59:46Z` as run
`34692464125`; `niftyreg` was dispatched at `2026-09-12T11:59:48Z` as run
`34692465359`.

Candidate port ready for dispatch: `brkraw` branch `arm64/brkraw`, candidate
`35e45882` based on accepted source `c6d782cd73cf88ccc44b837f705967b810519086`.
The one-line `aarch64` declaration passed validation and ARM64/x86_64
Dockerfile generation; its exact candidate was dispatched at
`2026-09-12T12:03:28Z` as run `34692637652`.
BrkRaw passed that run with 84 tests and is ready for serial integration.

Brainlife CLI candidate: `brainlifecli` branch
`arm64/brainlifecli`, candidate `5b401fe0` based on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086`. Its one-line `aarch64`
declaration passed validation and ARM64/x86_64 Dockerfile generation; its
integrated commit `f50c2fbc4377e4a19312019488e4323a189ef453` based on accepted
source `35e458827fb6522c147e4bd99121d1ed631dd6f7` was dispatched at
`2026-09-12T12:13:26Z` as run `34693086744`.

The exact accepted-pin rechecks for `dcm2bids` and `niistat` used source
`35e458827fb6522c147e4bd99121d1ed631dd6f7`; both passed. Their issue comments
record the tested source and counts. The HeuDiConv recheck uses the same source
and is still active.
`dcm2bids` started at `2026-09-12T12:15:09Z` as run `34693164459`; `niistat`
started at `2026-09-12T12:15:11Z` as run `34693166308`.
`heudiconv` started at `2026-09-12T12:18:42Z` as run `34693323676` and is in
fulltest.

GIMP started at `2026-09-12T12:24:27Z` as run `34693583287` on attempt 1 with
deadline `2026-09-13T00:24:27Z`. OpenRefine started at `2026-09-12T12:24:30Z`
as run `34693584794` on attempt 1 with deadline `2026-09-13T00:24:30Z`.

The exact accepted-pin checks for `gimp` and `openrefine` used current source
`f50c2fbc4377e4a19312019488e4323a189ef453` and passed. Their issue comments
record the tested source and counts.

The `dwidenoise2` port declared `aarch64` with no other recipe changes.
Validation and ARM64/x86_64 Dockerfile generation passed. Its exact candidate
`fb140e557113c668e65cd86060aa8ab1a8573a6a` passed run `34693799839` and is
now the accepted submodule pin. An invalid unverified ref was dispatched once
and cancelled before source checkout; it produced no build evidence.

GOUHFI attempt 1 failed after the native ARM64 image built because the runner
ran out of disk while exporting the Docker archive; SIF conversion and tests
did not run. Issue [#60](https://github.com/Vbitz/neurocontainers-arm64/issues/60)
records the infrastructure evidence. The single unchanged retry uses current
accepted source `f50c2fbc4377e4a19312019488e4323a189ef453` and will be recorded
here after dispatch.

The retry started at `2026-09-12T12:34:24Z` as run `34694039302`, attempt 2,
with deadline `2026-09-13T00:34:24Z`. It reproduced runner storage exhaustion
at `docker save` (`no space left on device`) after the native ARM64 image built;
SIF conversion and fulltest did not run. The two permitted unchanged attempts
are exhausted; issue #60 records the infrastructure blocker. The prepared `panoptica` candidate
`0e06c16b83f8597d4d68f9496f3f8631e5a56c89` started at `2026-09-12T12:34:26Z`
as run `34694040721`, attempt 1, with deadline `2026-09-13T00:34:26Z`. The
prepared `pcntoolkit` candidate `6d232dc0827985a17117c56a7b19cd199207102b`
started at `2026-09-12T12:34:28Z` as run `34694042021`, attempt 1, with
deadline `2026-09-13T00:34:28Z`.

The meganorm port declares `aarch64` with no other recipe changes. Validation
and ARM64/x86_64 Dockerfile generation passed on branch `arm64/meganorm` at
candidate `f2a8fc485f02fe6c0d40a79e52264330c278b584`, based on accepted source
`a9a30dd5`. A malformed manually reconstructed ref was dispatched as run
`34694862262` and canceled before build; it is not evidence. The exact Git SHA
was then dispatched as run `34694878402` at `2026-09-12T12:52:44Z`.

The panoptica commit was replayed onto accepted source `fb140e55` as
`72dd4d35a21dc701301565c7cc8d8c60afaea542`; validation and both architecture
generations passed. Its first integrated recheck, run `34694351552`, failed
before checkout because the local commit had not yet been published. The exact
commit was then pushed to `arm64/integrate-panoptica` and dispatched as retry
run `34694588175` at `2026-09-12T12:46:21Z`.

The pcntoolkit commit was replayed onto accepted source `fb140e55` as
`94903684137e1f47b8eb69a65525061cfbf1766c`; validation and both architecture
generations passed. Its first integrated recheck, run `34694375047`, failed
before checkout for the same unpublished-commit reason. The exact commit was
then pushed to `arm64/integrate-pcntoolkit` and dispatched as retry run
`34694590006` at `2026-09-12T12:46:24Z`.

Because FSQC advanced the accepted pin to `a9a30dd5`, the Panoptica recipe
commit was replayed onto that current pin as
`9b1f7d7a2c2d3decae0de23cb3bfff124e821e80`; validation and both architecture
generations passed. Its exact serial recheck is run `34694920638`, dispatched
at `2026-09-12T12:53:41Z`.

After accepting Panoptica at `9b1f7d7a`, the PCNtoolkit recipe commit was
replayed onto that current pin as
`70118cbab3e931402a951dae5ba66b63e30f051d`; validation and both architecture
generations passed. Its exact serial recheck is run `34695171335`, dispatched
at `2026-09-12T12:59:37Z`.

After accepting PCNtoolkit at `70118cba`, the verified MeGANorm recipe commit
was replayed onto that current pin as
`31091ade121699a43a8745a2633e325f47c99061`; validation and both architecture
generations passed. Its exact serial recheck is run `34695477795`, dispatched
at `2026-09-12T13:06:01Z`.

FSQC candidate `a9a30dd58530ec002184c2217ba8fcf3ed43c1c5` passed run
`34694302517` with 109 tests and was accepted serially. Its top-level pointer
commit is `64544e7`; the maintained accepted fork branch now points to the same
submodule SHA.

| Recipe | Baseline/source SHA | Fork branch | Run | Issue | Next action |
| --- | --- | --- | --- | --- | --- |
| `dcm2niix` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` (prior `87e1c726`) | pinned accepted branch | [34692396408](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692396408) | [#4](https://github.com/Vbitz/neurocontainers-arm64/issues/4) | verified: 106 passed |
| `niimath` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` (prior `87e1c726`) | pinned accepted branch | [34692464125](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692464125) | [#6](https://github.com/Vbitz/neurocontainers-arm64/issues/6) | verified: 115 passed |
| `niftyreg` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` (prior `87e1c726`) | pinned accepted branch | [34692465359](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692465359) | [#10](https://github.com/Vbitz/neurocontainers-arm64/issues/10) | verified: 89 passed |
| `vina` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` (prior `87e1c726`) | pinned accepted branch | [34692325207](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692325207) | [#3](https://github.com/Vbitz/neurocontainers-arm64/issues/3) | verified: 8 passed |
| `dcm2bids` | accepted source `35e458827fb6522c147e4bd99121d1ed631dd6f7` (prior `87e1c726`) | pinned accepted branch | [34693164459](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693164459) | [#5](https://github.com/Vbitz/neurocontainers-arm64/issues/5) | verified: 61 passed |
| `niistat` | accepted source `35e458827fb6522c147e4bd99121d1ed631dd6f7` (prior `87e1c726`) | pinned accepted branch | [34693166308](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693166308) | [#7](https://github.com/Vbitz/neurocontainers-arm64/issues/7) | verified: 93 passed |
| `heudiconv` | accepted source `35e458827fb6522c147e4bd99121d1ed631dd6f7` (prior `87e1c726`) | pinned accepted branch | [34693323676](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693323676) | [#9](https://github.com/Vbitz/neurocontainers-arm64/issues/9) | verified: 69 passed |
| `gimp` | accepted source `f50c2fbc4377e4a19312019488e4323a189ef453` (prior `87e1c726`) | pinned accepted branch | [34693583287](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693583287) | [#8](https://github.com/Vbitz/neurocontainers-arm64/issues/8) | verified: 7 passed |
| `openrefine` | accepted source `f50c2fbc4377e4a19312019488e4323a189ef453` (prior `87e1c726`) | pinned accepted branch | [34693584794](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693584794) | [#11](https://github.com/Vbitz/neurocontainers-arm64/issues/11) | verified: 2 passed |
| `dwidenoise2` | accepted candidate `fb140e557113c668e65cd86060aa8ab1a8573a6a` based on `f50c2fbc4377e4a19312019488e4323a189ef453` | `arm64/dwidenoise2` | [34693799839](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693799839) | [#61](https://github.com/Vbitz/neurocontainers-arm64/issues/61) | accepted: 5 passed; integrated |
| `panoptica` | serial candidate `9b1f7d7a2c2d3decae0de23cb3bfff124e821e80` based on accepted source `a9a30dd5` (prior integrated candidate `72dd4d35`) | `arm64/integrate-panoptica-fsqc` | prior [34694588175](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694588175), serial [34694920638](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694920638) | [#63](https://github.com/Vbitz/neurocontainers-arm64/issues/63) | in progress: exact serial integration recheck |
| `pcntoolkit` | serial candidate `70118cbab3e931402a951dae5ba66b63e30f051d` based on accepted source `9b1f7d7a` (prior integrated candidate `94903684`) | `arm64/integrate-pcntoolkit-panoptica` | prior [34694590006](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694590006), serial [34695171335](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34695171335) | [#62](https://github.com/Vbitz/neurocontainers-arm64/issues/62) | in progress: exact serial integration recheck |
| `fsqc` | accepted candidate `a9a30dd58530ec002184c2217ba8fcf3ed43c1c5` based on accepted source `fb140e55` | `arm64/fsqc` | [34694302517](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694302517) | [#64](https://github.com/Vbitz/neurocontainers-arm64/issues/64) | accepted: 109 passed; integrated |
| `meganorm` | accepted candidate `31091ade121699a43a8745a2633e325f47c99061` based on accepted source `70118cba` (prior candidate `f2a8fc48`) | `arm64/integrate-meganorm-pcntoolkit` | prior [34694878402](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694878402), serial [34695477795](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34695477795) | [#65](https://github.com/Vbitz/neurocontainers-arm64/issues/65) | accepted: 11 passed; integrated |
| `deepdisco` | accepted candidate `fbce330df22a4152be2a2be2e67ae5e959f8148c` based on accepted source `31091ade121699a43a8745a2633e325f47c99061` | `arm64/deepdisco` | [34696205436](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34696205436) | [#67](https://github.com/Vbitz/neurocontainers-arm64/issues/67) | accepted: 2 passed; integrated |
| `flames` | accepted candidate `1c6bd96c84cd75dc52aae6598cf363e24e7a37aa` based on accepted source `fbce330df22a4152be2a2be2e67ae5e959f8148c` (prior candidate `96144095`) | `arm64/integrate-flames-deepdisco` | prior [34696329756](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34696329756), serial [34696992986](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34696992986) | [#69](https://github.com/Vbitz/neurocontainers-arm64/issues/69) | accepted: 9 passed; integrated |
| `qsmxt` | accepted candidate `56253af124371ff19dd7c82cf97e82a60e10fcaf` based on accepted source `1c6bd96c84cd75dc52aae6598cf363e24e7a37aa` (prior verified `a0c486f7`) | `arm64/integrate-qsmxt-flames` | prior [34696916528](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34696916528), serial [34697632034](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34697632034) | [#68](https://github.com/Vbitz/neurocontainers-arm64/issues/68) | accepted: 9 passed; integrated |
| `mne` | accepted candidate `f8a66f994161507e1399826980f78c90fcec6e19` based on accepted source `56253af1` (prior verified `953c23b9`) | `arm64/integrate-mne-qsmxt` | prior [34696735862](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34696735862), serial [34698033237](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34698033237) | [#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70) | accepted: 6 passed; integrated |
| `mneextended` | candidate `91ac9396f876ee9835d13cb72903ad17a8f95d5a` based on prior accepted source `fbce330d` (prior `108f2d4a`, `f31fde3e`) | `arm64/mneextended` | prior [34697506684](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34697506684), retry [34697784145](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34697784145), ref-failure [34698178019](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34698178019), exact [34698395577](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34698395577) | [#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70) | blocked-upstream: cascading trame constraints (`trame-server<4` required, 4.0.0 installed) |
| `synthstrip` | accepted candidate `e90ee1a49ec687dd8582d10e7fb68546a008ecd4` based on accepted source `15a0dd8e` | `arm64/integrate-synthstrip-current` | exact [34698395635](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34698395635), stale integration [34703210392](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34703210392) | [#72](https://github.com/Vbitz/neurocontainers-arm64/issues/72) | accepted: 70 passed; integrated without duplicate run |
| `synthstroke` | accepted candidate `bb3f660d9c3ec0718df2f558cd15450eaffd8260` based on accepted source `f8a66f99` (prior `9e66780d`) | `arm64/integrate-synthstroke` | ref-failure [34698867860](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34698867860), first exact [34698887077](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34698887077), exact [34699377187](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699377187), serial [34699910413](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699910413) | [#73](https://github.com/Vbitz/neurocontainers-arm64/issues/73) | accepted: 4 passed; integrated at bb3f660d |
| `spinalcordtoolbox` | retry candidate `3dac0979b1d71e7f4a5d2a9e8d5c8dc08e9a5b0` based on accepted source `f8a66f99` (prior `2e72afcc`) | `arm64/spinalcordtoolbox` | first exact [34699323574](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699323574), retry exact [34699607997](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699607997) | [#74](https://github.com/Vbitz/neurocontainers-arm64/issues/74) | blocked-upstream: PyQt5 ARM64 source metadata build terminated with exit 143 after qmake fix |
| `clearswi` | candidate `86c62b327f7ddc784df2eb114f7bdd3f7f8ae091` based on accepted source `f8a66f99` | `arm64/clearswi` | exact [34699875754](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34699875754) | [#75](https://github.com/Vbitz/neurocontainers-arm64/issues/75) | blocked-upstream: Julia LLVM ARM64 `vscale` instruction-selection failure during PackageCompiler sysimage generation |
| `qsmbly` | accepted candidate `fb92480d3132c936de1c3cd4b88cb9e6cc61cb11` based on `bb3f660d` | `arm64/integrate-qsmbly` | ref-failure [34700948284](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34700948284), corrected exact [34701138583](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34701138583), serial [34701432576](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34701432576) | [#76](https://github.com/Vbitz/neurocontainers-arm64/issues/76) | accepted: 2 passed; integrated at fb92480d |
| `vertexwiser` | accepted candidate `5534389f33c579fc39cb307c43fbf7d30b980478` cherry-picked from `881380dbc85bbf7460e8071c1334c9d8ac6c51c5` onto accepted `fb92480d` | `arm64/integrate-vertexwiser` | prior [34701117134](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34701117134), serial [34701810565](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34701810565) | [#77](https://github.com/Vbitz/neurocontainers-arm64/issues/77) | accepted: 10 passed; integrated |
| `deep-quality-estimation` | accepted candidate `46d1a5ae9bb1881b7ecb7d36f41fdff27af5818a` replaying `74dd8ca6` and `891296e9` onto accepted `5534389f` | `arm64/integrate-deep-quality-estimation` | candidate [34702315565](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34702315565), serial [34702770551](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34702770551) | [#78](https://github.com/Vbitz/neurocontainers-arm64/issues/78) | accepted: 11 passed; integrated |
| `template` | accepted candidate `ffe5f289da8da47c006835876a86dcd07138b208` based on accepted source `46d1a5ae` (prior `0d53a8c8`) | `arm64/integrate-template-dqe` | candidate [34702446198](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34702446198), prior serial [34703023438](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34703023438), current serial [34703327433](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34703327433) | [#79](https://github.com/Vbitz/neurocontainers-arm64/issues/79) | accepted: 2 passed; integrated |
| `qmrlab` | accepted candidate `0e0f6329f18d4ff60628dfe2fedf16a8a6f6871b` based on accepted source `9602df1a` | `arm64/integrate-qmrlab-sodiumnufft` | exact [34705439660](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34705439660) | [#81](https://github.com/Vbitz/neurocontainers-arm64/issues/81) | accepted: 51 passed; integrated |
| `mipview` | accepted candidate `d7de67d4647d4bfb50eb14f799afd34fd57d3c34` based on accepted source `fd60cfea` | `arm64/mipview` | serial [34704666186](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34704666186) | [#83](https://github.com/Vbitz/neurocontainers-arm64/issues/83) | accepted: 4 passed; integrated |
| `openreconi2iexample` | accepted candidate `fd60cfea817a54dd286f386fef251b07d41dc192` based on accepted source `7592907b` (prior `56f4fe3`) | `arm64/integrate-openreconi2iexample-gingerale` | serial [34704212512](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34704212512) | [#82](https://github.com/Vbitz/neurocontainers-arm64/issues/82) | accepted: 5 passed; integrated |
| `gingerale` | accepted candidate `7592907bb1caf8c3da996156e87f765a727c8719` based on accepted source `ffe5f289` (prior `448b1de1`) | `arm64/integrate-gingerale-template` | candidate [34702611171](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34702611171), prior serial [34703078533](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34703078533), stale serial [34703452146](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34703452146), final serial [34703768813](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34703768813) | [#80](https://github.com/Vbitz/neurocontainers-arm64/issues/80) | accepted: 51 passed; integrated |
| `sodiumgridding` | accepted candidate `cd7950c00e93503648e96270f58104fae11f5718` based on accepted source `d7de67d4` | `arm64/sodiumgridding` | exact [34705231419](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34705231419) | [#84](https://github.com/Vbitz/neurocontainers-arm64/issues/84) | accepted: 7 passed; integrated |
| `sodiumnufft` | accepted candidate `9602df1a290918704615776c8c52916c374fd0c4` based on accepted source `cd7950c0` | `arm64/integrate-sodiumnufft-sodiumgridding` | exact [34705290732](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34705290732) | [#85](https://github.com/Vbitz/neurocontainers-arm64/issues/85) | accepted: 5 passed; integrated |
| `epirecon` | accepted candidate `89d8112a1b8b7f2c4bca58e61be30e72d7790f26` based on accepted source `0e0f6329` | `arm64/integrate-epirecon-qmrlab` | exact [34705779719](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34705779719) | [#86](https://github.com/Vbitz/neurocontainers-arm64/issues/86) | accepted: 7 passed; integrated |
| `sodiumgriddingptpi` | accepted candidate `15a0dd8efbaf96fe820c8f09658aea41629f805b` based on accepted source `89d8112a` | `arm64/integrate-sodiumgriddingptpi-epirecon` | exact [34705851195](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34705851195) | [#87](https://github.com/Vbitz/neurocontainers-arm64/issues/87) | accepted: 7 passed; integrated |
| `palm` | accepted candidate `6fe8f9f21abbb8ad7058b6bc26eef81b9b39db85` based on accepted source `e90ee1a4` | `arm64/integrate-palm-synthstrip` | exact [34706614272](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34706614272) | [#88](https://github.com/Vbitz/neurocontainers-arm64/issues/88) | accepted: 56 passed; integrated |
| `wftfi` | accepted candidate `9a383b0d951f71725f2a2dade16a12e372bd6253` based on accepted source `6fe8f9f2` | `arm64/wftfi` | exact [34707462294](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34707462294) | [#89](https://github.com/Vbitz/neurocontainers-arm64/issues/89) | accepted: 21 passed; integrated by ancestry |
| `openreconexample` | candidate `2eaed2732a85fa475cb823a336c62f682b8df90b` based on accepted source `9a383b0d` | `arm64/openreconexample` | cancelled ref [34708172513](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34708172513); exact [34708194854](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34708194854) | pending workflow issue | in progress |
| `blochsiegertb1mapping` | candidate `93a11a16885aec3a548584bb9f3f332fe726df1b` based on accepted source `9a383b0d` | `arm64/blochsiegertb1mapping` | queued [34708203749](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34708203749) | pending workflow issue | in progress |
| `ants` | candidate `f48620a9503c3f532fa16c1b1e9ccc96778a86c6` based on accepted source `e90ee1a4` | `arm64/ants` | exact [34706765954](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34706765954) | pending workflow issue | in progress |
| `openadscpu` | accepted source `70118cba`; no candidate | preflight | no run | [#66](https://github.com/Vbitz/neurocontainers-arm64/issues/66) | blocked-upstream: pinned antspyx 0.5.4 has no Linux ARM64 wheel; revisit on upstream ARM64 support |
| `julia` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685647289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685647289) | [#17](https://github.com/Vbitz/neurocontainers-arm64/issues/17) | verified: 137 passed; retain as accepted pin evidence |
| `apptainer` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685647267](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685647267) | [#15](https://github.com/Vbitz/neurocontainers-arm64/issues/15) | verified: 6 passed; retain as accepted pin evidence |
| `datalad` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685666449](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685666449) | [#12](https://github.com/Vbitz/neurocontainers-arm64/issues/12) | verified: 10 passed; retain as accepted pin evidence |
| `mricron` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685692303](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685692303) | [#13](https://github.com/Vbitz/neurocontainers-arm64/issues/13) | verified: 105 passed; retain as accepted pin evidence |
| `libreoffice` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685794423](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685794423) | [#16](https://github.com/Vbitz/neurocontainers-arm64/issues/16) | verified: 3 passed; retain as accepted pin evidence |
| `globus` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | `arm64/globus` | [34686096832](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686096832) | [#14](https://github.com/Vbitz/neurocontainers-arm64/issues/14) | verified; integrated into top-level pin |
| `bidstools` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | pinned accepted branch | baseline [34686282914](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686282914); accepted [34686613888](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686613888) | [#20](https://github.com/Vbitz/neurocontainers-arm64/issues/20) | verified: 12 passed |
| `dicompare` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | pinned accepted branch | baseline [34686283152](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686283152); accepted [34686615747](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686615747) | [#19](https://github.com/Vbitz/neurocontainers-arm64/issues/19) | verified: 105 passed |
| `eharmonize` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` (baseline `87e1c726`) | pinned accepted branch | baseline [34686283058](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686283058); accepted [34686618053](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686618053) | [#18](https://github.com/Vbitz/neurocontainers-arm64/issues/18) | verified: 6 passed |
| `afib1` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34686701687](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686701687) | [#21](https://github.com/Vbitz/neurocontainers-arm64/issues/21) | verified: 5 passed |
| `arfiproc` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34686847933](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686847933) | [#22](https://github.com/Vbitz/neurocontainers-arm64/issues/22) | verified: 6 passed |
| `b0map` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34686964891](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34686964891) | [#23](https://github.com/Vbitz/neurocontainers-arm64/issues/23) | verified: 8 passed |
| `bidsmanager` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34687075563](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34687075563) | [#24](https://github.com/Vbitz/neurocontainers-arm64/issues/24) | verified: 9 passed |
| `cbsb0stats` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34687077011](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34687077011) | [#25](https://github.com/Vbitz/neurocontainers-arm64/issues/25) | verified: 6 passed |
| `functionnectome` | `7bd4f9ee9734c4dd3a449290c39955f009f081d3` | pinned accepted branch | [34687208365](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34687208365) | [#26](https://github.com/Vbitz/neurocontainers-arm64/issues/26) | verified: 4 passed |
| `dicomtools` | `e430edb9d9a595878a619cb4bb00a68056665daf` | `arm64/dicomtools` | [34687413104](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34687413104) | [#27](https://github.com/Vbitz/neurocontainers-arm64/issues/27) | verified: 179 passed; integrated into accepted pin |
| `rapidtide` | `c6d782cd73cf88ccc44b837f705967b810519086` | `arm64/dicomtools` | [34688458132](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34688458132) | [#30](https://github.com/Vbitz/neurocontainers-arm64/issues/30) | verified: 5 passed; integrated into accepted pin |
| `radtract` | `031ff4750b9097aa0a552eb2efcccef00ab38a3b` | `arm64/dicomtools` | [34687953581](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34687953581) | [#29](https://github.com/Vbitz/neurocontainers-arm64/issues/29) | verified: 3 passed; integrated into accepted pin |
| `lqt` | accepted pin `031ff4750b9097aa0a552eb2efcccef00ab38a3b` | pinned accepted branch | [34688683840](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34688683840) | [#28](https://github.com/Vbitz/neurocontainers-arm64/issues/28) | verified: 6 passed |
| `segmentator` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34688945692](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34688945692) | [#31](https://github.com/Vbitz/neurocontainers-arm64/issues/31) | verified: 5 passed |
| `spant` | accepted pin `031ff4750b9097aa0a552eb2efcccef00ab38a3b` | pinned accepted branch | [34688352312](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34688352312) | [#34](https://github.com/Vbitz/neurocontainers-arm64/issues/34) | verified: 2 passed |
| `condaenvs` | accepted pin `031ff4750b9097aa0a552eb2efcccef00ab38a3b` | pinned accepted branch | [34688353976](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34688353976) | [#32](https://github.com/Vbitz/neurocontainers-arm64/issues/32) | verified: 3 passed |
| `fitlins` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689060946](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689060946) | [#33](https://github.com/Vbitz/neurocontainers-arm64/issues/33) | verified: 7 passed |
| `spmpython` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689239216](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689239216) | [#35](https://github.com/Vbitz/neurocontainers-arm64/issues/35) | verified: 82 passed |
| `cosmomvpa` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689424126](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689424126) | [#36](https://github.com/Vbitz/neurocontainers-arm64/issues/36) | verified: 6 passed |
| `irkernel` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689425438](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689425438) | [#37](https://github.com/Vbitz/neurocontainers-arm64/issues/37) | verified: 5 passed |
| `hdbet` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689514789](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689514789) | [#40](https://github.com/Vbitz/neurocontainers-arm64/issues/40) | verified: 6 passed |
| `totalsegmentator` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689567635](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689567635) | [#39](https://github.com/Vbitz/neurocontainers-arm64/issues/39) | verified: 3 passed |
| `mipav` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689681947](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689681947) | [#38](https://github.com/Vbitz/neurocontainers-arm64/issues/38) | verified: 7 passed |
| `amico` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689875666](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689875666) | [#41](https://github.com/Vbitz/neurocontainers-arm64/issues/41) | verified: 75 passed |
| `glmsingle` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34689909788](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34689909788) | [#43](https://github.com/Vbitz/neurocontainers-arm64/issues/43) | verified: 77 passed |
| `batchheudiconv` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690023102](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690023102) | [#42](https://github.com/Vbitz/neurocontainers-arm64/issues/42) | verified: 108 passed |
| `bidsme` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690122795](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690122795) | [#44](https://github.com/Vbitz/neurocontainers-arm64/issues/44) | verified: 82 passed |
| `blastct` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690252022](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690252022) | [#45](https://github.com/Vbitz/neurocontainers-arm64/issues/45) | verified: 6 passed |
| `nighres` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690354693](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690354693) | [#47](https://github.com/Vbitz/neurocontainers-arm64/issues/47) | verified: 70 passed |
| `xnat` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690473020](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690473020) | [#46](https://github.com/Vbitz/neurocontainers-arm64/issues/46) | verified: 99 passed |
| `workshopdemo` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` (prior `87e1c726`) | pinned accepted branch | [34692323241](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692323241) | [#1](https://github.com/Vbitz/neurocontainers-arm64/issues/1) | verified: 4 passed |
| `dafne` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690518800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690518800) | [#48](https://github.com/Vbitz/neurocontainers-arm64/issues/48) | blocked-upstream: headless GUI exit 139; revisit only with a direct upstream fix |
| `hnncore` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690701313](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690701313) | [#49](https://github.com/Vbitz/neurocontainers-arm64/issues/49) | verified: 73 passed |
| `vesselvio` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690762333](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690762333) | [#50](https://github.com/Vbitz/neurocontainers-arm64/issues/50) | verified: 96 passed |
| `topaz` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690938300](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690938300) | [#55](https://github.com/Vbitz/neurocontainers-arm64/issues/55) | verified: 126 passed |
| `mede` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691245302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691245302) | [#52](https://github.com/Vbitz/neurocontainers-arm64/issues/52) | verified: 2 passed |
| `builder` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691302636](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691302636) | [#51](https://github.com/Vbitz/neurocontainers-arm64/issues/51) | verified: 1 passed |
| `bidscoin` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691304372](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691304372) | [#54](https://github.com/Vbitz/neurocontainers-arm64/issues/54) | verified: 96 passed |
| `gouhfi` | retry source `f50c2fbc4377e4a19312019488e4323a189ef453` (attempt 1 source `c6d782cd`) | pinned accepted branch | [34694039302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34694039302) | [#60](https://github.com/Vbitz/neurocontainers-arm64/issues/60) | blocked-infrastructure: two docker export attempts exhausted runner disk |
| `neurodesktop-lite` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691454730](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691454730) | [#56](https://github.com/Vbitz/neurocontainers-arm64/issues/56) | blocked-upstream: jupyterlab-slurm frontend metadata mismatch |
| `prostatefiducialseg` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691824091](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691824091) | [#57](https://github.com/Vbitz/neurocontainers-arm64/issues/57) | verified: 4 passed |
| `brkraw` | accepted source `35e458827fb6522c147e4bd99121d1ed631dd6f7` (prior `c6d782cd`) | `arm64/brkraw` | [34692637652](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692637652) | [#58](https://github.com/Vbitz/neurocontainers-arm64/issues/58) | accepted: 84 passed |
| `brainlifecli` | accepted source `f50c2fbc4377e4a19312019488e4323a189ef453` (prior `35e45882`) | `arm64/brainlifecli-on-brkraw` | [34693086744](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34693086744) | [#59](https://github.com/Vbitz/neurocontainers-arm64/issues/59) | accepted: 74 passed |
| `tinyrange` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | preflight on accepted branch | no run | [#53](https://github.com/Vbitz/neurocontainers-arm64/issues/53) | blocked-prerequisite: essential fulltest requires QEMU |

## Verified results

- `dcm2niix` / `arm64`: run `34692396408`, source `c6d782cd`, 106 passed, 0 failed, 0 skipped; issue [#4](https://github.com/Vbitz/neurocontainers-arm64/issues/4).
- `vina` / `arm64`: run `34692325207`, source `c6d782cd`, 8 passed, 0 failed, 0 skipped; issue [#3](https://github.com/Vbitz/neurocontainers-arm64/issues/3).
- `dcm2bids` / `arm64`: run `34693164459`, source `35e45882`, 61 passed, 0 failed, 0 skipped; issue [#5](https://github.com/Vbitz/neurocontainers-arm64/issues/5).
- `niimath` / `arm64`: run `34692464125`, source `c6d782cd`, 115 passed, 0 failed, 0 skipped; issue [#6](https://github.com/Vbitz/neurocontainers-arm64/issues/6).
- `niistat` / `arm64`: accepted-pin run `34693166308`, source `35e45882`, 93 passed, 0 failed, 0 skipped; issue [#7](https://github.com/Vbitz/neurocontainers-arm64/issues/7). This supersedes the earlier source `87e1c726` check.
- `niftyreg` / `arm64`: run `34692465359`, source `c6d782cd`, 89 passed, 0 failed, 0 skipped; issue [#10](https://github.com/Vbitz/neurocontainers-arm64/issues/10).
- `heudiconv` / `arm64`: accepted-pin run `34693323676`, source `35e45882`, 69 passed, 0 failed, 0 skipped; issue [#9](https://github.com/Vbitz/neurocontainers-arm64/issues/9). This supersedes the earlier source `87e1c726` check.
- `gimp` / `arm64`: accepted-pin run `34693583287`, source `f50c2fbc`, 7 passed, 0 failed, 0 skipped; issue [#8](https://github.com/Vbitz/neurocontainers-arm64/issues/8). This supersedes the earlier source `87e1c726` check.
- `openrefine` / `arm64`: accepted-pin run `34693584794`, source `f50c2fbc`, 2 passed, 0 failed, 0 skipped; issue [#11](https://github.com/Vbitz/neurocontainers-arm64/issues/11). This supersedes the earlier source `87e1c726` check.
- `datalad` / `arm64`: run `34685666449`, source `87e1c726`, 10 passed, 0 failed, 0 skipped; issue [#12](https://github.com/Vbitz/neurocontainers-arm64/issues/12).
- `mricron` / `arm64`: run `34685692303`, source `87e1c726`, 105 passed, 0 failed, 0 skipped; issue [#13](https://github.com/Vbitz/neurocontainers-arm64/issues/13).
- `julia` / `arm64`: run `34685647289`, source `87e1c726`, 137 passed, 0 failed, 0 skipped; issue [#17](https://github.com/Vbitz/neurocontainers-arm64/issues/17).
- `apptainer` / `arm64`: run `34685647267`, source `87e1c726`, 6 passed, 0 failed, 0 skipped; issue [#15](https://github.com/Vbitz/neurocontainers-arm64/issues/15).
- `libreoffice` / `arm64`: run `34685794423`, source `87e1c726`, 3 passed, 0 failed, 0 skipped; issue [#16](https://github.com/Vbitz/neurocontainers-arm64/issues/16).
- `globus` / `arm64`: run `34686096832`, source `7bd4f9ee`, 72 passed, 0 failed, 0 skipped; issue [#14](https://github.com/Vbitz/neurocontainers-arm64/issues/14).
- `bidstools` / `arm64`: accepted-pin run `34686613888`, source `7bd4f9ee`, 12 passed, 0 failed, 0 skipped; issue [#20](https://github.com/Vbitz/neurocontainers-arm64/issues/20).
- `dicompare` / `arm64`: accepted-pin run `34686615747`, source `7bd4f9ee`, 105 passed, 0 failed, 0 skipped; issue [#19](https://github.com/Vbitz/neurocontainers-arm64/issues/19).
- `eharmonize` / `arm64`: accepted-pin run `34686618053`, source `7bd4f9ee`, 6 passed, 0 failed, 0 skipped; issue [#18](https://github.com/Vbitz/neurocontainers-arm64/issues/18).
- `afib1` / `arm64`: accepted-pin run `34686701687`, source `7bd4f9ee`, 5 passed, 0 failed, 0 skipped; issue [#21](https://github.com/Vbitz/neurocontainers-arm64/issues/21).
- `arfiproc` / `arm64`: accepted-pin run `34686847933`, source `7bd4f9ee`, 6 passed, 0 failed, 0 skipped; issue [#22](https://github.com/Vbitz/neurocontainers-arm64/issues/22).
- `b0map` / `arm64`: accepted-pin run `34686964891`, source `7bd4f9ee`, 8 passed, 0 failed, 0 skipped; issue [#23](https://github.com/Vbitz/neurocontainers-arm64/issues/23).
- `bidsmanager` / `arm64`: accepted-pin run `34687075563`, source `7bd4f9ee`, 9 passed, 0 failed, 0 skipped; issue [#24](https://github.com/Vbitz/neurocontainers-arm64/issues/24).
- `cbsb0stats` / `arm64`: accepted-pin run `34687077011`, source `7bd4f9ee`, 6 passed, 0 failed, 0 skipped; issue [#25](https://github.com/Vbitz/neurocontainers-arm64/issues/25).
- `functionnectome` / `arm64`: accepted-pin run `34687208365`, source `7bd4f9ee`, 4 passed, 0 failed, 0 skipped; issue [#26](https://github.com/Vbitz/neurocontainers-arm64/issues/26).
- `dicomtools` / `arm64`: run `34687413104`, candidate source `e430edb9`, 179 passed, 0 failed, 0 skipped; issue [#27](https://github.com/Vbitz/neurocontainers-arm64/issues/27).
- `radtract` / `arm64`: run `34687953581`, integrated source `031ff475`, 3 passed, 0 failed, 0 skipped; issue [#29](https://github.com/Vbitz/neurocontainers-arm64/issues/29).
- `rapidtide` / `arm64`: run `34688458132`, integrated source `c6d782cd`, 5 passed, 0 failed, 0 skipped; issue [#30](https://github.com/Vbitz/neurocontainers-arm64/issues/30).
- `segmentator` / `arm64`: run `34688945692`, source `c6d782cd`, 5 passed, 0 failed, 0 skipped; issue [#31](https://github.com/Vbitz/neurocontainers-arm64/issues/31).
- `lqt` / `arm64`: run `34688683840`, source `031ff475`, 6 passed, 0 failed, 0 skipped; issue [#28](https://github.com/Vbitz/neurocontainers-arm64/issues/28).
- `fitlins` / `arm64`: run `34689060946`, source `c6d782cd`, 7 passed, 0 failed, 0 skipped; issue [#33](https://github.com/Vbitz/neurocontainers-arm64/issues/33).
- `spant` / `arm64`: run `34688352312`, source `031ff475`, 2 passed, 0 failed, 0 skipped; issue [#34](https://github.com/Vbitz/neurocontainers-arm64/issues/34).
- `spmpython` / `arm64`: run `34689239216`, source `c6d782cd`, 82 passed, 0 failed, 0 skipped; issue [#35](https://github.com/Vbitz/neurocontainers-arm64/issues/35).
- `cosmomvpa` / `arm64`: run `34689424126`, source `c6d782cd`, 6 passed, 0 failed, 0 skipped; issue [#36](https://github.com/Vbitz/neurocontainers-arm64/issues/36).
- `condaenvs` / `arm64`: run `34688353976`, source `031ff475`, 3 passed, 0 failed, 0 skipped; issue [#32](https://github.com/Vbitz/neurocontainers-arm64/issues/32).
- `irkernel` / `arm64`: run `34689425438`, source `c6d782cd`, 5 passed, 0 failed, 0 skipped; issue [#37](https://github.com/Vbitz/neurocontainers-arm64/issues/37).
- `mipav` / `arm64`: run `34689681947`, source `c6d782cd`, 7 passed, 0 failed, 0 skipped; issue [#38](https://github.com/Vbitz/neurocontainers-arm64/issues/38).
- `totalsegmentator` / `arm64`: run `34689567635`, source `c6d782cd`, 3 passed, 0 failed, 0 skipped; issue [#39](https://github.com/Vbitz/neurocontainers-arm64/issues/39).
- `hdbet` / `arm64`: run `34689514789`, source `c6d782cd`, 6 passed, 0 failed, 0 skipped; issue [#40](https://github.com/Vbitz/neurocontainers-arm64/issues/40).
- `amico` / `arm64`: run `34689875666`, source `c6d782cd`, 75 passed, 0 failed, 0 skipped; issue [#41](https://github.com/Vbitz/neurocontainers-arm64/issues/41).
- `batchheudiconv` / `arm64`: run `34690023102`, source `c6d782cd`, 108 passed, 0 failed, 0 skipped; issue [#42](https://github.com/Vbitz/neurocontainers-arm64/issues/42).
- `glmsingle` / `arm64`: run `34689909788`, source `c6d782cd`, 77 passed, 0 failed, 0 skipped; issue [#43](https://github.com/Vbitz/neurocontainers-arm64/issues/43).
- `bidsme` / `arm64`: run `34690122795`, source `c6d782cd`, 82 passed, 0 failed, 0 skipped; issue [#44](https://github.com/Vbitz/neurocontainers-arm64/issues/44).
- `blastct` / `arm64`: run `34690252022`, source `c6d782cd`, 6 passed, 0 failed, 0 skipped; issue [#45](https://github.com/Vbitz/neurocontainers-arm64/issues/45).
- `xnat` / `arm64`: run `34690473020`, source `c6d782cd`, 99 passed, 0 failed, 0 skipped; issue [#46](https://github.com/Vbitz/neurocontainers-arm64/issues/46).
- `nighres` / `arm64`: run `34690354693`, source `c6d782cd`, 70 passed, 0 failed, 0 skipped; issue [#47](https://github.com/Vbitz/neurocontainers-arm64/issues/47).
- `vesselvio` / `arm64`: run `34690762333`, source `c6d782cd`, 96 passed, 0 failed, 0 skipped; issue [#50](https://github.com/Vbitz/neurocontainers-arm64/issues/50).
- `builder` / `arm64`: run `34691302636`, source `c6d782cd`, 1 passed, 0 failed, 0 skipped; issue [#51](https://github.com/Vbitz/neurocontainers-arm64/issues/51).
- `mede` / `arm64`: run `34691245302`, source `c6d782cd`, 2 passed, 0 failed, 0 skipped; issue [#52](https://github.com/Vbitz/neurocontainers-arm64/issues/52).
- `bidscoin` / `arm64`: run `34691304372`, source `c6d782cd`, 96 passed, 0 failed, 0 skipped; issue [#54](https://github.com/Vbitz/neurocontainers-arm64/issues/54).
- `workshopdemo` / `arm64`: run `34692323241`, source `c6d782cd`, 4 passed, 0 failed, 0 skipped; issue [#1](https://github.com/Vbitz/neurocontainers-arm64/issues/1).
- `topaz` / `arm64`: run `34690938300`, source `c6d782cd`, 126 passed, 0 failed, 0 skipped; issue [#55](https://github.com/Vbitz/neurocontainers-arm64/issues/55).

- `hnncore` / `arm64`: run `34690701313`, source `c6d782cd`, 73 passed, 0 failed, 0 skipped; issue [#49](https://github.com/Vbitz/neurocontainers-arm64/issues/49).
- `prostatefiducialseg` / `arm64`: run `34691824091`, source `c6d782cd`, 4 passed, 0 failed, 0 skipped; issue [#57](https://github.com/Vbitz/neurocontainers-arm64/issues/57).
- `brkraw` / `arm64`: run `34692637652`, accepted source `35e45882`, 84 passed, 0 failed, 0 skipped; issue [#58](https://github.com/Vbitz/neurocontainers-arm64/issues/58). Candidate is integrated into the accepted pin.
- `brainlifecli` / `arm64`: run `34693086744`, accepted source `f50c2fbc`, 74 passed, 0 failed, 0 skipped; issue [#59](https://github.com/Vbitz/neurocontainers-arm64/issues/59). Candidate is integrated into the accepted pin.
- `dwidenoise2` / `arm64`: run `34693799839`, accepted source `fb140e55`, 5 passed, 0 failed, 0 skipped; issue [#61](https://github.com/Vbitz/neurocontainers-arm64/issues/61). Candidate is integrated into the accepted pin.
- `fsqc` / `arm64`: run `34694302517`, accepted source `a9a30dd5`, 109 passed, 0 failed, 0 skipped; issue [#64](https://github.com/Vbitz/neurocontainers-arm64/issues/64). Candidate is integrated into the accepted pin.
- `meganorm` / `arm64`: run `34695477795`, accepted source `31091ade`, 11 passed, 0 failed, 0 skipped; issue [#65](https://github.com/Vbitz/neurocontainers-arm64/issues/65). Candidate is integrated into the accepted pin.
- `deepdisco` / `arm64`: run `34696205436`, accepted source `fbce330d`, 2 passed, 0 failed, 0 skipped; issue [#67](https://github.com/Vbitz/neurocontainers-arm64/issues/67). Candidate is integrated into the accepted pin.
- `flames` / `arm64`: run `34696992986`, accepted source `1c6bd96c`, 9 passed, 0 failed, 0 skipped; issue [#69](https://github.com/Vbitz/neurocontainers-arm64/issues/69). Candidate is integrated into the accepted pin.
- `qsmxt` / `arm64`: serial run `34697632034`, accepted source `56253af1`, 9 passed, 0 failed, 0 skipped; issue [#68](https://github.com/Vbitz/neurocontainers-arm64/issues/68). Candidate is integrated into the accepted pin.
- `mne` / `arm64`: serial run `34698033237`, accepted source `f8a66f99`, 6 passed, 0 failed, 0 skipped; issue [#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70). Candidate is integrated into the accepted pin.
- `wftfi` / `arm64`: run `34707462294`, accepted source `9a383b0d`, 21 passed, 0 failed, 0 skipped; issue [#89](https://github.com/Vbitz/neurocontainers-arm64/issues/89). Candidate is integrated into the accepted pin by direct ancestry.

## Blocked or failed results

- `dafne` / `arm64`: run `34690518800`, source `c6d782cd`, 10 passed and 1 failed in the fulltest runner; native headless GUI startup exited 139. Issue [#48](https://github.com/Vbitz/neurocontainers-arm64/issues/48) records the upstream blocker and revisit condition.
- `tinyrange` / `arm64`: no run; validation and both architecture generations passed, but its essential fulltest requires QEMU. Issue [#53](https://github.com/Vbitz/neurocontainers-arm64/issues/53) records the prerequisite blocker.
- `neurodesktop-lite` / `arm64`: run `34691454730`, source `c6d782cd`, build failed before SIF conversion and fulltest because the pinned `jupyterlab-slurm` source could not resolve `@jupyterlab/core-meta` 4.0.x. Issue [#56](https://github.com/Vbitz/neurocontainers-arm64/issues/56) records the upstream blocker.
- `openadscpu` / `arm64`: no run; the pinned `antspyx==0.5.4` release has no Linux ARM64 wheel, so a supported result would require porting that native dependency. Issue [#66](https://github.com/Vbitz/neurocontainers-arm64/issues/66) records the preflight blocker.
- `gouhfi` / `arm64`: runs `34691452949` and `34694039302` both built the native ARM64 image but failed exporting it with `no space left on device`; SIF conversion and fulltest did not run. Issue [#60](https://github.com/Vbitz/neurocontainers-arm64/issues/60) records the exhausted unchanged retry and revisit condition.
- `mneextended` / `arm64`: exact run `34698395577`, candidate `91ac9396`, reached the native ARM64 Docker build but failed before SIF conversion and fulltest. After the pyedflib wheel and `trame-client<4` fix, `pip check` reported `trame 3.13.2` requires `trame-server<4,>=3.12.2` while `trame-server 4.0.0` is installed. Issue [#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70) records the three-attempt investigation and upstream blocker.
- `spinalcordtoolbox` / `arm64`: exact retry `34699607997`, candidate `3dac0979`, installed qmake and resolved ARM64 packages but the pinned PyQt5 5.15.11 source metadata build was terminated with exit 143 after about 13 minutes. Issue [#74](https://github.com/Vbitz/neurocontainers-arm64/issues/74) records the two-attempt upstream blocker and revisit condition.
- `clearswi` / `arm64`: exact run `34699875754`, candidate `86c62b32`, installed and precompiled the Julia dependency set but failed during PackageCompiler sysimage generation with the ARM64 LLVM `vscale` instruction-selection error in `HostCPUFeatures`. No SIF or fulltest ran. Issue [#75](https://github.com/Vbitz/neurocontainers-arm64/issues/75) records the upstream blocker and revisit condition.

## Integration

- Accepted integration SHA: `9a383b0d951f71725f2a2dade16a12e372bd6253`
- Top-level submodule pointer accepts the tested MNE, SynthStroke, QSMbly,
  VertexWiseR, Deep Quality Estimation, Template, GingerALE, OpenRecon I2I,
  MipView, Sodiumgridding, Sodiumnufft, qMRLab, Epirecon, Sodiumgriddingptpi,
  SynthStrip, PALM, and wfTFI integrations. The earlier SynthStrip exact candidate run
  passed and was integrated by ancestry; its stale duplicate integration run
  also passed 70 tests and is bookkeeping only. PALM is integrated; ANTs has an exact
  native ARM64 run in progress.
  CLEARSWI and Spinal Cord Toolbox are blocked upstream;
  MNEextended is blocked
  by cascading trame dependency constraints. BrkRaw, Brainlife CLI, dicomtools, radtract,
  rapidtide, dwidenoise2, FSQC, Panoptica, PCNtoolkit, MeGANorm, DeepDisco, and
  FLAMeS remain included.

## Next action

Issue [#2](https://github.com/Vbitz/neurocontainers-arm64/issues/2) was refreshed
from accepted source `9a383b0d`. Exact native runs are dispatched for
`openreconexample` candidate `2eaed2732a85fa475cb823a336c62f682b8df90b` and
`blochsiegertb1mapping` candidate `93a11a16885aec3a548584bb9f3f332fe726df1b`;
monitor runs `34708194854` and `34708203749` alongside ANTs run `34706765954`.
The stale
SynthStrip run `34703210392` completed successfully and needs bookkeeping only.
Record reports and integrate passing tested commits serially; the OpenRecon
candidates descend from the current accepted pin and need no duplicate native
integration run, while ANTs is based on an older source and needs one exact
integrated recheck if it passes. Classify the first actionable error within
each recorded budget if a run fails, then continue screening the next eligible
undeclared recipe.
