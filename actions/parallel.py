# mathfilm/actions/parallel.py

"""
Acción compuesta para reproducir varias acciones simultáneamente.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction


@dataclass(slots=True, kw_only=True)
class Parallel(ManimAction):
    """
    Ejecuta varias acciones gráficas simultáneamente.

    Parameters
    ----------
    actions
        Acciones que se reproducirán al mismo tiempo
    start
        Inicio relativo de la acción compuesta.
    end
        Final relativo de la acción compuesta.

    Notes
    -----
    Los intervalos temporales de las acciones internas no se
    utilizan. Todas ocupan el intervalo completo de ``Parallel``.

    Para evitar ambigüedad, las acciones internas deben conservar
    sus valores predeterminados:

    - ``start = 0.0``
    - ``end = 1.0``
    """

    actions: tuple[ManimAction, ...]

    def __post_init__(self) -> None:
        """
        Valida la acción compuesta y sus acciones internas.
        """

        super(Parallel, self).__post_init__()

        if not self.actions:
            raise ValueError("Parallel necesita al menos una acción.")

        for index, action in enumerate(self.actions):
            if float(action.start) != 0.0 or float(action.end) != 1.0:
                raise ValueError(
                    "Las acciones internas de Parallel no deben "
                    "definir start ni end. "
                    f"Intervalo inválido en actions[{index}]."
                )

    def build_animation(self) -> manim.Animation:
        """
        Agrupa las animaciones para ejecutarlas simultáneamente.
        """

        animations = [action.build_animation() for action in self.actions]

        return manim.AnimationGroup(*animations, lag_ratio=0.0)
