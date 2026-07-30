"""
Representación de un fragmento del guión.
"""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

from mathfilm.core.types import Identifier, Seconds, WordsPerMinute

DEFAULT_WPM = WordsPerMinute(145)


@dataclass(slots=True, kw_only=True)
class Narration:
    """
    Narración asociada con una sección.

    Parameters
    ----------
    identifier
        Identificador único de la narración.

    text
        Texto de la narración.

    duration
        Duración activa declarada manualmente.

        Se utiliza cuando no existe un archivo de audio. Si también
        se proporciona audio, la duración real del archivo tiene
        prioridad.

    audio
        Archivo de audio opcional.

    padding_before
        Tiempo añadido antes del comienzo del audio y de las
        acciones.

    padding_after
        Tiempo añadido después del final del audio y de las
        acciones.

    Notes
    -----
    Los paddings son supraaccionales. No forman parte del intervalo
    sobre el que se interpretan los valores Progress de las
    acciones.
    """

    identifier: Identifier
    text: str

    duration: Seconds | None = None
    audio: Path | str | None = None

    padding_before: Seconds = Seconds(0.0)
    padding_after: Seconds = Seconds(0.0)

    def __post_init__(self) -> None:
        """
        Normaliza y valida los datos declarativos
        """
        if not self.text.strip():
            raise ValueError(
                "Narration.text no puede estar vacío."
            )

        if self.duration is None and self.audio is None:
            raise ValueError(
                "Narration necesita un archivo de audio o una "
                "duración explícita."
            )

        if self.duration is not None:
            if float(self.duration) <= 0.0:
                raise ValueError(
                    "Narration.duration debe ser positiva."
                )
        if float(self.padding_before) < 0.0:
            raise ValueError(
                "Narration.padding_before no puede ser negativo."
            )

        if float(self.padding_after) < 0.0:
            raise ValueError(
                "Narration.padding_after no puede ser negativo."
            )

        if self.audio is not None:
            self.audio = Path(self.audio)

    @property
    def word_count(self) -> int:
        """
        Número de palabras del texto
        """

        return len(self.text.split())

    @property
    def estimated_duration(self) -> Seconds:
        """
        Duración estimada de la narración
        """
        if self.duration is not None:
            return self.duration

        minutes = self.word_count / DEFAULT_WPM
        return Seconds(minutes * 60)
