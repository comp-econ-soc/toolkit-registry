# Tools

Utilities for working with the toolkit registry.

| Script | What it does |
|--------|--------------|
| `registry-validate.py` | Validate every YAML in `registry/` against the schema; check URLs are reachable. Exit code non-zero if any entry fails. |
| `registry-list.py` | Pretty-print the registry as a Markdown table. Supports `--kind`, `--classification`, `--cef-year` filters. |

Planned but not yet written (see `../README.md` "How to add an entry"):

| Script | Purpose |
|--------|---------|
| `registry-fetch.py` | Auto-fill metadata for a new entry from `urls.source_repository` (license, last release, top contributors via the GitHub API). |
| `registry-export.py` | Export the registry to CSV / JSON / a single Markdown table for sharing externally or feeding into other systems. |
| `registry-add.py` | Interactive prompt for a new toolkit entry. Walks through required fields, validates URLs as you enter them. |

## Requirements

Python 3.11+ with `pyyaml` and `requests`. Install:

```sh
pip install pyyaml requests
```

If you use `uv`:

```sh
uv pip install pyyaml requests
```

## Conventions

- Scripts are run from the repo root (`cd toolkit-registry && python tools/<script>.py`).
- Exit code 0 = success; non-zero = at least one failure.
- Status output is printed to stdout; warnings/errors to stderr.
