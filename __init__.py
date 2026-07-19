# mathfilm/__init__.py

"""
Interfaz pública principal de MathFilm v0.6.1.
"""

from mathfilm.actions.create import Create
from mathfilm.actions.hide import Hide
from mathfilm.actions.move_to import MoveTo
from mathfilm.actions.parallel import Parallel
from mathfilm.actions.sequence import Sequence
from mathfilm.actions.show import Show
from mathfilm.actions.stagger import Stagger
from mathfilm.actions.transform import Transform
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

__version__ = "0.6.1"

__all__ = [
    "Create",
    "Hide",
    "Identifier",
    "MoveTo",
    "Narration",
    "Parallel",
    "Progress",
    "Seconds",
    "Section",
    "Sequence",
    "Show",
    "Stagger",
    "Timeline",
    "Transform",
    "VideoScene",
    "WordsPerMinute",
    "Write",
]