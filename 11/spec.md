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

- The build CLI's remaining behavior — the consumption contract is R-2's deliverable; everything else about the CLI is up-beeblum#8's deliverable.
- Corpus content — the manifest is generated from the contract at pin time, never hand-maintained.

## 3. Requirements

- **R-1:** The manifest SHALL enumerate every book/edition the corpus spine carries, with row + flag counts, and record the source-pin SHA it was generated from.
- **R-2:** The build CLI (roadmap item 5, up-beeblum#8) SHALL consume the manifest; uncovered books SHALL appear as named gaps, never silently absent.
- **R-3:** Manifest regeneration SHALL be part of the pin-bump flow — running the pin-bump procedure SHALL regenerate the manifest.
- **R-4:** An enumerated-unknown book (a manifest state the corpus spine does not carry) SHALL fail the enumeration loudly with a named enumeration error, per the item's stated design.
- **R-5:** A manifest mismatching the spine at build time SHALL fail the build with a named staleness error.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Manifest matches the spine's actual rows | structural | regenerate; compare per-book counts vs the alignment store (R-1) |
| SC-2 | The build CLI's targets + gap notes follow the manifest | structural | run the build CLI; assert target set + gap notes agree with the manifest (R-2) |
| SC-3 | Pin-bump regenerates the manifest | structural | run the pin-bump flow; assert the manifest's source-pin SHA field changes to the new pin's SHA (R-1, R-3) |
| SC-4 | Stale manifest fails the build with the named staleness error | structural | flip a count in a staged manifest; assert the R-5 named staleness failure (R-5) |
| SC-5 | Enumerated-unknown book fails loudly | structural | feed a manifest row naming an absent book; assert the named enumeration failure (R-4) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |
| Roadmap item 1's regeneration tool | the pin-bump flow this integrates with | pending |
| Corpus spine (alignment store at the recorded pin) | the data SC-1's enumeration compares against | pending |
| Up-beeblum#8 (build CLI) | the consuming surface R-2 mandates | pending |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1, SC-3 |
| R-2 | SC-2 |
| R-3 | SC-3 |
| R-4 | SC-5 |
| R-5 | SC-4 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| Corpus exports contract | project guide | corpus/AGENTS.md (the corpus/ submodule — Brothertown-Language/algonquian-library) | read, 2026-11-23 |


## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Upstream data maturity** — the corpus surface this item consumes may be incomplete per book/edition; the coverage-driven model builds what exists and flags the rest, never fabricates; manifests record flags.

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
