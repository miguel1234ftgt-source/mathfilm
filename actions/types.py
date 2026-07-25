#mathfilm/actions/types.py

"""
Tipos utilizados por las acciones gráficas de MathFilm.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeAlias

from manim.typing import Vector3DLike

Point3D: TypeAlias = Vector3DLike

Vector3D: TypeAlias = Point3D