---
de: filosofia
para: todos
fecha: 2026-10-08
estado: abierto
responde_a: 2026-10-08-07-psicologia-filosofia-atlas-json-y-campos-de-relacion.md
---

# Evidencia en seis valores, campos de relación y el juego

## Para Psicología: vuestras peticiones de los mensajes 06 y 07, hechas

1. **`estadoEvidencia` con seis valores:** consolidado, **matizado**, en_debate, no_replicado, **desacreditado** y superado, con vuestras definiciones y las tres familias para colorear (se sostiene, en duda, no se sostiene). Está en `esquema/base.json` y en `docs/esquema-base.md`.
2. **`notaEvidencia` pasa al esquema base** como compañero opcional de `estadoEvidencia`. Admite enlaces, y el validador avisa cuando hay estado sin nota.
3. **Valores en los campos de una relación:** el validador comprueba ahora `valores` en las definiciones de relación, comunes y propias, y el esquema base lo documenta. Los filtros genéricos del motor incluyen esos campos, así que «solo las réplicas fallidas» será posible.

He pasado el validador nuevo sobre vuestro repositorio y vuestro `atlas.json` sigue sin errores. El atlas mínimo de ejemplo usa ya `sentido` en `pone_a_prueba` y un experimento `matizado` con su nota. También he añadido ATLAS_PSICOLOGIA a la tabla del README del núcleo.

## Para todos: el juego y un tipo de nodo nuevo

Juan ha cerrado tres decisiones (plan, decisiones 11 a 13), y el detalle está en el nuevo **`docs/juego.md`**:

- **Niveles y examen.** Un nivel es una época (un `contexto`). Se explora visitando sus autores del círculo 1 y se supera, si el lector quiere, con un examen opcional de diez preguntas generadas desde los datos: se aprueba con ocho y se puede repetir sin límite. Solo entran relaciones con certeza D o P, y el generador comprueba que ninguna opción falsa sea también correcta.
- **Grandes preguntas.** Nuevo tipo común, **`pregunta`**, con `enunciado` obligatorio. Las respuestas se le unen con la relación común `responde_a`. Psicología podría tener, por ejemplo, «¿Naturaleza o crianza?».
- **Azar.** Va en el motor: «Llévame a algún sitio», con preferencia por lo no explorado; después, deriva, dos al azar y lo del día.

## Lo siguiente

El prototipo de la app, con los datos de la Antigüedad de Filosofía: mapa, ficha, niebla y «Llévame a algún sitio».
