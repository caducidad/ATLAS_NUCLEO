# Atlas · núcleo común

Pieza compartida de la colección **Atlas**: mapas interactivos de disciplinas en los que autores, obras, conceptos y tesis forman una red navegable que se explora como un juego.

**Autor:** Juan Domínguez Gallego

> Estado: en desarrollo. Ya están el esquema base, el catálogo común de relaciones y el validador, extraídos del Atlas de la Filosofía. El motor de la app se construirá primero como prototipo con los datos de Filosofía y pasará aquí cuando funcione.

## La colección

| Atlas | Repositorio | Estado |
| --- | --- | --- |
| Atlas de la Filosofía | [ATLAS_FILOSOFIA](https://github.com/caducidad/ATLAS_FILOSOFIA) | Piloto de la Antigüedad con datos completos; ya usa el núcleo |
| Atlas de la Psicología | (pendiente) | Diseño de entidades y relaciones |
| Atlas de la Sociología | (pendiente) | Idea |
| Atlas de la Antropología | (pendiente) | Idea |

Las cuatro disciplinas comparten tronco y figuras (Durkheim, G. H. Mead, William James, Freud, Lévi-Strauss…), así que los atlas se enlazan entre sí mediante **puentes**.

## Qué va en el núcleo y qué no

**En el núcleo:** lo que es igual en todos los atlas.

- El esquema base de nodos y relaciones, y la forma de extenderlo.
- El catálogo de tipos de relación comunes.
- El validador.
- El motor de la app: un solo código que carga cualquier atlas.
- El formato del progreso del usuario.
- Las reglas de los puentes entre atlas.

**En cada atlas:** solo su contenido y sus extensiones (tipos de nodo propios, relaciones propias, temáticas, configuración visual).

## Estructura

```
docs/
  plan.md            Decisiones tomadas y plan de trabajo
  esquema-base.md    Esquema común: nodos, relaciones, textos, imágenes, progreso,
                     Guía de redacción y cómo amplía cada atlas el esquema
esquema/
  base.json          Esquema base legible por máquina
  relaciones.json    Catálogo común de tipos de relación
herramientas/
  validar.py         Validador común: esquema base más el atlas.json de cada atlas
  revisar_nombres.py Ayuda para la regla 1 de la Guía de redacción
ejemplos/
  atlas-minimo/      Atlas de ejemplo con un tipo y relaciones propios
buzon/               Mensajes entre las conversaciones que construyen la colección
  README.md          Cómo funciona el buzón
```

## Validar un atlas

```
python3 herramientas/validar.py RUTA_DEL_ATLAS
python3 herramientas/validar.py RUTA_DEL_ATLAS --con RUTA_DE_OTRO_ATLAS
```

La ruta es la carpeta que contiene el `atlas.json`. Con `--con` se comprueban también los ids de otros atlas. Solo necesita Python 3.

## Licencias

- **Textos y datos** (`docs/`, `buzon/` y catálogos comunes): [CC BY-SA 4.0](LICENSE-DATOS.md).
- **Código**: [licencia MIT](LICENSE).
