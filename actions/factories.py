# mathfilm/actions/factories.py

"""
Funciones auxiliares para construir acciones compuestas.

Estas funciones reducen el código repetitivo sin introducir nuvas
semánticas temporales. Todas devuelven acciones ya existentes.
"""

from __future__ import annotations

import manim

from mathfilm.actions.base import ManimAction
from mathfilm.actions.create import Create
from mathfilm.actions.hide import Hide
from mathfilm.actions.parallel import Parallel
from mathfilm.actions.show import Show
from mathfilm.actions.write import Write
from mathfilm.core.types import Progress


def parallel(
    *actions: ManimAction,
    start: Progress = Progress(0.0),
    end: Progress = Progress(1.0),
) -> Parallel:
    """
    Construye una composición simultánea.

    Parameters
    ----------
    *actions
        Acciones de Manim que se ejecutaran simultáneamente.

    start
        Inicio relativo de la composición exterior.

    end
        Final relativo de la composición exterior.
    """

    return Parallel(actions=actions, start=start, end=end)


def hide_all(
        *mobjects: manim.Mobject,
        start: Progress = Progress(0.0),
        end: Progress = Progress(1.0)
) -> Parallel:
    """
    Oculta varios objetos simultáneamente.
    """

    if not mobjects:
        raise ValueError("hide_all necesita al menos un mobject.")

    return Parallel(
        actions=tuple(
            Hide(mobject=mobject)
            for mobject in mobjects
        ),
        start=start,
        end=end
    )

def show_all(
        *mobjects: manim.Mobject,
        start: Progress = Progress(0.0),
        end: Progress = Progress(1.0)
) -> Parallel:
    """
    Muestra varios objetos simultáneamente mediante FadeIn.
    """
    if not mobjects:
        raise ValueError("show_all necesita al menos un mobject.")

    return Parallel(
        actions=tuple(
            Show(mobject=mobject)
            for mobject in mobjects
        ),
        start=start,
        end=end
    )

def write_all(
        *mobjects: manim.VMobject,
        start: Progress = Progress(0.0),
        end: Progress = Progress(1.0)
) -> Parallel:
    """
    Escribe varios objetos simultáneamente mediante Write.
    """
    if not mobjects:
        raise ValueError("write_all necesita al menos un mobject.")

    return Parallel(
        actions=tuple(
            Write(mobject=mobject)
            for mobject in mobjects
        ),
        start=start,
        end=end
    )


# mathfilm/actions/factories.py

def create_all(
    *mobjects: manim.VMobject,
    start: Progress = Progress(0.0),
    end: Progress = Progress(1.0),
) -> Parallel:
    """
    Dibuja varios objetos simultáneamente.
    """

    if not mobjects:
        raise ValueError(
            "create_all necesita al menos un mobject."
        )

    return Parallel(
        actions=tuple(
            Create(mobject=mobject)
            for mobject in mobjects
        ),
        start=start,
        end=end,
    )