# Esquema base de la colección Atlas

Versión 0.1 · 8 de octubre de 2026

Este documento describe lo que comparten todos los atlas de la colección: la forma de los datos, las relaciones comunes, las reglas de redacción y la manera en que cada atlas amplía el esquema con lo suyo. Lo propio de cada disciplina se documenta en su repositorio (en filosofía, `docs/esquema.md`).

La versión legible por máquina está en [`esquema/base.json`](../esquema/base.json) y [`esquema/relaciones.json`](../esquema/relaciones.json), y el validador [`herramientas/validar.py`](../herramientas/validar.py) comprueba los datos contra ella.

## Principios

- **Todo es un nodo.** Autores, obras, conceptos, tesis, escuelas, contextos y temáticas comparten una estructura común y se distinguen por el campo `tipo`. Cada atlas puede añadir tipos propios.
- **Clasificar no es relacionar.** A qué contexto, temática o escuela pertenece un nodo se guarda como lista dentro del propio nodo. Las relaciones se reservan para vínculos con significado.
- **Cada relación se guarda una sola vez.** La app calcula el inverso («fue maestro de» ↔ «fue discípulo de»).
- **La incertidumbre es un dato.** Fechas en horquilla, historicidad, autoría y certeza de cada relación son campos con valores fijos, no notas al margen.
- **Dos capas de texto.** `resumen` accesible y `profundizacion` rigurosa, con palabras enlazadas a otros nodos.
- **El progreso del lector va aparte.** Nunca se mezcla con los datos, así que estos se pueden actualizar sin borrar el avance de nadie.

## Estructura de un atlas

Cada atlas es un repositorio con un `atlas.json` en la raíz y sus datos repartidos en varios archivos:

```
atlas.json          Configuración y extensiones del atlas
datos/*.json        Nodos y relaciones, en varios archivos
imagenes/           Imágenes libres de derechos (opcional)
```

Cada archivo de datos tiene esta forma:

```json
{
  "version": "0.1",
  "actualizado": "2026-10-08",
  "descripcion": "…",
  "prefijoRelaciones": "cn",
  "nodos": [ { "id": "autor.confucio", "tipo": "autor", "…": "…" } ],
  "relaciones": [ { "id": "cn-0001", "origen": "…", "tipo": "…", "destino": "…" } ]
}
```

La app carga todos los archivos que enumera `atlas.json` y los une al arrancar, así que un enlace o una relación puede apuntar a un nodo de otro archivo del mismo atlas.

## Identificadores

- **Nodos:** `tipo.nombre`, en minúsculas, sin tildes ni espacios: `autor.platon`, `obra.republica`, `concepto.ren`. El prefijo evita choques como «Zhuangzi» autor frente a *Zhuangzi* obra.
- **Relaciones:** cada archivo declara un `prefijoRelaciones` propio y numera con él sus relaciones: `cn-0001`, `gr-0001`. Un archivo nuevo recibe un prefijo nuevo, así que la numeración no se agota ni choca.
- **Otros atlas:** se antepone el nombre del atlas y dos puntos: `filosofia:autor.descartes`, `filosofia:gr-0001`. Dentro de un atlas los ids van sin prefijo.
- **Años:** números enteros, negativos antes de Cristo (−551 = 551 a. C.). No existe el año 0: de −1 se pasa a 1.

## Nodos

### Campos comunes

| Campo | Obligatorio | Qué contiene |
| --- | --- | --- |
| `id` | Sí | Identificador `tipo.nombre` |
| `tipo` | Sí | autor, obra, concepto, tesis, escuela, contexto, tematica o un tipo propio del atlas |
| `nombre` | Sí | Forma visible: «Confucio», «Analectas» |
| `resumen` | Sí | Dos o tres frases accesibles, con enlaces |
| `nombreOriginal` | No | Escritura original: 孔子, Πλάτων |
| `alias` | No | Otras formas para el buscador |
| `contextos` | No | Lista de ids de contexto |
| `tematicas` | No | Lista de ids de temática |
| `escuelas` | No | Lista de ids de escuela |
| `profundizacion` | No | Texto riguroso, con enlaces |
| `fechas` | Según tipo | Objeto de fechas (abajo) |
| `imagenes` | No | Lista de imágenes (abajo) |
| `estadoEvidencia` | No | consolidado, en_debate, no_replicado o superado (abajo) |
| `fuentes` | No | Referencias bibliográficas para la profundización |

Cada atlas puede declarar campos propios y hacer obligatorios campos que aquí son opcionales; en filosofía, por ejemplo, `tradicion` es obligatoria.

### Tipos comunes

