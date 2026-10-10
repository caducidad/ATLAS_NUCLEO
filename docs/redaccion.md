# Cómo se redactan las fichas

Versión 0.1 · 10 de octubre de 2026

Procedimiento que sigue el Atlas de la Filosofía y que se propone para toda la colección. Complementa la Guía de redacción de [`esquema-base.md`](esquema-base.md), que dice cómo debe quedar cada texto; este documento dice cómo se llega a él.

## 1. Antes de escribir

- **Una investigación previa por bloque** (en filosofía, un informe de la Antigüedad por tradiciones): qué entra, qué figuras forman el canon, qué fechas y debates hay, y una bibliografía.
- **Verificar la bibliografía** antes de usarla: editorial, traductor, año e ISBN contrastados con los catálogos (editoriales, Biblioteca Nacional, Dialnet). Lo que no se pueda confirmar se marca como no verificado.
- **Revisar las fechas** de cada figura del canon contra varias obras de referencia, anotar las contradicciones y señalar los debates abiertos que necesitarían un especialista. Las fechas inciertas se guardan como horquillas, nunca como un número.

## 2. Orden de trabajo de cada tanda

Una tanda es un bloque coherente (una tradición, un periodo). Se redacta por partes y después se une:

1. **Épocas y escuelas**, porque los demás nodos se clasifican en ellas.
2. **Autores del círculo 1**, con resumen, profundización y anécdotas. Luego, los de los círculos 2 y 3 que hagan falta.
3. **Obras, conceptos y tesis** que los autores ya mencionan en sus textos. Hay que crear todos los nodos enlazados.
4. **Relaciones**, al final, cuando todos los nodos existen: maestros, obras, influencias con su fuente, y los paralelos con otras tradiciones con su eje de comparación.

Dentro de cada ficha: primero el **resumen** (dos o tres frases que entienda cualquiera), después la **profundización** y por último las **anécdotas**, cada una con su referencia y su fiabilidad.

## 3. Comprobaciones antes de subir

1. **Validador** (`herramientas/validar.py`): sin errores.
2. **Nombres sin enlazar** (`herramientas/revisar_nombres.py`): revisar a mano, empezando por los que se repiten en varias fichas.
   - Todo nombre propio va enlazado o explicado en la misma frase («el historiador griego Heródoto»).
   - Si aparece en varias fichas, merece ficha propia, aunque sea mínima. En Grecia y Roma así nacieron Alejandro Magno, Anaxímenes, Antístenes, Jenofonte, Arcesilao y Carnéades.
   - Los autores citados solo en una referencia también se explican («el escritor satírico Luciano de Samósata»).
3. **Relectura** de una muestra de fichas en voz alta: si una frase no se entiende sin conocer la fuente, se reescribe.

## 4. Revisión de Juan

Juan revisa cada tanda leyendo fichas sueltas y señala lo que no se entiende. Sus observaciones se convierten en reglas para todo lo que viene después. La Guía de redacción nació así, de la revisión de la ficha de Han Feizi.

## 5. Errores que ya cometimos

- **Referencias crípticas.** «(Shiji 63 · C)» no dice nada a un lector. Hay que citar con el nombre de la obra enlazado y el capítulo, y la app traduce la letra de fiabilidad a palabras.
- **Nombres sin contexto.** Personas y lugares mencionados de pasada, sin enlace ni explicación.
- **Redacción comprimida.** Frases que resumen tanto que no se entienden («dijo que moriría sin pesar…»). La claridad va antes que la brevedad.
- **Enlaces automáticos que se equivocan.** Al enlazar por script las primeras menciones, «la Upaniṣad» (una concreta) acabó apuntando al corpus entero, y «Uno de ellos» al concepto del Uno. Todo enlace automático se revisa después.
- **Archivos rotos al escribir por partes.** Un campo vacío mal cerrado truncó un archivo entero. Por eso el validador se pasa siempre antes de subir.

## 6. Lo que todavía no hacemos bien

Conviene saberlo para no confiarse:

- **Muchas citas de anécdotas se escribieron de memoria** (pasajes de Diógenes Laercio, Plutarco, Tácito, Plinio…). Están marcadas con su fiabilidad, pero aún no se han cotejado una por una con las ediciones. Es un trabajo pendiente antes de publicar en serio.
- **Las fechas de Grecia y Roma y las del Próximo Oriente** no han pasado todavía por la revisión que sí tuvieron las de India y China.
- **El juicio de un especialista** no lo sustituye ninguna de estas comprobaciones: los debates abiertos se señalan para que alguien que domine el campo pueda revisarlos.

## Para psicología, en particular

- **Estado de la evidencia:** cada estado lleva su `notaEvidencia`, con la fuente de la réplica o de la crítica, y fechada. Es el equivalente de las fechas revisadas en filosofía.
- **Las fuentes modernas son verificables:** artículos con DOI, réplicas publicadas. Es más fácil que en la Antigüedad citar exactamente, y por tanto más exigible.
