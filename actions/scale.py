#mathfilm/actions/scale.py

"""
Acción para cambiar el tamaño de un objeto.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.target import TargetAction
from mathfilm.actions.types import Point3D

@dataclass(slots=True, kw_only=True)
class Scale(TargetAction):
    """
    Escala un objeto respecto a su centro o a un punto dado.

    Parameters
    ----------
    mobject
        Objeto que será escalado
    factor
        Factor multiplicativo de escala.

        Un valor mayor que ``1`` aumenta el tamaño.

        Un valor entre ``0.0`` y ``1.0`` lo reduce.
    about_point
        Punto opcional respecto al cual se realiza la escala.
        Cuando es ``None``, Manim utiliza el centro del objeto.
    """

    factor: float
    about_point: Point3D | None = None

    def __post_init__(self) -> None:
        """
        Valida la acción y el factor de escala
        """

        super().__post_init__()

        if self.factor <= 0.0:
            raise ValueError(
                "Scale.factor debe ser estrictamente positivo. "
                f"Valor recibido: {self.factor}."
            )

    def configure_target(self, target: manim.Mobject) -> None:
        """
        Escala el objetivo.
        """
        
        if self.about_point is None:
            target.scale(self.factor)
            return
        
        target.scale(self.factor, about_point=self.about_point)