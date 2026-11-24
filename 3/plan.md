# PLAN: up-beeblum#3 — Roadmap, README, AGENTS.md

## 1. Goal

Implements the validated spec up-beeblum#3: authors the three project documents — `ROADMAP.md` (the follow-up spec catalogue), `README.md` (identity/architecture/provenance), `AGENTS.md` (operative agent rules) — from the design record, cross-checked claim by claim, consistent with the scaffold and single-sourced across the trio. PR #2 carries the work (the stacked scope's open branch).

## 2. Execution surface

Repository `Brothertown-Language/up-beeblum`; working branch `feature/initial-contents` (the scope's open branch — the documents land as this issue's commits and ride PR #2's stacked shape); the store (`.issues/3/`) is workspace data outside the tree. Toolchain: none of the items builds or runs code — authoring plus the read/grep instruments.

## 3. Items

**Item 1 — ROADMAP.md (SC-1)**
- **Deliverable:** `ROADMAP.md` enumerating the nine R-1 follow-up items with one-line descriptions and design anchors (spec/issue + session-record references), no status fields.
- **RED:** `ROADMAP.md` absent; the R-1 item enumeration fails.
- **GREEN:** write the file from §7's design record; each item names its successor spec's scope.
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** read ROADMAP.md; locate each of the nine R-1 items + anchors; `grep -nE '^[[:space:]]*(STATUS|Status|status)[[:space:]]*[:=]' ROADMAP.md` → zero matches.

**Item 2 — README.md (SC-2)**
- **Deliverable:** `README.md` stating the R-2 facts, with the name-derivation note and intent-only phrasing for unimplemented facts.
- **RED:** `README.md` absent.
- **GREEN:** write the file from the design record; the regeneration fact is phrased as roadmap-work intent.
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** read README.md; locate and assert each R-2 fact + intent-only phrasing for unimplemented roadmap facts.

**Item 3 — AGENTS.md (SC-3)**
- **Deliverable:** `AGENTS.md` carrying the R-3 operative rules, including the WLRP notation carve-out and the flagged-never-filled/no-regex disciplines.
- **RED:** `AGENTS.md` absent.
- **GREEN:** write the file from the sibling convention set (adjusted to this repo's facts).
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** read AGENTS.md; locate and assert each R-3 rule.

**Item 4 — Claim cross-check (SC-4)**
- **Deliverable:** the executed claim-by-claim cross-check record (chat, not a file): every load-bearing claim in the three documents traced to §7's sources.
- **RED:** cannot run before Items 1–3 exist (nothing to cross-check).
- **GREEN:** run the cross-check; an uncited load-bearing claim is an authoring defect fixed in the owning document.
- **Tier marks:** authors no tests; instrument class = recorded dispatch evidence.
- **Instrument:** the cross-check walk, executed at cycle time, findings remediated in place.

**Item 5 — Consistency + single-sourcing pass (SC-5)**
- **Deliverable:** the executed three-document consistency read; contradictions or doubled authorities fixed in place.
- **RED:** requires Items 1–3 complete.
- **GREEN:** read all three; assert single-sourcing + no contradictions; assert the attribution footer in each.
- **Tier marks:** authors no tests; instrument class = recorded dispatch evidence.
- **Instrument:** the consistency read, executed at cycle time.

## 4. Dependency order

Items 1→2→3 author independently; Items 4→5 consume their union and run last. No cycles.

## 5. Traceability

| Item | SC |
|------|----|
| Item 1 | SC-1 |
| Item 2 | SC-2 |
| Item 3 | SC-3 |
| Item 4 | SC-4 |
| Item 5 | SC-5 |

Every SC carries exactly one item; every item traces to exactly one SC.

## 6. Verification summary

- Fact checks: Items 1–3's read/locate/grep instruments.
- Recorded dispatch evidence: Items 4–5's executed walks (cited in the PR body's evidence section).
- Authored tests: none — the stage is documentation-only.

## 7. Status boundary

No status fields; loop history in `.issues/3/audit/validation.yaml`.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
