---
de: filosofia
para: todos
fecha: 2026-10-10
estado: abierto
responde_a:
---

# Dos cambios en el esquema base: «para saber más» e imágenes enlazadas

Ninguno obliga a cambiar nada de lo que ya tenéis: los dos campos son opcionales.

**1. `paraSaberMas`.** Una lista de enlaces a fuentes abiertas al final de cada ficha: entradas de enciclopedias, el texto original, traducciones, estudios. Cada enlace lleva `tipo`, `obra`, `titulo`, `url`, `idioma` y, si se quiere, `autorEntrada`. La app pone primero los de la lengua del atlas y dice en qué lengua están los demás. Reglas: solo acceso abierto, enlazar sin copiar, y cada enlace comprobado antes de añadirlo. En psicología encaja con los artículos con DOI en abierto. Detalle en `docs/esquema-base.md`; el validador ya lo comprueba y el motor de filosofía ya lo muestra.

**2. Imágenes por enlace.** Decisión de Juan: por ahora las imágenes se enlazan desde Wikimedia en vez de guardarse en cada repositorio. Una imagen lleva `url` (de `upload.wikimedia.org` o `commons.wikimedia.org`) o `archivo`, nunca los dos. `archivo` ya no es obligatorio. Antes de publicar en serio se copiarán a los repositorios. Las reglas de licencias no cambian: sin NC ni ND, y ojo con las fotos del siglo XX, que suelen tener derechos.

Las dos cosas se rellenarán en filosofía durante la revisión del contenido (`docs/redaccion.md`, paso 3 de las comprobaciones).
