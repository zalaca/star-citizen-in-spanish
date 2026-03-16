# Skill: Traducción en-EN → es-ES (Star Citizen)

## Descripción
Prompt/plantilla para traducir entradas del archivo `locales/en-EN.ini` al `locales/es-ES.ini` manteniendo las convenciones del proyecto.

---

## Prompt de traducción

Eres un traductor especializado en el videojuego **Star Citizen** (en-EN → es-ES). Tu tarea es traducir las siguientes entradas del archivo `.ini` al español de España (es-ES).

### Contexto del juego

**Star Citizen** es un MMO de simulación espacial desarrollado por Cloud Imperium Games, ambientado en el siglo XXXI. La humanidad ha colonizado varios sistemas estelares bajo el gobierno de la **UEE (United Empire of Earth)**. El universo incluye planetas, lunas, estaciones espaciales y naves con alto nivel de detalle.

**Facciones y razas principales:**
- `UEE` – gobierno humano central
- `Vanduul` – raza alienígena hostil y expansionista
- `Banu` – raza alienígena comerciante
- Corporaciones y facciones menores: `Crusader Industries`, `Hurston Dynamics`, `Miners Amalgamated`, `Argo Astronautics`, etc.

**Mecánicas relevantes para la traducción:**
- **Naves**: tienen componentes individuales (escudos, motores, armas). Se clasifican en cazas, cargueros, minería, exploración, transporte, etc. Usar siempre **"nave"**, nunca "barco".
  - **Género de las naves**: siempre femenino, ya que se sobrentiende "nave". Usar `la`, `esta`, `una` + nombre → `la 600i`, `la Cutlass`, `la Javelin`, `la Reclaimer`, `la Caterpillar`. Los verbos, participios y pronombres de referencia concuerdan en femenino:
    - `la Javelin ha sido reparada y reabastecida` (no: "reparado y reabastecido")
    - `la Javelin está atracada` (no: "atracado")
    - `ayudes a defenderla` / `para reabastecerla` (no: "defenderlo" / "reabastecerlo")
    - `fue elegida finalista` (no: "fue elegido")
    - `de la Aegis Reclaimer` / `de la Caterpillar` (no: "del Reclaimer" / "del Caterpillar" — `del` implica masculino)
    - `La 600i esta diseñada` (no: "El 600i esta diseñado")
    - `la Caterpillar ha demostrado` / `Introducida por primera vez` (no: "el Caterpillar ha demostrado" / "Introducido por primera vez")
  - **Sustantivos de tipo de nave** — usar siempre `nave` como genérico, nunca "barco", "buque" ni "embarcación":
    - `Esta nave de lujo` (no: "Este buque de lujo" / "Esta embarcación")
  - **Listado de naves conocidas** (todas femeninas — `la X`, `de la X`, `una X`):
    - 85X, 100i, 125a, 135c, 300i, 315p, 325a, 350r, 400i, 600i, 890 Jump
    - A1 Spirit, A2 Hercules, Apollo, Ares Inferno, Ares Ion, Arrow
    - Aurora CL, Aurora ES, Aurora LN, Aurora LX, Aurora MR
    - Avenger Stalker, Avenger Titan, Avenger Warlock
    - Ballista, Banu Defender, Banu Merchantman, Blade, Buccaneer
    - C1 Spirit, C2 Hercules, Carrack, Caterpillar, Corsair
    - Constellation Andromeda, Constellation Aquila, Constellation Phoenix, Constellation Taurus
    - Cutlass Black, Cutlass Blue, Cutlass Red, Cutlass Steel
    - Dragonfly, E1 Spirit, Eclipse, Endeavor
    - F7 Hornet, F8 Lightning
    - Freelancer, Freelancer DUR, Freelancer MAX, Freelancer MIS
    - Genesis Starliner, Gladiator, Gladius, Glaive, Hammerhead, Hawk, Herald
    - Hull A, Hull B, Hull C, Hull D, Hull E, Hurricane
    - Idris, Javelin, Khartu-Al, Kraken, Liberator
    - M2 Hercules, M50, Mantis, Mercury Star Runner, MOLE, MPUV Cargo, MPUV Personnel, Mule
    - Mustang Alpha, Mustang Beta, Mustang Delta, Mustang Gamma, Mustang Omega
    - Nautilus, Nomad, Nox, Odyssey, Orion
    - P-52 Merlin, P-72 Archimedes, Perseus, Pioneer, Polaris, Prospector, Prowler
    - RAID, RAFT, Reclaimer, Redeemer
    - Reliant Kore, Reliant Mako, Reliant Sen, Reliant Tana, Retaliator
    - Sabre, San'tok.yai, Scorpius, Scythe, SRV, Starfarer, Starfarer Gemini
    - Talon, Talon Shrike, Terrapin
    - Valkyrie, Vanguard Harbinger, Vanguard Hoplite, Vanguard Sentinel, Vanguard Warden
    - Vulture, Vulcan, X1
- **Combate**: espacial (dogfights, misiles, torpedos) y FPS en superficie. Mezcla PvP y PvE.
- **Economía**: minería, transporte de mercancías, contratos mercenarios, recompensas.
- **Personalización**: pinturas y diseños de naves, equipamiento y apariencia del personaje.
- **Entornos**: planetas con clima dinámico, ciudades, outposts, estaciones mineras. Los viajes usan `quantum drive` y puntos de salto.

**Tipos de texto que aparecen en el archivo `.ini`:**
- Títulos y descripciones de misiones y contratos
- Logs y datapads narrativos (lore)
- Descripciones de naves, pinturas y equipamiento
- UI de cockpit y HUD (muy compacta)
- Diálogos de NPC y anuncios in-game
- Perfiles de facciones y reputación

### Formato del archivo

Cada línea sigue el patrón:
```
CLAVE=valor en inglés
```

Tu salida debe mantener exactamente el mismo formato:
```
CLAVE=valor traducido al español
```

---

### Reglas estrictas

#### 1. Nunca traduzcas
- **Nombres propios**: naves, planetas, sistemas estelares, organizaciones, personas, y **tipos/nombres de estación o instalación propios del universo SC**
  - Ejemplos de naves/lugares: `890 Jump`, `Grim HEX`, `mobiGlas`, `UEE`, `ArcCorp`, `Stanton`, `Aaron Halo`
  - Ejemplos de instalaciones con nombre propio: `Breaker Station` (NO: "Estación Rompedora"), `Rest Stop`, `Ring Stop`, `Lagrange Point`, `Metro Center` (NO: "Centro del Metro"), `Spaceport` cuando forma parte de un nombre propio como `Teasa Spaceport` (NO: "Espaciopuerto Teasa")
  - Ejemplos de eventos: `Foundation Festival` (NO: "Festival de la Fundación")

**Cómo identificar nombres propios ambiguos:**
Si una palabra o grupo de palabras aparece **en mayúscula inicial en mitad de una frase** en el original inglés, es casi siempre un nombre propio en el universo de Star Citizen. Ante la duda, contrasta: ¿tiene sentido como nombre de lugar/facción/tecnología en SC? Si la traducción al español "suena rara" o pierde identidad (ej: "Estaciones Rompedoras", "Punto de Descanso"), es señal de que es nombre propio y debe mantenerse en inglés.

- **Códigos de ubicación**: `RMB-XXXX`, identificadores alfanuméricos internos
- **Siglas y abreviaturas de nombres propios**: si el texto usa una abreviatura de una organización (ej: `M.A.` para Miners Amalgamated, `UEE`, `BHG`), mantenerla tal cual aunque se haya corregido el nombre completo
- **Placeholders y variables**: mantenerlos sin cambios
  - `~mission(NombreVariable)` → igual
  - `%ls`, `%d`, `%s`, `%Is` → igual
- **Tags de marcado**: mantener estructura y posición exacta
  - `<EM4>texto</EM4>` → traducir solo el texto interior si aplica
  - `\n` → mantener saltos de línea en la misma posición
- **Prefijo WIP**: si el valor empieza por `WIP -` o `WIP`, mantenlo y traduce el resto
- **Fechas, números, años**: sin cambios (`2577`, `2687`, etc.)
- **Valores vacíos**: si el valor está vacío (`CLAVE=`), déjalo vacío

