#!/usr/bin/env python3
"""news-image-20261118 v2: write the front page to the output directory.

The entry image (entry.png, a 1024x1024 newspaper front page summing up
Wednesday 18 November 2026 in six stories) is composed in advance and
ships in this repository. This program only copies it to the output
directory, so both graded runs write identical bytes. Standard library
only, no network.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit("copy incomplete: size mismatch")
    print("wrote", target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
