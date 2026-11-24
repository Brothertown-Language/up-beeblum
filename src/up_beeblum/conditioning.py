# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Conditioning rule engine for the Wampanoag prefix system — up-beeblum#5.

Applies the personal-prefix conditioning rules recorded in the component
inventory (``data/derivations/components.tsv``, rule ids R01..R08) to produce
inflected surfaces. Rules are data-sourced: every surface rule cites the thesis
(Fermino 2000) page or the corpus's Goddard-1981 proofed lines it encodes.

Conversion is segmentation + rule classes — never regex on the surface; the
only pattern logic here is the stem-initial class a caller supplies (its
identity is a lexicon-side attribute, derived in the item-3 map stage, never
regex-sniffed here).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY_PATH = REPO_ROOT / "data" / "derivations" / "components.tsv"

SLOTS = ("1", "2", "3", "X", "1p", "12", "2p", "3p")
BASE_PREFIX = {"1": "nu", "2": "ku", "3": "wu", "X": "mu", "1p": "nu", "12": "ku", "2p": "ku"}


@dataclass(frozen=True)
class InflectionClass:
    """The noun-class metadata an inflected stem carries (lexicon-side facts)."""

    NI: bool
    dependent: bool
    initial: str  # "consonant" | "vowel" | "8" | "hC" | concrete letter (m/p/k/w)
    pos_theme: str = ""


def _prefix(slot: str, stem: str, cls: InflectionClass) -> str:
    if slot == "X":
        # mu- conditions like the other prefixes where the thesis attests it
        # (muhkôt: dependent vowel-initial drops the prefix vowel, p.19).
        if cls.initial == "vowel" and cls.dependent:
            return "m"
        return BASE_PREFIX["X"]
    base = BASE_PREFIX["1" if slot in ("1", "1p") else "2" if slot in ("2", "12", "2p") else "3"]
    if cls.initial == "8":
        # R07: third-person wu- is deleted entirely before /8/-initial stems
        # (singular and plural both surface without the prefix, p.22);
        # R06: the other prefixes lose their vowel before /8/-initial stems.
        if slot in ("3", "3p"):
            return ""
        return base[0]
    if cls.initial == "vowel" and cls.dependent:
        # R03: dependent vowel-initial: the prefix drops its vowel.
        return base[0]
    if cls.initial == "vowel" and not cls.dependent:
        # R04: non-dependent vowel-initial: full prefix + intrusive -t-.
        return f"{base}t"
    third = slot in ("3", "3p")
    if third and cls.initial == "hC":
        # R08: wu- retained before Mass /hC/ (wuh-); uh- is the attested
        # variant (a form matching either variant is rule-derived).
        return "wuh"
    if third and stem[0] in "mpkw":
        # R05: third person drops its w before m/p/k/w-initial stems.
        return "u"
    # R01/R02: expected full prefix (consonant-initial general).
    return base


def _suffixes(slot: str, cls: InflectionClass, pl_obj: bool = False) -> str:
    out = ""
    if slot in ("1p", "12"):
        out += "un"  # S01
    elif slot in ("2p", "3p"):
        out += "uw"  # S02
    if pl_obj:
        # S05: plural-object markers -ash (NI) / -ak (NA); the 3p carries the
        # intervening -ôw- before the marker.
        out += "ôw" if slot == "3p" else ""
        out += "ash" if cls.NI else "ak"
    if not cls.NI and slot == "3":
        out += "ah"  # S04 (3p's -ôw-ah handled below)
    if not cls.NI and slot == "3p":
        out += "ôwah"  # S04: theme surfaces -uw + -ôw- + -ah
    return out


def third_person_forms(stem: str, cls: InflectionClass) -> set[str]:
    """The attested third-person surfaces for ``stem`` (R08's variant spellings).

    Before Mass /hC/ clusters (PA *wC- etyma whose *w survives as the /h/
    cluster on the stem) the third-person prefix wu- is retained — the
    attested spellings are wuh- and its uh- (u-) variant (Goddard 1981).
    """
    stem = stem.lstrip("-")
    if cls.initial == "hC":
        return {"wu" + stem, "u" + stem}
    return {inflect(stem, cls, slots=("3",))["3"]}


def inflect(stem: str, cls: InflectionClass, slots: tuple[str, ...] = SLOTS,
            pl_obj: bool = False) -> dict[str, str]:
    """Inflect ``stem`` across the personal slots, conditioned per the inventory."""
    stem = stem.lstrip("-")
    forms: dict[str, str] = {}
    for slot in slots:
        prefix = _prefix(slot, stem, cls)
        body = stem
        if slot != "X" and cls.pos_theme:
            body = body + cls.pos_theme  # T01: possession theme -m class
        forms[slot] = prefix + body + _suffixes(slot, cls, pl_obj)
    return forms
