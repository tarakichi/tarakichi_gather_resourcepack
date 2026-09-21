#!/usr/bin/env python3
"""
インベントリ画面の背景（textures/gui/container/inventory.png と crafting_table.png）に、
チップスロット（右側 3 列 x 3 行）の枠を描いて、assets/ 以下に書き出す。

  python3 tools/make_gui.py <クライアント jar か、assets の入った展開済みフォルダ>

- 枠の絵は、textures/item/chip_slot.png（16x16）を、9 マスぶん並べて使う。絵を描き直したら、もう一度実行する。
- 元の背景（Mojang の素材）は、リポジトリに入っていないので、Minecraft のクライアント jar（versions/<版>/<版>.jar）を渡す。
- 必要なもの: Python 3 と Pillow（pip install pillow）
"""
import io
import os
import sys
import zipfile
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = ["inventory", "crafting_table"]
# 主インベントリのスロットの内側（16x16）の左上 = (8 + 18 * 列, 84 + 18 * 行)。チップスロットは、右側 3 列（列 6〜8）× 3 行
CHIP_COLS = (6, 7, 8)
ROWS = (0, 1, 2)


def load_base(src, name):
    rel = f"assets/minecraft/textures/gui/container/{name}.png"
    if os.path.isdir(src):
        return Image.open(os.path.join(src, rel)).convert("RGBA")
    with zipfile.ZipFile(src) as z:
        return Image.open(io.BytesIO(z.read(rel))).convert("RGBA")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    tile = Image.open(os.path.join(ROOT, "assets/minecraft/textures/item/chip_slot.png")).convert("RGBA")
    if tile.size != (16, 16):
        sys.exit("chip_slot.png は 16x16 にしてください")
    out_dir = os.path.join(ROOT, "assets/minecraft/textures/gui/container")
    os.makedirs(out_dir, exist_ok=True)
    for name in TARGETS:
        im = load_base(src, name)
        for r in ROWS:
            for c in CHIP_COLS:
                im.paste(tile, (8 + 18 * c, 84 + 18 * r))
        im.save(os.path.join(out_dir, f"{name}.png"))
        print("書き出し:", f"assets/minecraft/textures/gui/container/{name}.png")


if __name__ == "__main__":
    main()
