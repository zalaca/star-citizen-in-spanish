# SKILL: Traducción SC en-EN → es-ES

## ⚠ REGLAS CRÍTICAS (leer siempre primero)

- **Placeholders: NUNCA modificar** — `~mission(NombreVariable)`, `%ls`, `%d`, `%s`, `%S`, `%i`, `%Is` se copian exactamente como están, incluyendo mayúsculas. Nunca inventar placeholders que no existan en en-EN.
- **`\n` son literales** — dos caracteres `\` + `n`, nunca un salto de línea real. Cada clave ocupa exactamente una línea.
- **Orden de claves = en-EN.ini** — no reordenar, no agrupar, no alphabetizar.
- **Tildes y ñ SÍ se usan** — `á, é, í, ó, ú, ñ` son correctas en todos los valores.
- **Antes de traducir: leer la clave en en-EN.ini** — el contexto original es imprescindible.
- **Español de España (castellano)** — nunca variantes latinoamericanas.
- **Tutear al jugador** — tú, no usted.

---

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
  - **Listado de naves conocidas** — todas femeninas, ninguna se traduce. Ver [Apéndice: Lista de naves](#apéndice-lista-de-naves) al final del documento.
- **Género de otras entidades** — referencia rápida para concordancia:

  | Sustantivo | Género | Ejemplos |
  |-----------|--------|---------|
  | estación / instalación | Femenino | la estación Kareah, la instalación minera |
  | outpost / puesto avanzado | Masculino | el outpost de Shubin, un puesto avanzado |
  | planeta | Masculino | el planeta ArcCorp, Hurston es hostil |
  | sistema (estelar) | Masculino | el sistema Stanton, el sistema Pyro |
  | punto de salto | Masculino | el punto de salto a Pyro |
  | flota | Femenino | la flota enemiga, una flota potente |
  | escuadrón / escuadrilla | Masculino / Femenino | el escuadrón de ataque, la escuadrilla de caza |
  | cinturón (asteroidal) | Masculino | el cinturón Keeger, un cinturón de asteroides |

- **Combate**: espacial (dogfights, misiles, torpedos) y FPS en superficie. Mezcla PvP y PvE.
- **Economía**: minería, transporte de mercancías, contratos mercenarios, recompensas.
- **Personalización**: pinturas y diseños de naves, equipamiento y apariencia del personaje.
- **Entornos**: planetas con clima dinámico, ciudades, outposts, estaciones mineras. Los viajes usan `quantum drive` y puntos de salto.

**Tipos de texto:** misiones/contratos, lore (logs, datapads), descripciones de naves y equipamiento, UI/HUD compacta, diálogos de NPC, perfiles de facciones.

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
  - `Shattered Blade` (artículo masculino plural → `los Shattered Blade`, NO: "Espada Fragmentada")
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
  - `People's Service Station X` (estaciones sociales de Nyx: Alpha, Delta, Theta, Lambda, Omicron) — mantener siempre el nombre completo en inglés; solo traducir la parte contextual de ubicación (ej: "People's Service Station Alpha en el cinturón Keeger") (NO: "Estacion de Servicio Popular Alfa")
  - `Starmap` (mapa de navegación del juego) — mantener siempre en inglés (NO: "mapa estelar", "mapa Starmap")
- Items y documentación del juego: `Blueprint`, `Blueprints` — mantener en inglés (NO: "Plano/s")
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
  - `nice one` (exclamación de aprobación en combate/acción) → `¡Buena!` (NO: "Bonita" — calco literal de "nice")
  - `we're clear` (zona libre de amenazas, contexto militar/aviación) → `Zona despejada.` (NO: "Estamos libres" — calco)
  - `stay sharp` / `look sharp` → `estate alerta` (NO: infinitivo "estar atento" — [I]; NO: "mirada aguda" — calco literal)
  - `ease up` (reducir intensidad) → `afloja` (NO: infinitivo "suavizar" — [I])
  - `blow by blow` (descripción detallada en deportes o combate) → `golpe a golpe` (NO: "paso a paso" — calco de "step by step", significado diferente)
  - `point to us` / `point to them` (marcador deportivo) → `punto para nosotros` / `punto para ellos` (NO: "señalar a nosotros" — calco literal)
  - `falling in on your position` (unirse a formación militar) → `Incorporándome a tu posición.` (NO: "Caer en tu posición" — calco literal)
  - `swarmed` en contexto militar → `rodeados` (no: "enjambrados")
  - `ghost` / `ghosted` (verbo de combate: matar/destruir) → `eliminar`, `liquidar`, `matar`, `destruir` según contexto (NO: "fantasma" — error de traducción literal del sustantivo)
    - `Ghost 'em!` → `¡Elimínalos!`
    - `Who ghosted this bastard?` → `¿Quién ha matado a este bastardo?`
    - `just got ghosted` (nave) → `acaban de destruirla` / (persona) → `acaban de matarlo`
  - `bogey` / `bogie` (aviación: contacto hostil no identificado) → mantener como `bogey` (NO: "fantasma")
  - `overwhelmed` (servicios/instalaciones saturados) → `desbordado/desbordadas` (no: "abrumado" — suena latinoamericano). Ej: "medical facilities overwhelmed" → "instalaciones médicas desbordadas"
  - `overwhelmed` (persona agobiada, contexto personal) → `agobiado` (no: "abrumado")
  - `overwhelmed` (en combate, superado por el enemigo) → `superado` / `desbordado` (no: "abrumado")
  - `overwhelming` (adjetivo de intensidad militar: probabilidades, fuerza, evidencia) → `aplastante` / `arrollador` (no: "abrumador" — aceptable pero menos natural en España)
  - `as well as` → `además de` / `y` (NO: "así como" cuando es mera adición, no comparación)
  - `in addition to` → `además de` (NO: "en adición a" — anglicismo)
  - `at your earliest convenience` → `cuando puedas` / `a la mayor brevedad` (NO: calco literal "a tu conveniencia más temprana")
  - `you are required to` → `debes` / `tienes que` (NO: "se te requiere que" — impersonal forzado)
  - `worth it / worth the risk` → `merece la pena` / `vale la pena` (NO: "vale eso" / "vale el riesgo" — calco de "it's worth it")
  - `on a regular basis` → `habitualmente` / `con regularidad` (NO: "en una base regular" — calco directo)
  - `going forward / moving forward` → `a partir de ahora` / `en adelante` (NO: "yendo hacia adelante" — calco)
  - `there is no doubt` → `sin duda` / `no hay duda de que` (NO: "no hay ninguna duda que" — falta "de")
  - `due to the fact that` → `debido a que` / `porque` / `ya que` (NO: "debido al hecho de que" — calco verboso)
  - `in the event that` → `si` / `en caso de que` (NO: "en el evento de que" — calco directo)
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
    - `Dispatch` (vocativo de radio, al llamar a central) → `Central` (NO: "Despacho", "Envio") → `Dispatch, we have a contact` → `Central, tenemos un contacto`
