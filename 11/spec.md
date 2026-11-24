# SPEC: Editions coverage manifest

## 1. Intent and Executive Summary

**Problem Statement:** The coverage-driven rule ('builds what it can covering both complete editions if possible') needs its manifest surface.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** A coverage manifest enumerating per edition/book: the corpus spine's rows, their flag states, and what the build covers; the build reads it to decide targets.

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** The manifest is generated from the corpus contract at pin time, never hand-maintained; unknown books fail the enumeration loudly.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

The build pipeline's other stages; corpus content.

## 3. Requirements

- **R-1:** The manifest enumerates every book/edition the corpus spine carries, with row + flag counts.
- **R-2:** The build consumes the manifest; uncovered books appear as named gaps, never silently absent.
- **R-3:** Manifest regeneration is part of the pin-bump flow.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Manifest matches the corpus spine's actual rows (R-1) | structural | regenerate; compare per-book counts to the alignment store |
| SC-2 | Build targets + gap notes follow the manifest (R-2) | structural | run the build; assert target set and gap notes agree with the manifest |
| SC-3 | Stale manifest fails the build (R-3) | structural | flip a manifest count; assert the named staleness failure |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Roadmap item 1's regeneration tool | upstream | up-beeblum item 1's ticket | pending |

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
