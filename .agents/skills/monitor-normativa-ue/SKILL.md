---
name: monitor-normativa-ue
description: >
  Monitoriza semanalmente los cambios en la normativa ferroviaria de la UE
  (ERA/EUR-Lex). Ejecuta el scraper, compara con el estado anterior y genera
  un informe con documentos nuevos, derogados, sustituidos y modificados.
  Crea un PR con los cambios detectados.
---

# Monitor de Normativa Ferroviaria Europea

## Objetivo
Detectar cambios semanales en la documentación regulatoria de la Agencia Ferroviaria
de la Unión Europea (ERA) y generar un informe estructurado.

## Instrucciones de Ejecución

### 1. Preparación del entorno
Instala las dependencias necesarias:
```bash
pip install requests beautifulsoup4 lxml
```

### 2. Ejecutar la detección de cambios
Ejecuta el script de detección de cambios con actualización del baseline:
```bash
python detect_changes.py --update-baseline
```

Este script:
- Lee el estado anterior desde `era_regulacion_estados_miembros.json`
- Hace scraping de las fuentes de ERA para obtener datos frescos
- Compara ambos estados y detecta: documentos nuevos, derogados, sustituidos,
  con cambios de estado, modificados, y cambios en recursos de TSIs
- Genera un informe en `informes/informe_cambios_YYYY-MM-DD.md`
- Actualiza el JSON base con los nuevos datos

### 3. Revisar el informe generado
Lee el informe generado en `informes/informe_cambios_YYYY-MM-DD.md` y revisa
su contenido. Si hay cambios significativos, procede al paso 4.

### 4. Crear PR con los cambios (solo si hay cambios)
Si se detectaron cambios significativos:

1. Crea una rama con la fecha:
```bash
git checkout -b informe-normativa/YYYY-MM-DD
```

2. Añade los ficheros modificados:
```bash
git add era_regulacion_estados_miembros.json informes/
```

3. Haz commit con un mensaje descriptivo que resuma los cambios encontrados:
```bash
git commit -m "informe semanal: cambios normativa ferroviaria UE YYYY-MM-DD

<resumen breve de los cambios más relevantes>

Co-Authored-By: Oz <oz-agent@warp.dev>"
```

4. Crea un Pull Request con el título `Informe semanal: Cambios normativa ferroviaria UE — YYYY-MM-DD` y una descripción que incluya:
   - El resumen del informe
   - Los cambios más relevantes destacados
   - Enlaces a las fuentes (ERA / EUR-Lex)

### 5. Si no hay cambios
Si el informe indica "Sin cambios significativos", no es necesario crear un PR.
Simplemente informa de que la revisión se ha completado sin cambios.

## Fuentes monitorizadas
- **ERA**: https://www.era.europa.eu (TSIs, opiniones, recomendaciones)
- **EUR-Lex**: https://eur-lex.europa.eu (directivas, reglamentos, decisiones)

## Categorías de cambios detectados
- **Documentos nuevos**: regulaciones, directivas o TSIs que se publican por primera vez
- **Documentos derogados**: normativa que ha sido explícitamente derogada
- **Documentos sustituidos**: normativa reemplazada por versiones actualizadas
- **Cambios de estado**: transiciones como "En vigor" → "Modificado"
- **Modificaciones**: cambios en campos de documentos existentes (descripción, enmiendas, plazos)
- **Recursos TSI**: guías de aplicación, PDFs y documentos técnicos añadidos o retirados
