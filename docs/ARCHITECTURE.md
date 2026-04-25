# Plaza — Arquitectura

Este documento describe cómo está estructurado Plaza internamente: qué capas lo componen, qué hace cada una, cómo se comunican entre sí, y qué invariantes deben preservarse en las fronteras entre ellas.

La arquitectura es la implementación interna de los principios. Cada decisión arquitectónica puede trazarse a uno o más principios que la respaldan. Cuando una elección arquitectónica y un principio entran en conflicto, el principio gana — la arquitectura se ajusta.

Este documento no es un manual de implementación. No prescribe lenguajes, frameworks, ni tecnologías específicas más allá de los estándares que los principios ya establecen. Lo que prescribe son **responsabilidades, fronteras, e invariantes**.

---

## Vista general

Plaza procesa datos en cinco capas funcionales, cada una con un propósito distinto. Los datos fluyen principalmente en una dirección: desde las fuentes oficiales hasta las superficies de acceso públicas.

```
┌─────────────────────────────────────────────────────────────┐
│ Fuentes oficiales (SCIJ, Imprenta Nacional, Poder Judicial) │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. Adquisición    (Acquisition)                             │
│    Obtiene artefactos o datos por la vía habilitada         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Refinamiento   (Refinement)                              │
│    Interpreta artefactos crudos en datos estructurados      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Reconciliación (Reconciliation)                          │
│    Consolida evidencia, resuelve o declara conflictos       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Canonicalización (Canonicalization)                      │
│    Promueve estado reconciliado al grafo canónico público   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. Publicación    (Publication)                             │
│    Expone el grafo canónico por las superficies públicas    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Consumidores (Sistemas IA, investigadores, aplicaciones)    │
└─────────────────────────────────────────────────────────────┘
```

Tres capas son **mutables y operacionales** (adquisición, refinamiento, reconciliación): aquí vive el trabajo en progreso, la incertidumbre, los conflictos no resueltos. Dos capas son **inmutables una vez publicadas** (canonicalización, publicación): aquí vive lo que Plaza le entrega al mundo, con las garantías de estabilidad definidas en las políticas públicas.

La frontera entre las capas mutables y las inmutables — entre reconciliación y canonicalización — es la frontera más importante de esta arquitectura. Cruzar esa frontera requiere satisfacer todos los principios simultáneamente. Nada cruza silenciosamente; nada cruza sin evidencia.

---

## Principios arquitectónicos derivados

Cada capa respeta restricciones arquitectónicas que derivan directamente de los principios:

| Principio | Implicación arquitectónica |
|---|---|
| 1 — Evidencia antes que inferencia | Cada afirmación en el grafo canónico tiene vínculo rastreable a al menos un artefacto crudo. |
| 2 — Identidad permanente | Las URIs emitidas por la canonicalización nunca cambian. |
| 3 — Fuentes oficiales como autoridad | La adquisición nunca modifica artefactos; preserva lo que la fuente dijo y respeta la vía habilitada para accederlos. |
| 4 — Procedencia explícita | PROV-O atraviesa todas las capas; cada entidad canónica carga su cadena de procedencia. |
| 5 — Precisión temporal | Las versiones son entidades de primera clase en el grafo canónico, con URIs propias. |
| 6 — Estándares como columna | El grafo canónico se expresa en RDF con ELI, schema.org/Legislation, PROV-O, SKOS, Dublin Core Terms y extensiones `plaza:` mínimas. Akoma Ntoso se genera como serialización XML documental en la capa de publicación. |
| 7 — Separación dato/aplicación | La capa de publicación es una frontera dura: las aplicaciones consumen las superficies públicas, nunca acceden a las capas operacionales. |
| 10 — Disciplina reconstructiva | Los artefactos crudos son inmutables; cada capa posterior es derivable re-ejecutando las capas previas. |
| 11 — Honestidad operativa | Cada capa preserva las distinciones de estado (ausente, fallido, inferido, verificado) sin colapsarlas. |
| 12 — Un hogar canónico por responsabilidad | Cada capa tiene una única responsabilidad y un único módulo canónico que la implementa. |

Los Principios 8 (Ética en el modelado de entidades sensibles) y 9 (Apertura por arquitectura) no aparecen en esta tabla porque operan a nivel de gobernanza y política del proyecto, no de arquitectura técnica interna. Su implementación vive en [`SCOPE.md`](SCOPE.md) y [`LICENSING.md`](LICENSING.md) respectivamente.

---

## Las cinco capas

### Precondición: fuente habilitada

Ninguna fuente entra a adquisición mientras Plaza no haya determinado, de forma explícita:

- la base jurídica o licencia aplicable;
- la vía de acceso preferente;
- las restricciones específicas de la fuente;
- la finalidad original o función pública bajo la cual la fuente fue publicada o recabada;
- el uso previsto por Plaza sobre esa fuente;
- el juicio de compatibilidad entre la finalidad original y el uso previsto;
- si existen datos personales o incidentales relevantes;
- si la fuente requiere convenio formal;
- si la operación activa obligaciones adicionales de protección de datos o cumplimiento.

La regla general de Plaza es jerárquica: primero publicación proactiva, luego solicitud formal, luego convenio, y solo de forma residual adquisición automatizada. La adquisición no decide esa vía; la ejecuta.

### 1. Adquisición

**Responsabilidad**: obtener artefactos o datos de las fuentes oficiales por la vía previamente habilitada, preservando evidencia inmutable junto con su procedencia y el contexto de acceso.

**Entradas**: fuentes oficiales (SCIJ, Imprenta Nacional, Poder Judicial, etc.), accedidas según la vía habilitada para cada caso (publicación proactiva, respuesta a solicitud formal, entrega bajo convenio, feeds institucionales o adquisición automatizada respetuosa cuando corresponda).

**Salidas**: artefactos crudos con metadata de procedencia — URL original cuando exista, vía de acceso utilizada, timestamp de captura o recepción, hash del contenido, fuente, identidad de adquisición (el identificador que la fuente usa para referirse a este recurso: por ejemplo, los parámetros `nValor1:nValor2:nValor3` en SCIJ).

**Invariantes**:

- Los artefactos son inmutables una vez adquiridos. Si una fuente cambia, se adquiere un nuevo artefacto con timestamp posterior; el anterior se preserva.
- La adquisición nunca interpreta. No intenta identificar tipo de norma, no parsea texto, no asigna identidad canónica. Su única tarea es preservar fielmente lo que la fuente entregó.
- Las distinciones operativas se preservan: un recurso no encontrado (404) no es lo mismo que una adquisición fallida (timeout) no es lo mismo que una página de error disfrazada (HTTP 200 con contenido de error). Cada estado se registra distintamente.
- La adquisición nunca decide por sí sola usar automatización cuando existe una vía institucional o jurídica preferente mejor definida.
- Las fuentes oficiales se acceden con discreción: tasas respetuosas, user-agent identificable, respeto a robots.txt donde aplique. La adquisición automatizada es un huésped en servidores ajenos.

**Dependencias**: esta capa depende únicamente de las fuentes externas ya habilitadas. No depende de ninguna otra capa de Plaza.

**Sustituibilidad**: esta capa es la más específica por fuente. Cada fuente oficial requiere su propio módulo de adquisición con su propio conocimiento del canal habilitado. Agregar una fuente nueva (por ejemplo, el Digesto Tributario de Hacienda) requiere solo un módulo de adquisición nuevo — no toca las demás capas.

---

### 2. Refinamiento

**Responsabilidad**: interpretar los artefactos crudos en datos estructurados, preservando la trazabilidad a la evidencia original.

**Entradas**: artefactos crudos de la capa de adquisición, junto con su metadata de procedencia.

**Salidas**: datos estructurados específicos de la fuente. Para SCIJ, esto significa fichas parseadas, artículos identificados, relaciones extraídas (afectaciones, concordancias, reglamentaciones, descriptores, etc.), versiones detectadas, pistas de publicación capturadas. Para cada pieza de dato estructurado, un vínculo a la sección del artefacto crudo que la respalda.

**Invariantes**:

- El refinamiento no inventa. Si un campo no está en el artefacto crudo, se marca como ausente, nunca se completa con heurísticas sin marca explícita.
- El refinamiento es determinista: la misma entrada produce siempre la misma salida. Un refinamiento que dependa de fecha actual, aleatoriedad, o servicios externos no es refinamiento — es otra capa mal etiquetada.
- El refinamiento preserva texto crudo cuando la interpretación es incompleta. Mejor guardar el texto original de una celda ambigua que forzar una interpretación errónea.
- El refinamiento es re-ejecutable. Si se mejora el parser, se reprocesan los artefactos crudos y se obtiene mejor dato sin volver a la fuente.

**Dependencias**: depende de la capa de adquisición.

**Sustituibilidad**: como la adquisición, esta capa es específica por fuente. Un parser SCIJ no sabe nada de La Gaceta ni viceversa.

---

### 3. Reconciliación

**Responsabilidad**: consolidar evidencia de una o múltiples fuentes en un estado operacional coherente, resolviendo conflictos donde sea posible y dejándolos visibles donde no.

