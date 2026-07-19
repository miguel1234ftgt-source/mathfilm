# mathfilm/actions/hide.py

"""
Acción para ocultar gradualmente un objeto de Manim.
"""

from __future__ import annotations
from dataclasses import dataclass
import manim

from mathfilm.actions.base import ManimAction


@dataclass(slots=True, kw_only=True)
class Hide(ManimAction):
    """
    Oculta un objeto mediante ``manim.FadeOut``.

    Parameters
    ----------
    mobject
        Objeto que desaparecerá
    """

    mobject: manim.Mobject

    def build_animation(self) -> manim.Animation:
        """
        Construye la animación de salida.
        """

        return manim.FadeOut(self.mobject)