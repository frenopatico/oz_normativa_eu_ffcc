# Análisis de los Cambios Recientes en la ETI de Señalización (ETI CCS)

## Resumen Ejecutivo

El Reglamento de Ejecución (UE) 2023/1695 de la Comisión, de 10 de agosto de 2023, establece la nueva especificación técnica de interoperabilidad (ETI) relativa a los subsistemas de control-mando y señalización del sistema ferroviario de la Unión Europea, derogando el Reglamento (UE) 2016/919.

La aplicación de la nueva ETI CCS ha sido obligatoria desde su entrada en vigor en agosto de 2023.

## 1. Contexto y Motivación de la Revisión

La revisión de la ETI se realiza conforme al artículo 3, apartado 5, letras b) y f), de la Decisión Delegada (UE) 2017/1474 de la Comisión, con el fin de tomar en consideración la evolución del sistema ferroviario de la Unión y las actividades de investigación e innovación en este ámbito, y actualizar las referencias a las normas.

Esta versión puede considerarse la mayor revolución en la señalización ferroviaria europea desde la implementación del ERTMS debido a la introducción de dos sistemas que traerán un cambio total en el sector.

## 2. Principales Cambios e Innovaciones

### 2.1. Nueva Estructura de Baselines: ETCS Baseline 4 Release 1 (B4R1)

Mientras que la versión 2016 de la ETI CCS utilizaba tres baselines diferentes (BL2, BL3MR1 y BL3R2), la nueva versión tiene solo una: baseline 4 (BL4). Dentro de esta BL4 se distinguen cuatro versiones de sistema diferentes (2.1, 2.2, 2.3 y 3.0).

La ETI CCS 2023/1695 incluye principalmente cambios vinculados a la introducción de ETCS Baseline 4 Release 1, ATO Baseline 1 Release 1 y RMR (compuesto de GSM-R Baseline 1 Maintenance Release 1 + FRMCS Baseline 0).

**Configuraciones ETCS B4R1:**

- **ETCS B4R1 (hasta SV2.1)**: requerido a corto plazo como funcionalidad obligatoria (incluyendo relocation without linking), manteniendo ETCS B3R2 OBU con todas las correcciones de errores que puedan impedir el servicio normal y la mejora 'relocation without linking' requerida para algunas implementaciones L1 LS existentes

- **ETCS B4R1 (hasta SV2.2)**: requerido a corto plazo como opcional en caso de implementar funcionalidad ATO

- **ETCS B4R1 (hasta SV3.0)**: requerido a medio plazo como funcionalidad obligatoria (es decir, ETCS preparado para 'FRMCS' y 'Maniobras Supervisadas' incluyendo DAC). La estrategia a medio plazo debe ser definida por el Estado miembro (NIP) y el resultado esperado es que ETCS SV3.0 será impulsado por la obsolescencia de GSM-R

### 2.2. Introducción del Sistema de Operación Automática de Trenes (ATO)

La ETI CCS 2023/1695 introduce los Grados de Automatización 1 y 2. ATO se considera como una tercera parte nueva de CCS.

La ETI CCS 2023/1695 incluye el conjunto de especificaciones ATO con el objetivo de lograr la interoperabilidad para ATO GoA1/2.

**Componentes del Sistema ATO:**

- **ATO On-Board (ATO-OB)**: representa el subsistema y conjunto de funciones automatizadas no relacionadas con la seguridad del conductor

- **ATO Trackside (ATO-TS)**: representa un conjunto de funciones que interactúan con los sistemas en vía que contienen los datos operacionales y de infraestructura requeridos por el ATO-OB

- ATO (Operación Automática de Trenes) es el sistema que automatiza la operación del tren hasta Grado de Automatización 2 (GoA2). El ATO GoA2 inicia y detiene el tren automáticamente con ETCS proporcionando la funcionalidad de protección automática del tren (ATP) para habilitar las funciones ATO

**Beneficios del ATO:**

ATO proporciona beneficios de capacidad y reduce el consumo de energía (ferrocarril verde).

### 2.3. Future Railway Mobile Communication System (FRMCS)

El sistema RMR de clase A comprende dos sistemas de radio clase A: GSM-R y FRMCS (Future Railway Mobile Communication System) que pueden implementarse ambos al mismo tiempo o cada uno de forma independiente.

**Contexto de la Transición:**

GSM-R (2G) quedará obsoleto entre 2035-2040 y debe ser reemplazado por FRMCS (5G). La mayor digitalización del ferrocarril con 5G abre muchas posibilidades.

Debido al decreciente soporte ofrecido por los fabricantes para equipos GSM/2G y la imposibilidad de un sistema basado en tecnología 2G para satisfacer los flujos de datos requeridos por las aplicaciones ferroviarias del futuro, la obsolescencia de los equipos GSM-R, que se espera para 2030-2035, hace que la implementación y transición a FRMCS sea una realidad urgente.

