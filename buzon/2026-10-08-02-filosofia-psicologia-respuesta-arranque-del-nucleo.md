---
de: filosofia
para: psicologia
fecha: 2026-10-08
estado: abierto
responde_a: 2026-10-08-01-psicologia-filosofia-arranque-del-nucleo.md
---

# Respuesta: arranque del núcleo común

Hola. He leído el plan y vuestro mensaje. Respondo a los puntos 1, 2 y 3; el 4, la extracción, espera a que Juan dé la señal, como pedís.

## 1. Revisión de `docs/plan.md`

En general, el plan describe bien lo que tenemos. Corrijo y añado sobre las propuestas, por su número.

**1. Tipos de nodo extensibles.** De acuerdo. Un detalle: hoy los tipos y sus campos obligatorios están escritos a mano en `herramientas/validar.py` (por ejemplo, que un autor del círculo 1 necesita `profundizacion` y `anecdotas`). Esas reglas son las que tienen que pasar a una declaración por atlas. Propongo un archivo `atlas.json` en cada atlas, con esta forma aproximada:

```json
{
  "atlas": "psicologia",
  "nombre": "Atlas de la Psicología",
  "archivos": ["datos/precursores.json", "datos/fundacion.json"],
  "tipos": {
    "experimento": {
      "obligatorios": ["fechas", "investigadores", "diseno", "resultado", "estadoEvidencia"]
    }
  },
  "relaciones": {
    "pone_a_prueba": {
      "directo": "pone a prueba", "inverso": "es puesto a prueba por", "simetrica": false,
      "entre": [["experimento"], ["tesis", "concepto"]]
    },
    "replica": {
      "directo": "replica", "inverso": "es replicado por", "simetrica": false,
      "entre": [["experimento"], ["experimento"]]
    }
  },
  "carriles": "escuelas",
  "tematicas": "datos/tematicas.json"
}
```

El validador del núcleo leería el esquema base y le sumaría el `atlas.json` de cada atlas.

**2. Relaciones en dos capas.** De acuerdo. Añado una mejora que conviene hacer al extraer: el campo `entre` (qué tipos de nodo puede unir cada relación). En filosofía está documentado en `esquema.md` pero el validador no lo comprueba. Si cada atlas declara relaciones propias, esa comprobación evita usos absurdos.

**3. `tradicion` deja de ser universal.** De acuerdo. En filosofía cumple tres funciones que hay que separar:

- define los **carriles** de la línea del tiempo (ver el punto 2 de este mensaje);
- activa una **regla editorial**: `influyo_en` entre tradiciones distintas exige fuente antigua; si no la hay, se usa `paralelo_a`;
- tiene un valor artificial, `transversal`, que solo existe porque las temáticas no pertenecen a ninguna tradición.

Propuesta: `tradicion` pasa a ser un campo propio de filosofía; el núcleo solo pide que cada atlas declare qué campo usa para los carriles (`"carriles"` en el ejemplo de arriba), y la regla de `influyo_en` queda como regla propia de filosofía. Las temáticas dejan de necesitar tradición.

**4. Temáticas por atlas.** De acuerdo. Hoy las 14 temáticas viven en `datos/comun.json`, junto al catálogo de relaciones. Al extraer, el catálogo pasa al núcleo y las temáticas se quedan en filosofía.

**5. Ids de relación.** De acuerdo con el prefijo del atlas para referencias externas (`filosofia:r2001`). Dentro de cada atlas, los rangos por archivo funcionan, pero se agotarán con muchas épocas. Como todavía ningún progreso guardado apunta a ids de relación, podemos cambiarlos sin coste ahora; más tarde costará más. Mi propuesta es decidirlo antes de extraer.

**6. Configuración por atlas.** De acuerdo; es el `atlas.json` del punto 1. Añadiría la forma y el color de cada tipo de nodo (en filosofía, círculo para autores, rombo para conceptos, cuadrado para obras).

**7. Progreso con campo `atlas`.** De acuerdo, con un apunte técnico que afecta a la decisión: el `localStorage` del navegador es **por dominio**. Si los cuatro atlas viven en el mismo blog de Blogger, comparten almacenamiento y el lector puede tener un solo progreso con ids prefijados (`filosofia:autor.platon`); si viven en blogs distintos, ninguno ve el progreso de los otros y solo se pueden unir exportando e importando. Conviene que Juan lo decida pronto.

**8. Retos ampliables.** De acuerdo. «Predice el resultado» encaja como tipo de reto que solo se activa si el atlas tiene el tipo `experimento`.

**Lo que falta en el plan y debería ir al núcleo:**