**Entradas**: datos estructurados de la capa de refinamiento, de una o múltiples fuentes.

**Salidas**: estado reconciliado con entidades candidatas a ser canónicas, sus relaciones, sus versiones, y los conflictos sin resolver asociados. Este estado vive en una base de datos operacional (por ejemplo, SQLite) que es mutable y de uso interno.

**Invariantes**:

- Los conflictos se declaran, no se esconden. Si dos fuentes dicen cosas distintas sobre la misma norma, la reconciliación no elige silenciosamente — registra el conflicto con evidencia de ambos lados.
- La reconciliación puede ser provisional. Un estado reconciliado puede estar incompleto, con entidades pendientes de validación, con conflictos abiertos, con versiones no asignadas todavía. Eso es normal.
- La reconciliación nunca fabrica identidad canónica. Puede proponerla, pero la asignación de URIs canónicas es responsabilidad de la capa siguiente.
- La reconciliación no cruza la frontera hacia canonicalización sin satisfacer criterios explícitos de calidad (definidos en `QUALITY_AND_VALIDATION.md`).

**Dependencias**: depende del refinamiento.

**Sustituibilidad**: la reconciliación puede usar distintas tecnologías de almacenamiento operacional (SQLite, PostgreSQL, un grafo mutable), siempre que cumpla los invariantes. La elección es operacional, no arquitectónica. SQLite es suficientemente expresivo y operativamente simple para el volumen esperado del corpus legal costarricense (decenas de miles de entidades), por lo que es una elección de implementación razonable — pero el contrato arquitectónico no depende de ella.

---

### 4. Canonicalización

**Responsabilidad**: promover el estado reconciliado a un grafo canónico expresado en los estándares semánticos internacionales, con URIs permanentes y procedencia completa.

**Entradas**: estado reconciliado, con entidades que cumplen los criterios de calidad para ser publicadas.

**Salidas**: el grafo canónico de Plaza. Un conjunto de triples RDF alineados a los estándares RDF adoptados: ELI para identidad, metadata legal, FRBR y relaciones normativas; PROV-O para procedencia; SKOS para vocabularios; Dublin Core Terms para metadata auxiliar; schema.org/Legislation para interoperabilidad web; y W3C ORG para estructuras institucionales cuando se incorporen. Cada entidad tiene una URI canónica siguiendo la política de URIs.

**Invariantes**:

- Las URIs emitidas nunca cambian. La canonicalización se compromete para siempre con cada URI que publica.
- Cada triple del grafo canónico tiene procedencia rastreable, implementada vía PROV-O. Para cualquier afirmación, un consumidor puede preguntar "¿de qué artefacto crudo vino esto?" y obtener respuesta.
- La canonicalización no inventa. Si el estado reconciliado no alcanza el umbral de calidad para una entidad, esa entidad no recibe URI canónica. Se queda en reconciliación hasta que el umbral se cumpla.
- La canonicalización es una frontera dura. El grafo canónico es el único estado que se expone públicamente. Las capas operacionales no son accesibles desde afuera.
- Las promociones al grafo canónico son auditadas. Cada promoción se registra — qué entidad, cuándo, con qué evidencia, bajo qué criterios. Esto permite reversión si se descubre un error crítico.

**Dependencias**: depende de la reconciliación.

**Sustituibilidad**: la canonicalización debe producir RDF válido bajo los estándares adoptados para el grafo canónico. La tecnología de almacenamiento del grafo canónico (triple store, archivos Turtle, JSON-LD, o materialización relacional) es operacional; el contrato es el grafo RDF mismo.

---

### 5. Publicación

**Responsabilidad**: exponer el grafo canónico al mundo a través de las superficies públicas definidas en `ACCESS_SURFACES.md`.

**Entradas**: el grafo canónico.

**Salidas**: las superficies públicas activas — snapshots descargables, API REST, servidor MCP, feed Atom, catálogo DCAT y representaciones negociadas por contenido, incluyendo HTML, JSON-LD, Turtle y Akoma Ntoso XML cuando exista estructura documental suficiente.

**Invariantes**:

- La publicación no modifica el grafo canónico. Solo lo presenta en distintos formatos y bajo distintos protocolos.
- Las superficies respetan los contratos declarados: estabilidad de URIs, idempotencia, formatos estándar, sin endpoints privilegiados.
- Los snapshots son atómicos e inmutables. Un snapshot publicado nunca se modifica — si hay errores, se publica un snapshot nuevo.
- La publicación respeta content negotiation: una URI canónica puede servirse en múltiples formatos, pero la URI es la misma.

