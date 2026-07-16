"""
Adaptador hacia manim.Scene.
"""

from __future__ import annotations
import manim

class ManimSceneAdapter:
    """
    Adaptador sencillo sobre manim.Scene
    """

    def __init__(self, scene: manim.Scene) -> None:
        self.scene = scene

    def play(self, *animations) -> None:
        self.scene.play(*animations)

    def wait(self, seconds: float) -> None:
        self.scene.wait(seconds)

    def add(self, *objects) -> None:
        self.scene.add(*objects)

    def remove(self, *objects) -> None:
        self.scene.remove(*objects)