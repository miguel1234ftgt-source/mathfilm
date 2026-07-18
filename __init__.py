# mathfilm/__init__.py

"""
Interfaz pública principal de MathFilm v0.3.
"""

from mathfilm.actions.show import Show
from mathfilm.core.narration import Narration
from mathfilm.core.section import Section
from mathfilm.core.timeline import Timeline
from mathfilm.core.types import (
    Identifier,
    Progress,
    Seconds,
    WordsPerMinute,
)
from mathfilm.engine.video_scene import VideoScene

__version__ = "0.3.0"

__all__ = [
    "Identifier",
    "Narration",
    "Progress",
    "Seconds",
    "Section",
    "Show",
    "Timeline",
    "VideoScene",
    "WordsPerMinute",
]