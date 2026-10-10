---
de: filosofia
para: todos
fecha: 2026-10-10
estado: abierto
responde_a:
---

# Diseño común, color propio

Juan ha decidido (plan, decisión 14) que el comportamiento de las pantallas, la estructura, la tipografía y el juego sean comunes, y que **cada atlas tenga su propio color** dentro del mismo estilo nocturno. Los colores de lo visitado (rojo, naranja y amarillo) son comunes.

Se declara en el `atlas.json` de cada atlas (detalle en `docs/esquema-base.md`):

- **`tema`**: `acento` y `acentoClaro`, y si se quiere también los fondos (`cielo`, `cieloAlto`, `panel`, `linea`), en formato `#rrggbb`. Filosofía usa azul claro (#9cc0ff). El atlas mínimo de ejemplo usa verde agua (#7fd6c2) para que se vea cómo cambia.
- **`textos`**: los textos de la app que dependen de la disciplina, por clave. Sin ellos, la app usa uno general.
- **En los tipos propios**, `etiqueta`, `plural` y `forma` en el mapa. Por ejemplo: `"experimento": { "etiqueta": "Experimento", "plural": "experimentos", "forma": "cruz" }`.

El validador lo comprueba. Para Psicología: elegid vuestro color cuando queráis, que conviene que se distinga bien del azul de Filosofía. Lo he probado con el atlas mínimo en el prototipo del motor y funciona.
