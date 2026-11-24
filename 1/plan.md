# PLAN: up-beeblum#1 — Repository initial contents (scaffold)

## 1. Goal

Implements the validated spec `up-beeblum#1`: establishes the repository's mechanical scaffold — package directory, uv/pytest/ruff/pyright toolchain, smoke-tier test, committed-data skeleton, the two reference-only submodules, the exact ignore set, and the `private/` placement manifest — verified from a fresh clone. PR-1 carries the squashed work.

## 2. Execution surface

Repository: `Brothertown-Language/up-beeblum` (this workspace). Branch: `feature/initial-contents`, cut from `main` (root commit `68948da`, the pushed default). Environment facts the items depend on: `uv`/`uvx` on PATH; origin = `git@github.com:Brothertown-Language/up-beeblum.git`; the `issues-data` store branch never enters feature work.

## 3. Items

**Item 1 — Toolchain declaration (SC-5)**
- **Deliverable:** `pyproject.toml` + `uv.lock` declaring `[project]` (`up-beeblum`, dev deps: pytest), `[tool.pytest.ini_options]` with `testpaths = ["test"]`, `[tool.ruff]`, `[tool.pyright]` with `include = ["src"]`.
- **RED:** `uv sync` exits non-zero (no `pyproject.toml` in the tree).
- **GREEN:** write `pyproject.toml`; run `uv sync` to produce `uv.lock`.
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** read `pyproject.toml`; assert the three R-2 values; `uv sync` exit 0.

**Item 2 — Smoke suite, collectable (SC-8)**
- **Deliverable:** `test/test_smoke.py` — one test asserting the package import fails-or-succeeds as written (the RED state: import of `up_beeblum`).
- **RED:** `uv run pytest test/ --collect-only -q` reports 0 tests (no `test/` directory).
- **GREEN:** write the test file; collection reports 1 test (the test itself still red — import fails — which Item 3 turns green).
- **Tier marks:** the authored test is **smoke tier** (the default run; no mark needed, register-free by the test-discipline default).
- **Instrument:** `uv run pytest test/ --collect-only -q` count ≥ 1, exit 0.

**Item 3 — Package skeleton (SC-6)**
- **Deliverable:** `src/up_beeblum/__init__.py` (docstring + attribution footer); the pyproject gains `pythonpath = ["src"]` under pytest config so the import resolves from a source checkout.
- **RED:** `uv run pytest test/` fails — the smoke test's import raises ModuleNotFoundError.
- **GREEN:** write the package file; the smoke test passes.
- **Tier marks:** authors no tests; the Item 2 test is the instrument's carrier.
- **Instrument:** `uv run pytest test/` exit 0; path-existence for `src/up_beeblum/__init__.py`.

**Item 4 — Reference submodules (SC-3)**
- **Deliverable:** `.gitmodules` declaring `corpus/` → `github.com/Brothertown-Language/algonquian-library` and `snea-lib/` → `github.com/Brothertown-Language/snea-lib`; gitlinks staged; both submodule checkouts de-initialised so the paths stay unmaterialized (per-path, non-recursive).
- **RED:** `.gitmodules` absent — `git config --file .gitmodules --list` exits non-zero.
- **GREEN:** `git submodule add` each origin at its path, then `git submodule deinit` each (leaving the gitlinks + the declared config, no working trees).
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** `git config --file .gitmodules --list` output compared to R-3's values; both checkout paths remain absent.

**Item 5 — Data skeleton (SC-2)**
- **Deliverable:** `data/editions/1663-first/`, `data/editions/1685-second/`, `data/derivations/`, `data/manifests/`, each carrying a `.gitkeep` placeholder; no book content.
- **RED:** none of the four paths exist.
- **GREEN:** create the directories with `.gitkeep`.
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** path-existence check enumerating the four paths.

**Item 6 — Ignore set (SC-4)**
- **Deliverable:** `.gitignore` whose effective pattern set equals exactly: `.issues/`, `.opencode/`, `private/`, `tmp/`, `outputs/`, `*.aux`, `*.log`, `*.out`, `*.toc`.
- **RED:** `.gitignore` absent (or its line set differs from the R-5 enumeration).
- **GREEN:** write the file with exactly the eight patterns plus a generated-output comment block (comment lines excluded from the effective set the instrument parses).
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** parse `.gitignore` effective lines; set-equality against the R-5 list.

**Item 7 — Private/ placement manifest (SC-7)**
- **Deliverable:** `private/.gitignore` (self-exclusion by default) and `private/README.md` (manifest of record note: in-copyright material untracked; acquisition-route inventory).
- **RED:** `private/` absent.
- **GREEN:** create both files.
- **Tier marks:** authors no tests; instrument class = fact check.
- **Instrument:** path-existence of both files; `git check-ignore private/` reports exclusion.

**Item 8 — Fresh-clone integration run (SC-1)**
- **Deliverable:** the executed proof, no new files: the scaffold's self-containment claim demonstrated from a clean clone.
- **RED:** clone `origin/main` to a temp dir; `uv sync` exits non-zero (empty scaffold — the current pushed state).
- **GREEN:** clone the `feature/initial-contents` worktree to a temp dir; assert `corpus/` and `snea-lib/` absent; `uv sync && uv run pytest test/` exits 0.
- **Tier marks:** authors no tests; instrument class = recorded dispatch evidence (this run's output cited in the PR body).
- **Instrument:** the clone-run commands above, executed and recorded this cycle.

## 4. Dependency order

Items 1→2→3 (toolchain before the suite before the package the suite imports); Items 4→5 are independent of 1–3 but precede Item 8 (the fresh clone must contain every scaffold element the final run proves); Items 6→7 are independent of everything but also precede Item 8 (the clone-run's environment is the fully scaffolded tree); Item 8 runs last against the completed branch. No cycles: each item's RED/GREEN references only earlier state.

## 5. Traceability

| Item | SC |
|------|----|
| Item 1 | SC-5 |
| Item 2 | SC-8 |
| Item 3 | SC-6 |
| Item 4 | SC-3 |
| Item 5 | SC-2 |
| Item 6 | SC-4 |
| Item 7 | SC-7 |
| Item 8 | SC-1 |

Every SC carries exactly one item; every item traces to exactly one SC — no orphans in either direction.

## 6. Verification summary

- Fact checks (run at item cycle time): Items 1, 3–7's path/config/line-set checks.
- Authored tests: one — `test/test_smoke.py` (Item 2), **smoke tier**, the default run.
- Recorded dispatch evidence: Item 8's fresh-clone run output — cited in the PR body (the SC-1 behavioral proof).
- At cycle time: Items 1–7's instruments; at PR-check time: Item 8's full run re-stated from its recorded output.

## 7. Status boundary

No status fields or completion markers in this plan. Implementation state lives in the pipeline; loop history in `.issues/1/audit/validation.yaml`.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
