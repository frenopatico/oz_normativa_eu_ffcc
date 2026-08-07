# Informe de Cambios en Normativa Ferroviaria UE — 2026-08-07

## Resumen

- **Período**: 2026-03-07T19:37:21.700296+00:00 → 2026-08-07T17:01:19.887160+00:00
- **Total documentos (anterior)**: 37
- **Total documentos (actual)**: 37

### Desglose de cambios

- Documentos nuevos: **0**
- Documentos derogados: **0**
- Documentos sustituidos: **0**
- Otros cambios de estado: **0**
- Documentos modificados: **0**
- Documentos eliminados del catálogo: **0**
- Recursos TSI añadidos: **2**
- Recursos TSI eliminados: **0**

## 📚 Cambios en Recursos Adicionales de TSIs

### Nuevos recursos (2)
- [Commission Implementing Regulation (EU) 2026/693 of 19 March 2026 amending Impl…](https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en
- [INFORMATIVE. Changes to Annex I](https://www.era.europa.eu/sites/default/files/2026-04/compare%20ccs%20tsi%20amendment.pdf)
  - Fuente: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en

## 🔎 Análisis del cambio relevante

### Reglamento de Ejecución (UE) 2026/693 — modificación de la ETI CCS

Verificado en EUR-Lex el 2026-08-07.

- **Título oficial**: *Commission Implementing Regulation (EU) 2026/693 of 19 March 2026 amending Implementing Regulation (EU) 2023/1695 as regards new testing specifications, a set of reduced specifications and transitional measures* (Text with EEA relevance)
- **CELEX**: `32026R0693`
- **Adopción**: 19 de marzo de 2026
- **Publicación DOUE**: OJ L, 2026/693, 15.4.2026 — referencia interna `C/2026/1769`
- **Entrada en vigor**: vigésimo día siguiente a su publicación (≈ 5 de mayo de 2026)
- **Estado**: en vigor
- **Base jurídica**: Directiva (UE) 2016/797, art. 5(11) y art. 48(2)
- **Norma modificada**: Reglamento de Ejecución (UE) 2023/1695 (ETI de control-mando y señalización, CCS)
- **Enlace**: https://eur-lex.europa.eu/eli/reg_impl/2026/693/oj/eng

#### Contenido de la modificación

1. **Nuevas especificaciones de ensayo** — se introducen procedimientos de ensayo para
   equipos ETCS embarcados y de vía basados en *Baseline 4* y para equipos ATO basados en
   *Baseline 1*, con el fin de garantizar la circulación segura y con prestaciones
   aceptables sobre líneas ETCS/ATO conformes.
2. **Conjunto de especificaciones reducidas** — el Reglamento 2023/1695 definía únicamente
   las funcionalidades de la versión de sistema más completa (3.0). La modificación añade
   la descripción detallada de las funcionalidades de las dos versiones reducidas,
   **2.1 y 2.2**, dentro del conjunto único de especificaciones.
3. **Medidas transitorias** — se ajustan las disposiciones transitorias aplicables a
   contratos ya en ejecución, para evitar costes indebidos derivados de cambios demasiado
   frecuentes en el marco jurídico.
4. **Artículo 2 del Reglamento 2023/1695 modificado** — se suprime la segunda frase del
   apartado 1 y se sustituyen los apartados 2 y 3, reformulando el régimen de no aplicación
   de la ETI a los subsistemas CCS de vía y embarcados ya puestos en el mercado y en
   servicio antes del **28 de septiembre de 2023**, salvo en los supuestos enumerados.

#### Documento de apoyo publicado por ERA

- **INFORMATIVE. Changes to Annex I** (PDF comparativo del Anexo I de la ETI CCS):
  https://www.era.europa.eu/sites/default/files/2026-04/compare%20ccs%20tsi%20amendment.pdf

#### Impacto para los estados miembros

- Afecta a la **ETI CCS**, de aplicación directa en todos los estados miembros; no requiere
  transposición, pero sí adaptación de procesos nacionales.
- Las **autoridades nacionales de seguridad (ANS)** y los **organismos notificados (NoBo)**
  deberán aplicar los nuevos procedimientos de ensayo en las evaluaciones de conformidad de
  subsistemas CCS y en las autorizaciones de puesta en el mercado de vehículos.
- Los **administradores de infraestructura** y **empresas ferroviarias** con proyectos ETCS
  Baseline 4 / ATO Baseline 1 en curso deben revisar las medidas transitorias para
  determinar el régimen aplicable a sus contratos vigentes.
- La formalización de las versiones de sistema **2.1 y 2.2** aporta seguridad jurídica a los
  despliegues que no implementan la versión 3.0 completa.

#### Actualización pendiente del catálogo

El catálogo `era_regulacion_estados_miembros.json` describe la ETI CCS mediante una entrada
fija basada en el Reglamento 2023/1695. Conviene registrar el Reglamento 2026/693 como
enmienda de esa entrada para que futuras revisiones partan de un estado consolidado.

## ⚠️ Salvedades de cobertura de esta ejecución

Durante el scraping se registraron las siguientes limitaciones, que reducen la cobertura del
informe respecto al alcance teórico:

- La página general de documentos de ERA (`https://www.era.europa.eu/documents`) devolvió
  **0 documentos**. La respuesta se obtuvo correctamente, por lo que el problema apunta a
  contenido cargado dinámicamente o a un cambio de maquetación que invalida los selectores.
- Dos páginas de ETIs devolvieron **HTTP 403 Forbidden**, por lo que sus recursos no se
  revisaron en esta ejecución:
  - ETI Aplicaciones Telemáticas para el Servicio de Viajeros (TAP)
  - ETI Aplicaciones Telemáticas para el Servicio de Mercancías (TAF)
  Ninguna de las dos aportaba recursos al estado anterior, de modo que **no se ha perdido
  información** ya registrada ni se han generado falsos "recursos eliminados".
- El bloque `documentos_regulatorios` (37 documentos) proviene de listas mantenidas a mano en
  `scrape_era_regulations.py`, no de scraping. Por tanto, los contadores de documentos
  nuevos, derogados, sustituidos y modificados solo pueden variar si se actualiza ese código:
  los **0** de esas categorías no deben interpretarse como confirmación de ausencia de
  cambios normativos.

---
*Informe generado automáticamente el 2026-08-07 17:03 UTC*
*Fuente: [ERA](https://www.era.europa.eu) / [EUR-Lex](https://eur-lex.europa.eu)*
