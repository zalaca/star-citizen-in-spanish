# Star Citizen en Español

Traducción al español de España para **Star Citizen** — actualizada con los cambios de la versión **4.7.0**.

---

## Instalación

### Opción 1 — Descarga directa (recomendado)

1. Descarga el ZIP desde el último release:
   **[⬇ Descargar star-citizen-en-espanol.zip](https://github.com/zalaca/star-citizen-in-spanish/releases/latest/download/star-citizen-en-espanol.zip)**
2. Extrae el ZIP.
3. Copia el contenido extraído en el directorio de instalación de Star Citizen:

### Opción 2 — Git

```bash
git clone https://github.com/zalaca/star-citizen-in-spanish.git
```

Luego copia el contenido de la carpeta `copy/` en el directorio de instalación:

---

### Directorio de destino

El directorio de instalación depende de dónde tengas instalado el juego. **No tiene por qué estar en `C:`** — si lo instalaste en otro disco o carpeta, busca la carpeta `LIVE` dentro de tu instalación de Star Citizen.

La ruta por defecto es:

```
C:\Program Files\Roberts Space Industries\Star Citizen\LIVE
```

> Si no sabes dónde tienes el juego instalado, ábrelo desde el RSI Launcher, ve a **Settings** y busca la ruta de instalación.

> La traducción es compatible tanto con **LIVE** como con **PTU**. Si quieres usarla en PTU, repite el proceso copiando los archivos en la carpeta `PTU` en lugar de `LIVE`.

La estructura de archivos debe quedar así:

```
LIVE/
├── user.cfg
└── data/
    └── Localization/
        └── spanish_(spain)/
            └── global.ini
```

> El archivo `user.cfg` le indica al juego que use el idioma español. Si ya tienes un `user.cfg` propio, añade esta línea manualmente:
> ```
> g_language=spanish_(spain)
> ```

---

## Metodología

Un proyecto hecho por entretenimiento y para aportar a la comunidad hispanohablante de Star Citizen.

El proceso combina dos elementos:

- **SKILL.md** — una guía de estilo propia que recoge reglas de traducción, glosario de términos del universo, criterios de género gramatical (naves en femenino, planetas en masculino), y convenciones tipográficas específicas para Star Citizen.
- **Revisión manual** — cada entrada se contrasta con el texto original en inglés (`en-EN.ini`) para garantizar fidelidad al contexto y al tono.

El objetivo es una traducción natural al español de España, evitando calcos del inglés y adaptando expresiones idiomáticas sin perder la esencia del universo de Star Citizen.

---

## Notas

- Compatible con la versión **LIVE** de Star Citizen.
- La traducción es un trabajo en progreso — se actualiza regularmente.
- Algunos términos propios del universo se mantienen en inglés de forma intencionada (nombres de naves, facciones, lugares).

---

## Contribuir

Si encuentras errores o quieres sugerir mejoras, abre un [issue](../../issues) en este repositorio. Cualquier aportación es bienvenida y muy agradecida.
