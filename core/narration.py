"""
Representación de un fragmento del guión.
"""

from __future__ import annotations
from dataclasses import dataclass

from ..core.types import Identifier, Seconds, WordsPerMinute

DEFAULT_WPM = WordsPerMinute(145)

@dataclass(
    frozen=True,
    slots=True,
    kw_only=True
)
class Narration:
    """
    Fragmento del guión.

    Parameters
    ----------
    identifier
        Identificador único.

    text
        Texto narrado.

    duration
        Duración manual.

        Si es None se estima automáticamente
    """

    identifier: Identifier
    text: str
    duration: Seconds | None = None

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