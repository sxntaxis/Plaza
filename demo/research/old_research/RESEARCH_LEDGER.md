# Plaza — Legacy Research Ledger

**Propósito:** registrar qué conocimiento reutilizable se absorbió de cada documento legacy y dónde quedó. Este ledger existe para evitar volver a abrir `olddocs.tar.xz`.

**Regla:** si una pieza no aparece aquí, no se considera conocimiento útil para Plaza nueva, salvo que una investigación fresca demuestre lo contrario.

---

## Leyenda

| Estado | Significado |
|---|---|
| **Absorbido** | El conocimiento útil fue migrado a este distill. |
| **Parcial** | Solo se conservó una parte; el resto se descarta. |
| **Archivado** | Útil como historia, no como insumo activo. |
| **Descartado** | No debe usarse para decisiones nuevas. |
| **Requiere web refresh** | Sirve como pista, pero cualquier afirmación factual actual debe verificarse en web antes de implementar. |

---

## Research core

| Documento legacy | Estado | Qué se extrajo | Quedó en | Qué se descartó |
|---|---:|---|---|---|
| `docs/research/README.md` | Parcial | La regla de que research no es normativo y debe subordinarse a docs canónicos. | `README.md` | El mapa viejo de clases. |
| `docs/research/RDF_adoption_roadmap.md` | Absorbido | Arquitectura por capas; no reemplazar operación por RDF; adoptar estándares por responsabilidad; postergar SPARQL; riesgos de vanity standards, dual truth, identifiers inestables y people modeling prematuro. | `STANDARDS_RESEARCH_NOTES.md`, `FUTURE_STATE_HUB_NOTES.md` | La propuesta vieja de URIs `/id/...`; la jerarquía que trataba ELI como solo “guiding pattern”; cualquier secuencia dependiente de SQLite legacy. |
| `docs/research/Knowledge-Graph_Standards.md` | Parcial | Lista de estándares candidatos; idea de JSON-LD/Turtle mínimo; SHACL como validación; PROV-O; DCAT; SKOS; schema.org; Dublin Core. | `STANDARDS_RESEARCH_NOTES.md` | FOAF como adopción temprana; LKIF/ODRL como necesidades iniciales; tablas SQL legacy; ejemplos SPARQL como diseño actual. |
| `docs/research/SCIJ_Surfaces.md` | Absorbido | Inventario de tabs SCIJ; URL families; marcadores `nValor`; banners de versión; surfaces de afectaciones, concordancias, reglamentaciones, pronunciamientos, acciones constitucionales, observaciones, descriptores, selectiva, temática y normas usuales; fixtures sugeridos; controlled scrape rules. | `source_adapters/SCIJ.md`, `USER_TASKS_AND_DEMO_LEADS.md` | Nombres de tablas legacy; afirmación de cobertura actual; migraciones SQL; timeline viejo. |
| `docs/research/Harvest_Research.md` | Parcial | SCIJ tabs; reconciliation checklist; fixtures; reglas de scrape prudente; no mezclar tipos de relación. | `source_adapters/SCIJ.md` | SQL snippets, prompt de implementación, estado de repo viejo. |
| `docs/research/RAG.md` | Parcial | IA debe consumir retrieval verificable; no interpretar; surfaces SCIJ relevantes para contexto; fixture discipline. | `RAG_AND_MCP_RESEARCH_NOTES.md`, `source_adapters/SCIJ.md` | Tablas y migraciones legacy; nombres de módulos; enlaces eliminados. |
| `docs/research/SCIJ Field Validation and Campaign Notes.md` | Parcial | Valor de validación en vivo; proof de adquisición amplia; disciplina de working set; no confundir campaña con modelo. | `source_adapters/SCIJ.md`, `REQUIREMENTS_TRACEABILITY_NOTES.md` | Estado de campaña como verdad; números de cobertura como promesa. |
| `docs/research/harvest_observations.md` | Absorbido | Separación entre mecánica reusable y assumptions no reusables; URL authority centralizada; URL validation debe gobernar; version follow-up semánticamente frágil; `failed` vs `review_needed`; no copiar SCIJ a La Gaceta. | `source_adapters/SOURCE_ADAPTER_TEMPLATE.md`, `source_adapters/SCIJ.md`, `source_adapters/GACETA.md`, `REQUIREMENTS_TRACEABILITY_NOTES.md` | Crítica a módulos concretos del repo viejo; nombres de actores internos. |
| `docs/research/Gaceta.md` | Absorbido | Comportamiento de La Gaceta: publicación por fecha, `COMP`, `ALCA`, PDFs, HTML view, metadata en texto, secciones, no RSS/sitemap confiable, discovery date-driven, PDF como artefacto primario, tasa prudente. | `source_adapters/GACETA.md`, `SOURCE_REGISTRY_CANDIDATES.md` | Afirmaciones legales no verificadas por `LEGAL_BASIS.md`; suposición de que todo lo visible es publicable. |
| `docs/research/Fuentes oficiales para descargar textos jurídicos de Costa Rica en texto completo.md` | Absorbido | Mapa de fuentes: PGR/SCIJ, Imprenta/La Gaceta, Asamblea, TSE, Hacienda, Poder Judicial/Nexus, SINABI, Archivo. | `SOURCE_REGISTRY_CANDIDATES.md` | URLs como contrato estable; licencias sin verificación; “última actualización” como verdad actual. |
| `docs/research/Costa Rican Legal Information Needs and SCIJ-Parity Opportunities for the Plaza Project.md` | Parcial | Parity como bundle de comportamientos, no UI; tareas de usuario; métricas de cobertura/calidad; valor de versión, publicación, relaciones y búsqueda. | `USER_TASKS_AND_DEMO_LEADS.md` | “SQLite as source of truth” como dogma; UI parity; roadmaps fechados; estado del repo viejo. |
| `docs/research/Plaza as the Costa Rican State Hub: Vision & Roadmap.md` | Parcial bajo restricción | Visión de largo plazo: capa institucional, cargos, titularidad oficial con evidencia. | `FUTURE_STATE_HUB_NOTES.md` | Personas como capa temprana; perfiles; relaciones biográficas; state hub como scope activo. |
| `docs/research/IEEE.md` | Parcial | Uso sano de requisitos verificables, acceptance criteria, traceability matrix, viewpoints. | `REQUIREMENTS_TRACEABILITY_NOTES.md` | SRS completo estilo enterprise; documentación lifecycle pesada; roadmap de compliance. |

