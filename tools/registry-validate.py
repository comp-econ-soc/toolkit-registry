#!/usr/bin/env python3
"""Validate the toolkit registry: schema check + URL liveness.

Exit 0 if every entry passes; exit 1 if any entry fails.

Run from repo root:
    python tools/registry-validate.py
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML required. pip install pyyaml")
try:
    import requests
except ImportError:
    sys.exit("ERROR: requests required. pip install requests")

REGISTRY_DIR = Path(__file__).resolve().parent.parent / "registry"
TIMEOUT = 10  # seconds for HTTP HEAD checks
SCHEMA_VERSION = 1

REQUIRED_TOP_LEVEL = ["schema_version", "slug", "name", "kind", "classification",
                      "urls", "language", "license", "maintainers", "provenance"]
REQUIRED_PROVENANCE = ["added_to_registry", "added_by", "primary_source", "last_verified"]
KIND_VALUES = {"toolkit", "method", "research_program"}


def check_url(url: str) -> tuple[bool, str]:
    """Return (ok, status_message) for an HTTP HEAD against url."""
    try:
        r = requests.head(url, timeout=TIMEOUT, allow_redirects=True,
                          headers={"User-Agent": "sce-toolkit-registry-validator/1"})
        ok = 200 <= r.status_code < 400
        return ok, f"HTTP {r.status_code}"
    except requests.RequestException as e:
        return False, f"{type(e).__name__}: {e}"


def validate_entry(path: Path) -> list[str]:
    """Return list of human-readable error strings (empty if entry passes)."""
    errors: list[str] = []
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        return [f"YAML parse failure: {e}"]
    if not isinstance(data, dict):
        return ["root is not a mapping"]

    # Schema version
    sv = data.get("schema_version")
    if sv != SCHEMA_VERSION:
        errors.append(f"schema_version is {sv!r}; expected {SCHEMA_VERSION}")

    # Required top-level fields
    for k in REQUIRED_TOP_LEVEL:
        if k not in data:
            errors.append(f"missing required field: {k}")

    # Slug must match filename stem
    expected_slug = path.stem
    if data.get("slug") != expected_slug:
        errors.append(f"slug {data.get('slug')!r} does not match filename stem {expected_slug!r}")

    # Kind enum
    if data.get("kind") not in KIND_VALUES:
        errors.append(f"kind {data.get('kind')!r} not in {sorted(KIND_VALUES)}")

    # urls.landing_page required
    urls = data.get("urls") or {}
    if not urls.get("landing_page"):
        errors.append("urls.landing_page is required")

    # At least one maintainer with a name
    maint = data.get("maintainers") or []
    if not isinstance(maint, list) or not maint or not maint[0].get("name"):
        errors.append("at least one maintainer with a name is required")

    # Provenance required fields
    prov = data.get("provenance") or {}
    for k in REQUIRED_PROVENANCE:
        if not prov.get(k):
            errors.append(f"provenance.{k} is required")

    # URL liveness — every non-empty url field
    for kind, url in urls.items():
        if not url:
            continue
        if not isinstance(url, str) or not url.startswith(("http://", "https://", "file:")):
            errors.append(f"urls.{kind} is not a recognized URL scheme: {url!r}")
            continue
        if url.startswith("file:"):
            continue  # local file references are not network-checked
        ok, msg = check_url(url)
        if not ok:
            errors.append(f"urls.{kind} unreachable: {url} — {msg}")

    return errors


def main() -> int:
    if not REGISTRY_DIR.is_dir():
        sys.exit(f"ERROR: registry directory not found at {REGISTRY_DIR}")
    yaml_files = sorted(REGISTRY_DIR.glob("*.yaml"))
    if not yaml_files:
        print("(no entries in registry/)")
        return 0

    failed = 0
    for path in yaml_files:
        errors = validate_entry(path)
        if errors:
            failed += 1
            print(f"FAIL  {path.name}")
            for e in errors:
                print(f"      - {e}")
        else:
            print(f"OK    {path.name}")

    print()
    print(f"Total: {len(yaml_files)}   Pass: {len(yaml_files) - failed}   Fail: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
