#!/usr/bin/env python3
"""
Detector de candidatos a revisión en es-ES.ini
Genera un informe agrupado por tipo de problema.
NO modifica ningún fichero.
"""

import re
import os
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ES_FILE = os.path.join(BASE, "locales", "es-ES.ini")
EN_FILE = os.path.join(BASE, "locales", "en-EN.ini")
OUT_FILE = os.path.join(BASE, "memory", "review_candidates.txt")

# ─── Carga del fichero ────────────────────────────────────────────────────────

def load_ini(path):
    """Devuelve dict {clave: valor} preservando el orden."""
    data = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if "=" in line:
                key, _, val = line.partition("=")
                data[key] = val
    return data

# ─── Helpers ──────────────────────────────────────────────────────────────────

def is_item_desc(key):
    """Claves de descripción de item/vehículo/equipo."""
    k = key.lower()
    return any(k.startswith(p) for p in ['item_desc', 'item_name', 'item_type',
                                          'vehicle_desc', 'vehicle_name',
                                          'items_commodities'])

def is_dialogue(key):
    """Claves de diálogo o callout de combate."""
    k = key.lower()
    return any(p in k for p in ['_ig_', '_cv_', '_dlg', 'dlg_', 'ph_pu_',
                                 'pu_gen', 'pu_csc', 'pu_nt', 'pu_adv'])

def is_ui(key):
    """Claves de interfaz de usuario."""
    k = key.lower()
    return any(k.startswith(p) for p in ['ui_', 'hud_', 'dfm_', 'ea_ui',
                                          'notification_', 'pause_', 'hint'])

# ─── Reglas de detección ─────────────────────────────────────────────────────

def check_calcos_estructurales(key, es, en):
    """Calcos literales del inglés documentados en SKILL.md."""
    hits = []

    # Patrones simples sin contexto especial
    simple = [
        (r'\ben términos de\b',        '"en términos de" -> "en cuanto a / respecto a"'),
        (r'\ben terminos de\b',        '"en terminos de" -> "en cuanto a / respecto a"'),
        (r'\bhacer frente a\b',        '"hacer frente a" -> "enfrentarse a / combatir"'),
        (r'\ba nivel de\b',            '"a nivel de" -> simplificar'),
        (r'\ben lo que respecta a\b',  '"en lo que respecta a" -> "en cuanto a"'),
        (r'\bhacer referencia a\b',    '"hacer referencia a" -> "referirse a"'),
        (r'\bestaba en ruta hacia\b',  '"estaba en ruta hacia" -> "se dirigía a"'),
        (r'\bfinalizaci[oó]n con [eé]xito\b', '"finalización con éxito" restante -> verificar'),
        (r'\bcompletar el objetivo\b', '"completar el objetivo" -> verificar naturalidad'),
    ]
    for pat, note in simple:
        if re.search(pat, es, re.IGNORECASE):
            hits.append(note)

    # "por parte de" — solo en contextos que no sean legales/formales
    if re.search(r'\bpor parte de\b', es, re.IGNORECASE):
        # Omitir boilerplate legal de contratos
        if not re.search(r'personas? o entidades?|destinatario previsto|informaci[oó]n confidencial', es, re.IGNORECASE):
            hits.append('"por parte de" -> voz activa o genitivo directo')

    # "al mismo tiempo" — solo en diálogo/misiones, no en item descriptions
    if re.search(r'\bal mismo tiempo\b', es, re.IGNORECASE) and not is_item_desc(key):
        hits.append('"al mismo tiempo" -> "a la vez" (diálogo/narración)')

    # "en este momento" — solo en diálogo, no en anuncios formales
    if re.search(r'\ben este momento\b', es, re.IGNORECASE) and is_dialogue(key):
        hits.append('"en este momento" -> "ahora mismo"')

    # "se encuentra" — solo en misiones/diálogo, no en lore/enciclopedia/UI
    if re.search(r'\bse encuentra\b', es, re.IGNORECASE):
        k = key.lower()
        is_lore = any(p in k for p in ['_desc', 'system_', 'planet_', 'location_',
                                        'journal_', 'histmarker', 'repui', 'repstanding'])
        if not is_lore:
            hits.append('"se encuentra" -> "está" / voz activa')

    # "en particular" — solo cuando es realmente redundante (sin sustantivo previo)
    # Patrón: "en particular," o "en particular." o ". En particular," (al inicio de cláusula)
    # Excluir: "X en particular" cuando hay sustantivo/pronombre antes
    for m in re.finditer(r'\ben particular\b', es, re.IGNORECASE):
        start = m.start()
        # Buscar si hay un sustantivo/pronombre justo antes
        before = es[max(0, start-30):start].strip()
        # Si justo antes hay un nombre o pronombre (no puntuación/conector), es uso válido
        if not re.search(r'\b(este|esta|estos|estas|ese|esa|uno|una|el|la|los|las|aquel|cualquier)\b\s*\w+\s*$', before, re.IGNORECASE):
            hits.append('"en particular" al inicio de cláusula -> revisar si es redundante')
            break  # solo reportar una vez por clave

    return hits