---

## Roadmaps con información de source behavior

Estos documentos no se conservan como roadmaps. Solo se extrajo comportamiento estable de fuente o reglas de validación.

| Documento legacy | Estado | Qué se extrajo | Quedó en | Qué se descartó |
|---|---:|---|---|---|
| `docs/roadmaps/districts/harvest_scij_roadmap.md` | Parcial | Frontera harvest/extract; status de SCIJ como distrito; exit criteria reutilizables a nivel conceptual. | `source_adapters/SCIJ.md`, `REQUIREMENTS_TRACEABILITY_NOTES.md` | Fases, fechas, tareas cerradas. |
| `docs/roadmaps/districts/extract_scij_roadmap.md` | Parcial | Extract como capa distinta a adquisición; criterios de salida. | `source_adapters/SCIJ.md` | Estado de implementación. |
| `docs/roadmaps/districts/harvest_gaceta_roadmap.md` | Parcial | La Gaceta necesita adapter propio; extract layer existe aparte; corpus-grounded rediscovery. | `source_adapters/GACETA.md` | Estado “completo” de familias; fases ejecutadas. |
| `docs/roadmaps/districts/extract_gaceta/taxonomy.md` | Absorbido con reducción | Taxonomía de familias Gaceta; overlaps con SCIJ; familias de alto riesgo; no resolver referencias a SCIJ en extract; defer reconciliation. | `source_adapters/GACETA.md` | Prioridades P3/P4/P5 como roadmap activo; extracción estructurada de datos personales. |
| `docs/roadmaps/districts/extract_gaceta/segmentation_spec.md` | Absorbido | Jerarquía issue/section/item/block; estrategias de segmentación; headers; page boundary; QA: completeness, overlap, size, confidence. | `source_adapters/GACETA.md`, `source_adapters/SOURCE_ADAPTER_TEMPLATE.md` | Timeouts/multithreading como reglas de implementation actual. |
| `docs/roadmaps/districts/extract_gaceta/extraction_schema.md` | Parcial con restricciones | Estructura issue/segment; source evidence; legal references raw; candidate relations unresolved; validation rules. | `source_adapters/GACETA.md` | Campos de personas, partes, residencias, bidders, adjudicatarios como extraction target publicable. |
| `docs/roadmaps/districts/extract_gaceta/FAMILY_COVERAGE_REPORT.md` | Parcial | Lista de familias y métricas como orientación de volumen, no como verdad actual; pipeline flow conceptual. | `source_adapters/GACETA.md` | Claims de cobertura; componentes implementados; números como current facts. |
| `docs/roadmaps/OFFICIAL_SOURCE_ACCESS.md` | Parcial | Regla: fuente oficial y vía institucional primero; data contract; decisiones de licencia; reshape de scope hacia adquisición institucional. | `SOURCE_REGISTRY_CANDIDATES.md` | Lanes semanales, tareas de ejecución, naming note. |
| `docs/roadmaps/EXTRACTION_REFACTOR.md` | Parcial mínimo | Principio de separar lógica de fuente, common pipeline infra y operator interface. | `source_adapters/SOURCE_ADAPTER_TEMPLATE.md` | Todos los nombres de módulos, refactors, “actors” y swaps. |
| `docs/roadmaps/EXTRACT_SCIJ_ROLES.md` | Parcial mínimo | Separación de responsabilidades: discovery, validation, registration, custody, reporting. | `source_adapters/SOURCE_ADAPTER_TEMPLATE.md` | Nombres de roles/personajes, función ownership vieja. |

