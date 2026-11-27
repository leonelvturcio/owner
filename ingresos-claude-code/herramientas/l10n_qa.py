#!/usr/bin/env python3
"""QA de localización: compara un archivo fuente (en.json) con su traducción (es.json).

Detecta los errores que más quejas generan en juegos/apps traducidos:
  - claves que faltan o sobran
  - placeholders perdidos o alterados  ({name}, {{count}}, %s, %d, %1$s, <b>, [color=red])
  - textos sin traducir (idénticos al original)
  - textos demasiado largos (rompen la UI)

Uso:
  python3 l10n_qa.py en.json es.json [--max-ratio 1.5]

Soporta JSON plano o anidado. Código de salida 1 si hay errores (sirve para CI).
"""
import argparse
import json
import re
import sys

PLACEHOLDER = re.compile(
    r"\{\{[^}]+\}\}"          # {{count}}
    r"|\{[^{}]*\}"            # {name} / {0}
    r"|%\d*\$?[sdif@]"        # %s %d %1$s %@
    r"|</?[a-zA-Z][^>]*>"     # <b> </b> <color=#fff>
    r"|\[/?[a-zA-Z_]+[^\]]*\]"  # [color=red] [/color] (BBCode / Godot / Unity rich text)
)


def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out


def placeholders(text):
    return sorted(PLACEHOLDER.findall(text)) if isinstance(text, str) else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("target")
    ap.add_argument("--max-ratio", type=float, default=1.5,
                    help="longitud máxima traducción/original (default 1.5)")
    args = ap.parse_args()

    with open(args.source, encoding="utf-8") as f:
        src = flatten(json.load(f))
    with open(args.target, encoding="utf-8") as f:
        tgt = flatten(json.load(f))

    errors, warnings = [], []

    for k in src.keys() - tgt.keys():
        errors.append(f"FALTA      {k}")
    for k in tgt.keys() - src.keys():
        warnings.append(f"SOBRA      {k}")

    for k in sorted(src.keys() & tgt.keys()):
        s, t = src[k], tgt[k]
        if not isinstance(s, str) or not isinstance(t, str):
            continue
        if placeholders(s) != placeholders(t):
            errors.append(f"PLACEHOLDER {k}: {placeholders(s)} -> {placeholders(t)}")
        if s.strip() and s == t and len(s) > 3:
            warnings.append(f"SIN TRADUCIR {k}: {s!r}")
        if len(s) >= 12 and len(t) > len(s) * args.max_ratio:
            warnings.append(f"LARGO      {k}: {len(t)}/{len(s)} chars ({len(t)/len(s):.2f}x)")

    for line in errors:
        print("❌ " + line)
    for line in warnings:
        print("⚠️  " + line)
    print(f"\n{len(src)} claves revisadas · {len(errors)} errores · {len(warnings)} avisos")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
