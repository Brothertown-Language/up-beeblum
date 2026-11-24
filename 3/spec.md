# SPEC: Roadmap, README, AGENTS.md — project documents (stacked stage)

## 1. Intent and Executive Summary

**Problem Statement:** up-beeblum's scaffold (up-beeblum#1, PR #2) carries no identity or operating documentation: no README stating what the project is, no AGENTS.md stating its operative agent rules, and no ROADMAP enumerating the follow-up work the initial-contents stage explicitly deferred.

**Root Cause / Motivation:** The developer directive (2026-11-24) sequences the stacked stage: after the scaffold PR, "create the spec for the needed roadmap file/readme file/agents.md file and implement for stacked PR, then file the follow up specs based on the roadmap." The roadmap is the entry point for all follow-up specs; README and AGENTS are the surfaces every future session and human reader consume first.

**Approach Chosen:** Author the three documents from the 2026-11-23 design record and verified sibling conventions; the roadmap owns sequencing, README owns identity, AGENTS owns operating rules. No machinery changes.

**Alternatives Considered & Why Discarded:**
- *Wiki-based documentation* — discarded: these documents are the repo tree's contract surfaces (the directive names files); wiki is direct-publish and out of the named scope.
- *Deferring AGENTS.md content to per-rule specs* — discarded: the operating rules are design-record facts already fixed; staging them as specs invents ceremony.

**Key Design Decisions:**
- **Roadmap as the follow-up spec catalogue** — each item names its successor spec's scope; status lives in trackers, never in the file.
- **WLRP notation carve-out recorded in AGENTS.md** — text 1 renders in WLRP orthography; the single documented deviation from the parent project's BL-notation ruling (2026-11-23).
- **Provenance posture in README** — biblical texts public-domain per the 2026-11-23 ruling (proofed transcriptions of PD works are PD); Fermino 2000 / Hicks 2006 referenced from the snea-phonetics research tree (`feature/thesis-reference-pdfs`), never copied.

