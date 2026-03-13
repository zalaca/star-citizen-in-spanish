# Star Citizen en Español

Traducción al español de España para **Star Citizen**.

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

```
C:\Program Files\Robert Space Industries\Star Citizen\LIVE
```

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

## Notas

- Compatible con la versión **LIVE** de Star Citizen.
- La traducción es un trabajo en progreso — se actualiza regularmente.
- Algunos términos propios del universo se mantienen en inglés de forma intencionada (nombres de naves, facciones, lugares).

---

## Contribuir

Si encuentras errores o quieres sugerir mejoras, abre un [issue](../../issues) en este repositorio.