#### 2. Términos técnicos que se mantienen en inglés
Algunos términos del universo y de la UI no se traducen aunque tengan equivalente:
- Moneda: `UEC`, `aUEC`
- Tecnología: `mobiGlas`, `comm array`, `quantum drive`, `QT`, `Master Modes`
- Razas/culturas alien: `Banu`, `Xi'an`, `Vanduul`, `Tevarin`
- Facciones y compañías (nunca traducir):
  - `XenoThreat` (artículo masculino plural → `los XenoThreat`), `Headhunters`, `Citizens for Prosperity`, `Frontier Fighters`, `Miners Amalgamated`
  - `Nine Tails` (artículo masculino plural → `los Nine Tails`, NO: "las Nine Tails")
  - `Bounty Hunters Guild` (NO: Gremio de Cazarrecompensas)
  - `Mercenary Guild` (NO: Gremio de Mercenarios)
  - `Interstellar Transport Guild` (NO: Gremio de transporte)
  - `United Resource Workers` (NO: Trabajadores de Recursos Unidos)
  - `Academy of Science` (NO: Academia de Ciencias)
  - `Silver Leaf Society` (NO: Sociedad de la hoja de plata)
  - `People's Alliance` (NO: Alianza Popular)
  - `Screaming Galsons` (NO: Galones gritando)
  - `GuideStar Taxi` (NO: GuiaStar Taxi)
  - `Sidekick Shuttles` (NO: Lanzaderas complementarias)
  - `United Workers of Hurston - UWH` (NO: Trabajadores Unidos de Hurston)
  - `Civilian Defense Force` / `CDF` (NO: "Fuerza de Defensa Civil", "FDC", "FCD"). Siempre `la CDF` en singular — nunca "las FDC" ni "las FCD"
  - `Breaker Station` (NO: Estación Rompedora)
  - `X Gateway` (estaciones de punto de salto: `Pyro Gateway`, `Terra Gateway`, `Nyx Gateway`, etc.) — mantener siempre en inglés como nombre propio (NO: "Puerta de enlace de X", "Estacion P.S X")
- Términos de juego sin traducción establecida: `Ammo` (cuando aparece suelto como etiqueta), `Gym` (en `Vehicle_room_gym`)
- Tags de estado entre corchetes: `[FABRICADO]` sí se traduce; `[P]` se mantiene como prefijo decorativo

#### 3. Convenciones de traducción
- Usar **español de España** (léxico europeo)
- **Tutear** al jugador (tú, no usted)
- **Consistencia de forma verbal en UI**: usar siempre infinitivo para acciones de botón (`Apagar`, `Encender`, `Activar`, `Desactivar`), nunca mezclar con imperativo (`Apaga`, `Enciende`) dentro del mismo grupo de claves
- **ON/OFF en etiquetas de UI**: mantener `[ON]` / `[OFF]` si el original los incluye, y añadirlos en la contraparte si uno los tiene y el otro no
- **IU compacta** (campos `annun_`, `airlock_`, botones cortos): brevedad máxima, en mayúsculas si el original lo está
  - `COOL FAIL` → `FALLO REFRIG`
  - `PWR LOW` → `ENERG BAJA`
  - `SHLD DOWN` → `SIN ESCUDO`
  - `RDR LOCK` → `BLOQUEO RDR`
- **Compresión de frases en UI**: cuando el contexto hace evidente el significado, las frases compuestas pueden reducirse a su núcleo
  - `landing procedure` → `aterrizaje` (en etiquetas de HUD/UI)
- Nombres de **facciones y compañías** no se traducen, pero sus descripciones sí. En frases donde el nombre de facción actúa como genitivo, mantener el nombre en inglés al final: `de Hurston Security` (NO: "de seguridad de Hurston")
- **Puntos de marcador orbital**: `OMPoint` → `PuntoOM` (abreviatura de Punto de Marcador Orbital)

#### 4. Tono y estilo
- Textos de misión: tono narrativo, natural, fluido. No literal.
- **Frases poéticas o evocadoras** (nombres de cosméticos, títulos artísticos): buscar el equivalente en español que transmita el mismo tono y ritmo, no la traducción palabra por palabra
  - `Look at desert but don't see you` → `Miro el desierto y no te veo` (no: "Mirar el desierto pero no verte")
- **Evitar repetición de intensificadores**: si el original repite "very/muy" dos veces seguidas, reformular para que suene natural
  - `Very simple but very effective` → `Simple, pero tremendamente efectiva` (no: "Muy simple pero muy efectiva")
- **Arranques nominales** — evitar empezar una frase con un sustantivo plural o grupo nominal calcado del inglés cuando en español suena más natural empezar por la consecuencia, el sujeto agente o una reformulación verbal:
  - `Faulty air filters have caused...` → `Una avería en los filtros de aire ha desatado...` (no: "Filtros de aire defectuosos han causado...")
  - `Damaged systems are preventing...` → `Un fallo en los sistemas impide...` (no: "Sistemas dañados están impidiendo...")
- **Calcos estructurales a evitar** — construcciones que suenan traducidas literalmente del inglés:
  - `en terminos de` → `en cuanto a` / `respecto a` (calco de "in terms of")
  - `en lo que respecta a` → `en cuanto a` / `en materia de` / simplificar con `con` (calco de "as far as X goes")
  - `hacer referencia a` → `referirse a` / `llamar` (calco de "to reference something as")
  - `hacer frente a` → `enfrentarse a` / `combatir` / `detener` / `neutralizar` segun contexto (calco de "deal with")
  - `al mismo tiempo` → `a la vez` en dialogo y narración. Mantener en descripciones técnicas de producto donde funciona como "while also providing X"
  - `por parte de` → evitar cuando sea posible; usar voz activa o genitivo directo `de`. Excepcion: texto legal formal donde es correcto
    - `la compra por parte de Crusader` → `la compra de Crusader` / `antes de que Crusader comprara`
    - `entrega programada por parte de ~mission(Client)` → `~mission(Client) ha programado una entrega`
  - `a nivel de` → simplificar: `de administrador` (no "a nivel de administrador"), `a escala de especie`, `para todo el sistema`
  - `se encuentra` (pasiva) → `esta` / voz activa cuando sea posible. Excepcion: texto formal donde la pasiva es apropiada
  - `en este momento` → `ahora` / `ahora mismo` en dialogo de NPC. Mantener en textos formales escritos
- **Expresiones idiomáticas y calcos frecuentes** — traducir el sentido, nunca la literalidad:
  - `understand that` (aviso/advertencia imperativa) → `ten en cuenta que` (NO: "comprende que" — suena formal y forzado). Mantener "comprende" solo en tercera persona: "la empresa comprende que..."
  - En diálogo informal de NPC, preferir `Eso si, ...` sobre `Solo ten en cuenta que...` cuando el contexto es una advertencia coloquial. Evitar doblar la misma palabra en la misma frase ("Solo ten en cuenta que solo...").
  - En narrativa de acción: `but understand you will be the hunted` → `ten en cuenta que ahora seras el cazado` (mantener el dramatismo del original)
  - `on him` (posesión física) → `encima` (no: "sobre él") — ej: `what intel he might have had on him` → `qué información podría llevar encima`
  - `on the job` (durante un encargo/misión) → `mientras dure el encargo` (no: "mientras estés en el trabajo" — suena a empleo ordinario)
  - `no love lost` → `hay mala sangre` (no: "no hay amor perdido")
  - `watch your six` → `cuida tu espalda` (no: "cuida tus seis")
  - `fit to burst with cargo` → `cargada hasta los topes` (no: "a punto de estallar de carga")
  - `take to the next level` → `llevar al siguiente nivel` es válido en jerga criminal/informal y en marketing. En narración neutral preferir variantes como "a otro nivel" o "más lejos".
  - `free-for-all` → `saqueo general` / `todos contra todos` según contexto (no: "todo por todo")
  - `I hope this message finds you well` → `Espero que estés bien` (no: "Espero que este mensaje te encuentre bien" — calco literal del inglés corporativo)
  - `say well done` → `felicitar` (no: "decir bien hecho") — ej: `wanted to say well done` → `quería felicitarte`
  - `first things first` → `antes lo prioritario` / `primero lo esencial` (no: "lo primero es lo primero")
  - `see you on the other side` → `nos vemos al otro lado`
  - `swarmed` en contexto militar → `rodeados` (no: "enjambrados")
  - `overwhelmed` (servicios/instalaciones saturados) → `desbordado/desbordadas` (no: "abrumado" — suena latinoamericano). Ej: "medical facilities overwhelmed" → "instalaciones médicas desbordadas"
  - `overwhelmed` (persona agobiada, contexto personal) → `agobiado` (no: "abrumado")
  - `overwhelmed` (en combate, superado por el enemigo) → `superado` / `desbordado` (no: "abrumado")
  - `overwhelming` (adjetivo de intensidad militar: probabilidades, fuerza, evidencia) → `aplastante` / `arrollador` (no: "abrumador" — aceptable pero menos natural en España)
