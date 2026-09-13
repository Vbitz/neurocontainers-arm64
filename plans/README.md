# ARM64 recipe research plans

Research date: 2026-09-13. Accepted recipe source: `457c5a31b9830587801a06e7d6f81f18293135e8`.

Scope: the **148 recipes** discussed after the previous porting pass: all 149 recipes without a declared `aarch64` architecture at this pin, excluding `neurocommand` (its separate infrastructure-blocked candidate). LAYNII is already accepted and is also outside this inventory.

These plans reassess the earlier blocker labels. An x86 download, missing ARM image, or need to compile an ordinary dependency does **not** establish a fundamental upstream limitation. Source availability does not establish runtime success either. Each file records the current recipe, primary sources, a scoped conclusion, a plan and validation requirements. No new builds were dispatched for this research task.

Important corrections include the published ARM modsort asset, newer DSI Studio ARM assets, LCModel source, official FSL ARM packages, TensorFlow ARM wheels, and source/CPU routes missed in earlier assessments. Prior issue outcomes and the old completion checkpoint are historical; this research does not inherit their blanket claim that every remaining recipe is fundamentally blocked.

## Findings

| Assessment | Recipes |
| --- | ---: |
| Binary distribution; no public source-build route found | 2 |
| Plausible recipe-level port; no fundamental blocker established | 28 |
| Native dependency or legacy environment needs a supported build route | 18 |
| Complete dependency stack unresolved | 56 |
| GPU capability or supported CPU-mode prerequisite | 7 |
| Concrete prior build failure; not a general architecture prohibition | 5 |
| Different operating-system application port required | 1 |
| Required vendor runtime/standalone execution path unavailable | 31 |

## Recipe index

