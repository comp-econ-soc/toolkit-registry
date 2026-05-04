# Changelog

All notable changes to the SCE Toolkit Registry are recorded here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
the registry uses date-based releases rather than semantic versioning.

## 2026-05-04 — schema cleanup + license corrections

### Changed
- `hark.yaml`: removed `urls.documentation_extra` (duplicate of `urls.documentation`).
- `abm4policy.yaml`, `mandel-abm.yaml`, `mesa.yaml`: standardized `cef_history.cef_2026.notes_2026` → `notes` (the `_2026` suffix was redundant under the `cef_2026` parent key; matches the pattern used by `gdsge` and `hetsol`).
- `baseforhank.yaml`: license `MIT` → `GPL-3.0` (verified via GitHub License API on `BASEforHANK/BASEtoolbox.jl`); confidence bumped to `high`.
- `rise.yaml`: license `BSD-3-Clause` → `LicenseRef-RISE-Maih` (the LICENSE file is a custom Junior Maih copyright that GitHub classifies as NOASSERTION); notes extended.

### Verified-correct (no change)
HARK Apache-2.0, SSJ MIT, GEModelTools MIT, Mesa Apache-2.0 confirmed against upstream LICENSE files.

### Verified-genuinely-unspecified (no change)
`matsya` (econ-ark/matsya has no LICENSE file), `agentblocks` (no public repo), `hetsol` (Reiter's MATLAB tarballs include no LICENSE), and the five `research_program` entries (no packaged software to license).

---

## 2026-05-04 — bulk population (22 entries)

### Added
- 22 toolkit entries spanning the DDSL family (dolo, sym-gcubed, matsya), the HA-DSGE solver family (baseforhank, ssj, hark, hetsol, gdsge, gemodeltools, vfi-toolkit, rise), general-purpose / structural / methodological (quantecon, maliar-dl-methods, deqn, rust-dynprog-methods), and agent-based modeling (eurace-flame, agentblocks, dosi-abm, ace-tesfatsion, mesa, abm4policy, mandel-abm).
- All 23 entries (the 22 above plus the existing `dynare.yaml`) pass `tools/registry-validate.py`.

### Changed
- Three URL corrections caught by the validator before commit: `hark.yaml` (dropped non-existent `econ-ark.org/about/`, added `documentation_extra: docs.econ-ark.org`), `quantecon.yaml` (`about_page` → `quantecon.org/about/`), `vfi-toolkit.yaml` (dropped offline forum + 406-rejecting about_page).

### Notes
- Eight entries are `kind: research_program` or `kind: method` rather than packaged toolkits — appropriate for individual researchers' computational-methods agendas (Maliar, Rust, Dosi-lineage, Tesfatsion, Mandel, Kaszowska-Mojsa) or named-method-with-reference-code (DEQN). Confidence levels per entry reflect single-source vs cross-referenced.

---

## 2026-05-04 — initial bootstrap

### Added
- Registry scaffolding: `README.md` (schema documentation), `CHANGELOG.md`, `registry/` directory, `tools/` directory.
- First reference entry: `registry/dynare.yaml` — populated end-to-end from the Dynare 7.0 capabilities note in the McKibbin-Software-Group repo plus the Dynare team page (`dynare.org/about`).
- Minimum-viable tooling: `tools/registry-validate.py` (schema check + URL liveness), `tools/registry-list.py` (pretty-print as table), `tools/README.md` (tool index).

### Notes
- Schema version 1 is established with this bootstrap commit; future incompatible changes bump the `schema_version:` field on every YAML.
- Twenty-two additional toolkit entries identified in the CEF 2026 pre-conference and invited-session work are queued for population — see the plan at `/tmp/plans/toolkit-registry-plan_2026-05-04.md` (workspace-side) for the list and the per-entry methodology.
- Registry created on the new `@comp-econ-soc` GitHub organization (founded 2026-05-04). The org's existence is itself a prerequisite for governance of this and future SCE collaborative repos.
