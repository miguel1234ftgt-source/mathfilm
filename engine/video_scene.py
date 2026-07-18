#mathfilm/engine/video_scene.py
"""
Escena base para MathFilm
"""


from __future__ import annotations
import manim


from mathfilm.core.director import Director
from mathfilm.core.narration import Narration
from mathfilm.core.section import Section
from mathfilm.core.timeline import Timeline
from mathfilm.engine.manim_scene_adapter import (
    ManimSceneAdapter,
)


class VideoScene(manim.Scene):
    """
    Clase base de las escenas creadas con MathFilm.

    Las escenas concretas deben implementar ``construct()``,
    igual que una escena normal de Manim
    """

    def setup(self) -> None:
        """
        Inicializa la infraestructura de MathFilm.

        Manim ejecuta este método antes de ``construct()``.
        """

        super().setup()

        self.timeline = Timeline()
        self.director = Director()


    def section(self, narration: Narration) -> Section:
        """
        Crea y registra una sección narrativa.

        Parameters
        ----------
        narration
            Narración asociada a la nueva sección

        Returns
        -------
        Section
            Sección recien creada.
        """

        section = Section(narration=narration)
        self.timeline.add_section(section)
        return section

    def render_timeline(self) -> None:
        """
        Ejecuta la línea termporal registrada.

        Este método debe llamarse al final de ``construct()``.
        """
        adapter = ManimSceneAdapter(self)
        self.director.render(
            timeline=self.timeline,
            scene=adapter,
        )