def check_latinoamericanismos(key, es, en):
    """Palabras/formas latinoamericanas o anglicismos a evitar."""
    hits = []

    # Reglas directas sin excepciones
    simple = [
        (r'\benojad[oa]\b',  '"enojado" -> "cabreado/enfadado"'),
        (r'\babrumad[oa]\b', '"abrumado" -> "desbordado/agobiado" según contexto'),
        (r'\babrumador\b',   '"abrumador" -> "aplastante/arrollador"'),
        (r'\belegible\b',    '"elegible" -> "apto/apta"'),
        (r'\bdisrump',       '"disrumpir" -> "desbaratar/perturbar" (anglicismo inválido)'),
        (r'\bpilotear\b',    '"pilotear" -> "pilotar"'),
        (r'\bbuque\b',       '"buque" -> "nave"'),
        (r'\bbarco\b',       '"barco" -> "nave" (contexto espacial)'),
    ]
    for pat, note in simple:
        if re.search(pat, es, re.IGNORECASE):
            hits.append(note)

    # "evidencia" — solo usos sustantivos, no el verbo "se evidencia"
    if re.search(r'\bevidencia\b', es, re.IGNORECASE):
        if not re.search(r'\bse evidencia\b|\bevidencia[rn]\b', es, re.IGNORECASE):
            hits.append('"evidencia" -> "pruebas" (contexto policial/legal)')

    # "outsourcing" — solo si NO forma parte de un nombre de empresa (precedido de palabra en inglés)
    if re.search(r'\boutsourcing\b', es, re.IGNORECASE):
        if not re.search(r'\b[A-Z][a-z]+ [A-Z][a-z]+ Outsourcing\b', es):
            hits.append('"outsourcing" -> "subcontratación"')

    # "ingresado/a" — solo usos de "entrar a" latinoamericano, no médico (ingresado en hospital)
    if re.search(r'\bingresad[oa]\b', es, re.IGNORECASE):
        if not re.search(r'ingresado en (el |un )?(hospital|centro|clínica)', es, re.IGNORECASE):
            hits.append('"ingresado" -> "introducido/entrado" según contexto')

    # "calificacion" — solo contextos de expediente/credenciales, no ratings técnicos
    if re.search(r'\bcalificaci[oó]n\b', es, re.IGNORECASE):
        # Omitir ratings técnicos conocidos
        if not re.search(r'calificaci[oó]n\s*(EVA|de efectividad|de riesgo|CrimeStat|de combate|minima|[A-Z]{2,})',
                         es, re.IGNORECASE):
            # Solo reportar si EN usa "qualification" (credencial) no "rating"
            if en and re.search(r'\bqualification\b', en, re.IGNORECASE):
                hits.append('"calificación" como credencial -> "habilitación/requisito"')

    # "escombros" — solo en contextos narrativos, no como nombre de item
    if re.search(r'\bescombros\b', es, re.IGNORECASE):
        if not (is_item_desc(key) or 'item_name' in key.lower() or 'item_type' in key.lower()
                or re.search(r'Construction|Construccion', es, re.IGNORECASE)):
            hits.append('"escombros" -> "restos" (debris de nave en contexto narrativo)')

    # "piso" — solo si queda algún floor no convertido (items de suelo son válidos)
    if re.search(r'\bpiso\b', es, re.IGNORECASE):
        k = key.lower()
        # Omitir claves que ya son de suelo/decoración o apartamento
        if not any(p in k for p in ['flair', 'floor_', '_floor', 'apartment', 'piso_']):
            # Solo si el contexto sugiere planta de edificio (no suelo, no apartamento)
            if re.search(r'\bpiso\s+\d+\b|\bprimer piso\b|\bsegundo piso\b', es, re.IGNORECASE):
                hits.append('"piso" -> "planta" (planta de edificio en España)')

    # "fortaleza" — solo en contextos de nave/resistencia, no edificios reales
    if re.search(r'\bfortaleza\b', es, re.IGNORECASE):
        if is_item_desc(key) and re.search(r'(durabilidad|resistencia|fortitud)', en, re.IGNORECASE):
            hits.append('"fortaleza" -> "resistencia/aguante" (contexto nave/equipo)')

    # "refinamiento" — solo en contextos de diseño donde el EN dice "refinement" de calidad
    # (no en contextos industriales de refinado de mineral)
    if re.search(r'\brefinamiento\b', es, re.IGNORECASE):
        if en and re.search(r'\brefinement\b', en, re.IGNORECASE):
            if not re.search(r'(mineral|ore|mining|refinery|process|material)', en, re.IGNORECASE):
                hits.append('"refinamiento" -> verificar si calco de "refinement"')

    # "ambiente" — solo si EN dice "environment" en contexto técnico/de sistema
    if re.search(r'\bambiente\b', es, re.IGNORECASE):
        if en and re.search(r'\benvironment\b', en, re.IGNORECASE):
            if re.search(r'(game environment|work environment|operating environment)', en, re.IGNORECASE):
                hits.append('"ambiente" -> posible calco de "environment" técnico')

    return hits


