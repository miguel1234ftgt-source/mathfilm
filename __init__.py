# mathfilm/__init__.py

"""
Interfaz pública principal de MathFilm v0.8.0.
"""

from mathfilm.actions.create import Create
from mathfilm.actions.factories import (
    create_all,
    hide_all,
    parallel,
    show_all,
    write_all,
)
from mathfilm.actions.hide import Hide
from mathfilm.actions.move_to import MoveTo
from mathfilm.actions.parallel import Parallel
from mathfilm.actions.rotate import Rotate
from mathfilm.actions.scale import Scale
from mathfilm.actions.sequence import Sequence
from mathfilm.actions.set_color import SetColor
from mathfilm.actions.set_opacity import SetOpacity
from mathfilm.actions.shift import Shift
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

__version__ = "0.8.0"

__all__ = [
    "Create",
    "Hide",
    "Identifier",
    "MoveTo",
    "Narration",
    "Parallel",
    "Progress",
    "Rotate",
    "Scale",
    "Seconds",
    "Section",
    "Sequence",
    "SetColor",
    "SetOpacity",
    "Shift",
    "Show",
    "Stagger",
    "Timeline",
    "Transform",
    "VideoScene",
    "WordsPerMinute",
    "Write",
    "create_all",
    "hide_all",
    "parallel",
    "show_all",
    "write_all",
]