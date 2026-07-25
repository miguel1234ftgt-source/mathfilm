# mathfilm/actions/rotate.py

"""
Acción para rotar un objeto.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.target import TargetAction
from mathfilm.actions.types import Point3D, Vector3D


@dataclass(slots=True, kw_only=True)
class Rotate(TargetAction):
    """
    Rota un objeto un ángulo determinado.

    Parameters
    ----------
    mobject
        Objeto que será rotado.

    angle
        Ángulo de rotación expresado en radianes.

    axis
        Eje de rotación.

    about_point
        Centro de rotación opcional.
    """

    angle: float
    axis: Vector3D 
    about_point: Point3D | None = None

    def configure_target(
        self,
        target: manim.Mobject,
    ) -> None:
        """
        Rota el objeto objetivo.
        """

        target.rotate(
            angle=self.angle,
            axis=self.axis, # type: ignore
            about_point=self.about_point, # type: ignore
        )