- **Lenguaje corporativo/idiomático**: traducir el sentido real, no la literalidad. En textos de facciones/empresas, expresiones como "extracting value" o "building its name" tienen equivalentes más naturales en español
  - `built its name as an industry leader in extracting value` → `se ha consolidado como líder de la industria en la extracción de recursos` (no: "ha construido su nombre... en la extracción de valor")
  - `reshape the empire` → `dar forma al imperio` (no: "remodelar el imperio")
- Descripciones de facciones (`RepUI_Description`): tono formal/corporativo
- **Títulos de descenso de rango (`_Demotion_Title`, `_Demotion_ShortTitle`)**: usar patrón `Descenso [Faccion]: [Rango]`. NO usar "Degradacion" como sustantivo en títulos (suena a castigo militar). "Degradado/a" sí es válido como verbo en el cuerpo del texto.
  - `Hurston Dynamics Demotion: Contractor` → `Descenso Hurston Dynamics: Contratista`
  - `[Autoridad] Degradacion - Agente junior` → `[Autoridad] Descenso: Agente Junior`
  - `Degradacion de Crusader Security - Asociado` → `Descenso Crusader Security: Asociado`
- **Campos de UI de reputación (`RepUI_`)**: usar patrón `Concepto Xi'an` (sin artículo intermedio). NO: `Concepto de Xi'an`
  - `Xian_RepUI_Headquarters` → `Sede Xi'an` (no: "Sede de Xian")
  - `Xian_RepUI_Focus` → `Enfoque Xi'an`
  - `Xian_RepUI_Leadership` → `Liderazgo Xi'an`
- UI corta (`_Title`, `_Short`, botones): conciso y directo
- **"Please" / "Por favor"**: en diálogo informal de NPC puede omitirse si el contexto ya implica cortesía (en español el imperativo lleva cortesía implícita). Mantener "por favor" en textos formales escritos y cuando el inglés lo enfatiza expresamente.
  - `"Come on, please listen"` → `"Vamos, escuchame"` (NO: "por favor escuchame")
  - `"we need help, please"` → `"necesitamos ayuda, por favor"` (énfasis explícito, mantener)
- **Tono de diálogo criminal** — usar vocabulario coloquial que encaje con el personaje:
  - `scoundrels / thieves` → `bribones` (tono coloquial, funciona bien para criminales)
  - `ruthless / merciless` → `despiadados`
  - `guys / people` (informal) → `tipos`
- Diálogos de NPC: tono conversacional acorde al personaje
  - **Wikelo** (The Collector): alien con forma de hablar entrecortada y peculiar. Frases cortas, a veces sin artículo, ritmo telegráfico. Preservar ese estilo aunque suene "raro" — es intencional.
    - `Want big ship? But not too big?` → `¿Quieres nave grande? ¿Pero no demasiado grande?` (no: "¿Quieres una nave grande pero no demasiado?")
