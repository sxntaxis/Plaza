# Plaza — Standards Research Notes

**Estado:** memoria de investigación.
**No es normativo.** Las decisiones vigentes viven en `DATA_MODEL.md`, `URI_POLICY.md`, `ACCESS_SURFACES.md`, `QUALITY_AND_VALIDATION.md`, `VERSIONING.md` y `REFERENCES.md`.

---

## Tesis destilada

El research legacy converge en una regla que la nueva Plaza ya adoptó correctamente:

> Plaza debe ser standards-aligned por capas, no standards-driven por ansiedad.

Los estándares no son una colección decorativa. Cada uno debe resolver una responsabilidad específica:

- identidad legal;
- modelo semántico;
- procedencia;
- vocabularios;
- validación;
- catálogo;
- serialización documental;
- consumo por IA;
- publicación web.

Cualquier estándar que no tenga una responsabilidad clara queda fuera o reservado.

---

## Stack activo de Plaza nueva

| Estándar / vocabulario | Estado recomendado | Rol en Plaza | Dónde vive la decisión actual |
|---|---:|---|---|
| **RDF** | Activo | Modelo de grafo canónico como triples. | `DATA_MODEL.md`, `ACCESS_SURFACES.md` |
| **ELI** | Activo, columna principal | Identidad legislativa, FRBR, metadata legal, versiones y relaciones normativas. | `URI_POLICY.md`, `DATA_MODEL.md` |
| **PROV-O** | Activo | Procedencia de entidades, afirmaciones, artefactos y actividades de procesamiento. | `ARCHITECTURE.md`, `DATA_MODEL.md`, `QUALITY_AND_VALIDATION.md` |
| **SKOS** | Activo | Vocabularios controlados: tipos de norma, emisores, estados, descriptores, tipos de subdivisión. | `DATA_MODEL.md`, `REFERENCES.md` |
| **SHACL** | Activo para validación | Restricciones estructurales del grafo antes de publicación y post-snapshot. | `QUALITY_AND_VALIDATION.md`, `DATA_MODEL.md` |
| **DCAT 3** | Activo para catálogo | Catalogar snapshots, distribuciones y servicios de datos. | `ACCESS_SURFACES.md`, `DATA_MODEL.md` |
| **Akoma Ntoso** | Activo como serialización derivada | Export XML documental cuando exista estructura suficiente. No gobierna identidad. | `DATA_MODEL.md`, `ACCESS_SURFACES.md` |
| **schema.org/Legislation** | Activo auxiliar | Interoperabilidad web y motores/herramientas generales. | `DATA_MODEL.md`, `README.md` |
| **Dublin Core Terms** | Activo auxiliar | Metadata bibliográfica general no cubierta suficientemente por ELI. | `DATA_MODEL.md` |
| **ISO 3166 / ISO 639 / ISO 8601** | Activo | Códigos de jurisdicción, idioma y fechas. | `URI_POLICY.md`, `REFERENCES.md` |
| **SemVer** | Activo para ontología/modelo/shapes/políticas | Versionado de contratos semánticos. | `VERSIONING.md` |

---

## Decisiones de arquitectura semántica extraídas

### 1. ELI identifica; Akoma serializa

Legacy research insistía en mirar Akoma Ntoso, pero también advertía que forzar la ingesta a ser Akoma-native demasiado temprano era un riesgo. La Plaza nueva resuelve esto mejor:

- **ELI** gobierna la identidad pública, versiones, FRBR y relaciones normativas.
- **Akoma Ntoso** representa estructura documental XML como export derivado.
- Una norma puede canonicalizarse sin Akoma si cumple ELI/PROV/SKOS/SHACL.
- Akoma no debe introducir identidades públicas alternativas.

### 2. RDF es contrato de publicación, no necesariamente motor operacional

El research legacy recomendaba mantener una operación relacional/raw-first y emitir RDF/JSON-LD/Turtle desde vistas/exportaciones. La nueva Plaza formula esto como capas:

- adquisición, refinamiento y reconciliación son operacionales y mutables;
- canonicalización produce el grafo canónico;
- publicación expone snapshots/API/MCP/DCAT/feeds.

