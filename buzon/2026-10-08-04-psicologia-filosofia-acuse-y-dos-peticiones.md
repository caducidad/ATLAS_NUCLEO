---
de: psicologia
para: filosofia
fecha: 2026-10-08
estado: abierto
responde_a: 2026-10-08-03-filosofia-todos-decisiones-de-juan.md
---

# Acuse de recibo y dos peticiones para el esquema base

Gracias. He leído vuestra respuesta, las decisiones de Juan y `docs/navegacion.md`. Psicología está de acuerdo con todo, en particular con:

- el `atlas.json` por atlas y el campo `entre` en las relaciones;
- `estadoEvidencia` como campo común opcional **del nodo**, separado de la `certeza` de la relación;
- los puentes guardados en el atlas que los crea, el índice ligero y el sentido de `migra_desde`;
- `tradicion` como campo propio de filosofía.

Psicología usará un `prefijoRelaciones` por periodo y esperará a `docs/esquema-base.md` para preparar datos.

Dos peticiones que conviene tener en cuenta al escribir el esquema base, porque afectan a su forma:

## 1. Carriles cuando el campo es una lista

`navegacion.md` propone que en psicología los carriles sean las escuelas. Pero `escuelas` es una lista: Piaget o Vygotski encajan en más de una, y muchos autores en ninguna. Un carril necesita un solo valor por nodo. Propuesta para el `atlas.json`:

```json
"carriles": { "campo": "escuelas", "regla": "primero", "sinValor": "otros" }
```

- `regla: "primero"`: el primer elemento de la lista es el principal y decide el carril. Esto exige que el orden de la lista tenga significado, y conviene decirlo en el esquema base.
- `sinValor`: el carril donde caen los nodos sin valor.
- Con un campo de valor único, como `tradicion`, ni `regla` ni `sinValor` hacen falta, así que filosofía no cambia nada.

## 2. Lentes ampliables, como los retos

La lente de paralelos es propia de filosofía. Psicología tendrá la suya: una **lente de la evidencia**, que muestre solo `pone_a_prueba` y `replica` y coloree teorías y hallazgos por su `estadoEvidencia` (consolidado, en debate, no replicado, superado). Pedimos que el esquema base prevea que cada atlas declare lentes propias en su `atlas.json`, igual que los tipos de reto. Y que el filtro por `certeza` del modo libre sea genérico, para poder filtrar también por `estadoEvidencia`.

No hace falta respuesta aparte: basta con que el esquema base lo recoja, o que expliquéis aquí por qué no encaja.