- **NPCs criminales específicos — perfiles de voz:**
  - **Ruto** (`PU_RUTO_*`, `mg_ruto_*`): fixer criminal con cara holográfica de celebridad. Tono frío y calculador, coloquial pero profesional. Primera persona siempre. Mucho slang criminal (ver tabla de slang). Broker de Nine Tails en Grim HEX.
    - `It's Ruto. We need to talk.` → `Aquí Ruto. Necesitamos hablar.`
    - `Clock's ticking on that job.` → `El reloj corre en ese trabajo.`
    - `Need someone to boost the stuff.` → `Solo necesito a alguien para ejecutarlo.`
  - **Eddie Parr** (`PU_PARR_*`): bartender e informante en Wally's (MicroTech). Tono muy coloquial, mucho slang callejero, lenguaje de barrio. Usa "jam", "tight", "score", "lit", etc. Ver tabla de slang.
    - `This is my jam.` → `Esto es lo mío.`
    - `¡Score!` → `¡Premio!`
    - `You're lit.` → `Estás hasta arriba.`
  - **Shaw** (`PU_SHAW_*`): contrabandista en Hurston. Tono ansioso y nervioso pero directo. Simpatizante de los trabajadores, mueve suministros de contrabando. Frases cortas, urgente, preocupada.
    - `Watch yourself.` → `Cuídate.`
    - `Got a shipment I need brought in. Keep a low profile.` → `Tengo un envío que necesito que me traigas. Mantén un perfil bajo.`
  - **Battaglia (Recco)** (`PU_BATTAGLIA_*`): broker de minería, pragmático y profesional. Tono calmado, honesto, directo. Habla como un empresario independiente de zona minera.
    - `Fly safe.` → `Vuela con cuidado.`
    - `Keep your wits, you hear?` → `Mantén los ojos abiertos, ¿entiendes?`

- **Descripciones de ediciones de cosméticos**: `The X edition features/was styled...` → `La edición X presenta/fue diseñada...`
  - `The Samaritan edition was styled for first responders to be highly visible.` → `La edición Samaritan fue diseñada para que los primeros en responder sean muy visibles.`
  - **NPCs corporativos (ArcCorp, Hurston Dynamics, microTech)**: tono formal y corporativo. Lenguaje de marketing pulido, con frases largas y vocabulario de empresa. Evasivos cuando conviene.
    - `Your productivity is our priority.` → `Tu productividad es nuestra prioridad.`
    - `Our records indicate no current openings...` → `Nuestros registros no muestran vacantes disponibles actualmente...`
  - **NPCs piratas/criminales genéricos**: tono agresivo, directo, amenazante. Pocas palabras, mucha presión. Pueden ser bruscos y maleducados.
    - `You picked the wrong ship to mess with.` → `Elegiste la nave equivocada para meterte con ella.`
    - `Hand it over. Now.` → `Suéltalo. Ahora.`
  - **NPCs mercaderes/comerciantes**: tono pragmático y amistoso interesado. Directos y cordiales. Orientados al trato, a cerrar la venta o a conseguir el encargo.
    - `Best prices in the system, guaranteed.` → `Los mejores precios del sistema, garantizado.`
    - `I've got exactly what you're looking for.` → `Tengo justo lo que buscas.`
  - **NPCs cazarrecompensas**: tono profesional y frío. Hablan de misiones como transacciones sin emoción. Registro semi-militar, tecnicismos de caza.
    - `Target acquired. Preparing for extraction.` → `Objetivo localizado. Preparando extracción.`
    - `Contract fulfilled.` → `Contrato cumplido.`

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

#### 5c. Tildes y ñ
**En traducciones nuevas, usar tildes y ñ con normalidad** — `á, é, í, ó, ú, ñ` son correctas y deben incluirse donde corresponda gramaticalmente.

- No modificar claves existentes solo para añadir o corregir tildes — solo corregir errores sustanciales de traducción.
- En revisiones masivas, no tocar acentuación de entradas ya existentes.
- **Al hacer una corrección sustancial en una clave existente** (tuteo, calco, significado, puntuación rota…), cambiar únicamente lo imprescindible para esa corrección — no añadir tildes de paso a otras palabras de la misma línea que no las tenían.

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

**Strings multilínea en Python:** Si construyes el valor de una clave como un string Python con saltos de línea reales (con triples comillas `\"\"\"...\"\"\"`  o concatenaciones con `\n`), el resultado escrito en el fichero tendrá newlines reales y romperá el parser. Usar siempre strings raw con `r'...'` y `\\n` explícitos, o bien construir el valor como una sola cadena y hacer `.replace('\n', '\\n')` antes de escribirlo. Tras cualquier escritura masiva, verificar con `grep` que no existen líneas sin `=`:

**Regla crítica al generar el fichero:** Nunca escribas el valor de una clave en múltiples líneas reales aunque el texto sea largo. Todo el contenido de una clave, incluyendo párrafos, debe ir en una sola línea con `\n` literales. Si usas un script o herramienta para escribir las traducciones, asegúrate de que el resultado final sea siempre `CLAVE=todo el texto en una sola línea\n`.

**Verificación de integridad:** Tras escribir el fichero, comprueba que ninguna línea carece de `=` (salvo líneas vacías). Una línea sin `=` indica un salto de línea real que ha roto una clave.

**Fidelidad estructural al en-EN:** No añadas `\n` adicionales respecto al original inglés por razones estéticas. La estructura de párrafos y saltos de línea del en-EN es la referencia. Añadir `\n` extra donde el inglés no los tiene es un error de traducción.

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

**Bloques añadidos por el traductor:** No añadas secciones que no existen en el en-EN (p. ej., bloques `* RESUMEN *` con tipo/ubicación/peligro de misión). La única fuente autorizada de estructura es el en-EN.

**Placeholder `[...]`:** Si una clave existente contiene `[...]` como contenido, no está completa — es un error de traducción pendiente, no contenido intencionado. Traducir íntegramente desde el en-EN.

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
| online (texto descriptivo, no etiqueta UI) | en línea (NO: "online" — anglicismo en texto corrido)                                                                                                                                                                                                |
| offline (texto descriptivo, no etiqueta UI) | sin conexión (NO: "offline" — anglicismo; distinto de la etiqueta UI "Desconectado")                                                                                                                                                                 |
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
| Data Runner | Data Runner (NO traducir — mantener en inglés como nombre propio del rol)                                                                                                                                                                                  |
| Escaped Ships (contador UI) | Naves huidas                                                                                                                                                                                                                                         |
| capable (personas/militares) | competente/competentes (NO: "capaz/capaces" en contextos de personas o agentes). Mantener "capaces" para objetos ("canones capaces de...") y expresiones idiomaticas ("ver de lo que son capaces")                                                   |
| redeem (ticket/bono) | canjear (NO: "convertir")                                                                                                                                                                                                                            |
| Energizing (efecto comida) | Energizante                                                                                                                                                                                                                                          |
| Hyper-Metabolic (efecto comida) | Hipermetabólico                                                                                                                                                                                                                                      |
| None (efectos comida/bebida) | Ninguno                                                                                                                                                                                                                                              |


#### Partes de nave e instalaciones

| en-EN | es-ES |
|-------|-------|
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


#### Sistemas y componentes de nave

| en-EN | es-ES |
|-------|-------|
| power plant | planta de energía |
| cooler | sistema de refrigeración |
| shield generator | generador de escudo |
| weapon hardpoint / weapon mount | punto de anclaje de arma |
| landing gear | tren de aterrizaje |
| thruster | propulsor |
| main thruster | propulsor principal |
| maneuvering thruster | propulsor de maniobra |
| fuel intake | toma de combustible |
| fuel tank | depósito de combustible |
| gimbal | gimbal (mantener en inglés — término técnico del juego) |
| flight blade | Blade de Vuelo (NO: "Cuchilla de Vuelo" — "blade" es nombre propio del componente) |
| fixed mount | montura fija |
| nombres de modelo de componente (quantum drives, jump drives, coolers, etc.) | mantener en inglés — son nombres de producto propios. Ej: "Explorer", "Exodus", "Odyssey", "IcePlunge". NO traducir aunque parezcan palabras comunes (NO: "Explorador", "Exodo") |
| scanning array | sistema de escaneo |
| gravity generator | generador de gravedad |
| repair bay | bahía de reparación |


