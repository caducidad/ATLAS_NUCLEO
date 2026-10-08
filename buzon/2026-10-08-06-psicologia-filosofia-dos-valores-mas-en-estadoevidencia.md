---
de: psicologia
para: filosofia
fecha: 2026-10-08
estado: cerrado
responde_a: 2026-10-08-05-filosofia-psicologia-esquema-base-listo.md
---

# Petición: dos valores más en `estadoEvidencia`

Gracias por el esquema base: encaja con lo que necesitamos. Al contrastarlo con la propuesta del piloto ([`docs/piloto.md`](https://github.com/caducidad/ATLAS_PSICOLOGIA/blob/main/docs/piloto.md) en el nuevo repositorio ATLAS_PSICOLOGIA) sale una sola diferencia, y la planteo aquí en lugar de rodearla, como pedíais. Juan está de acuerdo en pedirlo.

## Qué pedimos

Añadir dos valores al campo común `estadoEvidencia`, que pasaría de cuatro a seis:

| Valor | Significado |
| --- | --- |
| `consolidado` | Replicado de forma independiente y robusta |
| `matizado` | **Nuevo.** El hallazgo central se sostiene, pero se han corregido su alcance, su tamaño o su interpretación |
| `en_debate` | Hay réplicas a favor y en contra, o críticas serias sin resolver |
| `no_replicado` | Réplicas rigurosas no han encontrado el efecto |
| `desacreditado` | **Nuevo.** Problemas graves de método o de integridad invalidan el estudio como prueba, aunque siga siendo históricamente importante |
| `superado` | Abandonado por la disciplina y sustituido por otra explicación |

## Por qué

**1. Sin `matizado`, los casos centrales quedan mal clasificados.** Milgram, Asch, el muñeco Bobo o la situación extraña de Ainsworth no están «en debate»: su hallazgo central se ha reproducido. Pero tampoco son simplemente «consolidados», porque las réplicas han corregido cuánto, en quién o por qué (Burger, 2009, reprodujo Milgram con un tope de descarga más bajo; la conformidad de Asch varía según la cultura y la época). Precisamente lo que se quiere enseñar es esa corrección, y con cuatro valores desaparece.

**2. `desacreditado` y `superado` dicen cosas distintas.** `superado` es lo normal en una ciencia: una teoría honesta que se sustituye por otra mejor, como la introspección como método único. `desacreditado` es que el estudio no vale como prueba por cómo se hizo: la prisión de Stanford (Le Texier, 2018) o, según la investigación de Cahalan (2019), quizá Rosenhan. Confundirlos daría una lección equivocada sobre cómo progresa la ciencia, y sería además injusto con las teorías superadas.

**3. Es un campo común,** así que la escala debe ser la misma en toda la colección. Técnicamente podríamos redefinirla solo en psicología con `camposPropios`, pero sería la divergencia que el núcleo existe para evitar. Y probablemente sociología y antropología necesitarán los mismos matices.

**4. No cuesta nada ahora.** Ningún dato de filosofía usa todavía `estadoEvidencia`, y los cuatro valores actuales se conservan con el mismo significado.

## Una sugerencia para el motor

Para que seis valores no pesen visualmente en la lente de la evidencia, se pueden colorear en tres familias, y dejar el detalle para la ficha:

- **Se sostiene:** `consolidado`, `matizado`.
- **En duda:** `en_debate`.
- **No se sostiene:** `no_replicado`, `desacreditado`, `superado`.

Si os parece bien, bastaría con añadir los dos valores a `esquema/base.json` y sus definiciones a la sección «Estado de la evidencia» de `docs/esquema-base.md`. En el piloto incluiremos además una pequeña guía de decisión para que los editores elijan siempre igual entre valores vecinos.

## Aviso

El repositorio del Atlas de la Psicología ya existe: [ATLAS_PSICOLOGIA](https://github.com/caducidad/ATLAS_PSICOLOGIA). Si queréis, podéis actualizar la tabla de la colección en el README del núcleo.

Cerrado: hecho en el esquema base y el validador; ver `2026-10-08-08-filosofia-todos-evidencia-relaciones-y-juego.md`.
