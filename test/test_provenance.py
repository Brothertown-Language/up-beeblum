# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Provenance-integrity audit (up-beeblum#5, SC-3 / R-3).

No form is silently assigned: every non-flagged row of the per-form map
carries the provenance marker the class claims; every marker-less row carries
``flagged``. Reads the committed map (the real artifact, all 66,863 rows).
"""

from __future__ import annotations

from pathlib import Path

CLASSES = ("rule-derived", "human-verdict", "flagged")


def _map_rows() -> list[tuple[str, str, str]]:
    path = Path(__file__).resolve().parents[1] / "data/derivations/form-map.tsv"
    lines = path.read_text("utf-8").splitlines()
    data = [line for line in lines if line and not line.startswith("#")][1:]
    rows: list[tuple[str, str, str]] = []
    for line in data:
        parts = line.split("\t")
        match_key, cls = parts[0], parts[1]
        marker = parts[2] if len(parts) > 2 else ""
        rows.append((match_key, cls, marker))
    return rows


def test_map_carries_only_known_classes() -> None:
    rows = _map_rows()
    bad = {cls for _, cls, _ in rows if cls not in CLASSES}
    assert not bad, f"unknown provenance classes: {bad}"


def test_non_flagged_rows_carry_marker() -> None:
    rows = _map_rows()
    silently_assigned = [
        match_key for match_key, cls, marker in rows
        if cls in ("rule-derived", "human-verdict") and not marker.strip()
    ]
    assert not silently_assigned, (
        f"{len(silently_assigned)} rows claim a resolvable class without a "
        f"provenance marker (e.g. {silently_assigned[:5]})"
    )


def test_marker_less_rows_are_flagged() -> None:
    rows = _map_rows()
    offenders = [match_key for match_key, cls, marker in rows if not marker.strip() and cls != "flagged"]
    assert not offenders, (
        f"{len(offenders)} marker-less rows carry a non-flagged class "
        f"(e.g. {offenders[:5]})"
    )


def test_seeded_map_is_fully_honest() -> None:
    """The seed state: every row flagged (SC-3's no-silent-assignment guarantee)."""
    rows = _map_rows()
    unseeded = [(k, c) for k, c, _ in rows if c != "flagged"]
    assert not unseeded, f"{len(unseeded)} rows hold a resolved class at seed state"
