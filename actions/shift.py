#mathfilm/actions/shift.py

"""
Acción para desplazar relativamente un objeto.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.target import TargetAction
from mathfilm.actions.types import Vector3D


@dataclass(slots=True, kw_only=True)
class Shift(TargetAction):
    """
    Desplaza un objeto mediante un vector.

    Parameters
    ----------
    mobject
        Objeto que será desplazado.
    vector
        Vector de desplazamiento ``(x, y, z)``.

    Examples
    --------
    Desplazar dos unidades hacia la izquierda:
    ``vector=(-2.0, 0.0, 0.0)``
    """

    vector: Vector3D 


    def configure_target(self, target: manim.Mobject) -> None:
        """
        Desplaza el objetivo por el vector indicado.
        """

        target.shift(self.vector) # type: ignore