**Dependencias**: depende de la canonicalización.

**Sustituibilidad**: cada superficie de publicación puede implementarse con distintas tecnologías (diferentes servidores web, diferentes formatos de snapshot, diferentes bibliotecas MCP) siempre que el contrato de la superficie se respete.

---

## Sustratos de datos

La arquitectura distingue tres clases de almacenamiento, cada una con un régimen diferente:

### Almacén de artefactos crudos (inmutable)

**Qué guarda**: los artefactos obtenidos por la capa de adquisición — típicamente HTML, JSON, PDF, o cualquier formato que la fuente oficial entregó — junto con su metadata de procedencia.

**Régimen**: inmutable. Una vez escrito, un artefacto crudo nunca se modifica. Si la fuente cambia, se escribe un nuevo artefacto con timestamp posterior.

**Identificación**: cada artefacto se identifica por un hash criptográfico de su contenido. Dos capturas idénticas del mismo recurso producen el mismo hash — esto permite deduplicación y verificación de integridad.

**Tecnología**: típicamente sistema de archivos, con organización por fuente/año/mes. Para escalas mayores, cualquier almacén de objetos (S3-compatible) cumple el contrato. La inmutabilidad debe garantizarse técnicamente, no solo por convención.

### Almacén operacional (mutable)

**Qué guarda**: el estado reconciliado — entidades candidatas, relaciones, conflictos, resultados intermedios de refinamiento, metadata operacional (colas de trabajo, estados de procesamiento, logs estructurados).

**Régimen**: mutable por naturaleza. Aquí vive el trabajo en progreso. La reconciliación reescribe este estado conforme nueva evidencia llega y conforme se resuelven conflictos.

**Tecnología**: una base de datos relacional es la elección práctica. SQLite es adecuado para el volumen esperado y simplifica deployment. PostgreSQL u otras alternativas son igualmente válidas si el volumen o las necesidades de concurrencia lo ameritan.

**Relación con el grafo canónico**: el almacén operacional **no es** el grafo canónico. Es el lugar donde se prepara el estado que eventualmente se promueve al grafo. Nunca se expone públicamente.

### Grafo canónico (inmutable-una-vez-publicado)

**Qué guarda**: las entidades canónicas de Plaza con sus URIs permanentes, sus relaciones, sus versiones, y su procedencia PROV-O, todo expresado en las ontologías estándar.

**Régimen**: inmutable una vez publicado. Una entidad promovida al grafo canónico permanece. Las correcciones no se hacen reescribiendo — se hacen publicando una nueva afirmación que explícitamente refiere a la anterior (por ejemplo, mediante mecanismos de rectificación documentados con PROV-O).

**Identificación**: cada entidad tiene su URI canónica según `URI_POLICY.md`.

**Tecnología**: un triple store RDF nativo es la opción más directa. Alternativamente, el grafo puede materializarse como archivos Turtle o JSON-LD versionados en Git, lo cual ofrece ventajas de trazabilidad histórica y simplicidad operacional. La elección depende de las necesidades de consulta — un triple store permite consultas SPARQL eficientes; archivos versionados requieren herramientas externas para consultas complejas pero son más portables y auditables.

---

## Fronteras y garantías

Cada frontera entre capas tiene un contrato explícito.

### Fuentes → Adquisición

**Garantía de Plaza hacia las fuentes**: respeto operacional y jurídico. La adquisición se comporta como un huésped considerado: identifica su identidad cuando corresponde, respeta tasas, no sobrecarga, acepta ser rechazada, y no trata toda fuente como scrapeable por defecto.

**Garantía de las fuentes hacia la adquisición**: ninguna. Las fuentes oficiales operan según sus propias reglas. La adquisición debe tolerar disponibilidad variable, cambios de formato, errores intermitentes y canales de acceso heterogéneos.

### Adquisición → Refinamiento

**Contrato**: el refinamiento recibe artefactos inmutables con metadata de procedencia completa, incluyendo la vía de acceso utilizada cuando sea relevante. Nunca recibe datos ya interpretados.

### Refinamiento → Reconciliación

**Contrato**: la reconciliación recibe datos estructurados con trazabilidad a los artefactos crudos que los respaldan. Recibe incertidumbre marcada, no silenciada.

### Reconciliación → Canonicalización

**Contrato**: esta es la frontera más dura. La canonicalización solo acepta entidades que cumplen criterios explícitos de calidad. Una entidad que no los cumple permanece en reconciliación hasta que los cumpla — nunca se promueve a la fuerza.

### Canonicalización → Publicación

