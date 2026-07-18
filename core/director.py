# mathfilm/core/director.py
"""
Director temporal de MathFilm.

El Director recorre la línea temporal y convierte los intervalos
relativos de cada acción en tiempos reales medidos en segundos.

El núcleo sigue siendo independiente de Manim: únicamente conoce
el protocolo SceneAdapter
"""

from __future__ import annotations

from mathfilm.core.section import Section
from mathfilm.core.timeline import Timeline
from mathfilm.core.types import Seconds
from mathfilm.engine.scene_adapter import SceneAdapter


class Director:
    """
    Coordina la ejecución temporal de una línea narrativa.
    """

    def render(
        self,
        timeline: Timeline,
        scene: SceneAdapter,
    ) -> None:
        """
        Ejecuta todas las secciones en orden.

        Parameters
        ----------
        timeline
            Línea temporal que se ejecutará.

        scene
            Adaptador del motor gráfico.
        """

        for section in timeline.sections:
            self._render_section(
                section=section,
                scene=scene,
            )

    def _render_section(self, *, section: Section, scene: SceneAdapter) -> None:
        """
        Ejecuta una sección individual.

        la variable ``cursor`` representa el progreso temporal
        ya consumido dentro de la sección, entre 0.0 y 1.0.
        """

        section.validate_schedule()

        section_duration = section.duration
        cursor = 0.0

        for action in section.ordered_actions:
            action_start = float(action.start)

            # Si existe un hueco antes de la acción, se introduce
            # una espera proporcional a la duración de la sección.
            if action_start > cursor:
                relative_wait = action_start - cursor
            
                self._wait_relative(
                    scene=scene,
                    section_duration=section_duration,
                    relative_duration=relative_wait,
                )
            
            action.execute(
                scene=scene,
                duration=action.duration_for(section_duration)
            )

            cursor = float(action.end)

        #si la última acción termina antes del final de la
        #narración, esperamos el tiempo restante.
        if cursor < 1.0:
            self._wait_relative(
                scene=scene,
                section_duration=section_duration,
                relative_duration=1.0 - cursor,
            )

    @staticmethod
    def _wait_relative(
        *,
        scene: SceneAdapter,
        section_duration: Seconds,
        relative_duration: float,
    ) -> None:
        """
        Convierte una espera relativa en segundos.
        """

        seconds = float(section_duration) * relative_duration

        #Manim acepta esperas positivas. Evitamos llamadas
        #innecesarias causadas por errores de redondeo.
        if seconds > 0.0:
            scene.wait(seconds)