**User Intent / Original Prompt** (developer statements verbatim):
- "then create the spec for the needed roadmap file/readme file/agents.md file and implement for stacked PR, then file the follow up specs based on the roadmap." (2026-11-24)
- Design-record anchors the documents state (2026-11-23, quoted verbatim in up-beeblum#1's spec §1 except where noted): "sub-modules for now are reference only, the repo needs to be self-contained"; "=> Regenerated"; "for now, tex/PDF; markdown"; "version builds what it can covering both complete editions if possible"; "/original/=>/IPA/=>Wampanoag" — "place into the new repo along side the rest of the new"; and the PD ruling — recorded only in this session's chat, never in a store artifact: "proofed public domain is public domain".

## 2. Not Included

- Any machinery — the roadmap describes follow-up items; this spec implements none of them.
- The `__pycache__` debris cleanup itself — the roadmap (R-1) names ignore-policy hardening as a follow-up item.
- Wiki surfaces, CI, website integration — deferred to roadmap consideration.
- The derivation engine, build pipeline, corpus content — the scaffold spec's exclusions carry into the roadmap items.

## 3. Requirements

- **R-1:** `ROADMAP.md` SHALL enumerate the program's follow-up work items — corpus pin-bump ingestion + text-copy regeneration tooling; derivation data (component/allomorph inventory per Fermino/Goddard/Nisinoon + per-form map with verdict flags); stage-1 orthography→IPA conversion (segmentation + rule-class nomination + constrained ML assist); stage-2 deterministic IPA→WLRP letter map incl. the loan-class policy; works registry + spine join; LaTeX/PDF interlinear + Markdown emission; per-row provenance/apparatus rendering; editions coverage manifest; ignore-policy hardening (Python debris: `__pycache__/`) — each with a one-line description and design anchors, carrying no status fields.
- **R-2:** `README.md` SHALL state: what the repository is (quad-text polyglot edition of the Eliot Indian Bible); the four texts (modern WLRP Wampanoag, colonial original orthography, English frame, WEB) and both editions' column sets (1663: WLRP/eliot1663/Geneva/WEB; 1685: WLRP/eliot-E2/KJV/WEB); the self-contained architecture with regenerated text copies + build-manifest provenance; delivery targets (interlinear LaTeX/PDF + Markdown); the reference-only submodules; provenance and licensing posture (biblical texts public-domain per the 2026-11-23 ruling; Fermino 2000 / Hicks 2006 cited by reference from the snea-phonetics research tree); and a pointer to ROADMAP.md.
- **R-3:** `AGENTS.md` SHALL carry the operative rules: build/test/lint/type commands (`uv sync`; `uv run pytest test/`; `uvx ruff check src/ test/`; `uvx pyright src/`); the issue-store flow (`.opencode/tools/local-issues`); branch-before-modification and the human merge boundary; temp-file and AI-attribution rules; the WLRP notation carve-out; the no-regex discipline and the flagged-never-filled discipline for unresolved readings; the reference-only submodule contract and the pin-bump regeneration policy; and the `private/` placement rule.
- **R-4:** The three documents SHALL be mutually consistent on every architecture fact; each operative fact is stated once (single-sourcing) with other mentions pointing at their owner; and each document carries the AI-attribution footer.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | ROADMAP.md exists; each R-1 item appears with a one-line description and design anchor; no status fields | structural | read ROADMAP.md; assert the item set + anchors; `grep -nE '^[[:space:]]*(STATUS|Status|status)[[:space:]]*[:=]' ROADMAP.md` → zero matches |
| SC-2 | README.md carries each R-2 fact, and states unimplemented roadmap facts in intent-only phrasing ("will land via roadmap work"), never as delivered | structural | read README.md; locate and assert each R-2 fact (identity, texts + column sets, architecture/regeneration/manifests, delivery, submodules, provenance/licensing, roadmap pointer); for regeneration and unimplemented roadmap facts, assert the intent-only phrasing |
| SC-3 | AGENTS.md carries each R-3 rule | structural | read AGENTS.md; locate and assert each R-3 rule |
| SC-4 | No fabricated content: every load-bearing claim traces to §7's sources | structural | cross-check each load-bearing claim against §7; any uncited load-bearing claim fails |
| SC-5 | Mutual consistency + single-sourcing + attribution | structural | read all three; assert no operative fact stated twice-as-authority or contradictorily; assert the footer in each |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| up-beeblum#1's spec + scaffold (PR #2) | the documents state the scaffold's established facts | satisfied |
| The 2026-11-23 design record (quoted in up-beeblum#1's spec §1) | the fact source for R-1..R-4 content | satisfied |
| The Fermino/Hicks reference PDFs (tracked, snea-phonetics `feature/thesis-reference-pdfs`) | provenance-referenced resources | satisfied |
| Parent-project conventions (snea-phonetics AGENTS.md) | the operating-rule convention source | satisfied |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1 |
| R-2 | SC-2 |
| R-3 | SC-3 |
| R-4 | SC-4, SC-5 |

Every SC traces (SC-1→R-1, SC-2→R-2, SC-3→R-3, SC-4/SC-5→R-4); no orphans in either direction.

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| The 2026-11-23 design record | conversation | quoted verbatim in up-beeblum#1 spec §1, except the PD ruling ("proofed public domain is public domain"), which is quoted from this session's chat directly (held in session context, 2026-11-23) | read, this session |
| up-beeblum scaffold tree | repository | branch `feature/initial-contents` | read (implement + verify runs, 2026-11-24) |
| snea-phonetics AGENTS.md | project guide | /home/muksihs/git/snea-phonetics/AGENTS.md | read, 2026-11-23 |
| Reference PDFs tracking | store row | snea-phonetics `docs/research/reference-pdfs/` + catalogue rows (branch `feature/thesis-reference-pdfs`) | read + sha-recorded, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (snea-phonetics submodule) | read, 2026-11-23 |
| WLRP research record | session evidence | /tmp/opencode/wlrp-research/, /tmp/opencode/hicks-research/ | subagent reports, 2026-11-23/24 |

## 8. Cost Frame

- **SC-1..SC-3:** document reads cost seconds; skipping costs the documents asserting facts by construction.
- **SC-4:** the claim-by-claim cross-check costs minutes; skipping costs invented content entering the repo's contract surface — the defect class the project's no-fabrication disciplines guard against.
- **SC-5:** the three-document consistency read costs minutes; skipping costs contradicting statements in the repo's first-read surfaces.

## 9. Edge Cases

- **README states a fact the scaffold doesn't yet implement** — Condition: text-copy regeneration (roadmap item) is described but unimplemented. Expected behavior: README/ROADMAP describe intent ("will land via roadmap work") without claiming delivered state; no status fields. Resolution: SC-2's instrument reads intent-only phrasing for unimplemented facts.
- **Name spelling (up-beeblum)** — Condition: the repository name is the modern-orthography rendering of the title. Expected behavior: README records the name's derivation (title word, rule-derived 2026-11-23, reconcile-if-WLRP-publishes note). Resolution: recorded once in README.

## 10. Completion gate

Every success criterion passes before the stage's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
