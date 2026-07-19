#mathfilm/actions/write.py

"""
Acción para escribir progresivamente un objeto de Manim.

Se utiliza principalmente con texto, fórmulas y otros objetos
cuyos trazos puedan aparecer de manera progresiva.
"""

from __future__ import annotations
from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class Write(ManimAction):
    """
    Escribe progresivamente un objeto.

    Es especialmente apropiada para textos y expresiones
    matemáticas.
    """

    mobject: manim.VMobject
    

    def build_animation(self) -> manim.Animation:
        """
        Construye la animación de escritura.
        """

        return manim.Write(self.mobject)