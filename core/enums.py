"""
Enumeraciones comunes del proyecto.
"""

from enum import Enum


class Track(Enum):
    """
    Pistas disponibles dentro de la línea temporal.

    Actualmente solamente existe la pista de narración.

    En futuras versiones se añadirán:

    - Cámara
    - Audio
    - Subtítulos
    """

    NARRATION = "narration"

    ANIMATION = "animation"