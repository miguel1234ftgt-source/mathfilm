#mathfilm/actions/move_to.py

"""
Acción para mover un objeto hacia una posición determinada.
"""

from __future__ import annotations
from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

Position = tuple[float, float, float]


@dataclass(slots=True, kw_only=True)
class MoveTo(ManimAction):
    """
    Mueve un objeto hacia una posición absoluta.

    Parameters
    ----------
    mobject
        Objeto que será desplazado.

    position
        Coordenadas finales ``(x, y, z)``.
    """

    mobject: manim.Mobject
    position: Position

    def build_animation(self) -> manim.Animation:
        """
        Construye la animación de desplazamiento.
        """

        self.mobject.generate_target()

        if self.mobject.target is None:
            raise RuntimeError(
                "Manim no generó un objeto objetivo para MoveTo."
            )

        self.mobject.target.move_to(self.position)

        return manim.MoveToTarget(self.mobject)