def check_usted_en_objetivos(key, es, en):
    """Formas de usted en claves de objetivo de misión."""
    obj_keys = ['_obj', '_long', '_short', '_title', 'mission_', 'objective', 'task_']
    is_obj = any(k in key.lower() for k in obj_keys)
    if not is_obj:
        return []

    hits = []

    # "Viaje" como imperativo: solo si NO va precedido de sustantivo o adjetivo
    # "Viaje Quantum", "Rutas de Viaje", "Aviso de Viaje" son sustantivos → excluir
    if re.search(r'\bViaje\b', es):
        # Excluir si va seguido de sustantivo que indica que es noun ("Quantum", "de Yela", etc.)
        # o precedido de "de", "Rutas de", "Aviso de"
        if not re.search(r'\b(Quantum|de [A-Z]|\bRutas de\b|\bAviso de\b|\bde\b)\s+Viaje\b|'
                         r'\bViaje\s+(Quantum|de [A-Z]|[A-Z][a-z]+\b)', es):
            hits.append('"Viaje" -> "Viaja" (usted -> tú)')

    # "Informe" como imperativo: solo si NO va seguido de "de" (que indica sustantivo)
    if re.search(r'\bInforme\b', es):
        if not re.search(r'\bInforme\s+de\b', es):
            hits.append('"Informe" -> "Contacta/Informa" (usted -> tú)')

    # Resto de verbos: solo al inicio de la cadena o tras puntuación
    imperativos = [
        (r'(?:^|[.!?¡¿\n])\s*Localice\b', '"Localice" -> "Localiza"'),
        (r'(?:^|[.!?¡¿\n])\s*Proteja\b',  '"Proteja" -> "Protege"'),
        (r'(?:^|[.!?¡¿\n])\s*Elimin[e]\b', '"Elimine" -> "Elimina"'),
        (r'(?:^|[.!?¡¿\n])\s*Dirí?jase\b', '"Diríjase" -> "Dirígete"'),
        (r'(?:^|[.!?¡¿\n])\s*Regrese\b',  '"Regrese" -> "Regresa"'),
        (r'(?:^|[.!?¡¿\n])\s*Entregue\b', '"Entregue" -> "Entrega"'),
        (r'(?:^|[.!?¡¿\n])\s*Recoja\b',   '"Recoja" -> "Recoge"'),
        (r'(?:^|[.!?¡¿\n])\s*Esper[e]\b', '"Espere" -> "Espera"'),
        (r'(?:^|[.!?¡¿\n])\s*Hable\b',    '"Hable" -> "Habla"'),
    ]
    for pat, note in imperativos:
        if re.search(pat, es, re.MULTILINE):
            hits.append(note)

    return hits


