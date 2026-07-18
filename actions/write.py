#mathfilm/actions/write.py

"""
Acción para escribir progresivamente un objeto de Manim.

Se utiliza principalmente con texto, fórmulas y otros objetos
cuyos trazos puedan aparecer de manera progresiva.
"""

from __future__ import annotations
from dataclasses import dataclass

import manim

from mathfilm.core.action import Action
from mathfilm.core.types import Seconds
from mathfilm.engine.scene_adapter import SceneAdapter

@dataclass(slots=True, kw_only=True)
class Write(Action):
    """
    Escribe progresivamente un objeto mediante ``manim.Write``.

    Parameters
    ----------
    mobject
        Objeto de Manim que será escrito.

    end
        Final relativo de la acción dentro de la sección.
    """

    mobject: manim.VMobject
    

    def execute(self, scene: SceneAdapter, duration: Seconds) -> None:
        """
        Ejecuta la animación de escritura.
        """

        animation = manim.Write(
            self.mobject,
        )

        scene.play(
            animation,
            run_time=float(duration),
            )