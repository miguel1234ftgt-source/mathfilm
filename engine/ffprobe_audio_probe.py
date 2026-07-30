#mathfilm/engine/ffprobe_audio_probe.py

"""
Obtención de duraciones mediante ffprobe.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from mathfilm.core.types import Seconds
from mathfilm.engine.audio_probe import AudioProbe

class AudioProbeError(RuntimeError):
    """
    Error al inspeccionar un archivo de audio.
    """


class FFprobeAudioProbe(AudioProbe):
    """
    Obtiene la duración de archivos multimedia mediante ffprobe
    """

    def duration(self, path: Path) -> Seconds:
        """
        Devuelve la duración del archivo indicado.
        """

        resolved_path = path.expanduser().resolve()

        if not resolved_path.is_file():
            raise FileNotFoundError(
                "No se encontró el archivo de audio: "
                f"{resolved_path}"
            )

        command = [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(resolved_path)
        ]

        try:
            result = subprocess.run(
                command,
                check=True,
                capture_output=True,
                text=True
            )
        except FileNotFoundError as error:
            raise AudioProbeError(
                "No se encontró ffprobe. Comprueba que FFmpeg "
                "Esté instalado y disponible en PATH."
            ) from error 
        except subprocess.CalledProcessError as error:
            message = error.stderr.strip()

            raise AudioProbeError(
                "ffprobe no pudo inspeccionar el archivo "
                f"{resolved_path}: {message}"
            ) from error
        
        try:
            payload: dict[str, Any] = json.loads(result.stdout)
            raw_duration = payload["format"]["duration"]
            duration = float(raw_duration)
        except (
            KeyError,
            TypeError,
            ValueError,
            json.JSONDecodeError
        ) as error:
            raise AudioProbeError(
                "ffprobe no devolvió una duración válida para "
                f"{resolved_path}."
            ) from error

        if duration <= 0.0:
            raise AudioProbeError(
                "El archivo de audio tiene una duración inválida: "
                f"{duration}."
            )
        return Seconds(duration)