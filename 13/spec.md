# SPEC: Research — EGGROLL (zero-backprop training) as the training option for the orthography→IPA conversion NN

## 1. Intent and Executive Summary

**Problem Statement:** The Stage-1 orthography→IPA conversion engine (up-beeblum#6; ROADMAP item 3) plans a constrained NN ML assist — a torch subproject in the corrector pattern that ranks and corrects within legal phoneme space, confidence-gated, weights regenerable from tracked training data, output provisional until a reviewed verdict lands. No training-method evaluation exists for that assist: the engine spec records the assist's behavior gates, but the method by which its weights are trained rests on an unevidenced default (the backprop-trained default implied by the torch placement). The developer (2026-11-24) has named EGGROLL — "a way to train massive neural networks with zero backprop" — as the option to research for this training need; the decision currently has no evidence record.

**Root Cause / Motivation:** The conversion chain /original/=>/IPA/=>Wampanoag was architectured on 2026-11-23 with a NN assist for the orthography conversion (quoted ruling in up-beeblum#1 spec §1); up-beeblum#6 fixed the assist's behavioral contract, not its training method. EGGROLL (Evolution Guided GeneRal Optimisation via Low-rank Learning; "Evolution Strategies at the Hyperscale", arXiv:2511.16652, v2 2026-02-16, Sarkar/Fellows/Duque et al.) is an evolution-strategies variant that structures each population member's parameter perturbation as a rank-r matrix, evaluates fitness forward-only (no backpropagation pass), and fuses the population-summed high-rank update directly into the parameters; it reports a ~100× speed-up over naïve ES, up to 91% of pure batch-inference throughput, and generality to any inference system with a defined fitness function, including non-differentiable components. The developer's directive (2026-11-24) names it as the option to research for the conversion training need; the evaluation is owed before the assist's training path is built, at up-beeblum#6 planning time.

**Approach Chosen:** A research deliverable under this issue's store folder (research/): an evaluation report grounded on the primary sources (the arXiv paper and the released reference code), evaluating EGGROLL's mechanics and evidence against the assist's stated constraint set (up-beeblum#6 R-1–R-4 + ROADMAP item 3), comparing it to the backprop-trained default on the adoption-deciding axes, and recording one dated recommendation as the decision input for up-beeblum#6's implementation. No model code, no dependency changes, no training runs land from this spec.

**Alternatives Considered & Why Discarded:**
- *Folding the evaluation into the up-beeblum#6 spec* — discarded: the directive names the research as its own item; #6's spec carries the engine's behavioral contract, and pre-committing its approach text to a method before the evaluation lands would put the decision ahead of its evidence; the report is the record #6's planning cites.
- *Researching a different training family (Forward-Forward, zeroth-order/MeZO, OpenAI-style naïve ES) instead* — discarded: the developer named EGGROLL as the option; other families surface only as comparison context where the verdict needs them.
- *Adopting EGGROLL directly into the #6 approach without evaluation* — discarded: no fit evidence exists for this task; the paper's demonstrations (pure-int integer RNN pretraining, RWKV RL post-training) do not cover a constrained correction task over a phoneme space.

**Key Design Decisions:** The deliverable is a recommendation, not a commitment — the evaluation decides, and the #6 planning consumes the verdict. Evaluation axes are fixed by the assist's own constraint set, so the verdict is directly consumable there. Primary-source grounding (paper + released code) is mandated since the term has fast-moving secondary coverage; secondary summaries are context only.

**User Intent / Original Prompt** (verbatim, dated): "add a spec to research 'EGGROLL, a way to train massive neural networks with zero backprop' as the option for training the neural network for the legacy orthography/ipa conversion needs" (developer directive, 2026-11-24). Anchors: "we should be able to use a neural network for improved handling of the orthography conversion based on pronunciations? /original/=>/IPA/=>Wampanoag" (2026-11-23, quoted in up-beeblum#1 spec §1); ROADMAP item 3 (up-beeblum#3).

## 2. Not Included

- Training implementation, model code, or dependency additions (torch, ES libraries) — the research is an evaluation record; implementation follows the pipeline on up-beeblum#6.
- Amendments to up-beeblum#6's spec text — its revision happens when the research verdict is consumed there, not under this spec.
- Non-EGGROLL training families as research subjects — they appear only as comparison context where the verdict needs them.
- Re-exposition of EGGROLL's theory (derivations/proofs) — the report cites the paper; it does not reproduce it.
- Stage-2 letter rendering and rendering/apparatus (per up-beeblum#6's exclusions).

## 3. Requirements

- **R-1:** The research report SHALL ground its EGGROLL mechanism and claims on the primary sources — arXiv:2511.16652 and the released reference code (ESHyperscale/HyperscaleES, nano-egg) — with each load-bearing claim carrying a resolving citation; secondary summaries appear only as context, and nothing load-bearing rests solely on them.
- **R-2:** The report SHALL evaluate EGGROLL against each constraint the assist's spec states — up-beeblum#6 R-1–R-4 and ROADMAP item 3's terms: constrained decoding to legal phoneme space, confidence gating, provisional flags until reviewed verdict, weights regenerable from tracked training data, and the torch subproject placement — stating how ES-style training interacts with each, or that it is orthogonal.
- **R-3:** The report SHALL compare EGGROLL against the backprop-trained default on the adoption-deciding axes: throughput/compute cost at this task's expected model scale (with the estimating assumptions stated), objective/fitness design for the correction task (correction accuracy against reviewed per-form verdicts), toolchain fit (the jax-based released references vs the torch placement), and training-run maturity/regenerability.
- **R-4:** The report SHALL record exactly one dated recommendation — adopt EGGROLL as the training method, retain the backprop default, or a conditional/hybrid path — with its rationale and the decisive evidence, filed under this issue's store folder.

## 4. Success criteria

| ID | Criterion | Class | Instrument |
|------|-----------|-------|------------|
| SC-1 | The report's mechanics section states the mechanism class accurately (Gaussian ES variant; per-member forward-only fitness evaluations; rank-r low-rank perturbations; population-summed high-rank fused updates) consistent with the primary paper, and every load-bearing claim carries a resolving primary-source citation | structural | read .issues/13/research/ report; compare the mechanics statements against arXiv:2511.16652's abstract/TL;DR text; enumerate load-bearing claims and assert each citation resolves to the cited source text or code path (R-1) |
| SC-2 | The report contains a constraint-by-constraint evaluation covering all five stated constraints | structural | read the report; match each named constraint (constrained decode, confidence gate, provisional flags, weight regenerability, torch placement) to its evaluation; assert none missing (R-2) |
| SC-3 | The report contains the backprop-baseline comparison addressing each named adoption axis with evidence | structural | read the report; assert the four axes (scale throughput/cost with stated assumptions, fitness design, toolchain fit, maturity/regenerability) each carry an evidenced treatment (R-3) |
| SC-4 | The report records exactly one dated recommendation among the three stated options, with rationale and decisive evidence, filed under the store folder | structural | read the report's verdict section; assert exactly one of {adopt, retain default, hybrid/conditional} with rationale + decisive evidence + date, at the stated path (R-4) |

## 5. Dependencies

| Reference | Relationship | Status |
|-----------|--------------|--------|
| up-beeblum#6 spec | the engine whose ML assist is the research subject; its constraint set is the evaluation frame | satisfied (read) |
| ROADMAP.md (up-beeblum#3) | item 3's ML-assist terms (torch corrector pattern, regenerable weights) | satisfied (read) |
| arXiv:2511.16652 (v2) | the primary paper; the mechanics/claims anchor | satisfied (fetched 2026-11-24) |
| ESHyperscale/HyperscaleES, ESHyperscale/nano-egg | released jax reference implementations | pending (examined at research execution) |

## 6. Traceability

| Requirement | Success criteria |
|-------------|------------------|
| R-1 | SC-1 |
| R-2 | SC-2 |
| R-3 | SC-3 |
| R-4 | SC-4 |

## 7. Documentation Sources

| Source | Type | Location | Verification |
|--------|------|----------|--------------|
| "Evolution Strategies at the Hyperscale" (arXiv:2511.16652, v2 2026-02-16) | paper | https://arxiv.org/abs/2511.16652 | fetched 2026-11-24 |
| EGGROLL project page (TL;DR, algorithm walkthrough, code links) | project site | https://eshyperscale.github.io/ | fetched 2026-11-24 |
| ROADMAP.md | roadmap | repository root | read 2026-11-24 |
| up-beeblum#6 spec | spec | .issues/6/spec.md | read 2026-11-24 |
| up-beeblum#1 spec §1 (architecture rulings quoted) | spec | .issues/1/spec.md | read 2026-11-24 |
| pyproject.toml + src/ tree | repo state | repository root / src/up_beeblum/ | read + globbed 2026-11-24 (no NN code, no torch dependency — current state) |

## 8. Cost Frame

Each instrument is a read/spot-verification of the report at research time (minutes); skipping risks an unevidenced method decision baked into #6 — citation drift (SC-1), a constraint gap (SC-2), an unsubstantiated comparison (SC-3), or a missing/unbounded verdict (SC-4) each costs a wrong training-path decision downstream.

## 9. Edge Cases

- **Term conflation** — Condition: secondary sources conflate EGGROLL with other zero-backprop families (Forward-Forward, zeroth-order optimization). Expected: the report pins the mechanism class per the primary paper, not secondary framing. Resolution: R-1/SC-1.
- **Preprint maturity** — Condition: v2 is an early research checkpoint (the authors' own framing); results may move. Expected: maturity and moving-target risk appear in the verdict's grounds. Resolution: R-3/SC-3, R-4/SC-4.
- **Task-class mismatch** — Condition: the paper's demonstrations (pure-integer RNN pretraining; RWKV 1.5B/7B RL post-training on countdown/GSM8K) include no constrained correction task over a phoneme space. Expected: the evaluation treats this axis explicitly rather than extrapolating headline results. Resolution: R-2/SC-2.
- **Toolchain mismatch** — Condition: the released reference implementations are jax-based while the assist is planned as a torch subproject. Expected: the comparison states the adaptation path and its risk, not an assumption. Resolution: R-3/SC-3.
- **Fitness-estimation noise** — Condition: ES fitness estimates carry sampling noise; the assist's confidence gating must not be confounded with the update noise. Expected: the evaluation separates the two layers. Resolution: R-2/SC-2.

## 10. Completion gate

Every success criterion passes before this issue's research deliverable is complete; partial implementation is not permitted.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
