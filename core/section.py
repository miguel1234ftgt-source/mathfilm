"""
Representación de una sección del vídeo
"""

from __future__ import annotations
from dataclasses import dataclass, field
from ..core.action import Action
from ..core.narration import Narration

@dataclass(
    slots=True
)
class Section:
    """
    Unidad básica de vídeo.
    
    Una sección contiene

    - una narración
    - una colección de acciones
    """
    narration: Narration
    actions: list[Action] = field(default_factory=list)

    def add_action(
            self,
            action: Action,
    ) -> None:
        """
        Añade una acción a la sección
        """

        self.actions.append(action)