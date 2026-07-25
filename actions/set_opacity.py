# mathfilm/actions/set_opacity.py

"""
Acción para modificar la opacidad de un objeto.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.target import TargetAction


@dataclass(slots=True, kw_only=True)
class SetOpacity(TargetAction):
    """
    Modifica la opacidad general de un objeto.

    Parameters
    ----------
    opacity
        Valor comprendido entre ``0.0`` y ``1.0``.
    """

    opacity: float

    def __post_init__(self) -> None:
        """
        Valida la acción y la opacidad.
        """

        super().__post_init__()

        if not 0.0 <= self.opacity <= 1.0:
            raise ValueError(
                "SetOpacity.opacity debe encontrarse entre "
                "0.0 y 1.0. "
                f"Valor recibido: {self.opacity}."
            )

    def configure_target(
        self,
        target: manim.Mobject,
    ) -> None:
        """
        Modifica la opacidad del objetivo.
        """

        target.set_opacity(self.opacity)