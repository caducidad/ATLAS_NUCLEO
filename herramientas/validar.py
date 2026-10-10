#!/usr/bin/env python3
"""Validador común de la colección Atlas.

Comprueba los datos de un atlas contra el esquema base del núcleo
(esquema/base.json y esquema/relaciones.json) más las extensiones que
el propio atlas declara en su atlas.json.

Uso:
    python3 herramientas/validar.py RUTA_DEL_ATLAS
    python3 herramientas/validar.py RUTA_DEL_ATLAS --con RUTA_DE_OTRO_ATLAS

RUTA_DEL_ATLAS es la carpeta que contiene atlas.json. Con --con se cargan
otros atlas para comprobar los ids externos (filosofia:autor.platon); sin
ellos, esas referencias solo generan un aviso.

Solo necesita Python 3, sin instalar nada. Termina con código 1 si hay errores.
"""
import argparse
import collections
import copy
import json
import os
import re
import sys

NUCLEO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ENLACE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
REFERENCIA = re.compile(r"\(([^()]*· [^()]*)\)")
ID_NODO = re.compile(r"^[a-z_]+\.[a-z0-9_]+$")
TEMA = ("acento", "acentoClaro", "cielo", "cieloAlto", "panel", "linea")
FORMAS = ("circulo", "cuadrado", "rombo", "triangulo", "estrella", "cruz", "y")


def leer_json(ruta):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- esquema

def cargar_esquema(atlas):
    """Une el esquema base con las extensiones de atlas.json."""
    base = leer_json(os.path.join(NUCLEO, "esquema", "base.json"))
    catalogo = leer_json(os.path.join(NUCLEO, "esquema", "relaciones.json"))["tiposRelacion"]
    errores = []

    tipos = copy.deepcopy(base["tiposNodo"])
    for nombre, definicion in atlas.get("tiposNodo", {}).items():
        destino = tipos.setdefault(nombre, {"obligatorios": []})
        destino["obligatorios"] = destino.get("obligatorios", []) + definicion.get("obligatorios", [])
        destino.setdefault("valores", {}).update(definicion.get("valores", {}))
    for nombre, campos in atlas.get("obligatorios", {}).items():
        if nombre not in tipos:
            errores.append(f"atlas.json: «obligatorios» menciona el tipo desconocido «{nombre}»")
            continue
        tipos[nombre]["obligatorios"] = tipos[nombre].get("obligatorios", []) + campos

    valores_comunes = dict(base["camposComunes"].get("valores", {}))
    for campo, definicion in atlas.get("camposPropios", {}).items():
        if "valores" in definicion:
            valores_comunes[campo] = definicion["valores"]
        for nombre in definicion.get("obligatorioEn", []):
            if nombre not in tipos:
                errores.append(f"atlas.json: «{campo}» es obligatorio en el tipo desconocido «{nombre}»")
                continue
            tipos[nombre]["obligatorios"] = tipos[nombre].get("obligatorios", []) + [campo]

    relaciones = copy.deepcopy(catalogo)
    for nombre, definicion in atlas.get("relaciones", {}).items():
        if nombre in relaciones:
            errores.append(f"atlas.json: la relación «{nombre}» ya existe en el catálogo común")
        relaciones[nombre] = definicion

    return {
        "base": base,
        "tipos": tipos,
        "valoresComunes": valores_comunes,
        "listas": {**base["camposComunes"]["listas"], **atlas.get("listas", {})},
        "textos": base["camposComunes"]["textos"],
        "obligatoriosComunes": base["camposComunes"]["obligatorios"],
        "acompanantes": base["camposComunes"].get("acompanantes", {}),
        "obligatoriosSi": atlas.get("obligatoriosSi", []),
        "relaciones": relaciones,
        "reglas": atlas.get("reglas", []),
    }, errores


# ---------------------------------------------------------------- datos

def cargar_atlas(ruta_atlas):
    atlas = leer_json(os.path.join(ruta_atlas, "atlas.json"))
    nodos, relaciones, cabeceras = [], [], {}
    for relativa in atlas.get("archivos", []):
        datos = leer_json(os.path.join(ruta_atlas, relativa))
        nombre = os.path.basename(relativa)
        cabeceras[nombre] = datos
        for n in datos.get("nodos", []):
            n["_archivo"] = nombre
            nodos.append(n)
        for r in datos.get("relaciones", []):
            r["_archivo"] = nombre
            r["_prefijo"] = datos.get("prefijoRelaciones")
            relaciones.append(r)
    return atlas, nodos, relaciones, cabeceras


