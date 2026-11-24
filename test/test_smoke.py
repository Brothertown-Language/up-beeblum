# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Smoke tier: the up_beeblum package imports from a source checkout.

The scaffold's default-tier test — this is the suite SC-1's fresh-clone run
executes; it must stay fast, dependency-light, and self-contained (it
imports neither submodule).
"""

# Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)


def test_package_imports() -> None:
    """The package is importable from the source tree."""
    import up_beeblum

    assert up_beeblum.__name__ == "up_beeblum"
