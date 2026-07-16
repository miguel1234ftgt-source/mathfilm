"""
mathfilm.core.timeline

La línea temporal del vídeo.

En esta primera versión únicamente mantiene el orden
de las secciones.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from ..core.section import Section

@dataclass(slots=True)
class Timelilne:
    """
    Colección ordenada de secciones.
    """

    sections: list[Section] = field(default_factory=list)

    def add_section(self, section: Section) -> None:
        """
        Añade una sección al final de la línea temporal.
        """

        self.sections.append(section)