# ARM64 porting checkpoint

Updated: 2026-09-12 (Australia/Brisbane)

## Current state

- Top-level branch: `main`
- Top-level commit: `2803f8da6264ec7e35c96a9466c00243cf6b8298`
- Pinned submodule: `neurocontainers@c6d782cd73cf88ccc44b837f705967b810519086`
- Submodule checkout: `arm64/dicomtools`, clean, origin `Vbitz/neurocontainers`
- Fork Actions: disabled (`enabled: false`)
- Existing verified pipeline check: `workshopdemo` / `arm64`, run [34684189569](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34684189569), 4 passed, source `87e1c726`
- Coverage snapshot: 57 of 247 recipes declare ARM64 support at accepted source `c6d782cd`; the tracker is issue [#2](https://github.com/Vbitz/neurocontainers-arm64/issues/2)

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
as run `34690938300`.
The MEDE verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:30:54Z`
as run `34691245302`.
The Builder verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:32:14Z`
as run `34691302636`.
The BIDScoin verification on accepted source
`c6d782cd73cf88ccc44b837f705967b810519086` started at `2026-09-12T11:32:16Z`
as run `34691304372`.

| Recipe | Baseline/source SHA | Fork branch | Run | Issue | Next action |
| --- | --- | --- | --- | --- | --- |
| `dcm2niix` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110310](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110310) | [#4](https://github.com/Vbitz/neurocontainers-arm64/issues/4) | verified: 106 passed; retain as accepted pin evidence |
| `niimath` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110419](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110419) | [#6](https://github.com/Vbitz/neurocontainers-arm64/issues/6) | verified: 115 passed; retain as accepted pin evidence |
| `niftyreg` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110299](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110299) | [#10](https://github.com/Vbitz/neurocontainers-arm64/issues/10) | verified: 89 passed; retain as accepted pin evidence |
| `vina` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685110418](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685110418) | [#3](https://github.com/Vbitz/neurocontainers-arm64/issues/3) | verified: 8 passed; retain as accepted pin evidence |
| `dcm2bids` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685269662](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685269662) | [#5](https://github.com/Vbitz/neurocontainers-arm64/issues/5) | verified: 61 passed; retain as accepted pin evidence |
| `niistat` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685269554](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685269554) | [#7](https://github.com/Vbitz/neurocontainers-arm64/issues/7) | verified: 93 passed; retain as accepted pin evidence |
| `heudiconv` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685389090](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685389090) | [#9](https://github.com/Vbitz/neurocontainers-arm64/issues/9) | verified: 69 passed; retain as accepted pin evidence |
| `gimp` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685484205](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685484205) | [#8](https://github.com/Vbitz/neurocontainers-arm64/issues/8) | verified: 7 passed; retain as accepted pin evidence |
| `openrefine` | `87e1c7265e8b6c767cd3154c67caca984116711e` | pinned `main` | [34685556897](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34685556897) | [#11](https://github.com/Vbitz/neurocontainers-arm64/issues/11) | verified: 2 passed; retain as accepted pin evidence |
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
| `dafne` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690518800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690518800) | [#48](https://github.com/Vbitz/neurocontainers-arm64/issues/48) | blocked-upstream: headless GUI exit 139; revisit only with a direct upstream fix |
| `hnncore` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690701313](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690701313) | [#49](https://github.com/Vbitz/neurocontainers-arm64/issues/49) | verified: 73 passed |
| `vesselvio` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690762333](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690762333) | [#50](https://github.com/Vbitz/neurocontainers-arm64/issues/50) | verified: 96 passed |
| `topaz` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34690938300](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34690938300) | pending | in progress |
| `mede` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691245302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691245302) | pending | in progress |
| `builder` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691302636](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691302636) | pending | queued |
| `bidscoin` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691304372](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691304372) | pending | queued |
| `mede` | accepted pin `c6d782cd73cf88ccc44b837f705967b810519086` | pinned accepted branch | [34691245302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34691245302) | pending | queued |

## Verified results

- `dcm2niix` / `arm64`: run `34685110310`, source `87e1c726`, 106 passed, 0 failed, 0 skipped; issue [#4](https://github.com/Vbitz/neurocontainers-arm64/issues/4).
- `vina` / `arm64`: run `34685110418`, source `87e1c726`, 8 passed, 0 failed, 0 skipped; issue [#3](https://github.com/Vbitz/neurocontainers-arm64/issues/3).
- `dcm2bids` / `arm64`: run `34685269662`, source `87e1c726`, 61 passed, 0 failed, 0 skipped; issue [#5](https://github.com/Vbitz/neurocontainers-arm64/issues/5).
- `niimath` / `arm64`: run `34685110419`, source `87e1c726`, 115 passed, 0 failed, 0 skipped; issue [#6](https://github.com/Vbitz/neurocontainers-arm64/issues/6).
- `niistat` / `arm64`: run `34685269554`, source `87e1c726`, 93 passed, 0 failed, 0 skipped; issue [#7](https://github.com/Vbitz/neurocontainers-arm64/issues/7).
- `niftyreg` / `arm64`: run `34685110299`, source `87e1c726`, 89 passed, 0 failed, 0 skipped; issue [#10](https://github.com/Vbitz/neurocontainers-arm64/issues/10).
- `heudiconv` / `arm64`: run `34685389090`, source `87e1c726`, 69 passed, 0 failed, 0 skipped; issue [#9](https://github.com/Vbitz/neurocontainers-arm64/issues/9).
- `gimp` / `arm64`: run `34685484205`, source `87e1c726`, 7 passed, 0 failed, 0 skipped; issue [#8](https://github.com/Vbitz/neurocontainers-arm64/issues/8).
- `openrefine` / `arm64`: run `34685556897`, source `87e1c726`, 2 passed, 0 failed, 0 skipped; issue [#11](https://github.com/Vbitz/neurocontainers-arm64/issues/11).
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

- `hnncore` / `arm64`: run `34690701313`, source `c6d782cd`, 73 passed, 0 failed, 0 skipped; issue [#49](https://github.com/Vbitz/neurocontainers-arm64/issues/49).

## Blocked or failed results

- `dafne` / `arm64`: run `34690518800`, source `c6d782cd`, 10 passed and 1 failed in the fulltest runner; native headless GUI startup exited 139. Issue [#48](https://github.com/Vbitz/neurocontainers-arm64/issues/48) records the upstream blocker and revisit condition.

## Integration

- Accepted integration SHA: `c6d782cd73cf88ccc44b837f705967b810519086`
- Top-level submodule pointer advances from `031ff475` to the tested rapidtide candidate; dicomtools and radtract remain included.

## Next action

Monitor Topaz, MEDE, Builder, and BIDScoin, record each result in its issue and
this plan, then refill available slots with the next eligible declared recipe.
Reconcile the remaining declared inventory before ending the run.
