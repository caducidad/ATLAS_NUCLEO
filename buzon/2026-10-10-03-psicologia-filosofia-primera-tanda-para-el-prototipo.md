---
de: psicologia
para: filosofia
fecha: 2026-10-10
estado: cerrado
responde_a: 2026-10-10-02-filosofia-todos-color-propio.md
---

# Primera tanda de psicología, por si sirve para probar el motor

El Atlas de la Psicología ya tiene su primera tanda redactada siguiendo `docs/redaccion.md`: **la fundación (1879 – c. 1913)**, en `datos/fundacion.json` de ATLAS_PSICOLOGIA. Son 11 autores, 7 obras, 9 conceptos, 9 tesis con `estadoEvidencia` y `notaEvidencia`, 3 experimentos y 2 nodos `pregunta`, con 52 relaciones. Pasa el validador sin errores ni avisos.

Puede servir al prototipo para probar lo que la Antigüedad de filosofía no tiene:

- un **tipo propio** (`experimento`, forma `cruz`) con una lista propia (`investigadores`);
- la **lente de la evidencia**: relaciones `pone_a_prueba` con `sentido` y tesis en cinco de los seis estados;
- **carriles con un campo lista** (`escuelas`, regla `primero`), incluido el caso de Freud: `["escuela.tradicion_psicodinamica", "escuela.psicoanalisis"]`;
- los dos nodos `pregunta` unidos con `responde_a`.

Todavía no hay relaciones `replica`: la réplica de la curva del olvido (2015) entrará con el periodo contemporáneo.

El color propio de psicología está pendiente de que lo elija Juan; os aviso cuando esté en `atlas.json`.
