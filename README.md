# SCE Toolkit Registry

A curated, source-grounded registry of the computational-economics toolkits in active use by the Society for Computational Economics (SCE) community.

## What is here

- **`registry/`** — one YAML file per toolkit. The filename stem is the toolkit's `slug`. Each file contains canonical URLs, maintainers, license, language, last release, and SCE-specific tracking (which CEF year invited which presenter, which session the toolkit appeared in).
- **`tools/`** — scripts that operate on `registry/`: validate the schema, list entries as a table, fetch metadata from upstream, export to CSV/JSON, walk through adding a new entry.
- **`CHANGELOG.md`** — human-readable log of registry changes.

## Schema

Each toolkit entry follows this shape. Required fields are noted **R**; optional **O**.

```yaml
schema_version: 1                         # R: bump on incompatible changes

slug: dynare                              # R: filename stem; lowercase, hyphenated
name: DYNARE                              # R: canonical capitalized name
aka: []                                   # O: list of alternative names

kind: toolkit                             # R: one of {toolkit, method, research_program}
                                          #   - toolkit: packaged framework with installer + docs
                                          #   - method: named technique with reference implementation
                                          #   - research_program: research umbrella with multiple loosely-coupled artefacts

classification: []                        # R: free tags (e.g. DDSL, DSGE-solver, HA-capable, ABM)

urls:                                     # R: at least landing_page required
  landing_page: ~                         # R: project's primary public page
  documentation: ~                        # O: docs site if separate
  source_repository: ~                    # O: canonical Git host URL
  package_index: ~                        # O: PyPI / CRAN / Conda / etc.
  forum: ~                                # O: community forum
  about_page: ~                           # O: about / team page

language: []                              # R: list of primary implementation languages

license: ~                                # R: SPDX identifier, "proprietary", or "unspecified"

maintainers:                              # R: at least one entry
  - name: ~                               # R per entry
    role: ~                               # O: founder | core developer | maintainer | contributor
    affiliation: ~                        # O
    email: ~                              # O: only if publicly listed on the toolkit's own page

primary_contact:                          # O
  name: ~
  email: ~

last_known_release:                       # O
  version: ~
  date: ~

cef_history: {}                           # O: SCE-specific tracking, keyed by year:
                                          # cef_2026:
                                          #   preconference_invitee: <name>
                                          #   main_session: <A or B>
                                          #   main_session_presenter: <name>
                                          #   sponsor_status: <set only if SCE-sponsored>

notes: ~                                  # O: free-form prose

provenance:                               # R
  added_to_registry: 2026-mm-dd
  added_by: ~
  primary_source: ~                       # URL or path
  cross_references: []                    # O
  last_verified: 2026-mm-dd
  confidence: high                        # O: high | medium | low (single-source ⇒ low)
```

## Inclusion rule

A toolkit belongs in this registry if it has had an SCE relationship — i.e., a maintainer or representative has been (a) a CEF pre-conference invitee, (b) a main-program invited-session presenter, (c) part of the AC-level toolkit conversation, or (d) cited substantively in SCE governance materials. The registry is a map of the **SCE-touching** toolkit landscape, not a catalog of every macro tool ever published.

Five entry kinds are accepted under `kind:`. Most entries will be `toolkit`. Use `method` for a named technique with reference code (e.g. Deep Equilibrium Nets); use `research_program` for an individual researcher's broader computational-methods program when there isn't a single packaged artefact (e.g. some ABM lineages).

## How to add an entry

1. Run `tools/registry-add.py` for an interactive walk-through, or copy an existing entry as a template.
2. Verify the file passes `tools/registry-validate.py`.
3. Add a row to `CHANGELOG.md` summarizing the change.
4. Open a PR (preferred) or commit directly if you are an org owner.

## How to verify the registry

```sh
python tools/registry-validate.py        # schema + URL liveness checks
python tools/registry-list.py            # pretty-print as a table
python tools/registry-list.py --kind toolkit --classification DDSL  # filtered view
```

## Maintenance cadence

- **Per change:** validate before commit; update `provenance.last_verified` for any entry touched.
- **Quarterly:** run `registry-validate.py` against all entries; rotate `last_verified` dates for entries whose URLs still resolve and whose maintainers are unchanged.
- **Per CEF year:** add any toolkits that surfaced in that year's pre-conference or invited sessions; update `cef_history` for existing entries.

## Related materials

- Plan that scoped this registry: see the `/tmp/plans/toolkit-registry-plan_2026-05-04.md` file in the SCE officers' workspace.
- Capability deep-dives for some entries: `McKibbin-Software-Group` repo (`research/{dynare,dolo,gcubed}-capabilities.md`, etc.).
- Pre-conference roster + presenter assignments: `cef_venice_2026/email/invitee-mail-merge.yaml` (private).
- Public CEF 2026 invited-session descriptions: `workspace-comp-econ-soc/artifacts/cef-2026/computational-tools-session-{ddsl,non-ddsl}.md`.
