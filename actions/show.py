#mathfilm/actions/show.py
"""
Acción para mostrar gradualmente un objeto de Manim.
"""

from __future__ import annotations
from dataclasses import dataclass
import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class Show(ManimAction):
    """
    Muestra un objeto mediante una transición FadeIn.

    Parameters
    ----------
    mobject
        Objeto de Manim que aparecerá en pantalla.
    """

    mobject: manim.Mobject

    def build_animation(self) -> manim.Animation:
        """
        Construye la animación de entrada.
        """

        return manim.FadeIn(self.mobject)