def check_expresiones_idiomaticas(key, es, en):
    """Calcos de expresiones idiomáticas conocidas."""
    hits = []

    patterns = [
        (r'no hay amor perdido',      '"no hay amor perdido" -> "hay mala sangre"'),
        (r'cuida tus seis',           '"cuida tus seis" -> "cuida tu espalda"'),
        (r'lo primero es lo primero', '"lo primero es lo primero" -> "antes de nada"'),
        (r'hostiles entrantes',       '"hostiles entrantes" -> "¡Hostiles detectados!"'),
        (r'nos estamos mudando',      '"nos estamos mudando" -> "¡En marcha!"'),
        (r'trabajo mojado',           '"trabajo mojado" -> "Trabajo Sucio"'),
        (r'la palabra es que',        '"la palabra es que" -> "Parece que"'),
        (r'esperanza de encontrarte bien', '"Espero encontrarte bien" -> "Espero que estés bien"'),
        (r'admiran?(?:se|os)',        '"admirarse/fan out" -> "dispersarse"'),
        (r'gremio de cazadores',      '"gremio de cazadores" -> "Bounty Hunters Guild"'),
        (r'estaci[oó]n fragmentadora', '"Estación Fragmentadora" -> "Breaker Station"'),
    ]
    for pat, note in patterns:
        if re.search(pat, es, re.IGNORECASE):
            hits.append(note)

    # "uso de energía" — solo si no es ya "consumo de energía"
    if re.search(r'\buso de energ[ií]a\b', es, re.IGNORECASE):
        hits.append('"uso de energía" -> "consumo de energía"')

    # "en la carrera" — solo si EN tiene "on the run" (huyendo), no racing
    if re.search(r'\ben la carrera\b', es, re.IGNORECASE):
        if en and re.search(r'\bon the run\b', en, re.IGNORECASE):
            hits.append('"en la carrera" -> "en retirada/huyendo" (si significa "on the run")')

    # "a punto de estallar" — solo si en contexto de carga/nave, no combate genérico
    if re.search(r'a punto de estallar', es, re.IGNORECASE):
        if re.search(r'(carg|repleto|lleno|full|loaded)', es + (en or ''), re.IGNORECASE):
            hits.append('"a punto de estallar de carga" -> "cargada hasta los topes"')

    return hits


