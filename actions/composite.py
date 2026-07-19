#mathfilm/actions/composite.py

"""
Clase base para composiciones de acciones gráficas.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class CompositeAction(ManimAction):
    """
    Base común para acciones que contienen otras acciones.

    Las acciones internas no poseen intervalo independiente
    dentro de la sección. La composición exterior controla su
    inicio y su final.
    """

    actions: tuple[ManimAction,...]

    def __post_init__(self) -> None:
        """
        Valida el intervalo exterior y las acciones internas.
        """

        super().__post_init__()

        if not self.actions:
            raise ValueError(
                f"{type(self).__name__} necesita al menos "
                "una acción interna."
            )

        for index, action in enumerate(self.actions):
            self._validate_child_action(
                action=action,
                index=index,
            )

    def _validate_child_action(self, *, action: ManimAction, index: int):
        """
        Valida una acción contenida por la composición
        """

        if not isinstance(action, ManimAction):
            raise TypeError(
                f"{type(self).__name__}.actions [{index}] "
                "debe ser una instancia de ManimAction. "
                f"Se recibió {type(action).__name__}."
            )

        start = float(action.start)
        end = float(action.end)

        if start != 0.0 or end != 1.0:
            raise ValueError(
                f"{type(self).__name__}.actions[{index}] "
                "no debe definir un intervalo temporal propio. "
                "Las acciones internas deben conservar "
                "start=0.0 y end=1.0. "
                f"Se recibió [{start}, {end}]."
            )

    def build_animations(self) -> tuple[manim.Animation, ...]:
        """
        Construye todas las animaciones internas.
        """

        return tuple(
            action.build_animation()
            for action in self.actions
        )
        