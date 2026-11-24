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

- **R-1:** Works are declared in the registry only; the CLI enumerates targets from it.
- **R-2:** The join consumes the corpus contract's alignment store and versification maps, keyed on verse_id.
- **R-3:** Column sets resolve per edition without hardcoding.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Adding a declared work changes output without code change (R-1) | structural | add a test work row; run; assert the new work renders |
| SC-2 | Joined rows carry verse_id + all declared columns (R-2) | structural | inspect joined output on a known verse range |
| SC-3 | Unknown column in a work declaration fails loudly (R-3) | structural | feed a bad declaration; assert a named error, not silent drop |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Corpus works-registry pattern | model | corpus docs/research/data/eliot-tritext/works-registry.yaml | read, 2026-11-23 |

## 6. Traceability

Each requirement names the SCs verifying it (in §4's criterion wording); each SC names its R-x. No orphans in either direction.

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
