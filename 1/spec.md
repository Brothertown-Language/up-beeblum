# SPEC: Repository initial contents — scaffold (PR 1)

## 1. Intent and Executive Summary

**Problem Statement:** The repository `up-beeblum` (Brothertown-Language org, public) is empty. The quad-text Eliot Bible edition program designed this session — four parallel texts (WLRP-modern Wampanoag / colonial original orthography / English frame / WEB) across both printed editions, delivered as LaTeX/PDF interlinear works plus Markdown from a self-contained, coverage-driven build — has a finalized design but no working repository scaffold, so no roadmap item can implement against a real tree.

**Root Cause / Motivation:** The design was fixed in this session's brainstorm (2026-11-23) and the developer directed repo creation (done) followed by the initial-contents scaffold (this spec) as the first implementation of the new repository; every downstream artifact (roadmap, README, AGENTS.md, follow-up specs) files against what this scaffold establishes.

**Approach Chosen:** Establish the mechanical scaffold the design fixes — package and uv toolchain, the committed-data directory skeleton, the two reference-only submodules, the ignore and `private/` placement policy, and a smoke-tier suite that proves self-containment from a fresh clone. Nothing that belongs to the stacked spec (README/AGENTS.md/ROADMAP) or the roadmap (build pipeline, derivation engine, corpus content) lands here.

