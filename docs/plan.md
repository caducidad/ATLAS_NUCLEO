# Plan de la colección Atlas

Versión 0.1 · 8 de octubre de 2026

Este documento recoge las decisiones tomadas y las propuestas pendientes. Las decisiones se cierran aquí; la discusión va en el `buzon/`.

## Decisiones tomadas

1. **Cuatro atlas y un núcleo.** Filosofía, Psicología, Sociología y Antropología, cada uno en su repositorio, más este repositorio con lo común.
2. **Orden de trabajo.**
   1. El Atlas de la Filosofía sigue avanzando, y de él se extrae el núcleo común.
   2. Después, el piloto del Atlas de la Psicología, construido ya sobre el núcleo.
   3. Sociología y Antropología más adelante. Cuando toque, conviene empezar con unos pocos nodos de prueba para comprobar que el esquema común aguanta.
3. **Mismo montaje técnico en todos.** Datos en JSON servidos desde GitHub Pages, app en el navegador (HTML, JavaScript, quizá React) integrada en Blogger, sin servidores ni cuentas.
4. **El Atlas de la Filosofía es punto de partida, no molde.** Se hereda lo que funciona y se cambia lo que en otra disciplina pide otra cosa.
5. **Nombre de la colección:** «Atlas de la…» para todos.

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

Propuestas, pendientes de revisar desde el Atlas de la Filosofía:

1. **Tipos de nodo extensibles.** Un conjunto común (autor, obra, concepto, tesis, escuela, contexto, temática) y la posibilidad de que cada atlas declare tipos propios con sus campos (por ejemplo `experimento` en psicología).
2. **Catálogo de relaciones en dos capas.** Las comunes en el núcleo y las propias en cada atlas.
3. **`tradicion` deja de ser universal.** En filosofía organiza el contenido; en psicología, sociología y antropología, disciplinas modernas y sobre todo occidentales, apenas sirve. Cada atlas declara sus ejes de organización.
4. **Temáticas por atlas.** Las 14 temáticas actuales son de filosofía; cada atlas tiene las suyas.
5. **Ids de relación sin choques entre atlas.** Hoy cada archivo usa un rango (`r0001`–`r0999`…). Con varios atlas hace falta que sean únicos por atlas y se distingan con el prefijo del atlas.
6. **Configuración por atlas** para el motor: nombre, lista de archivos, colores, tipos y relaciones propios.
7. **Formato del progreso** con un campo `atlas`, para que un lector pueda tener progreso en varios.
8. **Retos ampliables.** Cada atlas puede añadir tipos de reto propios (ver psicología, abajo).

## Puentes entre atlas

Propuesta:

- **Referencia con prefijo.** Dentro de un atlas los ids van sin prefijo; para apuntar a otro atlas se antepone su nombre: `filosofia:autor.descartes`, `sociologia:autor.durkheim`.
- **Cada figura tiene un atlas «de casa».** Durkheim no tiene dos fichas: vive en un atlas y los demás lo referencian. Pendiente decidir el criterio (¿la disciplina con la que más se le identifica?).
- **Cada puente se guarda una sola vez,** como cualquier relación, en el archivo del nodo de origen. El validador comprueba los ids externos cuando el otro atlas está disponible y, si no, avisa sin dar error.
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

## Pendiente de conocer

- **La navegación desde distintos puntos de vista** del Atlas de la Filosofía: no está en su `docs/esquema.md` y debería documentarse, porque el núcleo tendrá que soportarla.
- **El código de la app:** dónde está y en qué estado, para decidir qué pasa al núcleo.
