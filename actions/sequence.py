#mathfilm/actions/sequence.py

"""
Acción compuesta para ejecutar animaciones consecutivamente.

Todas las acciones internas se distribuyen dentro del intervalo
temporal asignado a Sequence.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class Sequence(ManimAction):
    """
    Ejecuta varias acciones gráficas una después de otra.

    Parameters
    ----------
    actions
        Acciones que serán ejecutadas consecutivamente.
    
    Notes
    -----
    Las acciones internas no controlan su propio intervalo
    temporal. Deben conservar:

    - ``start = 0.0``
    - ``end = 1.0``

    El intervalo exterior de ``Sequence`` determina la duración
    total de toda la composición.
    """

    actions: tuple[ManimAction, ...]

    def __post_init__(self) -> None:
        """
        Valida la acción compuesta.
        """

        super(Sequence, self).__post_init__()

        if not self.actions:
            raise ValueError(
                "Sequence necesita al menos una acción"
            )

        for index, action in enumerate(self.actions):
            if (
                float(action.start) != 0.0
                or float (action.end) != 1.0
            ):
                raise ValueError(
                    "Las acciones internas de Sequence no deben "
                    "definir start ni end. "
                    f"Intervalo inválido en actions[{index}]."
                )
        
    def build_animation(self) -> manim.Animation:
        """
        Construye la sucesión de animaciones.
        """

        animations = tuple(
            action.build_animation()
            for action in self.actions
        )

        return manim.Succession(
            *animations
        )