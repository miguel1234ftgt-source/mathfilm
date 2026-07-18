# mathfilm/__init__.py

"""
Interfaz pública principal de MathFilm v0.4.
"""

from mathfilm.actions.show import Show
from mathfilm.actions.hide import Hide
from mathfilm.actions.move_to import MoveTo
from mathfilm.actions.write import Write

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

__version__ = "0.4.0"

__all__ = [
    "Show",
    "Hide",
    "MoveTo",
    "Write",
    "Identifier",
    "Narration",
    "Progress",
    "Seconds",
    "Section",
    "Timeline",
    "VideoScene",
    "WordsPerMinute",
]