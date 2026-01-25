#!/usr/bin/env python3
"""Copy XSTest result files from TELOS_Master."""
import shutil
from pathlib import Path

src_dir = Path("/Users/brunnerjf/Desktop/TELOS_Master/validation")
dst_dir = Path("/Users/brunnerjf/Desktop/TELOS-Validation")

files = [
    "xstest_validation_results.json",
    "xstest_healthcare_validation_results.json"
]

for f in files:
    src = src_dir / f
    dst = dst_dir / f
    if src.exists():
        shutil.copy(src, dst)
        print(f"Copied: {f}")
    else:
        print(f"Source not found: {f}")

print("Done!")
