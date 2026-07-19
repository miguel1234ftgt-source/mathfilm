#mathfilm/actions/transform.py

"""
Acción para transformar un objeto en otro.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class Transform(ManimAction):
    """
    Reemplaza un objeto por otro mediante una transformación

    Parameters
    ----------
    source
        Objeto presente incialmente en la escena.
    target
        Objeto que reemplazara al objeto incial.
    """

    source: manim.Mobject | manim.VMobject
    target: manim.Mobject | manim.VMobject

    def build_animation(self) -> manim.Animation:
        """
        Construye la transformación.
        """

        return manim.ReplacementTransform(
            self.source,
            self.target,
        )