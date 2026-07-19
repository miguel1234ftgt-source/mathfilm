#mathfilm/actions/base.py

"""
Clases base para acciones abstractas del núcleo con
animaciones concretas de Manim.
"""


from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass

import manim

from mathfilm.core.action import Action
from mathfilm.core.types import Seconds
from mathfilm.engine.scene_adapter import SceneAdapter


@dataclass(slots=True, kw_only=True)
class ManimAction(Action):
    """
    Clase base para acciones representables como una animación de Manim

    Las subclases únicamente debem implementar ``build_animation``.
    La lógica cómun de reproducción y duración se concentra aquí.
    """


    @abstractmethod
    def build_animation(self) -> manim.Animation:
        """
        Construye la animación de Manim.

        Returns
        -------
        manim.Animation
            Animación lista para ser producida.
        """

    def execute(self, scene: SceneAdapter, duration: Seconds) -> None:
        """
        Construye y reproduce la animación.

        Parameters
        ----------
        scene
            Adaptador gráfico utilizado para reproducirla.

        duration
            Duración total asignada por el director.
        """

        scene.play(
            self.build_animation(),
            run_time=float(duration),
        )