**Contrato**: la publicación opera sobre el grafo canónico como si fuera de solo lectura. Nunca lo modifica, nunca lo reinterpreta, nunca lo aumenta.

### Publicación → Consumidores

**Contrato**: los definidos en `ACCESS_SURFACES.md`. Las superficies son el único punto de contacto entre Plaza y el mundo. No hay back doors.

---

## Extensibilidad

La arquitectura está diseñada para admitir extensión sin refactoring:

### Agregar una nueva fuente oficial

Agregar La Gaceta, el Digesto Tributario de Hacienda, o cualquier otra fuente oficial requiere:

1. Un nuevo módulo de adquisición específico para la fuente.
2. Un nuevo módulo de refinamiento específico para el formato de la fuente.
3. Extensiones a los criterios de reconciliación para considerar evidencia de la nueva fuente.

**No requiere** cambios en canonicalización, en el grafo canónico, o en las superficies de publicación. Esas capas hablan en estándares universales; el grafo canónico no sabe ni le importa si un hecho vino de SCIJ o de La Gaceta — solo le importa que tenga procedencia rastreable.

### Agregar un nuevo tipo de entidad (por ejemplo, instituciones)

Agregar la capa institucional (cuando el SCOPE lo permita) requiere:

1. Extensión del grafo canónico con las nuevas clases de W3C ORG.
2. Nuevos criterios de canonicalización para decidir cuándo una institución se promueve.
3. Extensión de los criterios de reconciliación para manejar evidencia institucional (típicamente extraída de las mismas fuentes que ya se capturan).
4. Posiblemente extensiones al `URI_POLICY.md` para acomodar las URIs de instituciones.

**No requiere** recapturar fuentes, reescribir artefactos crudos, ni cambiar las superficies de publicación (las superficies exponen lo que haya en el grafo canónico).

### Agregar una nueva superficie de acceso

Agregar, por ejemplo, un endpoint SPARQL (cuando el SCOPE lo permita) requiere:

1. Un nuevo módulo de publicación que sirve SPARQL sobre el grafo canónico.
2. Actualización de `ACCESS_SURFACES.md` documentando el contrato.

**No requiere** tocar ninguna capa anterior. El grafo canónico ya es RDF; exponer SPARQL es un problema de capa de publicación.

---

## Lo que esta arquitectura explícitamente NO es

### No es una pipeline lineal simple

Aunque el flujo es principalmente descendente (adquisición → publicación), hay ciclos legítimos:

- La reconciliación puede solicitar nuevas capturas si descubre evidencia faltante.
- El refinamiento puede re-ejecutarse sobre artefactos antiguos cuando mejora el parser.
- La canonicalización puede revertir promociones si se descubre que violan invariantes.

Lo que **no** hay son ciclos hacia arriba desde publicación: la publicación nunca modifica capas anteriores. Es estrictamente de solo lectura sobre el grafo canónico.

### No es service-oriented con boundaries de red

Las capas son conceptuales, no necesariamente procesos separados. La implementación puede correr todas las capas en un único proceso, o dividirlas en servicios, según conveniencia operacional. La frontera arquitectónica es de **responsabilidad**, no de red.

### No es tolerante a borrar artefactos crudos

Borrar un artefacto crudo destruye la capacidad de reconstruir. Es una operación que, si ocurre, debe ser excepcional, documentada, y justificada (por ejemplo, datos personales accidentalmente capturados que no deberían estar). La arquitectura asume que los artefactos crudos se preservan indefinidamente.

### No es un monolito con módulos; no es micro-servicios con colas

Es una arquitectura de capas con fronteras estrictas. La implementación de las capas puede usar cualquier patrón que respete esas fronteras: clases con interfaces claras, módulos con funciones puras, o servicios independientes con colas. Lo que importa es que las fronteras no se violen, no el patrón específico.

---

## Relación con otras políticas

- [`PRINCIPLES.md`](PRINCIPLES.md) — los principios que esta arquitectura implementa.
- [`SCOPE.md`](SCOPE.md) — qué entidades esta arquitectura maneja hoy y cuáles potencialmente en el futuro.
- [`URI_POLICY.md`](URI_POLICY.md) — el contrato de identidad que la capa de canonicalización debe satisfacer.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — los contratos que la capa de publicación debe cumplir.
- [`DATA_MODEL.md`](DATA_MODEL.md) — la especificación detallada del grafo canónico: qué clases, qué propiedades, qué restricciones, alineadas a las ontologías estándar.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — los criterios explícitos que una entidad debe satisfacer para cruzar la frontera de reconciliación hacia canonicalización.