| Tipo | Obligatorios | Otros campos |
| --- | --- | --- |
| **autor** | `fechas` | `circulo` (1 canon, 2 secundario, 3 puente), `lugarOrigen`, `anecdotas` |
| **obra** | `autoria`, `fechas` | `idiomaOriginal`, `capas` (estratos del texto con su fecha y testimonio), `primerTestimonio` |
| **concepto** | — | `terminoOriginal`, `transliteracion`, `traduccion`, `notaTraduccion` |
| **tesis** | `enunciado` | La afirmación en una frase |
| **escuela** | `naturaleza` | real o rotulo_historiografico (una etiqueta puesta después, como «presocráticos») |
| **contexto** | `horquilla` (`inicio` y `fin`) | `lugar`; las subdivisiones se mencionan en el texto |
| **tematica** | — | Cada atlas tiene las suyas |

`autoria` admite: autor, atribuida, escuela, compilacion o anonima.

**Obras sin autor directo.** Si el autor no escribió la obra (una compilación de discípulos), no se usa `escribio`, sino `es_fuente_de` desde la obra. Si la autoría es dudosa, se usa `escribio` con certeza C.

### Fechas

Cada fecha es una horquilla, nunca un número suelto, para que la línea del tiempo pueda dibujar la incertidumbre:

```json
"fechas": {
  "nacimiento": { "min": -551, "max": -551 },
  "muerte": { "min": -479, "max": -479 },
  "tipo": "tradicional",
  "historicidad": "historico",
  "alternativas": [
    { "etiqueta": "Tradicional", "nacimiento": { "min": -552, "max": -552 }, "muerte": { "min": -479, "max": -479 } }
  ],
  "nota": "…"
}
```

- **Tramos:** `nacimiento` y `muerte`, o `activo` cuando solo se conoce el periodo de actividad (o, en un experimento, el de realización). Las obras usan `composicion`.
- `tipo`: exacta, aproximada, tradicional o actividad (esta última exige el tramo `activo`).
- `historicidad`: historico, probable, debatido, legendario o colectivo.
- `alternativas`: otras cronologías, cada una con su `etiqueta`. Por defecto la app muestra la principal; las alternativas se ven en la ficha y como barra fantasma en la línea del tiempo.

## Textos

**Enlaces.** Se escriben con doble corchete: `[[concepto.ren|humanidad]]` muestra «humanidad» y lleva a `concepto.ren`; `[[autor.mencio]]` muestra el nombre del nodo. Un enlace a otro atlas lleva su prefijo: `[[filosofia:autor.descartes|Descartes]]`.

**Anécdotas.** Un único bloque de texto por nodo. Cada anécdota termina con su fuente y su fiabilidad entre paréntesis, sin paréntesis dentro:

```
… aceptó la comparación riendo ([[obra.shiji|Shiji]], cap. 47 · C).
```

Escala de fiabilidad: **A** fuente contemporánea de los hechos; **B** fuente posterior pero seria; **C** tradición o anécdota literaria; **L** leyenda. La app nunca muestra la letra suelta, sino su significado.

## Guía de redacción

Tres reglas para todos los textos de todos los atlas (resumen, profundización, anécdotas y notas):

1. **Ningún nombre propio sin contexto.** Toda persona, obra, lugar o institución que aparezca en un texto, o está enlazada a su ficha, o se explica en la misma frase («el ingeniero Gongshu Ban», «el historiador griego Heródoto»). Si un nombre se repite en varias fichas, merece ficha propia, aunque sea mínima.
2. **Claridad antes que brevedad.** Frases completas que se entiendan sin conocer la fuente: quién hace qué y por qué. Si una anécdota necesita contexto para tener sentido, se le da, aunque quede más larga.
3. **Referencias legibles.** Las fuentes se citan con nombre y capítulo, enlazando a la ficha de la obra cuando existe.

El validador comprueba la regla 3 y el formato de los enlaces. Para la regla 1 hay una ayuda, [`herramientas/revisar_nombres.py`](../herramientas/revisar_nombres.py), que lista los nombres en mayúscula que quedan fuera de los enlaces; la decisión final es humana.

## Imágenes

```json
"imagenes": [
  {
    "archivo": "imagenes/china/confucio-retrato.webp",
    "fuente": "https://commons.wikimedia.org/wiki/File:…",
    "tipo": "retrato_imaginario",
    "pie": "Confucio. Representación imaginaria, grabado de época Ming (s. XVI).",
    "fechaObra": "s. XVI",
    "autorObra": "Anónimo",
    "licencia": "dominio_publico",
    "credito": ""
  }
]
```

