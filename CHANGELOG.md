# Changelog

All notable changes to the SCE Toolkit Registry are recorded here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
the registry uses date-based releases rather than semantic versioning.

## 2026-05-04 — initial bootstrap

### Added
- Registry scaffolding: `README.md` (schema documentation), `CHANGELOG.md`, `registry/` directory, `tools/` directory.
- First reference entry: `registry/dynare.yaml` — populated end-to-end from the Dynare 7.0 capabilities note in the McKibbin-Software-Group repo plus the Dynare team page (`dynare.org/about`).
- Minimum-viable tooling: `tools/registry-validate.py` (schema check + URL liveness), `tools/registry-list.py` (pretty-print as table), `tools/README.md` (tool index).

### Notes
- Schema version 1 is established with this bootstrap commit; future incompatible changes bump the `schema_version:` field on every YAML.
- Twenty-two additional toolkit entries identified in the CEF 2026 pre-conference and invited-session work are queued for population — see the plan at `/tmp/plans/toolkit-registry-plan_2026-05-04.md` (workspace-side) for the list and the per-entry methodology.
- Registry created on the new `@comp-econ-soc` GitHub organization (founded 2026-05-04). The org's existence is itself a prerequisite for governance of this and future SCE collaborative repos.
