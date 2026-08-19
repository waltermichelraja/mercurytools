"""entry point for the `mercurytools` console script."""


from __future__ import annotations

from mercurytools import __version__


def main() -> None:
    """print the installed mercurytools version."""
    print(__version__)