"""รวมไฟล์ games/*.json ทุกไฟล์เป็น games.json ไฟล์เดียว

ใช้งาน:
  python3 scripts/build.py --out _site/games.json            # ตอน deploy: ข้ามไฟล์ที่ผิด
  python3 scripts/build.py --out /tmp/games.json --strict    # ตอนตรวจ PR: ไฟล์ผิด = ไม่ผ่าน
"""
import glob
import json
import os
import sys

REQUIRED = ["team", "title", "play"]


def load(path):
    with open(path, encoding="utf-8") as f:
        g = json.load(f)
    if not isinstance(g, dict):
        raise ValueError("ไฟล์ต้องเป็นเกมเดียวในรูปแบบ { ... }")
    missing = [k for k in REQUIRED if not str(g.get(k, "")).strip()]
    if missing:
        raise ValueError("ขาดช่อง: " + ", ".join(missing))
    for key in ("play", "repo"):
        if g.get(key) and not str(g[key]).startswith("https://"):
            raise ValueError(f"ลิงก์ '{key}' ต้องขึ้นต้นด้วย https://")
    return g


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    out = args[args.index("--out") + 1] if "--out" in args else "games.json"

    games, errors = [], []
    for path in sorted(glob.glob("games/*.json")):
        try:
            games.append(load(path))
            print(f"✅ {path}")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{path}: {e}")
            print(f"::error file={path}::{e}")

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(games, f, ensure_ascii=False, indent=2)
    print(f"\nรวมได้ {len(games)} เกม, ผิดพลาด {len(errors)} ไฟล์ → {out}")

    if strict and errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
