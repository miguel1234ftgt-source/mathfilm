# mathfilm/core/section_timing.py

"""
Temporización resuelta de una sección.
"""

from __future__ import annotations

from dataclasses import dataclass

from mathfilm.core.types import Progress, Seconds


@dataclass(frozen=True, slots=True)
class SectionTiming:
    """
    Distribución temporal efectiva de una acción.

    La duración activa es el intervalo sobre el que operan las
    acciones. Los padings se encuentran dura de dicho intervalo
    """

    active_duration: Seconds
    padding_before: Seconds = Seconds(0.0)
    padding_after: Seconds = Seconds(0.0)

    def __post_init__(self) -> None:
        if float(self.active_duration) <= 0.0:
            raise ValueError("SectionTiming.active_duration debe ser positiva.")

        if float(self.padding_before) < 0.0:
            raise ValueError("SectionTimig.padding_before no puede ser " "negativo.")

        if float(self.padding_after) < 0.0:
            raise ValueError("SectionTimig.padding_after no puede ser " "negativo.")

    @property
    def total_duration(self) -> Seconds:
        """
        Duración total ocupada por la sección en el vídeo.
        """

        return Seconds(
            float(self.padding_before)
            + float(self.active_duration)
            + float(self.padding_after)
        )


    def active_seconds(self, progress: Progress) -> Seconds:
        """
        Convierte un progreso en segundos de la ventada activa.

        No incorpora padding_before.
        """

        return Seconds(float(progress) * float(self.active_duration))
    
    def absolute_seconds(self, progress: Progress) -> Seconds:
        """
        Convierte un progreso en segundos desde el inicio completo
        de la sección.

        Esta operación sí incorpora padding_before.
        """

        return Seconds(float(self.padding_before) + float(self.active_seconds(progress)))

    