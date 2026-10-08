#!/usr/bin/env python3
"""Ayuda para aplicar la regla 1 de la Guía de redacción.

Lista las palabras en mayúscula que aparecen fuera de un enlace [[id|texto]]
en los textos de un atlas (resumen, profundización, anécdotas y notas de las
relaciones), agrupadas por el número de fichas en que aparecen.

Es una herramienta heurística: no distingue nombres de personas de lugares o
títulos, ni sabe si un nombre ya se explica en la misma frase. Sirve para
revisar a mano, empezando por los nombres que se repiten en varias fichas,
que según la Guía merecen ficha propia.

Uso:
    python3 herramientas/revisar_nombres.py RUTA_DEL_ATLAS [--min N]
"""
import argparse
import collections
import json
import os
import re

ENLACE = re.compile(r"\[\[[^\]]*\]\]")
FRASE = re.compile(r"(?<=[.!?:;«»])\s+")
MAYUSCULA = re.compile(r"\b[A-ZÁÉÍÓÚÑÜ][\wáéíóúñüāīūēōṛṣṇṭḍśḥṃšəŋ'’-]+")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("atlas", help="carpeta del atlas (la que contiene atlas.json)")
    parser.add_argument("--min", type=int, default=1, help="mostrar solo nombres que aparecen en al menos N fichas")
    args = parser.parse_args()

    with open(os.path.join(args.atlas, "atlas.json"), encoding="utf-8") as f:
        atlas = json.load(f)
    apariciones = collections.defaultdict(set)

    def revisar(texto, donde):
        limpio = ENLACE.sub("§", texto)
        for frase in FRASE.split(limpio):
            palabras = MAYUSCULA.findall(frase)
            if frase[:1].isupper():
                palabras = palabras[1:]  # la primera palabra de la frase va en mayúscula por norma
            for p in palabras:
                if not re.fullmatch(r"[IVXLC]+", p):  # números romanos
                    apariciones[p].add(donde)

    for relativa in atlas.get("archivos", []):
        with open(os.path.join(args.atlas, relativa), encoding="utf-8") as f:
            datos = json.load(f)
        for n in datos.get("nodos", []):
            for campo in ("resumen", "profundizacion", "anecdotas"):
                if n.get(campo):
                    revisar(n[campo], n["id"])
        for r in datos.get("relaciones", []):
            if r.get("nota"):
                revisar(r["nota"], r["id"])

    filas = sorted(((len(v), k, sorted(v)) for k, v in apariciones.items() if len(v) >= args.min), reverse=True)
    for veces, palabra, donde in filas:
        muestra = ", ".join(donde[:5]) + (" …" if len(donde) > 5 else "")
        print(f"{palabra:<22} {veces:>3}  {muestra}")


if __name__ == "__main__":
    main()
