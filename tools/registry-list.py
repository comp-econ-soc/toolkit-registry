#!/usr/bin/env python3
"""List the toolkit registry as a Markdown table.

Usage:
    python tools/registry-list.py
    python tools/registry-list.py --kind toolkit
    python tools/registry-list.py --classification DDSL
    python tools/registry-list.py --cef-year 2026

Run from repo root.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML required. pip install pyyaml")

REGISTRY_DIR = Path(__file__).resolve().parent.parent / "registry"


def load_all() -> list[dict]:
    out: list[dict] = []
    for p in sorted(REGISTRY_DIR.glob("*.yaml")):
        try:
            d = yaml.safe_load(p.read_text())
            if isinstance(d, dict):
                d["__path"] = str(p.relative_to(REGISTRY_DIR.parent))
                out.append(d)
        except yaml.YAMLError as e:
            print(f"WARN: skipping {p.name}: {e}", file=sys.stderr)
    return out


def filter_entries(entries: list[dict], args) -> list[dict]:
    out = entries
    if args.kind:
        out = [e for e in out if e.get("kind") == args.kind]
    if args.classification:
        c = args.classification
        out = [e for e in out if c in (e.get("classification") or [])]
    if args.cef_year:
        key = f"cef_{args.cef_year}"
        out = [e for e in out if (e.get("cef_history") or {}).get(key)]
    return out


def render_table(entries: list[dict]) -> str:
    if not entries:
        return "(no entries match)"
    rows = []
    rows.append(["Slug", "Name", "Kind", "License", "Languages", "Maintainers", "Landing"])
    rows.append(["---"] * len(rows[0]))
    for e in entries:
        slug = e.get("slug", "?")
        name = e.get("name", "?")
        kind = e.get("kind", "?")
        license_ = e.get("license") or "—"
        langs = ", ".join((e.get("language") or [])[:3]) or "—"
        maints = (e.get("maintainers") or [])
        maint_str = ", ".join(m.get("name", "?") for m in maints[:3])
        if len(maints) > 3:
            maint_str += f" (+{len(maints)-3})"
        landing = (e.get("urls") or {}).get("landing_page") or "—"
        rows.append([slug, name, kind, license_, langs, maint_str or "—", landing])
    # Render
    out_lines = []
    for r in rows:
        out_lines.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out_lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="List toolkit-registry entries.")
    ap.add_argument("--kind", choices=["toolkit", "method", "research_program"])
    ap.add_argument("--classification")
    ap.add_argument("--cef-year", type=int)
    args = ap.parse_args()

    entries = load_all()
    entries = filter_entries(entries, args)
    print(render_table(entries))
    print()
    print(f"({len(entries)} entries shown)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
