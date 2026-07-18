# mathfilm/actions/hide.py

"""
Acción para ocultar gradualmente un objeto de Manim.
"""

from __future__ import annotations
from dataclasses import dataclass
import manim

from mathfilm.core.action import Action
from mathfilm.core.types import Seconds
from mathfilm.engine.scene_adapter import SceneAdapter


@dataclass(slots=True, kw_only=True)
class Hide(Action):
    """
    Oculta un objeto mediante ``manim.FadeOut``.

    Parameters
    ----------
    mobject
        Objeto que desaparecerá

    start
        Inicio relativo de la acción

    end
        Final relativo
    """

    mobject: manim.Mobject

    def execute(self, scene: SceneAdapter, duration: Seconds) -> None:
        """
        Ejecuta la transición de salida.
        """

        animation = manim.FadeOut(
            self.mobject,
        )

        scene.play(animation, run_time=float(duration))
