#mathfilm/core/timeline.py
"""
Línea temporal principal de MathFilm.

La línea temporal conserva el orden narrativo de las sección.
La planificación interna de cada sección se delega en Section.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from mathfilm.core.section import Section

@dataclass(slots=True)
class Timeline:
    """
    Colección ordenada de secciones narrativas.
    """

    sections: list[Section] = field(default_factory=list)

    def add_section(self, section: Section) -> Section:
        """
        Añade una sección al final de la línea temporal.

        Parameters
        ----------
        section
            Sección que añadirá.
        
        Returns
        -------
        Section
            La misma instancia añadida.

        Raises
        ------
        ValueError
            Si ya existe una sección con el mismo identificador.
        """

        new_identifier = section.narration.identifier

        if any(
            existing.narration.identifier == new_identifier
            for existing in self.sections
        ):
            raise ValueError(
                "Ya existe una sección con el identificador "
                f"{new_identifier}."
            )
        
        self.sections.append(section)
        return section

    def clear(self) -> None:
        """
        Elimina todas las secciones de la línea temporal.
        """

        self.sections.clear()

    def __len__(self):
        """
        Devuelve el número de secciones.
        """
        
        return len(self.sections)