def check_pronombres_sujeto(key, es, en):
    """Pronombres sujeto innecesarios (español los omite)."""
    hits = []

    # "nosotros hemos/somos" — siempre innecesario salvo contraste explícito
    if re.search(r'\bnosotros hemos\b', es, re.IGNORECASE):
        hits.append('Pronombre sujeto innecesario: "nosotros hemos" -> "hemos"')
    if re.search(r'\bnosotros somos\b', es, re.IGNORECASE):
        # Excluir contraste: "nosotros somos X y ellos son Y"
        if not re.search(r'nosotros somos.{0,30}(y|pero).{0,30}(ellos|son)', es, re.IGNORECASE):
            hits.append('Pronombre sujeto innecesario: "nosotros somos" -> "somos"')

    # "ellos son" — excluir partitivo ("de ellos son", "sobre ellos son") y contraste
    if re.search(r'\bellos son\b', es, re.IGNORECASE):
        if not re.search(r'(de ellos son|sobre ellos|ellos son .{0,20} y nosotros)', es, re.IGNORECASE):
            hits.append('Pronombre sujeto innecesario: "ellos son" -> "son"')

    # "ellos tienen" — siempre innecesario en callouts de combate
    if re.search(r'\bellos tienen\b', es, re.IGNORECASE):
        hits.append('Pronombre sujeto innecesario: "ellos tienen" -> "tienen"')

    # "yo tengo" — innecesario salvo énfasis dramático claro
    if re.search(r'\byo tengo\b', es, re.IGNORECASE):
        hits.append('Pronombre sujeto innecesario: "yo tengo" -> "tengo"')

    # "yo soy" — excluir introducciones de personaje (seguido de nombre propio)
    if re.search(r'\byo soy\b', es, re.IGNORECASE):
        # Omitir "Yo soy [NombrePropio]" — introducción de personaje
        if not re.search(r'\byo soy\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\b', es):
            hits.append('Pronombre sujeto innecesario: "yo soy" -> "soy"')

    return hits


def check_html_entities(key, es, en):
    """Entidades HTML que deben estar decodificadas."""
    hits = []
    if '&amp;' in es:
        hits.append('Entidad HTML "&amp;" -> "&"')
    if '&lt;' in es:
        hits.append('Entidad HTML "&lt;" -> "<"')
    if '&gt;' in es:
        hits.append('Entidad HTML "&gt;" -> ">"')
    if '&nbsp;' in es:
        hits.append('Entidad HTML "&nbsp;" -> espacio')
    return hits


def check_sin_traducir(key, es, en):
    """Valor idéntico al EN cuando debería estar traducido."""
    if not en or not es:
        return []
    if es.strip() != en.strip():
        return []

    # Excluir patrones que se mantienen en inglés por convención
    skip_patterns = [
        r'^[A-Z0-9_\-\s]+$',   # Solo mayúsculas/números (UI codes)
        r'^\d+$',               # Solo números
        r'^WIP',                # WIP prefix
        r'^\[',                 # Tags [P] etc
        r'^The\s+\w',           # Nombres propios "The X"
        r'^[A-Z][a-z]+\s+[A-Z]',  # "NombreApellido" — nombre de personaje
    ]
    for pat in skip_patterns:
        if re.match(pat, es.strip()):
            return []

    # Excluir claves de tipo "from" (remitente de mensaje) — nombres de org/personaje
    if key.lower().endswith('_from') or key.lower().endswith('_name'):
        return []

    # Solo reportar si tiene contenido significativo en inglés
    if len(es) > 10 and re.search(r'\b(the|and|for|with|your|that|this|from)\b', es, re.IGNORECASE):
        return ['Posible sin traducir: valor idéntico al EN']
    return []


def check_longitud_sospechosa(key, es, en):
    """Detecta traducciones anormalmente cortas respecto al original."""
    if not en or not es:
        return []
    len_en = len(en)
    len_es = len(es)
    if len_en < 20:
        return []

    # Excluir claves donde EN es un placeholder ("X description.", "X name.")
    if re.match(r'^[A-Za-z\s]+ (description|name|title)\.$', en.strip(), re.IGNORECASE):
        return []

    ratio = len_es / len_en
    hits = []
    if ratio < 0.3:
        hits.append(f'Traducción muy corta: ES={len_es} chars vs EN={len_en} chars (ratio {ratio:.2f})')
    elif ratio > 3.5:
        # Excluir cuando EN es muy corto y ES añade contexto legítimo
        if len_en > 30:
            hits.append(f'Traducción muy larga: ES={len_es} chars vs EN={len_en} chars (ratio {ratio:.2f})')
    return hits


