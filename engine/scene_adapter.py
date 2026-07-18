#mathfilm/engine/scene_adapter.py
"""
Contrato mínimo entre MathFilm y un motor gráfico

Este módulo no importa Manim. El protocolo expresa únicamente
las operaciones que MathFilm necesita realizar sobre una escena.
"""

from __future__ import annotations

from typing import Any, Protocol

class SceneAdapter(Protocol):
    """
    Interfaz mínima que debe implementar un adaptador gráfico.
    """

    def play (self, *animations: Any, run_time:float | None = None) -> None:
        """
        Reproduce una o varias animaciones

        Parameters
        ----------
        animations
            Animaciones que serán ejecutadas.
        
        run_time
            Duración opcional de la reproducción.
        """
        ...

    def wait(
            self,
            seconds: float
    ) -> None:
        """
        Mantiene la escena sin cambios durante cierto tiempo.
        """
        ...

    def add(self, *objects: Any) -> None:
        """
        Añade objetos inmediatamente a la escena.
        """
        ...

    def remove(self, *objects: Any) -> None:
        """
        Elimina objetos inmediatamente de la escena.
        """
        ...