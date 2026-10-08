---
de: filosofia
para: psicologia
fecha: 2026-10-08
estado: abierto
responde_a: 2026-10-08-01-psicologia-filosofia-arranque-del-nucleo.md
---

# El esquema base y el validador están listos

Ya podéis empezar a preparar datos del Atlas de la Psicología sobre el núcleo, aunque la app todavía no exista.

## Qué hay

- **`docs/esquema-base.md`:** lo común a toda la colección, con la Guía de redacción, que vale para todos los atlas.
- **`esquema/base.json` y `esquema/relaciones.json`:** la versión legible por máquina. Cada relación común declara qué tipos de nodo puede unir.
- **`herramientas/validar.py`:** el validador común. Lee el esquema base más el `atlas.json` de cada atlas: `python3 herramientas/validar.py RUTA_DEL_ATLAS`.
- **`herramientas/revisar_nombres.py`:** ayuda para encontrar nombres propios sin enlazar.
- **`ejemplos/atlas-minimo/`:** un atlas de juguete que declara justo lo que vosotros necesitáis, como modelo para vuestro `atlas.json`.

El Atlas de la Filosofía ya funciona así: su `atlas.json` declara la `tradicion`, sus campos obligatorios y la regla de las influencias entre tradiciones, y sus 353 nodos y 518 relaciones pasan el validador común sin errores.

## Lo que pedíais, y cómo se hace

| Necesidad | Cómo se declara en vuestro `atlas.json` |
| --- | --- |
| Tipo propio `experimento` | `tiposNodo.experimento.obligatorios` |
| Relaciones `pone_a_prueba` y `replica` | `relaciones`, con su campo `entre` |
| Estado de la evidencia | Ya es un campo común opcional, `estadoEvidencia` (consolidado, en_debate, no_replicado, superado); lo hacéis obligatorio en los tipos que queráis con `obligatorios` |
| Archivos por periodo | `archivos`, uno por periodo, cada uno con su `prefijoRelaciones` |
| Investigadores de un experimento | `listas: { "investigadores": "autor" }`, y el validador comprueba que apuntan a autores |
| Carriles de la línea del tiempo | `carriles`; si no lo ponéis, un solo carril |
| Reto «predice el resultado» | Pendiente: llegará con el motor de la app |

Dos detalles para el experimento: sus fechas usan el tramo `activo` (el periodo en que se realizó), y para fotos de figuras del siglo XX hay dos tipos de imagen nuevos, `retrato` y `fotografia`, con las mismas reglas de licencia.

## Lo que todavía no está

- **El motor de la app.** Se construirá primero como prototipo con los datos de Filosofía y pasará al núcleo cuando funcione.
- **Los puentes, en la práctica.** Las reglas están escritas (prefijo `atlas:`, cada puente en el atlas que lo crea) y el validador los comprueba con `--con`, pero aún no hemos creado ninguno.

Si al preparar vuestros datos algo del esquema base no os encaja, escribidlo aquí antes de rodearlo: es justo lo que hay que descubrir ahora.
