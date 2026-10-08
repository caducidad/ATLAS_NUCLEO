# Plan de la colección Atlas

Versión 0.2 · 8 de octubre de 2026

Este documento recoge las decisiones tomadas y las propuestas pendientes. Las decisiones se cierran aquí; la discusión va en el `buzon/`.

## Decisiones tomadas

1. **Cuatro atlas y un núcleo.** Filosofía, Psicología, Sociología y Antropología, cada uno en su repositorio, más este repositorio con lo común.
2. **Orden de trabajo.**
   1. El Atlas de la Filosofía sigue avanzando, y de él se extrae el núcleo común en dos tiempos:
      - **Ya:** la parte barata y segura, es decir, el esquema base, el catálogo común de relaciones y el validador.
      - **Después de probarlo:** el motor de la app. Se construye primero el prototipo con los datos de Filosofía, escrito pensando en que sirva a todos los atlas, se prueba con lectores reales y solo entonces se declara común. No se diseña un motor para cuatro atlas sin haber visto funcionar uno.
   2. Después, el piloto del Atlas de la Psicología, construido ya sobre el núcleo.
   3. Sociología y Antropología más adelante. Cuando toque, conviene empezar con unos pocos nodos de prueba para comprobar que el esquema común aguanta.
3. **Mismo montaje técnico en todos.** Datos en JSON servidos desde GitHub Pages, app en el navegador (HTML, JavaScript, quizá React) integrada en Blogger, sin servidores ni cuentas.
4. **El Atlas de la Filosofía es punto de partida, no molde.** Se hereda lo que funciona y se cambia lo que en otra disciplina pide otra cosa.
5. **Nombre de la colección:** «Atlas de la…» para todos.
6. **Los cuatro atlas en un solo blog.** No pesa más: cada atlas es una página que carga solo sus datos. Como el navegador guarda el progreso por sitio web, el lector puede tener un solo progreso para toda la colección, con ids prefijados por atlas.
7. **Ids de relación con prefijo por archivo.** Cada archivo declara en su cabecera un `prefijoRelaciones` y numera con él (`cn-0001`, `gr-0001`…), en lugar de rangos numéricos que acaban agotándose. Desde otro atlas se citan con el prefijo del atlas: `filosofia:gr-0001`. Ya aplicado en Filosofía.
8. **Cada puente lo guarda el atlas que lo crea,** en su propio archivo de puentes. El núcleo no guarda contenido de ningún atlas: solo las reglas de los puentes y, si hace falta, un índice de todos ellos generado automáticamente, que nadie edita a mano.
9. **Un responsable del núcleo:** la conversación del Atlas de la Filosofía, que conoce el esquema y los datos. Los demás atlas proponen cambios en el buzón y Juan decide aquí.
10. **Un atlas cada vez y pocos puentes al principio,** solo los más valiosos. El rigor del contenido (fechas, fuentes, citas comprobadas) no se rebaja para ir más rápido.

## Lo que el núcleo hereda del Atlas de la Filosofía

Ya probado en el piloto de la Antigüedad (353 nodos, 518 relaciones) y documentado en su `docs/esquema.md`:

- Todo es un nodo, distinguido por `tipo`.
- Clasificar no es relacionar: contextos, temáticas y escuelas como listas dentro del nodo.
- Cada relación se guarda una sola vez y la app calcula el inverso.
- Ids `tipo.nombre` globales; los datos se reparten en varios archivos que se cargan y se unen al arrancar.
- Fechas en horquilla, historicidad y certeza de cada relación como campos obligatorios.
- Dos capas de texto (`resumen` y `profundizacion`) con enlaces `[[id|texto]]`.
- Anécdotas con fuente y fiabilidad.
- Progreso del usuario separado de los datos, en el navegador, exportable.
- Juego que orienta sin bloquear: niebla de guerra, retos, misiones, anécdotas coleccionables.
- Validador en Python sin dependencias.

## Lo que hay que generalizar para que sirva a todos los atlas

Propuestas revisadas desde el Atlas de la Filosofía (ver `buzon/2026-10-08-02-filosofia-psicologia-respuesta-arranque-del-nucleo.md`); se cierran al hacer la extracción:

