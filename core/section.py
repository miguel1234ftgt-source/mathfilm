#mathfilm/core/section.py
"""
Representación de una sección narrativa de MathFilm

Una sección agrupa:

- un fragmento de narración;
- las acciones visuales que ocurren durante ese fragmento.
"""

from __future__ import annotations
from dataclasses import dataclass, field

from .action import Action
from .narration import Narration
from .types import Seconds

@dataclass(
    slots=True,
    kw_only=True
)
class Section:
    """
    Unidad narrativa básica de un vídeo.

    Parameters
    ----------
    narration
        Fragmento del guión asociado a la sección.

    actions
        Acciones visuales de la sección.
    """
    narration: Narration
    actions: list[Action] = field(default_factory=list)

    @property
    def duration(self) -> Seconds:
        """
        Duración total de la sección
        """

        return self.narration.estimated_duration
    
    @property
    def ordered_actions(self) -> tuple[Action, ...]:
        """
        Devuelve las acciones ordenadas por su inicio.

        Se devuelve una tupla para evitar que el consumidor
        modifique accidentalmente la lista original.
        """

        return tuple(
            sorted(
                self.actions,
                key=lambda action: float(action.start)
            )
        )


    def add_action(
            self,
            action: Action,
    ) -> Action:
        """
        Añade una acción y devuelve la propia acción.

        Devolverla permite, cuando resulte conveniente, guardar
        la referencia durante la construcción de una escena.

        Parameters
        ----------
        action
            Acción que se añadirá.

        Returns
        -------
        Action
            La misma instancia añadida.
        """

        self.actions.append(action)
        self.validate_schedule()

        return action

    def validate_schedule(self) -> None:
        """
        Valida la planificación temporal de la sección

        En la versión 0.3 las acciones deben ser secuenciales.
        Dos acciones no pueden ocupar simultáneamente el mismo intervalo temporal.

        Raises
        ------
        ValueError
            Si dos acciones se solapan.
        """

        actions = self.ordered_actions
        
        for previous, current in zip(actions, actions[1:], strict=False):
            previous_end = float(previous.end)
            current_start = float(current.start)

            if current_start < previous_end:
                raise ValueError(
                    "La acciones de una sección no pueden "
                    "Solaparse en MathFilm v0.3. "
                    f"La acción {type(previous).__name__} termina "
                    f"en {previous_end}, pero "
                    f"{type(current).__name__} comienza en "
                    f"{current_start}."
                )