#### Roles y tipos de nave

| en-EN | es-ES |
|-------|-------|
| gunship | Cañonera (NO: "nave de guerra" — demasiado genérico). Concordancia femenina: "Cañonera pesada"                                                                                                                                                       |
| heavy gunship | Cañonera pesada                                                                                                                                                                                                                                      |
| carrier-based [tipo] | [tipo] de portanaves. Ej: "Carrier-Based Bomber" → "Bombardero de portanaves" (NO: "basado en portador")                                                                                                                                             |
| Scout (rol de nave) | Reconocimiento (NO: dejar en inglés)                                                                                                                                                                                                                 |
| Touring (rol de nave) | dejar en inglés "Touring" (NO traducir — es un término específico del juego que designa un rol de nave, igual que "Snub" o "Scout") |
| Repair (rol de nave) | Reparacion (sustantivo, NO: "Reparar" — infinitivo)                                                                                                                                                                                                  |
| Short Range Patrol | Patrulla de corto alcance (NO: añadir "Caza" si no está en el original)                                                                                                                                                                              |
| UltraLight Ground | Terrestre ultraligero (Ground = terrestre, NO: "Suelo")                                                                                                                                                                                              |
| Snub Fighter | Caza SNUB (mantener SNUB — término específico del juego)                                                                                                                                                                                             |


#### Navegación y ubicaciones

| en-EN | es-ES |
|-------|-------|
| bearing / heading | rumbo / dirección |
| vector | vector (mantener en inglés en UI técnica) |
| sector | sector |
| jump point to X | punto de salto a X |
| route | ruta |
| waypoint | punto de ruta / waypoint (en UI técnica) |
| coordinates | coordenadas |
| distance / range | distancia / alcance |
| in orbit around X | en órbita alrededor de X (NO: "orbitando X" en texto formal) |
| on [location] (ubicación, claves `mission_location_*`) | en [ubicación] — usar siempre "en", no "al". Ej: "Last Ditch on Monox" → "Last Ditch en Monox" |
| [nombre], [Sistema] (formato de ubicación) | [nombre], Sistema [nombre] — Ej: "Keene, Killian System" → "Keene, Sistema Killian" |


#### Slang criminal de NPCs de misión (Ruto, Parr, etc.)

Jerga usada por personajes del submundo criminal. Traducir siempre el sentido, nunca la literalidad.

| en-EN | es-ES | Notas |
|-------|-------|-------|
| `hitter` (operador de alto nivel) | `operador` (NO: "bateador" — calco de béisbol sin sentido en español) | |
| `my jam` / `that's my jam` (lo que me gusta/domino) | `lo mío` (NO: "mi mermelada") | "This is my jam" → "Esto es lo mío" |
| `tight` (genial, en forma, bien) | `brutal` / `en forma` (segun contexto) | "You're looking tight" → "Estás en forma" |
| `flush` (bien de dinero/trabajo, abundante) | `bien de trabajos` / `bien provisto` (NO: "al ras") | "Been flush recently" → "Ha habido trabajo de sobra" |
| `score` (premio, botín, golpe exitoso) | `premio` / `golpe` (NO: "puntaje") | "¡Score!" → "¡Premio!" |
| `swing by` (pasarse por un sitio) | `pásate por` (NO: "Swing por" — calco literal) | "Swing by Grim HEX" → "Pásate por Grim HEX" |
| `hit me up` (contáctame) | `contáctame` (NO: "golpéame") | |
| `call it a night` (dejarlo por hoy) | `dejarlo por hoy` / `dar la noche por terminada` | |
| `high and dry` (en apuros, colgado) | `en apuros` / `colgado` (NO: "altos y secos") | |
| `end of my rope` (al límite de mi paciencia) | `al límite` / `sin aguante` (NO: "al final de mi cuerda") | |
| `signing off` (despedida en comms) | `cerrando comunicacion` / `me despido` (NO: dejar sin traducir "signing off") | |
| `those are the breaks` (así son las cosas, qué le vas a hacer) | `así son las cosas` (NO: "esos son los descansos") | |
| `no sweat` (sin problema, no hay de qué) | `sin problema` (NO: "sin sudor") | |
| `lit` (drogado, colocado) | `hasta arriba` (NO: "iluminado") | "You're lit" → "Estás hasta arriba" |
| `wading deep` (metido a fondo en algo) | `metido a fondo` (NO: "vadeando profundo") | |
| `crashing [sb's] good time` (aguar la fiesta a alguien) | `aguando la fiesta a [alguien]` (NO: "estrellando el buen tiempo de") | |
| `hitters` (consumidores de droga, en argot) | `consumidores` / `usuarios` (NO: "bateadores") | Contexto: clientela de drogas |
| `mark` (objetivo señalado para eliminar) | `objetivo` (NO: "marca") | "Got a mark that needs popping" → "Tengo un objetivo que hay que liquidar" |
| `popping` (matar en argot criminal) | `liquidar` (NO: "perforar") | |
| `haul` (botín, robo, lo que se lleva) | `golpe` / `robo` / `botín` (NO: "recorrido") | "A decent haul" → "Un golpe bastante decente" |
| `boost [sth]` (robar, ejecutar un robo) | `ejecutar [el robo]` / `llevárselo` (NO: "impulsar las cosas") | |
| `relieve [sth] of [cargo]` (aligerar una nave de su carga robándola) | `aligerar [nave] de [contenido]` (NO: "liberar") | Concordar en femenino con "nave" |
| `bear with me` (sígueme, ten paciencia conmigo) | `sígueme en esto` (NO: "Ten paciencia conmigo en este") | |
| `Easy.` (calmar tensión tras un roce) | `Con calma.` (NO: "Fácil." / "Easy." sin traducir) | PhysicalBump |
| `Watch yourself.` (despedida de cuidado) | `Cuídate.` (NO: "Mírate.") | Farewell informal |
| `take care of this` (encárgate de esto, resuélvelo) | `encárgate de esto` (NO: "cuida esto" — "cuidar" implica proteger, no resolver) | "Take care of this quick, okay?" → "Encárgate de esto rapido, ¿vale?" |
| `you better come at [sb] with your A-game` (más te vale ir con todo) | `más te vale ir con todo` (NO: "acércate con tu mejor juego" — calco de béisbol) | "You better come at them with your A-game" → "Mas te vale ir con todo" |
| `sort out [sth]` (gestionar, encargarse de, mover) | `mover` / `encargarse de` / `gestionar` según contexto (NO: "clasificar") | "Help me sort out a batch" → "Ayudarme a mover un lote" |
| `mug` (argot: tipo, fulano, persona) | `tipo` / `fulano` (NO: "taza" — falso amigo literal) | "I've got another mug ready" → "Tengo a otro tipo listo" |
| `snag [sth]` (pillar, conseguir, hacerse con) | `pillar` / `conseguir` (NO: "engancharte" — confunde con hook/addict) | "Could you snag [item]?" → "¿Podrias pillarme [item]?" |

#### Vocabulario coloquial, criminal y apodos