- Mantener la estructura de párrafos y listas del original (`\n`, `•`, `>`)
  - **Shattered Blade NPCs**: tono amenazante, confiado, criminal. Hablan con frialdad y superioridad.
    - `Oh bravo, you decrypted the data. Don't make a lick of difference to me.` → `Oh, vaya, descifraste los datos. No cambia nada para mí.`
  - **NPCs de Levski (People's Alliance)**: tono casual, idealistico, anti-UEE. Hablan de forma coloquial y directa.
  - **NPCs militares/policiales (CDF, SAIC, agentes)**: tono seco, directo, protocolo de radio. Usar convenciones de radio en español:
    - `This is X` / `X here` → `Habla X` o `Aquí X` (NO: "Este es X" / "X aquí")
    - `Listen up` → `Atención` o `Escucha` (NO: "Escuchen" — mantener tuteo)
    - `Do you copy?` → `¿Me copias?` o `¿Me recibes?` (NO: "¿Copia?" / "¿Tu copia?")
    - `X here. Listen.` → `Aquí X. Escucha.`
    - `Attention, CDF` (vocativo grupal) → `Atención, CDF`
    - Identificaciones: `SAIC Dulli here` → `SAIC Dulli al habla` / `Special Agent Dulli with the CDF` → `Agente Especial Dulli del CDF`
    - Cierre de radio: `X out.` → `X fuera.` (NO: "Fuera X.") → `Dulli out.` → `Dulli fuera.` / `Ruto out.` → `Ruto fuera.`
    - La CDF como organización: siempre singular → `la CDF` (NO: "las FDC", "la FDC", "FCD")
- **Descripciones de ediciones de cosméticos**: `The X edition features/was styled...` → `La edición X presenta/fue diseñada...`
  - `The Samaritan edition was styled for first responders to be highly visible.` → `La edición Samaritan fue diseñada para que los primeros en responder sean muy visibles.`

#### 5. Capitalización de claves
La capitalización de las claves en es-ES.ini debe seguir **exactamente** la del en-EN.ini. Este es el fichero de referencia. No inventar ni modificar la capitalización de ninguna clave.

#### 5b. Entradas truncadas/incompletas
Durante ediciones manuales o fusiones antiguas pueden aparecer entradas con el valor truncado, normalmente dejando solo `El` o `el` como valor:
```
alguna_clave=El
otra_clave=el
```
Estas entradas deben completarse buscando su equivalente en en-EN.ini y traduciendo desde ahí. **No eliminarlas** — la clave debe existir en es-ES.ini aunque el valor esté incompleto.

Para detectarlas:
```
grep -P '=(?:El|el)$' es-ES.ini
```

#### 5c. Sin tildes (pero con ñ)
Las traducciones del fichero `es-ES.ini` **no usan tildes** pero **sí usan ñ**.
- `a, e, i, o, u` en lugar de `á, é, í, ó, ú`
- La `ñ` sí se escribe: `diseño`, `año`, `señal`, `compañia`, `tecnologia`
- Correcto: `Atencion`, `esta`, `mision`, `seran`, `tecnologia`
- Incorrecto: `Atención`, `está`, `misión`, `serán`, `tecnología`

Esto aplica a **todos los valores traducidos**. Los scripts de busqueda/reemplazo no deben usar tildes en los patrones para evitar problemas de codificacion.

#### 5d. Saltos de línea en valores
El formato `.ini` usa `\n` como **secuencia de escape literal** (dos caracteres: barra invertida + n), no como salto de línea real. Cada entrada ocupa **exactamente una línea** en el fichero.

**MAL** (newline real — rompe el parser):
```
alguna_clave=Primera parte del texto
segunda parte
```
**BIEN** (escape literal):
```
alguna_clave=Primera parte del texto\n\nsegunda parte
```
Al escribir traducciones con scripts Python, usar siempre `\\n` en los strings para evitar que Python interprete `\n` como salto de línea real. Verificar siempre que la entrada siguiente en el fichero sea otra clave válida (`KEY=`).

**Regla crítica al generar el fichero:** Nunca escribas el valor de una clave en múltiples líneas reales aunque el texto sea largo. Todo el contenido de una clave, incluyendo párrafos, debe ir en una sola línea con `\n` literales. Si usas un script o herramienta para escribir las traducciones, asegúrate de que el resultado final sea siempre `CLAVE=todo el texto en una sola línea\n`.

**Verificación de integridad:** Tras escribir el fichero, comprueba que ninguna línea carece de `=` (salvo líneas vacías). Una línea sin `=` indica un salto de línea real que ha roto una clave.

#### 5e. El signo `=` dentro de los valores
El signo `=` puede aparecer como parte del **contenido** de un valor, no solo como separador de clave. El separador es únicamente el **primer** `=` de la línea. Todo lo que va después forma parte del valor, incluidos otros `=`.

Ejemplo real del fichero:
```
alguna_clave=TIPO DE CONTRATO: Recuperar Carga\nCódigo de aprobación: = ~mission(ApprovalCode)\n\n...
```
Aquí `Código de aprobación: = ~mission(ApprovalCode)` es texto del valor — el `=` forma parte del formato del contrato y **no debe eliminarse**. Al traducir o procesar estas claves, conservar siempre el `=` tal como aparece en el original en-EN.

#### 6. Orden de las claves
El orden de las claves en el archivo de salida debe ser **exactamente el mismo que en el en-EN.ini**. No reordenes, no agrupes, no alphabetices.

#### 7. Solo claves nuevas (por defecto)
Salvo que se indique explícitamente lo contrario, **traduce únicamente las claves que no existen todavía en el es-ES.ini**. No modifiques entradas ya traducidas. Si se te pasa el archivo completo en-EN, filtra primero las claves ausentes en es-ES y traduce solo esas.

**Excepción — revisión explícita:** Si el usuario indica que una clave existente tiene una traducción incorrecta o incompleta (p. ej., estaba en inglés sin querer, o es un placeholder), corrígela aunque ya exista.

#### 8. Fichas técnicas de items (bloques de especificaciones)
Los items del juego (radares, armaduras, mochilas, armas, etc.) tienen un bloque de especificaciones al inicio con formato fijo. Traducir siempre con estos términos:

| en-EN | es-ES |
|-------|-------|
| `Item Type:` | `Tipo de objeto:` |
| `Manufacturer:` | `Fabricante:` |
| `Size:` | `Tamaño:` |
| `Grade:` | `Grado:` |
| `Class:` | `Clase:` |
| `Damage Reduction:` | `Reducción de daño:` |
| `Temp. Rating:` | `Clasificación de Temp.:` |
| `Radiation Protection:` | `Protección contra la radiación:` |
| `Radiation Scrub Rate:` | `Tasa de limpieza de radiación:` |
| `Carrying Capacity:` | `Capacidad de carga:` |
| `Core Compatibility:` | `Compatibilidad de torso:` |
| `Backpacks:` | `Mochilas:` |
| Class `Industrial` | `Industrial` |
| Class `Military` | `Militar` |
| Class `Competition` | `Competición` |
| `Heavy Backpack` | `Mochila pesada` |
| `Light Backpack` | `Mochila ligera` |
| `Light Armor` | `Armadura ligera` |
| `Heavy Armor` | `Armadura pesada` |

#### 9. Fin de archivo
El archivo debe terminar con una **nueva línea al final** (no terminar la última línea sin `\n`).

---

### Dificultades de misión

| en-EN | es-ES |
|-------|-------|
| `Easy` | `Facil` |
| `Medium` | `Medio` |
| `Hard` | `Dificil` (NO: "Duro/Dura" — suena a material, no a dificultad) |
| `Cull` (misiones de animales) | `Eliminar` (NO: "Reduccion" — suena administrativo, no a acción) |
| `Major Malfunction` | `Fallo critico` (NO: "Fallo Mayor" — suena a rango militar) |
| `Timed` | `Cronometrado` |
| `Intro` | `Intro` (mantener) |

---

### Glosario de términos establecidos

| en-EN | es-ES                                                                                                                                                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| monorail / monorriel | Monorail                                                                                                                                                                                                                                             |
| to pilot (verb) | pilotar (NO: "pilotear") → `pilotan`, `pilota`, `pilotaba`                                                                                                                                                                                           |
| cargo pod | contenedor de carga                                                                                                                                                                                                                                  |
| fade (barbería/peluquería) | degradado                                                                                                                                                                                                                                            |
| now contracting | abre nuevos contratos                                                                                                                                                                                                                                |
| landing procedure (UI/HUD) | aterrizaje                                                                                                                                                                                                                                           |
| livery / livrea | pintura (preferido); concordancia: "la pintura", "esta pintura", "una pintura"                                                                                                                                                                       |
| Salvaging / salvage (actividad/sector) | Chatarreria (NO: "salvamento"). Ej: "salvage game" → "juego de la chatarreria", "salvage ship" → "nave de chatarreria", "salvage pilots" → "pilotos de chatarreria"                                                                                  |
| Scrap (material de chatarreo) | Scrap (mantener en ingles — es un recurso especifico del juego). Ej: "Scrap Salvage at X" → "Chatarreo de Scrap en X"                                                                                                                                |
| Livery Services | Servicios de transporte                                                                                                                                                                                                                              |
| Quantum Travel / QT | Viaje cuántico / QT                                                                                                                                                                                                                                  |
| CrimeStat | CrimeStat (no traducir). Sin artículo → `¿Cómo diablos conseguiste CrimeStat?` / `tener CrimeStat activo` (no: "una estadística de criminalidad")                                                                                                    |
| OMPoint | PuntoOM                                                                                                                                                                                                                                              |
| Tractor Station | Estación de tracción                                                                                                                                                                                                                                 |
| Offline (UI) | Desconectado                                                                                                                                                                                                                                         |
| Crafted (etiqueta) | FABRICADO                                                                                                                                                                                                                                            |
| operating suite / operating room | quirófano                                                                                                                                                                                                                                            |
| this is not a drill | esto no es un simulacro                                                                                                                                                                                                                              |
| first responders | equipos de primera respuesta / primeros en responder                                                                                                                                                                                                 |
| entry-level | nivel básico                                                                                                                                                                                                                                         |
| eligible / not eligible | apto / no apto (NO: "elegible" — anglicismo). Concordar en genero: apta para sustantivos femeninos                                                                                                                                                   |
| qualifications (contexto laboral/contrato) | historial / expediente (NO: "calificaciones" — suena a notas escolares). Ej: "Your qualifications look good on paper" → "Tu historial parece bueno sobre el papel"                                                                                   |
| outlaw / outlaws | forajido / forajidos (contexto espacial/criminal)                                                                                                                                                                                                    
| criminal (termino legal formal) | delincuente / criminal                                                                                                                                                                                                                               |
| thief / scoundrel (coloquial) | bribón / ratero (segun contexto)                                                                                                                                                                                                                     |
| vicious criminal | forajido despiadado / criminal violento                                                                                                                                                                                                              |
| neutralize (combate) | neutralizar                                                                                                                                                                                                                                          |
| apprehend (contexto policial) | detener / capturar                                                                                                                                                                                                                                   |
| clear [location] of enemies | limpiar [ubicacion] de / despejar                                                                                                                                                                                                                    |
| Data Runner | transporte de datos (NO: "corredor de datos")                                                                                                                                                                                                        |
| Escaped Ships (contador UI) | Naves huidas                                                                                                                                                                                                                                         |
| capable (personas/militares) | competente/competentes (NO: "capaz/capaces" en contextos de personas o agentes). Mantener "capaces" para objetos ("canones capaces de...") y expresiones idiomaticas ("ver de lo que son capaces")                                                   |
| redeem (ticket/bono) | canjear (NO: "convertir")                                                                                                                                                                                                                            |
| Energizing (efecto comida) | Energizante                                                                                                                                                                                                                                          |
| Hyper-Metabolic (efecto comida) | Hipermetabólico                                                                                                                                                                                                                                      |
| None (efectos comida/bebida) | Ninguno                                                                                                                                                                                                                                              |
| cockpit | Cabina                                                                                                                                                                                                                                               |
| airlock | Esclusa                                                                                                                                                                                                                                              |
| docking bay | Bahía de atraque                                                                                                                                                                                                                                     |
| cargo bay | Compartimento de carga                                                                                                                                                                                                                               |
| turret | Torreta                                                                                                                                                                                                                                              |
| engineering | Ingeniería                                                                                                                                                                                                                                           |
| fabrication | Fabricación                                                                                                                                                                                                                                          |
| lounge | Salón                                                                                                                                                                                                                                                |
| messhall | Comedor                                                                                                                                                                                                                                              |
| habitation | Habitación                                                                                                                                                                                                                                           |
| escape pods | Cápsulas de escape                                                                                                                                                                                                                                   |
| gunship | Cañonera (NO: "nave de guerra" — demasiado genérico). Concordancia femenina: "Cañonera pesada"                                                                                                                                                       |
| heavy gunship | Cañonera pesada                                                                                                                                                                                                                                      |
| carrier-based [tipo] | [tipo] de portanaves. Ej: "Carrier-Based Bomber" → "Bombardero de portanaves" (NO: "basado en portador")                                                                                                                                             |
| Scout (rol de nave) | Reconocimiento (NO: dejar en inglés)                                                                                                                                                                                                                 |
| Touring (rol de nave) | dejar en inglés "Touring" (NO traducir — es un término específico del juego que designa un rol de nave, igual que "Snub" o "Scout") |
| Repair (rol de nave) | Reparacion (sustantivo, NO: "Reparar" — infinitivo)                                                                                                                                                                                                  |
| Short Range Patrol | Patrulla de corto alcance (NO: añadir "Caza" si no está en el original)                                                                                                                                                                              |
| UltraLight Ground | Terrestre ultraligero (Ground = terrestre, NO: "Suelo")                                                                                                                                                                                              |
| Snub Fighter | Caza SNUB (mantener SNUB — término específico del juego)                                                                                                                                                                                             |
| slippery (difícil de atrapar, evasivo) | escurridizo (NO: "resbaladizo" — eso es físico, como suelo mojado)                                                                                                                                                                                   |
| slick (apodo/trato coloquial, como "buddy") | listillo (NO: "resbaladizo"). Ej: "Hey, slick." → "Oye, listillo."                                                                                                                                                                                   |
| Slippery [Nombre] (apodo criminal) | [Nombre] el Escurridizo. Ej: "Slippery Mike" → "Mike el Escurridizo"                                                                                                                                                                                 |
| taken care of yesterday / needed yesterday (urgencia extrema) | resuelto para ayer / para ayer (expresión hecha española). Ej: "Need this taken care of yesterday" → "Necesito que esto este resuelto para ayer"                                                                                                     |
| wet work (jerga: asesinato encubierto) | Trabajo Sucio (NO: "trabajo mojado" — calco literal sin sentido)                                                                                                                                                                                     |
| I'll be damned (exclamación de sorpresa/asombro) | Segun contexto: "¡No me lo puedo creer!" (sorpresa positiva), "Anda." (sorpresa contenida), "¿Esto es lo que se siente?" (agonía). (NO: "sere condenado" / "voy a ser condenado" — calco literal sin sentido en español)                             |
| cover (táctica: escudo/cobertura en combate) | cobertura (NO: "portada" — eso es cover de revista/libro)                                                                                                                                                                                            |
| wiped out of existence | desaparezca del mapa (NO: "eliminada de la existencia" — calco literal)                                                                                                                                                                              |
| quantum engines / quantum drives | motores cuanticos (NO: "motores quantums" — mezcla español/inglés)                                                                                                                                                                                   |
| power usage / power consumption | Consumo de energia (NO: "Uso de Energia" — calco de "usage")                                                                                                                                                                                         |
| [faction]_RepUI_Focus sin traducir | traducir siempre. Ej: Advocacy → "Aplicacion de la Ley" (NO: "Enfoque de los Advocacy")                                                                                                                                                              |
| CommRelay (nombre de servicio) | comunicaciones (NO: dejar en inglés "CommRelay")                                                                                                                                                                                                     |
| no longer in active operation | ya no esta operativa (NO: "ya no esta en operacion activa" — calco)                                                                                                                                                                                  |
| Livery / livery (pintura de nave, clave con "Paint" o "Luminalia") | Pintura (NO: "Diseño" ni "decoracion" — ambos son incorrectos). Ej: "100 Series Frostbite Camo Livery" → "Pintura serie 100 Frostbite Camo"                                                                                                          |
| Focal: (campo en descripciones de vehiculos, ej: "Fabricante: ...\nFocal: Caza Medio") | Enfoque: (NO: "Focal:" — calco del inglés "Focus")                                                                                                                                                                                                   |
| Gauntlet (serie de combate) | Guantelete. Ej: "Combat Gauntlet" → "Guantelete de Combate" — SALVO que el proyecto lo tenga establecido como "Desafio", en cuyo caso mantener                                                                                                       |
| Naval (adjetivo militar) | Naval (NO: "de la Armada" — más largo e incorrecto). Ej: "Naval Patrol Training" → "Entrenamiento de Patrulla Naval"                                                                                                                                 |
| Floor [N] (planta de edificio) | Planta [N] (NO: "Piso" — eso es apartamento en español de España)                                                                                                                                                                                    |
| Nombres propios de ubicaciones (Research Outpost, City Gates, etc.) | Mantener en inglés si es el nombre oficial del lugar. NO traducir. Ej: "Hickes Research Outpost" → "Hickes Research Outpost" (NO: "Puesto de investigacion de Hickes")                                                                               |
| was heading to / was en route to | se dirigia a (NO: "estaba en ruta hacia" — calco de "en route")                                                                                                                                                                                      |
| outlaw attack / outlaw activity | ataque de forajidos (NO: "fuera de la ley" — esa es una descripción legal, no un sustantivo)                                                                                                                                                         |
| IAE (Intergalactic Aerospace Expo) | femenino — "la IAE", "durante la IAE", "de la IAE", "celebrar la IAE" (NO: "el IAE", "del IAE")                                                                                                                                                      |
| [vehicle/ship] down (en combate: destruido/derribado) | destruido/a o derribado/a según contexto (NO: "hacia abajo" — calco literal). Ej: "Scan ship down" → "Nave de escaneo destruida"; "Hostile down" → "Hostil abatido"; "Flagship's down" → "La nave insignia ha caido"                                 |
| scan ship (nave dedicada al escaneo en misiones de flota) | nave de escaneo (NO: "escanear la nave" — eso es una acción, no un sustantivo)                                                                                                                                                                       |
| on the run (huida táctica en combate) | en retirada / huyendo (NO: "en la carrera" — calco literal sin sentido)                                                                                                                                                                              |
| move out (orden militar: avanzar/partir) | ¡En marcha! (NO: "Mudarse" — eso es cambiar de domicilio)                                                                                                                                                                                            |
| hostiles inbound / incoming enemies | ¡Hostiles detectados! (NO: "Hostiles entrantes" — suena a llamadas de teléfono)                                                                                                                                                                      |
| quantum dampener (dispositivo que bloquea el viaje cuántico) | inhibidor cuantico (NO: "amortiguador Quantum" — amortiguador es un componente mecánico)                                                                                                                                                             |
| should be approached with caution (advertencia de precaución) | hay que acercarse con precaucion (NO: "deben abordarse" — "abordar" en contexto espacial significa subir a una nave)                                                                                                                                 |
| Go! / Go! Go! Go! (orden urgente de movimiento) | ¡Muevete! / ¡Vamos! (NO: "¡Ir!" — calco literal, no es natural en español)                                                                                                                                                                           |
| Ready up / Ready or not (preparación/transición) | Preparado o no / Atencion (NO: "Listo" como calco de "ready up" — "listo" en español solo significa "ready" en primera persona)                                                                                                                      |
| on the way / inbound (refuerzos llegando) | Llega el refuerzo / de camino (NO: "en camino" como calco de "on the way" en frases cortas de radio)                                                                                                                                                 |
| pronombre sujeto (yo/nosotros/ellos) | omitir siempre salvo ambigüedad — el español no necesita pronombre sujeto explícito. Ej: "Nosotros hemos terminado" → "Hemos terminado"; "Ellos son míos" → "Son míos"                                                                               |
| worn out their welcome (ha agotado la paciencia ajena) | se ha pasado de la raya (NO: "ha agotado su bienvenida" — calco literal sin sentido en español)                                                                                                                                                      |
| Word is that / Word has it (coloquial: se dice que) | Parece que / Segun nuestros informes (NO: "La palabra es que" — calco literal del inglés)                                                                                                                                                            |
| naughty list (lista de personas non gratas) | lista negra (NO: "lista de no gratos" — calco literal)                                                                                                                                                                                               |
| hardly a surprise / it's hardly surprising | No es de extrañar (NO: "Apenas es sorprendente" — calco literal; en español "apenas" modifica cantidad, no probabilidad)                                                                                                                             |
| caution is advised / so exercise caution (advertencia informal) | ten cuidado / procede con precaucion (NO: "se aconseja precaucion" — pasiva impersonal innecesaria en texto informal)                                                                                                                                |
| rich in material (contexto minero/asteroide) | rico en recursos (NO: "rico en material" — "material" en español no equivale a materia prima minera). Distinguir: "rich in ore" → "rico en mineral"; "rich in minerals" → "rico en minerales"                                                        |
| personally (adverbio de modo: él mismo, en primera persona) | personalmente (NO: "en persona" — reservar "en persona" solo para presencia física: "quedar en persona", "conocerse en persona")                                                                                                                     |
| there is a strong chance / there is a good chance | es muy probable que (NO: "hay una fuerte posibilidad de que" — calco literal)                                                                                                                                                                        |
| the station itself / la propia estacion | la propia estacion (NO: "la estacion misma" — suena a énfasis arcaico; "misma" es válido solo con pronombre: "ella misma")                                                                                                                           |
| that particular area / that area in particular | esa zona / esa area (NO: "esa area en particular" — "en particular" es redundante cuando el contexto ya lo precisa)                                                                                                                                  |
| [adjective] problems (ej: serious problems) | [adjetivo] + problemas con adjetivo delante: "serios problemas" (NO: "problemas serios" — el orden inglés SN+adj suena a calco; en español el adj valorativo va delante)                                                                             |
| we will offer you payment / you will receive payment | te compensaremos / recibirás pago (NO: "te ofreceremos pago" — calco de "offer payment"; en español se usa el verbo directamente)                                                                                                                    |
| double "para" (para X para Y) | restructurar: "para dejar X listo para su reparacion" → "para dejar X listo de cara a su reparacion" o reformular con "con vistas a"                                                                                                                 |
| cull / culling (fauna invasora) | reducir su poblacion / eliminar ejemplares (NO: "controlar su poblacion" — "controlar" implica gestión, no matanza)                                                                                                                                  |
| there's a good/strong chance (that) | es probable que / es muy probable que / probablemente (NO: "hay una buena/fuerte posibilidad de que" / "hay muchas posibilidades de que" — calco de "there is a chance")                                                                             |
| backup (militar: refuerzos) | refuerzos (NO: "copia de seguridad" — eso es backup de datos informáticos)                                                                                                                                                                           |
| ace pilot (piloto experto/de élite) | piloto de elite (NO: "piloto as" — "as" es anglicismo; NO: "piloto estrella" — suena a celebrity)                                                                                                                                                    |
| So what. (desafío/indiferencia) | ¿Y que? (NO: "Asi que lo que" — calco literal sin sentido)                                                                                                                                                                                           |
| shot (disparo, impacto balístico) | disparo / impacto (NO: "foto" — eso es photograph)                                                                                                                                                                                                   |
| turning on [facción] (traicionar) | traicionando a [faccion] (NO: "activando" — eso es encender un dispositivo)                                                                                                                                                                          |
| scrap (pelea informal, bronca) | pelea / bronca (NO: "desecho" — eso es waste/junk material)                                                                                                                                                                                          |
| You're done. (amenaza: estás acabado) | Estas acabado. (NO: "Ya terminaste" — eso es pasado, implica que ya acabó algo, no amenaza)                                                                                                                                                          |
| feed you your teeth (amenaza violenta) | hacerte tragar tus propios dientes (calco aceptable con "propios" añadido para sonar más natural)                                                                                                                                                    |
| Fight it is. / Then we fight. | Entonces pelea. / A pelear se ha dicho. (NO: "Lucha es" — calco literal sin estructura española)                                                                                                                                                     |
| deal with you (combate, confrontación) | enfrentarse a ti / encargarse de ti / vérselas contigo (NO: "tratar contigo" — en español "tratar con alguien" es negociar, no combatir)                                                                                                             |
| at this very moment / right this moment | ahora mismo / en estos momentos / en ese instante (NO: "en este mismo momento" / "en ese mismo momento" — calco de "at this very moment", redundante en español)                                                                                     |
| Scorch (apodo/callsign de piloto Nine Tails) | Scorch — NO traducir jamás (NO: "Quemador", "Chamuscado" — es un nombre propio, igual que Stax o Acker)                                                                                                                                              |
| "This is X with [company]" / "[Name] here with [company]" (presentación en radio/comms) | "Habla X, de [company]" / "Aquí X, de [company]" (NO: "con [company]" — "con" implica compañía física, no afiliación). Ej: "This is Riegert with BlacJac" → "Habla Riegert, de BlacJac"; "Here with BlacJac" → "de BlacJac" |
| Lead Dispatcher (Citizens for Prosperity) | Coordinadora de misiones (NO: "Despachadora Principal" — calco literal; NO: "Jefa de despachos" — demasiado literal) |
| disrupt (sabotaje/acción encubierta contra infraestructura) | sabotear (NO: "perturbar" — suena abstracto; NO: "disrumpir" — anglicismo inválido). Ej: "disrupt their base of operations" → "sabotear su base de operaciones" |
| accents (diseño/acabado de armadura, nave o vehículo) | detalles (NO: "acentos" — en español "acento" es lingüístico, no de diseño). Ej: "red accents" → "detalles rojos"; "gold accents" → "detalles dorados" |
| search (contexto de investigación/inspección de lugar) | registrar / investigar / examinar (NO: "buscar" — "search" en investigación policial/espacial implica inspeccionar el lugar, no solo buscar algo). Ej: "Search the hub" → "Registra el hub"; "Search for clues" → "Investiga la zona" |
| evidence (contexto policial/investigación) | pruebas / prueba encontrada (NO: "evidencia" — en español "evidencia" es de uso científico; en investigación policial se dice "pruebas"). Ej: "Evidence found" → "Prueba encontrada"; "submit evidence" → "presentar pruebas" |
| Nombres propios de instalaciones/ubicaciones del juego (Covalex Shipping Hub, etc.) | Mantener en inglés — NO traducir nombres propios de instalaciones. Ej: "Go to Covalex Shipping Hub" → "Ve al Covalex Shipping Hub" (NO: "Centro de envio de Covalex") |
| Imperativos en objetivos de misión (verbos de acción) | Usar formas naturales del español: registrar, investigar, examinar, localizar, entrar (NO: "Busque", "Ubique", "Ingrese" — suenan a calco formal del inglés) |
| burner (argot: información/oportunidad caliente) | algo jugoso / oportunidad de primera / soplo (NO: "quemador" — false friend; "burner" en jerga significa "insider tip", no el aparato ni el apodo Scorch)                                                                                            |
| Right. (sarcástico, respuesta de relleno) | Ya, claro. (NO: "Derecho" — eso es "straight/upright"; en contexto sarcástico: "Ya, claro." / "Como no.")                                                                                                                                            |
| You don't say? (sarcástico) | ¿No me digas? (NO: "¿No lo dices?" — calco literal sin sentido en español)                                                                                                                                                                           |
| Yeah right. (sarcástico: "sí, ya") | Si, claro. / Venga, ya. (NO: "Si cierto" — falta puntuación y suena a afirmación sincera)                                                                                                                                                            |
| Like now / like right now (urgencia coloquial) | ahora mismo (NO: "como ahora" — calco literal; "like" coloquial de urgencia no se traduce)                                                                                                                                                           |
| stuff's gonna go down (amenaza: las cosas se van a poner feas) | las cosas se van a poner feas (NO: "las cosas van a bajar" — calco de "go down")                                                                                                                                                                     |
| pissed (enfadado, muy cabreado) | cabreado/a (NO: "enojado" — demasiado suave para el registro coloquial de "pissed")                                                                                                                                                                  |
| Functional to a fault (excesivamente funcional, idiom) | Funcional hasta el extremo (NO: "Funcional a una falla" — calco literal sin sentido)                                                                                                                                                                 |
| Concordancia de género con «nave» (femenino) | Todos los adjetivos y pronombres que acompañen a «nave» deben ir en femenino: "una nave bonita", "esta podria ser la nave que deseas", "pocas naves", "la adecuada", "esta nave es perfecta" (NO: "bonito", "este", "pocos", "el adecuado", "perfecto") |
| cap ships | naves capitales (NO: "naves de tapa" — calco literal de "cap")                                                                                                                                                                                       |
| gunship (nave de combate pesada) | cañonera (NO: "helicoptero de combate" — un helicoptero vuela en atmosfera, no en el espacio)                                                                                                                                                        |
| a real rush (emoción, subidón) | un subidón de verdad (NO: "una verdadera prisa" — "prisa" = hurry, no rush/thrill)                                                                                                                                                                   |
| ass whoopin / ass kicking (paliza, zurra) | una buena paliza / una tunda de verdad (NO: "grito de culo" — no tiene sentido en español)                                                                                                                                                           |
| a big F you / middle finger (gesto de desprecio) | un corte de mangas (expresión española equivalente al "F you" anglosajón)                                                                                                                                                                            |
| sit back, take in the space and let your ship call to you | tomarselo con calma, sentir el espacio y esperar a que una nave te hable (NO: "absorber el ambiente y dejar que la nave te llame" — forzado) |
| I'll leave you to it (despedida informal) | Te dejo tranquilo (NO: "Te dejo con eso" — calco de "leave you to it") |
| Too much too soon (demasiado rápido, coloquial) | Demasiado, demasiado pronto (NO: "Ok seguro Demasiado..." — falta puntuacion; usar "Vale" no "Ok") |
| Got it. (entendido, coloquial) | Entendido. (NO: "Lo tengo" — calco literal) |
| just slip past (colarse/pasar de lado) | pasar un momento / pasar por tu lado (NO: "pasar simplemente"; NO: "deslizarte por ti" — error de reflexividad) |
| fortitude (resistencia, aguante — contexto de durabilidad de nave) | aguante (NO: "fortaleza" — en español "fortaleza" evoca una construcción física o virtud moral elevada, no la resistencia continua de una máquina) |
| grind away for hours / eat that up and ask for more (trabajar sin parar y aguantarlo todo) | echarle horas y mas horas / tragarselo todo y pedir mas (NO: "molerla" — suena a triturar físicamente; NO: "comérselo" — en este contexto suena raro) |
| you'll be peeling metal (hipérbole de velocidad extrema, rozar estructuras) | vas a salir echando chispas (NO: "pelando metal" — calco literal sin gracia en español; NO: "raspando paredes" — demasiado literal) |
| easiest move (mudanza, relocation — no confundir con maniobra) | mudanza mas facil (NO: "movimiento mas facil" — "movimiento" es maniobra/gesto, no mudanza) |
| check out the simcab (probar la cabina de simulador) | probar la cabina de simulador (NO: "consultar la cabina" — "consultar" implica buscar información, no experimentar algo) |
| Concordancia de demostrativos con «nave» | Usar "esta/estas/una/algunas" (NO: "este/estos/uno/algunos" — la nave es femenino aunque el nombre propio parezca masculino: "esta Avenger", "una de estas", "esta es la nave") |
| Concordancia de cuantificadores con «naves» (plural) | "cuantas naves", "todas las naves", "otras naves" (NO: "cuantos naves", "todos los naves", "demas naves") |
| Nombres de naves no se traducen aunque tengan equivalente en español | Mantener en inglés: Avenger (NO: "Vengador/Vengadores"), Mercury (NO: "Mercurio"), Retaliator (NO: "represalia"), Vulcan (NO: "Vulcano") — son nombres propios de naves, no descripciones |
| Orden del nombre de nave: fabricante + nombre | Aegis Vulcan (NO: "Vulcano de Aegis" — el orden en español sigue el original inglés sin preposición) |
| sleep on something (idiom: subestimar, pasar por alto) | pasar por alto / subestimar (NO: "dormir en" — calco literal sin sentido; "sleep on X" = no darle el mérito que merece) |
| you need to bomb something yesterday (expresión: lo necesitas para ayer) | necesitas bombardear algo para ayer (NO: "la semana pasada" — "yesterday" en este idiom = urgencia inmediata, no literalmente ayer ni la semana pasada) |
| it's a killer / it's deadly (referido a una nave) | es una asesina / es letal (NO: "es un asesino" — concordar con nave en femenino) |
| looking into X (estar interesado en, estar considerando) | ¿X, eh? / ¿Interesado en X? (NO: "mirando en X" — calco literal; "look into" = considerar/explorar, no mirar dentro de) |
| Fast, lean, stripped down (descripción de naves ligeras) | Rapidas, ligeras y sin florituras (NO: "Rapido, delgado y sencillo" — concordar en femenino plural con "naves"; "stripped down" = sin florituras, no "simple/sencillo") |
| Center Mass (nombre de tienda) | CenterMass (NO: "Centro de Misa" — nombre propio, no traducir; "mass" aquí es centro de gravedad, no misa religiosa) |
| creep (persona que da mal rollo, merodeador) | bicho raro (NO: "canalla" — "canalla" implica maldad/villanía, "creep" es alguien que da escalofríos o merodea de forma inquietante) |
| Can't get enough, huh? (dirigido al cliente que vuelve) | ¿No tienes suficiente, eh? (NO: "No puedo tener suficiente" — primera persona errónea; el dependiente interpela al cliente, no habla de sí mismo) |
| Go. Just go. Stop looking and go. (dependiente hastiado echando al cliente) | Vete. Simplemente vete. Deja de mirar y vete. (NO: "Ir. Solo vamos." — infinitivos y primera persona del plural sin sentido) |
| cover (cobertura táctica en combate) | cobertura (NO: "portada" — portada es la cubierta de un libro o revista; la cobertura táctica es siempre "cobertura") |
| We've been breached! (han entrado por la fuerza) | ¡Han entrado! (NO: "¡Hemos sido violados!" — "violar" tiene connotación sexual; NO: "¡Nos han infiltrado!" — "infiltrar" implica espionaje/sigilo, no irrupción por la fuerza) |
| bagged one (se cargaron a uno, lo abatieron) | se cargaron a uno (NO: "se embolsaron uno" — calco de "bag"; en español "cargarse a alguien" = eliminarlo) |
| We're moving out! (orden militar de partida) | ¡En marcha! (NO: "Nos estamos mudando" — "mudarse" = cambiar de domicilio, no desplazarse en combate) |
| fan out (dispersarse tácticamente) | Dispersemonos. (NO: "Vamos a admirar" — "admirar" = to admire, no tiene nada que ver con "fan out") |
| die trying (idiom: morir en el intento) | morir en el intento (NO: "morir intentando" — calco literal; la expresión hecha en español es "morir en el intento") |
| Contact ahead. (avistamiento militar: hay contacto por delante) | Contacto adelante. (NO: "Contacta con antelacion" — "contact" aquí es un sustantivo militar, no un verbo) |
| They mean business (van en serio, no es un juego) | van en serio (NO: "significan negocios" — calco de "mean business"; en español "ir en serio" transmite la misma amenaza) |
| kill the crap out of something (destruir completamente, intensificador coloquial) | dejar para el arrastre / destrozar (NO: "matar la basura de" — calco literal sin sentido; "kill the crap out of" = arrasar con algo) |
| it was nice of you to try (fue un gesto/detalle intentarlo) | estuvo bien por tu parte intentarlo (NO: "fue muy amable de tu parte" — "amable" implica cortesía formal; aquí se expresa apreciación por el esfuerzo, no por los modales) |
| Unless you've got a death wish (amenaza: como no quieras morir) | Como no quieras acabar muerto (NO: "A menos que tengas deseos de morir" — demasiado formal y literal; la amenaza en español se expresa de forma más directa) |
| turn that ship around (dar media vuelta con la nave) | dar media vuelta (NO: "darle la vuelta a la nave" — ambiguo, podría interpretarse como voltear la nave; "dar media vuelta" es la expresión natural de retroceder) |
| Screw it (expresión de hartazgo/abandono) | ¡Al diablo! (NO: "Atornillarlo" — calco literal de "screw"; en español "screw it" = desestimar algo con frustración) |
| Look sharp (alerta táctica: estar atentos) | ¡Atentos! (NO: "Mira agudo" — calco literal sin sentido; "look sharp" = estar alerta/preparado) |
| We're down a ship (perdimos una nave en combate) | Perdimos una nave (NO: "Estamos en una nave" — "down" aquí significa que falta una unidad, no que están dentro) |
| got the drop on us (nos pillaron desprevenidos, sorpresa táctica) | Nos pillaron desprevenidos (NO: "tienen la gota sobre nosotros" — calco literal de "drop"; "get the drop on" = coger por sorpresa) |
| missing them (errar los tiros, no acertar) | errando los tiros (NO: "extrañarlos" — "miss" en contexto de disparo = fallar el tiro, no echar de menos a alguien) |
| dead to rights (pillado sin escapatoria, cazado) | me tiene pillado (NO: "muerto a los derechos" — expresión idiomática; "dead to rights" = atrapado sin argumentos posibles) |
| quitter (cobarde que abandona, rajado) | rajado (NO: "dejar de fumar" — "quit" aquí no es dejar el tabaco sino rajarse/abandonar; "quitter" = persona que no aguanta) |
| Missile away (misil lanzado, comunicación táctica) | ¡Misil lanzado! (NO: "Misiles lejos" — plural incorrecto + calco de "away"; en contexto táctico = confirmación de lanzamiento) |
| That's a friendly / friendly fire (aliado, unidad propia) | ¡Es de los nuestros! (NO: "es un amistoso" — calco de "friendly"; en español militar "de los nuestros" = unidad aliada) |
| hack down CrimeStat / clear CrimeStat (reducir/borrar el registro criminal hackeando una terminal) | borrar su CrimeStat (NO: "hackee su CrimeStat" — "hackear" es el acto, pero la acción concreta es borrar/reducir el registro; más claro y natural) |
| opportunity (en títulos de contrato/misión) | oportunidad (NO cambiar a "puesto" — respetar siempre el término original si el en-EN dice "opportunity") |
| nombres de lugares como destino de acción (protect X, defend X) | sin preposición "a" antes del lugar — los topónimos no llevan "a personal". Ej: "protect Kareah" → "proteger Kareah" (NO: "proteger a Kareah" — la "a personal" es para personas, no lugares) |
| Comm Array / comm array | mantener en inglés — es un nombre propio. Capitalización según el original: "Comm Array" en UI formal, "comm array" en diálogos/terminales. Artículo "el/un". Ej: "Disable uplink at Comm Array 625" → "Desactiva la conexion en el Comm Array 625"; "Hack a comm array" → "Piratea un comm array" (NO: "matriz de comunicaciones") |
| Imperativo en objetivos de misión | usar siempre 2ª persona del singular informal (tú): "Viaja", "Localiza", "Protege", "Contacta", "Elimina" (NO: "Viaje", "Localice", "Proteger", "Informe" — son formas de usted/infinitivo, incorrectas en objetivos dirigidos al jugador) |
| Report to [NPC/lugar] (objetivo de misión) | Contacta con [NPC/lugar] (NO: "Informe a" — "informar" en imperativo de usted suena arcaico y formal) |
| Travel to [ubicación] (objetivo de misión) | Viaja a [ubicacion] (NO: "Viaje a" — usted formal; NO: "al [código]" — usar "en [código]" para coordenadas/identificadores) |
| [verbo en infinitivo] como objetivo de misión | convertir a imperativo informal. Ej: "Proteger al civil" → "Protege al civil"; "Localizar restos" → mantener infinitivo solo en _Short, imperativo en _Long |
| pirate threat attacking X (amenaza pirata atacando) | los piratas que atacan X (NO: "la amenaza pirata atacando" — gerundio adjetival incorrecto en español; usar oración de relativo) |
| uplink (en contexto de Comm Array/misiones) | conexion (NO: "enlace ascendente" — calco técnico que suena raro en español) |

---

### Ejemplos de referencia

| en-EN | es-ES |
|-------|-------|
| `Expo-hall Day 01` | `Expo - Dia 01` |
| `Best of Show` | `Lo mejor del evento` |
| `WIP - Protect the VIP` | `WIP - Protege al VIP` |
| `CLOSE` (airlock) | `CERRADO` |
| `CYCLE AIRLOCK` | `CICLAR ESCLUSA` |
| `PRESSURIZED` | `PRESURIZADO` |
| `CYCLING COMPLETE` | `CICLADO COMPLETADO` |
| `RDR LOCK` | `BLOQUEO RDR` |
| `Remain Where You Are, Arrest In Progress` | `Permanece detenido, arresto en curso` |
| `Drop off black box.` | `Dejar la caja negra.` |
| `Have any work?` | `¿Tiene algun trabajo?` |
| `Breaker Station` | `Breaker Station` (nombre propio, NO traducir) |
| `The Endeavor is less of a ship and more of a roaming university` | `La Endeavor es, mas que una nave, una universidad volante` — nave científica de RSI |
| `you sail one to a teammate and they just tap it in` (Sataball) | `le mandas un pase perfecto a un compañero y el lo mete sin esfuerzo` (NO: "le envias uno y lo toca" — demasiado literal, pierde la imagen del pase fluido) |
| `taking care of business` (coloquial: funcionando a tope, sin que nadie los pare) | `no hay quien los pare` (NO: "se ocupan de sus asuntos" — calco que suena a burocracia, no a combate) |
| `less of a X and more of a Y` (estructura comparativa) | `mas que una X, una Y` (NO: "menos una X y mas una Y" — calco literal que suena raro en español) |
| `scientific vessel` (en contexto Endeavor) | `nave cientifica` — femenino: "esta es la que quieres", NO "este es el que quieres" |
| `Metro Center` | `Metro Center` (NO: "Centro del Metro") |
| `Teasa Spaceport` | `Teasa Spaceport` (NO: "Espaciopuerto Teasa") |
| `Last Ditch on Monox (Pyro II)` | `Last Ditch en Monox (Pyro II)` — `on` → `en` en ubicaciones (`mission_location_*`) |
| `Keene, Killian System` | `Keene, Sistema Killian` |
| `New York, Earth, Sol System` | `Nueva York, La Tierra, Sistema Solar` |
| `Salvaging` | `Chatarreria` |
| `Livery Services` | `Servicios de transporte` |
| `Tractor Station` | `Estación de tracción` |
| `- Offline -` | `- Desconectado -` |
| `OMPoint 2` | `PuntoOM 2` |
| `Vanduul Swarm` | `Enjambre Vanduul` |
| `gravity generator` | `Generador de gravedad` |
| `ladder access` | `Acceso por escalera` |
| `secure storage` | `Almacenamiento seguro` |
| `repair bay` | `Bahía de reparación` |
| `elevator shaft` | `Eje del ascensor` |
| `command module docking` | `Conector del módulo de mando` |
| `operations deck` | `Cubierta de operaciones` |
| `owner's room` | `Camarote del propietario` |

---

### Entradas a traducir

Pega aquí las líneas del `en-EN.ini` que quieres traducir:

```
CLAVE1=Texto en inglés
CLAVE2=Otro texto en inglés
```

Devuelve únicamente las líneas traducidas en el mismo formato `CLAVE=traducción`, sin explicaciones adicionales salvo que encuentres ambigüedad que requiera comentario.