| Recipe | Assessment |
| --- | --- |
| [afni](afni.md) | Plausible recipe-level port; no fundamental blocker established |
| [aidamri](aidamri.md) | Complete dependency stack unresolved |
| [ashs](ashs.md) | Complete dependency stack unresolved |
| [aslprep](aslprep.md) | Complete dependency stack unresolved |
| [bcbtoolkit](bcbtoolkit.md) | Complete dependency stack unresolved |
| [bidsappaa](bidsappaa.md) | Required vendor runtime/standalone execution path unavailable |
| [bidsappbaracus](bidsappbaracus.md) | Complete dependency stack unresolved |
| [bidsappbrainsuite](bidsappbrainsuite.md) | Required vendor runtime/standalone execution path unavailable |
| [bidsapphcppipelines](bidsapphcppipelines.md) | Required vendor runtime/standalone execution path unavailable |
| [bidsappmrtrix3connectome](bidsappmrtrix3connectome.md) | Complete dependency stack unresolved |
| [bidsapppymvpa](bidsapppymvpa.md) | Complete dependency stack unresolved |
| [bidsappspm](bidsappspm.md) | Required vendor runtime/standalone execution path unavailable |
| [bidsvue](bidsvue.md) | Plausible recipe-level port; no fundamental blocker established |
| [blender](blender.md) | Plausible recipe-level port; no fundamental blocker established |
| [braid](braid.md) | Complete dependency stack unresolved |
| [brainager](brainager.md) | Required vendor runtime/standalone execution path unavailable |
| [brainles-preprocessing](brainles-preprocessing.md) | Native dependency or legacy environment needs a supported build route |
| [brainlesion](brainlesion.md) | Concrete prior build failure; not a general architecture prohibition |
| [brainnetviewer](brainnetviewer.md) | Required vendor runtime/standalone execution path unavailable |
| [brainstorm](brainstorm.md) | Required vendor runtime/standalone execution path unavailable |
| [brainsuite](brainsuite.md) | Required vendor runtime/standalone execution path unavailable |
| [brainvisa](brainvisa.md) | Complete dependency stack unresolved |
| [cartool](cartool.md) | Different operating-system application port required |
| [cat12](cat12.md) | Required vendor runtime/standalone execution path unavailable |
| [civet](civet.md) | Plausible recipe-level port; no fundamental blocker established |
| [clearswi](clearswi.md) | Concrete prior build failure; not a general architecture prohibition |
| [clinica](clinica.md) | Complete dependency stack unresolved |
| [clinicadl](clinicadl.md) | Complete dependency stack unresolved |
| [conn](conn.md) | Required vendor runtime/standalone execution path unavailable |
| [connectomemapper3](connectomemapper3.md) | Required vendor runtime/standalone execution path unavailable |
| [connectomeworkbench](connectomeworkbench.md) | Complete dependency stack unresolved |
| [convert3d](convert3d.md) | Plausible recipe-level port; no fundamental blocker established |
| [cpac](cpac.md) | Complete dependency stack unresolved |
| [deepisles](deepisles.md) | GPU capability or supported CPU-mode prerequisite |
| [deeplabcut](deeplabcut.md) | Plausible recipe-level port; no fundamental blocker established |
| [deepretinotopy](deepretinotopy.md) | Complete dependency stack unresolved |
| [deepsif](deepsif.md) | GPU capability or supported CPU-mode prerequisite |
| [deepwmh](deepwmh.md) | Complete dependency stack unresolved |
| [delphi](delphi.md) | Native dependency or legacy environment needs a supported build route |
| [dhcpstructuralpipeline](dhcpstructuralpipeline.md) | Complete dependency stack unresolved |
| [diffusiontoolkit](diffusiontoolkit.md) | Binary distribution; no public source-build route found |
| [dsistudio](dsistudio.md) | Plausible recipe-level port; no fundamental blocker established |
| [eeglab](eeglab.md) | Required vendor runtime/standalone execution path unavailable |
| [elastix](elastix.md) | Plausible recipe-level port; no fundamental blocker established |
| [emuses](emuses.md) | Native dependency or legacy environment needs a supported build route |
| [enigma-pd-wml](enigma-pd-wml.md) | Complete dependency stack unresolved |
| [esilpd](esilpd.md) | GPU capability or supported CPU-mode prerequisite |
| [exploreasl](exploreasl.md) | Required vendor runtime/standalone execution path unavailable |
| [ezbids](ezbids.md) | Complete dependency stack unresolved |
| [fastcsr](fastcsr.md) | Complete dependency stack unresolved |
| [fastsurfer](fastsurfer.md) | Complete dependency stack unresolved |
| [fatsegnet](fatsegnet.md) | Native dependency or legacy environment needs a supported build route |
| [fetalsegmentation](fetalsegmentation.md) | Complete dependency stack unresolved |
| [fetalsynthseg](fetalsynthseg.md) | Plausible recipe-level port; no fundamental blocker established |
| [fieldtrip](fieldtrip.md) | Required vendor runtime/standalone execution path unavailable |
| [fmriprep](fmriprep.md) | Complete dependency stack unresolved |
| [freesurfer](freesurfer.md) | Required vendor runtime/standalone execution path unavailable |
| [fsl](fsl.md) | Plausible recipe-level port; no fundamental blocker established |
| [gigaconnectome](gigaconnectome.md) | Plausible recipe-level port; no fundamental blocker established |
| [halfpipe](halfpipe.md) | Complete dependency stack unresolved |
| [hcpasl](hcpasl.md) | Complete dependency stack unresolved |
| [hmri](hmri.md) | Required vendor runtime/standalone execution path unavailable |
| [hypermapp3r](hypermapp3r.md) | Native dependency or legacy environment needs a supported build route |
| [ilastik](ilastik.md) | Complete dependency stack unresolved |
| [itksnap](itksnap.md) | Plausible recipe-level port; no fundamental blocker established |
| [jamovi](jamovi.md) | Complete dependency stack unresolved |
| [jidt](jidt.md) | Complete dependency stack unresolved |
| [lashis](lashis.md) | Complete dependency stack unresolved |
| [lcmodel](lcmodel.md) | Plausible recipe-level port; no fundamental blocker established |
| [lesymap](lesymap.md) | Native dependency or legacy environment needs a supported build route |
| [linda](linda.md) | Native dependency or legacy environment needs a supported build route |
| [lstai](lstai.md) | Plausible recipe-level port; no fundamental blocker established |
| [matlab](matlab.md) | Required vendor runtime/standalone execution path unavailable |
| [matlabruntime](matlabruntime.md) | Required vendor runtime/standalone execution path unavailable |
| [megnet](megnet.md) | Plausible recipe-level port; no fundamental blocker established |
| [meica](meica.md) | Complete dependency stack unresolved |
| [metabody](metabody.md) | Complete dependency stack unresolved |
| [mfcsc](mfcsc.md) | Required vendor runtime/standalone execution path unavailable |
| [mgltools](mgltools.md) | Complete dependency stack unresolved |
| [micapipe](micapipe.md) | Required vendor runtime/standalone execution path unavailable |
| [mimosa](mimosa.md) | Native dependency or legacy environment needs a supported build route |
| [minc](minc.md) | Complete dependency stack unresolved |
| [mitkdiffusion](mitkdiffusion.md) | Complete dependency stack unresolved |
| [modsort](modsort.md) | Plausible recipe-level port; no fundamental blocker established |
| [mricrogl](mricrogl.md) | Plausible recipe-level port; no fundamental blocker established |
| [mriqc](mriqc.md) | Complete dependency stack unresolved |
| [mritools](mritools.md) | Native dependency or legacy environment needs a supported build route |
| [mrsimetabolicconnectome](mrsimetabolicconnectome.md) | Complete dependency stack unresolved |
| [mrsiproc](mrsiproc.md) | Required vendor runtime/standalone execution path unavailable |
| [mrtrix3](mrtrix3.md) | Complete dependency stack unresolved |
| [mrtrix3src](mrtrix3src.md) | Complete dependency stack unresolved |
| [mrtrix3tissue](mrtrix3tissue.md) | Complete dependency stack unresolved |
| [musclemap](musclemap.md) | Plausible recipe-level port; no fundamental blocker established |
| [napari](napari.md) | Complete dependency stack unresolved |
| [nesvor](nesvor.md) | GPU capability or supported CPU-mode prerequisite |
| [networkcorrespondancetoolkit](networkcorrespondancetoolkit.md) | Concrete prior build failure; not a general architecture prohibition |
| [neurodock](neurodock.md) | Complete dependency stack unresolved |
| [nftsim](nftsim.md) | Plausible recipe-level port; no fundamental blocker established |
| [nibabies](nibabies.md) | Complete dependency stack unresolved |
| [niftymic](niftymic.md) | Native dependency or legacy environment needs a supported build route |
| [nipype](nipype.md) | Required vendor runtime/standalone execution path unavailable |
| [noddi](noddi.md) | Required vendor runtime/standalone execution path unavailable |
| [openads](openads.md) | GPU capability or supported CPU-mode prerequisite |
| [openadscpu](openadscpu.md) | Native dependency or legacy environment needs a supported build route |
| [openmsk](openmsk.md) | GPU capability or supported CPU-mode prerequisite |
| [oshyx](oshyx.md) | Complete dependency stack unresolved |
| [osprey](osprey.md) | Required vendor runtime/standalone execution path unavailable |
| [ospreybids](ospreybids.md) | Required vendor runtime/standalone execution path unavailable |
| [palmettobug](palmettobug.md) | Complete dependency stack unresolved |
| [pals](pals.md) | Complete dependency stack unresolved |
| [petprep](petprep.md) | Complete dependency stack unresolved |
| [physio](physio.md) | Required vendor runtime/standalone execution path unavailable |
| [prequal](prequal.md) | Complete dependency stack unresolved |
| [pydeface](pydeface.md) | Plausible recipe-level port; no fundamental blocker established |
| [qsiprep](qsiprep.md) | Complete dependency stack unresolved |
| [qsirecon](qsirecon.md) | Complete dependency stack unresolved |
| [quickshear](quickshear.md) | Plausible recipe-level port; no fundamental blocker established |
| [qupath](qupath.md) | Complete dependency stack unresolved |
| [rabies](rabies.md) | Complete dependency stack unresolved |
| [relion](relion.md) | GPU capability or supported CPU-mode prerequisite |
| [romeo](romeo.md) | Plausible recipe-level port; no fundamental blocker established |
| [root](root.md) | Plausible recipe-level port; no fundamental blocker established |
| [rshrf](rshrf.md) | Plausible recipe-level port; no fundamental blocker established |
| [rstudio](rstudio.md) | Complete dependency stack unresolved |
| [samri](samri.md) | Complete dependency stack unresolved |
| [samsrfx](samsrfx.md) | Required vendor runtime/standalone execution path unavailable |
| [slicer](slicer.md) | Complete dependency stack unresolved |
| [slicersalt](slicersalt.md) | Complete dependency stack unresolved |
| [soopct](soopct.md) | Native dependency or legacy environment needs a supported build route |
| [sovabids](sovabids.md) | Plausible recipe-level port; no fundamental blocker established |
| [spinalcordtoolbox](spinalcordtoolbox.md) | Concrete prior build failure; not a general architecture prohibition |
| [spm12](spm12.md) | Required vendor runtime/standalone execution path unavailable |
| [spm12bi](spm12bi.md) | Required vendor runtime/standalone execution path unavailable |
| [spm25](spm25.md) | Required vendor runtime/standalone execution path unavailable |
| [startrack](startrack.md) | Required vendor runtime/standalone execution path unavailable |
| [surfice](surfice.md) | Plausible recipe-level port; no fundamental blocker established |
| [svrtk](svrtk.md) | Complete dependency stack unresolved |
| [syncro](syncro.md) | Native dependency or legacy environment needs a supported build route |
| [synthseg](synthseg.md) | Plausible recipe-level port; no fundamental blocker established |
| [terastitcher](terastitcher.md) | Plausible recipe-level port; no fundamental blocker established |
| [tgvqsm](tgvqsm.md) | Native dependency or legacy environment needs a supported build route |
| [topofit](topofit.md) | Native dependency or legacy environment needs a supported build route |
| [trackvis](trackvis.md) | Binary distribution; no public source-build route found |
| [tractseg](tractseg.md) | Native dependency or legacy environment needs a supported build route |
| [vesselboost](vesselboost.md) | Native dependency or legacy environment needs a supported build route |
| [vmtk](vmtk.md) | Native dependency or legacy environment needs a supported build route |
| [voreen](voreen.md) | Concrete prior build failure; not a general architecture prohibition |
| [xcpd](xcpd.md) | Complete dependency stack unresolved |

## Evidence limits

Registry observations apply to the exact image inspected; no new image was built. PyPI filenames establish distribution availability, not a solved environment. Where current upstream versions differ from the pinned recipe, the plan records a potential migration rather than calling the old version supported. An inaccessible endpoint is an unresolved research limit, not proof that source does not exist.

All plans retain scientific functionality and the original fulltest/deployment gates. The research records are local documentation; builds and future failure outcomes should continue to be recorded in the matching GitHub issues.