| en-EN | es-ES |
|-------|-------|
| slippery (difícil de atrapar, evasivo) | escurridizo (NO: "resbaladizo" — eso es físico, como suelo mojado)                                                                                                                                                                                   |
| slick (apodo/trato coloquial, como "buddy") | listillo (NO: "resbaladizo"). Ej: "Hey, slick." → "Oye, listillo."                                                                                                                                                                                   |
| Slippery [Nombre] (apodo criminal) | [Nombre] el Escurridizo. Ej: "Slippery Mike" → "Mike el Escurridizo"                                                                                                                                                                                 |
| taken care of yesterday / needed yesterday (urgencia extrema) | resuelto para ayer / para ayer (expresión hecha española). Ej: "Need this taken care of yesterday" → "Necesito que esto este resuelto para ayer"                                                                                                     |
| wet work (jerga: asesinato encubierto) | Trabajo Sucio (NO: "trabajo mojado" — calco literal sin sentido)                                                                                                                                                                                     |
| I'll be damned (exclamación de sorpresa/asombro) | Segun contexto: "¡No me lo puedo creer!" (sorpresa positiva), "Anda." (sorpresa contenida), "¿Esto es lo que se siente?" (agonía). (NO: "sere condenado" / "voy a ser condenado" — calco literal sin sentido en español)                             |
| wiped out of existence | desaparezca del mapa (NO: "eliminada de la existencia" — calco literal)                                                                                                                                                                              |
| quantum engines / quantum drives | motores cuanticos (NO: "motores quantums" — mezcla español/inglés)                                                                                                                                                                                   |
| power usage / power consumption | Consumo de energia (NO: "Uso de Energia" — calco de "usage")                                                                                                                                                                                         |
| [faction]_RepUI_Focus sin traducir | traducir siempre. Ej: Advocacy → "Aplicacion de la Ley" (NO: "Enfoque de los Advocacy")                                                                                                                                                              |
| CommRelay (nombre de servicio) | comunicaciones (NO: dejar en inglés "CommRelay")                                                                                                                                                                                                     |
| no longer in active operation | ya no esta operativa (NO: "ya no esta en operacion activa" — calco)                                                                                                                                                                                  |
| Livery / livery (pintura de nave, clave con "Paint" o "Luminalia") | Pintura (NO: "Diseño" ni "decoracion" — ambos son incorrectos). Ej: "100 Series Frostbite Camo Livery" → "Pintura serie 100 Frostbite Camo"                                                                                                          |
| claves `item_Name*_Paint_*` (pinturas de nave) | formato: `Pintura [NaveEN] [NombrePinturaEN sin "Livery"]`. El nombre de la pintura es un nombre de producto y se mantiene en inglés. NO traducirlo. NO usar "Librea". Ej: `item_NameAsgard_Paint_Black_Grey_Red_Pirate_Skull` → `Pintura Asgard Skullcrusher` |
| Focal: (campo en descripciones de vehiculos, ej: "Fabricante: ...\nFocal: Caza Medio") | Enfoque: (NO: "Focal:" — calco del inglés "Focus")                                                                                                                                                                                                   |
| Gauntlet (serie de combate) | Guantelete. Ej: "Combat Gauntlet" → "Guantelete de Combate" — SALVO que el proyecto lo tenga establecido como "Desafio", en cuyo caso mantener                                                                                                       |
| Naval (adjetivo militar) | Naval (NO: "de la Armada" — más largo e incorrecto). Ej: "Naval Patrol Training" → "Entrenamiento de Patrulla Naval"                                                                                                                                 |
| Floor [N] (planta de edificio) | Planta [N] (NO: "Piso" — eso es apartamento en español de España)                                                                                                                                                                                    |
| Nombres propios de ubicaciones (Research Outpost, City Gates, etc.) | Mantener en inglés si es el nombre oficial del lugar. NO traducir. Ej: "Hickes Research Outpost" → "Hickes Research Outpost" (NO: "Puesto de investigacion de Hickes")                                                                               |
| was heading to / was en route to | se dirigia a (NO: "estaba en ruta hacia" — calco de "en route")                                                                                                                                                                                      |
| outlaw attack / outlaw activity | ataque de forajidos (NO: "fuera de la ley" — esa es una descripción legal, no un sustantivo)                                                                                                                                                         |
| IAE (Intergalactic Aerospace Expo) | femenino — "la IAE", "durante la IAE", "de la IAE", "celebrar la IAE" (NO: "el IAE", "del IAE")                                                                                                                                                      |


#### Combate espacial y órdenes militares

| en-EN | es-ES |
|-------|-------|
| Crash Close / Collision Imminent (alertas de proximidad de nave — claves `*_ProxAlert_*`) | Colisión [dirección] próxima (NO: dejar en inglés "Rear Crash Close", "Front Crash Close"). Direcciones: `Front` → `delantera`, `Rear` → `trasera`, `Port` → `a babor`, `Starboard` → `a estribor`, `Deck` → `inferior`, `Overhead` → `superior`. Ej: "Rear Crash Close" → "Colisión trasera próxima"; "Port Crash Close" → "Colisión a babor próxima" |

| en-EN | es-ES |
|-------|-------|
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
| wanted (título de misión o anuncio de trabajo: se busca a alguien para un encargo) | "Se busca [profesión/rol]" (NO: "[profesión] buscado/a" — suena a ficha policial, no a oferta de trabajo). Ej: "Private Investigator Wanted" → "Se busca investigador privado"; "Bounty Hunter Wanted" → "Se busca cazarrecompensas" |
| accents (diseño/acabado de armadura, nave o vehículo) | detalles (NO: "acentos" — en español "acento" es lingüístico, no de diseño). Ej: "red accents" → "detalles rojos"; "gold accents" → "detalles dorados" |
| rolling (maniobra de vuelo) | alabeo (término aeronáutico; NO: "laminacion" — eso es industria de metales) |
| strafing (movimiento lateral con propulsores de maniobra) | desplazamiento lateral (NO: "ametrallamiento" — eso es disparar con ametralladora) |
| draw / DRAW (resultado de partida: empate) | EMPATE (NO: "DIBUJAR" — calco literal de "draw") |
| kick player (botón de expulsión en lobby) | EXPULSAR JUGADOR (NO: "JUGADOR DE PATADA" — calco literal) |
| player handle (identificador de usuario en lobby) | Identificador de jugador (NO: "Mango de jugador" — "mango" es fruta o asa, no nombre de usuario) |
| friendly fire (UI de Arena Commander) | FUEGO AMIGO (NO: "FUEGO AMISTOSO" — el término militar estándar en español es "fuego amigo") |
| SPECTRUM (nombre propio del sistema de matchmaking de AC) | SPECTRUM — NO traducir (NO: "ESPECTRO"). En títulos de pantalla: "PARTIDA SPECTRUM", "SPECTRUM / PARTIDA PUBLICA" |
| Public Match / Private Match (UI de Arena Commander) | PARTIDA PUBLICA / PARTIDA PRIVADA (femenino — "partida" es femenino; NO: "PARTIDO PUBLICO" / "PARTIDO PRIVADO") |
| [X] Kill (puntuación de Arena Commander: Ace Kill, Revenge Kill, Martyr Kill, Nemesis Kill) | Baja de [X] — Ej: "Ace Kill" → "Baja de As"; "Revenge Kill" → "Baja de Venganza"; "Martyr Kill" → "Baja de Martir"; "Nemesis Kill" → "Baja de Nemesis" (NO: "X matar" — calco literal) |
| Respawns Replenished (UI de AC, contador de reapariciones) | REAPARICIONES REABASTECIDAS (NO: "RESPONSABILIDADES REEMPLAZADAS" — error de traducción; "respawn" = reaparición) |
| Apodos/callsigns de NPCs (PirateCaptain, etc.) | Mantener en inglés como nombres propios: Singer, Ringo, Fluster, Boom Boom, Headcase (NO traducir: "Cantante", "Ponerse nervioso", "auge auge") |
| Restricted Area [Left/Right/Above/Below/Ahead/Behind] | area restringida a la izquierda / a la derecha / arriba / abajo / mas adelante / detras (NO: "restante" por "left" — "left" aquí es dirección, no "restante") |


