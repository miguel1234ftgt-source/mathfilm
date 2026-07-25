#mathfilm/actions/move_to.py

"""
Acción para mover un objeto hacia una posición determinada.
"""

from __future__ import annotations
from dataclasses import dataclass

import manim

from mathfilm.actions.target import TargetAction
from mathfilm.actions.types import Point3D



@dataclass(slots=True, kw_only=True)
class MoveTo(TargetAction):
    """
    Mueve un objeto hacia una posición absoluta.

    Parameters
    ----------
    mobject
        Objeto que será desplazado.

    position
        Coordenadas finales ``(x, y, z)``.
    """

    position: Point3D 

    def configure_target(self, target: manim.Mobject) -> None:
        target.move_to(self.position) # type: ignore