---

## Documentos legacy no usados para este distill

| Documento legacy | Decisión |
|---|---|
| `docs/AGENTS.md` | Operativo del repo viejo; no se importó. |
| `docs/ARCHITECTURE.md` | Reemplazado por `ARCHITECTURE.md` actual. |
| `docs/DB_ROLES.md` | Implementación vieja; no se importó. |
| `docs/ID_POLICY.md` | Reemplazado por `URI_POLICY.md` actual. |
| `docs/OBSERVABILITY.md` | Operativo viejo; solo ideas generales cubiertas en requirements notes. |
| `docs/REPORTING_AND_LOGS_POLICY.md` | Operativo viejo; no se importó como política. |
| `docs/RUNTIME_ARTIFACT_GOVERNANCE.md` | Puede tener valor operativo futuro, pero queda fuera de este research distill. |
| `docs/TESTING.md` | Operativo viejo; no se importó. |
| `docs/requirements/Plaza_SRS.md` | Reemplazado conceptualmente por docs fundacionales actuales. |
| `docs/traceability/requirements_traceability.md` | Operativo viejo; solo se conservó la idea de trazabilidad. |
| `docs/roadmaps/audit/*` | One-time audit; descartado. |
| `docs/roadmaps/ROADMAP*.md` | Roadmaps obsoletos; descartados como authority. |
| `docs/FAIR_REQUEST_PGR.pdf` | Comunicación externa histórica; no forma parte de research técnico. |

---

## Conclusión de cierre

El contenido legacy útil quedó absorbido en este distill. El resto debe considerarse archivo histórico frío.

Si el equipo necesita saber “qué decía legacy sobre SCIJ, La Gaceta, estándares, fuentes oficiales, RAG, state hub o requirements”, este directorio reemplaza la consulta directa a `olddocs/`.