#### Misiones, objetivos y UI

| en-EN | es-ES |
|-------|-------|
| search (contexto de investigación/inspección de lugar) | registrar / investigar / examinar (NO: "buscar" — "search" en investigación policial/espacial implica inspeccionar el lugar, no solo buscar algo). Ej: "Search the hub" → "Registra el hub"; "Search for clues" → "Investiga la zona" |
| evidence (contexto policial/investigación) | pruebas / prueba encontrada (NO: "evidencia" — en español "evidencia" es de uso científico; en investigación policial se dice "pruebas"). Ej: "Evidence found" → "Prueba encontrada"; "submit evidence" → "presentar pruebas"; "destroy evidence" → "destruir pruebas" |
| Nombres propios de instalaciones/ubicaciones del juego (Covalex Shipping Hub, etc.) | Mantener en inglés — NO traducir nombres propios de instalaciones. Ej: "Go to Covalex Shipping Hub" → "Ve al Covalex Shipping Hub" (NO: "Centro de envio de Covalex") |
| Imperativos en objetivos de misión (verbos de acción) | Usar formas naturales del español: registrar, investigar, examinar, localizar, entrar (NO: "Busque", "Ubique", "Ingrese" — suenan a calco formal del inglés) |
| light workload / light load (carga de trabajo) | carga de trabajo baja (NO: "ligera" — en contexto de carga de trabajo se usa "baja/alta", no "ligera/pesada") |
| refinement (en contexto de refinería industrial) | refinado / trabajos de refinado (NO: "refinamiento" — en español "refinamiento" se usa para modales/pulido, no para procesos industriales). Ej: "for your refinement needs" → "para sus trabajos de refinado" |
| outsourcing / outsource (cabeceras de contratos corporativos) | subcontratación / subcontratar (NO: "outsourcing" — anglicismo; en cabeceras de misión usar "SUBCONTRATACIÓN DE [EMPRESA]"; el campo "Outsource Manager" → "Responsable de Subcontratacion"). Ej: "HURSTON DYNAMICS OUTSOURCING" → "SUBCONTRATACIÓN DE HURSTON DYNAMICS" |
| rat (argot criminal: soplón, traidor, persona que no paga) | rata (NO: "chincheta" — "rat" en argot no es el roedor ni el objeto de papelería; es un insulto a alguien desleal o que no cumple). Ej: "Take care of a rat I've been dealing with" → "ocuparme de una rata con la que llevo tratando" |
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
| a real rush (emoción, subidón) | un subidón de verdad (NO: "una verdadera prisa" — "prisa" = hurry, no rush/thrill)                                                                                                                                                                   |
| ass whoopin / ass kicking (paliza, zurra) | una buena paliza / una tunda de verdad (NO: "grito de culo" — no tiene sentido en español)                                                                                                                                                           |
| a big F you / middle finger (gesto de desprecio) | un corte de mangas (expresión española equivalente al "F you" anglosajón)                                                                                                                                                                            |
| sit back, take in the space and let your ship call to you | tomarselo con calma, sentir el espacio y esperar a que una nave te hable (NO: "absorber el ambiente y dejar que la nave te llame" — forzado) |
| I'll leave you to it (despedida informal) | Te dejo tranquilo (NO: "Te dejo con eso" — calco de "leave you to it") |
| Take care. (despedida informal) | Cuidate. (NO: "Cuida." — incompleto; en español la forma natural es el reflexivo "cuídate") |
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
| `Have a good one.` (despedida coloquial) | `Que te vaya bien.` (NO: "Tener una buena." — infinitivo sin sujeto, incorrecto en español) |
| `Should be all set.` (despedida / confirmación) | `Todo listo.` (NO: "Debe estar todo listo." — "debe" añade incertidumbre que no existe en el original) |
| `You need help with something?` (oferta de ayuda, NPC) | `¿Necesitas ayuda con algo?` (NO: "¿Necesito ayuda con algo?" — error de persona: "necesito" = yo, "necesitas" = tú) |
| `Pay attention.` (imperativo, NPC al chocarse) | `Presta atencion.` (NO: "Prestar atencion." — infinitivo en lugar de imperativo) |
| `The vehicle terminal is right that way. You're welcome to use it.` | `La terminal de Vehiculos esta justo por alli. Puedes usarla.` (NO: "es correcta de esa manera" — calco que no tiene sentido en español) |
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
| I'm a friendly / Friendly, friendly! (diálogo de fuego amigo) | ¡Soy un amigo! / ¡Amigo, amigo! (NO: "Soy amigable", "Soy amistoso", "Amable, amable" — "friendly" en contexto táctico = aliado, no personalidad simpática) |
| my bad (disculpa coloquial por error propio) | ha sido culpa mía / me he equivocado (NO: "mi malo" — latinamericanismo; en castellano no existe esa construcción) |
| Watch it! (advertencia/protesta por golpe o peligro) | ¡Cuidado! / ¡Ojo! (NO: "¡Míralo!" — calco literal de "watch it"; la expresión española equivalente es de alerta, no de mirar algo) |
| Hold your fire! (orden táctica de no disparar) | ¡Alto el fuego! (NO: "¡Espera el fuego!" — calco literal; "alto el fuego" es la expresión militar estándar en español) |
| The authorities are going to hear about this (amenaza de denuncia) | Las autoridades se van a enterar de esto (NO: "van a escuchar de esto" — calco de "hear about"; en español "enterarse de algo" = to hear about something) |
| Shot got away from me (tiro que se fue sin querer) | Se me fue el tiro (NO: "El tiro se escapó de mí" — calco literal; "irse el tiro" es la expresión natural en español) |
| Hey + insulto (interpelación enfadada) | ¡Oye, [insulto]! (NO: "Hola, [insulto]" — "Hey" como exclamación de enfado = "¡Oye!" / "¡Eh!", nunca saludo) |
| hack down CrimeStat / clear CrimeStat (reducir/borrar el registro criminal hackeando una terminal) | borrar su CrimeStat (NO: "hackee su CrimeStat" — "hackear" es el acto, pero la acción concreta es borrar/reducir el registro; más claro y natural) |
| opportunity (en títulos de contrato/misión) | oportunidad (NO cambiar a "puesto" — respetar siempre el término original si el en-EN dice "opportunity") |
| take out (destruir/derribar una nave o unidad en combate) | derribar (NO: "sacar", "eliminar a" — "take out" en contexto de combate espacial = destruir físicamente; "derribar" es el equivalente militar natural en español) |
| nombres de lugares como destino de acción (protect X, defend X) | sin preposición "a" antes del lugar — los topónimos no llevan "a personal". Ej: "protect Kareah" → "proteger Kareah" (NO: "proteger a Kareah" — la "a personal" es para personas, no lugares) |
| Comm Array / comm array | mantener en inglés — es un nombre propio. Capitalización según el original: "Comm Array" en UI formal, "comm array" en diálogos/terminales. Artículo "el/un". Ej: "Disable uplink at Comm Array 625" → "Desactiva la conexion en el Comm Array 625"; "Hack a comm array" → "Piratea un comm array" (NO: "matriz de comunicaciones") |
| Imperativo en objetivos de misión | usar siempre 2ª persona del singular informal (tú): "Viaja", "Localiza", "Protege", "Contacta", "Elimina" (NO: "Viaje", "Localice", "Proteger", "Informe" — son formas de usted/infinitivo, incorrectas en objetivos dirigidos al jugador) |
| Report to [NPC/lugar] (objetivo de misión) | Contacta con [NPC/lugar] (NO: "Informe a" — "informar" en imperativo de usted suena arcaico y formal) |
| Travel to [ubicación] (objetivo de misión) | Viaja a [ubicacion] (NO: "Viaje a" — usted formal; NO: "al [código]" — usar "en [código]" para coordenadas/identificadores) |
| [verbo en infinitivo] como objetivo de misión | convertir a imperativo informal. Ej: "Proteger al civil" → "Protege al civil"; "Localizar restos" → mantener infinitivo solo en _Short, imperativo en _Long |
| pirate threat attacking X (amenaza pirata atacando) | los piratas que atacan X (NO: "la amenaza pirata atacando" — gerundio adjetival incorrecto en español; usar oración de relativo) |
| uplink (en contexto de Comm Array/misiones) | conexion (NO: "enlace ascendente" — calco técnico que suena raro en español) |


