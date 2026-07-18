# mathfilm/actions/__init__.py

"""
Paquete de acciones de MathFilm.
"""

from mathfilm.actions.hide import Hide
from mathfilm.actions.move_to import MoveTo
from mathfilm.actions.show import Show
from mathfilm.actions.write import Write

__all__: list[str] = [
    "Hide",
    "MoveTo",
    "Show",
    "Write",
]