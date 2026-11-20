# Informe de Cambios en Normativa Ferroviaria UE — 2026-11-20

## Resumen

- **Período**: 2026-03-07T19:37:21.700296+00:00 → 2026-11-20T17:02:14.606729+00:00
- **Total documentos (anterior)**: 37
- **Total documentos (actual)**: 37

### Desglose de cambios

- Documentos nuevos: **0**
- Documentos derogados: **0**
- Documentos sustituidos: **0**
- Otros cambios de estado: **0**
- Documentos modificados: **0**
- Documentos eliminados del catálogo: **0**
- Recursos TSI añadidos: **4**
- Recursos TSI eliminados: **0**

## Revisión de las novedades y alcance

La comparación abarca desde el **7 de marzo de 2026**, fecha del último baseline disponible; no únicamente la última semana. Hay novedades relevantes que justifican revisión.

### ETI de control-mando y señalización (CCS)

- **Reglamento de Ejecución (UE) 2026/693**, de 19 de marzo de 2026, publicado en el DOUE el **15 de abril de 2026**. Modifica el Reglamento de Ejecución (UE) 2023/1695: incorpora nuevos procedimientos de ensayo para ETCS baseline 4 y ATO baseline 1, especificaciones de las versiones reducidas 2.1 y 2.2 y ajustes de los regímenes transitorios. También completa obligaciones relativas a compatibilidad del sistema de radio y sustituye íntegramente los anexos I y II.
- El artículo 3 establece la entrada en vigor a los veinte días de la publicación, es decir, el **5 de mayo de 2026**. El artículo 2 no exige volver a notificar los organismos de evaluación de la conformidad ya notificados con arreglo a las versiones indicadas de la ETI CCS.
- Fuentes contrastadas: [texto oficial en EUR-Lex](https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng) y [página CCS de ERA](https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en).
- ERA enlaza un [comparativo informativo de cambios del anexo I](https://www.era.europa.eu/sites/default/files/2026-04/compare%20ccs%20tsi%20amendment.pdf). Se verificó su descarga (HTTP 200 y firma PDF); no sustituye al texto oficial ni se ha realizado una revisión íntegra del PDF.

### Seguridad en túneles (SRT)

- Se incorpora un enlace al **Reglamento de Ejecución (UE) 2024/191**, de 8 de enero de 2024, publicado el **9 de enero de 2024**. Corrige la definición de túnel ferroviario en determinadas versiones lingüísticas del Reglamento 1303/2014: búlgaro, alemán, polaco, portugués y esloveno. Las demás versiones, incluida la española, no están afectadas.
- Es una **incorporación al inventario de enlaces observado**, no una norma publicada durante el período de comparación.
- Fuentes contrastadas: [EUR-Lex (ELI)](https://eur-lex.europa.eu/eli/reg_impl/2024/191/oj/eng) y [página SRT de ERA](https://www.era.europa.eu/domains/technical-specifications-interoperability/safety-railway-tunnels-tsi_en). El enlace CELEX original devolvió HTTP 403 al verificarlo; la consulta por ELI permitió contrastar el texto.

### Interpretación de los recuentos

- Se mantienen los datos brutos del detector en el JSON y en el listado automático inferior: **4 apariciones añadidas corresponden a 3 URL únicas nuevas**. El enlace al Reglamento 2026/693 aparece dos veces en la página CCS.
- El total bruto de recursos pasa de **88 a 91**: se añaden cuatro apariciones y desaparece una de las dos apariciones de un enlace al Reglamento 2023/1695. Esa URL sigue presente, por lo que no se considera un recurso retirado ni una derogación.
- Los **37 documentos del catálogo** no cambian según el detector. La modificación jurídica de la ETI CCS confirmada arriba se detecta como recurso añadido, no como modificación de una ficha: el catálogo legal se construye principalmente con datos estáticos del scraper.

### Incidencias y límites de cobertura

- Las páginas ERA de [telemática de viajeros](https://www.era.europa.eu/domains/technical-specifications-interoperability/telematics-applications-passenger-service-tsi_en) y [telemática de mercancías](https://www.era.europa.eu/domains/technical-specifications-interoperability/telematics-applications-freight-service-tsi_en) devolvieron **HTTP 403**. No se verificaron sus posibles novedades. El baseline anterior tampoco contenía recursos procedentes de estas páginas, de modo que estos fallos no generaron retiradas en la comparación.
- La página general de documentos de ERA devolvió **0 documentos extraídos**. Esto no demuestra ausencia de publicaciones: el extractor utiliza encabezados `h1` y no realiza una búsqueda exhaustiva ni paginada.
- EUR-Lex se consultó para contrastar los dos actos detectados, no como rastreo completo de nuevas publicaciones o de cambios de vigencia de los 37 documentos.
- El baseline actualizado es una captura de las fuentes accesibles, **no una certificación de revisión completa de toda la normativa ferroviaria europea**. No puede concluirse que no haya otras modificaciones, derogaciones o sustituciones.

## 📚 Cambios en Recursos Adicionales de TSIs

### Nuevos recursos (4)
- [Commission Implementing Regulation (EU) 2024/191 correcting language versions o…](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0191)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/safety-railway-tunnels-tsi_en
- [Commission Implementing Regulation (EU) 2026/693 of 19 March 2026 amending Impl…](https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en
- [INFORMATIVE. Changes to Annex I](https://www.era.europa.eu/sites/default/files/2026-04/compare%20ccs%20tsi%20amendment.pdf)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en
- [Commission Implementing Regulation (EU) 2026/693 of 19 March 2026 amending Impl…](https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en

---
*Informe generado automáticamente el 2026-11-20 17:02 UTC*
*Fuente: [ERA](https://www.era.europa.eu) / [EUR-Lex](https://eur-lex.europa.eu)*