#mathfilm/engine/audio_probe.py

"""
Abstracciones para obtener metadatos de archivos de audio.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from mathfilm.core.types import Seconds


class AudioProbe(ABC):
    """
    Servicio capaz de obtener metadatos de un archivo de audio.
    """

    @abstractmethod
    def duration(self, path: Path) -> Seconds:
        """
        Devuelve la duración efectiva del archivo
        """