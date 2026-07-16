"""
Clase base para todas las acciones.

Las acciones representan eventos que ocurren
duranta una sección

Todavía no se conoce Manim.
"""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from ..core.types import Progress

@dataclass(
    slots=True,
    kw_only=True
)
class Action(ABC):
    """
    Acción abstracta

    Parameters
    ----------
    start
        Inicio relativo dentro de la narración

        Debe estar entre 0 y 1.

    end
        Fin relativo
    """
    start: Progress = Progress(0.0)
    end: Progress = Progress(1.0)