#### Minería, recursos y naves especializadas

| en-EN | es-ES |
|-------|-------|
| undersuit (prenda interior del traje espacial) | mono (NO: "pijama espacial" — suena informal y confuso; NO: "traje interior" — demasiado genérico). Plural: monos. Ej: "Clothing & Undersuits" → "Ropa y monos" |
| legs (pieza de armadura para las piernas, claves `*_legs_*`) | piernas (NO: "pantalones" — pantalones es ropa civil, las piezas de armadura son piernas). Ej: "Carrion Legs" → "Piernas Carrion". Los keys `*_pants_*` sí se traducen como "pantalones" porque son ropa. |
| debris / wreckage (restos de nave destruida) | restos (NO: "escombros" — eso es rubble de edificios). "Debris field" → campo de restos. "Heavy Debris" (característica de carrera) → Gran Densidad de Restos |
| Delivery Drop Off (marcador de misión) | Punto de entrega (NO: "Entrega de entrega" — duplicado sin sentido) |
| Pick-up location / collection point (marcador de misión) | Punto de recogida (NO: "Sitio de recogida" — usar siempre "punto" para unificar con "Punto de entrega") |
| recovery (sustantivo: acción de recuperar algo) | la recuperación — femenino (NO: "el recuperacion" — recuperación es femenino; ej: "la recuperacion segura", "la recuperacion del sitio") |
| state of the art (tecnología punta) | de última generación (NO: "de arte estatal" — calco literal; NO: "de vanguardia" — demasiado genérico en contexto de item) |
| Nombres de módulos mineros consumibles (Stampede, Lifeline, Rime, Surge, Torpid, Optimum, Brandt, Forel, Waveshift, Okunis, Sabir, BoreMax, Stalwart, Optimax) | Mantener en inglés como nombres propios — NO traducir. Ej: "Stampede usa una lente de última generación" (NO: "La estampida usa...") |
| cluster factor / cluster modifier (minería: factor de agrupamiento de fragmentos) | Modificador de fragmentación (nombre del módulo/stat); en descripciones: "mantiene los fragmentos de mineral valioso más agrupados al fracturarse" (NO: "Modificador de cluster", NO: "Modificador de racimo") |
| mining ship / nave minera | nave minera — femenino (NO: "nave minero" — concordar con el género de "nave"). Ej: "cualquier nave minera compatible" |
| Krypton (commodity, gas noble) | Krypton — mantener en inglés. Es el nombre del gas en el universo de SC (NO: "Criptón") |
| Fair Chance Act (ley de la UEE) | Ley de Oportunidades Justas (NO: "Ley de Oportunidad Justa", NO: "Fair Chance Act" sin traducir) |
| Blueprint / Blueprints (esquemas de fabricación) | Blueprint / Blueprints — mantener en inglés (NO: "Plano/s"). Ej: "Possible Blueprints" → "Posibles Blueprints" |
| Dispatcher (título de cargo NPC) | Coordinador / Coordinadora (NO: "Despachador/a"). Ej: "Lead Dispatcher" → "Coordinadora principal" |
| _raw (sufijo de commodity mineral en bruto) | (Bruto) — ej: `Copper Raw` → `Cobre (Bruto)`; `Gold Raw` → `Oro (Bruto)` (NO: "(Crudo)", "(En Bruto)", "(Mineral Bruto)") |
| Nombres de minerales ficticios de SC (Taranite, Bexalite, Laranite, Hephaestanite, Borase, Agricium, Stileron, Saldynium, Jaclium, Lindinium, Dolivine, Feynite, Aphorite, Hadanite, Janalite, Quantanium, Riccite) | Mantener en inglés — NO traducir. Son nombres propios del universo SC sin equivalente real. Ej: `Taranita` → `Taranite`; `Bexalita` → `Bexalite` |
| Nombres de minerales reales (Copper, Gold, Iron, Titanium, Silicon, Tungsten, Aluminium, Beryl, Diamond, Quartz, Thorium, Uranium, Lithium, Hydrogen, etc.) | Traducir al español: Cobre, Oro, Hierro, Titanio, Silicio, Wolframio, Aluminio, Berilo, Diamante, Cuarzo, Torio, Uranio, Litio, Hidrógeno. Verificar que el mineral existe en la tabla periódica antes de traducir. |
| Corundum | Corundum — mantener en inglés (NO: "Corindón") |
| amortiguador (componente físico de armadura, shock-absorbing) | amortiguador — correcto para componentes físicos de absorción de impacto en armaduras. NO confundir con quantum dampener (→ inhibidor) |

---

### Misiones GoblinG — OPERACIÓN DE RECURSOS

- Prefijo de título: **OPERACIÓN DE RECURSOS:** (NO: "Impulso de Recursos", "Iniciativa de Recursos" — se unificó todo)
- Cabeceras de los mensajes de Hurston: **SUBCONTRATACIÓN DE HURSTON DYNAMICS** (NO: "OUTSOURCING DE HURSTON DYNAMICS")
- Campo de cabecera: **RESPONSABLE DE SUBCONTRATACION:** (NO: "GESTOR DE OUTSOURCING", "Outsource Manager")
- Referencia interna al tracker del juego: **Operacion de Recursos Second Life** (nombre propio del journal in-game)

Campos de cabecera estándar en descripciones de misión (traducción fija):

| Inglés | Español |
|--------|---------|
| `CONTRACT:` | `CONTRATO:` |
| `CONTRACTOR AFFILIATION:` | `AFILIACION DEL CONTRATISTA:` |
| `RISK ASSESSMENT:` | `EVALUACION DE RIESGOS:` |
| `RUSH CONTRACT:` | `CONTRATO URGENTE:` |

Oficiales de enlace que firman los mensajes:

