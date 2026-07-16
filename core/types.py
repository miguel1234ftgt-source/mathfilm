"""
mathfilm.core.types
===================

Tipos básicos utilizados por todo el proyecto.

No contienen lógica.
Únicamente mejoran la legibilidad del código y ayudan
al análisis estático mediante mypy.

Todos los tipos aquí definidos representan conceptos
del dominio de MathFilm.
"""

from __future__ import annotations

from typing import NewType

#---------------------------------------------------
# Tiempo
#---------------------------------------------------

Seconds = NewType("Seconds", float)

Progress = NewType("Progress", float)

#---------------------------------------------------
# Narración
#---------------------------------------------------

WordsPerMinute = NewType(
    "WordsPerMinute",
    int,
)

#---------------------------------------------------
# Identificadores
#---------------------------------------------------

Identifier = NewType(
    "Identifier",
    str,
)