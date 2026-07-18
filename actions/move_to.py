#mathfilm/actions/move_to.py

"""
Acción para mover un objeto hacia una posición determinada.
"""

from __future__ import annotations
from dataclasses import dataclass

import manim

from mathfilm.core.action import Action
from mathfilm.core.types import Seconds
from mathfilm.engine.scene_adapter import SceneAdapter

Position = tuple[float, float, float]


@dataclass(slots=True, kw_only=True)
class MoveTo(Action):
    """
    Mueve un objeto hacia una posición absoluta.

    Parameters
    ----------
    mobject
        Objeto que será desplazado.

    position
        Coordenadas finales ``(x, y, z)``.

    start
        Inicio relativo de la acción
    
    end
        Final relativo de la acción

    Examples
    --------
    Mover un objeto tres unidades hacia la izquierda:

    ``position=(-3.0, 0.0, 0.0)``
    """

    mobject: manim.Mobject
    position: Position

    def execute(self, scene: SceneAdapter, duration: Seconds) -> None:
        """
        Ejecuta el desplazamiento.
        """

        animation = self.mobject.animate.move_to(
            self.position,
        )

        scene.play(
           animation,
           run_time=float(duration)
        )