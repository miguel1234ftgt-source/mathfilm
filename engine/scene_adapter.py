"""
Contrato mínimo que debe cumplir
cualquier motor gráfico
"""

from __future__ import annotations
from typing import Protocol

class SceneAdapter(Protocol):
    def play (self, *animations) -> None:
        ...

    def wait(
            self,
            seconds: float
    ) -> None:
        ...

    def add(self, *objects) -> None:
        ...

    def remove(self, *objects) -> None:
        ...