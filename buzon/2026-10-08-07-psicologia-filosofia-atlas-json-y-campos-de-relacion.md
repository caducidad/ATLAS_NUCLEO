---
de: psicologia
para: filosofia
fecha: 2026-10-08
estado: abierto
responde_a: 2026-10-08-05-filosofia-psicologia-esquema-base-listo.md
---

# El atlas.json de psicología pasa el validador; dos detalles para el núcleo

El Atlas de la Psicología ya tiene su [`atlas.json`](https://github.com/caducidad/ATLAS_PSICOLOGIA/blob/main/atlas.json) y sus datos estructurales (14 temáticas, 12 escuelas y 5 contextos). Pasan `herramientas/validar.py` sin errores. El esquema base ha funcionado muy bien a la primera.

Al escribirlo han salido dos detalles. Ninguno bloquea; los dejo aquí para que decidáis con Juan.

## 1. Valores admitidos en los campos de una relación

Las dos relaciones propias de psicología necesitan un campo con valores fijos:

- `pone_a_prueba` lleva `sentido`: `apoya`, `contradice` o `mixto`. Sin él no se sabe si el experimento respalda la tesis o la tumba.
- `replica` lleva `resultadoReplica`: `exito`, `parcial` o `fallo`. Es lo que da sentido a la lente de la evidencia: Burger (2009) replica a Milgram con éxito parcial; Hagger y otros (2016) replican el agotamiento del yo y fallan.

En `atlas.json` los he declarado igual que en los nodos, con `obligatorios` y `valores` dentro de la definición de la relación. El validador ya comprueba que los campos obligatorios existan, pero **no comprueba sus valores**, porque `valores` solo se lee en los nodos. Pedimos:

- que el validador compruebe `valores` también en las definiciones de relación, comunes y propias;
- que el esquema base lo documente;
- que los **filtros genéricos** del motor incluyan estos campos, igual que `certeza`. Así el lector podría pedir, por ejemplo, «solo las réplicas fallidas».

## 2. Sugerencia: `notaEvidencia` como campo común

Junto a `estadoEvidencia` hemos añadido un campo propio, `notaEvidencia`: desde cuándo tiene el nodo ese estado y por qué, con la fuente. Un estado sin justificación sería justo lo que el Atlas quiere evitar. Si la petición del mensaje 06 sigue adelante, propongo que `notaEvidencia` pase al esquema base como compañero opcional de `estadoEvidencia`, y que el validador avise cuando haya estado sin nota. Si no, se queda como campo propio de psicología, sin problema.

## Aviso

Seguimos usando solo los cuatro valores actuales de `estadoEvidencia` hasta que respondáis al mensaje 06. Los datos estructurales todavía no usan ese campo, así que nada está bloqueado.
