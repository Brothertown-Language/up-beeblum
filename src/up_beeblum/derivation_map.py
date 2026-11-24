# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Per-form derivation map builder — up-beeblum#5.

Seeds the per-match_key provenance map over the corpus lexicon
(``corpus/docs/research/data/eliot-tritext/lexicon/word-forms.tsv`` at the
recorded pin). Seeding policy (the derive-and-flag discipline's data side):
every form enters the map carrying a provenance class from birth; at seed
time no lexicon-side class metadata is derived, so every form is seeded
``flagged`` — no form is ever silently assigned. Resolution to
``rule-derived`` / ``human-verdict`` happens per-row later, only with the
provenance marker row, never silently.

The seed is deterministic per corpus pin: same pin, byte-identical output.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS_ROOT = REPO_ROOT / "corpus"
LEXICON_REL = Path("docs/research/data/eliot-tritext/lexicon/word-forms.tsv")
MAP_PATH = REPO_ROOT / "data" / "derivations" / "form-map.tsv"
MANIFEST_PATH = REPO_ROOT / "data" / "derivations" / "form-map.manifest.json"

MAP_HEADER = (
    "# Per-form derivation map — up-beeblum#5. Seeded flagged (derive-and-flag:\n"
    "# no form is silently assigned). Resolution carries a provenance marker\n"
    "# per-row, never silently. Deterministic per corpus/ pin; the manifest\n"
    "# beside this file records the corpus SHA this map was generated from.\n"
    "match_key\tprovenance_class\tmarker\tnote"
)


def _corpus_sha(corpus_root: Path) -> str:
    """The corpus/ pin SHA this map is generated from (recorded in the manifest)."""
    pin = (corpus_root / ".git").is_dir()
    if pin:
        return subprocess.run(
            ["git", "-C", str(corpus_root), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    # corpus/ checked out as a plain tree (no .git): record the tree identity
    # from the parent repo's submodule status instead — never guessed.
    out = subprocess.run(
        ["git", "ls-files", "--stage", "corpus"],
        check=True, capture_output=True, text=True,
    ).stdout
    return out.split(" ")[1].strip() if out else "unknown"


def build_map(corpus_root: Path) -> str:
    """Build the map text: every lexicon match_key, class ``flagged``, seed rows."""
    lexicon = corpus_root / LEXICON_REL
    rows = lexicon.read_text("utf-8").splitlines()
    if not rows or not rows[0].startswith("match_key"):
        raise ValueError(f"unexpected lexicon format: {lexicon}")
    keys = [line.split("\t")[0] for line in rows[1:] if line]
    seen: set[str] = set()
    body: list[str] = []
    for key in keys:
        if key in seen:
            raise ValueError(f"duplicate match_key in lexicon: {key}")
        seen.add(key)
        body.append(f"{key}\tflagged\t\t")
    return MAP_HEADER + "\n" + "\n".join(body) + "\n"


def emit(corpus_root: Path = DEFAULT_CORPUS_ROOT, map_path: Path = MAP_PATH,
         manifest_path: Path = MANIFEST_PATH) -> int:
    text = build_map(corpus_root)
    map_path.write_text(text, "utf-8")
    manifest = {
        "artifact": "form-map.tsv",
        "corpus_sha": _corpus_sha(corpus_root),
        "rows": text.count("\n") - MAP_HEADER.count("\n") - 1,  # data rows (colheader excluded)
        "provenance_classes": {"flagged": "seed state; rule-derived/human-verdict resolve per-row with a marker"},
        "generator": "src/up_beeblum/derivation_map.py",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", "utf-8")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    corpus_root = Path(argv[0]) if argv else DEFAULT_CORPUS_ROOT
    return emit(corpus_root)


if __name__ == "__main__":
    raise SystemExit(main())
