#mathfilm/__init__.py

"""
Interfaz pública principal de MathFilm v0.3.
"""

from actions import Show
from core import (
    Identifier,
    Narration,
    Progress,
    Seconds,
    Section,
    Timeline,
    WordsPerMinute
)

from engine import VideoScene

__version__ = "0.3.0"

__all__ = [
    "Identifier",
    "Narration",
    "Progress",
    "Seconds",
    "Section",
    "Timeline",
    "WordsPerMinute"
]