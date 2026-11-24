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

- **R-1:** The repository SHALL carry a Python package `up_beeblum` under `src/` with a uv-managed toolchain — `pyproject.toml` carrying pytest, ruff, and pyright configuration consistent with the family AGENTS.md command table (`uv run pytest test/`, `uvx ruff check src/ test/`, `uvx pyright src/`).
- **R-2:** The repository SHALL declare reference-only submodules `algonquian-library` and `snea-lib` in `.gitmodules` at their canonical paths (`corpus/`, `snea-lib/`) with canonical GitHub origins (`Brothertown-Language/algonquian-library`, `Brothertown-Language/snea-lib`).
- **R-3:** The repository SHALL carry the committed-data skeleton: `data/editions/{1663-first,1685-second}/` per-edition text-copy directories for the four columns (modern WLRP, original orthography, English frame, WEB), plus `data/derivations/` (per-form derivation data) and `data/manifests/` (build manifests), each present in the tree.
- **R-4:** The smoke test suite SHALL pass with neither submodule materialized: `uv sync && uv run pytest test/` exits 0 from a fresh clone.
- **R-5:** `.gitignore` SHALL exclude `private/`, `tmp/`, and build/LaTeX output artifacts.
- **R-6:** `private/` SHALL carry its `.gitignore` and a README manifest consistent with the family placement rules (in-copyright material untracked by design; an acquisition-route inventory of record).

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Fresh-clone smoke green: `uv sync && uv run pytest test/` exits 0 with neither submodule materialized | behavioral | clone to a temp dir; assert both submodule paths absent; run both commands; assert exit 0 |
| SC-2 | Layout skeleton matches R-3 (every named directory exists in the tree) | structural | path-existence check enumerating the R-3 paths |
| SC-3 | `.gitmodules` lists exactly the two reference submodules with canonical URLs and paths | structural | `git config --file .gitmodules --list` output compared against the R-2 values |
| SC-4 | Ignore policy excludes `private/`, `tmp/`, build/LaTeX outputs; `private/` contains `.gitignore` + README manifest | structural | grep `.gitignore` for the exclusion set; path-existence check in `private/` |
| SC-5 | `pyproject.toml` carries the pytest, ruff, and pyright configuration sections | structural | read `pyproject.toml`; assert the three sections exist |

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
| R-1 | SC-5 |
| R-2 | SC-3 |
| R-3 | SC-2 |
| R-4 | SC-1 |
| R-5 | SC-4 |
| R-6 | SC-4 |

Every SC traces (SC-1→R-4, SC-2→R-3, SC-3→R-2, SC-4→R-5/R-6, SC-5→R-1); no orphans in either direction.

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
- **SC-2..SC-5:** path/list checks cost seconds; skipping costs the structure drifting from the design record silently.

## 9. Edge Cases

- **Fresh clone without submodule materialization** — Condition: clone with submodules absent (the `.gitmodules`-declared paths hold no content). Expected behavior: `uv sync && pytest green`; Resolution: SC-1's instrument asserts the absence before running, which is the property's proof.
- **Submodule accidentally materialized** — Condition: a consumer runs `git submodule update --init` before the test. Expected behavior: the suite stays green (self-containment means the build does not depend on either); the absence assertion in SC-1's instrument reports the environment deviation rather than failing the smoke result. Resolution: recorded; the criterion's property holds under both states.
- **Empty-repo branch state** — Condition: the repository's trunk (created 2026-11-23, contains only the bootstrap commit). Expected behavior: the scaffold lands on a feature branch and PR-1; the store's `issues-data` branch never enters the main history.

## 10. Completion gate

Every success criterion passes before the PR-1 deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