**Alternatives Considered & Why Discarded:**
- *Full build + derivation engine with the scaffold* — discarded: the roadmap (the stacked stage's deliverable) owns sequencing; front-loading it invents scope the directive stages.
- *No submodules in initial contents* — discarded: the developer directive states the submodules; the tree carries them from the first content PR.
- *Copying the family's full test-tier register machinery* — discarded: this repository starts with a smoke tier; tiering grows when the roadmap names heavy work.

**Key Design Decisions:**
- Package `up_beeblum` with a uv-managed toolchain (pytest/ruff/pyright) — family toolchain parity; tradeoff: none material.
- Reference submodules declared in `.gitmodules`, never build dependencies — preserves the self-containment property; tradeoff: provenance must come from build manifests, not runtime references.
- Committed-data skeleton with per-edition/per-book layout and manifest placeholders — realizes the committed-copies architecture; tradeoff: the top-level shape is frozen before the first book lands, reshapeable at one level by roadmap work.
- `private/.gitignore` + manifest seeded at birth — placement rules apply from day one; tradeoff: none.

**User Intent / Original Prompt** (developer statements verbatim, 2026-11-23):
- "We need to look into setting up a quad-text version of the eliot bibles. text 1: Wampanoag - in modern Wampanoag orthography  text 2: Original orthography  text 3: English text translated from (Geneva, KJV, ...)  test 4: Modern WEB bible. brainstorm. this will be done with a new repo, but the new repo will need to submodule the relevant snea-* algonquian-* repos."
- "=> Wôpanâak Language Reclamation Project's modern orthography" — "best effort based on available pronunciation rules, et al"
- "the new repo will need to maintain repo copies of the various texts used." — "=> Regenerated"
- "for now, tex/PDF; markdown"
- "sub-modules for now are reference only, the repo needs to be self-contained"
- "version builds what it can covering both complete editions if possible"
- "we should be able to use a neural network for improved handling of the orthography conversion based on pronunciations? /original/=>/IPA/=>Wampanoag" — "place into the new repo along side the rest of the new"
- "Include adding these PDFs as tracked items. create the new repo, public, then file the spec to setup the repo's initial contents and implement for PR, then create the spec for the needed roadmap file/readme file/agents.md file and implement for stacked PR, then file the follow up specs based on the roadmap."

## 2. Not Included

- `README.md`, `AGENTS.md`, and the roadmap document — the stacked spec's named deliverables (the directive stages them separately).
- The works-registry build/render pipeline, the derivation engine (rule classes, per-form map, ML assist), and all corpus-data content — follow-up roadmap items.
- CI pipelines — not named by the directive; deferred to the roadmap.
- The Fermino 2000 / Hicks 2006 reference PDFs — tracked in the snea-phonetics research tree (`feature/thesis-reference-pdfs`, 2026-11-23); this repository cites them by reference.
- The remote issue store's bootstrapping (.opencode checkout clone, store init) — workspace maintenance executed before this spec filed; not tree content.

## 3. Requirements

- **R-1:** The repository SHALL carry the package directory `src/up_beeblum/` containing at least a module entry point (`__init__.py`).
- **R-2:** The toolchain SHALL be uv-managed: `pyproject.toml` carrying exactly `[tool.pytest.ini_options]` with `testpaths = ["test"]`, a `[tool.ruff]` section targeting the `src/` and `test/` trees, and a `[tool.pyright]` section with `include = ["src"]` — matching the family AGENTS.md command table (`uv run pytest test/`, `uvx ruff check src/ test/`, `uvx pyright src/`).
- **R-3:** The repository SHALL declare reference-only submodules `algonquian-library` and `snea-lib` in `.gitmodules` at their canonical paths (`corpus/`, `snea-lib/`) with canonical GitHub origins (`Brothertown-Language/algonquian-library`, `Brothertown-Language/snea-lib`).
- **R-4:** The repository SHALL carry the committed-data skeleton: the edition directories `data/editions/1663-first/` and `data/editions/1685-second/`, plus `data/derivations/` and `data/manifests/`; per-book text copies land under the stated layout rule `data/editions/<edition>/<BOOK>/<column>.tsv` — column codes `wlp` (modern WLRP), `orig` (original orthography), `frame` (the edition's English frame), `web` — with no book data in the scaffold (books land via roadmap work).
- **R-5:** `.gitignore` SHALL carry exactly this exclusion set: `.issues/`, `.opencode/`, `private/`, `tmp/`, `outputs/`, and the LaTeX byproduct extensions `*.aux`, `*.log`, `*.out`, `*.toc`.
- **R-6:** `private/` SHALL carry its `.gitignore` and a README manifest consistent with the family placement rules (in-copyright material untracked by design; an acquisition-route inventory of record).
- **R-7:** The repository SHALL carry a smoke test suite under `test/` containing at least one pytest-collectable test, so the SC-1 run exercises a real suite rather than an empty target.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Fresh-clone smoke green: `uv sync && uv run pytest test/` exits 0 with neither submodule materialized | behavioral | clone to a temp dir; assert both submodule paths absent; run both commands; assert exit 0 |
| SC-2 | Layout skeleton matches R-4: the two edition directories, `data/derivations/`, and `data/manifests/` exist | structural | path-existence check enumerating those four paths |
| SC-3 | `.gitmodules` lists exactly the two reference submodules with canonical URLs and paths | structural | `git config --file .gitmodules --list` output compared against the R-3 values |
| SC-4 | `.gitignore`'s effective patterns (non-blank, non-comment lines) equal the R-5 set, with nothing added | structural | parse `.gitignore` lines minus blank/comment lines; compare the resulting set for equality against the R-5 enumeration |
| SC-5 | `pyproject.toml` carries the R-2 sections with the R-2 stated values (`testpaths = ["test"]`, `[tool.ruff]`, pyright `include = ["src"]`) | structural | read `pyproject.toml`; assert those three concrete values |
| SC-6 | `src/up_beeblum/` exists and contains an `__init__.py` | structural | path-existence check for `src/up_beeblum/__init__.py` |
| SC-7 | `private/` contains a `.gitignore` and a README manifest; neither is tracked by the parent repository | structural | path-existence of `private/.gitignore` + `private/README.md`; `git check-ignore private/` confirms exclusion |
| SC-8 | The smoke suite is collectable: pytest reports at least one collected test from `test/` | structural | `uv run pytest test/ --collect-only -q` reports a test count ≥ 1, exit 0 |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| `Brothertown-Language/up-beeblum` repository (created public, 2026-11-23) | the scaffold's host repository | satisfied |
| Family conventions: snea-phonetics AGENTS.md build-command table + `.gitignore` policy (read this session) | toolchain and ignore-policy convention source | satisfied |
| Issue #1's remote filing (github.com/Brothertown-Language/up-beeblum/issues/1) | this spec's remote record | satisfied |
| Fermino 2000 / Hicks 2006 | derivation anchors, needed by later roadmap items only | pending (not this change's) |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-6 |
| R-2 | SC-5, SC-1 |
| R-3 | SC-3, SC-1 |
| R-4 | SC-2 |
| R-5 | SC-4 |
| R-6 | SC-7 |
| R-7 | SC-8, SC-1 |

Every SC traces (SC-1→R-2/R-3/R-7, SC-2→R-4, SC-3→R-3, SC-4→R-5, SC-5→R-2, SC-6→R-1, SC-7→R-6, SC-8→R-7); no orphans in either direction.

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| up-beeblum repository | repository | github.com/Brothertown-Language/up-beeblum (public) | live `gh repo create` output, 2026-11-23 |
| snea-phonetics AGENTS.md | project guide | /home/muksihs/git/snea-phonetics/AGENTS.md | read, this session |
| snea-phonetics `.gitignore` | config | /home/muksihs/git/snea-phonetics/.gitignore | read, this session |
| corpus AGENTS.md (exports contract) | project guide | corpus/AGENTS.md | read, 2026-11-23 |
| Remote issue #1 | tracker | github.com/Brothertown-Language/up-beeblum/issues/1 | filed live, 2026-11-23 |
| This session's brainstorm record | conversation | session context (developer directives, 2026-11-23) | quoted verbatim in §1 |

## 8. Cost Frame

- **SC-1:** acting costs one temp-dir clone + `uv sync` (seconds-to-minutes, network to origin once); skipping costs the self-containment claim being asserted rather than proven — a scaffold that builds only in this dev checkout is the bitrot the property guards against.
- **SC-2, SC-3, SC-5, SC-6:** path/config reads cost seconds; skipping costs the structure drifting from the design record silently.
- **SC-4:** one line-set parse of `.gitignore` costs seconds; skipping costs a silent ignore-policy drift (the exact-set equality is what notices an added or dropped pattern).
- **SC-7:** two path checks + one `git check-ignore` call cost seconds; skipping costs the placement policy holding by convention rather than by check (in-copyright content silently tracked is the state this excludes).
- **SC-8:** one pytest collect costs seconds; skipping costs the smoke run exercising an empty target, which would still satisfy SC-1's exit-0 condition vacuously.

## 9. Edge Cases

- **Fresh clone without submodule materialization** — Condition: clone with submodules absent (the `.gitmodules`-declared paths hold no content). Expected behavior: `uv sync && pytest green`. Resolution: SC-1's instrument asserts the absence before running, which is the property's proof.
- **Submodule accidentally materialized** — Condition: a consumer runs `git submodule update --init` before the run. Expected behavior: SC-1's absence preconditions report the environment deviation (both paths present), and the criterion's verification is the absent-state run; the smoke suite itself imports neither submodule. Resolution: the materialized state is not a verification target of this spec — de-materialize (`git submodule deinit --all --force` per the branch card's remediation path) and re-run; the deviation is recorded, not a permanent failure.
- **Empty-repo branch state** — Condition: the repository's trunk (created 2026-11-23, contains only the bootstrap commit). Expected behavior: the scaffold lands on a feature branch and PR-1; the store's `issues-data` branch never enters the main history.

## 10. Completion gate

Every success criterion passes before the PR-1 deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
