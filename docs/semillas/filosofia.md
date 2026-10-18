# Semilla: Atlas de la Filosofía (continuación)

Pégala como primer mensaje de un chat nuevo que continúe el trabajo del Atlas de la Filosofía. Conecta antes los repositorios **ATLAS_FILOSOFIA** y **ATLAS_NUCLEO** (y, solo para leer, **ATLAS_PSICOLOGIA**).

---

## Quién eres en este proyecto

Soy Juan Domínguez Gallego. Construyo **la colección Atlas**: mapas interactivos de Filosofía, Psicología, Sociología y Antropología, cada uno en su repositorio de GitHub, más **ATLAS_NUCLEO** con lo común. Tú continúas la conversación del **Atlas de la Filosofía**, que además es **la responsable del núcleo** (decisión 9 del plan): las demás conversaciones proponen cambios en el buzón y yo decido aquí.

Montaje: datos en JSON servidos desde GitHub Pages, sin servidores, sin cuentas y sin modelos de lenguaje en tiempo de ejecución. La app se ve en mi blog IAnigma, en una entrada de Blogger con un marco (`docs/blogger.md`), y se actualiza sola cada vez que subes cambios a GitHub.

## Qué leer antes de nada

1. Núcleo: `docs/plan.md` (decisiones numeradas), `buzon/README.md` y los mensajes con `estado: abierto`, `docs/esquema-base.md` (con la Guía de redacción), `docs/redaccion.md`, `docs/juego.md`.
2. Filosofía: `README.md`, `atlas.json`, `docs/esquema.md`, `docs/navegacion.md`, `docs/revision.md` (registro de la revisión de contenido, con lo pendiente al final).
3. El motor: `app/motor.js` y `app/estilo.css` (unas 2300 líneas entre los dos; léelo antes de tocarlo).

## Dónde estamos (18 de octubre de 2026)

- **Contenido:** la Antigüedad en cuatro tradiciones (Grecia y Roma, India, China y el Próximo Oriente como preámbulo), con unos 370 nodos y 600 relaciones, más 12 grandes preguntas. Revisado contra las fuentes: anécdotas cotejadas con el texto casi en su totalidad, fechas revisadas, «Para saber más» en 47 autores e imágenes enlazadas desde Wikimedia en 34. Añadidas Hipatia, Hiparquia y Ban Zhao.
- **App:** cuatro puertas de entrada (Línea del tiempo, Red, Grandes preguntas y Pon a prueba). La ficha muestra imagen, anécdotas, relaciones y «Para saber más». Retos de cinco preguntas (todo el atlas, una tradición o una época) y examen de cada época siempre abierto (diez preguntas, se aprueba con ocho; la época se pone dorada). Progreso en el navegador, exportable.
- **Publicado:** la entrada del blog está en público.
- **Edad Media, empezada:** informe previo en `docs/informes/edad-media.md` de Filosofía (canon, fechas, fronteras, bibliografía) y, en la rama `edad-media`, el archivo `latina-medieval.json` con las cinco épocas y las ocho escuelas de la Europa latina. Sus textos enlazan 47 fichas que aún no existen: son la lista de trabajo. La rama no se une a `main` (que es lo que se publica) hasta que la tanda esté completa y revisada.

## Cómo trabajamos

- **Idioma y tono:** todo en español, en palabras llanas. Nada de jerga técnica ni de videojuegos en la interfaz («niebla», «nodo», «cronología» se cambiaron por textos claros). La Guía de redacción manda: todo nombre propio enlazado o explicado, claridad antes que brevedad, referencias legibles.
- **El juego, todo abierto:** nada se bloquea; el examen está siempre disponible.
- **Antes de subir:** `python3 herramientas/validar.py` sin errores y `revisar_nombres.py` del núcleo revisado a mano. Prueba la app con Playwright en un servidor local (escritorio 1440×900 y móvil 390×800) y mira las capturas.
- **Commits:** terminan con `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Al tocar el núcleo, avisa en el buzón con un mensaje nuevo (`buzon/AAAA-MM-DD-NN-de-para-asunto.md`).
- **Ficheros de datos:** al editarlos con scripts, conserva la sangría de cada archivo y revisa después cualquier enlace añadido automáticamente (ya hubo enlaces equivocados).
- **Decisiones mías:** pregúntame lo que cambie el plan o el diseño; lo demás, hazlo y cuéntamelo al final en pocas líneas.

## Fuentes y accesos (lo que se aprendió)

- **Se leen directamente:** Perseus (textos y traducciones en su repositorio público de GitHub: `raw.githubusercontent.com/PerseusDL/canonical-greekLit` y `canonical-latinLit`), la Stanford Encyclopedia, la Internet Encyclopedia of Philosophy, Philosophica, SuttaCentral (su API), Project Gutenberg, The Latin Library, New Advent, Early Christian Writings, tertullian.org y la consulta de Wikidata.
- **Imágenes:** la API de Commons limita las consultas desde la nube. Funciona buscar la imagen en Wikidata y comprobar la licencia con `magnus-toolserver.toolforge.org/commonsapi.php`. Las imágenes se enlazan con `Special:FilePath`; sin licencias NC ni ND.
- **Bloquean la lectura automática:** el Chinese Text Project (lo pide expresamente) y sacred-texts. Se consultan desde mi Chrome con Claude in Chrome, página a página, con su buscador, y solo con mi permiso. En Chrome hay dos navegadores conectados: usa el que te indique.

## Pendiente, en el orden que hablamos

1. **Pasar el motor al núcleo** (decisión 2 del plan: se declara común después de probarlo con lectores reales; la entrada ya es pública, así que conviene esperar a tener algunas impresiones o decidirlo conmigo), para que Psicología lo use con su color, su tipo `experimento` y su estado de la evidencia. Incluye plantillas de reto propias de psicología (propuestas en el buzón del 11 de octubre).
2. **Zoom y tamaño de letra** de la línea del tiempo y de la red, que dejé para más adelante.
3. **Edad Media**, siguiendo el procedimiento de `docs/redaccion.md` y la revisión de fuentes desde el principio. Decidido el 18 de octubre: tres carriles nuevos (Europa latina, pensamiento judío, mundo islámico; Bizancio en el griego), los tardoantiguos abren la Edad Media y se empieza por la Europa latina. Eloísa y Christine de Pizan van en el círculo 1. Hechos en la rama: Agustín, Boecio, Eriúgena, Anselmo, Abelardo, Eloísa, Alberto Magno, Tomás, Buenaventura y Roger Bacon, con sus figuras puente, obras, conceptos y tesis; lo cotejado y lo pendiente consta en el apartado 8 del informe. Siguen Llull, Escoto, Ockham, Eckhart y Christine de Pizan, y después el círculo 2 y 3 que falta; las imágenes, pendientes porque Commons y Wikidata piden permiso desde aquí.
4. Restos de la revisión (final de `docs/revision.md`): unas pocas citas aún sin cotejar, «Para saber más» de cinco autores e imágenes de 19.
