---
name: investigar-normativa-ferroviaria-ue
description: Busca, analiza y resume leyes, directivas y Especificaciones Técnicas de Interoperabilidad (ETI/TSI) de la Agencia Ferroviaria de la Unión Europea (ERA) y EUR-Lex.
---

# Investigación de Normativa Ferroviaria Europea

## Contexto
El sector ferroviario en Europa está regido por el pilar técnico del Cuarto Paquete Ferroviario. [cite_start]Los agentes deben priorizar la interoperabilidad, la seguridad y las normas de la ERA[cite: 33].

## Instrucciones de Ejecución

1. **Búsqueda en Fuentes Oficiales**:
   - [cite_start]Utiliza la capacidad de **Búsqueda Web** para acceder prioritariamente a `eur-lex.europa.eu` y `era.europa.eu`[cite: 729].
   - [cite_start]Identifica si la consulta se refiere a seguridad, interoperabilidad o gestión del tráfico (ERTMS)[cite: 261].

2. **Verificación de Vigencia**:
   - [cite_start]Antes de resumir, comprueba el estado del documento (En vigor, Derogado o Modificado)[cite: 261].
   - [cite_start]Busca específicamente "ETI" (Especificaciones Técnicas de Interoperabilidad) actuales para el subsistema afectado[cite: 485].

3. **Tabla de Decisión de Fuentes**:
   | Necesidad de Información | Fuente Primaria |
   | :--- | :--- |
   | Texto legal completo (Directivas/Reglamentos) | EUR-Lex |
   | Estándares Técnicos y Certificación | ERA (European Union Agency for Railways) |
   | Normas nacionales de ejecución | Organismos Nacionales de Seguridad (NSA) |

4. **Extracción de "ADN" Normativo**:
   - [cite_start]Resume los puntos críticos de cumplimiento[cite: 660].
   - [cite_start]Lista los plazos de implementación mencionados en los artículos de "Disposiciones Transitorias"[cite: 261].

5. **Gobernanza y Auditoría**:
   - [cite_start]Proporciona un **enlace directo (URL)** a cada fuente consultada para facilitar la revisión humana[cite: 310].
   - [cite_start]Si existe una contradicción entre una directiva general y una ETI específica, escala la duda al usuario humano[cite: 217, 747].

## Ejemplos de Prompt para el Agente
- [cite_start]"Busca el Reglamento de Ejecución (UE) 2019/773 sobre la explotación y gestión del tráfico y resume su impacto en el frenado de trenes de carga"[cite: 228].
- [cite_start]"Identifica las últimas actualizaciones de la ETI de Seguridad en los Túneles Ferroviarios"[cite: 228].

## Restricciones (Guardrails)
- [cite_start]**Nunca** cites blogs de opinión o noticias secundarias como fuente legal[cite: 486].
- [cite_start]**Nunca** asumas que una normativa española o francesa es idéntica a la europea sin verificar la directiva de transposición[cite: 487].
