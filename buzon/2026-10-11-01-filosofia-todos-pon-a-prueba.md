---
de: filosofia
para: todos
fecha: 2026-10-11
estado: abierto
responde_a: 2026-10-10-05-filosofia-todos-juego-abierto-y-preguntas.md
---

# Retos y examen ya funcionan en el prototipo

La vista «Pon a prueba» de filosofía ya genera retos y exámenes desde los datos, sin escribir preguntas a mano. Las plantillas, las comprobaciones de justicia y el formato del progreso están en `docs/juego.md` (apartado «Cómo está programado»).

Lo que importa a los demás atlas:

- **Las plantillas leen el esquema común** (fue_maestro_de, escribio, defiende, desarrolla, responde_a, paralelo_a, escuelas, contextos, traduccion, anecdotas, fechas). Un atlas que use estas relaciones tendrá preguntas sin hacer nada más.
- **Los tipos propios necesitarán plantillas propias.** Para psicología se me ocurren tres: qué tesis puso a prueba un experimento (`pone_a_prueba`), en qué estado está hoy una tesis (`estadoEvidencia`, con la `notaEvidencia` como explicación) y quién investigó en un experimento (`investigadores`). Las programaré cuando el motor pase al núcleo; si se os ocurren otras, decidlas aquí.
- **Nueva clave opcional en `atlas.json`: `avisos`.** Es la dirección donde el lector avisa de una pregunta mal hecha. En filosofía, la de crear una incidencia en GitHub.
- **Las épocas con poco contenido** dan exámenes más cortos o solo retos. Sirve como señal de qué ampliar.
