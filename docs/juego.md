# El juego de los atlas

Versión 0.1 · 8 de octubre de 2026

Cómo funciona el juego en todos los atlas de la colección. El principio que lo ordena todo: **el juego orienta y premia, nunca bloquea.** Todo el contenido es siempre accesible; el juego solo ayuda a decidir por dónde seguir y a saber cuánto se ha recorrido.

## Niebla de guerra (decidido)

El mapa empieza en penumbra y se enciende a medida que se explora, como unas brasas:

| Visitas a un nodo | Aspecto |
| --- | --- |
| 0 | Sin explorar: contorno discontinuo y apagado |
| 1 | Rojo brasa |
| 2-4 | Naranja |
| 5 o más | Amarillo: lo que más arde es lo más trabajado |

Los umbrales se ajustarán al probar. Abrir la ficha de un nodo cuenta como visita.

## Niveles (decidido)

**Un nivel es una época:** cada nodo de tipo `contexto` (las Cien Escuelas, los presocráticos, la India védica…). Cada nivel pasa por tres estados:

1. **Sin explorar.**
2. **Explorado:** el lector ha visitado todos los autores del círculo 1 de esa época. Llega solo, navegando.
3. **Superado:** el lector ha aprobado el examen de la época. En el mapa, la época se enciende en dorado.

Un atlas cuyos autores no usen `circulo` considera explorada una época cuando se han visitado todos sus autores.

## Examen (decidido; se programa con los retos)

**Opcional.** Nadie lo necesita para leer nada: sirve para quien quiera comprobar lo que sabe y «sellar» un nivel.

- **Diez preguntas** generadas desde los datos de la época; **se aprueba con ocho aciertos**.
- **Se puede repetir sin límite**, y cada vez salen preguntas distintas.
- **Cada fallo lleva a la ficha** donde está la respuesta: el examen también enseña.

**Tipos de pregunta** que salen de los datos sin escribir nada nuevo:

- quién fue maestro de quién (`fue_maestro_de`) y quién escribió qué (`escribio`);
- quién defendió una tesis, a partir de su `enunciado`;
- qué significa un término original (`terminoOriginal` y `traduccion`);
- de quién es una anécdota, con el nombre oculto;
- quién vivió antes, de dos autores (`fechas`);
- qué responde una tradición a una gran pregunta (`responde_a`);
- qué es paralelo a qué en otra tradición (`paralelo_a`), en los atlas que lo usen.

**Reglas para que las preguntas sean justas:**

- Solo se usan relaciones con certeza **D** (documentado) o **P** (probable). Lo conjetural y lo legendario no entra en un examen.
- Las opciones falsas son del mismo tipo y, si es posible, de la misma época o tradición, para que sean plausibles.
- El generador comprueba en el grafo que **ninguna opción falsa sea también correcta** (a «¿quién influyó en Platón?» responden bien varios).
- Las fechas solo se comparan cuando las horquillas no se solapan.
- Cada pregunta tiene un botón «esta pregunta está mal» para avisar al autor del atlas.

Los **retos** sueltos, fuera del examen, usan el mismo generador.

## Grandes preguntas (decidido)

Un tipo de nodo común, `pregunta`: las preguntas de fondo de cada disciplina, como «¿De qué está hecho todo?» en filosofía o «¿Naturaleza o crianza?» en psicología.

- Campo obligatorio: `enunciado`, la pregunta tal como se formula.
- Las respuestas son tesis (u otros nodos) unidos con la relación común `responde_a`: `tesis.agua_principio responde_a pregunta.de_que_esta_hecho_todo`.
- Son una **puerta de entrada** más al mapa, junto a la cronológica, la temática y la libre, con su propia lente: la pregunta en el centro y las respuestas alrededor, agrupadas por el campo de carriles (en filosofía, por tradición).

## Azar

Va en el motor de la app, sin nada nuevo en los datos.

- **«Llévame a algún sitio»** (en el prototipo): lleva a un nodo al azar, con más probabilidad de caer en lo que aún no se ha explorado.
- **Deriva** (propuesto): un paseo de varios pasos siguiendo relaciones al azar.
- **Dos al azar** (propuesto): la app elige dos nodos lejanos y muestra la cadena de relaciones más corta que los une.
- **Lo del día** (propuesto): una pregunta, una anécdota y un paralelo que cambian cada día y son los mismos para todos los lectores. Se calculan con un generador pseudoaleatorio sembrado con la fecha, sin servidor.
- **En los retos y el examen:** el orden de las preguntas y de las opciones.

## Anécdotas coleccionables (decidido)

La caja de anécdotas de un autor se desbloquea como una carta al visitarlo por primera vez. «Mi progreso» muestra la colección.

## Fuera del núcleo del juego

Rangos y logros quedaron fuera por decisión de Juan.

## Datos que añade al progreso

```json
"niveles": {
  "filosofia:contexto.cien_escuelas": { "superado": "2026-10-20", "mejor": 9, "intentos": 2 }
}
```

El estado «explorado» no se guarda: se calcula a partir de las visitas.
