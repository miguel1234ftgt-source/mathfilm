# mathfilm/actions/set_color.py

"""
Acción para cambiar el color de un objeto.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.target import TargetAction


@dataclass(slots=True, kw_only=True)
class SetColor(TargetAction):
    """
    Cambia el color de un objeto.

    Parameters
    ----------
    mobject
        Objeto cuyo color será modificado.

    color
        Color final compatible con Manim.
    """

    color: manim.ManimColor

    def configure_target(
        self,
        target: manim.Mobject,
    ) -> None:
        """
        Cambia el color del objetivo.
        """

        target.set_color(self.color)