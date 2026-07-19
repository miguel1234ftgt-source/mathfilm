#mathfilm/actions/stagger.py

"""
Acción compuesta para ejecutar animaciones de manera escalonada.

Cada animación empieza después de que ha transcurrido una fracción
del desarrollo de la animación anterior.
"""

from __future__ import annotations

from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction


@dataclass(slots=True, kw_only=True)
class Stagger(ManimAction):
    """
    Ejecuta acciones con un retraso relativo entre sus inicios.

    Parameters
    ----------
    actions
        Acciones que serán ejecutadas de forma escalonada.
    lag_ratio
        Fracción del desarrollo de una animación que debe
        transcurrir antes de iniciar la siguiente.

        Un valor de ``0.0`` equivale a ejecución simultánea.

        Un valor de ``1.0`` hace que cada animación comience
        después de terminar la anterior.

    Notes
    -----
    Las acciones internas debe conservar sus intervalos
    predeterminados. El intervalo de ``Stagger`` controla el
    tiempo total de la composición.
    """

    actions: tuple[ManimAction, ...]
    lag_ratio: float = 0.1

    def __post_init__(self) -> None:
        """
        Valida las acciones y el retraso relativo.
        """

        super(Stagger, self).__post_init__()

        if not self.actions:
            raise ValueError(
                "Stagger necesita al menso una acción."
            )
        
        if not 0.0 <= self.lag_ratio <= 1.0:
            raise ValueError(
                "lag_ratio debe econtrarse entre 0.0 y 1.0."
            )
        
        for index, action in enumerate(self.actions):
            if(
                float(action.start) != 0.0
                or float(action.end) != 1.0
            ):
                raise ValueError(
                    "Las acciones internas de Stagger no deben "
                    "definir start ni end. "
                    f"Intervalo inválido en actions[{index}]."
                )
    
    def build_animation(self) -> manim.Animation:
        """
        Construye la composición escalonada.
        """

        animations = tuple(
            action.build_animation()
            for action in self.actions
        )

        return manim.LaggedStart(
            *animations,
            lag_ratio=self.lag_ratio,
        )