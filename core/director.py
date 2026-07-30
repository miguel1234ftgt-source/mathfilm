# mathfilm/core/director.py
"""
Director temporal de MathFilm.

El Director recorre la línea temporal y convierte los intervalos
relativos de cada acción en tiempos reales medidos en segundos.

El núcleo sigue siendo independiente de Manim: únicamente conoce
el protocolo SceneAdapter
"""

from __future__ import annotations
from dataclasses import dataclass

from mathfilm.core.section import Section
from mathfilm.core.timeline import Timeline
from mathfilm.core.types import Seconds
from mathfilm.engine.narration_resolver import NarrationResolver
from mathfilm.engine.scene_adapter import SceneAdapter


@dataclass(slots=True)
class Director:
    """
    Coordina la ejecución temporal de una línea narrativa.
    """

    timeline: Timeline
    scene: SceneAdapter
    narration_resolver: NarrationResolver

    def render(self) -> None:
        """
        Ejecuta todas las secciones en orden.

        Parameters
        ----------
        timeline
            Línea temporal que se ejecutará.

        scene
            Adaptador del motor gráfico.
        """

        for section in self.timeline.sections:
            self.render_section(
                section=section,
            )

    def render_section(
        self,
        section: Section,
    ) -> None:
        """
        Ejecuta una sección completa.
        """

        resolved = self.narration_resolver.resolve(section.narration)

        timing = resolved.timing

        # Margen externo anterior.
        self.scene.wait(timing.padding_before)

        print(
            "[MathFilm] Narración:",
            section.narration.identifier,
        )
        print(
            "[MathFilm] Audio resuelto:",
            resolved.audio,
        )
        print(
            "[MathFilm] Duración activa:",
            resolved.timing.active_duration,
        )

        # Audio y acciones comienzan en el mismo instante.
        if resolved.audio is not None:
            self.scene.add_sound(resolved.audio)

        # Progress se resuelve exclusivamente respecto de
        # active_duration.
        self._render_actions(
            section=section,
            duration=timing.active_duration,
        )

        # Margen externo posterior.
        self.scene.wait(timing.padding_after)

    def _render_actions(self, *, section: Section, duration: Seconds) -> None:
        """
        Ejecuta las acciones durante la ventada activa.

        Esta función debe conservar el algoritmo de planificación
        existente. La diferencia es que recibe active_duration,
        nunca total_duration
        """

        self._render_section(section=section, duration=duration)

    def _render_section(self, *, section: Section, duration: Seconds) -> None:
        """
        Ejecuta una sección individual.

        la variable ``cursor`` representa el progreso temporal
        ya consumido dentro de la sección, entre 0.0 y 1.0.
        """

        section.validate_schedule()

        active_duration = duration
        cursor = 0.0

        for action in section.ordered_actions:
            action_start = float(action.start)

            # Si existe un hueco antes de la acción, se introduce
            # una espera proporcional a la duración de la sección.
            if action_start > cursor:
                relative_wait = action_start - cursor

                self._wait_relative(
                    scene=self.scene,
                    section_duration=active_duration,
                    relative_duration=relative_wait,
                )

            action.execute(
                scene=self.scene, duration=action.duration_for(active_duration)
            )

            cursor = float(action.end)

        # si la última acción termina antes del final de la
        # narración, esperamos el tiempo restante.
        if cursor < 1.0:
            self._wait_relative(
                scene=self.scene,
                section_duration=active_duration,
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

        # Manim acepta esperas positivas. Evitamos llamadas
        # innecesarias causadas por errores de redondeo.
        if seconds > 0.0:
            scene.wait(seconds)