| Facción | Nombre | Cargo (es-ES) |
|---------|--------|---------------|
| MicroTech | Aster Remmington | Oficial de Enlace de Contratistas |
| Hurston Dynamics | A. Carmichael | Responsable de Subcontratacion |
| ArcCorp | Ella Tieno | Oficial de Enlace de Contratistas |
| Crusader Industries | Denver Samuels | Oficial de Enlace con Contratistas |

**Nota:** "El" en los mensajes de ArcCorp es el apodo de **Ella Tieno** — NO es el artículo español. Mantener como "El" (sin tilde, es un nombre propio abreviado).
---

### InterSec Defense Solutions

Empresa privada de seguridad y defensa con sede en el sistema Nyx. Contrata pilotos independientes para misiones de combate contra forajidos y Vanduul.

- **Nombre oficial:** `InterSec Defense Solutions` — nunca traducir (NO: "Soluciones de Defensa InterSec")
- **Firmante:** Deacon Tobin, `Gerente de Operaciones` (NO: "Gestor de Operaciones")
- **Tono:** formal/corporativo-militar, tercera persona en el cuerpo, tuteo al contratista
- **Prefijos de cabecera fijos:**

| Inglés | Español |
|--------|---------|
| `MISSION SPECS` | `ESPECIFICACIONES DE LA MISION` |
| `Area of Operation:` | `Area de Operaciones:` |
| `Hostile Forces:` | `Fuerzas Hostiles:` |
| `Equipment Specs:` | `Especificaciones del Equipo:` |
| `Briefing:` | `Informe:` |
| `Capital Ship` | `Nave Capital` |
| `Heavy Gun-Ship` | `Nave de Artilleria Pesada` |
| `Combat-rated Ship(s)` | `Nave(s) con capacidad de combate` |

- **Pie de mensaje fijo:** `Esta comunicacion consiste en informacion confidencial destinada unicamente al destinatario. Por favor, ignorala si la recibes por error y notifica al remitente. Todas las operaciones se realizan bajo el riesgo personal del contratista y deben cumplir con la ley de la UEE y del sistema donde sea aplicable.`
- **Pie alternativo (oferta no vinculante):** `Esta comunicacion consiste en una oferta no vinculante que, una vez aceptada, puede ser terminada inmediatamente por cualquiera de las partes sin previo aviso. Todas las operaciones se realizan bajo el riesgo personal del contratista y deben cumplir con la ley del sistema donde sea aplicable.`
- **"engage with hostiles"** → `enfrentate a los hostiles` (NO: "involucrate con los hostiles")
- **"strong group of ships"** → `una flota potente` (NO: "un grupo fuerte de naves")
- **"highly skilled"** → `muy cualificado` (NO: "altamente cualificado")
- **"It is critical that"** → `Es fundamental que` (NO: "Es critico que")

---

### Patrones de lenguaje por tipo de misión

#### Escolta y protección
- Objetivo: **"Protege a [objetivo]"** / **"Escolta a [objetivo]"** (NO: "Defender a", "Guardar a")
- Ataque al objetivo: `VIP under attack` → `¡El VIP está siendo atacado!`
- Éxito: `VIP extracted safely` → `VIP evacuado con éxito`
- Fallo: `VIP lost` → `VIP perdido` / `Misión fallida: VIP eliminado`

#### Entrega y transporte
- Recogida: **"Recoge [paquete]"** en [origen]
- Entrega: **"Entrega [paquete]"** en [destino]
- Marcadores: `Pick-up location` → `Punto de recogida`; `Delivery Drop Off` → `Punto de entrega`
- Urgencia: `time-sensitive delivery` → `entrega urgente` (NO: "entrega sensible al tiempo" — calco)
- Pérdida: `Package lost` → `Paquete perdido`

#### Investigación y reconocimiento
- Inspección: **"Registra [zona]"** / **"Investiga [ubicación]"** (NO: "Busca en" para inspecciones)
- Escaneo: `Scan [objetivo]` → `Escanea [objetivo]`
- Hallazgo: `Evidence found` → `Prueba encontrada`
- Datos: `Retrieve data` → `Recupera los datos` / `Obtén los datos`

#### Combate y eliminación
- Objetivo: **"Elimina [objetivo]"** / **"Neutraliza [amenaza]"** — reservar "destruye" para objetos inanimados (naves, instalaciones), no personas
- Confirmación: `Hostile eliminated` → `Hostil eliminado`
- Oleada: `Wave X of Y` → `Oleada X de Y`
- Limpieza de zona: `Clear the area` → `Despeja la zona`

#### Sabotaje e infiltración
- Verbos: **"Sabotea [objetivo]"** / **"Hackea [terminal]"** / **"Desactiva [sistema]"**
- `Disable uplink` → `Desactiva la conexión`
- `Plant device` → `Coloca el dispositivo`
- `Avoid detection` → `Evita ser detectado`
- `Remain undetected` → `Permanece sin ser detectado`

---

### Misiones de personas desaparecidas (`searchbody_*`, `MissingPersons_*`)

Misiones en las que el contratista investiga restos de naves para localizar o confirmar el estado de una persona desaparecida. Tono: discreto, empático, formal escrito.

**Terminología fija:**

| Inglés | Español |
|--------|---------|
| `missing person` | `persona desaparecida` (NO: "cliente desaparecido") |
| `wreck site` / `derelict site` | `sitio del accidente` / `lugar del naufragio` |
| `the wreckage` / `the derelict` | `los restos` |
| `the ship's remains` | `los restos de la ~mission(Ship)` |
| `Confirm Status` | `Confirmar el estado` |
| `Investigation Point` | `Punto de Investigacion` |
| `closure` | `consuelo` / `paz` (NO: "cierre" — suena técnico) |
| `foul play` | `juego sucio` |
| `conduct an onsite search` | `realizar una busqueda en el sitio` |
| `ascertain` | `determinar` |
| `perish` | `fallecer` / `morir` (NO: "perecer" — registro demasiado literario) |

**Patrones de objetivos de tripulación (`MissingPersons_Crew_*`):**
- Usar siempre **"Localizar X"** como verbo inicial (NO: "X de localización", "Encontrar X")
- `Locate Co-pilot` → `Localizar copiloto`
- `Locate Scan Tech` → `Localizar tecnologia de escaneo`

**Frases de aviso/peligro (`searchbody_danger_*`):**
- Siempre tuteo: "te recordaramos", "ten cuidado"
- `take your time` → `actuar con calma` (NO: "tomarte tu tiempo")
- `don't get sloppy` → `no seas descuidado`

**Frases de urgencia (`searchbody_timed_*`):**
- `close this matter` → `cerrar este asunto`
- `expedite matters` → `acelerar el proceso`
- `ASAP` → `lo antes posible`

**Al final de `searchbody_desc_0001`:** incluir siempre la frase de cierre: `Tu ayuda en este asunto es muy apreciada.`

---

### Patrones problemáticos documentados

Errores recurrentes detectados en el proyecto — no repetir:

