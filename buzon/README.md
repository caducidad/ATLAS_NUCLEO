# Buzón

La colección se construye con varias conversaciones de Claude a la vez, una por atlas, y ninguna ve lo que hablan las otras. El buzón es el sitio donde se dejan mensajes entre ellas, con Juan como coordinador.

## Al empezar cada sesión

1. Leer los mensajes con `estado: abierto` dirigidos a tu atlas o a `todos`.
2. Leer `docs/plan.md` si ha cambiado desde la última vez.

## Cómo escribir un mensaje

Un archivo por mensaje, que no se edita después salvo para cambiar su estado:

```
buzon/AAAA-MM-DD-NN-de-para-asunto.md
```

- `NN`: número del mensaje en ese día (01, 02…), para que el orden alfabético sea el cronológico.
- `de` y `para`: `filosofia`, `psicologia`, `sociologia`, `antropologia`, `nucleo` o `todos`.

Cabecera de cada mensaje:

```
---
de: psicologia
para: filosofia
fecha: 2026-10-08
estado: abierto
responde_a: (nombre del archivo, si es una respuesta)
---
```

## Estados

- `abierto`: pendiente de leer o de hacer.
- `en_curso`: alguien ha empezado con lo que pide.
- `cerrado`: hecho o descartado. Se indica al final del mensaje, en una línea, qué se hizo y dónde.

Las respuestas van en un mensaje nuevo con `responde_a`, nunca dentro del original. Las decisiones que se cierran pasan a `docs/plan.md`, que es la referencia; el buzón es solo la conversación.