- `tipo`: retrato_imaginario, retrato, fotografia, escultura, manuscrito, inscripcion, lugar, objeto u otro.
- `licencia`: dominio_publico, CC0, CC-BY o CC-BY-SA (versiones 2.0, 2.5, 3.0 y 4.0). **No se admiten licencias no comerciales (NC) ni sin obras derivadas (ND)**, porque son incompatibles con la licencia CC BY-SA de los datos.
- `credito`: obligatorio con CC BY y CC BY-SA; es la atribución que la app muestra bajo la imagen.
- **La obra frente a la foto.** Una obra antigua puede ser de dominio público y la foto de un objeto en tres dimensiones tener derechos del fotógrafo: cuenta la licencia de la foto. Con figuras del siglo XX, muchas fotografías siguen protegidas.
- **Rigor en el pie.** Toda imagen de una persona hecha mucho después indica que es una representación imaginaria y su fecha.
- **Tamaño.** WebP, unos 800 píxeles de lado mayor (alrededor de 100 KB); la app solo las carga al abrir la ficha.

## Relaciones

Catálogo común, en [`esquema/relaciones.json`](../esquema/relaciones.json):

| Clave | Se lee (directo) | Se lee (inverso) | Entre | Simétrica |
| --- | --- | --- | --- | --- |
| `escribio` | escribió | escrita por | autor → obra | No |
| `parte_de` | es parte de | contiene | obra → obra; temática → temática; contexto → contexto | No |
| `fue_maestro_de` | fue maestro de | fue discípulo de | autor → autor | No |
| `influyo_en` | influyó en | recibió influencia de | cualquiera | No |
| `critica` | critica | es criticado por | cualquiera | No |
| `desarrolla` | desarrolla | es desarrollado por | cualquiera | No |
| `responde_a` | responde a | recibe respuesta de | cualquiera | No |
| `defiende` | defiende | es defendida por | autor, escuela u obra → tesis | No |
| `trata_sobre` | trata sobre | se trata en | obra o tesis → concepto o tesis | No |
| `comenta` | comenta | es comentada por | autor u obra → obra | No |
| `es_fuente_de` | es fuente sobre | se conoce a través de | obra → autor, escuela, contexto u obra | No |
| `se_opone_a` | se opone a | se opone a | concepto, tesis, escuela o autor, entre sí | Sí |
| `paralelo_a` | es paralelo a | es paralelo a | cualquiera | Sí |

Cada relación es un objeto con su grado de certeza:

```json
{
  "id": "cn-0045",
  "origen": "autor.xunzi",
  "tipo": "critica",
  "destino": "autor.mencio",
  "certeza": "D",
  "fuente": "Xunzi, cap. 23",
  "nota": "Rechaza que la naturaleza humana sea buena."
}
```

- `certeza` (obligatoria): **D** documentado, **P** probable, **C** conjetural, **L** legendario.
- `fuente`: dónde consta la relación.
- `nota`: explicación breve, con enlaces si hace falta.
- `ejeComparacion`: obligatorio en `paralelo_a`; dice en qué se parecen los dos nodos («impermanencia»). `paralelo_a` sirve para comparar sin afirmar una influencia que no consta.
- No puede haber dos relaciones con el mismo origen, tipo y destino.

## Estado de la evidencia

`certeza` dice si consta una **relación** (que A influyó en B). `estadoEvidencia` dice cómo está hoy una **afirmación**: una tesis, una teoría o un hallazgo.

- `consolidado`: aceptado por la comunidad y bien apoyado.
- `en_debate`: discutido o con resultados contradictorios.
- `no_replicado`: intentos serios de repetirlo han fallado.
- `superado`: abandonado o sustituido por otra explicación.

Es un campo opcional para todos los nodos; cada atlas decide en qué tipos lo hace obligatorio.

## Extender el esquema: `atlas.json`

Cada atlas declara aquí lo suyo. Todos los campos salvo `atlas`, `nombre` y `archivos` son opcionales.

```json
{
  "atlas": "psicologia",
  "nombre": "Atlas de la Psicología",
  "version": "0.1",
  "nucleo": "0.1",
  "archivos": ["datos/tematicas.json", "datos/fundacion.json"],
  "carriles": "escuelas",
  "camposPropios": {
    "tradicion": { "valores": ["…"], "obligatorioEn": ["autor", "obra"] }
  },
  "listas": { "investigadores": "autor" },
  "obligatorios": { "autor": ["circulo"] },
  "obligatoriosSi": [
    { "tipo": "autor", "si": { "circulo": 1 }, "campos": ["profundizacion", "anecdotas"] }
  ],
  "tiposNodo": {
    "experimento": { "obligatorios": ["fechas", "investigadores", "diseno", "resultado", "estadoEvidencia"] }
  },
  "relaciones": {
    "pone_a_prueba": {
      "directo": "pone a prueba", "inverso": "es puesta a prueba por", "simetrica": false,
      "entre": [[["experimento"], ["tesis", "concepto"]]]
    }
  },
  "reglas": [
    { "regla": "fuenteSiDifiere", "relacion": "influyo_en", "campo": "tradicion", "mensaje": "…" }
  ]
}
```

