#mathfilm/actions/target.py

"""
Clase base para transformaciones mediante objetos objetivo.

Una TargetAction:

1. genera una copia objetivo del objeto.
2. modifica esa copia.
3. transforma el objeto original hacia el estado resultante.
"""

from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass

import manim

from mathfilm.actions.base import ManimAction

@dataclass(slots=True, kw_only=True)
class TargetAction(ManimAction):
    """
    Acción que transforma un objeto hacia un estado objetivo.

    Las sublclases implementan ``configure_target`` para describir
    únicamente la modificación que debe aplicarse al objetivo.
    """
    
    mobject: manim.Mobject

    @abstractmethod
    def configure_target(
        self,
        target: manim.Mobject
    ) -> None:
        """
        Modifica el objeto objetivo

        Parameters
        ---------- 
        target
            Copia del objetivo original que representa su estado
            final.
        """

    def build_animation(self) -> manim.Animation:
        """
        Construye la transformación hacia el estado objetivo
        """
        
        self.mobject.generate_target()

        target = self.mobject.target

        if target is None:
            raise RuntimeError(
                f"{type(self).__name__} no pudo generar "
                "el objeto objetivo."
            )

        self.configure_target(target)

        return manim.MoveToTarget(self.mobject)