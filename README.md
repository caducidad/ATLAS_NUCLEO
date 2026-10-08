# Atlas · núcleo común

Pieza compartida de la colección **Atlas**: mapas interactivos de disciplinas en los que autores, obras, conceptos y tesis forman una red navegable que se explora como un juego.

**Autor:** Juan Domínguez Gallego

> Estado: en planificación. De momento el repositorio contiene el plan de trabajo y el buzón de coordinación. El esquema común, el validador y el motor de la app se irán extrayendo del Atlas de la Filosofía.

## La colección

| Atlas | Repositorio | Estado |
| --- | --- | --- |
| Atlas de la Filosofía | [ATLAS_FILOSOFIA](https://github.com/caducidad/ATLAS_FILOSOFIA) | Piloto de la Antigüedad con datos completos |
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
  plan.md      Decisiones tomadas y plan de trabajo
buzon/         Mensajes entre las conversaciones que construyen la colección
  README.md    Cómo funciona el buzón
```

## Licencias

- **Textos y datos** (`docs/`, `buzon/` y catálogos comunes): [CC BY-SA 4.0](LICENSE-DATOS.md).
- **Código**: [licencia MIT](LICENSE).
