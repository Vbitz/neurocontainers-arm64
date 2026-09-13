# ARM64 porting checkpoint

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after ITK-SNAP Qt source retry dispatch

- Root checkpoint commit before this edit: `32e4ade`; accepted submodule pin remains
  `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` (PyDeface integrated on BIDSvue;
  native 60/60 fulltests in [run 34771433995](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34771433995)).
- Prepared EMUSES candidate `685f5f4d9636d34aa8237646535d2a7dfc3a525d` on
  `arm64/emuses-integrated-80a`, based on the accepted pin. It removes only
  the x86-generated NVIDIA/Triton lock entries on native aarch64 so the
  published PyTorch 2.7.1 ARM64 wheel can resolve; the x86 path remains
  unchanged. Local validation and both architecture generations pass. Issue
  [#94](https://github.com/Vbitz/neurocontainers-arm64/issues/94) records the
  hypothesis and the candidate. Dispatch after a native slot opens.
- The local submodule checkout is now `arm64/emuses-integrated-80a` at
  `685f5f4d9636d34aa8237646535d2a7dfc3a525d`; the root working tree therefore
  intentionally shows the submodule pointer modified. Do not accept that
  pointer until this exact candidate passes all gates.
- DSI Studio candidate `bdb427db440ea72de1e6fc50fc7a115c41fef5aa` was
  dispatched as attempt 2/6 in [run 34774820860](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774820860)
  after CLEARSWI completed successfully. Issue
  [#195](https://github.com/Vbitz/neurocontainers-arm64/issues/195) has the
  retry evidence. The run is queued/in progress; EMUSES remains the next
  queued candidate after another slot opens.
- EMUSES candidate `685f5f4d9636d34aa8237646535d2a7dfc3a525d` is now dispatched
  as attempt 3/6 in [run 34775307167](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775307167).
  Issue [#94](https://github.com/Vbitz/neurocontainers-arm64/issues/94) has
  the lock-cleanup hypothesis and exact candidate. The current local checkout
  remains `arm64/blender-integrated` at
  `171bd9b6c54a199718a24f064f5a2809df1fa6d`; the EMUSES candidate is immutable
  on its pushed branch.
- CLEARSWI's candidate passed its pre-integration native run with 68/68 tests.
  Its intended commits are replayed onto accepted pin `80a84327` as
  `21382bb0421c036c87a86e29c796cfcdeb319e35` on
  `arm64/clearswi-integrated-80a`; local validation and both architecture
  generations pass. Exact integrated verification is queued for the next
  native slot, and the local submodule checkout is this branch.
- EMUSES candidate `685f5f4d9636d34aa8237646535d2a7dfc3a525d` passed native
  Docker/SIF/deploy/fulltest in [run 34775307167](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775307167)
  with 2/2 fulltests passing and no skips. It descends directly from accepted
  pin `80a84327`, so the local checkout has switched to this candidate for
  serial top-level integration; issue [#94](https://github.com/Vbitz/neurocontainers-arm64/issues/94)
  records the verified result.
- CLEARSWI was replayed onto the new accepted EMUSES pin as candidate
  `488f143223358f000b57fdc06b2693a89b896110` on
  `arm64/clearswi-integrated-emuses` and dispatched in [run 34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906)
  for exact integrated verification. The local checkout is this branch;
  accept it only after all 68 native fulltests pass.
- DSI Studio run [34774820860](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774820860)
  built and converted successfully but failed five required AutoTrack tests
  (78/83 executed checks passed). The release-aligned test corrections did not
  resolve the official ARM64 CPU runtime's exit-1 behavior for those bundle
  operations. The bounded investigation is exhausted; issue
  [#195](https://github.com/Vbitz/neurocontainers-arm64/issues/195) records the
  concrete upstream runtime/data revisit condition. No pin change.
- ITK-SNAP candidate `258f746afb80f90077beb6fb63d0a336745fbb1e` addresses the
  last two Qt 6.4 source errors from run 34773851298. The final bounded retry
  is [run 34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451);
  the local checkout is `arm64/itksnap-integrated-80a` at that candidate.
- Blender run [34774135689](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774135689)
  reached the bundled Flex configure and failed on missing `autopoint`. The
  six native attempt and twelve-hour investigation budgets are exhausted, so
  no seventh run will be dispatched. Prepared candidate
  `171bd9b6c54a199718a24f064f5a2809df1fa6d` adds the package and remains
  pushed on `arm64/blender-integrated` for a future authorized window. The
  local submodule checkout is that branch at this candidate.

- Top-level parent commit: `6da579a`; accepted submodule pin is now
  `80a84327a6659b0ac79a44f2c1853faa9eb84f4b` (PyDeface integrated on BIDSvue;
  native 60/60 fulltests in [run 34771433995](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34771433995)).
  Fork Actions remains disabled (`enabled: false`), and coverage issue #2 was
  refreshed after acceptance.
- Active exact investigations (four build slots):
  - ITK-SNAP integrated candidate `701e4cd9f3d0bb8dc65b65bb655975b20ba19cfe`,
    run [34773851298](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773851298),
    attempt 4/6. The prior retry compiled ITK/VTK and then exposed three
    `std::string`/`QDebug` incompatibilities plus a missing `QTimeZone` include
    in the application source; this candidate applies those narrow fixes on
    the accepted PyDeface pin.
  - MIMoSA `c58b71e8e7400e0beb6026201b323c5d7aa3916d`, run
    [34773252089](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773252089),
    attempt 3/6. The FSL correction reached ANTsRCore but its R Makevars
    used small `-fpic`, overflowing the ARM64 GOT at link time; this retry
    uses large `-fPIC`.
  - CLEARSWI `256b2824f39066e26a632a754f271879c3c085e9`, run
    [34772631281](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34772631281),
    attempt 2/6. The first source candidate built and passed deploy checks;
    only the five-operation phase-scaling test exceeded its 120-second test
    limit, so this retry raises that test limit to 300 seconds.
  - Blender candidate `42b819836f9e594be0648660fb118d735b6e4c5d`, run
    [34774135689](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34774135689),
    attempt 3/6. The unchanged retry reached native dependency configure and
    exposed a missing `libasound2-dev` package; this candidate adds it to the
    ARM dependency set.
- mritools is blocked-upstream after two native attempts. CompileMRI.jl v3.3.0
  reaches ARM64 Julia dependency setup but its released App bootstrap leaves
  incompatible `RomeoApp`/`ClearswiApp`/`MriResearchTools` dependencies; issue
  #156 and `plans/mritools.md` contain both runs and the exact errors.
- Local submodule checkout is `arm64/dsistudio-integrated-80a` at
  `bdb427db440ea72de1e6fc50fc7a115c41fef5aa`; the active source branches and
  exact run IDs are recorded above. PyDeface is accepted; the remaining
  candidates must be replayed onto this newer pin before their own acceptance.
- Prepared next slot: DSI Studio candidate
  `bdb427db440ea72de1e6fc50fc7a115c41fef5aa` on
  `arm64/dsistudio-integrated-80a`. Its fulltest now follows the current
  2026.7.25 ARM64 CPU CLI's connectivity filenames, error wording and exact
  non-empty atlas IDs; local validation and both architecture generations
  pass. Dispatch when one of the four active runs completes.
- Prepared ITK-SNAP integration candidate `f4a84c7150db1e9a35cb9f26014304a7ed0b3804`
  on `arm64/itksnap-integrated`, replaying the source-build fixes onto the
  prior accepted pin. Local validation and both architecture generations pass;
  if `34771393155` is green, replay these commits onto `80a84327` and rerun
  that exact integrated candidate before acceptance.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after mritools bootstrap retry and CLEARSWI preparation

- Root commit: `edce8c3`; accepted submodule pin remains
  `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db` (BIDSvue on top of AFNI,
  5/5 native fulltests). Fork Actions remains disabled.
- Active exact investigations:
  - ITK-SNAP `7ceabea5d97151a98cf6655055729804870b33ee`, run
    [34769119103](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769119103),
    attempt 2/6.
  - PyDeface `90ee2948253826e0413ca90be894f381d10009eb`, run
    [34769469302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769469302),
    attempt 4/6.
  - MIMoSA `1f1fa6ea2942b55d1c3ec01e615d38c2b777babc`, run
    [34770095073](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770095073),
    attempt 2/6, selecting the verified ARM FSL 6.0.7.22 route.
  - mritools retry `bec588b5d45ad87e68ab5ccb4a19ea8ab969975a`, run
    [34770328188](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770328188),
    attempt 2/6, suppressing CompileMRI's incomplete-project auto-precompile.
- mritools attempt 1 reached Julia/CompileMRI dependency setup on native ARM64
  and stopped at the App bootstrap ordering error; issue #156 records the
  first actionable error and retry hypothesis.
- Prepared CLEARSWI `cf9a122bc839f0bde01d013bdf17ef7a915541e7` on
  `arm64/clearswi-bids`, based on the accepted pin. It adds the official
  Julia Linux AArch64 archive and skips only the failing custom PackageCompiler
  sysimage on ARM64; local validation and both architecture generations pass.
  Dispatch after the next runner slot opens.
- Local submodule checkout is `arm64/mritools-bids` at
  `bec588b5d45ad87e68ab5ccb4a19ea8ab969975a`; the CLEARSWI candidate remains
  pushed on its separate branch.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after MIMoSA FSL retry and mritools dispatch

- Root commit: `ded33f4`; accepted submodule pin remains
  `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db` (BIDSvue on top of AFNI,
  5/5 native fulltests). Fork Actions remains disabled (`enabled: false`).
- Active exact investigations:
  - ITK-SNAP candidate `7ceabea5d97151a98cf6655055729804870b33ee`, run
    [34769119103](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769119103),
    attempt 2/6, enabling VTK `RenderingExternal`.
  - PyDeface candidate `90ee2948253826e0413ca90be894f381d10009eb`, run
    [34769469302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769469302),
    attempt 4/6, pinning ARM setuptools below the `pkg_resources` warning
    threshold.
  - MIMoSA retry candidate `1f1fa6ea2942b55d1c3ec01e615d38c2b777babc`, run
    [34770095073](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770095073),
    attempt 2/6, selecting FSL 6.0.7.22 for ARM64 while preserving 6.0.7.16
    on x86_64. The first attempt stopped because FSL 6.0.7.16 had no
    `linux-aarch64` installer match.
  - mritools candidate `1304e3bd5ba0694b92bcaeae838167f2767fa164`, run
    [34770096752](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34770096752),
    attempt 1/6, using the upstream CompileMRI.jl source route with Julia
    1.10.10 AArch64.
- VMTK is blocked-upstream after four native attempts reached VTK 9.1
  `vtkSEPReader.cxx` compilation errors; issue #240 records the first
  actionable failure.
- The two invalid-ref dispatches `34770042730` and `34770044122` were
  cancelled during preflight; they produced no recipe build evidence.
- Local submodule checkout is `arm64/mimosa-bids` at
  `1f1fa6ea2942b55d1c3ec01e615d38c2b777babc`; mritools remains prepared on
  `arm64/mritools-bids` at `1304e3bd5ba0694b92bcaeae838167f2767fa164`.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after VMTK blocker and MIMoSA dispatch

- Root commit: `6548925`; accepted submodule pin remains
  `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db` (BIDSvue on top of AFNI,
  5/5 native fulltests). Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP candidate `7ceabea5d97151a98cf6655055729804870b33ee`, run
    [34769119103](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769119103),
    attempt 2/6.
  - PyDeface candidate `90ee2948253826e0413ca90be894f381d10009eb`, run
    [34769469302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769469302),
    attempt 4/6.
  - MIMoSA candidate `3ca09fbd6a8ab952d7189bbac2d1c85860571d0f`, run
    [34769582813](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769582813),
    attempt 1/6, testing the existing native R/ANTsR/FSL path.
- VMTK candidate `974bb148` is blocked-upstream after native VTK 9.1
  compilation failed in `vtkSEPReader.cxx`; issue #240 records the exact
  compiler errors and revisit condition. The local submodule checkout is
  `arm64/bidsvue-afni` at the accepted `ba7af584`; no candidate pointer is
  pending integration.
- Prepared next candidate: mritools `1304e3bd5ba0694b92bcaeae838167f2767fa164`
  on `arm64/mritools-bids`, based on the accepted BIDSvue pin. It uses the
  upstream CompileMRI.jl source build and official Julia Linux AArch64 binary;
  local validation and both architecture generations pass. Dispatch it after
  MIMoSA or another active run frees a slot.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after BIDSvue acceptance and PyDeface retry dispatch

- Root commit: `2a9c2ab`; accepted submodule pin is now
  `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db` (BIDSvue on top of AFNI,
  5/5 native fulltests). Fork Actions is disabled. Coverage issue #2 was
  refreshed after acceptance.
- Active exact investigations:
  - ITK-SNAP candidate `7ceabea5d97151a98cf6655055729804870b33ee`, run
    [34769119103](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769119103),
    attempt 2/6, explicitly enabling VTK `RenderingExternal`.
  - PyDeface candidate `90ee2948253826e0413ca90be894f381d10009eb`, run
    [34769469302](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769469302),
    attempt 4/6, pinning ARM setuptools below the `pkg_resources` warning
    threshold after the previous candidate passed 58/59 tests.
  - VMTK `974bb14826c93d9836203186ed6335a82a4e6320`, run
    [34768651549](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768651549),
    attempt 4/6.
- Prepared next candidate: MIMoSA `3ca09fbd` on branch
  `arm64/mimosa-afni`, based on the accepted AFNI pin with the existing native
  R/ANTsR/FSL build path declared for ARM64. Dispatch it when a slot opens.
- The local submodule checkout is `arm64/bidsvue-afni` at the accepted
  `ba7af584`; no candidate pointer is pending integration.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after ITK-SNAP VTK module retry dispatch

- Root commit: `acb1258c022e5c46bf3071424e1dc5fb7d4822fb`; accepted submodule
  pin remains `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` (AFNI, 114/114
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP candidate `7ceabea5d97151a98cf6655055729804870b33ee`, run
    [34769119103](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769119103),
    attempt 2/6, explicitly enabling VTK `RenderingExternal` after the prior
    VTK package configuration omitted that required component. An earlier
    short-SHA dispatch was rejected during checkout before the recipe ran.
  - PyDeface candidate `90ee29484e38e84a4b4a1f5da96ea7f2040ad2af2`, run
    [34769427700](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34769427700),
    attempt 4/6, pinning ARM setuptools below the documented warning threshold
    after the previous candidate passed 58/59 tests.
  - VMTK `974bb14826c93d9836203186ed6335a82a4e6320`, run
    [34768651549](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768651549),
    attempt 4/6.
  - BIDSvue `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db`, run
    [34768724186](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768724186),
    attempt 5/6.
- ITK-SNAP’s previous candidate `fdf69113` built ITK and VTK but stopped at
  the final CMake configure because `RenderingExternal` was absent from the
  installed VTK package. The local submodule checkout is now
  `arm64/itksnap-root` at `7ceabea5`; the root pointer remains intentionally
  unstaged while native runs execute.

### Prepared next candidate

- MIMoSA candidate `3ca09fbd` is based on accepted pin `8a9e48a7` on branch
  `arm64/mimosa-afni`. It adds the ARM declaration to the existing native R,
  ANTsR and FSL build path; recipe validation and both architecture Dockerfile
  generations pass. Dispatch it when one of the four active runs completes.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after BIDSvue launcher-path retry dispatch

- Root commit: `9a9cd6fc3b7baae48913afd53e66a64c75f64b8c`; accepted submodule
  pin remains `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` (AFNI, 114/114
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - PyDeface `3baa7a0662abfd352ab10f0d8342a12ef157990a`, run
    [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096).
  - VMTK `974bb14826c93d9836203186ed6335a82a4e6320`, run
    [34768651549](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768651549),
    attempt 4/6.
  - BIDSvue `ba7af5842b2c41dbc98ffd8d1e25431acf19a7db`, run
    [34768724186](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768724186),
    attempt 5/6, correcting the ARM launcher path after the source build
    reached 3/4 fulltest checks.
- BIDSvue’s Rust 1.88 candidate built and passed desktop metadata and runtime
  library checks; only `/usr/local/bin` versus the required `/usr/bin` launcher
  path failed. The local submodule checkout is `arm64/bidsvue-afni` at
  `ba7af584`; the root pointer remains intentionally unstaged while native runs
  execute.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after VMTK CMake compatibility retry

- Root commit: `7f36f264aae7052ee161779b3a275c091c9a1fe7`; accepted submodule
  pin remains `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` (AFNI, 114/114
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - PyDeface `3baa7a0662abfd352ab10f0d8342a12ef157990a`, run
    [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096).
  - BIDSvue integrated replay `6886b829d871a3b6315660e222305dfdebf918b5`, run
    [34767968286](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767968286),
    attempt 4/6.
  - VMTK `974bb14826c93d9836203186ed6335a82a4e6320`, run
    [34768651549](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768651549),
    attempt 4/6, using Ubuntu CMake 3.28 for the upstream superbuild.
- VMTK attempt 3 reached native VTK configuration but the conda CMake release
  rejected VTK 9.1’s legacy minimum version. This candidate uses the supported
  Ubuntu CMake while retaining the official source superbuild; further VMTK
  source failures will be classified as upstream blockers. The local submodule
  checkout is `arm64/vmtk-afni` at `974bb148`; the root pointer remains
  intentionally unstaged while native runs execute.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after VMTK superbuild configuration retry

- Root commit: `1ea3fffb8d6e3809c825a3a2b39c5ee5535a3b7b`; accepted submodule
  pin remains `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` (AFNI, 114/114
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - PyDeface `3baa7a0662abfd352ab10f0d8342a12ef157990a`, run
    [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096).
  - BIDSvue integrated replay `6886b829d871a3b6315660e222305dfdebf918b5`, run
    [34767968286](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767968286),
    attempt 4/6.
  - VMTK `f6cdfb24a53e56f251a96e72f934ecfb5d68f3c8`, run
    [34768446912](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768446912),
    attempt 3/6, the final configuration retry before upstream-blocker
    classification.
- VMTK attempt 2 reached VTK configuration but its legacy superbuild passed an
  empty Python major version. The candidate now sets `PYTHON_VERSION_MAJOR=3`
  explicitly while retaining the official upstream ITK/VTK source superbuild.
  The local submodule checkout is `arm64/vmtk-afni` at `f6cdfb24`; the root
  pointer remains intentionally unstaged while native runs execute.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after VMTK superbuild retry dispatch

- Root commit: `f5eff7dd27d88eec3b312cb2416d663d12b216a6`; accepted submodule
  pin remains `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` (AFNI, 114/114
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - PyDeface `3baa7a0662abfd352ab10f0d8342a12ef157990a`, run
    [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096).
  - BIDSvue integrated replay `6886b829d871a3b6315660e222305dfdebf918b5`, run
    [34767968286](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767968286),
    attempt 4/6.
  - VMTK retry `c11f9b0b61e73d22fb56a4172ea9d5da6e5bac92`, run
    [34768254230](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34768254230),
    attempt 2/6, switching from missing conda ITK CMake metadata to VMTK’s
    pinned upstream ITK/VTK superbuild.
- VMTK attempt 1 stopped before compilation because conda-forge ARM `itk`
  lacks `ITKConfig.cmake`; that does not establish an application blocker, so
  the documented superbuild is being tested once. The local submodule checkout
  is `arm64/vmtk-afni` at `c11f9b0b`; the root pointer remains intentionally
  unstaged while native runs execute.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after AFNI acceptance and BIDSvue/VMTK dispatch

- Root commit: `205b7e4`; accepted submodule pin is now
  `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6` (AFNI, 114/114 native checks)
  on top of ROOT. Fork Actions is disabled.
- Active exact investigations:
  - ITK-SNAP source build `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - PyDeface setuptools compatibility retry `3baa7a0662abfd352ab10f0d8342a12ef157990a`,
    run [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096).
  - BIDSvue integrated replay `6886b829d871a3b6315660e222305dfdebf918b5`,
    run [34767968286](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767968286),
    attempt 4/6, using Rust 1.88 after the prior locked Cargo graph required
    that released toolchain.
  - VMTK source candidate `766d5b541b8b4d41d74ce1e001cd0ca57e598ea9`, run
    [34767998185](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767998185),
    attempt 1/6, using native conda-forge VTK/ITK and VMTK’s system-dependency
    CMake build.
- BIDSvue’s Rust 1.86 retry failed at the Tauri build because `darling`,
  `plist`, `serde_with`, and `time` require rustc 1.88. The integrated 1.88
  candidate is the second and final dependency-toolchain adjustment.
- The local submodule checkout is `arm64/vmtk-afni` at `766d5b54`; the root
  pointer remains intentionally unstaged while native runs execute. Next action
  is to reconcile the four runs, integrate only exact passing candidates onto
  this AFNI pin, and continue through any remaining feasible plans.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after VMTK ARM source candidate preparation

- Root commit: `c57b3642e18f4e8da6c85803eb33f0b215adc68f`; accepted submodule
  pin remains `3bdd670d17eb6aae64902d1aed8091b2c464a79a` (ROOT, 102/102
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - AFNI integrated replay `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6`, run
    [34765634289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765634289).
  - ITK-SNAP source build `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - PyDeface setuptools compatibility retry `3baa7a0662abfd352ab10f0d8342a12ef157990a`,
    run [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096).
  - BIDSvue Rust 1.86 retry `88dc77ffa13fe277c7b27c174c4b495979f35e36`, run
    [34767566758](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767566758).
- Prepared VMTK branch `arm64/vmtk-root` at candidate
  `7da7a75b`. It adds the ARM Miniforge installer, uses native conda-forge
  VTK/ITK, and builds VMTK 1.5.0 from its pinned upstream source with the
  documented system-dependency CMake mode. Validation and both architecture
  Dockerfile generations pass. Dispatch it when a slot opens.
- BIDSvue attempt 2 reached the native Rust sidecar build and failed because
  the locked `icu_*`/`idna_adapter` dependencies require rustc 1.86; that
  supported toolchain update is now attempt 3. The local submodule checkout is
  `arm64/vmtk-root` at `7da7a75b`; the root pointer remains intentionally
  unstaged while native runs execute.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after PyDeface compatibility retry dispatch

- Root commit: `fee983c6374e541aa62a5cef37b06b2b48965055`; accepted submodule
  pin remains `3bdd670d17eb6aae64902d1aed8091b2c464a79a` (ROOT, 102/102
  native checks). Fork Actions is disabled.
- Active exact investigations:
  - AFNI integrated replay `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6`, run
    [34765634289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765634289).
  - ITK-SNAP source build `fdf69113`, run
    [34767223157](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767223157).
  - BIDSvue retry `3140e416`, run
    [34767319894](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767319894),
    fixing the missing `src-tauri/binaries` destination exposed after the native
    dcm2niix build passed.
  - PyDeface retry `3baa7a0662abfd352ab10f0d8342a12ef157990a`, branch
    `arm64/pydeface-root`, run
    [34767487096](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34767487096),
    attempt 3/6. It pins ARM setuptools below 81 after PyDeface’s prior
    20-test failure due to missing `pkg_resources`.
- MRIcroGL is blocked upstream after attempt 5/6: its final ARM64 link still
  requires x86_64 Linux and aarch64 Darwin prebuilt objects. Quickshear remains
  blocked at the required SynthStrip distance-transform runtime assertion.
- The local submodule checkout is `arm64/pydeface-root` at `3baa7a06`; the root
  pointer remains intentionally unstaged while native runs execute. Next action
  is to reconcile these four exact runs, integrate only exact passing candidates
  serially, and continue through the remaining feasible research plans.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after BIDSvue dispatch and MRIcroGL blocker

- Root commit: `5565b0d` (`Checkpoint ARM64 implementation runs`); accepted
  submodule pin remains `3bdd670d17eb6aae64902d1aed8091b2c464a79a` (ROOT,
  102/102 native checks). Fork Actions is disabled.
- Active exact investigations:
  - AFNI integrated replay `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6`, run
    [34765634289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765634289),
    still running from the current accepted pin.
  - PyDeface `809b10067d2fc8b011b2758511e78e1318538e37`, run
    [34766115338](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34766115338),
    attempt 2/6, bootstrapping pip in the native FSL ARM64 environment.
  - BIDSvue `2524ed481d41f0d0e8d9ab4bc82a6d17f3ea19d5`, branch
    `arm64/bidsvue-root`, run
    [34766831522](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34766831522),
    attempt 1/6. The candidate builds the Tauri app and its three Linux
    sidecars from pinned upstream source using native ARM64 dependencies.
    Investigation started `2026-09-13T15:51:06Z`, deadline
    `2026-09-14T03:51:06Z`.
- MRIcroGL attempt 5/6 is blocked upstream: run
  [34766081264](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34766081264)
  reached the final ARM64 link, where the v1.2.20211006 archive hardcodes
  x86_64 Linux and aarch64 Darwin object files. Issue #97 records the
  concrete blocker and the condition for revisiting it.
- Quickshear remains a required runtime blocker: its ARM FreeSurfer SynthStrip
  script lacks the tested distance-transform output option (41/43 checks).
- The local submodule checkout is `arm64/bidsvue-root` at `2524ed48`; the root
  pointer remains intentionally unstaged while native runs execute. Next action
  is to reconcile AFNI, PyDeface, and BIDSvue, integrate only exact passing
  candidates serially, then select the next feasible recipe from the remaining
  inventory.

## Latest implementation checkpoint — 2026-09-14

### Checkpoint after MRIcroGL zlib and PyDeface pip fixes

- Root commit: `9723f91488cd573529175fced3bbd5fec11d2f61`; accepted
  submodule pin remains `3bdd670d17eb6aae64902d1aed8091b2c464a79a` (ROOT,
  102/102 native checks). Fork Actions is disabled.
- Active exact investigations:
  - AFNI integrated replay `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6`, run
    [34765634289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765634289),
    still in progress after replaying the 114/114 candidate onto the ROOT pin.
  - MRIcroGL candidate `2a75c0b8f1461417e10bc9c45edd42d5b1fa9790`, branch
    `arm64/mricrogl-fsl`, run
    [34766081264](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34766081264).
    This is attempt 5/6: it adds native `zlib1g-dev` and disables the
    upstream Linux-only x86 Cloudflare zlib object selection so FPC links
    against Ubuntu's ARM64 zlib after the prior source fixes.
  - PyDeface candidate `809b10067d2fc8b011b2758511e78e1318538e37`, branch
    `arm64/pydeface-root`, run
    [34766115338](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34766115338).
    This is attempt 2/6: FSL 6.0.7.22 installed successfully, then exposed
    that its Python had no pip; the candidate runs `fslpython -m ensurepip`
    before the existing package installation.
- Quickshear candidate `90a169d1cde93600af0da8d07986285e792fad32`, run
  [34764132084](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764132084),
  built and deployed but failed the required SynthStrip distance-transform
  operation (41/43 raw checks). The ARM FreeSurfer 7.4.1 script has no `-d`
  output option; issue #228 comment records this as a required runtime
  blocker pending a compatible upstream ARM release.
- Local submodule branch is `arm64/pydeface-root` at `809b1006`; the root
  pointer is intentionally unstaged while the native runs execute. Next
  action is to reconcile these exact runs, integrate only passing candidates,
  then investigate the remaining plausible source routes (BIDSvue, ITK-SNAP,
  and MuscleMap) without repeating completed blockers.

### Checkpoint after MRIcroGL retry dispatch

### Checkpoint after ROOT acceptance and AFNI/PyDeface replay

- Root commit: `9723f91`; accepted submodule pin is
  `3bdd670d17eb6aae64902d1aed8091b2c464a79a` (ROOT, 102/102 native checks)
  on top of FSL `9a5ae40`. Fork Actions remains disabled.
- Active exact investigations:
  - AFNI integrated candidate `8a9e48a7028b53be7b93eb6706a55a6a9ec801e6`,
    run [34765634289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765634289),
    replayed from the passing AFNI candidate onto the accepted ROOT base.
  - Quickshear `90a169d1cde93600af0da8d07986285e792fad32`, run
    [34764132084](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764132084).
  - MRIcroGL `71dc49e023b13b9a263115e76ca9ba294df2e904`, run
    [34765456689](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765456689),
    targeting the hardcoded Lazarus x86_64 project metadata.
  - PyDeface integrated candidate `b4bb772377fa516abfd7b53667936d947e874b5c`,
    run [34765662024](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765662024),
    using the native FSL ARM64 environment while retaining x86_64 Miniconda.
- ROOT is accepted from exact run 34764973586: 102 passed, 0 failed, 0
  skipped. AFNI’s source candidate passed 114/114 before replay; acceptance is
  deferred until the exact replay run completes. The local submodule branch is
  `arm64/pydeface-root` at `b4bb7723`; its root pointer is intentionally
  unstaged while the four runner slots are active.

- Root commit: `8bfb440`; accepted submodule pin remains
  `9a5ae40c67667a088f50f0e9885833b983893f98` (FSL, 129/129 native checks).
- Active exact investigations:
  - AFNI `a51788253403b44c819d4273a134eedfe822aad3`, run
    [34763111015](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763111015).
  - Quickshear `90a169d1cde93600af0da8d07986285e792fad32`, run
    [34764132084](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764132084).
  - ROOT `3bdd670d17eb6aae64902d1aed8091b2c464a79a`, run
    [34764973586](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764973586).
  - MRIcroGL `71dc49e023b13b9a263115e76ca9ba294df2e904`, run
    [34765456689](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765456689),
    after fixing the dcm2niix output path and the hardcoded Lazarus x86_64
    project target.
- MRIcroGL run 34765237503 is recorded as attempt 2/6; its native dcm2niix
  build passed, then Lazarus selected unavailable `ppcx64`. The current run is
  the targeted ARM project configuration retry. PyDeface
  `ef08d99accaff64e04c2352da607e1ba6f94fafa` remains prepared on
  `arm64/pydeface-fsl` for the next free slot.
- The local submodule branch is `arm64/mricrogl-fsl` at `71dc49e0`; the root
  pointer is intentionally unstaged. Fork Actions remains disabled.

- Root commit: `ce55490`; accepted submodule pin remains
  `9a5ae40c67667a088f50f0e9885833b983893f98` (FSL, 129/129 native checks).
  Fork Actions remains disabled. The local submodule pointer is intentionally
  unstaged while candidate runs execute.
- Active exact investigations:
  - AFNI `a51788253403b44c819d4273a134eedfe822aad3`, run
    [34763111015](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763111015),
    attempt 2, correcting the official ARM R-bundle extraction directory.
  - Quickshear `90a169d1cde93600af0da8d07986285e792fad32`, run
    [34764132084](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764132084),
    attempt 2, extending only the existing CPU SynthStrip timeout.
  - ROOT `3bdd670d17eb6aae64902d1aed8091b2c464a79a`, run
    [34764973586](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764973586),
    attempt 2, selecting `apt` for the Ubuntu ARM64 base while retaining `yum`
    for the x86_64 ROOT base.
  - MRIcroGL `0838b0602c221df151c16d12e1764e23a0bcffb9`, run
    [34765237503](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34765237503),
    attempt 2, fixing the ARM dcm2niix output path after its source build
    succeeded.
- LST-AI is blocked by the required x86-only Greedy binary and exhausted one
  permitted unchanged Zenodo retry. Surf Ice is blocked by the upstream
  FreePascal ARM64 compiler internal error. DSI Studio and Blender remain
  failed-runtime and data/build-download investigations respectively; their
  branches are preserved without speculative retries.
- Prepared next candidate: PyDeface `ef08d99accaff64e04c2352da607e1ba6f94fafa`
  on `arm64/pydeface-fsl`, based on the accepted FSL pin and validated for both
  ARM64 and x86_64 generation. Dispatch it when one of the four active slots
  opens. The current local submodule branch is `arm64/mricrogl-fsl` at
  `0838b060`.

## Active implementation checkpoint — 2026-09-14

- Root acceptance commit: `5af67a2`; accepted submodule pin:
  `9a5ae40c67667a088f50f0e9885833b983893f98` (FSL, 129/129 native checks).
  Fork Actions remains disabled.
- Active exact investigations:
  - AFNI candidate `a51788253403b44c819d4273a134eedfe822aad3`, run
    [34763111015](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763111015),
    correcting the official ARM R-bundle extraction directory.
  - Quickshear candidate `90a169d1cde93600af0da8d07986285e792fad32`, run
    [34764132084](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764132084),
    extending only the existing CPU SynthStrip timeout.
  - LST-AI candidate `0a3bd626eda2eb4629437503011c0e084b3d2a3b`, retry run
    [34764566352](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764566352),
    after the first unchanged attempt hit a Zenodo HTTP 504 before staging.
  - ROOT candidate `faa846d618b7ba7346ac768414ddd232fb33d6a8`, run
    [34764723926](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34764723926),
    replayed on the accepted FSL pin with the official ARM64 `6.30.02-conda`
    base and the x86_64 Ubuntu counterpart.
- Prepared candidates waiting for a free slot and replay onto the current pin:
  - Surf Ice `579728b6` on `arm64/surfice-source`, documented Lazarus/Qt source
    build with system Python 3.8 embedding.
  - MRIcroGL `221ff266` on `arm64/mricrogl-source`, documented Lazarus/Qt
    NoPython source build with native dcm2niix.
- Recent outcomes requiring bookkeeping: DSI Studio run
  [34763556926](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763556926)
  built and converted but failed 16/83 runtime checks with the CPU ARM archive;
  Blender run
  [34763788910](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763788910)
  reached the native dependency build but GMP download timed out. Neither is
  accepted; preserve their branches and do not repeat without a concrete
  recipe-level hypothesis or the permitted transient retry.
- Current local submodule branch: `arm64/root-fsl` at `faa846d6`; the root
  pointer is intentionally unstaged while remote runs execute. Next actions:
  reconcile AFNI, Quickshear, LST-AI and ROOT; replay any passing candidate
  serially from the accepted pin; then dispatch Surf Ice, MRIcroGL, or the next
  feasible plan and keep the issue/plan checkpoints synchronized.

## Active implementation checkpoint — 2026-09-14

- Root commit: `91b0dc4` (`neurocontainers` is intentionally checked out on a
  candidate branch; do not stage that pointer until a candidate is accepted).
- Accepted submodule pin: `6103a923f43106c039ddf22a59c99c25352e459b`.
- Fork Actions remains disabled (`enabled: false`).
- Active exact ARM64 runs, all dispatched with `upload_image=false`:
  - FSL candidate `9a5ae40c67667a088f50f0e9885833b983893f98`, run
    [34762946871](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34762946871),
    fixing the ARM FSL deploy path after 128/128 functional tests passed.
  - AFNI candidate `a51788253403b44c819d4273a134eedfe822aad3`, run
    [34763111015](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763111015),
    selecting the official ARM AFNI and R bundles.
  - Blender candidate `e885463c45c0fb902a9e6747ffcc80914045d63f`, run
    [34763301992](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763301992),
    adding the documented Linux dependency set after the first native build
    exposed missing build tools.
  - DSI Studio CPU ARM candidate `31c89f647a4e3427ce7ddef94a2de81c40e2ebb9`, run
    [34763556926](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763556926),
    switching from the GPU/full ARM release to the official CPU ARM64 archive
    after the full release built but its CLI actions exited early.
- Queued candidates waiting for a free runner slot:
  - Quickshear `90a169d1cde93600af0da8d07986285e792fad32` on
    `arm64/integrate-quickshear-fetalsynthseg`; increases only the existing
    SynthStrip command timeout from 300 to 1200 seconds after the prior run
    passed packaging and timed out during CPU inference.
  - LST-AI `0a3bd626eda2eb4629437503011c0e084b3d2a3b` on
    `arm64/lstai-openads`; builds the pinned dcm2niix source on ARM64 while
    retaining the x86 release asset.
- Next work after a slot opens: dispatch exactly one queued candidate, then
  integrate any passing candidate serially from the accepted pin. Prepare
  PyDeface only after FSL is accepted; continue with BIDSvue, MuscleMap,
  MRIcroGL/Surf Ice and ROOT as bounded recipe investigations.

Updated: 2026-09-13 (Australia/Brisbane)

## Current state

- Top-level branch: `main`
- Top-level commit before this checkpoint: `96bc2e1` (DSI Studio retry and LST-AI blocker checkpoint)
- Pinned submodule: `neurocontainers@77b1ebe055243e309f5d5cbc0e7be279b72e9251` (TeraStitcher added after NFTsim)
- Submodule checkout: `arm64/integrate-terastitcher-nftsim`, accepted NFTsim run `34754095890` passed 68/68 and exact TeraStitcher replay `34754970340` passed 5/5 through build, SIF conversion, deploy checks and fulltest. Current exact integrated verification is active for DSI Studio `34755647607`, DeepLabCut `34756027424`, SovaBIDS `34756025699`, and MEGNET `34756122909` (queued). LST-AI is blocked on its required x86-64 Greedy binary. Prepared rsHRF candidate: `4cb7f929`. Earlier blocked outcomes remain recorded in their per-recipe issues. Origin `Vbitz/neurocontainers`.
- Fork Actions: disabled (`enabled: false`)
- Existing verified pipeline check: `workshopdemo` / `arm64`, run [34692323241](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34692323241), 4 passed, source `c6d782cd`
- Coverage snapshot: 102 of 247 declarations, refreshed from accepted source `77b1ebe055243e309f5d5cbc0e7be279b72e9251`; issue [#2](https://github.com/Vbitz/neurocontainers-arm64/issues/2)

## Per-recipe research — 2026-09-13

The user's research request covers **148 unsupported recipes**, excluding the
separately tracked NeuroCommand infrastructure candidate. All have individual
source-cited assessments and next steps in [plans/README.md](plans/README.md).
Research baseline: top-level `b4725fe20333308ce9f150bf252ea11902e71a74`, accepted
submodule `457c5a31b9830587801a06e7d6f81f18293135e8`. The submodule branch and
accepted pin are unchanged. No recipes were edited and no builds were dispatched
or repeated during this task; this is research, not new runtime verification.

**Correction to the historical audits below:** those audits overstated the
blockers. They must not be read as proof that every remaining application lacks
an ARM source/build route. Published modsort ARM assets, newer DSI Studio ARM
assets, LCModel source, official FSL ARM packages and TensorFlow ARM wheels
contradict several earlier diagnoses. The individual plans supersede those
blanket assessments while retaining previous native failure evidence.

Research classifications: 28 plausible recipe-level candidates, 56 unresolved
complete dependency stacks, 18 native/legacy dependency build investigations,
31 vendor-runtime deployment blockers, 7 GPU/CPU-mode prerequisites, 5 concrete
prior build failures, 2 binary distributions with no public source-build route
found, and 1 Windows application port. These categories do not imply that all
unresolved dependencies are fundamentally unportable.

Next porting candidates, if resumed: modsort (same-version published ARM asset),
DSI Studio (released ARM asset requiring a version mapping/update), LCModel
(source build), and SynthSeg (documented CPU path and ARM TensorFlow wheels).
Check each existing investigation budget and issue before any new attempt.
The current implementation goal supersedes the research-only checkpoint below.
The first implementation candidate, `modsort`, is proven on branch
`arm64/modsort` at candidate `c38fa11e`, with native run
[34751788247](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34751788247)
passing build, SIF conversion, deploy checks and all 8 fulltest checks after
one targeted zlib linker-package fix.
Its issue [#155](https://github.com/Vbitz/neurocontainers-arm64/issues/155)
contains the full attempt history. The accepted submodule pin is being advanced
serially to `c38fa11e2377ad2a9775fdd5fc3993c8b44155de` before accepting another
candidate. DSI Studio, SynthSeg and DeepLabCut are active; LCModel remains next
after reviewing its source/runtime completeness.
Research files were committed and pushed as `aade145`. Essential corrections
were mirrored in [coverage issue #2](https://github.com/Vbitz/neurocontainers-arm64/issues/2#issuecomment-5652645856)
and the existing modsort, DSI Studio, LCModel, FSL, DeepLabCut, LSTAI, SynthSeg
and TopoFit issues. Fork Actions remains disabled. Inventory, source-reference
presence, local links and unchanged accepted pin were checked; all 148 plans
are accounted for. One ARM64 recipe run is active; no other new runner jobs
were queued.

## Implementation goal checkpoint — 2026-09-13

The current top-level checkpoint advances the accepted submodule source to
`77b1ebe055243e309f5d5cbc0e7be279b72e9251`, after TeraStitcher’s integrated
native run [34754970340](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754970340)
passed build, SIF conversion, deploy checks and all 5 fulltest checks. NFTsim’s
integrated native run [34754095890](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754095890)
also passed all 68 checks. Modsort and SynthSeg remain
integrated and proven by native run [34751788247](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34751788247)
with 8 passed, 0 failed and 0 skipped. SynthSeg is also accepted after
integrated native run [34753249262](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34753249262)
passed build, SIF conversion, deploy checks and all 18 fulltest checks.

The following candidates are being tested from exact immutable submodule SHAs:

- DeepLabCut has been replayed onto the accepted pin at
  `df17f30548918cd26573988e94cc8bcfa4a5ba8d` on branch
  `arm64/integrate-deeplabcut-nftsim`; integrated run
  [34755044427](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34755044427)
  is in progress. The preceding candidate run
  [34753282289](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34753282289)
  passed 101/101 but was based on the prior accepted pin.
- NFTsim is accepted at integrated candidate
  `ce058afece0774f0fe915f3bc07c04507c7665bc` on branch
  `arm64/integrate-nftsim-synthseg`; run
  [34754095890](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754095890)
  passed 68/68. The earlier candidate run
  [34753242671](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34753242671)
  also passed on its prior baseline; the integrated run is the acceptance evidence.
- DSI Studio is being verified at integrated candidate
  `fde81b639abf8a2b8a5efce3a6f8152dd2414127` on branch
  `arm64/integrate-dsistudio-terastitcher`; final bounded run
  [34755647607](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34755647607)
  is in progress after switching affected AutoTrack checks to the current
  FIB-derived defaults and correcting endpoint connectivity output naming. The
  preceding integrated run [34754629806](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754629806)
  passed 77/83.
- TeraStitcher is accepted at integrated candidate
  `77b1ebe055243e309f5d5cbc0e7be279b72e9251` on branch
  `arm64/integrate-terastitcher-nftsim`; exact run
  [34754970340](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754970340)
  passed native build, SIF conversion, deploy checks and 5/5 fulltest. The
  preceding candidate run [34754399137](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34754399137)
  also passed on its prior baseline.
- LST-AI candidate `c992e97d08411e21cf4c55863030272563c1722e` on branch
  `arm64/lstai` built and converted successfully, passing 10/11 checks. It is
  blocked because the required v1.1.0 `greedy` registration binary is x86-64
  and no ARM64 release or documented portable build route was found; issue
  [#207](https://github.com/Vbitz/neurocontainers-arm64/issues/207#issuecomment-5653090650)
  records the exact failure.

DeepLabCut passed an earlier candidate run, but its candidate was based on the
previous accepted pin and still requires the exact integrated run above before
acceptance. Convert3D reached
the native build but is blocked because Debian Bookworm has no ARM64
`libinsighttoolkit5-dev` package and building ITK itself exceeds recipe scope;
run [34752548314](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34752548314)
and issue [#133](https://github.com/Vbitz/neurocontainers-arm64/issues/133) record
that outcome. LCModel is blocked at source audit because the public source
contains only the core executable while the recipe requires unavailable
ancillary tools; issue [#205](https://github.com/Vbitz/neurocontainers-arm64/issues/205)
records the source-completeness blocker. TeraStitcher’s first two source-build
candidates failed as described above; its third candidate passed all 5 fulltest
checks and still requires serial replay onto the accepted NFTsim pin.
Coverage issue #2 will be refreshed after this accepted TeraStitcher pin. The
top-level submodule pointer must remain at this accepted SHA while DSI Studio
and DeepLabCut finish. When a run completes, record its exact source and test
counts, then integrate successful candidates serially from the latest accepted
pin (currently `77b1ebe055243e309f5d5cbc0e7be279b72e9251`); retain failed
branches and record the first actionable error before selecting the next plan.

## Remaining unsupported inventory audit

At accepted source `457c5a31b9830587801a06e7d6f81f18293135e8`, 149 recipes
without an `aarch64` declaration have a matching `arm64-container` issue and a
durable blocker or native failure outcome. The current issue audit counts 128
`blocked-prerequisite`, 16 `blocked-upstream`, 3 legacy-format
`blocked-upstream`, 1 bounded-follow-up `blocked-upstream`, and 1
`blocked-infrastructure` outcome. The prerequisite records cover unavailable
ARM64 binaries or base images, GPU or license requirements, and unsupported
external services; the upstream records cover native dependency, compiler,
package, or source-build limitations. A native build was dispatched whenever a
bounded ARM64 recipe-level hypothesis was available. For hard preflight
blockers, no speculative or inherently unsupported build was queued. The
`openadscpu` / issue [#66](https://github.com/Vbitz/neurocontainers-arm64/issues/66)
record was refreshed during this investigation.

## Full unsupported inventory investigation

The prior audit was followed by an explicit recipe-by-recipe pass under the
current accepted source. Existing blocker comments were retained where the
affected recipe is unchanged from its recorded baseline, avoiding duplicate builds for fixed
x86_64-only assets, unavailable image manifests, GPU or license prerequisites,
and native dependency blockers already demonstrated by an exact ARM64 run.

The first new recipe-level candidate was `neurocommand` 1.0.0. Investigation
started 2026-09-13T09:23:22Z; deadline 2026-09-13T21:23:22Z. Candidate
`438050de3f8e251edf8a6f8ae454e15731e15984` on `arm64/neurocommand` preserved
the amd64 Apptainer package and built upstream Apptainer 1.4.4 from its release
source with the official Go 1.23.6 ARM64 toolchain on `aarch64`. Validation and
both Dockerfile generations passed. Run [34749429556](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34749429556)
failed at workflow startup, and the single unchanged retry returned HTTP 500
without creating a run. Issue [#158](https://github.com/Vbitz/neurocontainers-arm64/issues/158)
records the `blocked-infrastructure` outcome and revisit condition. The
candidate branch remains available and is not pinned.

The LAYNII dispatch initially returned HTTP 500, but its permitted unchanged
retry succeeded as [34749541502](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34749541502).
The exact candidate `457c5a31b9830587801a06e7d6f81f18293135e8` passed native
ARM64 Docker build, SIF conversion, deploy checks, and fulltest with 60 passed,
0 failed, and 0 skipped. It was fast-forwarded into the accepted fork branch
and the top-level pointer is advanced in this checkpoint.

## Focused follow-up outcomes

The user requested bounded follow-up on promising prior failures. The first
candidate is `mneextended`, whose previous native ARM64 run failed `pip check`
because `trame 3.13.2` requires `trame-server<4,>=3.12.2` while the resolved
server was 4.0.0. Conda-forge publishes `trame-server 3.13.0` as a noarch
package. Follow-up started at `2026-09-13T07:26:10Z`; it is limited to this
targeted recipe correction and one native build attempt under the prior
investigation budget. Issue [#71](https://github.com/Vbitz/neurocontainers-arm64/issues/71)
has the hypothesis and checkpoint.

Candidate `cd385b882d68ef08fafd8381b388e20f58d65c72` on
`arm64/mneextended-trame-server` is based on accepted source `7282a7d3` and
includes the previously tested ARM64 VS Code asset selection, pyedflib wheel
fallback, and `trame-client<4` correction, plus the new direct
`trame-server<4` constraint. Recipe validation and ARM64/x86_64 Dockerfile
generation passed. The branch is pushed. Exact native ARM64 run
[34745332614](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34745332614)
was dispatched at `2026-09-13T07:28:48Z` with `upload_image=false`; inspect its
result before considering another recipe. It passed native ARM64 build, SIF
conversion, deploy checks, and fulltest with 111 passed, 0 failed, and 0
skipped. Issue #71 records the verified candidate; serial replay onto the
accepted pin produced integrated SHA `7bffacf617a8e2b65f00f9e8eaa5e7e70d11cba0`
on `arm64/integrate-mneextended-trame`. Local validation and both architecture
generations passed. Raw-SHA serial runs
[34746072594](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34746072594)
and [34746170718](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34746170718)
were metadata-only source-resolution failures; the former used a malformed SHA
and the latter used the exact SHA but GitHub still could not resolve the object.
Fixed branch-ref run
[34746330768](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34746330768)
resolved the correct source and reached the build, where a transient VS Code
extension HTTP 503 failed the job. One unchanged retry
[34746559924](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34746559924)
was dispatched at `2026-09-13T07:59:32Z` and passed with 111 passed, 0 failed,
and 0 skipped. The top-level pointer was advanced to this exact integrated SHA
in commit `e5aec43`; coverage issue #2 was refreshed from it and now reports
97 of 247 declarations.

`networkcorrespondancetoolkit` is the second focused follow-up. Its first
candidate `5b1f1176992b3692e1187ef8223bde7a2e180803` removed only
ARM-incompatible Conda build hashes and the x86-only `ld_impl_linux-64` line;
native run [34745548264](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34745548264)
then exposed the pinned pip VTK wheel as unavailable on ARM64, and the next
candidate reached a VTK/libgcc version conflict. The final targeted candidate
`1de789e513cf9a1b26acda0cce6fb6acbda44662` on
`arm64/networkcorrespondancetoolkit-arm64-lock` keeps VTK 9.3.0 but selects its
Conda-forge ARM64 package on that architecture and unlocks the three compiler
runtime pins that conflict with VTK's `libgcc-ng>=12` requirement. Recipe
validation and ARM64/x86_64 Dockerfile generation passed. Exact native ARM64
run [34745899127](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34745899127)
was created at `2026-09-13T07:42:35Z` with `upload_image=false` and failed
before SIF conversion because the ARM64 Qt stack required unavailable Wayland
1.26 or OpenSSL newer than the locked 3.0.13. NCT is blocked-upstream after
four real attempts total; issue #99 records the three focused follow-ups and
the revisit condition. No active builds remain.

BrainLesion received one additional bounded recipe-level follow-up from the
current accepted pin. Candidate `9d8d71cbff92fcce2e79ad0c6d464f494427376e` on
`arm64/brainlesion-build-deps` added g++, then run
[34747415296](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34747415296)
confirmed the compiler but exposed missing git and make in the antspyx source
setup. Candidate `fc0e838959b69665233dac90b63bdf9c3c4797c9` replaced that with
`build-essential` and git; local validation and both architecture generations
passed. Native run
[34747574400](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34747574400)
then reached the bundled ITK/ANTs configuration and failed on its `master`
branch assumption plus missing PNG/ZLIB development libraries. With two
recipe-level prerequisite corrections exhausted, issue #247 records the
blocked-upstream outcome, three total native attempts, the start/deadline, and
the condition for revisiting. The failed branch remains available; no further
ANTs source or dependency port is planned.

## Second pass active work

The user-directed second pass is assessing the 151 recipes without ARM64
declarations. It began with `sigviewer`, which has a published Debian bullseye
ARM64 package at the pinned `0.6.4-1` version. Investigation started at
`2026-09-13T04:19:41Z`; deadline `2026-09-13T16:19:41Z`; attempt 1/6.
Candidate `c34a2103117399b31000f4d74bb378482e03f691` on branch
`arm64/sigviewer` adds `aarch64`, tracks Debian amd64 and arm64 package indexes
independently, and makes the libbiosig fulltest lookup multiarch-safe. Local
validation and both architecture generations passed. Exact native dispatch
[34737708431](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34737708431)
checked out the candidate and passed the ARM64 build, SIF conversion, deploy
checks, and fulltest with 36 passed, 0 failed, and 0 skipped. Issue
[#96](https://github.com/Vbitz/neurocontainers-arm64/issues/96) records the
source and report artifact. The candidate is accepted at top-level commit
`9767ce6`; no duplicate run was dispatched after acceptance.

`emuses` is blocked upstream. Investigation started at
`2026-09-13T04:24:42Z`; deadline `2026-09-13T16:24:42Z`; attempt 1/6 was a
cancelled malformed-ref dispatch [34737820842](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34737820842)
with no checkout or recipe evidence. The corrected candidate
`d5aaf861187bdbdf92ac5ec9143be4034a9a7f37` on branch `arm64/emuses` adds only
`aarch64`; local validation and both architecture generations passed. Exact
dispatch [34737868781](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34737868781)
checked out the candidate but failed during pip-sync because the lock requires
`triton==3.3.1`, for which no ARM64 distribution was available. SIF conversion,
deploy checks, and fulltest did not run. Issue
[#94](https://github.com/Vbitz/neurocontainers-arm64/issues/94) records the
error, artifact, and revisit condition. Attempts: 2/6; no retry is planned
until upstream publishes a compatible ARM64 Triton release or updates the
locked dependency. The malformed run is retained only as bookkeeping.

`code` was the third-second-pass candidate. Investigation started at
`2026-09-13T04:27:26Z`; deadline `2026-09-13T16:27:26Z`. Candidate
`1cc5c3e34b1e3f5f1151caadb62e5b5c634133a9` on branch `arm64/code` adds
architecture-specific official assets for VS Code, Julia 1.6.3, and Go 1.17.2
while retaining their x86_64 assets. Local validation and both architecture
generations passed. Attempt 1 [34738038980](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34738038980)
was cancelled before recipe checkout after a malformed ref was detected and
has no recipe evidence. Corrected attempt 2/6 is
[34738072738](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34738072738),
completed exact native ARM64 run [34738072738](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34738072738)
with the candidate source checked out. Docker build, SIF conversion, deploy
checks, and fulltest passed with 84 passed, 0 failed, and 0 skipped. Its
candidate predates the accepted sigviewer pin, so the recipe commit was
replayed onto accepted source `c34a2103` as
`15337e04a04ddf0303b610d304c350008df371ea` on `arm64/integrate-code`.
Local validation and both architecture generations passed. Exact integrated
dispatch [34738779168](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34738779168)
passed with 84 passed, 0 failed, and 0 skipped. The integrated commit is now
accepted at top-level commit `8da6e50`; issue
[#95](https://github.com/Vbitz/neurocontainers-arm64/issues/95) has the durable
verified result. Attempts: 3/6 including the metadata-only malformed-ref
dispatch and the independent candidate run.

`mricrogl` is blocked at preflight. The pinned 1.2.20211006 release provides
only x86_64 Linux MRIcroGL archives, and its required libqt5pas 1.2.9 release
provides only x86_64/amd64 packages. Issue
[#97](https://github.com/Vbitz/neurocontainers-arm64/issues/97) records the
official release assets and the revisit condition. No candidate branch or
native build was created; attempts: 0/6.

`palmettobug` was the fourth-second-pass candidate. Investigation started at
`2026-09-13T04:42:37Z`; deadline `2026-09-13T16:42:37Z`; attempt 1/6.
Candidate `0482f4d71952b2a1cec16005bdcbbc50de6c92a0` on branch
`arm64/palmettobug` adds only `aarch64`; its Miniconda template generated the
official Linux aarch64 installer and local validation plus both architecture
generations passed. Exact native dispatch
[34738541920](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34738541920)
failed during package installation because `palmettobug==0.2.11` pins
`PySide6==6.4.3`, which has no ARM64 distribution. SIF conversion, deploy
checks, and fulltest did not run. Issue [#98](https://github.com/Vbitz/neurocontainers-arm64/issues/98)
records the first error and revisit condition. Outcome: blocked-upstream;
attempts: 1/6; no retry until an upstream-compatible PalmettoBUG dependency set
is released.

Code's successful integrated run is recorded in issue [#95](https://github.com/Vbitz/neurocontainers-arm64/issues/95),
and the original malformed-ref dispatch remains metadata-only. PalmettoBUG
run `34738541920` is recorded as blocked-upstream. NCT run `34739158124` is
also recorded as blocked-upstream. No unchanged successful recipe has been
rerun.

`networkcorrespondancetoolkit` is the fifth-second-pass candidate. Investigation
started at `2026-09-13T04:58:50Z`; deadline `2026-09-13T16:58:50Z`; attempt
1/6. Candidate `95e84c71ac36869953fa124f514f2a6673b96e44` on branch
`arm64/networkcorrespondancetoolkit` adds `aarch64` and selects the official
Linux aarch64 Miniconda installer with its matching checksum while preserving
the x86_64 path. Local validation and both architecture generations passed.
Exact native dispatch [34739158124](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34739158124)
failed during Conda environment creation after the ARM64 platform was selected.
The first actionable error is the upstream lock's x86 package build pin:
`ca-certificates==2024.6.2=hbcca054_0` is unavailable for `linux-aarch64`.
SIF conversion, deploy checks, and fulltest did not run. Issue
[#99](https://github.com/Vbitz/neurocontainers-arm64/issues/99) records the
log, artifact, attempt 1/6, and revisit condition: an upstream ARM64-compatible
environment lock. No retry is planned.

`voreen` was assessed as the next source-build candidate. Investigation started at
`2026-09-13T05:12:49Z`; deadline `2026-09-13T17:12:49Z`; attempt 2/6.
Candidate `151c8c5d7b0f7153ea9f71d2e219f8d07632f5d1` on branch `arm64/voreen`
adds `aarch64` to the existing Ubuntu 24.04 CMake/Qt build and adds a headless
`voreentool` startup and usage-output assertion to the fulltest. Local
validation and both architecture generations passed. Attempt 1
[34739742820](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34739742820)
reached native ARM64 CMake but stopped because Boost package mode could not
find `boost_math_c99l`; no SIF or fulltest ran. Attempt 2 applied the standard
module-mode Boost discovery setting `Boost_NO_BOOST_CMAKE=ON`, but the bundled
Voreen `FindBoostVRN.cmake` still requested the unavailable `math_c99l` and
`math_tr1l` components. Exact native dispatch
[34739991537](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34739991537)
failed before compilation with the same dependency mismatch. Outcome:
blocked-upstream; no further retry is planned unless Voreen documents an ARM64
fix or releases updated Boost discovery logic. Issue
[#117](https://github.com/Vbitz/neurocontainers-arm64/issues/117) has the durable
failure note and revisit condition.

`bart` is the next bounded CPU/source candidate. Investigation started at
`2026-09-13T05:29:28Z`; deadline `2026-09-13T17:29:28Z`; attempt 1/6.
Candidate `e3f721a72f6e1b1f23d5962118f2873abbcdd203` on branch `arm64/bart`
adds `aarch64`, uses the multi-architecture Ubuntu 22.04 base for ARM64, and
retains the NVIDIA CUDA base and `CUDA=1` build for x86_64. The ARM64 command
uses BART's documented `CUDA=0` CPU build. Local validation and ARM64 and
x86_64 Dockerfile generation passed. Exact native dispatch
[34740461864](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34740461864)
passed Docker build, SIF conversion, deploy checks, and fulltest with 117
passed, 0 failed, and 0 skipped. Issue [#180](https://github.com/Vbitz/neurocontainers-arm64/issues/180)
records the verified result. The candidate is accepted in the current
top-level pin without a duplicate native run.

`lesionquantificationtoolkit` completed as a verified source candidate.
Investigation started at `2026-09-13T05:31:57Z`; deadline
`2026-09-13T17:31:57Z`; attempt 1/6. Candidate
`afc5c52d0d5d32e3d02c3fa1a94562274016f803` on branch
`arm64/lesionquantificationtoolkit` adds `aarch64` to the Ubuntu 24.04 R
source build and preserves the existing R package installation and fulltest.
Local validation and ARM64 and x86_64 Dockerfile generation passed. Exact
native dispatch [34740546339](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34740546339)
passed the native ARM64 build, SIF conversion, deploy checks, and fulltest with
101 passed, 0 failed, and 0 skipped. The recipe commit was replayed as
`70663adeaca16eae8c1e0b79fef1c3c0c3cecf86` on the accepted Lipsia pin; local
validation and both architecture generations passed, and the top-level pin now
includes it. Issue [#182](https://github.com/Vbitz/neurocontainers-arm64/issues/182)
records the result.

`lipsia` completed as a verified source candidate. Investigation started at
`2026-09-13T05:34:46Z`; deadline `2026-09-13T17:34:46Z`; attempt 1/6.
Candidate `01ea960b11e8c47698b02c93f9ce99007ca50be2` on branch `arm64/lipsia`
adds `aarch64` to the tagged Linux source build, whose setup script selects
the native GCC/G++ toolchain and the recipe supplies system GSL, Boost, and
OpenBLAS. Local validation and ARM64 and x86_64 Dockerfile generation passed.
Exact native dispatch
[34740665171](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34740665171)
passed the native ARM64 build, SIF conversion, deploy checks, and fulltest with
101 passed, 0 failed, and 0 skipped. Issue [#181](https://github.com/Vbitz/neurocontainers-arm64/issues/181)
records the result. Its one-line declaration was replayed as `dc20187f` onto
the current accepted pin and integrated without a duplicate native run.

`gliomoda` completed as a verified bounded CPU candidate. Investigation started at
`2026-09-13T05:38:52Z`; deadline `2026-09-13T17:38:52Z`; attempt 1/6.
Candidate `a9b7f2675cd9553388d30aa7df2bcdc053fa058d` on branch
`arm64/gliomoda` adds `aarch64` and selects the official PyPI ARM64 CPU torch
package while preserving the x86_64 CUDA 12.4 path. Local validation and both
architecture generations passed. Exact native dispatch
[34740874041](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34740874041)
passed the native ARM64 build, SIF conversion, deploy checks, and fulltest with
17 passed, 0 failed, and 0 skipped. The recipe commit was replayed as
`c6371e97` on accepted LQT source, and the top-level pin now includes it at
root commit `9ab887a`. Issue [#225](https://github.com/Vbitz/neurocontainers-arm64/issues/225)
records the result; no duplicate native run was dispatched after the isolated
replay.

`petu` completed as a verified bounded CPU candidate. Investigation started at
`2026-09-13T05:48:11Z`; deadline `2026-09-13T17:48:11Z`; attempt 1/6.
Candidate `2cb7b104d99cfe2505e20882dd606f4261499cf3` on branch `arm64/petu`
adds `aarch64` and selects the official PyPI ARM64 CPU torch package while
preserving the x86_64 CUDA 12.4 path. Local validation and both architecture
generations passed. Exact native dispatch
[34741200931](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34741200931)
passed the native ARM64 build, SIF conversion, deploy checks, and fulltest with
12 passed, 0 failed, and 0 skipped. The recipe commit was replayed as
`6502b535` on accepted BrainLes AURORA source, and the top-level pin now
includes it at root commit `f46433d`. Issue
[#246](https://github.com/Vbitz/neurocontainers-arm64/issues/246) records the
result; no duplicate native run was dispatched after the isolated replay.

`brats` completed as a verified bounded orchestrator candidate. Investigation started at
`2026-09-13T06:13:56Z`; deadline `2026-09-13T18:13:56Z`; attempt 1/6.
Candidate `fd560efddeb3694b9f7319738e0dea40fa7b4dd22` on branch `arm64/brats`
adds `aarch64`, builds Apptainer 1.4.4 from its official source tarball with
Go 1.23.6 on ARM64, and preserves the x86_64 Debian package path. Local
validation and both architecture generations passed. Exact native dispatch
[34742237759](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34742237759)
failed during the final ARM64 image setup because the source-built Apptainer
already installed `/usr/local/bin/singularity` and the recipe then tried to
create the same symlink. The x86_64 package path was unaffected. Retry
candidate `166f9dac76f26c1906acaf468665916a2b0bbca6` keeps the symlink step
x86_64-only and leaves the shared version checks in place. Local validation and
both architecture generations passed. Exact retry
[34742518202](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34742518202)
passed the native ARM64 build, SIF conversion, deploy checks, and fulltest with
21 passed, 0 failed, and 0 skipped. The two commits were replayed as
`7093c8f2` and `7282a7d3` on accepted PeTu source, and the top-level pin now
includes them at root commit `ab58a0b`. Issue
[#248](https://github.com/Vbitz/neurocontainers-arm64/issues/248) records both
attempts; the candidate is integrated without a duplicate native run. Attempts:
2/6; deadline `2026-09-13T18:13:56Z`.

`brainlesion` is blocked upstream after a dependency-resolution probe. Investigation started at
`2026-09-13T06:14:35Z`; deadline `2026-09-13T18:14:35Z`; attempt 1/6.
Candidate `83f5dc9524138a524d901655d7ca9a89899f0256` on branch
`arm64/brainlesion` adds `aarch64` to the bundle of the ARM64-tested CPU
components. Local validation and both architecture generations passed. Exact
native dispatch
[34742264785](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34742264785)
failed during the ARM64 image build while installing pinned `antspyx==0.6.3`.
The package has no Linux ARM64 wheel and its source fallback stopped because
CMake could not find `g++`; SIF conversion, deploy checks, and fulltest did not
run. Issue [#247](https://github.com/Vbitz/neurocontainers-arm64/issues/247)
records the blocked-upstream result and revisit condition. Attempts: 1/6; no
retry is planned without a released ARM64 wheel or documented ARM64 source
build path for `antspyx`.

`brainles-aurora` completed as a verified bounded CPU candidate. Investigation
started at `2026-09-13T05:50:32Z`; deadline `2026-09-13T17:50:32Z`; attempt
1/6. Candidate `dc828b57afcfaf21f4613d731b5676dcb16cacaa` on branch
`arm64/brainles-aurora` adds `aarch64` and selects the official PyPI ARM64 CPU
torch package while preserving the x86_64 CUDA 12.4 path. Local validation and
both architecture generations passed. Exact native dispatch
[34741297561](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34741297561)
passed the native ARM64 build, SIF conversion, deploy checks, and fulltest with
15 passed, 0 failed, and 0 skipped. The recipe commit was replayed as
`68873023` on accepted GlioMODA source, and the top-level pin now includes it at
root commit `3ab93f6`. Issue [#237](https://github.com/Vbitz/neurocontainers-arm64/issues/237)
records the result; no duplicate native run was dispatched after the isolated
replay.

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
recipe work; corrected exact run `34708194854` passed with 6 passed, 0 failed,
and 0 skipped. Attempt budget:
2/6 including the cancelled metadata-only dispatch.

`blochsiegertb1mapping` investigation started at `2026-09-12T17:23:50Z` from
accepted source `9a383b0d951f71725f2a2dade16a12e372bd6253`; deadline
`2026-09-13T05:23:50Z`. Candidate `93a11a16885aec3a548584bb9f3f332fe726df1b`
on branch
`arm64/blochsiegertb1mapping` adds only `aarch64`. It reuses the same accepted
OpenRecon source build, and its fulltest performs numerical Bloch-Siegert map
assertions over synthetic ISMRMRD images. Validation and both architecture
generations passed; exact run `34708203749` passed with 2 passed, 0 failed,
and 0 skipped. Attempt budget: 1/6. The recipe commit was replayed onto the
accepted source as integration commit `2884a0e6`; it is accepted in this
checkpoint without a duplicate native run.

`openreconexample` exact run `34708194854` passed with 6 passed, 0 failed, and
0 skipped. Its recipe commit was replayed as integration commit `9975caf0` and
then combined with the Bloch-Siegert declaration in `2884a0e6`; local
validation and both architecture generations passed. The cancelled invalid-ref
dispatch remains metadata-only, and no duplicate native integration run was
dispatched because the recipe changes are independent declarations.

ANTs investigation started at `2026-09-12T16:57:23Z` on attempt 1 from
accepted source `e90ee1a49ec687dd8582d10e7fb68546a008ecd4`; deadline
`2026-09-13T04:57:23Z`. Candidate `f48620a9503c3f532fa16c1b1e9ccc96778a86c6`
on branch `arm64/ants` adds `aarch64` and makes the existing source-build
compiler flags conditional: the x86_64 path retains its generic x86 flags,
while ARM64 uses the compiler defaults. Upstream ANTs source is built by the
existing Neurodocker template, and the fulltest runs version checks, image
conversion, denoising, thresholding, and smoothing operations. Validation and
both architecture generations passed. Exact run `34706765954` was dispatched
with `upload_image=false` and passed all gates with 103 passed, 0 failed, and 0
skipped. The recipe commit was replayed onto the current accepted source as
`88fb85137ac628e23542a923dfc005f8918bf306`; local validation and both
architecture generations passed, and it is accepted without a duplicate native
integration run. Issue [#93](https://github.com/Vbitz/neurocontainers-arm64/issues/93)
contains the report, logs, and artifact links. Attempt budget: 1/6.

Elastix preflight completed on 2026-09-13. The pinned 5.1.0 recipe downloads
only the upstream Ubuntu 20.04 Linux binary, with no ARM64 Linux asset
identified. Its CMake source build requires an externally provisioned ITK 5.3
installation, so this is a blocked-upstream preflight result rather than a
bounded recipe configuration port. Issue [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92)
records the evidence and revisit condition; no candidate branch or build was
created.

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

The accepted source contains 151 undeclared recipes after the BraTS
integration. A full preflight screen on 2026-09-13 found LQT, GlioMODA,
Lipsia, BART, PeTu, BrainLes AURORA, and BraTS as bounded source candidates;
BrainLesion is recorded as blocked by its pinned `antspyx` dependency. The remaining
inventory falls into
these groups:

- fixed x86_64 or amd64 downloads and containers, including AFNI, ASHS, BIDS
  Apps, BrainSuite, Cartool, Connectome Workbench, Convert3D, DSI Studio,
  FreeSurfer, FSL, LAYNII, MATLAB/SPM, MRIcroGL, MRtrix bundles, RStudio,
  Slicer, SPM variants, TrackVis, and the standalone proprietary tools;
- GPU-only or GPU-weighted recipes whose pinned CUDA images, wheels, or model
  assets have no native ARM64 path, including BraTS, DeepRetinotopy, DeepWMH,
  FastCSR, OpenMSK, RELION, SynthSeg, TopoFit, and VesselBoost;
- multi-architecture base images or package environments without an ARM64
  release path established during screening, including ASLPrep, BIDS Apps,
  fMRIPrep, Halfpipe, Nibabies, NiftyMIC, qsiprep/qsirecon, rsHRF, and xcp-d;
- native dependency or prerequisite blockers already recorded for OpenADS,
  FSL, MRtrix3, CPAC, LINDA, MNEextended, Spinal Cord Toolbox, CLEARSWI,
  GOUHFI, DAFNE, NeuroDesktop Lite, and TinyRange; and
- source bundles that embed one of those x86 or GPU dependencies, or require
  a broad compiler/library port. Elastix, MRIcroGL, OpenADS, FSL, MRtrix3,
  CPAC, and LINDA are recorded as explicit upstream/prerequisite preflight
  blockers in issues [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92),
  [#97](https://github.com/Vbitz/neurocontainers-arm64/issues/97),
  [#241](https://github.com/Vbitz/neurocontainers-arm64/issues/241),
  [#242](https://github.com/Vbitz/neurocontainers-arm64/issues/242),
  [#243](https://github.com/Vbitz/neurocontainers-arm64/issues/243),
  [#244](https://github.com/Vbitz/neurocontainers-arm64/issues/244), and
  [#245](https://github.com/Vbitz/neurocontainers-arm64/issues/245).

No speculative changes were made to these recipes. Revisit them only when the
upstream asset, base image, package, license prerequisite, or documented ARM64
build path changes.

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
| `openreconexample` | accepted candidate `2884a0e6a7d23e43fc51f58e32302ecc3689c27e` integrating `2eaed2732a85fa475cb823a336c62f682b8df90b` on accepted `9a383b0d` | `arm64/integrate-openrecon-blochsiegert` | cancelled ref [34708172513](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34708172513); exact [34708194854](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34708194854) | [#90](https://github.com/Vbitz/neurocontainers-arm64/issues/90) | accepted: 6 passed; integrated without duplicate run |
| `blochsiegertb1mapping` | accepted candidate `2884a0e6a7d23e43fc51f58e32302ecc3689c27e` integrating `93a11a16885aec3a548584bb9f3f332fe726df1b` on accepted `9a383b0d` | `arm64/integrate-openrecon-blochsiegert` | exact [34708203749](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34708203749) | [#91](https://github.com/Vbitz/neurocontainers-arm64/issues/91) | accepted: 2 passed; integrated without duplicate run |
| `ants` | accepted candidate `88fb85137ac628e23542a923dfc005f8918bf306` replaying `f48620a9503c3f532fa16c1b1e9ccc96778a86c6` onto accepted source `2884a0e6` | `arm64/integrate-ants-openrecon` | exact [34706765954](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34706765954) | [#93](https://github.com/Vbitz/neurocontainers-arm64/issues/93) | accepted: 103 passed; integrated without duplicate run |
| `elastix` | accepted source `88fb85137ac628e23542a923dfc005f8918bf306`; no candidate | preflight | no run | [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92) | blocked-upstream: no ARM64 Linux release asset; source build requires ITK 5.3 |
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
- `openreconexample` / `arm64`: run `34708194854`, tested source `2eaed273`, 6 passed, 0 failed, 0 skipped; issue [#90](https://github.com/Vbitz/neurocontainers-arm64/issues/90). Candidate is integrated at `2884a0e6` without a duplicate native run.
- `blochsiegertb1mapping` / `arm64`: run `34708203749`, tested source `93a11a16`, 2 passed, 0 failed, 0 skipped; issue [#91](https://github.com/Vbitz/neurocontainers-arm64/issues/91). Candidate is integrated at `2884a0e6` without a duplicate native run.
- `ants` / `arm64`: run `34706765954`, tested source `f48620a9`, 103 passed, 0 failed, 0 skipped; issue [#93](https://github.com/Vbitz/neurocontainers-arm64/issues/93). Candidate is integrated at `88fb8513` without a duplicate native run.
- `sigviewer` / `arm64`: run `34737708431`, tested source `c34a2103`, 36 passed, 0 failed, 0 skipped; issue [#96](https://github.com/Vbitz/neurocontainers-arm64/issues/96). Candidate is integrated at `c34a2103` without a duplicate native run.
- `lipsia` / `arm64`: run `34740665171`, tested source `01ea960b`, 101 passed, 0 failed, 0 skipped; issue [#181](https://github.com/Vbitz/neurocontainers-arm64/issues/181). Candidate is integrated at `dc20187f` without a duplicate native run.
- `lesionquantificationtoolkit` / `arm64`: run `34740546339`, tested source `afc5c52d`, 101 passed, 0 failed, 0 skipped; issue [#182](https://github.com/Vbitz/neurocontainers-arm64/issues/182). Candidate is integrated at `70663ade` without a duplicate native run.
- `gliomoda` / `arm64`: run `34740874041`, tested source `a9b7f267`, 17 passed, 0 failed, 0 skipped; issue [#225](https://github.com/Vbitz/neurocontainers-arm64/issues/225). Candidate is integrated at `c6371e97` without a duplicate native run.
- `brainles-aurora` / `arm64`: run `34741297561`, tested source `dc828b57`, 15 passed, 0 failed, 0 skipped; issue [#237](https://github.com/Vbitz/neurocontainers-arm64/issues/237). Candidate is integrated at `68873023` without a duplicate native run.
- `petu` / `arm64`: run `34741200931`, tested source `2cb7b104`, 12 passed, 0 failed, 0 skipped; issue [#246](https://github.com/Vbitz/neurocontainers-arm64/issues/246). Candidate is integrated at `6502b535` without a duplicate native run.
- `brats` / `arm64`: retry run `34742518202`, tested source `166f9dac`, 21 passed, 0 failed, 0 skipped; issue [#248](https://github.com/Vbitz/neurocontainers-arm64/issues/248). Candidate is integrated at `7282a7d3` after one targeted configuration retry.

## Blocked or failed results

- `dafne` / `arm64`: run `34690518800`, source `c6d782cd`, 10 passed and 1 failed in the fulltest runner; native headless GUI startup exited 139. Issue [#48](https://github.com/Vbitz/neurocontainers-arm64/issues/48) records the upstream blocker and revisit condition.
- `tinyrange` / `arm64`: no run; validation and both architecture generations passed, but its essential fulltest requires QEMU. Issue [#53](https://github.com/Vbitz/neurocontainers-arm64/issues/53) records the prerequisite blocker.
- `neurodesktop-lite` / `arm64`: run `34691454730`, source `c6d782cd`, build failed before SIF conversion and fulltest because the pinned `jupyterlab-slurm` source could not resolve `@jupyterlab/core-meta` 4.0.x. Issue [#56](https://github.com/Vbitz/neurocontainers-arm64/issues/56) records the upstream blocker.
- `openadscpu` / `arm64`: no run; the pinned `antspyx==0.5.4` release has no Linux ARM64 wheel, so a supported result would require porting that native dependency. Issue [#66](https://github.com/Vbitz/neurocontainers-arm64/issues/66) records the preflight blocker.
- `gouhfi` / `arm64`: runs `34691452949` and `34694039302` both built the native ARM64 image but failed exporting it with `no space left on device`; SIF conversion and fulltest did not run. Issue [#60](https://github.com/Vbitz/neurocontainers-arm64/issues/60) records the exhausted unchanged retry and revisit condition.
- `mneextended` / `arm64`: exact run `34698395577`, candidate `91ac9396`, reached the native ARM64 Docker build but failed before SIF conversion and fulltest. After the pyedflib wheel and `trame-client<4` fix, `pip check` reported `trame 3.13.2` requires `trame-server<4,>=3.12.2` while `trame-server 4.0.0` is installed. Issue [#70](https://github.com/Vbitz/neurocontainers-arm64/issues/70) records the three-attempt investigation and upstream blocker.
- `spinalcordtoolbox` / `arm64`: exact retry `34699607997`, candidate `3dac0979`, installed qmake and resolved ARM64 packages but the pinned PyQt5 5.15.11 source metadata build was terminated with exit 143 after about 13 minutes. Issue [#74](https://github.com/Vbitz/neurocontainers-arm64/issues/74) records the two-attempt upstream blocker and revisit condition.
- `clearswi` / `arm64`: exact run `34699875754`, candidate `86c62b32`, installed and precompiled the Julia dependency set but failed during PackageCompiler sysimage generation with the ARM64 LLVM `vscale` instruction-selection error in `HostCPUFeatures`. No SIF or fulltest ran. Issue [#75](https://github.com/Vbitz/neurocontainers-arm64/issues/75) records the upstream blocker and revisit condition.
- `elastix` / `arm64`: no run; the pinned 5.1.0 release has no identified ARM64 Linux asset, and its source build requires ITK 5.3. Issue [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92) records the blocked-upstream preflight and revisit condition.
- `openads` / `arm64`: no run; the pinned `sljhlab/openads:gpu` image has no ARM64 manifest and its fulltest requires GPU access. Issue [#241](https://github.com/Vbitz/neurocontainers-arm64/issues/241) records the blocked-prerequisite preflight and revisit condition.
- `fsl` / `arm64`: no run; the recipe's bundled FSL distribution and template are pinned to x86_64 assets with no ARM64 release path. Issue [#242](https://github.com/Vbitz/neurocontainers-arm64/issues/242) records the blocked-prerequisite preflight and revisit condition.
- `mrtrix3` / `arm64`: no run; its pinned FSL base image `vnmd/caid/fsl_6.0.3:20200905` has no established ARM64 path. Issue [#243](https://github.com/Vbitz/neurocontainers-arm64/issues/243) records the blocked-prerequisite preflight and revisit condition.
- `cpac` / `arm64`: no run; the pinned `fcpindi/c-pac:release-v1.8.7.post1.dev3` image is amd64-only. Issue [#244](https://github.com/Vbitz/neurocontainers-arm64/issues/244) records the blocked-prerequisite preflight and revisit condition.
- `linda` / `arm64`: no run; the pinned `dorianps/linda:latest` image is amd64-only. Issue [#245](https://github.com/Vbitz/neurocontainers-arm64/issues/245) records the blocked-prerequisite preflight and revisit condition.
- `brainlesion` / `arm64`: exact run `34742264785`, candidate `83f5dc95`, failed while building the pinned `antspyx==0.6.3` source fallback because CMake could not find `g++`; no Linux ARM64 wheel is published. Issue [#247](https://github.com/Vbitz/neurocontainers-arm64/issues/247) records the blocked-upstream result and revisit condition.
- `emuses` / `arm64`: exact run `34737868781`, candidate `d5aaf861`, failed during pip-sync because the lock requires `triton==3.3.1`, which has no ARM64 distribution. SIF conversion and fulltest did not run. Issue [#94](https://github.com/Vbitz/neurocontainers-arm64/issues/94) records the blocked-upstream result and revisit condition.
- `mricrogl` / `arm64`: no run; MRIcroGL 1.2.20211006 and its required libqt5pas 1.2.9 releases provide only x86_64/amd64 Linux assets. Issue [#97](https://github.com/Vbitz/neurocontainers-arm64/issues/97) records the blocked-prerequisite result and revisit condition.
- `palmettobug` / `arm64`: exact run `34738541920`, candidate `0482f4d7`, failed during package installation because the pinned `PySide6==6.4.3` has no ARM64 distribution. Issue [#98](https://github.com/Vbitz/neurocontainers-arm64/issues/98) records the blocked-upstream result and revisit condition.
- `networkcorrespondancetoolkit` / `arm64`: exact run `34739158124`, candidate `95e84c71`, failed during Conda environment creation because the upstream lock pins `ca-certificates==2024.6.2=hbcca054_0`, unavailable for `linux-aarch64`. Issue [#99](https://github.com/Vbitz/neurocontainers-arm64/issues/99) records the blocked-upstream result and revisit condition.
- `voreen` / `arm64`: exact runs `34739742820` and `34739991537`, candidates `bb08bc1c` and `151c8c5d`, both stopped in native ARM64 CMake configuration before compilation. Voreen 5.3.0's bundled `FindBoostVRN.cmake` requests `math_c99l` and `math_tr1l`, unavailable from Ubuntu 24.04's ARM64 Boost 1.83.0 packages; package mode and module mode both fail. Issue [#117](https://github.com/Vbitz/neurocontainers-arm64/issues/117) records the blocked-upstream result and revisit condition.
- `bart` / `arm64`: exact dispatch `34740461864`, candidate `e3f721a7`, passed all gates with 117 passed, 0 failed, and 0 skipped. The ARM64 path uses upstream BART's `CUDA=0` CPU build; the x86_64 CUDA path is preserved. Issue [#180](https://github.com/Vbitz/neurocontainers-arm64/issues/180) records the verified result; the candidate is accepted at `e3f721a7`.

## Latest implementation checkpoint — 2026-09-13 22:05 Australia/Brisbane

The accepted submodule pin remains `77b1ebe055243e309f5d5cbc0e7be279b72e9251`; the local checkout is back on `arm64/integrate-terastitcher-nftsim` and is clean. Fork Actions remains disabled. Four runner slots are occupied by the following exact candidates:

- DeepLabCut: prior candidate run `34755044427` passed 101/101. Replay candidate `add4f3fe915a514d3fa4294b768b29934933b928` is on `arm64/integrate-deeplabcut-terastitcher`, with exact run `34756027424` active.
- SovaBIDS: first candidate run `34755714902` failed during the indirect PyQt5 source metadata build because SIP could not find qmake. Retry candidate `7a9deaee23242820fb6fbd5c27df862e67975a9d` adds ARM Qt development packages and configures qmake for the pinned PyQt5 source build; exact run `34756025699` is active. The earlier malformed-source dispatch `34755995546` was cancelled before build.
- MEGNET: prior candidate run `34755697611` passed 6/6. Replay candidate `1ce18a5642515bbb314ea48def4ac022c91264e8` is on `arm64/integrate-megnet-terastitcher`; exact run `34756122909` is queued.
- DSI Studio: final bounded candidate `fde81b639abf8a2b8a5efce3a6f8152dd2414127` is on `arm64/integrate-dsistudio-terastitcher`; exact run `34755647607` remains in its runtime test phase. The prior integrated run passed 77/83; if the five named AutoTrack bundles still fail, the six-attempt budget is exhausted and the release/runtime mismatch will be recorded as the blocker.

The rsHRF source-build candidate `4cb7f92901acfe61bc28321084ba02a690ff4167` is pushed on `arm64/rshrf`, validated, and ready for dispatch when a slot opens. No additional recipe is queued until one of the four active investigations completes. A prior DeepLabCut malformed-source dispatch `34755840907` failed during checkout and is metadata-only; its exact replacement is the active run above.

## Integration

- Accepted integration SHA: `7282a7d3`
- Top-level submodule pointer accepts the tested MNE, SynthStroke, QSMbly,
  VertexWiseR, Deep Quality Estimation, Template, GingerALE, OpenRecon I2I,
  MipView, Sodiumgridding, Sodiumnufft, qMRLab, Epirecon, Sodiumgriddingptpi,
  SynthStrip, PALM, wfTFI, OpenRecon example, Bloch-Siegert, ANTs, sigviewer,
  and Code, BART, Lipsia, LQT, GlioMODA, BrainLes AURORA, PeTu, and BraTS integrations. The earlier SynthStrip exact candidate run
  passed and was integrated by ancestry; its stale duplicate integration run
  also passed 70 tests and is bookkeeping only. PALM and ANTs are integrated;
  the ANTs exact native ARM64 run passed 103 tests, and sigviewer passed 36
  tests. Code's integrated run passed 84 tests, BART passed 117 tests, Lipsia
  and LQT each passed 101 tests, GlioMODA passed 17 tests, and BrainLes AURORA
  passed 15 tests, PeTu passed 12 tests, and BraTS passed 21 tests. Elastix, FSL, MRtrix3, CPAC, and LINDA are recorded as
  preflight prerequisite blockers; emuses is blocked by its locked Triton dependency,
  MRIcroGL by unavailable ARM64 binaries, PalmettoBUG by its pinned PySide6
  dependency, and NCT by its x86-specific Conda lock.
  CLEARSWI, Spinal Cord Toolbox, and Voreen are blocked upstream;
  MNEextended is blocked
  by cascading trame dependency constraints. BrkRaw, Brainlife CLI, dicomtools, radtract,
  rapidtide, dwidenoise2, FSQC, Panoptica, PCNtoolkit, MeGANorm, DeepDisco, and
  FLAMeS remain included.

## Next action

Issue [#2](https://github.com/Vbitz/neurocontainers-arm64/issues/2) was refreshed
from accepted source `7282a7d3` and now reports 96 of 247 declarations.
The exact native runs `34708194854` and `34708203749` verified
`openreconexample` and `blochsiegertb1mapping`, respectively, and their
independent declarations are integrated at `2884a0e6`. ANTs run
`34706765954` passed 103 tests and its isolated commit is integrated at
`88fb8513` without a duplicate native run. Sigviewer run `34737708431` passed
36 tests and is integrated at `c34a2103` without a duplicate native run.
Elastix, emuses, MRIcroGL, OpenADS, FSL, MRtrix3, CPAC, LINDA, PalmettoBUG,
NCT, Voreen, and BrainLesion are recorded as blocked with their revisit
conditions. LQT, GlioMODA, BrainLes AURORA, PeTu, and BraTS are integrated. The
BraTS retry `34742518202` passed after the targeted symlink fix; BART run
`34740461864` and Lipsia run `34740665171` passed and are accepted.
Code's integrated run `34738779168` passed and is accepted at `15337e04`.
Lipsia is integrated at `dc20187f`, LQT at `70663ade`, GlioMODA at `c6371e97`,
BrainLes AURORA at `68873023`, PeTu at `6502b535`, and BraTS at `7282a7d3` are
integrated without duplicate native integration runs. BrainLesion is blocked at
issue [#247](https://github.com/Vbitz/neurocontainers-arm64/issues/247). All 247
recipes now have an `arm64-container` issue marker: 96 declarations are
accepted and the remaining 151 unsupported recipes have recorded preflight
blockers or failed ARM64 attempts. No builds are active; the next action is to
leave this checkpoint for future upstream changes rather than duplicate any
unchanged verification.

## Active implementation checkpoint — 2026-09-13 22:15 Australia/Brisbane

- Accepted submodule candidate: `1ce18a5642515bbb314ea48def4ac022c91264e8`, descended from `77b1ebe055243e309f5d5cbc0e7be279b72e9251` and verified by exact native run [34756122909](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756122909): MEGNET build, SIF, deploy, and 6/6 fulltest checks passed. The local submodule is on `arm64/integrate-megnet-terastitcher` while the root pointer is being accepted.
- DeepLabCut integrated candidate `add4f3fe915a514d3fa4294b768b29934933b928` remains active in run [34756027424](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756027424).
- DSI Studio final bounded candidate `fde81b639abf8a2b8a5efce3a6f8152dd2414127` remains active in run [34755647607](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34755647607); its investigation is at attempt 6/6.
- SovaBIDS candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` is pushed on `arm64/sovabids`. The prior checkout-only run [34756247757](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756247757) used an incorrect SHA and is metadata-only; the corrected exact dispatch is [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235).
- rsHRF candidate `4cb7f92901acfe61bc28321084ba02a690ff4167` is validated and pushed on `arm64/rshrf`, waiting for a runner slot. Fork Actions is confirmed disabled.
- Next action: commit the MEGNET pointer, refresh coverage issue #2 from the new accepted pin, then monitor the three active investigations and dispatch rsHRF as soon as a slot opens. Keep each candidate’s exact source SHA tied to its run before acceptance.

## Active implementation checkpoint — 2026-09-13 22:25 Australia/Brisbane

- Accepted submodule pin is now `1ce18a5642515bbb314ea48def4ac022c91264e8`; the root commit accepting MEGNET is `3baa72dd26979ae61254b7d928f610deb834ad3`. The local root and submodule checkouts are clean, and fork Actions remains disabled.
- DeepLabCut candidate `add4f3fe915a514d3fa4294b768b29934933b928` passed exact run [34756027424](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756027424) with 101/101 checks, but it was based before MEGNET acceptance. It must be replayed onto `1ce18a5` and rerun before root acceptance.
- gigaconnectome candidate `ca080b166bdacce2d9dbd48189ec254131605603` is in run [34756916668](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756916668).
- rsHRF candidate `9b60afc24a471a606cb2145b36a21c9b01cd089b` is in run [34756942808](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756942808), replayed onto the MEGNET accepted pin.
- SovaBIDS corrected candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` is in run [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235). DSI Studio final bounded candidate `fde81b639abf8a2b8a5efce3a6f8152dd2414127` remains in run [34755647607](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34755647607), attempt 6/6.
- Next action: reconcile active runs; on the first completed slot, replay and dispatch DeepLabCut on `1ce18a5` if needed, then continue to the next unblocked source-build plan. No active run is to be duplicated.

## Active implementation checkpoint — 2026-09-13 22:35 Australia/Brisbane

- DeepLabCut exact run [34756027424](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756027424) passed 101/101 on candidate `add4f3fe915a514d3fa4294b768b29934933b928`. Its replay onto accepted MEGNET is prepared and pushed as `0b386176700eaaf42bc213de235238c8ce5f3ef8` on `arm64/integrate-deeplabcut-megnet`, awaiting a slot for exact final verification.
- gigaconnectome candidate `ca080b166bdacce2d9dbd48189ec254131605603` hit Debian Bullseye mirror 404s before recipe installation in [34756916668](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756916668); one unchanged transient retry is [34757066283](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757066283).
- rsHRF candidate `9b60afc24a471a606cb2145b36a21c9b01cd089b` is in exact run [34757064676](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757064676). The earlier dispatch [34756942808](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756942808) used a root SHA and is checkout metadata-only.
- SovaBIDS candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` remains in [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235); DSI Studio candidate `fde81b639abf8a2b8a5efce3a6f8152dd2414127` remains in [34755647607](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34755647607), attempt 6/6.
- Four runner slots are occupied. The local checkout is back on accepted submodule pin `1ce18a5642515bbb314ea48def4ac022c91264e8`; root is clean at `9de3e01` and fork Actions is disabled.

## Active implementation checkpoint — 2026-09-13 22:40 Australia/Brisbane

- rsHRF candidate `9b60afc24a471a606cb2145b36a21c9b01cd089b` passed exact native run [34757064676](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757064676) with build, SIF, deploy, and 2/2 fulltest checks. It is descended from the accepted `1ce18a5` pin and is being integrated now.
- DSI Studio final candidate `fde81b639abf8a2b8a5efce3a6f8152dd2414127` failed five required AutoTrack operations in [34755647607](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34755647607), after 79/84 checks passed. Issue #195 records the six-attempt bounded runtime blocker; no unchanged or speculative retry remains.
- gigaconnectome unchanged retry [34757066283](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757066283) reproduced the Debian Bullseye package mirror 404 before application installation. This is now a recipe/base maintenance decision, not evidence of an application dependency blocker.
- DeepLabCut replay candidate `0b386176700eaaf42bc213de235238c8ce5f3ef8` is validated and pushed, awaiting a slot. SovaBIDS candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` remains active in [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235).
- The gigaconnectome retry and rsHRF exact run are complete, so two slots are free after the rsHRF acceptance bookkeeping. Next action: commit the rsHRF pointer, refresh coverage, dispatch the exact DeepLabCut replay, and use the remaining slot for a targeted gigaconnectome base-image fix or the prepared ROMEO source route.

## Active implementation checkpoint — 2026-09-13 22:38 Australia/Brisbane

- Accepted submodule pin is `9b60afc24a471a606cb2145b36a21c9b01cd089b` and the root acceptance commit is `ecd3fd56d5963992ec6310c4104172d0606b6972`. The local submodule is back on `arm64/integrate-rshrf-megnet`; fork Actions remains disabled.
- DeepLabCut candidate `0ed4b3c91637e7bee190bbfb66ba2ddfa0edbeeb` is based on the accepted pin and is in exact native run [34757340002](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757340002).
- SovaBIDS candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` is in corrected exact run [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235); the earlier mistyped-SHA run is checkout metadata only.
- gigaconnectome candidate `dc1439d82ec42fd3cb5b38e85ca1d5800a3484b2` changes the ARM64 base from Bullseye to the official ARM64-capable Python 3.9 Bookworm image after two reproducible Debian mirror 404 failures. It is in run [34757505350](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757505350).
- ROMEO candidate `0291d268b03c1840639d452f5be7952edd73d01c` is replayed onto the accepted pin, validated for ARM64 and x86_64 generation, and is in run [34757529921](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757529921).
- Four runner slots are occupied. DSI Studio remains a bounded failed-runtime blocker at 79/84 checks; its issue comment records the five required AutoTrack failures. LST-AI remains blocked by its bundled x86-64 `greedy` binary.
- Next action: reconcile the four exact runs, accept only candidates whose exact source SHA and fulltest pass are confirmed, then refill each completed slot from the next feasible research plan while replaying candidates onto any newer accepted pin.

## Active implementation checkpoint — 2026-09-13 22:45 Australia/Brisbane

- gigaconnectome candidate `dc1439d82ec42fd3cb5b38e85ca1d5800a3484b2` passed exact native run [34757505350](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757505350): 94/94 checks passed. The ARM64 path uses the official Python 3.9 Bookworm base after the Bullseye mirror failure; the x86_64 image path is preserved. Integrating this tested candidate now.
- DeepLabCut `0ed4b3c91637e7bee190bbfb66ba2ddfa0edbeeb` remains active in [34757340002](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757340002).
- SovaBIDS `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` remains active in [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235).
- ROMEO `0291d268b03c1840639d452f5be7952edd73d01c` remains active in [34757529921](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757529921).
- OpenADS CPU candidate `d351f60f31c5f6cb6e9f467b777423a8638b584f` is prepared on `arm64/openadscpu-rshrf`, validated for ARM64 and x86_64 generation, and ready for the freed slot.
- Next action: push the integrated gigaconnectome pin, refresh coverage, dispatch OpenADS CPU, then reconcile the remaining exact runs before selecting another candidate.

## Active implementation checkpoint — 2026-09-13 22:55 Australia/Brisbane

- Accepted top-level pin: root `0f1fc1993b3000c4eec1800289b1a822e2e705f6`; submodule `dc1439d82ec42fd3cb5b38e85ca1d5800a3484b2` (`arm64/gigaconnectome-rshrf`). Gigaconnectome is natively verified by run [34757505350](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757505350), 94/94, and is integrated in the root pin.
- DeepLabCut final replay: branch `arm64/integrate-deeplabcut-gigaconnectome`, candidate `4d92aaab39c59ea92490b8e456c088633467379e`, run [34758030010](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758030010), in progress. Prior pre-integration candidate passed 101/101 but is not accepted.
- SovaBIDS: branch `arm64/sovabids`, candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3`, run [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235), in progress, application attempt 3/6. Two configuration fixes have already addressed qmake discovery and SIP's config-setting syntax.
- OpenADS CPU: branch `arm64/openadscpu-gigaconnectome`, candidate `f93cd2d27d38d979ceba1b49a88b105312ae8146`, run [34758279055](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758279055), in progress, attempt 2/6. Added ARM-only CMake and image-library development packages after attempt 1's antspyx/ITK PNG/ZLIB discovery failure.
- Convert3D: branch `arm64/convert3d-gigaconnectome`, candidate `c68cb38d776f5c112b6945d585350a15affcc8c5`, run [34758333296](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758333296), queued, attempt 1/6. ARM route builds pinned upstream c3d v1.3.0 source with Debian ITK; x86 nightly archive route is unchanged.
- ROMEO: candidate `0291d268b03c1840639d452f5be7952edd73d01c`, run [34757529921](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34757529921), failed runtime: native build/SIF succeeded, but 15/104 suite tests passed and 89 failed because the Julia route does not implement the legacy ROMEO CLI contract. Candidate remains on `arm64/romeo-rshrf`; no accepted pin change.
- DSI Studio and LST-AI remain bounded blockers recorded in issues [195](https://github.com/Vbitz/neurocontainers-arm64/issues/195) and [207](https://github.com/Vbitz/neurocontainers-arm64/issues/207). No retry is queued without a changed upstream/runtime condition.
- Current checkout: root `main`, submodule `arm64/gigaconnectome-rshrf`, clean and aligned with the accepted pin. Active build capacity is full. Next action: reconcile completed runs, integrate exact passing candidates serially, and refill each freed slot from the unattempted plausible plans.

## Active implementation checkpoint — 2026-09-13 23:06 Australia/Brisbane

- DeepLabCut candidate `4d92aaab39c59ea92490b8e456c088633467379e` is being accepted from exact native run [34758030010](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758030010): ARM64 build, SIF conversion, deploy checks, and 101/101 fulltest checks passed. It is based directly on the accepted gigaconnectome pin `dc1439d82ec42fd3cb5b38e85ca1d5800a3484b2`.
- SovaBIDS candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` remains in exact run [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235), application attempt 3/6. The two configuration corrections addressed qmake discovery and SIP's pip configuration syntax; the remaining result will determine whether the pinned PyQt source route is viable.
- OpenADS CPU candidate `f93cd2d27d38d979ceba1b49a88b105312ae8146` remains in [34758279055](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758279055), attempt 2/6, after adding ARM image-library development packages for antspyx's CMake probe.
- Convert3D candidate `9751eadaa69100b6852b9a408fb2c8f940c1de73` is in [34758515536](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758515536), attempt 2/6. It builds upstream ITK 5.3.0 from source because Debian and Ubuntu do not publish the required `libinsighttoolkit5-dev` package for ARM64.
- FetalSynthSeg candidate `76966107d77a038bc2ab0ed864502373bf81e4b2` is pushed on `arm64/fetalsynthseg-gigaconnectome`, validated, and generated for ARM64 and x86_64. It uses upstream source commit `03c439edef02fc830e31a38169c5aa09ca98eeb4`, the official `KISPI-all_fss.ckpt` checkpoint, and a Python 3.10 Bookworm ARM64 base. It is waiting for a runner slot.
- ROMEO launcher candidate `2e51a465affc5e6a872d1952e378d7610b74ea48` is pushed on `arm64/romeo-rshrf`, with a narrow upstream extension-loading fix ready for dispatch when a slot opens. The prior candidate remains a failed runtime result because its Julia launcher did not implement the recipe's legacy CLI contract.
- Current checkout is the DeepLabCut integration branch; root pointer is staged for this accepted candidate only after the root checkpoint is committed. Fork Actions remains disabled. The next action is to commit and push this submodule pointer, refresh issue #2, then dispatch the first waiting candidate as soon as a slot frees.

## Active implementation checkpoint — 2026-09-13 23:21 Australia/Brisbane

- FetalSynthSeg is accepted at submodule pin `e673b917ca5a8ae6e6f7ec74da961cb62e99fc5e`; exact native run [34759079934](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759079934) passed ARM64 build/SIF conversion, deploy checks, and 4/4 fulltest checks. Root acceptance commit is `0e1e58a58c166aff278a9e5a116da4a2c2031ba2`.
- OpenADS CPU pre-integration candidate passed 3/3 in [34758279055](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34758279055). Its two commits were replayed onto the FetalSynthSeg accepted pin as candidate `6103a923f43106c039ddf22a59c99c25352e459b` on `arm64/integrate-openads-fetalsynthseg`; exact integrated run [34759549792](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759549792) is queued.
- Convert3D candidate `3ace005bc8e3897cca655933e0ecc36dcbea6222` on `arm64/convert3d-gigaconnectome` replaces the unavailable shallow checkout with the exact pinned C3D source archive. Exact run [34759364144](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759364144) is in progress, attempt 3/6; the prior attempt built ITK then failed before C3D compilation because the shallow checkout lacked the historical commit.
- Quickshear candidate `728ddc01946474919fa56478f989c787dbf1a26a` is replayed onto the FetalSynthSeg pin on `arm64/integrate-quickshear-fetalsynthseg`; validation and both architecture generations pass. Exact native run [34759506409](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759506409) is in progress, attempt 1/6.
- SovaBIDS exact candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` had a runner termination after 59 minutes with no logs, artifacts, build, or test result. The single allowed unchanged infrastructure retry is attempt 2 of run [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235), while the recipe application investigation remains attempt 3/6.
- Current checkout: root `main`, submodule `arm64/integrate-openads-fetalsynthseg` at `6103a923f43106c039ddf22a59c99c25352e459b`; root pointer is intentionally uncommitted until integrated OpenADS verification passes. Four workflow slots are occupied by Sova retry, Convert3D, Quickshear, and integrated OpenADS. ROMEO remains prepared for the next freed slot.

## Active implementation checkpoint — 2026-09-13 23:24 Australia/Brisbane

- OpenADS CPU integrated candidate `6103a923f43106c039ddf22a59c99c25352e459b` is queued in [34759549792](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759549792) after the pre-integration candidate passed 3/3.
- Quickshear candidate `728ddc01946474919fa56478f989c787dbf1a26a` is in [34759506409](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759506409), attempt 1/6, with the official SynthStrip ARM64 runtime route.
- SovaBIDS is on unchanged infrastructure retry 2 of run [34756526235](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34756526235); the recipe application investigation remains attempt 3/6.
- Convert3D exact candidate `3ace005bc8e3897cca655933e0ecc36dcbea6222` is in [34759364144](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759364144), attempt 3/6, testing the pinned C3D archive after ITK source build succeeded.
- ROMEO integrated candidate `d3dc7e78e987057c381f1e6fa68a87f9be5e63cb` is pushed on `arm64/integrate-romeo-fetalsynthseg`, validated for both architectures, and waiting for a slot. Elastix candidate `8fc287ee` is pushed on `arm64/elastix-fetalsynthseg`, validated and generated for both architectures; it builds pinned Elastix 5.1.0 plus ITK 5.3.0 from official source archives on ARM64 and preserves the x86_64 release asset.
- Current checkout: root `main`, submodule `arm64/elastix-fetalsynthseg` at `8fc287ee`; root pointer remains intentionally uncommitted. The next actions are to review the four active runs, integrate exact passing candidates serially onto the accepted pin, and dispatch ROMEO or Elastix as slots free.

## Active implementation checkpoint — 2026-09-13 23:39 Australia/Brisbane

The accepted top-level source remains `e673b917ca5a8ae6e6f7ec74da961cb62e99fc5e`; fork Actions is still disabled. The local submodule checkout is `arm64/integrate-convert3d-fetalsynthseg` at `cc184c96741fb8dd2058107e4d68034161ac95d7`, intentionally unaccepted while its exact run completes. Four runner slots are occupied:

- OpenADS CPU candidate `6103a923f43106c039ddf22a59c99c25352e459b` is in exact integrated run [34759549792](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759549792), after its pre-integration candidate passed 3/3.
- Quickshear candidate `78b50a88e34e9942f5d90ac95e2cc093f8d49b4a` is in exact run [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970). It adds Ubuntu `python-is-python3` after the prior run showed the official SynthStrip script's `python` shebang failing with exit 127.
- Convert3D candidate `cc184c96741fb8dd2058107e4d68034161ac95d7` is in exact run [34760271991](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760271991), replayed onto the accepted FetalSynthSeg pin. It adds the ITK-documented C++14 setting after the source build reached C3D compilation and failed on C++14-only ITK 5.3 headers.
- ROMEO candidate `d3dc7e78e987057c381f1e6fa68a87f9be5e63cb` is in exact run [34760348265](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760348265), replayed onto the accepted FetalSynthSeg pin. It restores the upstream ROMEO application entry point and legacy CLI contract.

SovaBIDS candidate `a4757fef0ea1c5723e264a9bf6fa41e10dadcad3` is recorded as `blocked-infrastructure` in issue [#167](https://github.com/Vbitz/neurocontainers-arm64/issues/167#issuecomment-5653614496) after its one allowed unchanged retry. Both native jobs reached the pinned PyQt5 5.15.11 source build and ended with exit 143 without a compiler diagnostic or test artifact; no further unchanged retry is planned. Convert3D's previous exact run [34759364144](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759364144) is recorded in issue [#133](https://github.com/Vbitz/neurocontainers-arm64/issues/133#issuecomment-5653606033) as the C++14 configuration failure; the new attempt is the only active retry for that changed hypothesis. The invalid Quickshear dispatch [34760107036](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760107036) was cancelled during checkout before build execution and is recorded in issue [#228](https://github.com/Vbitz/neurocontainers-arm64/issues/228#issuecomment-5653591438).

Waiting, validated candidates based on the accepted FetalSynthSeg pin are FSL `68f591a2736d5ac150847f7e337426aea7479bcd` on `arm64/fsl-fetalsynthseg`, Elastix `8fc287eeec2679bf502dd7b44979d06dd0c8fb9d` on `arm64/elastix-fetalsynthseg`, and the current ROMEO candidate above. Dispatch the next one only after reconciling a completed active run; do not duplicate any active recipe or rerun an unchanged passed candidate. When a candidate passes, integrate its intended commits serially from the newest accepted pin and rerun the exact integrated SHA if its original run predates that pin.

## Active implementation checkpoint — 2026-09-13 23:44 Australia/Brisbane

- CIVET candidate `8132ea70` is pushed on `arm64/civet-fetalsynthseg`, based on accepted pin `e673b917ca5a8ae6e6f7ec74da961cb62e99fc5e`. It adds ARM64 and renders CIVET's `Linux-{{ arch }}` build/runtime paths; fulltest path checks now follow native `uname -m`. Validation and ARM64/x86_64 generation passed.
- CIVET issue [#130](https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653651154) records the candidate, investigation window `2026-09-13T13:44:15Z`–`2026-09-14T01:44:15Z`, and next action to dispatch when a slot opens.
- Current local checkout is root `main` at `40ed139`, with submodule `arm64/civet-fetalsynthseg` at `8132ea70`; the root pointer remains intentionally uncommitted. Four native runs remain active: OpenADS [34759549792](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759549792), Quickshear [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970), Convert3D [34760271991](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760271991), and ROMEO [34760348265](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760348265).
- Next action: reconcile the first completed run, integrate only an exact passing candidate, then dispatch FSL, Elastix, or CIVET into the freed slot while preserving the current accepted pin.

## Active implementation checkpoint — 2026-09-13 23:49 Australia/Brisbane

- OpenADS CPU is accepted at submodule pin `6103a923f43106c039ddf22a59c99c25352e459b`; exact native run [34759549792](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34759549792) passed build, SIF conversion, deploy checks, and 3/3 fulltest checks. Root acceptance commit is `83329ad`.
- FSL candidate `376177f3214085eb471f03054f9e8d8adaba65be` is replayed onto the OpenADS accepted pin on `arm64/integrate-fsl-openads`, pushed and validated for ARM64/x86_64 generation. The exact corrected dispatch is [34760837466](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760837466); the canceled checkout-only dispatch [34760802896](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760802896) used a malformed ref and is metadata-only.
- CIVET candidate `8132ea70` remains validated and waiting on `arm64/civet-fetalsynthseg`; issue [#130](https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653651154) records its investigation window. Elastix `8fc287ee` remains waiting on its prepared branch.
- Active native runs are Quickshear [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970), Convert3D [34760271991](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760271991), ROMEO [34760348265](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760348265), and FSL [34760837466](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760837466). The local submodule is `arm64/integrate-fsl-openads` at `376177f3`; the root pointer remains intentionally uncommitted.
- Next action: reconcile the first completed run, serially accept any exact passing candidate, refresh coverage, and dispatch CIVET or Elastix into the next free slot after replaying it onto the newest accepted pin.

## Active implementation checkpoint — 2026-09-13 23:54 Australia/Brisbane

- ROMEO integrated candidate `d3dc7e78e987057c381f1e6fa68a87f9be5e63cb` failed exact run [34760348265](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760348265): build/SIF passed, but 15/104 fulltest checks passed because `StatsBase` was not instantiated. The concrete error is recorded in [issue #164](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5653679626).
- ROMEO retry candidate `c788ce6e2837aeaebfd1afe4a34784cf674eeba6` is correctly based directly on accepted OpenADS pin `6103a923f43106c039ddf22a59c99c25352e459b`, on `arm64/integrate-romeo-openads`, pushed and validated for both architectures. It adds `Pkg.instantiate()` before package additions; the earlier `6c0e3abc` branch inherited unaccepted FSL and was never dispatched.
- Convert3D attempt 4 failed [34760271991](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760271991) because its CMakeLists resets C++11 despite the cache setting. Final candidate `11d634d6270ec6ffa0303c46219427b72178630b` adds an explicit `-std=c++14` compiler flag and is dispatched in [34761033940](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761033940), attempt 5/6.
- FSL exact candidate `376177f3214085eb471f03054f9e8d8adaba65be` is active in [34760837466](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760837466). Quickshear remains active in [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970). ROMEO corrected candidate is queued for the next slot; CIVET and Elastix remain validated/waiting.
- Current local submodule is `arm64/integrate-romeo-openads` at `c788ce6e`; root remains `main` at `27b1234` with the pointer intentionally uncommitted. Next action: reconcile Convert3D/FSL/Quickshear, dispatch corrected ROMEO or the next queued candidate as slots free, and integrate only exact passing candidates.

## Active implementation checkpoint — 2026-09-13 23:53 Australia/Brisbane

- Corrected ROMEO candidate `c788ce6e2837aeaebfd1afe4a34784cf674eeba6` is in exact native run [34761092200](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761092200). It is based directly on accepted OpenADS pin `6103a923f43106c039ddf22a59c99c25352e459b` and includes the `Pkg.instantiate()` fix.
- Four workflow slots are now occupied by Quickshear [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970), FSL [34760837466](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760837466), Convert3D [34761033940](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761033940), and ROMEO [34761092200](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761092200). CIVET and Elastix remain validated/waiting.
- Current local submodule is `arm64/integrate-romeo-openads` at `c788ce6e`; root `main` is `5e9e5ae` with the submodule pointer intentionally uncommitted. Next action: reconcile completed runs, integrate exact passing candidates serially, then refill each freed slot from CIVET, Elastix, or the next feasible plan.

## Active implementation checkpoint — 2026-09-13 23:59 Australia/Brisbane

- CIVET has been replayed onto accepted OpenADS pin `6103a923f43106c039ddf22a59c99c25352e459b` as candidate `dfc9bb57a627cf6fa4c35b0fa2e95d6c6148fcad` on `arm64/integrate-civet-openads`; validation and both architecture generations pass. It is waiting for a native slot; issue [#130](https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653708673) records the corrected candidate.
- Elastix has been replayed onto the same accepted pin as candidate `cd8bbc9679b2b80535d20d61fbb5fcbe54ab9dc3` on `arm64/integrate-elastix-openads`; validation and both architecture generations pass. It is queued for a native slot; issue [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92#issuecomment-5653711644) records the source-build hypothesis.
- Active exact runs remain Quickshear [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970), FSL [34760837466](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760837466), Convert3D [34761033940](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761033940), and ROMEO [34761092200](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761092200). No additional recipe is dispatched until one completes.
- Current local submodule is `arm64/integrate-elastix-openads` at `cd8bbc96`; root `main` is `26b9c0f` with pointer intentionally uncommitted. Next action: reconcile the four runs, accept exact passes serially, then dispatch CIVET or Elastix from this current accepted base.

## Active implementation checkpoint — 2026-09-14 00:09 Australia/Brisbane

- ROMEO candidate `c788ce6e2837aeaebfd1afe4a34784cf674eeba6` failed exact native run [34761092200](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761092200): ARM64 build/SIF passed, but the Julia ROMEO CLI again passed only 15/104 runtime checks. Issue [#164](https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5653761465) records the repeated runtime failure, the Julia package-extension error, the two attempted configuration fixes, and the bounded stop condition.
- CIVET candidate `dfc9bb57a627cf6fa4c35b0fa2e95d6c6148fcad` is dispatched in exact native run [34761692429](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761692429), attempt 1/6, on issue [#130](https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653764998).
- Blender candidate `e136c09bb421422652358d5c8fe7a8f0bfec3b9c` is pushed on `arm64/blender-openads`, based on accepted pin `6103a923f43106c039ddf22a59c99c25352e459b`. It adds the documented ARM64 source build using Blender v5.0.1, `install_linux_packages.py`, `make deps`, and `make`, while preserving the x86_64 binary route. Validation and ARM64/x86_64 generation pass; issue [#122](https://github.com/Vbitz/neurocontainers-arm64/issues/122#issuecomment-5653774839) records it as queued, attempt 0/6.
- FSL [34760837466](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760837466), Quickshear [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970), and Convert3D [34761033940](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34761033940) remain active. Elastix candidate `cd8bbc9679b2b80535d20d61fbb5fcbe54ab9dc3` is validated and queued on issue [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92#issuecomment-5653711644).
- Accepted top-level submodule pin remains `6103a923f43106c039ddf22a59c99c25352e459b`; root `main` is `a931c5db0f719accebf53b7a3759931ecc2c2a8b`. The local submodule is `arm64/blender-openads` at `e136c09b`; the root pointer is intentionally uncommitted while this candidate and the queued candidates await native verification. Fork Actions remains disabled.
- Next action: reconcile the first completed native run, integrate only its exact passing candidate serially, and dispatch Elastix or Blender as slots open. If the current shared FSL template candidate passes, replay queued FSL-dependent candidates from the new accepted pin before dispatch.

## Active implementation checkpoint — 2026-09-14 00:15 Australia/Brisbane

- Goal remains active: implement and natively verify every feasible recipe from the 148-recipe research inventory; do not declare completion while feasible queue remains.
- Top-level branch: `main`; root commit: `542f3d1` (`Checkpoint ARM64 recipe implementation queue`).
- Accepted top-level submodule pin: `6103a923f43106c039ddf22a59c99c25352e459b` (OpenADS CPU accepted after FetalSynthSeg); root pointer remains intentionally unstaged while candidate work is checked out.
- Local submodule checkout: branch `arm64/blender-openads`, candidate `e136c09bcd6146e05268d3345eeefd4d2787640c`, clean and pushed. It has been dispatched and can be switched away safely.
- Active native ARM64 runs (four-slot limit): Quickshear `34760141970` (candidate `78b50a88e34e9942f5d90ac95e2cc093f8d49b4a`, runtime tests); FSL `34760837466` (candidate `376177f3214085eb471f03054f9e8d8adaba65be`, runtime tests); Elastix `34762067564` (candidate `cd8bbc9679b2b80535d20d61fbb5fcbe54ab9dc3`); Blender `34762069436` (candidate `e136c09bcd6146e05268d3345eeefd4d2787640c`).
- Completed outcomes: Convert3D candidate `11d634d6270ec6ffa0303c46219427b72178630b`, run `34761033940`, blocked-upstream after ITK 5.3/C3D C++11-vs-C++14 incompatibility; CIVET candidate `dfc9bb57a627cf6fa4c35b0fa2e95d6c6148fcad`, run `34761692429`, blocked-upstream after pinned Netpbm 10.35.94 ARM64 build failures and legacy HDF5 1.8.8/NetCDF 3.6.1 configure failures. Issue comments record exact errors and revisit conditions.
- Issue checkpoints: Convert3D blocker `https://github.com/Vbitz/neurocontainers-arm64/issues/133#issuecomment-5653798905`; CIVET blocker `https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653806029`; Elastix dispatch `https://github.com/Vbitz/neurocontainers-arm64/issues/92#issuecomment-5653806019`; Blender SHA correction/dispatch `https://github.com/Vbitz/neurocontainers-arm64/issues/122#issuecomment-5653806021`.
- Next action: inspect the four active runs at normal intervals; meanwhile switch the local submodule to the accepted pin and prepare the next bounded source or package route from the promising queue (AFNI, BIDSvue, ITK-SNAP, ROOT, MuscleMap, SurfIce, or PyDeface after FSL's shared template result). Keep completed/blocked recipes out of the queue.

## Active implementation checkpoint — 2026-09-14 00:35 Australia/Brisbane

Goal remains active: implement and natively verify every feasible ARM64 recipe; do not close while eligible feasible recipes remain.

Current root commit: f3f6cdc. Accepted top-level submodule pin: 6103a923f43106c039ddf22a59c99c25352e459b. Fork Actions permission remains disabled.

Current local submodule checkout: branch arm64/dsistudio-openads, clean, candidate a261c44525bf7e16a607363d862248c985501828, based directly on the accepted pin. AFNI candidate 24dabfa115f94bf7ad569c8771392b23610a818e and Blender retry 3a54628be2fc312f43ae8aa45646e882330c8cd4 are pushed. FSL deploy correction 9a5ae40c67667a088f50f0e9885833b983893f98 is pushed and waiting for a slot.

Active native ARM64 runs:
- Quickshear: 34760141970, candidate 78b50a88e34e9942f5d90ac95e2cc093f8d49b4a; runtime/fulltest active.
- Elastix: 34762067564, candidate cd8bbc9679b2b80535d20d61fbb5fcbe54ab9dc3; build active.
- AFNI: 34762470058, candidate 24dabfa115f94bf7ad569c8771392b23610a818e; exact dispatch active.
- Blender: 34762534470, candidate 3a54628be2fc312f43ae8aa45646e882330c8cd4; exact retry active.

Recent outcomes:
- Convert3D blocked-upstream after five attempts: C3D 61753cca with ITK 5.3.0 remains forced to C++11 despite recipe flags; issue comment https://github.com/Vbitz/neurocontainers-arm64/issues/133#issuecomment-5653798905.
- CIVET blocked-upstream: legacy Netpbm, HDF5 1.8.8, and NetCDF 3.6.1 fail on aarch64; issue comment https://github.com/Vbitz/neurocontainers-arm64/issues/130#issuecomment-5653806029.
- ROMEO failed-runtime after three attempts: upstream Julia dependency precompile error remains after CLI and instantiate fixes; issue comment https://github.com/Vbitz/neurocontainers-arm64/issues/164#issuecomment-5653761465.
- FSL candidate 376177f3214085eb471f03054f9e8d8adaba65be built and passed 128 functional tests; only the deploy path failed, now corrected in 9a5ae40c.
- Blender first candidate failed because the official dependency installer required sudo/doas; retry adds sudo as an ARM build prerequisite.
- DSI Studio candidate a261c445 is prepared and waiting; it updates to official 2026.7.25 archives and normalizes the fulltest to the upstream atlas/tract layout. Issue: https://github.com/Vbitz/neurocontainers-arm64/issues/195.

Next actions: monitor the four active runs; record exact outcomes; dispatch FSL and DSI Studio serially as slots open; integrate only candidates whose exact native build, SIF conversion, deploy checks, and fulltest all pass; continue through the remaining feasible inventory.


## Active implementation checkpoint — 2026-09-14 00:42 Australia/Brisbane

Goal remains active: implement and natively verify every feasible recipe from the 148-recipe research inventory; do not close while an eligible feasible route remains.

- Root branch is `main` at `0ef4f866af7d6b0add82d17dace9d10628653dd0`; accepted top-level submodule pin remains `6103a923f43106c039ddf22a59c99c25352e459b`. Fork Actions remains disabled.
- Local submodule checkout is clean on `arm64/dsistudio-openads` at candidate `0e7e2230b8e77411e03bf20431cb0488ba0902d3`; the root submodule pointer is intentionally modified while candidate work is dispatched.
- Four native ARM64 slots are occupied: FSL corrected candidate `9a5ae40c67667a088f50f0e9885833b983893f98` in run [34762946871](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34762946871); AFNI retry `a51788253403b44c819d4273a134eedfe822aad3` in run [34763111015](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763111015); Blender attempt 3 `e885463c45c0fb902a9e6747ffcc80914045d63f` in run [34763301992](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763301992); DSI Studio attempt 2 `0e7e2230b8e77411e03bf20431cb0488ba0902d3` in run [34763301952](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34763301952).
- Quickshear run [34760141970](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34760141970) has completed with failure after build/SIF; its artifact is pending first-error review. DSI Studio run [34762948512](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34762948512) failed 23/83 because the release supplied XCB but the fulltest forced offscreen, and several checks used stale asset paths; attempt 2 tests a display-aware Xvfb route and current archive paths.
- Elastix is recorded as blocked-upstream in issue [#92](https://github.com/Vbitz/neurocontainers-arm64/issues/92#issuecomment-5653939321) after ITK 5.3.0 failed at `uint8_t` declaration in `itkMathematicalMorphologyEnums.h` before Elastix compilation.
- Blender attempt 3 installs the Ubuntu equivalents listed by Blender's dependency checker; AFNI attempt 2 uses the ARM archive's extracted R bundle directory. Both candidates validated for ARM64/x86_64 generation before dispatch.

Next action: inspect completed Quickshear and the four active runs at normal intervals; integrate exact passing candidates serially from the current accepted pin, and refill each freed slot from the remaining feasible queue. Do not rerun recipes whose exact native evidence already passed.
## Active implementation checkpoint — 2026-09-14

The goal remains active: implement and natively verify every feasible recipe from the 148-recipe inventory, and record a concrete blocker for every recipe that remains infeasible. The accepted top-level submodule pin is `685f5f4d9636d34aa8237646535d2a7dfc3a525d`; fork Actions remains disabled.

Current native runs to reconcile:

- CLEARSWI integrated candidate `488f143223358f000b57fdc06b2693a89b896110`, run [34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906).
- ITK-SNAP integrated final source retry `258f746afb80f90077beb6fb63d0a336745fbb1e`, run [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451).
- MIMoSA candidate `c58b71e8e7400e0beb6026201b323c5d7aa3916d`, run [34773252089](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773252089).

TractSeg candidate `a6bd2f46399657df8b56cfc12ce48f147796d1fc` is pushed on `arm64/tractseg-modern-arm`, based on the accepted pin, and waiting for a native slot. It uses the documented MRtrix3 3.0.4 source build on ARM64 because the release has no Linux ARM64 archive, and uses the native torch 2.4.1 wheel because the old torch 1.6.0 CPU path has no ARM64 wheel. Validation and both architecture generations passed. Issue checkpoint: [#238 comment](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5655429034). Investigation window is `2026-09-13T19:06:28Z`–`2026-09-14T07:06:28Z`, attempt 1/6.

Recent bounded outcomes: DSI Studio is blocked on five essential ARM64 AutoTrack runtime operations after a native build; Blender exhausted its six-attempt budget at the bundled Flex configure step (`autopoint`), with an untested dependency candidate preserved; EMUSES passed and is accepted at the current pin. Do not duplicate these runs without new upstream or integration evidence.

Next actions: reconcile the three active runs, dispatch TractSeg when a slot opens, integrate exact passing candidates serially from the newest accepted pin, and continue through the remaining feasible queue. Preserve the local candidate branch and do not stage the intentional submodule pointer until a candidate is verified.

## Active implementation checkpoint — 2026-09-14 05:16 Australia/Brisbane

TractSeg candidate `a6bd2f46399657df8b56cfc12ce48f147796d1fc` had a pre-build infrastructure failure in run [34776715361](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776715361): Zenodo returned HTTP 504 for the declared `best_weights_ep62.npz` after the builder's three retries. The candidate and recipe remain unchanged. The one allowed unchanged retry is now queued/in progress as [34777140518](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777140518), attempt 2/6; the original investigation window remains `2026-09-13T19:06:28Z`–`2026-09-14T07:06:28Z`.

Accepted top-level submodule pin remains `685f5f4d9636d34aa8237646535d2a7dfc3a525d`; root `main` remains at `3052705`; local submodule is clean on `arm64/accepted-work` at the accepted pin. Active native runs are CLEARSWI [34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906), ITK-SNAP [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451), MIMoSA [34773252089](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34773252089), and the TractSeg retry above. Do not dispatch another recipe until one of these four runs completes; then refill the slot with the next unattempted feasible plan.

Candidate queued: `brainles-preprocessing` candidate `2f061f36896188f8be2d00b73519d819c8c2d164` on `arm64/brainles-preprocessing-source`, based on accepted pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`. It adds the documented ARM64 antspyx source-build route (`antspyx==0.5.4`, `--no-binary=antspyx`) with native CMake/ITK prerequisites, while preserving the x86_64 wheel route. Local recipe validation and both architecture Dockerfile generations passed. Issue [#186](https://github.com/Vbitz/neurocontainers-arm64/issues/186) records the reopened source investigation. Dispatch only after a current run completes; do not count the old preflight as a source-build attempt.

TractSeg candidate `a6bd2f46399657df8b56cfc12ce48f147796d1fc` is blocked-infrastructure after the one permitted unchanged retry: [run 34777140518](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777140518) received another Zenodo HTTP 504 for `best_weights_ep266.npz` after three retries, following the first run's identical 504 for a different weight. Issue [#238](https://github.com/Vbitz/neurocontainers-arm64/issues/238#issuecomment-5655494602) records the result and revisit condition. No further TractSeg retry is planned without a reachable artifact or stable mirror.

BrainLesion source candidate `2f061f36896188f8be2d00b73519d819c8c2d164` is dispatched in [run 34777430024](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777430024), attempt 1/6, from `arm64/brainles-preprocessing-source`. Active runs are CLEARSWI [34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906), ITK-SNAP [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451), and BrainLesion [34777430024](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777430024); one native slot remains available for the next candidate after reconciling these runs.

BrainLesion's first attempt failed in pre-build staging with Zenodo HTTP 504 for `hdbet_0_model`; the one permitted unchanged retry is queued as [run 34777631695](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777631695), attempt 2/6. Active native runs are CLEARSWI [34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906), ITK-SNAP [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451), and BrainLesion [34777631695](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777631695); one slot is available for Napari.

Napari candidate `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc` is dispatched in [run 34777662542](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777662542), attempt 1/6, from `arm64/napari-cpu-arm`. Four native slots are now occupied: CLEARSWI [34775763906](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34775763906), ITK-SNAP [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451), BrainLesion [34777631695](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777631695), and Napari [34777662542](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777662542). Prepare the next candidate while these runs execute; dispatch only as slots free.

Candidate queued: Napari `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc` on `arm64/napari-cpu-arm`, based on accepted pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`. It preserves the x86_64 CUDA route and uses the official PyTorch CPU index for matching Linux ARM64 torch/torchvision wheels. Local validation and both architecture generations passed. Issue [#219](https://github.com/Vbitz/neurocontainers-arm64/issues/219) records the new evidence and candidate. Dispatch when a native slot is available; one slot is currently free.

Candidate queued: TopoFit `383a955c977619a8c64d2e2340ff724f551fe8f9` on `arm64/topofit-cortech-arm`, based on accepted pin `685f5f4d9636d34aa8237646535d2a7dfc3a525d`. It uses the documented Cortech Conan/Meson source build with native `armv8` settings and an ARM64 CPU PyTorch wheel, while preserving the x86_64 CUDA/wheel route. Local validation and both architecture generations passed. Issue [#236](https://github.com/Vbitz/neurocontainers-arm64/issues/236) records the candidate. Dispatch when a slot frees; all four current runs remain active.

## Active implementation checkpoint — 2026-09-14

- BrainLesion source candidate `2f061f36896188f8be2d00b73519d819c8c2d164` is blocked-infrastructure after its two permitted native attempts, [34777430024](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777430024) and [34777631695](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777631695), both failed during pre-build staging on Zenodo HTTP 504 for `hdbet_0_model`. The source build was not reached. Issue [#186](https://github.com/Vbitz/neurocontainers-arm64/issues/186#issuecomment-5655583825) records the blocker and revisit condition.
- Napari candidate `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc` passed exact native run [34777662542](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34777662542): ARM64 build, SIF, deploy and fulltest all passed, with 4/4 tests and no skips. It is ready for serial acceptance from the current pin.
- Napari is now accepted serially: the top-level submodule pin is `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc`, with final evidence in [issue #219](https://github.com/Vbitz/neurocontainers-arm64/issues/219#issuecomment-5655589051). Future candidates must be replayed from this pin before dispatch or acceptance.
- Current local submodule is clean on `arm64/napari-cpu-arm` at the accepted candidate; the root pointer is staged for this acceptance checkpoint. ITK-SNAP run [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451) is still active. TopoFit candidate `383a955c` and any other candidate based on the former `685f5f4d` pin require replay onto `8bcc3e3d` before dispatch.
- TopoFit has been replayed onto the accepted Napari pin as integrated candidate `c8e10fe8e0263b5ceecb53489856daf332ddf419` on `arm64/topofit-cortech-arm-integrated`; recipe validation and both architecture generations pass. It is ready for native dispatch in the freed slot while ITK-SNAP run [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451) continues.
- TopoFit is now dispatched from that exact integrated SHA in [run 34778187761](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778187761), attempt 1/6. Active native work is ITK-SNAP [34776098451](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34776098451) and TopoFit [34778187761](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778187761); two runner slots remain available for the next candidates after their state is recorded.
- MIMoSA’s previously green recipe was replayed with both required commits onto the accepted pin as `5341ef2ec334b3d82589af78a2e17cfc5dd63a80` on `arm64/mimosa-bids-integrated-v2`; local validation and both architecture generations pass. Exact integration run [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112) is attempt 4/6. Three native runs are now active: ITK-SNAP, TopoFit and MIMoSA; one slot remains.
- VesselBoost candidate `0e80eb6d366ef992c52e3b6777af599ae5dc004e` is dispatched in [run 34778576148](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778576148), attempt 1/6, from `arm64/vesselboost-cpu-arm`. It uses the documented CPU mode, official ARM64 PyTorch wheels and an antspyx source build. Four native slots are occupied: ITK-SNAP, TopoFit, MIMoSA and VesselBoost. No additional dispatch is planned until a slot completes.

## Active implementation checkpoint — 2026-09-14 (continued)

- Goal remains active. Accepted top-level submodule pin is `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc`; fork Actions remains disabled.
- Local submodule is clean on `arm64/itksnap-qt6-compat-8bcc` at candidate `c14b22703394ab8ed56510580ef8c381605fb9ec`; the root pointer is intentionally modified while candidate work is dispatched.
- TopoFit retry candidate `1e161313793613e5c6e8b3ae086e6e5488028eac` adds `ninja-build` after exact run `34778187761` failed at meson-python's missing Ninja check. Local validation and ARM64/x86_64 generation passed. Exact retry is [run 34778828330](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778828330), attempt 2/6, on issue [#236](https://github.com/Vbitz/neurocontainers-arm64/issues/236#issuecomment-5655679365).
- VesselBoost candidate `0e80eb6d366ef992c52e3b6777af599ae5dc004e` was originally dispatched with a short ref in `34778576148` and failed before checkout; that run is metadata-only. The corrected full-SHA dispatch is [run 34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), attempt 1/6, recorded on issue [#239](https://github.com/Vbitz/neurocontainers-arm64/issues/239#issuecomment-5655681204).
- ITK-SNAP candidate `c14b22703394ab8ed56510580ef8c381605fb9ec` replays the complete source route onto the accepted pin and fixes the remaining localized Qt 6.4 `QDebug`/`std::string` expressions in `SSHTunnelTest`. Exact retry is [run 34778923438](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778923438), attempt 2/6, on issue [#148](https://github.com/Vbitz/neurocontainers-arm64/issues/148#issuecomment-5655689337).
- ITK-SNAP run 34778923438 failed before build because the retry's Python lambda was parsed by YAML as a mapping, producing an invalid shell command. Candidate `817d0c540376842f9b63304be53f7c7b0f1538a4` replaces it with explicit replacements; validation and both generations pass. Exact retry is [run 34779151809](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779151809), attempt 3/6, on issue [#148](https://github.com/Vbitz/neurocontainers-arm64/issues/148#issuecomment-5655716502).
- MIMoSA integrated candidate `5341ef2ec334b3d82589af78a2e17cfc5dd63a80` remains in [run 34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112). Review its exact source metadata and fulltest before any acceptance.
- Four native jobs are now active: MIMoSA, TopoFit retry, VesselBoost corrected dispatch, and ITK-SNAP retry. Do not dispatch another recipe until a slot completes. Next queue candidates remain SoopCT and other unattempted feasible source/package routes; do not repeat already passing or bounded-blocked recipes.
- SoopCT candidate `d4566cb95d73717f55176350179fb8cb8f1f776f` is pushed on `arm64/soopct-antspyx-source`, based on accepted pin `8bcc3e3d`; local validation and both architecture generations pass. Issue [#232](https://github.com/Vbitz/neurocontainers-arm64/issues/232#issuecomment-5655706831) records it as queued. Dispatch its exact full SHA as soon as one native slot completes.

## Active implementation checkpoint — 2026-09-14 (ITK-SNAP correction)

- The four current native slots are MIMoSA [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112), TopoFit [34778828330](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778828330), VesselBoost [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), and ITK-SNAP [34779151809](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779151809).
- ITK-SNAP run `34778923438` failed before source build due a YAML-to-shell quoting defect in the retry command; it did not test the application. Corrected candidate `817d0c540376842f9b63304be53f7c7b0f1538a4` is pushed and dispatched as attempt 3/6. Issue [#148](https://github.com/Vbitz/neurocontainers-arm64/issues/148#issuecomment-5655716502) records the exact cause.
- SoopCT `d4566cb95d73717f55176350179fb8cb8f1f776f` remains the next queued candidate. Refill only a completed slot, then dispatch its full SHA; preserve all successful and blocked outcomes without duplicate reruns.
- QuPath candidate `386964db1c454c002ebd562d06bd1cdcbedcdb99` is pushed on `arm64/qupath-source-arm`, based on accepted pin `8bcc3e3d`; local validation and both architecture generations pass. Issue [#229](https://github.com/Vbitz/neurocontainers-arm64/issues/229#issuecomment-5655740136) records it as queued behind the current four native jobs. Dispatch its exact full SHA when a slot completes.
- QuPath queued candidate was amended to `292b588d105673f8498d7faac750470cec58bce4` to set the extracted Gradle wrapper executable before source build; the corrected SHA and typo correction are recorded on issue [#229](https://github.com/Vbitz/neurocontainers-arm64/issues/229#issuecomment-5655762106). Dispatch this exact SHA when a slot completes.
- Syncro candidate `8dd676cecc56534da67f43997407e9237b4cb2ae8` is pushed on `arm64/syncro-native-components`, based on accepted pin `8bcc3e3d`; it replaces the x86-only SynthStrip base with the accepted source/model route and uses ARM64 torch, TensorFlow and antspyx source builds. Validation and both generations pass. Issue [#234](https://github.com/Vbitz/neurocontainers-arm64/issues/234#issuecomment-5655788200) records it as queued; dispatch its exact full SHA when a slot completes.
- TopoFit candidate `88e6776aeb27f16ef43e015acb426b7e87fe0d1c` passed exact native run [34779394328](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779394328): ARM64 build, SIF conversion, deploy checks and fulltest passed with 15 passed, 0 failed and 0 skipped. It is accepted as the new top-level submodule pin; issue [#236](https://github.com/Vbitz/neurocontainers-arm64/issues/236) has the evidence. The investigation used 3 attempts and required only the ordinary `ninja-build` and `pkg-config` recipe prerequisites.

## Active implementation checkpoint — 2026-09-14 (TopoFit accepted)

- Root `main` is being advanced from accepted submodule pin `8bcc3e3dd69d25fdb16b2f3084d89cf25ddfb5dc` to TopoFit candidate `88e6776aeb27f16ef43e015acb426b7e87fe0d1c` after exact run [34779394328](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779394328) passed native ARM64 build, SIF, deploy and fulltest (15/15, zero skips).
- The accepted submodule pin is now `88e6776aeb27f16ef43e015acb426b7e87fe0d1c`, pushed through root commit `d98c4dd`. The local submodule is on the new SoopCT descendant branch while its candidate is dispatched. Existing active runs remain MIMoSA [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112), VesselBoost [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), and ITK-SNAP [34779151809](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779151809).
- SoopCT was replayed onto the accepted pin as candidate `d977311057123bb1efdb704ea7b4f9858ae52ad2` on `arm64/soopct-antspyx-source-topofit`; local validation and both architecture generations passed. Exact native run [34780565877](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34780565877) is attempt 1/6. QuPath and Syncro remain queued and must be replayed onto `88e6776a` before dispatch.
- QuPath was replayed onto the accepted pin as candidate `9f347a012fc015fe9af9b5d798bece0bd6c7152c` on `arm64/qupath-source-arm-topofit`; validation and both architecture generations passed. It is queued for the next available slot.
- Syncro was replayed onto the accepted pin as candidate `0be219003af62ffcac5f673f6795034346de0b0d` on `arm64/syncro-native-components-topofit`; validation and both architecture generations passed. It is queued for the next available slot.
- CLEARSWI's already passing two-commit route was replayed onto the accepted pin as candidate `94156207825a53e6bc2aa086c60c273824360741` on `arm64/clearswi-topofit`; validation and both architecture generations passed. It is queued behind the current native runs for required integrated verification, avoiding an unchanged rerun.
- PALS candidate `5fa9705a7ff388e51330bbbfa00e1298b37abf23` is pushed on `arm64/pals-miniconda-arm`, based on accepted pin `88e6776a`; it adds the official ARM64 Miniconda installer with a pinned SHA256 while preserving x86_64, and adds a real bundled-atlas lesion-overlap fulltest. Validation, ARM64/x86_64 generation and installer reachability passed. It is queued behind the current four native runs.
- MIMoSA's active older-base candidate has a prepared integrated descendant `6940147e3090cf6729d769c574614740e9bfc522` on `arm64/mimosa-topofit`; validation and both architecture generations passed. If run [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112) passes, dispatch this exact SHA for required current-pin verification before acceptance.
- VesselBoost's active older-base candidate has a prepared integrated descendant `a95b10b2079a98b60652392acd857433035da60a` on `arm64/vesselboost-topofit`; validation and both architecture generations passed. If run [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136) passes, dispatch this exact SHA for required current-pin verification before acceptance.
- ITK-SNAP's active older-base candidate has a prepared integrated descendant `141af5d6843fb84bedb1224851f5cc6601a7e034` on `arm64/itksnap-topofit`; validation and both architecture generations passed. If run [34779151809](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779151809) passes, dispatch this exact SHA for required current-pin verification before acceptance.

## Active implementation checkpoint — 2026-09-14 (SoopCT and ITK-SNAP outcomes)

- Goal remains active. Accepted top-level submodule pin is `88e6776aeb27f16ef43e015acb426b7e87fe0d1c`; fork Actions remains disabled.
- SoopCT run [34780565877](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34780565877) built ARM64/SIF and passed 5/6 fulltests; the ANTsPy import failed because Miniconda's `libstdc++.so.6` lacked `GLIBCXX_3.4.30`. Targeted candidate `3185beb81152728d6abc16cda172ca06270535b1` installs ARM64 `libstdc++6` and links Miniconda's soname to the Ubuntu system library. Validation and both generations pass. The first incorrectly formed dispatch was canceled before checkout and is not counted; corrected retry [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956) is attempt 2/6.
- PALS candidate `5fa9705a7ff388e51330bbbfa00e1298b37abf23` is dispatched in [run 34782446828](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782446828), using the accepted TopoFit pin as its baseline. It remains in progress.
- ITK-SNAP run [34779151809](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34779151809) passed build, SIF and deploy and failed 2/106 fulltests: C3D `-region` and `-pad`, both with glibc buffer-overflow aborts. The upstream C3D `ReadIndexVector` one-byte allocation defect is the first actionable cause; a source fix would violate the third-party port boundary. Issue [#148](https://github.com/Vbitz/neurocontainers-arm64/issues/148#issuecomment-5656100070) records `blocked-upstream`; prepared descendant `141af5d6843fb84bedb1224851f5cc6601a7e034` is preserved without dispatch.
- Native runs still in progress are MIMoSA [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112), VesselBoost [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), SoopCT retry [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956), and PALS [34782446828](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782446828). Do not dispatch another recipe until a slot completes. Next queued candidates are the current-pin MIMoSA/VesselBoost descendants if their older-base runs pass, then CLEARSWI, QuPath and Syncro exact current-pin candidates.

## Active implementation checkpoint — 2026-09-14 (PALS retry)

- PALS run [34782446828](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782446828) passed native build/SIF and 3/4 checks; the only failure was the test fixture's missing output directory, followed by PALS's `add_to_log` error path. Candidate `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006` adds the required `mkdir -p` and passed local validation plus both architecture generations.
- The corrected exact PALS retry is queued as [34782946174](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782946174), attempt 2/6. The malformed expanded SHA in an earlier issue note was corrected before dispatch and was never used.
- Active native work remains SoopCT [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956), MIMoSA [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112), VesselBoost [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), and PALS retry [34782946174](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782946174). Hold the queue until a slot completes.

## Active implementation checkpoint — 2026-09-14 (MIMoSA integration)

- MIMoSA older-base candidate `5341ef2ec334b3d82589af78a2e17cfc5dd63a80` passed native build/SIF/deploy and 21/21 fulltests in [34778357112](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778357112). Current-pin descendant `6940147e3090cf6729d769c574614740e9bfc522` passed local validation and both architecture generations and is dispatched in [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), attempt 5/6.
- The active native set is now SoopCT [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956), VesselBoost [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), PALS retry [34782946174](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782946174), and MIMoSA current-pin verification [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918). No additional dispatch until a slot completes.

## Active implementation checkpoint — 2026-09-14 (replay after PALS acceptance)

- Accepted top-level submodule pin is now `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`, pushed in root commit `7b6c11b`; coverage issue #2 was refreshed from this pin.
- Prepared current-pin descendants from the new accepted pin, each locally validated with ARM64/x86_64 generation: SoopCT `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5` on `arm64/soopct-pals`, MIMoSA `8aff06bb67d3aa099cb7fdfb0617d33f361508e7` on `arm64/mimosa-pals`, and VesselBoost `6d47f60d5ff28aac70af62d4d133406bf8a025be` on `arm64/vesselboost-pals`.
- Existing active runs remain SoopCT [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956), VesselBoost [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136), and MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918); PALS accepted at [34782946174](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782946174). Review each result before dispatching its new descendant, and do not accept older-base evidence.

## Active implementation checkpoint — 2026-09-14 (VesselBoost timeout retry)

- PALS is verified and accepted at `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006`; the durable verified issue note is on [issue #226](https://github.com/Vbitz/neurocontainers-arm64/issues/226#issuecomment-5656230085).
- VesselBoost older-base evidence [34778848136](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34778848136) passed 43/46 tests and failed only three 120-second TTA timeouts. Current-pin candidate `f5e832e68861afee8823074ce72d83c932ccd2e1` adds 300-second timeouts to those tests and is dispatched in [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), attempt 2/6.
- Current native runs to reconcile are SoopCT [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), and VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179). The fourth slot is available for a prepared current-pin candidate after one result is reviewed.

## Active implementation checkpoint — 2026-09-14 (SoopCT and CLEARSWI integration dispatches)

- SoopCT’s pre-PALS candidate passed all 7 fulltests in [34782488956](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34782488956). Current-pin replay `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5` is dispatched in [34783752296](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783752296).
- CLEARSWI’s prior integrated candidate passed all 68 tests; current-pin replay `98735ad44f94c9e5be7ca9ba759167eeec9f349b` is dispatched in [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469).
- Four native runs are now occupied: SoopCT [34783752296](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783752296), CLEARSWI [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), and VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179). Review completed results before dispatching QuPath or Syncro.

## Active implementation checkpoint — 2026-09-14 (next candidates prepared)

- QuPath commits `540c3f69` and `9f347a01` were replayed onto accepted pin `ee0cba5b7c5d95f7cc89e12c68dfcedd70cff006` as `c6ba42ff597871788f7223f90568c83df7bc0e60` on `arm64/qupath-pals`; validation and both architecture generations pass.
- Syncro commit `0be21900` was replayed onto the same accepted pin as `a186f7f89df41b56a8e3d937afd0d6eefa49d3b7` on `arm64/syncro-pals`; validation and both architecture generations pass.
- Both candidates are pushed and queued. Do not dispatch until one of the four current native runs completes and its result is reviewed.

## Active implementation checkpoint — 2026-09-14 (SoopCT accepted)

- SoopCT current-pin replay `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5` passed integrated native run [34783752296](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783752296) with 7/7 tests, zero failures and zero skips. The top-level submodule pointer is being advanced to this exact tested SHA.
- The remaining active runs for CLEARSWI [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), and VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179) were built from the prior accepted pin `ee0cba5b`; review their results, then replay each successful recipe change onto the new SoopCT pin before acceptance.
- QuPath `c6ba42ff597871788f7223f90568c83df7bc0e60` and Syncro `a186f7f89df41b56a8e3d937afd0d6eefa49d3b7` are prepared from the prior pin and must also be replayed before dispatch.

## Active implementation checkpoint — 2026-09-14 (post-SoopCT replay queue)

- The active older-base jobs remain CLEARSWI [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), and VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179). Their intended changes are replayed onto accepted SoopCT pin `e3d7996e` as CLEARSWI `a1fa3f5201c459fbc9b0d9ee45171804e330c0f4`, MIMoSA `e0271a0cddcf0b1108c63df5d201099aca59f301`, and VesselBoost `aa85e3af73e3a933e1552eb9d995a804be7eae8c`; each passes local validation and both architecture generations.
- QuPath `d2230cc663289fef127a943989e0de5db7df0aea` and Syncro `c91eb0e5de57ad5dc6efd4cca25081983bfc9758` are also replayed onto `e3d7996e`, validated, pushed, and queued. Dispatch only after an active result is reviewed and a slot opens.

## Active implementation checkpoint — 2026-09-14 (QuPath dispatch)

- QuPath current-pin candidate `d2230cc663289fef127a943989e0de5db7df0aea` reached a successful Gradle build but failed at the versioned app-image copy path in [34785066541](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785066541). Targeted candidate `c98a89ee6799cd32b6a2247554cf8447a37f24aa` corrects that path, passes local validation and both architecture generations, and is dispatched in [34785400495](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785400495), attempt 2/6.
- Active native jobs are CLEARSWI [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), and QuPath [34785066541](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785066541). Syncro `c91eb0e5de57ad5dc6efd4cca25081983bfc9758` remains the next queued exact candidate.

## Active implementation checkpoint — 2026-09-14 (QuPath path fix)

- QuPath’s first current-pin build reached upstream Gradle success and failed only because the recipe expected a versioned Linux app-image directory. Candidate `c98a89ee6799cd32b6a2247554cf8447a37f24aa` corrects the copy path and is running in [34785400495](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785400495).
- Active native jobs are CLEARSWI [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), and QuPath retry [34785400495](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785400495). Syncro `c91eb0e5de57ad5dc6efd4cca25081983bfc9758` remains queued.

## Active implementation checkpoint — 2026-09-14 (CLEARSWI integrated replay)

- CLEARSWI prior-pin candidate `98735ad44f94c9e5be7ca9ba759167eeec9f349b` passed all 68 native tests in [34783811469](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783811469). Current accepted pin is `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5`; replay `a1fa3f5201c459fbc9b0d9ee45171804e330c0f4` is dispatched in [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800).
- Current active jobs are CLEARSWI replay [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), and QuPath retry [34785400495](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785400495). Syncro `c91eb0e5de57ad5dc6efd4cca25081983bfc9758` remains queued for the next slot.

## Active implementation checkpoint — 2026-09-14 (QuPath accepted)

- QuPath candidate `c98a89ee6799cd32b6a2247554cf8447a37f24aa` passed native ARM64 Docker build, SIF conversion, deploy checks, and 125/125 fulltests with no skips in [run 34785400495](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785400495). It is ready for serial top-level pin acceptance from accepted SoopCT pin `e3d7996e606f92bb8d4fa292bb7a8b8e7987d3a5`.
- After acceptance, replay queued Syncro and any later successful CLEARSWI, MIMoSA, and VesselBoost candidates from the new pin before integrating them.

## Active implementation checkpoint — 2026-09-14 (Syncro replay dispatched)

- Syncro candidate `625e8944fe195e5175fab9835a42f1b0f80c5d3c` is based on accepted QuPath pin `c98a89ee6799cd32b6a2247554cf8447a37f24aa`, passed local recipe validation and ARM64/default-architecture generation, and is queued in [run 34786442868](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786442868).
- Active native jobs are CLEARSWI replay [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), and Syncro [34786442868](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786442868). Integrate only exact candidates replayed from the newest accepted pin.

## Active implementation checkpoint — 2026-09-14 (Syncro targeted retry)

- Syncro run [34786442868](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786442868) failed before tests because SciPy was sent to the PyTorch wheel index. Candidate `7d9d2a442ce492a6ce8b1df1e6a1f8bfc9cbde6` separates those indexes and is queued in [run 34786862612](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786862612), attempt 2/6.
- Active native jobs are CLEARSWI [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), and Syncro retry [34786862612](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786862612). No new recipe is dispatched until one of these slots completes.

## Active implementation checkpoint — 2026-09-14 (Syncro exact retry dispatched)

- Syncro checkout-only run [34786862612](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786862612) used a mistyped SHA and did not execute a build. The exact pushed candidate `7d9d2a445467b75e4b881c27aae4f049fdac5050` is running in [34786938986](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786938986) for the SciPy index fix.
- Active native jobs remain CLEARSWI [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), and Syncro [34786938986](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786938986).

## Active implementation checkpoint — 2026-09-14 (CLEARSWI replay prepared after QuPath)

- CLEARSWI’s two intended commits were replayed onto the accepted QuPath pin `c98a89ee6799cd32b6a2247554cf8447a37f24aa` as `b878ef4914bed658c8df82cf8d418de21d13315f` on `arm64/clearswi-qupath`. The branch is pushed; validation and ARM64/x86_64 Dockerfile generation pass.
- The active SoopCT descendant run [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800) remains in progress. Dispatch `b878ef49` only after reviewing that result and an ARM64 slot opens; acceptance requires native verification of this exact QuPath descendant.

## Active implementation checkpoint — 2026-09-14 (Syncro ANTsPyX dependency retry)

- Syncro run [34786938986](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34786938986) failed in the ARM64 Docker build when ANTsPyX’s bundled ITK could not find system PNG headers/library. Candidate `5c761183` adds ARM64 `libpng-dev`; local validation and ARM64/x86_64 generation pass, and the branch `arm64/syncro-antspyx-png` is pushed.
- CLEARSWI [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800), MIMoSA [34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918), and VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179) remain active. One native slot is available for the Syncro targeted retry; do not dispatch CLEARSWI until its current SoopCT replay is reviewed and the QuPath descendant is exact.

- Syncro exact `libpng-dev` retry candidate `5c7611831036c5b0d22eab09254589031c9df017` is dispatched in [run 34787372368](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787372368). The canceled abbreviated-SHA checkout run [34787340767](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787340767) did no Docker or test work and is not counted.

## Active implementation checkpoint — 2026-09-14 (MIMoSA replay prepared after QuPath)

- MIMoSA candidate `6940147e3090cf6729d769c574614740e9bfc522` passed native ARM64 build/SIF/deploy and 20/20 fulltests in [run 34783066918](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783066918). Its two intended commits were replayed onto accepted QuPath pin `c98a89ee6799cd32b6a2247554cf8447a37f24aa` as `2c0198a5` on `arm64/mimosa-qupath`; validation and both architecture generations pass, and the branch is pushed.
- The exact MIMoSA QuPath descendant is ready for native dispatch when the current runner slot is confirmed free. Acceptance requires this exact candidate’s full native gates.

- MIMoSA exact candidate `2c0198a51f419c07267b00ea34f408f29e7e59f5` is dispatched in [run 34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497). Active jobs are CLEARSWI [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800), VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179), Syncro [34787372368](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787372368), and MIMoSA [34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497).

## Active implementation checkpoint — 2026-09-14 (CLEARSWI older replay passed)

- CLEARSWI SoopCT-based replay [34785901800](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34785901800) passed native build/SIF/deploy and 67/67 fulltests with zero failures and zero skips. The runner’s exact test count is 67 for this fulltest revision.
- QuPath-based descendant `b878ef4914bed658c8df82cf8d418de21d13315f` is pushed and locally validated. Dispatch it in the newly free slot; acceptance requires this exact newest-pin run.

- Exact CLEARSWI QuPath descendant `b878ef4914bed658c8df82cf8d418de21d13315f` is dispatched in [run 34787990978](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787990978). Current native work is CLEARSWI [34787990978](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787990978), MIMoSA [34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497), Syncro [34787372368](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787372368), and VesselBoost [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179).

## Active implementation checkpoint — 2026-09-14 (VesselBoost replay prepared after QuPath)

- VesselBoost PALS-based timeout candidate [34783650179](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34783650179) passed 46/46 fulltests with no skips. Its two intended commits were replayed onto accepted QuPath pin `c98a89ee6799cd32b6a2247554cf8447a37f24aa` as `0d952620` on `arm64/vesselboost-qupath`; validation and both architecture generations pass, and the branch is pushed.
- Dispatch the exact candidate `0d952620` in the newly free native slot. Acceptance requires its complete native build, SIF, deploy and fulltest evidence.

- Exact VesselBoost QuPath descendant `0d952620c20a5881fc9f93c6e64adccb77d87cc3` is dispatched in [run 34788113539](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34788113539). Current native work is CLEARSWI [34787990978](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787990978), MIMoSA [34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497), Syncro [34787372368](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787372368), and VesselBoost [34788113539](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34788113539).

## Active implementation checkpoint — 2026-09-14 (CLEARSWI accepted)

- CLEARSWI exact QuPath candidate `b878ef4914bed658c8df82cf8d418de21d13315f` passed native ARM64 build/SIF/deploy and 67/67 fulltests with zero failures and zero skips in [run 34787990978](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787990978). It was accepted serially as the top-level submodule pin in root commit `5b6e151`; coverage issue #2 was refreshed with Actions still disabled.
- The accepted pin is now `b878ef4914bed658c8df82cf8d418de21d13315f`. Active MIMoSA [34787670497](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787670497), Syncro [34787372368](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34787372368), and VesselBoost [34788113539](https://github.com/Vbitz/neurocontainers-arm64/actions/runs/34788113539) candidates were built from prior accepted pin `c98a89ee`; replay any successful intended changes onto `b878ef49` before acceptance.