| Clave | Para qué sirve |
| --- | --- |
| `archivos` | Archivos de datos que forman el atlas, en el orden en que se cargan |
| `carriles` | Campo que separa los carriles de la vista cronológica (en filosofía, `tradicion`); sin él, un solo carril |
| `camposPropios` | Campos que no existen en el esquema base, con sus valores admitidos y los tipos en que son obligatorios |
| `listas` | Campos propios que son listas de ids, con el tipo al que deben apuntar |
| `obligatorios` | Campos que pasan a ser obligatorios en un tipo común |
| `obligatoriosSi` | Campos obligatorios solo cuando se cumple una condición |
| `tiposNodo` | Tipos de nodo propios, con sus campos obligatorios y valores admitidos |
| `relaciones` | Relaciones propias, con el mismo formato que el catálogo común; no pueden repetir una clave común |
| `reglas` | Reglas editoriales propias. Hoy existe `fuenteSiDifiere`: una relación exige `fuente` cuando sus dos extremos tienen distinto valor en un campo |

Hay un ejemplo completo y válido en [`ejemplos/atlas-minimo`](../ejemplos/atlas-minimo).

## Puentes entre atlas

- **Referencia con prefijo:** `filosofia:autor.descartes`.
- **Cada figura tiene un atlas «de casa»** y los demás la referencian; no hay dos fichas de la misma persona.
- **Cada puente lo guarda el atlas que lo crea**, en sus propios archivos, como cualquier otra relación.
- **Validación:** con `--con` el validador carga los otros atlas y comprueba que los ids externos existen y que la relación une tipos admitidos; sin ellos, solo avisa.

## Progreso del lector

Se guarda en el navegador y es también el formato del archivo que se exporta e importa. Como los cuatro atlas viven en el mismo blog, comparten almacenamiento y el lector tiene un solo progreso, con los ids prefijados por atlas:

```json
{
  "formato": "atlas-progreso",
  "version": "0.2",
  "perfil": { "nombre": "Juan", "creado": "2026-10-08" },
  "visitas": {
    "filosofia:autor.confucio": { "veces": 5, "primera": "2026-10-08T10:12", "ultima": "2026-10-09T18:40" }
  },
  "recorrido": [
    { "id": "filosofia:autor.confucio", "t": "2026-10-08T10:12", "desde": null },
    { "id": "filosofia:concepto.ren", "t": "2026-10-08T10:14", "desde": "filosofia:autor.confucio" }
  ],
  "busquedas": [ { "atlas": "filosofia", "texto": "virtud", "t": "2026-10-08T10:20" } ],
  "retos": { "filosofia": { "aciertos": 12, "fallos": 4 } },
  "misiones": { "filosofia:mision.hilo_virtud": { "pasos": ["filosofia:autor.socrates", "filosofia:autor.platon"] } }
}
```

- **Niebla de guerra:** 0 visitas sin explorar; 1 rojo brasa; 2-4 naranja; 5 o más amarillo. Los umbrales se ajustarán al probar.
- **Mapa del recorrido:** sale de `recorrido`, porque cada paso guarda de qué nodo venía, aunque sea de otro atlas.
- **Varios perfiles:** cada perfil se guarda con su propia clave.
- **Ids que ya no existen:** se conservan al importar, sin mostrarlos.

## Validador

```
python3 herramientas/validar.py RUTA_DEL_ATLAS [--con RUTA_DE_OTRO_ATLAS ...]
```

Comprueba, entre otras cosas: tipos y forma de los ids; campos obligatorios y valores admitidos, comunes y propios; que las listas apunten a nodos del tipo correcto; enlaces y corchetes; fechas (tramos, horquillas en orden, alternativas con etiqueta); formato de las referencias de las anécdotas; imágenes y licencias; prefijos e ids de relación; que cada relación una tipos admitidos; certeza; campos obligatorios de cada relación; relaciones repetidas, y las reglas propias del atlas. Avisa de los nodos sin ninguna relación y de los ids externos sin comprobar. Solo necesita Python 3.
