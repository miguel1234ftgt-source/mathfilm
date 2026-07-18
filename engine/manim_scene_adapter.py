#mathfilm/engine/manim_scene_adapter.py
"""
Adaptador concreto entre MathFilm y Manim Community

Este es uno de los pocos módulos de infraestructura que importa
directamente la biblioteca manim.
"""

from __future__ import annotations
from typing import Any

import manim

class ManimSceneAdapter:
    """
    Envuelve una instancia de ``manim.Scene``.

    Parameters
    ----------
    scene
        Escena real soobre la que se ejecutarán las operaciones.
    """

    def __init__(self, scene: manim.Scene) -> None:
        self._scene = scene

    def play(self, *animations: Any, run_time: float | None = None) -> None:
        """
        Reproduce animaciones mediante ``manim.Scene.play``.
        """

        if run_time is None:
            self._scene.play(*animations)
            return

        self._scene.play(
            *animations,
            run_time=run_time
        )

    def wait(self, seconds: float) -> None:
        """
        Introduce una espera en la escena.
        """
        self._scene.wait(seconds)

    def add(self, *objects) -> None:
        """
        Añade objetos sin animación.
        """
        self._scene.add(*objects)

    def remove(self, *objects) -> None:
        """
        Elimina objetos sin animación.
        """
        self._scene.remove(*objects)