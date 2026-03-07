# Monitor de Normativa Ferroviaria Europea

Agente automatizado en Oz que cada viernes a las 17:00 UTC revisa la normativa ferroviaria de la UE, detecta cambios y genera un informe.

## Qué hace el agente

Cada ejecución sigue este flujo:

1. **Scraping** — Recopila datos frescos de [ERA](https://www.era.europa.eu) (Agencia Ferroviaria de la UE): TSIs, reglamentos, directivas, CSMs, opiniones y recomendaciones.
2. **Comparación** — Contrasta los datos frescos con el estado anterior almacenado en `era_regulacion_estados_miembros.json`.
3. **Clasificación de cambios** — Identifica y categoriza:
   - **Documentos nuevos**: regulaciones, directivas o TSIs publicadas por primera vez.
   - **Documentos derogados**: normativa explícitamente derogada.
   - **Documentos sustituidos**: normativa reemplazada por versiones actualizadas.
   - **Cambios de estado**: transiciones como "En vigor" → "Modificado".
   - **Modificaciones**: cambios en campos de documentos existentes (descripción, enmiendas, plazos de implementación, etc.).
   - **Recursos TSI**: guías de aplicación, PDFs y documentos técnicos añadidos o retirados de las páginas de TSIs.
4. **Informe** — Genera un informe markdown en `informes/informe_cambios_YYYY-MM-DD.md` y un JSON estructurado con los cambios en `informes/cambios_YYYY-MM-DD.json`.
5. **Pull Request** — Si hay cambios significativos, crea un PR con el informe y el JSON base actualizado. Si no hay cambios, simplemente lo registra.

## Fuentes monitorizadas

- **ERA** (https://www.era.europa.eu) — Página de documentos, páginas individuales de cada TSI.
- **EUR-Lex** (https://eur-lex.europa.eu) — Referencias CELEX de directivas y reglamentos.

### Documentación cubierta

| Categoría | Ejemplos |
|---|---|
| Cuarto Paquete Ferroviario | Reglamento 2016/796 (ERA), Directiva 2016/797 (Interoperabilidad), Directiva 2016/798 (Seguridad) |
| TSIs (Paquete 2023) | CCS, INF, ENE, LOC&PAS, WAG, NOI, SRT, PRM, OPE, TAP |
| TSIs (2026) | TSI Telematics (unificada TAP+TAF) |
| Reglamentos de implementación | Autorización de vehículos (2018/545), ECM (2019/779), TSI OPE (2019/773) |
| Métodos Comunes de Seguridad | CSM REA (402/2013), CSM SMS (2018/762), CSM MON (1078/2012) |
| Legislación base | Directiva SERA 2012/34, Certificación de maquinistas 2007/59 |
| Derechos de viajeros | Reglamento 2021/782 |
| Mercancías peligrosas | Directiva 2008/68 (RID) |

## Estructura del proyecto

```
norm_eu_ffcc/
├── .agents/skills/monitor-normativa-ue/
│   └── SKILL.md                           # Skill de Oz (instrucciones del agente)
├── informes/                              # Informes generados (uno por ejecución)
│   ├── informe_cambios_2026-03-14.md
│   └── cambios_2026-03-14.json
├── scrape_era_regulations.py              # Scraper de documentos de ERA
├── detect_changes.py                      # Detector de cambios y generador de informes
├── era_regulacion_estados_miembros.json   # Estado actual (baseline)
├── investigar-normativa-ferroviaria-ue.md # Skill de investigación de normativa
├── analisis_cambios_eti_ccs_2023.md       # Análisis de la ETI CCS 2023
└── README.md                              # Este fichero
```

## Gestión del agente programado

El agente está registrado en Oz con el ID `boBS2q8afa94pDJaThcfhs`.

### Ver estado y próxima ejecución

```bash
oz schedule list
```

### Ver detalles y ejecuciones pasadas

```bash
oz schedule get boBS2q8afa94pDJaThcfhs
```

### Pausar el agente

```bash
oz schedule pause boBS2q8afa94pDJaThcfhs
```

### Reactivar el agente

```bash
oz schedule unpause boBS2q8afa94pDJaThcfhs
```

### Cambiar la frecuencia

```bash
# Ejemplo: cambiar a lunes y viernes a las 9:00
oz schedule update boBS2q8afa94pDJaThcfhs --cron "0 9 * * 1,5"
```

Referencia rápida de expresiones cron:

| Expresión | Frecuencia |
|---|---|
| `0 17 * * 5` | Viernes a las 17:00 (actual) |
| `0 9 * * 1` | Lunes a las 9:00 |
| `0 8 1 * *` | Primer día de cada mes a las 8:00 |
| `0 10 */14 * *` | Cada 14 días a las 10:00 |

### Cambiar el prompt

```bash
oz schedule update boBS2q8afa94pDJaThcfhs \
  --prompt "Nuevo prompt con instrucciones adicionales"
```

### Eliminar el agente

```bash
oz schedule delete boBS2q8afa94pDJaThcfhs
```

## Ejecución manual (local)

El script de detección de cambios se puede ejecutar localmente sin necesidad del agente de Oz.

### Requisitos

```bash
pip install requests beautifulsoup4 lxml
```

### Ejecutar detección de cambios

```bash
# Ejecutar scraper + comparar + generar informe (sin actualizar baseline)
python detect_changes.py

# Ejecutar y actualizar el JSON base con los datos nuevos
python detect_changes.py --update-baseline

# Comparar dos ficheros JSON directamente (sin scraping)
python detect_changes.py --previous estado_anterior.json --current estado_nuevo.json

# Guardar informes en otro directorio
python detect_changes.py --output-dir /ruta/a/informes
```

### Solo scraping (sin comparación)

```bash
python scrape_era_regulations.py
```

Genera `era_regulacion_estados_miembros.json` con todos los documentos recopilados.

## Environment de Oz

| Propiedad | Valor |
|---|---|
| **Nombre** | `investigacion_ferroviaria_eu` |
| **ID** | `LILdQj4URzPVrUoI2hAF5M` |
| **Imagen Docker** | `warpdotdev/dev-base:latest` |
| **Repositorio** | `frenopatico/oz_normativa_eu_ffcc` |
| **Setup command** | `pip install requests beautifulsoup4 lxml` |

### Actualizar el environment

```bash
# Añadir un nuevo setup command
oz environment update LILdQj4URzPVrUoI2hAF5M --setup-command "pip install nueva-dependencia"

# Cambiar la imagen Docker
oz environment update LILdQj4URzPVrUoI2hAF5M --image python:3.12
```
