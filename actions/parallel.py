# mathfilm/actions/parallel.py

"""
Acción compuesta para reproducir varias acciones simultáneamente.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.composite import CompositeAction


@dataclass(slots=True, kw_only=True)
class Parallel(CompositeAction):
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


    def build_animation(self) -> manim.Animation:
        """
        Agrupa las animaciones para ejecutarlas simultáneamente.
        """

        return manim.AnimationGroup(*self.build_animations(), lag_ratio=0.0)