La herramienta de almacenamiento puede cambiar. El contrato semántico no.

### 3. SPARQL es futuro, no MVP

Un endpoint SPARQL público debe esperar a que existan:

- URIs estables;
- ontología estable;
- snapshots validados;
- consumidores reales;
- capacidad operativa para rate limiting y queries costosas.

Mientras tanto, snapshots Turtle/JSON-LD y API REST/MCP dan más valor con menos riesgo.

### 4. ORG es futuro institucional, no scope actual

W3C ORG es la opción natural para instituciones, unidades, cargos y relaciones organizacionales. Pero esa capa no debe entrar antes de que el corpus normativo sea estable.

### 5. Personas no son entidad temprana

Legacy sugería FOAF/schema Person para officeholders. En Plaza nueva esto queda fuertemente restringido:

- no perfilado;
- no biografía;
- no personas privadas;
- no relaciones personales;
- solo posible titularidad oficial de cargos, con actos oficiales, finalidad institucional y gobernanza explícita.

---

## Estándares descartados o pospuestos

| Estándar / enfoque | Estado | Razón |
|---|---:|---|
| **FOAF** | Pospuesto / no activo | Abre la puerta a modelado de personas. Solo considerar si una capa futura de titularidad oficial lo requiere y con justificación legal. |
| **schema.org/Person** | Pospuesto / no activo | Igual que FOAF. No usar para MVP ni demo. |
| **W3C ORG** | Reservado | Correcto para instituciones/cargos, pero no activo hasta que el corpus normativo madure. |
| **LKIF-Core** | No adoptar ahora | Potencialmente interesante para razonamiento legal, pero Plaza no razona ni interpreta. Añade complejidad sin necesidad actual. |
| **ODRL** | No adoptar ahora | Puede servir para políticas de derechos más complejas, pero licenciamiento/base jurídica actual se expresa mejor en docs, DCAT y metadata simple. |
| **OWL profundo / reasoning** | Pospuesto | Útil para ontología formal mínima, no para inferencia pesada. Evitar que Plaza se convierta en proyecto de razonamiento. |
| **Triple store como source of truth** | No adoptar ahora | Riesgo de dual truth o complejidad operacional. El grafo canónico puede publicarse sin que la ingesta dependa de un triple store. |
| **SPARQL público temprano** | Pospuesto | Costoso, difícil de proteger, innecesario para demo/MVP. |
| **Akoma-native ingestion** | No adoptar ahora | Akoma debe ser export documental derivado, no obligación de parser inicial. |

---

## Research fresco requerido antes de implementar detalles

Estas preguntas **sí requieren web refresh** antes de decisiones finales, porque estándares, versiones y mejores prácticas pueden cambiar.

### ELI

- ¿Cuál es la versión vigente de la ontología ELI?
- ¿Cuál es la guía oficial más reciente de implementación ELI?
- ¿Qué convenciones usan países con sistemas jurídicos civilistas para artículos, versiones y consolidaciones?
- ¿Cómo modelan versiones históricas vs versión vigente?
- ¿Qué propiedades ELI son preferibles para `amends`, `repeals`, `corrects`, `cites`, `applies`, `commences`?
- ¿Cómo se representa una implementación ELI no oficial/provisional de una jurisdicción?

### Akoma Ntoso

- ¿Cuál es la versión OASIS vigente y si hay errata/perfiles relevantes?
- ¿Cómo mapear artículos, transitorios, incisos, anexos y reformas costarricenses?
- ¿Cuál es el perfil mínimo para export válido sin sobre-modelar?
- ¿Qué validadores XSD/Schematron están mantenidos?

### SHACL

- ¿Cuál es el enfoque más simple para publicar `shapes.ttl` versionado?
- ¿Qué debe validar SHACL y qué debe quedar en validación procedimental?
- ¿Cómo representar severidad: violation, warning, info?
- ¿Cómo asociar SHACL version con ontology/model version?

### DCAT

- ¿Cómo describir correctamente snapshots como `dcat:Dataset` y `dcat:Distribution`?
- ¿Cómo representar API REST y MCP como `dcat:DataService`?
- ¿Cómo representar hash, snapshot chain, licencia, publisher y contact point?
- ¿Existe perfil regional o latinoamericano relevante que convenga seguir?

