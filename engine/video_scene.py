"""
Escena base para MathFilm
"""


from __future__ import annotations
import manim

from ..core.director import Director
from ..core.narration import Narration
from ..core.section import Section
from ..core.timeline import Timelilne

from ..engine.manim_scene_adapter import ManimSceneAdapter

class VideoScene(manim.Scene):
    """
    Clase base de todos los vídeos.
    """

    def setup(self) -> None:
        self.timeline = Timelilne()
        self.director = Director()

    def section(self, narration: Narration) -> Section:
        section = Section(narration=narration)
        self.timeline.add_section(section)
        return section

    def renderizar(self):
        adapter = ManimSceneAdapter(self)
        self.director.render(
            self.timeline,
            adapter,
        )