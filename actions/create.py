#mathfilm/actions/create.py

"""
Acción para dibujar progresivamente un objeto.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class Create(ManimAction):
    """
    Dibuja progresivamente un objeto mediante ``manim.Create``
    
    Parameters
    ----------
    mobject
        Objeto geométrico que será dibujado.
    """

    mobject: manim.VMobject

    def build_animation(self) -> manim.Animation:
        """
        Construye la animación de creación.
        """
        
        return manim.Create(self.mobject)
