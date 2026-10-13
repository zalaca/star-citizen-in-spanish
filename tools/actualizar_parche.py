"""Actualiza la traduccion cuando CIG publica un global.ini nuevo.

Uso:
    python tools/actualizar_parche.py RUTA/AL/global.ini            (solo informe)
    python tools/actualizar_parche.py RUTA/AL/global.ini --aplicar  (informe + actualiza ficheros)

Compara el ingles nuevo con locales/en-EN.ini y clasifica cada clave:
  - nueva:      no existia -> se anade a es-ES.ini con el texto en ingles (pendiente de traducir)
  - cambiada:   el ingles ha cambiado -> se conserva la traduccion actual (pendiente de revisar)
  - eliminada:  ya no existe -> se quita de es-ES.ini
  - igual:      se conserva la traduccion tal cual

Con --aplicar reescribe locales/en-EN.ini, locales/es-ES.ini y la copia de
copy/data/Localization/spanish_(spain)/global.ini, en el orden de claves del
ingles nuevo y con el formato del repo (UTF-8 con BOM, CRLF).

El informe (informe_parche.md por defecto) lista lo pendiente y avisa de las
claves cuya traduccion ha perdido placeholders del ingles nuevo.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EN = REPO / 'locales' / 'en-EN.ini'
ES = REPO / 'locales' / 'es-ES.ini'
COPIA = REPO / 'copy' / 'data' / 'Localization' / 'spanish_(spain)' / 'global.ini'

PLACEHOLDER = re.compile(r'~\w+\([^)]*\)|%(?:ls|Is|[sSdi])')


def leer(ruta):
    """Devuelve (lineas, dict clave->valor). Acepta BOM o no, CRLF o LF."""
    with open(ruta, encoding='utf-8-sig', newline='') as f:
        texto = f.read()
    # Solo CRLF (o LF si el fichero no usa CRLF) separa lineas: algunos valores
    # de CIG llevan un \r suelto dentro del texto y hay que conservarlo.
    lineas = texto.split('\r\n' if '\r\n' in texto else '\n')
    if lineas and lineas[-1] == '':
        lineas.pop()
    valores = {}
    for l in lineas:
        if '=' in l:
            k, v = l.split('=', 1)
            valores[k] = v
    return lineas, valores


def escribir(ruta, lineas):
    Path(ruta).write_bytes(('﻿' + '\r\n'.join(lineas) + '\r\n').encode('utf-8'))


def faltan(en, es):
    """Placeholders del ingles que no estan en la traduccion (los de mas se toleran: extras del pack)."""
    return Counter(PLACEHOLDER.findall(en)) - Counter(PLACEHOLDER.findall(es))


def recorta(t, n=300):
    return t if len(t) <= n else t[:n] + '…'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('nuevo', help='global.ini en ingles del parche nuevo')
    ap.add_argument('--aplicar', action='store_true', help='reescribe en-EN.ini, es-ES.ini y la copia')
    ap.add_argument('--informe', default='informe_parche.md', help='ruta del informe (por defecto informe_parche.md)')
    args = ap.parse_args()

    lineas_nuevo, en_nuevo = leer(args.nuevo)
    _, en_viejo = leer(EN)
    _, es = leer(ES)

    nuevas, cambiadas, eliminadas = [], [], [k for k in en_viejo if k not in en_nuevo]
    salida = []
    for l in lineas_nuevo:
        if '=' not in l:
            salida.append(l)
            continue
        k, v = l.split('=', 1)
        if k not in en_viejo or k not in es:
            nuevas.append(k)
            salida.append(l)
        else:
            if en_viejo[k] != v:
                cambiadas.append(k)
            salida.append(k + '=' + es[k])

    traducido = dict(x.split('=', 1) for x in salida if '=' in x)
    rotas = [(k, faltan(en_nuevo[k], traducido[k])) for k in en_nuevo
             if k not in nuevas and faltan(en_nuevo[k], traducido[k])]

    inf = [f'# Informe de parche\n',
           f'- Claves en el ingles nuevo: {len(en_nuevo)} (antes {len(en_viejo)})',
           f'- Nuevas (sin traducir): {len(nuevas)}',
           f'- Cambiadas en ingles (revisar traduccion): {len(cambiadas)}',
           f'- Eliminadas: {len(eliminadas)}',
           f'- Traducciones a las que les falta algun placeholder: {len(rotas)}\n']
    if rotas:
        inf.append('## Placeholders que faltan\n')
        for k, f in rotas:
            inf.append(f'- `{k}`: falta {", ".join(f"`{p}`" + (f" x{n}" if n > 1 else "") for p, n in f.items())}')
        inf.append('')
    if cambiadas:
        inf.append('## Cambiadas en ingles\n')
        for k in cambiadas:
            inf += [f'### `{k}`', f'- EN antes: {recorta(en_viejo[k])}', f'- EN ahora: {recorta(en_nuevo[k])}',
                    f'- ES actual: {recorta(es[k])}', '']
    if nuevas:
        inf.append('## Nuevas\n')
        for k in nuevas:
            inf.append(f'- `{k}` = {recorta(en_nuevo[k])}')
        inf.append('')
    if eliminadas:
        inf.append('## Eliminadas\n')
        for k in eliminadas:
            inf.append(f'- `{k}` (ES era: {recorta(es.get(k, ""), 120)})')
        inf.append('')
    Path(args.informe).write_text('\n'.join(inf), encoding='utf-8')

    print(f'Nuevas: {len(nuevas)} | Cambiadas: {len(cambiadas)} | Eliminadas: {len(eliminadas)} '
          f'| Placeholders que faltan: {len(rotas)}')
    print(f'Informe: {Path(args.informe).resolve()}')

    if args.aplicar:
        escribir(EN, lineas_nuevo)
        escribir(ES, salida)
        COPIA.parent.mkdir(parents=True, exist_ok=True)
        escribir(COPIA, salida)
        print('Aplicado: en-EN.ini, es-ES.ini y copia actualizados.')
    else:
        print('Modo informe: no se ha tocado ningun fichero (usa --aplicar).')


if __name__ == '__main__':
    sys.exit(main())