1. **Tipos de nodo extensibles.** Un conjunto común (autor, obra, concepto, tesis, escuela, contexto, temática) y la posibilidad de que cada atlas declare tipos propios con sus campos (por ejemplo `experimento` en psicología).
2. **Catálogo de relaciones en dos capas.** Las comunes en el núcleo y las propias en cada atlas.
3. **`tradicion` deja de ser universal.** En filosofía organiza el contenido; en psicología, sociología y antropología, disciplinas modernas y sobre todo occidentales, apenas sirve. Cada atlas declara sus ejes de organización.
4. **Temáticas por atlas.** Las 14 temáticas actuales son de filosofía; cada atlas tiene las suyas.
5. **Ids de relación sin choques entre atlas.** Decidido: ver la decisión 7.
6. **Configuración por atlas** para el motor: nombre, lista de archivos, colores, tipos y relaciones propios.
7. **Formato del progreso** con un campo `atlas`, para que un lector pueda tener progreso en varios.
8. **Retos ampliables.** Cada atlas puede añadir tipos de reto propios (ver psicología, abajo).
9. **Reglas editoriales comunes.** Pasan al núcleo la Guía de redacción (ningún nombre propio sin enlazar o explicar, claridad antes que brevedad, referencias legibles), las reglas de las imágenes y la escala de fiabilidad de las anécdotas, redactada en términos generales.

## Puentes entre atlas

Propuesta:

- **Referencia con prefijo.** Dentro de un atlas los ids van sin prefijo; para apuntar a otro atlas se antepone su nombre: `filosofia:autor.descartes`, `sociologia:autor.durkheim`.
- **Cada figura tiene un atlas «de casa».** Durkheim no tiene dos fichas: vive en un atlas y los demás lo referencian. Pendiente decidir el criterio; Filosofía propone la disciplina en la que se estudia su obra principal, con Juan como árbitro.
- **Cada puente se guarda una sola vez,** en el atlas que lo crea (decisión 8). El validador comprueba los ids externos cuando el otro atlas está disponible y, si no, avisa sin dar error.
- **Fichas de otros atlas sin cargarlos enteros** (propuesta): cada atlas publica un índice ligero de sus nodos (id, tipo, nombre, fechas y resumen) para que los demás puedan mostrarlos.
- **Relación propia de los puentes:** algo como `migra_desde` («concepto que pasa de una disciplina a otra»), además de las relaciones comunes que ya cruzan sin problema (`influyo_en`, `critica`, `desarrolla`…).

## Atlas de la Psicología: lo hablado hasta ahora

Para que el núcleo lo tenga en cuenta desde el principio:

- **Entidades:** autores, corrientes o escuelas, conceptos y teorías, épocas o contextos y, como tipo propio, **experimentos y estudios**.
- **Relaciones clave:** pertenece a una corriente (clasificación), formula, se opone a, influye en, maestro-discípulo (ya existe en filosofía) y **`pone_a_prueba`** (experimento → teoría o concepto; «demuestra» es demasiado fuerte), más **`replica`** entre experimentos.
- **Aparcadas para más adelante:** reformula o critica, nace como reacción a un contexto, concepto que se aplica a un trastorno o a una terapia (el lado clínico).
- **Campos del experimento:** investigadores, año, lugar, diseño, muestra, resultado, estado de replicación y cuestiones éticas.
- **Segunda certeza: el estado de la evidencia.** Además de si una relación está documentada, en psicología importa si una teoría o un hallazgo está consolidado, en debate, no replicado o superado. La crisis de replicación lo convierte en un contenido didáctico de primer orden.
- **Archivos por periodo,** no por tradición ni por corriente: precursores filosóficos y fisiológicos, fundación (desde 1879), grandes escuelas, revolución cognitiva, psicología contemporánea.
- **Temáticas:** percepción, memoria, aprendizaje, emoción y motivación, desarrollo, personalidad, psicología social, psicopatología, psicobiología… (por cerrar).
- **Reto propio: «predice el resultado».** Antes de ver un experimento, el lector apuesta qué pasó (en Milgram casi todo el mundo falla).
- **Imágenes:** muchas fotos de figuras del siglo XX todavía tienen derechos del fotógrafo; habrá menos material libre que en la Antigüedad.

## Resuelto

- **La navegación desde distintos puntos de vista** está documentada en [`docs/navegacion.md`](https://github.com/caducidad/ATLAS_FILOSOFIA/blob/main/docs/navegacion.md) del Atlas de la Filosofía. Para el núcleo, lo único que cambia por atlas es qué campo define los carriles de la vista cronológica.
- **El código de la app** todavía no existe: hay datos, validador, documentación y un boceto visual estático. El motor se escribirá directamente pensando en la colección (decisión 2).
