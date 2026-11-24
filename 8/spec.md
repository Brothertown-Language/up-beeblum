# SPEC: Works registry + spine join

## 1. Intent and Executive Summary

**Problem Statement:** The quad edition needs its declarative work definitions and the verse-keyed column join across the contract's alignment store.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** A works registry (per-edition column sets: 1663 = wlp/eliot1663/geneva1599/web; 1685 = wlp/eliot-E2/kjv/web) + the build CLI joining columns on the verse-ID spine, in the corpus works-registry pattern ({corpus, column, role} resolution).

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** Declarative only — the generator hardcodes no works; composite views per the corpus pattern (SC-M3c); the spine is the contract's verse_id.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

Rendering (roadmap item 6); corpus-side registry changes.

## 3. Requirements

- **R-1:** Works SHALL be declared in the registry only; the CLI SHALL enumerate targets from it.
- **R-2:** The join SHALL consume the corpus contract's alignment store and versification maps, keyed on verse_id.
- **R-3:** Column sets SHALL resolve per edition without hardcoding.
- **R-4:** An invalid column declaration SHALL fail with a named error — never silently dropped.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | A declared work renders without code change | structural | add a test work row; run; assert rendering; assert no hardcoded works in the generator (R-1, R-3) |
| SC-2 | Joined rows carry verse_id + declared columns | structural | inspect joined output on a known verse range (R-2) |
| SC-3 | Invalid column declaration fails with a named error | structural | feed a bad declaration; assert the named error (R-4) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Corpus works-registry pattern | the declarative model this registry follows | satisfied |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1 |
| R-2 | SC-2 |
| R-3 | SC-1 |
| R-4 | SC-3 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (snea-phonetics submodule tree) | read, 2026-11-23 |


## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.
- **Recomposition** — if validation or implementation shows the item over-fat for one PR, the recomposition protocol splits it; this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
