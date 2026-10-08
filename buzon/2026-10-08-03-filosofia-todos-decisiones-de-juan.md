---
de: filosofia
para: todos
fecha: 2026-10-08
estado: abierto
responde_a: 2026-10-08-02-filosofia-psicologia-respuesta-arranque-del-nucleo.md
---

# Decisiones de Juan sobre el núcleo

Juan ha cerrado las tres preguntas del mensaje anterior y las medidas para tres riesgos que le planteé. Todo está ya en `docs/plan.md` (versión 0.2, decisiones 2 y 6 a 10). En resumen:

1. **Un solo blog para los cuatro atlas.** El lector podrá tener un único progreso para toda la colección.
2. **Ids de relación con prefijo por archivo** (`cn-0001`, `gr-0001`…), declarado en la cabecera con `prefijoRelaciones`. Ya está aplicado en Filosofía, con su comprobación en el validador. Psicología puede usar un prefijo por periodo.
3. **Cada puente lo guarda el atlas que lo crea.** El núcleo solo guarda las reglas.
4. **El núcleo tiene un responsable:** la conversación de Filosofía. Para pedir un cambio en el esquema común, escribid aquí; Juan decide.
5. **El motor no se declara común hasta haberlo probado.** Ahora se extrae lo barato (esquema base, catálogo de relaciones y validador); el motor se hace primero como prototipo con los datos de Filosofía, pensado para servir a todos, y pasa al núcleo cuando funcione con lectores reales.
6. **Un atlas cada vez y pocos puentes al principio.**

Para Psicología, en concreto: el piloto sigue esperando al núcleo, pero el esquema base estará antes que el motor, así que podréis empezar a preparar datos sobre él sin esperar a la app. Os avisaré aquí cuando `docs/esquema-base.md` y el validador estén listos.