**Ventajas Tecnológicas del FRMCS:**

Avances como el uso de tecnología 5G versus el 2G de GSM-R, anchos de banda ligeramente más amplios en la banda de 900 MHz junto con la adición de la banda incomparable de 1900 MHz, y métodos de transmisión más eficientes (OFDM vs. TDMA) entre muchos otros factores, hacen de FRMCS el habilitador necesario para el futuro ferroviario digital.

**Estado de las Especificaciones:**

La ETI CCS 2023/1695 incluye solo el conjunto obligatorio de especificaciones FRMCS con el objetivo de lograr la interoperabilidad al implementar FRMCS. La arquitectura de referencia FRMCS se describe en los índices 95 y 96 (FRMCS FRS y SRS) de la Tabla A2 del Apéndice A de la ETI CCS. Se integran funcionalidades voluntarias adicionales en las especificaciones FRMCS.

Las especificaciones completas de FRMCS a bordo no forman parte de la ETI CCS 2023/1695.

**Régimen de Transición:**

Régimen de transición: plan de implementación de FRMCS como parte del NIP (incluso si las especificaciones aún no forman parte de la ETI CCS 2023/1695). La ETI CCS proporciona la obligación a los IMs de proporcionar al menos un período de notificación mínimo de 5 años antes de que se detengan los servicios GSM-R.

### 2.4. Nuevas Funcionalidades "Game Changers"

En Agosto de 2023, se ha publicado la última versión de las ETIs de Control Mando y Señalización, que incorpora significativos cambios en los documentos, incluyendo también nuevas funcionalidades a nivel de sistema que se han denominado "game changers".

**Maniobras Supervisadas (Supervised Manoeuvres):**

Las "Maniobras Supervisadas" permiten una supervisión mejorada de los movimientos de maniobra, similar al modo de operación de Supervisión Completa, cuando la cabina no está necesariamente en el frente de la cabina de maniobra.

Maniobras supervisadas: permiten un aumento de la seguridad y cuando se utiliza el acoplamiento automático digital permitirá eliminar las señales de maniobra.

**Relocation Without Linking:**

Mejora 'relocation without linking' requerida para algunas implementaciones L1 LS en vía existentes.

**Integridad del Tren:**

Detección híbrida de trenes: la integridad del tren permite un aumento de capacidad y/o sistemas reducidos de detección de trenes en vía.

### 2.5. Fusión de Niveles ETCS 2 y 3

El nivel 2 implica supervisión continua del movimiento del tren con comunicación constante vía RMR entre el tren y la vía. El nivel 2 tal como se define ahora en la ETI CCS 2023 fusiona el Nivel 2 y el Nivel 3 de ETCS como se describían en la ETI CCS anterior. Las señales de vía son opcionales en este caso, y las comprobaciones de detección e integridad del tren podrían realizarse mediante el equipo en vía fuera del alcance de ERTMS o gestionarse dentro del alcance del sistema ERTMS.

Desde un punto de vista de aplicación, el Nivel 3 ha sido eliminado, delegando cualquier funcionalidad de supervisión de integridad del tren al Nivel 2.

## 3. Régimen de Transición

El concepto de régimen de transición se introduce en todas las ETI relacionadas con a bordo y se basa en 4 categorías: fase de diseño iniciada después de que la ETI entre en vigor (vinculada a la primera/nueva autorización de un tipo de vehículo); fase de diseño iniciada antes de que la ETI entre en vigor; vehículos en operación (incluida la extensión del área de uso). Para cada cambio de ETI, la ETI CCS 2023/1695 establece las condiciones 'si' el cambio de ETI es obligatorio y el plazo 'cuándo' se vuelve obligatorio.

## 4. Sistema de Detección de Trenes

A más tardar el 31 de diciembre de 2024, los administradores de infraestructuras informarán a la Agencia sobre los límites de corriente de interferencia necesarios o las frecuencias de la gestión de frecuencias para los sistemas de detección de trenes conformes con la ETI. Estos límites o frecuencias se publicarán en el sitio web de la Agencia.

Con la publicación de los casos específicos, a más tardar el 31 de diciembre de 2025, los Estados miembros derogarán todas las normas nacionales relativas a la compatibilidad con los sistemas de detección de trenes, excepto en los casos contemplados en el artículo 13, apartado 2, letra f), de la Directiva (UE) 2016/797.

## 5. Mejoras en la Gestión de Cambios y Corrección de Errores

Para determinar la funcionalidad exacta de un sistema ETCS de infraestructura o de tren, es necesario no solo conocer la Versión del Sistema, sino también qué correcciones de errores, o Solicitudes de Cambio (CR), se han implementado. La ahora considerable lista de CRs se mantiene centralmente por la ERA (Agencia Ferroviaria Europea).

