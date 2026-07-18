# mathfilm/core/action.py
"""
Clase base para todas las acciones de MathFilm.

Una acción prepresenta un acontecimiento visual situado dentro
del intervalo temportal de una sección.

El núcleo no importa Manim. Las acciones concretas serán las
responsables de traducir esta descripción al motor gráfico
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .types import Progress, Seconds

if TYPE_CHECKING:
    from ..engine.scene_adapter import SceneAdapter

@dataclass(
    slots=True,
    kw_only=True
)
class Action(ABC):
    """
    Clase base de todas las acciones.

    Parameters
    ----------
    start
        Posición relativa en la que comienza la acción.

        Debe satisfacer:

            0.0 <= start < end <= 1.0
    
    end
        Posición relativa en la que termina la acción

    Notes
    -----
    Los valores son proporciones de la duración total de la
    narración asociada a la sección.

    Por ejemplo, si una narración dura 10 segundos:

    - start=0.2 equivale al segundos 2.
    - end=0.5 equivale al segundos 5.
    - la acción dura 3 segundos
    """
    start: Progress = Progress(0.0)
    end: Progress = Progress(1.0)

    def __post_init__(self) -> None:
        """
        Comprueba que el intervalo relativo sea válido.

        La validación se realiza al construir cualquier acción,
        evitando que un erro temporal llegue hasta el render.
        """

        start = float(self.start)
        end = float(self.end)

        if not 0.0 <= start <= 1.0:
            raise ValueError(
                "Action.start debe estar entre 0.0 y 1.0;",
                f"se recibió {start}"
            )

        if not 0.0 <= end <= 1.0:
            raise ValueError(
                "Action.end debe estar entre 0.0 y 1.0;"
                f"se recibió {end}"
            )
        
        if start >= end:
            raise ValueError(
                "Action.start debe ser estrictamente menor que "
                f"Action.end; se recibió start={start}, end={end}"
            )
        
    @property
    def relative_duration(self) -> Progress:
        """
        Devuelve la longitud relativa del intervalo.
        """

        return Progress(float(self.end) - float(self.start))
    
    def duration_for(self, section_duration: Seconds) -> Seconds:
        """
        Convierte la duración relativa a segundos.

        Parameters
        ----------
        section_duration
            Duración total de la sección

        Returns
        -------
        Seconds
            Duración real asignada a la acción
        """

        duration = (float(self.relative_duration) * float(section_duration))

        return Seconds(duration)

    @abstractmethod
    def execute(
        self,
        scene: SceneAdapter,
        duration: Seconds,
    ) -> None:
        """
        Ejecuta la acción mediante un adaptador gráfico.

        Paramters
        ---------
        scene
            Adaptador del motor gráfico.

        duration
            Duración real de la acción en segundos.
        """