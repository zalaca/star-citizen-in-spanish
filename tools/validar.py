"""Comprueba que la traduccion no esta rota antes de publicarla.

Uso:
    python tools/validar.py

Estructura (si falla algo, sale con codigo 1 y la release no se publica):
  - es-ES.ini tiene las mismas claves que en-EN.ini y en el mismo orden
  - cada linea es clave=valor, sin finales de linea mezclados ni caracteres de control
  - no falta ningun placeholder del ingles (~mission(...), %ls, %d...)
  - la copia de copy/ es identica a locales/es-ES.ini

Glosario: busca los terminos que SKILL.md prohibe ("Mapa Estelar",
"Fuerza de Defensa Civil", "babor"...). Muchas reglas solo saltan si el
ingles contiene el termino original, para no dar falsos positivos con
usos legitimos ("primer plano", "Marina Mercante"...). Tambien hace fallar
la validacion.
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from actualizar_parche import COPIA, EN, ES, PLACEHOLDER, leer

# (nombre, regex en es-ES, regex que debe aparecer en en-EN o None, regex de claves o None)
GLOSARIO = [
    ('Starmap', r'(?i)\bmapas? estelar', r'(?i)starmap', None),
    ('Blueprint', r'(?i)\bplanos?\b', r'\bBlueprints?\b', None),
    ('Multi-tool', r'(?i)multiherramienta|herramienta m[uú]ltiple', None, None),
    ('Quantum Drive (item)', r'(?i)\bmotor(es)? cu[aá]ntico', r'Quantum Drive', r'^item_Name'),
    ('(Modified)', r'\(Modificad[oa]\)', r'\(Modified\)', None),
    ('Datapad', r'(?i)\bpanel(es)? de datos\b', r'(?i)datapad', None),
    ('CrimeStat', r'(?i)estad[ií]stica (criminal|de criminalidad)', None, None),
    ('Comm Array', r'(?i)(repetidor|sat[eé]lite|matriz)(es)? de comunicaciones', None, None),
    ('SPECTRUM', r'\bEspectro\b', r'SPECTRUM', None),
    ('Data Runner', r'(?i)\bcorredor(es)? de datos\b', None, None),
    ('Krypton/Corundum', r'(?i)\bcript[oó]n\b|\bcorind[oó]n\b', None, None),
    ('Alpha (NATO)', r'\bAlfa\b', r'\bAlpha\b', None),
    ('CDF', r'Fuerza de Defensa Civil|\bF[DC][CD]\b', None, None),
    ('Navy = Armada', r'(?<!Infanteria de )(?<!Infantería de )\bMarina\b(?! Mercante)', r'\bNavy\b', None),
    ('Starman', r'(?i)\bmarineros?\b|\bhombres? estelar', r'(?i)\bstarm[ae]n\b', None),
    ('izquierda/derecha', r'(?i)\b(babor|estribor)\b', None, None),
    ('nave, no barco', r'(?i)\b(barcos?|buques?)\b', None, None),
    ('pilotar', r'(?i)\bpilote(a|ar|an|aba|aban|ando)\b', None, None),
    ('apto, no elegible', r'(?i)\belegibles?\b', None, None),
    ('ordnance', r'(?i)\bordenanzas?\b', r'(?i)\bordnance\b', None),
    ('desguace', r'(?i)\bchatarre(o|r[ií]a)\b|\bsalvamento\b', r'(?i)\bsalvag', None),
    ('castellano', r'(?i)\bcomputadoras?\b|\brentar\b|\bchecar\b|\benojad[oa]s?\b', None, None),
]


SALTOS = re.compile(r'(?:\\n)+')


def estructura(errores):
    with open(ES, encoding='utf-8-sig', newline='') as f:
        texto = f.read()
    # Git guarda LF y en Windows se extrae con CRLF: vale cualquiera de los dos, pero no mezclados
    crlf = texto.count('\r\n')
    lf = texto.count('\n') - crlf
    if crlf and lf:
        errores.append(f'finales de linea mezclados: {crlf} CRLF y {lf} LF')
    control = sum(1 for c in texto if ord(c) < 32 and c not in '\r\n\t')
    if control:
        errores.append(f'{control} caracteres de control')

    lineas_en, en = leer(EN)
    lineas_es, es = leer(ES)
    sin_igual = [l for l in lineas_es if '=' not in l]
    if sin_igual:
        errores.append(f'{len(sin_igual)} lineas sin "=", la primera: {sin_igual[0][:80]}')
    claves_en = [l.split('=', 1)[0] for l in lineas_en if '=' in l]
    claves_es = [l.split('=', 1)[0] for l in lineas_es if '=' in l]
    if claves_en != claves_es:
        faltan = [k for k in claves_en if k not in es]
        sobran = [k for k in claves_es if k not in en]
        errores.append(f'claves distintas de en-EN: faltan {len(faltan)} {faltan[:5]}, '
                       f'sobran {len(sobran)} {sobran[:5]}' if faltan or sobran else
                       'claves en distinto orden que en-EN')

    for k in en:
        falta = Counter(PLACEHOLDER.findall(en[k])) - Counter(PLACEHOLDER.findall(es.get(k, '')))
        if k in es and falta:
            errores.append(f'{k}: falta {", ".join(falta)}')
        # mismos cortes que en-EN pero con distintos saltos: un \n\n que se quedo en \n o al reves
        saltos_en, saltos_es = SALTOS.findall(en[k]), SALTOS.findall(es.get(k, ''))
        if len(saltos_en) == len(saltos_es) and saltos_en != saltos_es:
            errores.append(f'{k}: saltos de linea distintos de en-EN')

    if COPIA.read_bytes() != ES.read_bytes():
        errores.append(f'{COPIA.relative_to(ES.parent.parent)} no es identica a locales/es-ES.ini')
    return en, es


def glosario(en, es, errores):
    for nombre, prohibido, requiere_en, claves in GLOSARIO:
        r = re.compile(prohibido)
        for k, v in es.items():
            if claves and not re.search(claves, k):
                continue
            if requiere_en and not re.search(requiere_en, en.get(k, '')):
                continue
            m = r.search(v)
            if m:
                contexto = v[max(0, m.start() - 40):m.end() + 40]
                errores.append(f'[{nombre}] {k}: ...{contexto}...')


def main():
    errores = []
    en, es = estructura(errores)
    n = len(errores)
    glosario(en, es, errores)
    for e in errores:
        print(e)
    print(f'Estructura: {"OK" if not n else f"{n} errores"} | '
          f'Glosario: {"OK" if len(errores) == n else f"{len(errores) - n} avisos"} | {len(es)} claves')
    return 1 if errores else 0


if __name__ == '__main__':
    sys.exit(main())