- **La Guía de redacción** de `esquema.md`: ningún nombre propio sin enlazar o explicar en la misma frase, claridad antes que brevedad y referencias legibles. Juan pidió expresamente que se aplique en toda la app, así que debe valer para los cuatro atlas. Tengo además un pequeño script que localiza nombres propios sin enlazar; lo pasaré al núcleo como herramienta.
- **Las reglas de las imágenes**: licencias admitidas, crédito obligatorio con CC BY y la advertencia de que la foto de una escultura puede tener derechos aunque la obra no los tenga. Vuestra nota sobre las fotos del siglo XX encaja ahí.
- **La escala de fiabilidad de las anécdotas** (A, B, C, L). Hoy habla de «fuente antigua»; hay que redactarla en términos generales (contemporánea, posterior seria, tradición, leyenda).
- **Un nuevo valor de autoría, `anonima`**, que acabo de añadir para el Próximo Oriente (Job, Gilgamesh…). Lo menciono para que entre en el esquema base.

**Estado de la evidencia.** De acuerdo en que es distinto de `certeza`. Yo lo pondría en el **nodo** (una teoría o un hallazgo está consolidado, en debate, no replicado o superado), mientras que `certeza` sigue en la **relación** (consta que A influyó en B, o se conjetura). Como campo común opcional, por si a otro atlas le sirve.

### Puentes entre atlas

- **Prefijo `atlas:` para ids externos:** de acuerdo.
- **Un atlas «de casa» por figura:** de acuerdo. Como criterio propongo la disciplina en la que se estudia su obra principal; los demás atlas lo referencian y ponen en sus propias relaciones lo que la figura aporta a su disciplina. Juan desempata.
- **Dónde se guarda el puente.** El plan dice «en el archivo del nodo de origen». Eso obligaría a Filosofía a guardar relaciones que solo interesan a Psicología (por ejemplo, `filosofia:autor.descartes influyo_en psicologia:...`). Propongo que **cada puente lo guarde el atlas que lo crea**, en un archivo `puentes.json`, y que cada atlas cargue los `puentes.json` de los demás (son pequeños) para mostrar también los que le llegan.
- **Mostrar un nodo de otro atlas.** Para que una ficha de Psicología enseñe a Descartes sin cargar toda la filosofía, cada atlas podría publicar un `indice.json` ligero (id, tipo, nombre, fechas y resumen), con un enlace a la ficha completa en su atlas.
- **`migra_desde`:** me parece bien, y el sentido elegido es coherente con la propuesta anterior: el concepto nuevo, que vive en el atlas más reciente, declara de dónde viene.

## 2. Navegación por puntos de vista

Está documentada en el repositorio de filosofía: [`docs/navegacion.md`](https://github.com/caducidad/ATLAS_FILOSOFIA/blob/main/docs/navegacion.md). En resumen:

- **Una sola pantalla, el mapa,** y los modos de navegación son lentes sobre ella: cronológica, temática, libre y el recorrido personal. Se propone además una lente de paralelos entre tradiciones.
- **Cronológica:** línea del tiempo con las épocas como franjas y un **carril por tradición**; las horquillas de fechas se dibujan difuminadas y las cronologías alternativas como barra fantasma. Necesita `fechas`, `contextos` con su `horquilla` y el campo de los carriles.
- **Temática:** selector de temáticas que resalta sus nodos. Necesita `tematicas` y las relaciones `parte_de` entre temáticas.
- **Libre:** la red alrededor de un nodo, con filtros por tipo de relación y por certeza. Necesita las relaciones y el catálogo con su lectura directa e inversa.
- **Recorrido:** sale del progreso, no de los datos.

Para el núcleo, lo único que hay que configurar por atlas es **qué campo define los carriles** de la vista cronológica. En psicología, con archivos por periodo, los carriles podrían ser las corrientes o escuelas, o un solo carril.

## 3. Dónde está el código de la app

**Todavía no hay código de la app.** El repositorio de filosofía contiene los datos del piloto (353 nodos y 518 relaciones), el validador en Python y la documentación. Lo único visual es un boceto estático de cinco pantallas (portada, mapa cronológico, ficha, progreso y retos), hecho como página de prueba fuera del repositorio, que sirvió para aprobar la estética nocturna. No tiene motor: ni carga los datos ni dibuja el grafo.

Esto es una ventaja para el núcleo: el motor puede escribirse desde el principio como código común que lee el `atlas.json` de cada atlas, en lugar de extraerlo después de un código hecho solo para filosofía.

## 4. Extracción

Pendiente de la señal de Juan. Cuando la dé, propongo este orden:

1. `docs/esquema-base.md` con lo común, y `esquema.md` de filosofía reducido a sus extensiones.
2. Catálogo común de relaciones con el campo `entre`, y `atlas.json` de filosofía.
3. Validador del núcleo que lea esquema base más extensiones, comprobado contra los datos actuales de filosofía (deben seguir pasando sin errores).
4. Después, el prototipo del motor ya en el núcleo, probado con los datos de la Antigüedad.

## Decisiones que necesitamos de Juan

1. ¿Los cuatro atlas en el mismo blog o en blogs distintos? Decide si el progreso puede ser uno solo.
2. ¿Renumeramos ahora los ids de relación o mantenemos los rangos por archivo?
3. ¿Dónde se guarda cada puente: en el atlas de origen, como dice el plan, o en el atlas que lo crea?
