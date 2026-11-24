# SPEC: Ignore-policy hardening — Python debris

## 1. Intent and Executive Summary

**Problem Statement:** The exact ignore set (up-beeblum#1 R-5) omits Python run debris (__pycache__/, *.pyc) that every test cycle regenerates in the working tree.

**Root Cause / Motivation:** The validated roadmap (up-beeblum#3, ROADMAP.md) sequences this work after the scaffold (up-beeblum#1) and the documents stage; the developer directive (2026-11-24) files the follow-up specs from the roadmap so the pipeline takes items in order of importance.

**Approach Chosen:** Small spec + PR extending .gitignore's effective set by the two debris patterns; SC-4-style equality updated in the executing change's own record.

**Alternatives Considered & Why Discarded:**
- *Landing inside the scaffold or documents stage* — discarded: the roadmap owns sequencing; the item is its own deliverable.
- *Direct implementation without a filed spec* — discarded: the spec is the work's governing record.

**Key Design Decisions:** The exact-set discipline persists — the extension lands via this item's own change, not drift.

**User Intent / Original Prompt** (verbatim): "then file the follow up specs based on the roadmap" (2026-11-24); the item's ROADMAP row states its scope and anchors; the architecture rulings are quoted in up-beeblum#1's spec §1 and in README.md; the PD ruling is session chat, 2026-11-23.

## 2. Not Included

Any other ignore additions; upstream repos.

## 3. Requirements

- **R-1:** `.gitignore`'s effective set SHALL gain exactly `__pycache__/` and `*.pyc`.
- **R-2:** No other patterns SHALL change (the exact-set equality holds: the prior nine + exactly these two).

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | Effective set = prior nine + exactly the two debris patterns | structural | parse .gitignore; set-equality against the expected eleven (R-1, R-2) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| ROADMAP.md (up-beeblum#3) | this item's scope + anchors | satisfied |
| up-beeblum#1 scaffold | the surfaces this item extends | satisfied |


## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1 |
| R-2 | SC-1 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| ROADMAP.md (up-beeblum#3) | roadmap | repository root | read, 2026-11-24 |
| up-beeblum#1 spec R-5 — the exact nine-pattern ignore set | store record | .issues/1/spec.md | read, 2026-11-24 |


## 8. Cost Frame

Each instrument costs a read or run at implementation time (minutes); skipping risks unverified delivery — the failure models §4's instruments exist to observe.

## 9. Edge Cases

- **Input boundary** — a future ignore-set change would collide with the exact-set discipline; SC-1's equality instrument is what catches it, and the change lands by spec, never by drift.
- **Recomposition** — if validation or implementation shows the item over-fat, the recomposition protocol splits it and this spec becomes the umbrella (recorded at that time).

## 10. Completion gate

Every success criterion passes before this item's deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