def es_externo(id_):
    return ":" in id_


# ---------------------------------------------------------------- comprobaciones

def comprobar_tramo(tramo, etiqueta, errores):
    if not isinstance(tramo, dict) or not all(isinstance(tramo.get(k), int) for k in ("min", "max")):
        errores.append(f"{etiqueta}: debe ser {{\"min\": año, \"max\": año}} con años enteros")
    elif tramo["min"] > tramo["max"]:
        errores.append(f"{etiqueta}: min ({tramo['min']}) es mayor que max ({tramo['max']})")


def comprobar_fechas(i, fechas, esquema, errores):
    regla = esquema["base"]["fechas"]
    if fechas.get("tipo") not in regla["tipo"]:
        errores.append(f"{i}: fechas.tipo debe ser uno de {', '.join(regla['tipo'])}")
    if fechas.get("historicidad") not in regla["historicidad"]:
        errores.append(f"{i}: fechas.historicidad debe ser uno de {', '.join(regla['historicidad'])}")
    tramos = [t for t in regla["tramos"] if t in fechas]
    if not tramos:
        errores.append(f"{i}: fechas sin ningún tramo ({', '.join(regla['tramos'])})")
    for t in tramos:
        comprobar_tramo(fechas[t], f"{i}: fechas.{t}", errores)
    if fechas.get("tipo") == "actividad" and "activo" not in fechas:
        errores.append(f"{i}: fechas de tipo «actividad» sin el tramo «activo»")
    for k, alt in enumerate(fechas.get("alternativas", []), 1):
        if not alt.get("etiqueta"):
            errores.append(f"{i}: la cronología alternativa {k} no tiene etiqueta")
        tramos_alt = [t for t in regla["tramos"] if t in alt]
        if not tramos_alt:
            errores.append(f"{i}: la cronología alternativa {k} no tiene ningún tramo")
        for t in tramos_alt:
            comprobar_tramo(alt[t], f"{i}: alternativa {k}, {t}", errores)


def comprobar_anecdotas(i, texto, esquema, errores):
    letras = "".join(esquema["base"]["fiabilidadAnecdotas"])
    for ref in REFERENCIA.findall(texto):
        if not re.search(rf" · [{letras}]$", ref):
            errores.append(f"{i}: referencia mal formada «({ref})»")
    if not re.search(rf"· [{letras}]\)\.?$", texto.strip()):
        errores.append(f"{i}: la última anécdota no termina con su referencia")


def comprobar_imagenes(i, imagenes, esquema, ruta_atlas, errores):
    regla = esquema["base"]["imagenes"]
    for k, img in enumerate(imagenes, 1):
        etiqueta = f"{i}: imagen {k}"
        for campo in regla["obligatorios"]:
            if not img.get(campo):
                errores.append(f"{etiqueta}: falta «{campo}»")
        if img.get("tipo") and img["tipo"] not in regla["tipos"]:
            errores.append(f"{etiqueta}: tipo desconocido «{img['tipo']}»")
        licencia = img.get("licencia", "")
        if licencia and licencia not in regla["licencias"]:
            errores.append(f"{etiqueta}: licencia «{licencia}» no admitida (se excluyen NC y ND)")
        if licencia in regla["exigenCredito"] and not img.get("credito"):
            errores.append(f"{etiqueta}: la licencia {licencia} exige «credito»")
        if bool(img.get("archivo")) == bool(img.get("url")):
            errores.append(f"{etiqueta}: lleva «archivo» o «url», y solo uno de los dos")
        if img.get("archivo") and not os.path.exists(os.path.join(ruta_atlas, img["archivo"])):
            errores.append(f"{etiqueta}: no existe el archivo {img['archivo']}")
        if img.get("url"):
            m = re.match(r"https://([^/]+)/", img["url"])
            if not m or m.group(1) not in regla.get("hostsUrl", []):
                errores.append(f"{etiqueta}: «url» debe ser https y de {', '.join(regla.get('hostsUrl', []))}")