ETI CCS 2023/1695: Responsabilidad de los proveedores (en vía y a bordo) para la implementación de correcciones de errores en productos; Si los errores están impidiendo el servicio normal en proyectos específicos, los IMs y RUs deberán actuar.

## 6. Implementación en España

### 6.1. Normas Técnicas Nacionales

La Resolución 2/2024 de la Agencia Estatal de Seguridad Ferroviaria sobre normas técnicas nacionales en el ámbito de la interoperabilidad relativas a los subsistemas estructurales fijos fue firmada el 07/07/2025.

El Reglamento de Ejecución (UE) 2023/1695 de la Comisión de 10 de agosto de 2023 sobre la especificación técnica de interoperabilidad relativa a los subsistemas de control-mando y señalización del sistema ferroviario de la Unión Europea deroga el Reglamento (UE) 2016/919.

### 6.2. Especificaciones Técnicas de Circulación ETCS

La Resolución 4/2024 aprueba la "Especificación Técnica de Circulación. Funcionalidad nacional y valores nacionales del sistema ERTMS/ETCS [ETC ETCS (FN)]", versión 2 (22/03/2024).

La especificación detalla los requisitos de la funcionalidad nacional, en particular la funcionalidad correspondiente a transiciones dinámicas desde Niveles 1, STM/NTC, 2 o 3 de ETCS a Nivel 0 (con ASFA) y viceversa, de modo que se garantice la interoperabilidad nacional entre sistemas de distintos fabricantes. La especificación complementa y desarrolla lo previsto por el artículo 5AN1.1.4.1. "Transiciones nominales" del RCF, definiendo los requisitos técnicos de detalle necesarios tanto para los equipos de control, mando y señalización embarcados como de tierra.

## 7. Implicaciones para el Sector

### 7.1. Para Administradores de Infraestructura

La ETI CCS 2023 – que también establece requisitos obligatorios para la seguridad tecnológica – fue desarrollada, en parte, para abordar esta brecha en la adopción de ERTMS, mejorando la alineación de productos y especificaciones nacionales.

### 7.2. Para Operadores Ferroviarios

Con la transición a FRMCS como prioridad urgente, los administradores de infraestructura ferroviaria y los fabricantes deben adaptarse a esta nueva realidad tecnológica si desean mantenerse competitivos en un entorno cada vez más digitalizado. Los actores clave en este proceso deben estar preparados para adoptar estas tecnologías disruptivas, asegurar una transición fluida y liderar el cambio hacia un futuro ferroviario más conectado y automatizado.

### 7.3. Interoperabilidad

La ETI de CMS establece los requisitos técnicos para los sistemas de control, mando y señalización en toda Europa, con el objetivo de promover la interoperabilidad y la armonización en el sector ferroviario.

## 8. Conclusiones

La ETI CCS 2023/1695 representa una transformación fundamental en el panorama de la señalización ferroviaria europea:

1. **Simplificación estructural**: Consolidación de tres baselines en una sola (B4) con múltiples versiones del sistema

2. **Digitalización**: Introducción de FRMCS como sucesor de GSM-R, aprovechando la tecnología 5G

3. **Automatización**: Incorporación formal del ATO para grados de automatización 1 y 2

4. **Flexibilidad operativa**: Nuevas funcionalidades como maniobras supervisadas y relocation without linking

5. **Interoperabilidad mejorada**: Armonización de especificaciones nacionales y mejor gestión de versiones

6. **Transición planificada**: Régimen de transición claro con plazos definidos para implementación obligatoria

La implementación exitosa de estos cambios requerirá una estrecha coordinación entre Estados miembros, administradores de infraestructura, operadores ferroviarios y fabricantes de equipos.

## Referencias Normativas

- **Reglamento de Ejecución (UE) 2023/1695** de la Comisión de 10 de agosto de 2023 sobre la especificación técnica de interoperabilidad relativa a los subsistemas de control-mando y señalización
- **Directiva (UE) 2016/797** sobre la interoperabilidad del sistema ferroviario dentro de la Unión Europea
- **Reglamento (UE) 2016/919** (derogado por el Reglamento 2023/1695)
- **Guía de Aplicación de la ETI CCS 2023/1695** (ERA, diciembre 2024)

## Enlaces Útiles

- EUR-Lex: https://eur-lex.europa.eu/eli/reg_impl/2023/1695/oj
- ERA - Control Command and Signalling TSI: https://www.era.europa.eu/domains/technical-specifications-interoperability/control-command-and-signalling-tsi_en
- AESF - Normativa de Interoperabilidad: https://www.seguridadferroviaria.es/normativa/normativa-europea/normativa-en-materia-de-interoperabilidad