| Patrón incorrecto | Corrección | Motivo |
|---|---|---|
| `finalización exitosa del escenario` | `completar el escenario con exito` | Calco literal de "successful completion" |
| `Despacho, tenemos contacto` | `Central, tenemos un contacto` | `Dispatch` como vocativo de radio → `Central` |
| `Orden de muerte:` | `Orden de Eliminacion:` | "muerte" es demasiado crudo; el EN usa "assassination" |
| `Estacion Fragmentadora QV` | `QV Breaker Station` | `Breaker Station` es nombre propio, no se traduce |
| `Breaker Station QV` / `Breaker Stations de QV` / `Estaciones Breaker` | `QV Breaker Station` / `QV Breaker Stations` | El orden correcto es siempre QV primero |
| `los Salamandras de Garra` | `los Claw Salamanders` | Nombre propio de banda criminal, no se traduce |
| `Presa Confirmada` | `Recompensa Verificada` | "presa" = prey, no bounty |
| `oportuno fin` | `fin prematuro` | "untimely" = prematuro/inoportuno, nunca "oportuno" |
| `CONTRATOS Y DESPACHO` | `CONTRATOS Y OPERACIONES` | "Despacho" no es equivalente de "Dispatch" en contexto de operaciones |
| `GREMIO DE CAZADORES DE RECOMPENSAS` | `BOUNTY HUNTERS GUILD` | Nombre propio de faccion, nunca se traduce |
| `Juvenil` (fauna) | `Joven` | "Juvenil" es registro medico/cientifico, no de juego |
| `Autorizado por: ~mission(Contractor|Auth)` | _(eliminar)_ | Placeholder inventado, no existe en en-EN |
| `YOUR GOODS IN GOOD HANDS` (Red Wind) | `Tu mercancia en buenas manos` | Slogan unificado del proyecto |
| `hemos explorado [naves/zona]` | `hemos avistado` | "scout" = avistar/reconocer, no explorar |
| `para manejar [tarea]` | `para encargarse de [tarea]` | Calco de "to handle" — "manejar" suena a objeto fisico |
| `llevara algunos pasos` | `no sera sencillo` / `requerira varios intentos` | Calco de "take some steps" |
| `te llevara algunos pasos ponerla operativa` | `no sera sencillo ponerla operativa` | Calco de "it'll take some steps to get it operational" |
| `ten cuidado porque ya que` | `ten en cuenta que` | Conectores redundantes, usar uno solo |
| `Leyes de la Autoridad Xenotrade` | `Actas de la Autoridad de Xenocomercio` | Forma unificada en BHG_Certification_Criminal_Desc |

---

### Mensajes de estado de UI

Patrones para etiquetas de estado en HUD, esclusas, sistemas y terminales:

| en-EN | es-ES | Notas |
|-------|-------|-------|
| `PRESSURIZED` | `PRESURIZADO` | Participio, mayúsculas si el original lo está |
| `DEPRESSURIZED` | `DESPRESURIZADO` | |
| `CYCLING COMPLETE` | `CICLADO COMPLETADO` | |
| `CYCLE AIRLOCK` | `CICLAR ESCLUSA` | Infinitivo en órdenes de UI |
| `CLOSE` (esclusa) | `CERRADO` | |
| `OPEN` (esclusa) | `ABIERTO` | |
| `OFFLINE` | `DESCONECTADO` | Etiqueta UI (distinto de texto corrido) |
| `ONLINE` | `CONECTADO` | Etiqueta UI |
| `POWER FAILURE` | `FALLO DE ENERGÍA` | |
| `SYSTEM FAILURE` | `FALLO DE SISTEMA` | |
| `SHIELDS DOWN` | `SIN ESCUDO` | |
| `FUEL LOW` | `COMBUSTIBLE BAJO` | |
| `LOCKED` | `BLOQUEADO` | |
| `ARMED` | `ARMADO` | |
| `STANDBY` | `EN ESPERA` | |
| `ACTIVE` | `ACTIVO` | |
| `INACTIVE` | `INACTIVO` | |

**Regla general:** En etiquetas de estado, usar **participio** para estados pasivos (`PRESURIZADO`, `BLOQUEADO`) e **infinitivo** para acciones (`CICLAR`, `ABRIR`). Mayúsculas si el original las usa.

---

### Expresiones temporales

Patrones para traducir tiempo y duración de forma natural:

| en-EN | es-ES | Notas |
|-------|-------|-------|
| `X days ago` | `hace X días` | NO: "X días atrás" — calco del inglés |
| `for X days` | `durante X días` | Duración |
| `while / whilst` | `mientras` | Simultaneidad |
| `during` | `durante` | Duración con sustantivo |
| `as of now` | `a partir de ahora` / `desde ahora` | NO: "a partir de ahora mismo" — redundante |
| `from now on` | `a partir de ahora` / `en adelante` | |
| `until further notice` | `hasta nuevo aviso` | NO: "hasta notificación adicional" — calco |
| `at all times` | `en todo momento` | NO: "en todos los tiempos" — calco |
| `by the time you read this` | `cuando leas esto` | NO: "para cuando leas esto" — calco |
| `sooner or later` | `tarde o temprano` | NO: "antes o después" — calco |
| `in no time` | `en un momento` / `enseguida` | NO: "en ningún momento" — falso amigo |
| `once` (una vez que) | `una vez que` / `cuando` | NO: "una vez" sin nexo subordinante |
| `ever since` | `desde entonces` / `desde que` | NO: "nunca desde" — calco |

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
| `elevator shaft` | `Hueco del ascensor` |
| `maintenance shaft` | `Conducto de mantenimiento` (NO: "Eje de mantenimiento" — suena a pieza mecánica giratoria) |
| `command module docking` | `Conector del módulo de mando` |
| `operations deck` | `Cubierta de operaciones` |
| `owner's room` | `Camarote del propietario` |

---

## Apéndice: Lista de naves

Todas las naves son **femeninas** y **no se traducen** (`la X`, `de la X`, `una X`).

85X, 100i, 125a, 135c, 300i, 315p, 325a, 350r, 400i, 600i, 890 Jump,
A1 Spirit, A2 Hercules, Apollo, Ares Inferno, Ares Ion, Arrow,
Aurora CL, Aurora ES, Aurora LN, Aurora LX, Aurora MR,
Avenger Stalker, Avenger Titan, Avenger Warlock,
Ballista, Banu Defender, Banu Merchantman, Blade, Buccaneer,
C1 Spirit, C2 Hercules, Carrack, Caterpillar, Corsair,
Constellation Andromeda, Constellation Aquila, Constellation Phoenix, Constellation Taurus,
Cutlass Black, Cutlass Blue, Cutlass Red, Cutlass Steel,
Dragonfly, E1 Spirit, Eclipse, Endeavor,
F7 Hornet, F8 Lightning,
Freelancer, Freelancer DUR, Freelancer MAX, Freelancer MIS,
Genesis Starliner, Gladiator, Gladius, Glaive, Hammerhead, Hawk, Herald,
Hull A, Hull B, Hull C, Hull D, Hull E, Hurricane,
Idris, Javelin, Khartu-Al, Kraken, Liberator,
M2 Hercules, M50, Mantis, Mercury Star Runner, MOLE, MPUV Cargo, MPUV Personnel, Mule,
Mustang Alpha, Mustang Beta, Mustang Delta, Mustang Gamma, Mustang Omega,
Nautilus, Nomad, Nox, Odyssey, Orion,
P-52 Merlin, P-72 Archimedes, Perseus, Pioneer, Polaris, Prospector, Prowler,
RAID, RAFT, Reclaimer, Redeemer,
Reliant Kore, Reliant Mako, Reliant Sen, Reliant Tana, Retaliator,
Sabre, San'tok.yai, Scorpius, Scythe, SRV, Starfarer, Starfarer Gemini,
Talon, Talon Shrike, Terrapin,
Valkyrie, Vanguard Harbinger, Vanguard Hoplite, Vanguard Sentinel, Vanguard Warden,
Vulture, Vulcan, X1
