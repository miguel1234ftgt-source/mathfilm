#mathfilm/engine/narration_resolver.py

"""
Resolución de archivos y duraciones de narraciones.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from pathlib import Path

from mathfilm.core.narration import Narration
from mathfilm.core.section_timing import SectionTiming
from mathfilm.core.types import Seconds
from mathfilm.engine.audio_probe import AudioProbe

class NarrationDurationWarning(UserWarning):
    """
    Advertencia por discrepancia entre duración declarada y real.
    """


@dataclass(slots=True)
class ResolvedNarration:
    """
    Narración preparada para su ejecución
    """

    timing: SectionTiming
    audio: Path | None


@dataclass(slots=True)
class NarrationResolver:
    """
    Resuelve la duración efectiva de una narración.
    """
    
    audio_probe: AudioProbe
    duration_tolerance: Seconds = Seconds(0.25)

    def resolve(self, narration: Narration) -> ResolvedNarration:
        """
        Resuelve el audio y la temporización de la narración.
        """

        audio_path: Path | None = None

        if narration.audio is not None:
            audio_path = Path(narration.audio).expanduser().resolve()

            active_duration = self.audio_probe.duration(audio_path)

            self._validate_declared_duration(
                narration=narration,
                actual_duration=active_duration
            )

        elif narration.duration is not None:
            active_duration = narration.duration

        else:
            raise RuntimeError("La narración no contiene una fuente de duración.")

        timing = SectionTiming(
            active_duration=active_duration,
            padding_before=narration.padding_before,
            padding_after=narration.padding_after
        )

        return ResolvedNarration(
            timing=timing,
            audio=audio_path
        )

    def _validate_declared_duration(self, *, narration: Narration, actual_duration: Seconds) -> None:
        """
        Advierte si la duración declarada difiere del audio.
        """

        if narration.duration is None:
            return

        difference = abs(float(narration.duration) - float(actual_duration))

        if difference <= float(self.duration_tolerance):
            return

        warnings.warn(
            f"La narración '{narration.identifier}' declaró "
            f"{float(narration.duration):.3f } segundos, pero "
            f"el audio dura {float(actual_duration):.3f}. "
            "Se utilizará la duración del audio. "
        )