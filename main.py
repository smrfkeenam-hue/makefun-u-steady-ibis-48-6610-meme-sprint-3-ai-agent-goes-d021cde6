"""Meme Sprint 3: AI Agent Goes Rogue.

Writes the meme image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).
Standard library only; the image ships in this repository as entry.png.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png not found next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        raise SystemExit("copy incomplete: %d != %d" % (src_size, dst_size))
    print("wrote", dst, dst_size, "bytes")


if __name__ == "__main__":
    main()