def comprobar_saber_mas(i, enlaces, esquema, errores):
    regla = esquema["base"]["paraSaberMas"]
    vistos = set()
    for k, e in enumerate(enlaces, 1):
        etiqueta = f"{i}: para saber más {k}"
        for campo in regla["obligatorios"]:
            if not e.get(campo):
                errores.append(f"{etiqueta}: falta «{campo}»")
        if e.get("tipo") and e["tipo"] not in regla["tipos"]:
            errores.append(f"{etiqueta}: tipo desconocido «{e['tipo']}»")
        if e.get("url") and not re.match(r"https?://[^\s/]+\.[^\s/]+(/\S*)?$", e["url"]):
            errores.append(f"{etiqueta}: url mal formada «{e['url']}»")
        if e.get("idioma") and not re.match(r"^[a-z]{2,3}$", e["idioma"]):
            errores.append(f"{etiqueta}: idioma «{e['idioma']}» debe ser un código como es, en, fr")
        if e.get("url") in vistos:
            errores.append(f"{etiqueta}: enlace repetido")
        vistos.add(e.get("url"))


def falta(n, campo):
    return campo not in n or n[campo] is None or n[campo] == ""


def validar(ruta_atlas, otros):
    atlas, nodos, relaciones, cabeceras = cargar_atlas(ruta_atlas)
    esquema, errores = cargar_esquema(atlas)
    avisos = []
    externos_sin_comprobar = set()

    tipo_de = {}
    for otro in otros:
        o_atlas, o_nodos, _, _ = cargar_atlas(otro)
        for n in o_nodos:
            tipo_de[f"{o_atlas['atlas']}:{n['id']}"] = n.get("tipo")
    atlas_cargados = {i.split(":")[0] for i in tipo_de}

    cuenta = collections.Counter(n["id"] for n in nodos)
    for i, veces in cuenta.items():
        if veces > 1:
            errores.append(f"{i}: definido {veces} veces")
    for n in nodos:
        tipo_de[n["id"]] = n.get("tipo")

    def existe(id_, donde, tipo_esperado=None):
        if es_externo(id_):
            if id_.split(":")[0] not in atlas_cargados:
                externos_sin_comprobar.add(id_)
                return
        if id_ not in tipo_de:
            errores.append(f"{donde}: apunta a «{id_}», que no existe")
        elif tipo_esperado and tipo_de[id_] != tipo_esperado:
            errores.append(f"{donde}: «{id_}» debería ser de tipo {tipo_esperado}")

    def comprobar_texto(texto, donde):
        if texto.count("[[") != texto.count("]]"):
            errores.append(f"{donde}: corchetes desparejados")
        for destino in ENLACE.findall(texto):
            existe(destino, f"{donde}, enlace")

    # ---- nodos
    for n in nodos:
        i = n.get("id", "(sin id)")
        tipo = n.get("tipo")
        if tipo not in esquema["tipos"]:
            errores.append(f"{i}: tipo desconocido «{tipo}»")
            continue
        if not ID_NODO.match(i) or not i.startswith(tipo + "."):
            errores.append(f"{i}: el id debe tener la forma {tipo}.nombre, en minúsculas y sin tildes")
        definicion = esquema["tipos"][tipo]
        for campo in esquema["obligatoriosComunes"] + definicion.get("obligatorios", []):
            if falta(n, campo):
                errores.append(f"{i}: falta el campo obligatorio «{campo}»")
        for campo, admitidos in {**esquema["valoresComunes"], **definicion.get("valores", {})}.items():
            if campo in n and n[campo] not in admitidos:
                errores.append(f"{i}: {campo} «{n[campo]}» no admitido ({', '.join(map(str, admitidos))})")
        for condicion in esquema["obligatoriosSi"]:
            if condicion.get("tipo") == tipo and all(n.get(k) == v for k, v in condicion["si"].items()):
                for campo in condicion["campos"]:
                    if falta(n, campo):
                        detalle = ", ".join(f"{k} {v}" for k, v in condicion["si"].items())
                        errores.append(f"{i}: falta «{campo}», obligatorio con {detalle}")
        for campo, tipo_ref in esquema["listas"].items():
            for ref in n.get(campo, []):
                existe(ref, f"{i}: {campo}", tipo_ref)
        for campo in esquema["textos"]:
            if n.get(campo):
                comprobar_texto(n[campo], f"{i}: {campo}")
        if n.get("anecdotas"):
            comprobar_anecdotas(i, n["anecdotas"], esquema, errores)
        if n.get("fechas"):
            comprobar_fechas(i, n["fechas"], esquema, errores)
        if tipo == "contexto" and n.get("horquilla"):
            h = n["horquilla"]
            if not all(isinstance(h.get(k), int) for k in ("inicio", "fin")):
                errores.append(f"{i}: horquilla debe tener «inicio» y «fin» con años enteros")
            elif h["inicio"] > h["fin"]:
                errores.append(f"{i}: la horquilla empieza después de terminar")
        comprobar_imagenes(i, n.get("imagenes", []), esquema, ruta_atlas, errores)
        comprobar_saber_mas(i, n.get("paraSaberMas", []), esquema, errores)

    # ---- relaciones
    for i, veces in collections.Counter(r.get("id") for r in relaciones).items():
        if veces > 1:
            errores.append(f"relación {i}: id repetido")
    prefijos = collections.defaultdict(set)
    for r in relaciones:
        prefijos[r["_prefijo"]].add(r["_archivo"])
    for prefijo, archivos in prefijos.items():
        if not prefijo:
            errores.append(f"{', '.join(sorted(archivos))}: falta «prefijoRelaciones» en la cabecera")
        elif len(archivos) > 1:
            errores.append(f"prefijo de relaciones «{prefijo}» usado en varios archivos: {', '.join(sorted(archivos))}")
    triples = collections.Counter((r.get("origen"), r.get("tipo"), r.get("destino")) for r in relaciones)
    for (o, t, d), veces in triples.items():
        if veces > 1:
            errores.append(f"relación {o} {t} {d}: repetida {veces} veces")

    certezas = esquema["base"]["certezas"]
    conectados = set()
    for r in relaciones:
        rid = r.get("id", "(sin id)")
        if r["_prefijo"] and not re.fullmatch(re.escape(r["_prefijo"]) + r"-\d{4}", rid):
            errores.append(f"{rid}: el id debe tener la forma {r['_prefijo']}-0001 ({r['_archivo']})")
        for extremo in ("origen", "destino"):
            existe(r.get(extremo, ""), f"{rid}: {extremo}")
        definicion = esquema["relaciones"].get(r.get("tipo"))
        if not definicion:
            errores.append(f"{rid}: tipo de relación desconocido «{r.get('tipo')}»")
        else:
            entre = definicion.get("entre")
            to, td = tipo_de.get(r.get("origen")), tipo_de.get(r.get("destino"))
            if entre and to and td and not any(to in o and td in d for o, d in entre):
                errores.append(f"{rid}: «{r['tipo']}» no puede unir {to} → {td}")
            for campo in definicion.get("obligatorios", []):
                if falta(r, campo):
                    errores.append(f"{rid}: «{r['tipo']}» exige el campo «{campo}»")
            for campo, admitidos in definicion.get("valores", {}).items():
                if campo in r and r[campo] not in admitidos:
                    errores.append(f"{rid}: {campo} «{r[campo]}» no admitido ({', '.join(map(str, admitidos))})")
        if r.get("certeza") not in certezas:
            errores.append(f"{rid}: certeza debe ser {', '.join(certezas)}")
        if r.get("nota"):
            comprobar_texto(r["nota"], f"{rid}: nota")
        conectados |= {r.get("origen"), r.get("destino")}

    # ---- reglas propias del atlas
    nodo = {n["id"]: n for n in nodos}
    for regla in esquema["reglas"]:
        if regla.get("regla") == "fuenteSiDifiere":
            campo = regla["campo"]
            for r in relaciones:
                if r.get("tipo") != regla["relacion"] or r.get("fuente"):
                    continue
                a, b = nodo.get(r.get("origen"), {}), nodo.get(r.get("destino"), {})
                if a and b and a.get(campo) != b.get(campo):
                    errores.append(f"{r['id']}: {regla.get('mensaje', 'falta la fuente')}")
        else:
            errores.append(f"atlas.json: regla desconocida «{regla.get('regla')}»")

    # ---- tema y textos
    for clave, valor in atlas.get("tema", {}).items():
        if clave not in TEMA:
            errores.append(f"atlas.json: «tema.{clave}» no existe; se admiten {', '.join(TEMA)}")
        elif not re.fullmatch(r"#[0-9a-fA-F]{6}", str(valor)):
            errores.append(f"atlas.json: «tema.{clave}» debe ser un color como #9cc0ff")
    for clave, valor in atlas.get("textos", {}).items():
        if not isinstance(valor, str) or not valor.strip():
            errores.append(f"atlas.json: el texto «{clave}» está vacío")
    for tipo, definicion in atlas.get("tiposNodo", {}).items():
        if definicion.get("forma") and definicion["forma"] not in FORMAS:
            errores.append(f"atlas.json: forma «{definicion['forma']}» de «{tipo}» no existe; se admiten {', '.join(FORMAS)}")

    # ---- carriles y lentes
    if "carriles" in atlas:
        carriles = atlas["carriles"]
        if isinstance(carriles, str):
            carriles = {"campo": carriles}
        campo = carriles.get("campo")
        valores = [n[campo] for n in nodos if campo and n.get(campo) not in (None, "", [])]
        if not campo:
            errores.append("atlas.json: «carriles» necesita un «campo»")
        elif any(isinstance(v, list) for v in valores) and carriles.get("regla") != "primero":
            errores.append(f"atlas.json: el campo de carriles «{campo}» es una lista; "
                           "hace falta «regla»: «primero» (el primer elemento decide el carril)")
        elif not valores and "sinValor" not in carriles:
            avisos.append(f"el campo de carriles «{campo}» no aparece en ningún nodo")
    for nombre, lente in atlas.get("lentes", {}).items():
        if not lente.get("nombre"):
            errores.append(f"atlas.json: la lente «{nombre}» no tiene «nombre»")
        for rel in lente.get("relaciones", []):
            if rel not in esquema["relaciones"]:
                errores.append(f"atlas.json: la lente «{nombre}» usa la relación desconocida «{rel}»")

    # ---- avisos
    for campo, companero in esquema["acompanantes"].items():
        sin_nota = sorted(n["id"] for n in nodos if n.get(campo) and falta(n, companero))
        if sin_nota:
            avisos.append(f"«{campo}» sin «{companero}» que lo justifique: " + ", ".join(sin_nota))
    deben = set(esquema["base"]["nodosQueDebenRelacionarse"])
    aislados = sorted(n["id"] for n in nodos if n["id"] not in conectados and n.get("tipo") in deben)
    if aislados:
        avisos.append("nodos sin ninguna relación: " + ", ".join(aislados))
    if externos_sin_comprobar:
        avisos.append(f"{len(externos_sin_comprobar)} ids de otros atlas sin comprobar (usa --con): "
                      + ", ".join(sorted(externos_sin_comprobar)))
    return atlas, nodos, relaciones, errores, avisos


def main():
    parser = argparse.ArgumentParser(description="Valida los datos de un atlas de la colección.")
    parser.add_argument("atlas", help="carpeta del atlas (la que contiene atlas.json)")
    parser.add_argument("--con", nargs="*", default=[], help="otros atlas para comprobar ids externos")
    args = parser.parse_args()

    if not os.path.exists(os.path.join(args.atlas, "atlas.json")):
        print(f"No encuentro atlas.json en {args.atlas}")
        return 1
    atlas, nodos, relaciones, errores, avisos = validar(args.atlas, args.con)
    print(f"{atlas.get('nombre', atlas.get('atlas'))} · archivos:", ", ".join(os.path.basename(a) for a in atlas.get("archivos", [])))
    if errores:
        print(f"\n{len(errores)} ERRORES:")
        for e in errores:
            print("  -", e)
    else:
        print("\nSin errores.")
    for a in avisos:
        print("AVISO:", a)
    print("\nResumen:", dict(collections.Counter(n.get("tipo") for n in nodos)),
          f"| {len(nodos)} nodos | {len(relaciones)} relaciones")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
