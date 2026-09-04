# Informe de Cambios en Normativa Ferroviaria UE — 2026-09-04

## Resumen

- **Período**: 2026-03-07T19:37:21.700296+00:00 → 2026-09-04T17:03:15.031876+00:00
- **Total documentos (anterior)**: 37
- **Total documentos (actual)**: 37

### Desglose de cambios

- Documentos nuevos: **0**
- Documentos derogados: **0**
- Documentos sustituidos: **0**
- Otros cambios de estado: **1**
- Documentos modificados: **0**
- Documentos eliminados del catálogo: **0**
- Recursos TSI añadidos: **3**
- Recursos TSI eliminados: **0**

## 🔀 Cambios de Estado

- **ETI de Control-Mando y Señalización (TSI CCS)** (`TSI-CCS-2023`)
  - En vigor → En vigor (modificado por el Reglamento (UE) 2026/693)

## 📚 Cambios en Recursos Adicionales de TSIs

### Nuevos recursos (3)
- [Commission Implementing Regulation (EU) 2026/693 of 19 March 2026 amending Impl…](https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en
- [INFORMATIVE. Changes to Annex I](https://www.era.europa.eu/sites/default/files/2026-04/compare%20ccs%20tsi%20amendment.pdf)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en
- [Commission Implementing Regulation (EU) 2026/693 of 19 March 2026 amending Impl…](https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en

## 🧭 Notas de análisis

### Cambio relevante: enmienda de la ETI CCS
La página de la ETI CCS de ERA ha sustituido su bloque **Legal framework**: donde antes
figuraba el Reglamento de Ejecución (UE) 2023/1695, ahora aparece el **Reglamento de
Ejecución (UE) 2026/693, de 19 de marzo de 2026**, que modifica el 2023/1695. El
2023/1695 ha pasado al apartado *Previous version*. ERA acompaña el cambio con un
documento informativo de comparación de los cambios en el **Anexo I** de la ETI.

- Reglamento: <https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng> (CELEX 32026R0693)
- Comparativa Anexo I (informativo, PDF): <https://www.era.europa.eu/sites/default/files/2026-04/compare%20ccs%20tsi%20amendment.pdf>
- Página ERA: <https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en>

**Impacto para los estados miembros**: la ETI CCS sigue en vigor, pero su texto
consolidado cambia. Procede revisar el Anexo I (especificaciones ERTMS/ETCS del
Apéndice A) y el encaje con los planes nacionales de implementación (NIP) antes de
emitir nuevas autorizaciones de subsistemas CCS embarcados y en tierra.

### Acción aplicada sobre el catálogo
El catálogo interno (`scrape_era_regulations.py`) mantenía la ETI CCS como "En vigor"
sin enmiendas registradas. Se ha actualizado la ficha `TSI-CCS-2023` para reflejar la
enmienda, lo que aparece arriba como cambio de estado.

### Limitaciones de esta ejecución
- Las páginas de la **TSI TAP** y la **TSI TAF** devolvieron `403 Forbidden`, por lo que
  sus recursos no se han podido verificar en esta pasada. No se han registrado bajas de
  recursos derivadas de ello (ambas fuentes tampoco aportaban recursos en el estado
  anterior).
- El listado general `https://www.era.europa.eu/documents` devolvió 0 documentos: el
  scraping de esa página depende de contenido cargado por JavaScript y no aporta datos.
- El Reglamento (UE) 2026/693 aparece **duplicado** entre los recursos nuevos porque la
  página de ERA lo lista dos veces (cabecera y bloque *Legal framework*); es un único
  documento.
- EUR-Lex no ha sido accesible desde el entorno de ejecución para ampliar el título
  completo del reglamento, truncado en origen por ERA.

---
*Informe generado automáticamente el 2026-09-04 17:03 UTC*
*Fuente: [ERA](https://www.era.europa.eu) / [EUR-Lex](https://eur-lex.europa.eu)*