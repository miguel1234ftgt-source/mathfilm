"""
mathfilm.core.director

Coordina la ejecución del vídeo.

Actualmente únicamente recorre las secciones en orden.
"""

from __future__ import annotations
from ..core.timeline import Timelilne
from ..engine.scene_adapter import SceneAdapter


class Director:
    """
    Director del vídeo.
    """

    def render(
            self,
            timeline: Timelilne,
            scene: SceneAdapter,
    ) -> None:
        for section in timeline.sections:
            scene.wait(
                section.narration.estimated_duration
            )
            for action in section.actions:
                action.execute(scene)