def check_nombres_traducidos(key, es, en):
    """Nombres propios que NO deben traducirse."""
    patterns = [
        (r'Gremio de Cazadores',    '"Gremio de Cazadores" -> "Bounty Hunters Guild"'),
        (r'Gremio Mercenario',      '"Gremio Mercenario" -> "Mercenary Guild"'),
        (r'Alianza Popular',        '"Alianza Popular" -> "People\'s Alliance"'),
        (r'Espada Fragmentada',     '"Espada Fragmentada" -> "Shattered Blade"'),
        (r'Estaci[oó]n Rompedora',  '"Estación Rompedora" -> "Breaker Station"'),
        (r'Fuerza de Defensa Civil', '"Fuerza de Defensa Civil" -> "CDF"'),
        (r'Festival de la Fundaci[oó]n', '"Festival de la Fundación" -> "Foundation Festival"'),
        (r'Orden de [Mm]uerte',     '"Orden de Muerte" -> "Orden de Eliminación"'),
    ]
    hits = []
    for pat, note in patterns:
        if re.search(pat, es, re.IGNORECASE):
            hits.append(note)
    return hits

# ─── Motor principal ──────────────────────────────────────────────────────────

CHECKS = [
    ("CALCOS ESTRUCTURALES",        check_calcos_estructurales),
    ("LATINOAMERICANISMOS/ANGLICISMOS", check_latinoamericanismos),
    ("USTED EN OBJETIVOS",          check_usted_en_objetivos),
    ("EXPRESIONES IDIOMÁTICAS MAL TRADUCIDAS", check_expresiones_idiomaticas),
    ("PRONOMBRES SUJETO INNECESARIOS", check_pronombres_sujeto),
    ("ENTIDADES HTML",              check_html_entities),
    ("NOMBRES PROPIOS TRADUCIDOS",  check_nombres_traducidos),
    ("POSIBLE SIN TRADUCIR",        check_sin_traducir),
    ("LONGITUD SOSPECHOSA",         check_longitud_sospechosa),
]

def run():
    print("Cargando ficheros...")
    es_data = load_ini(ES_FILE)
    en_data = load_ini(EN_FILE)

    results = defaultdict(list)  # categoria -> [(key, es, en, [notas])]
    total_candidates = 0

    print(f"Analizando {len(es_data):,} claves...")

    for key, es_val in es_data.items():
        en_val = en_data.get(key, "")
        for category, check_fn in CHECKS:
            hits = check_fn(key, es_val, en_val)
            if hits:
                results[category].append((key, es_val, en_val, hits))
                total_candidates += 1

    # Escribir informe
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("INFORME DE CANDIDATOS A REVISIÓN — es-ES.ini\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Total de candidatos detectados: {total_candidates}\n")
        f.write(f"Claves analizadas: {len(es_data):,}\n\n")

        for category, check_fn in CHECKS:
            entries = results.get(category, [])
            if not entries:
                continue
            f.write("=" * 70 + "\n")
            f.write(f"## {category} ({len(entries)} candidatos)\n")
            f.write("=" * 70 + "\n\n")
            for key, es_val, en_val, notes in entries:
                f.write(f"KEY: {key}\n")
                if en_val:
                    en_preview = en_val[:200] + "..." if len(en_val) > 200 else en_val
                    f.write(f" EN: {en_preview}\n")
                es_preview = es_val[:200] + "..." if len(es_val) > 200 else es_val
                f.write(f" ES: {es_preview}\n")
                for note in notes:
                    f.write(f"  ⚠ {note}\n")
                f.write("\n")

    # Resumen en consola
    print(f"\nRESUMEN:")
    print(f"{'─'*50}")
    for category, check_fn in CHECKS:
        count = len(results.get(category, []))
        if count:
            print(f"  {category:<45} {count:>5}")
    print(f"{'─'*50}")
    print(f"  {'TOTAL':<45} {total_candidates:>5}")
    print(f"\nInforme completo guardado en: {OUT_FILE}")

if __name__ == "__main__":
    run()
