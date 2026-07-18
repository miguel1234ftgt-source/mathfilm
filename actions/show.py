#mathfilm/actions/show.py
"""
Acción para mostrar gradualmente un objeto de Manim.
"""

from __future__ import annotations
from dataclasses import dataclass
import manim

from core.action import Action
from core.types import Seconds
from engine.scene_adapter import SceneAdapter

@dataclass(slots=True, kw_only=True)
class Show(Action):
    """
    Muestra un objeto mediante una transición FadeIn.

    Parameters
    ----------
    mobject
        Objeto de Manim que aparecerá en pantalla.

    start
        Inicio relativo de la animación.

    end
        Final relativo de la animación
    """

    mobject: manim.Mobject

    def execute(self, scene: SceneAdapter, duration: Seconds) -> None:
        """
        Ejecuta la transición de entrada.
        """
        
        animation = manim.FadeIn(
            self.mobject,
            run_time=float(duration)
        )

        scene.play(animation)