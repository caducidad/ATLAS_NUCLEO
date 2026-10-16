# Cómo se redactan las fichas

Versión 0.1 · 10 de octubre de 2026

Procedimiento que sigue el Atlas de la Filosofía y que se propone para toda la colección. Complementa la Guía de redacción de [`esquema-base.md`](esquema-base.md), que dice cómo debe quedar cada texto; este documento dice cómo se llega a él.

## 1. Antes de escribir

- **Una investigación previa por bloque** (en filosofía, un informe de la Antigüedad por tradiciones): qué entra, qué figuras forman el canon, qué fechas y debates hay, y una bibliografía.
- **Verificar la bibliografía** antes de usarla: editorial, traductor, año e ISBN contrastados con los catálogos (editoriales, Biblioteca Nacional, Dialnet). Lo que no se pueda confirmar se marca como no verificado.
- **Revisar las fechas** de cada figura del canon contra varias obras de referencia, anotar las contradicciones y señalar los debates abiertos que necesitarían un especialista. Las fechas inciertas se guardan como horquillas, nunca como un número.

## 2. Dónde va cada cosa

Antes de escribir una tanda se decide en qué archivo irá. La regla común:

- **Un archivo de datos por tanda:** una tradición y una época en filosofía, un periodo en psicología. Cada atlas lista sus archivos y lo que contienen en su `docs/esquema.md`.
- **Lo transversal, en archivos propios:** temáticas, grandes preguntas.
- **Cada relación, en el archivo de la tanda que la crea,** aunque una a nodos de dos archivos. Se guarda una sola vez y el archivo más antiguo no se toca.
- **Un prefijo de relaciones por archivo,** declarado en su cabecera (`prefijoRelaciones`).

## 3. Orden de trabajo de cada tanda

Una tanda es un bloque coherente (una tradición, un periodo). Se redacta por partes y después se une:

1. **Épocas y escuelas**, porque los demás nodos se clasifican en ellas.
2. **Autores del círculo 1**, con resumen, profundización y anécdotas. Luego, los de los círculos 2 y 3 que hagan falta.
3. **Obras, conceptos y tesis** que los autores ya mencionan en sus textos. Hay que crear todos los nodos enlazados.
4. **Relaciones**, al final, cuando todos los nodos existen: maestros, obras, influencias con su fuente, y los paralelos con otras tradiciones con su eje de comparación.

Dentro de cada ficha: primero el **resumen** (dos o tres frases que entienda cualquiera), después la **profundización** y por último las **anécdotas**, cada una con su referencia y su fiabilidad.

## 4. Comprobaciones antes de subir

1. **Validador** (`herramientas/validar.py`): sin errores.
2. **Nombres sin enlazar** (`herramientas/revisar_nombres.py`): revisar a mano, empezando por los que se repiten en varias fichas.
   - Todo nombre propio va enlazado o explicado en la misma frase («el historiador griego Heródoto»).
   - Si aparece en varias fichas, merece ficha propia, aunque sea mínima. En Grecia y Roma así nacieron Alejandro Magno, Anaxímenes, Antístenes, Jenofonte, Arcesilao y Carnéades.
   - Los autores citados solo en una referencia también se explican («el escritor satírico Luciano de Samósata»).
3. **Para saber más e imágenes,** en la revisión de cada ficha: los enlaces a fuentes abiertas, empezando por las de español, y la imagen con su licencia comprobada en su página de origen. Las mismas fuentes sirven para cotejar fechas y citas.
4. **Relectura** de una muestra de fichas en voz alta: si una frase no se entiende sin conocer la fuente, se reescribe.

## 5. Revisión de Juan

Juan revisa cada tanda leyendo fichas sueltas y señala lo que no se entiende. Sus observaciones se convierten en reglas para todo lo que viene después. La Guía de redacción nació así, de la revisión de la ficha de Han Feizi.

## 6. Errores que ya cometimos

- **Referencias crípticas.** «(Shiji 63 · C)» no dice nada a un lector. Hay que citar con el nombre de la obra enlazado y el capítulo, y la app traduce la letra de fiabilidad a palabras.
- **Nombres sin contexto.** Personas y lugares mencionados de pasada, sin enlace ni explicación.
- **Redacción comprimida.** Frases que resumen tanto que no se entienden («dijo que moriría sin pesar…»). La claridad va antes que la brevedad.
- **Enlaces automáticos que se equivocan.** Al enlazar por script las primeras menciones, «la Upaniṣad» (una concreta) acabó apuntando al corpus entero, y «Uno de ellos» al concepto del Uno. Todo enlace automático se revisa después.
- **Archivos rotos al escribir por partes.** Un campo vacío mal cerrado truncó un archivo entero. Por eso el validador se pasa siempre antes de subir.

## 7. Lo que todavía no hacemos bien

Conviene saberlo para no confiarse:

- **Muchas citas de anécdotas se escribieron de memoria.** En filosofía ya se han cotejado con el texto las de Diógenes Laercio de los autores principales, y el resto de esos autores se ha revisado sin abrir el texto (registro en `docs/revision.md` del Atlas de la Filosofía). Faltan las demás, sobre todo las chinas e indias y las de los círculos 2 y 3.
- **No todas las fuentes se dejan leer automáticamente.** El Chinese Text Project lo prohíbe expresamente y Wikimedia limita las consultas; se respetan esas condiciones y se coteja a mano o con otras ediciones abiertas.
- **Las fechas** ya están revisadas en las cuatro tradiciones de filosofía.
- **El juicio de un especialista** no lo sustituye ninguna de estas comprobaciones: los debates abiertos se señalan para que alguien que domine el campo pueda revisarlos.

## Para psicología, en particular

- **Estado de la evidencia:** cada estado lleva su `notaEvidencia`, con la fuente de la réplica o de la crítica, y fechada. Es el equivalente de las fechas revisadas en filosofía.
- **Las fuentes modernas son verificables:** artículos con DOI, réplicas publicadas. Es más fácil que en la Antigüedad citar exactamente, y por tanto más exigible.
