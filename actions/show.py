"""
Muestra un componente
"""

from __future__ import annotations
from dataclasses import dataclass
import manim

from core.action import Action
from engine.scene_adapter import SceneAdapter

@dataclass(slots=True)
class Show(Action):

    mobject: manim.Mobject

    def execute(self, scene: SceneAdapter) -> None:
        scene.play(
            manim.FadeIn(self.mobject)
        )