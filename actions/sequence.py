#mathfilm/actions/sequence.py

"""
Acción compuesta para ejecutar animaciones consecutivamente.

Todas las acciones internas se distribuyen dentro del intervalo
temporal asignado a Sequence.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.composite import CompositeAction

@dataclass(slots=True, kw_only=True)
class Sequence(CompositeAction):
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

        
    def build_animation(self) -> manim.Animation:
        """
        Construye la sucesión de animaciones.
        """

        return manim.Succession(*self.build_animations())