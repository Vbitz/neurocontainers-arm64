# spmpython: native compiled runtime unavailable

**Assessment: Required vendor runtime/standalone execution path unavailable.**

Outcome: blocked-prerequisite

SPM-Python25.1.2.post2 on recipe Python3.12 requires spm-runtime-r2025b>=25.1.2. Actual SPM computations require the proprietary MATLAB Runtime R2025b; MathWorks publishes Linux glnxa64/x86-64, while ARM64 installers are for macOS only. Latest documented Linux R2026b still requires Intel/AMD x86-64. Released matlab-runtime0.0.6 installer map contains glnxa64/glnx86 and maca64, no Linux ARM. Recipe installs Python wrappers and runtime deployment package but no MATLAB engine. Existing82 cases exercise imports, pure Python containers, function availability and NumPy; none calls the compiled SPM computational engine. Historical82/82 therefore remains valid evidence of those checks, not scientific SPM execution on Linux ARM64. Ordinary recipe configuration cannot supply an unavailable proprietary native runtime. No emulation or replacement implementation is permitted.

Audited current upstream baseline `ff4961ece3a76e10456f7ba9a2207a5a4b0f3af6`, recipe25.1.2.post2/arm64. No candidate branch, build, upstream PR or release promotion was created. Attempts0/6, preflight start `2026-10-13T01:35:28.757561+00:00`, deadline `2026-10-13T13:35:28.757561+00:00`; no budget reset. Historical source `c6d782cd73cf88ccc44b837f705967b810519086` / run34689239216 and its passed counts retained.

Primary sources:
- https://pypi.org/pypi/spm-python/25.1.2.post2/json
- https://github.com/spm/spm-python#installation-instructions
- https://www.mathworks.com/products/compiler/matlab-runtime.html
- https://www.mathworks.com/support/requirements/matlab-linux.html
- https://github.com/balbasty/matlab-runtime/blob/ca6c34819b406ddfe3585163c4894b576a6036c8/matlab_runtime/utils.py

Revisit condition: Revisit only when MathWorks supplies supported native Linux ARM64 MATLAB Runtime and SPM-Python supplies compatible deployed binaries. Then add actual SPM computation/output assertions before root/upstream proof; do not rerun import-only suite as scientific verification.