### schema.org

- ¿Cuál es el estado actual de `schema:Legislation` y propiedades asociadas?
- ¿Qué conviene exponer en HTML con RDFa/JSON-LD para buscadores?
- ¿Dónde usar schema.org sin duplicar semántica ELI?

### MCP

- ¿Cuál es la versión/propuesta vigente del Model Context Protocol?
- ¿Qué forma de resource/tool conviene para retrieval por URI, búsqueda semántica y navegación temporal?
- ¿Cómo forzar citas verificables desde el servidor?

---

## Mapa de responsabilidades por capa

| Capa Plaza | Responsabilidad | Estándares relevantes | No debe hacer |
|---|---|---|---|
| Adquisición | Preservar artefactos crudos y contexto de acceso. | PROV-O conceptual, hashes, metadata interna. | Interpretar, asignar URI pública, resolver conflictos. |
| Refinamiento | Convertir artefactos de fuente en datos estructurados de fuente. | PROV-O, vocabularios preliminares. | Hacer claims canónicos sin evidencia. |
| Reconciliación | Consolidar evidencia, detectar conflictos, producir candidatos canónicos. | PROV-O, SKOS, criterios internos. | Esconder conflictos o sobreafirmar. |
| Canonicalización | Emitir grafo RDF público con URIs permanentes. | RDF, ELI, PROV-O, SKOS, Dublin Core, schema.org. | Publicar entidades sin criterios de calidad. |
| Validación | Verificar forma y criterios antes/después de snapshot. | SHACL, XML validators/Schematron para Akoma. | Confundir validez estructural con verdad jurídica. |
| Publicación | Exponer snapshots, API, MCP, DCAT, feeds y HTML. | JSON-LD, Turtle, Akoma, DCAT, Atom, RDFa. | Crear apps consumer-facing o endpoints ad hoc para un consumidor. |

---

## Anti-goals que sobreviven del research legacy

1. No reemplazar la arquitectura operacional por RDF antes de tiempo.
2. No crear un segundo modelo de verdad semántico separado del estado canonicalizado.
3. No publicar URIs si la evidencia de identidad está incompleta.
4. No meter SPARQL público por prestigio técnico.
5. No usar estándares que acerquen el proyecto a perfilado de personas.
6. No convertir Akoma Ntoso en identidad canónica.
7. No inventar vocabulario Plaza donde ELI/SKOS/PROV/DCAT ya cubren el caso.
8. No abrir una capa institucional antes de que el corpus normativo sea fiable.
9. No usar IA/RAG como excusa para interpretar derecho dentro del corpus.
10. No bloquear MVP/demo esperando una ontología perfecta.

---

## Salida mínima recomendada para demo/MVP

Sin hacer web refresh completo aún, el stack mínimo razonable es:

1. URI ELI/Plaza para norma.
2. URI ELI/Plaza para versión.
3. URI ELI/Plaza para artículo.
4. JSON-LD mínimo de `LegalResource` y `LegalExpression`.
5. Turtle snapshot mínimo.
6. PROV-O por recurso: fuente, URL, timestamp, hash, parser/activity.
7. SKOS mínimo: tipo de norma, emisor, estado de vigencia, tipo de subdivisión.
8. SHACL mínimo para LegalResource, LegalExpression, Subdivision y relación.
9. DCAT mínimo para describir el snapshot.
10. MCP/retrieval solo si puede devolver URIs verificables y no interpretaciones.

---

## Pregunta de control antes de adoptar cualquier estándar nuevo

Antes de agregar un estándar, responder:

1. ¿Qué responsabilidad concreta resuelve?
2. ¿Ya la resuelve un estándar activo?
3. ¿Aumenta riesgo legal, privacidad o scope creep?
4. ¿Puede implementarse como export derivado en vez de core?
5. ¿Tiene validadores o consumidores reales?
6. ¿Puede explicarse en una tabla de `DATA_MODEL.md` sin romper la arquitectura?

Si no pasa estas preguntas, no entra.
