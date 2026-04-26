# Plaza — Standards Implementation Profile

> **Documento:** `STANDARDS_IMPLEMENTATION_PROFILE.md`
> **Proyecto:** Plaza (infraestructura costarricense de datos jurídicos verificables)
> **Idioma:** Español
> **Estado:** Perfil de implementación de estándares — versión inicial para Demo/MVP y hoja de ruta para producción
> **Patch aplicado:** 2026-04-25 — incorpora auditoría quirúrgica ELI, adopta `https://demo.plaza.cr/eli/...` para Demo y corrige relación ley–decreto a `eli:based_on` / `eli:basis_for`
> **Fecha de referencia normativa:** abril de 2026

---

## 0. Executive decision summary

Plaza adopta una pila de estándares en la que **ELI V1.5** ([Publications Office](https://op.europa.eu/en/web/eu-vocabularies/eli)) gobierna la identidad jurídica y la estructura FRBR (Work / Expression / Manifestation, expresada en ELI como `eli:LegalResource` / `eli:LegalExpression` / `eli:Format`, ver [ELI Technical Guide](https://op.europa.eu/documents/2050822/2138819/ELI+-+A+Technical+Implementation+Guide.pdf/)); **RDF 1.1** es el modelo de datos canónico y **Turtle 1.1** ([W3C Recommendation 2014](https://www.w3.org/TR/turtle/)) es la serialización fuente de verdad para Demo/MVP; **PROV-O** ([W3C Recommendation 2013-04-30](https://www.w3.org/TR/prov-o/)) registra la procedencia de toda entidad canónica; **SKOS** ([W3C Recommendation 2009](https://www.w3.org/TR/skos-reference/)) modela vocabularios controlados; **SHACL Core 2017** ([W3C Recommendation](https://www.w3.org/TR/shacl/)) valida estructura antes de publicar; **DCAT 3** ([W3C Recommendation 22 August 2024](https://www.w3.org/TR/vocab-dcat-3/)) describe el catálogo de snapshots y servicios; **Akoma Ntoso 1.0** ([OASIS Standard, 29 August 2018](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html)) es **serialización XML derivada**, no identidad; **schema.org/Legislation** ([schema.org](https://schema.org/Legislation)) es interoperabilidad web auxiliar; **Dublin Core Terms** ([DCMI](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)) aporta metadatos bibliográficos auxiliares.

**Regla maestra:** *ELI identifica; Akoma Ntoso serializa; PROV-O explica de dónde viene cada afirmación; SHACL valida estructura, no verdad jurídica; DCAT publica snapshots; SKOS organiza vocabularios.*

**Demo/MVP:** 4 recursos legales reales, evidencia SCIJ ([PGR/SCIJ](https://pgrweb.go.cr/scij/ayuda/historia.aspx)) sin reconciliación con La Gaceta, Turtle como única serialización persistida, SHACL Core 2017 mínimo, MCP como única superficie de acceso, y URIs `https://demo.plaza.cr/eli/...` en lugar de `https://plaza.cr/eli/...`. No hay endpoint SPARQL público, ni modelado de personas, ni interpretación jurídica. La relación demostrativa ley–decreto debe modelarse por defecto con `eli:based_on` / `eli:basis_for`, no con `eli:applies`.

**Versionado:** ontología, modelo y SHACL comparten **SemVer 2.0.0** ([semver.org](https://semver.org/)); los snapshots usan identificadores calendáricos.

---

## 1. Sources and methodology

Este perfil se construyó priorizando fuentes oficiales y primarias, contrastando versión, estado normativo y trampas conocidas:

| Estándar | Fuente autoritativa consultada | Versión vigente verificada |
|---|---|---|
| ELI ontología | [op.europa.eu/en/web/eu-vocabularies/eli](https://op.europa.eu/en/web/eu-vocabularies/eli), [data.europa.eu/eli/ontology](https://data.europa.eu/eli/ontology) | **ELI Ontology V1.5 LATEST** según Publications Office / EU Vocabularies. Plaza debe fijar `plaza:eliOntologyVersion "1.5"` solo después de descargar y revisar el OWL/RDF oficial usado por el build. |
| ELI URI template | [eur-lex.europa.eu/eli-register/about.html](https://eur-lex.europa.eu/eli-register/about.html), [eli register about](https://eur-lex.europa.eu/eli-register/about.html) | Plantilla de componentes RFC 6570: `/eli/{jurisdiction}/{agent}/{sub-agent}/{year}/{month}/{day}/{type}/{natural identifier}/{level 1…}/{point in time}/{version}/{language}` ([EUR-Lex 52012XG1026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52012XG1026(01))) |
| RDF 1.1 / Turtle 1.1 | [w3.org/TR/turtle](https://www.w3.org/TR/turtle/) (1.1, REC 2014), [w3.org/TR/rdf12-turtle](https://www.w3.org/TR/rdf12-turtle/) (1.2, tracked) | Plaza implementa **RDF 1.1 / Turtle 1.1** como contrato de Demo/MVP. RDF/Turtle 1.2 se monitorea, pero ninguna feature 1.2 es requisito ni debe aparecer en snapshots Demo/MVP. |
| JSON-LD 1.1 | [w3.org/TR/json-ld11](https://www.w3.org/TR/json-ld11/) | W3C Recommendation 16 julio 2020 ([W3C News](https://www.w3.org/news/2020/json-ld-1-1-specifications-are-w3c-recommendations/)) |
| PROV-O | [w3.org/TR/prov-o](https://www.w3.org/TR/prov-o/) | W3C Recommendation 30 abril 2013 |
| SKOS | [w3.org/TR/skos-reference](https://www.w3.org/TR/skos-reference/) | W3C Recommendation 18 agosto 2009 |
| SHACL | [w3.org/TR/shacl](https://www.w3.org/TR/shacl/) (Core, REC 2017) y [w3.org/TR/shacl12-core](https://www.w3.org/TR/shacl12-core/) (1.2, tracked) | Plaza usa **SHACL Core 2017** para Demo/MVP. SHACL 1.2 se monitorea, pero no es contrato de validación hasta que sea estable y tenga soporte robusto de herramientas. |
| DCAT 3 | [w3.org/TR/vocab-dcat-3](https://www.w3.org/TR/vocab-dcat-3/) | W3C Recommendation 22 agosto 2024 |
| Akoma Ntoso | [docs.oasis-open.org/legaldocml/akn-core/v1.0](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html) | OASIS Standard 1.0, 29 agosto 2018 |
| schema.org/Legislation | [schema.org/Legislation](https://schema.org/Legislation) | Tipo `pending`/`new` derivado de la ontología ELI |
| DCMI Terms | [dublincore.org](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | DCMI Metadata Terms (mantenidos por DCMI) |
| ISO 3166-1 | [iso.org](https://www.iso.org/obp/ui/#iso:code:3166:CR) | Costa Rica = `CR` (alpha-2), `CRI` (alpha-3) |
| ISO 639 | [SIL](https://iso639-3.sil.org/code/spa), [LOC](https://www.loc.gov/standards/iso639-2/php/code_list.php) | Español: `es` (639-1), `spa` (639-2/3) |
| ISO 8601 | [iso.org/iso-8601](https://www.iso.org/iso-8601-date-and-time-format.html) | ISO 8601-1:2019 + Amd 2022 |
| SemVer | [semver.org](https://semver.org/) | 2.0.0 |
| SPDX (checksums DCAT) | DCAT 3 §spdx:Checksum ([w3.org/TR/vocab-dcat-3](https://www.w3.org/TR/vocab-dcat-3/)) | Recomendado para `spdx:checksum` en distribuciones |

**Metodología.** Cada decisión se etiqueta como (a) **requisito de estándar oficial**, (b) **decisión de proyecto Plaza** ya tomada (ver Critical Context del encargo), (c) **recomendación** del autor, o (d) **pregunta abierta**. La incertidumbre se marca explícitamente. Se evita inventar afirmaciones jurídicas sustantivas sobre el derecho costarricense; los ejemplos con identificadores de normas costarricenses se marcan como ilustrativos.

---

## 2. Standards stack by responsibility

| Capa | Responsabilidad | Estándar | Rol en Plaza | Rol que NO debe jugar |
|---|---|---|---|---|
| Identidad jurídica | Asignar URIs estables a cada Work/Expression/Format y a sus subdivisiones | **ELI** | Único gobernante de la identidad pública; FRBR-like | No es un esquema XML, no controla orden ni cantidad de componentes, no impone modelo de personas |
| Modelo de datos | Grafo de afirmaciones | **RDF 1.1** | Modelo abstracto canónico ([W3C](https://www.w3.org/TR/turtle/)) | No es un formato; no se confunde con su serialización |
| Serialización fuente-de-verdad | Texto legible y diff-friendly | **Turtle 1.1** | Persistencia primaria del grafo Plaza | No serializa OWL ni reglas; no es el contrato de API |
| Serialización web | Intercambio JSON-friendly | **JSON-LD 1.1** | Interoperabilidad futura con clientes web/MCP | No oculta URIs ni provenance |
| Serialización HTML embebida | Marcado en páginas oficiales (futuro lejano) | **RDFa** ([W3C, recomendado por ELI](https://eur-lex.europa.eu/eli-register/about.html)) | Pillar 3 de ELI cuando exista publicación HTML | No es prerrequisito ni para Demo ni para MVP |
| Procedencia | Trazabilidad a artefactos preservados | **PROV-O** | Cada `eli:LegalResource`, `eli:LegalExpression`, relación normativa y vocabulario es derivado por una `prov:Activity` desde `prov:Entity` (artefacto fuente) | No reemplaza la verificación legal; no contiene texto íntegro |
| Vocabularios controlados | Tipos de norma, emisores, estado de vigencia, subdivisiones | **SKOS** | `skos:ConceptScheme` versionado para cada eje | No expresa lógica jurídica; no infiere consecuencias |
| Validación estructural | Forma del grafo antes de publicar | **SHACL Core 2017** ([W3C](https://www.w3.org/TR/shacl/)) | Garantiza forma, cardinalidad, datatype, coherencia mínima | **No** valida verdad jurídica, **no** sustituye revisión humana |
| Catálogo y distribución | Snapshots, formatos, servicios, procedencia agregada | **DCAT 3** | Descripción de cada snapshot como `dcat:Dataset` con `dcat:Distribution` (Turtle, JSON-LD, SQLite, AKN), `dcat:DataService` (REST/MCP) | No reemplaza el grafo canónico; es metadatos del paquete |
| Serialización XML jurídica | Intercambio con sistemas Akoma-nativos | **Akoma Ntoso 1.0** | Export derivado, no governing | **No** ingresa como identidad ni como fuente; **no** bloquea Demo/MVP |
| Interop. web auxiliar | Buscadores, embeds | **schema.org/Legislation** | Marcado complementario en HTML público | No reemplaza ELI; no es el modelo canónico |
| Metadatos bibliográficos | Título, fecha, idioma, editor | **Dublin Core Terms** | Auxiliar; ELI ya re-declara muchos como subpropiedades ([data.europa.eu/eli/ontology](https://data.europa.eu/eli/ontology)) | No duplicar lo que ELI ya define |
| Códigos | País, idioma, fechas | **ISO 3166-1, ISO 639, ISO 8601** | `CR`, `es`/`spa`, `YYYY-MM-DD` | — |
| Versionado de ontología y SHACL | Compatibilidad y rupturas | **SemVer 2.0.0** | `MAJOR.MINOR.PATCH` aplicado a `ontology/plaza.ttl` y `ontology/shapes.ttl` | No se aplica a snapshots (calendar IDs) |

### 2.1 Estándares NO recomendados ahora

| Estándar | Por qué no | Cuándo reconsiderar |
|---|---|---|
| **FOAF** | Plaza no modela personas ni titulares de cargo en alcance actual | Solo si se incorporan emisores como agentes con biografía |
| **schema.org/Person** | Mismo motivo: scope explícitamente excluido | — |
| **W3C ORG** ontology | Modelaría jerarquías de órganos emisores; sobrepasa alcance | Si se modelan emisores con estructura interna |
| **LKIF** (Legal Knowledge Interchange Format) | Pesado, orientado a razonamiento jurídico; Plaza explícitamente no hace interpretación | Solo si Plaza acepta razonamiento legal en alcance |
| **ODRL** (políticas/derechos) | Plaza no modela licencias ejecutables sobre normas | Si se cataloga uso de datos derivados |
| **OWL razonamiento pesado** (DL, reglas, SWRL) | RDFS+SKOS+SHACL es suficiente; OWL DL agrega coste y trampas (open-world, dominios/rangos) | Si surge necesidad real de inferencia; Plaza usaría `owl:Class`/`owl:ObjectProperty` solo declarativamente |
| **Endpoint SPARQL público** | Costoso, denegación de servicio, expectativas legales | Tras MVP, con plan de infra y SLAs |
| **Akoma-native ingestion** | Convertiría AKN en identidad; rompe regla maestra | Nunca como capa canónica; sí como import diagnóstico |

---

## 3. ELI implementation profile for Costa Rican norms

### 3.1 Estructura ELI esencial

ELI extiende FRBR/FRBRoo con tres clases ([Springer / linked legal data landscape](https://link.springer.com/article/10.1007/s10506-021-09282-8), [data.europa.eu/eli/ontology](https://data.europa.eu/eli/ontology)):

- `eli:LegalResource` — la obra abstracta (e.g. *"Ley 9849"* sin idioma ni formato).
- `eli:LegalExpression` — realización en idioma + versión temporal (e.g. *"Ley 9849, versión consolidada 2021-08-01, en español"*).
- `eli:Format` — manifestación/formato de una expresión (e.g. PDF firmado, HTML, Turtle). No debe confundirse con `dcat:Distribution`: ELI describe el formato jurídico/documental; DCAT describe archivos o servicios publicados.
- `eli:LegalResourceSubdivision` — añadida en v1.1, modela artículo, transitorio, anexo, etc. ([data.europa.eu/eli/ontology](https://data.europa.eu/eli/ontology)).

Plaza reutiliza la jerarquía FRBR de ELI mediante las propiedades `eli:realizes` / `eli:is_realized_by` y `eli:embodies` / `eli:is_embodied_by`, heredadas de Metalex/FRBR.

### 3.2 Propiedades ELI mínimas adoptadas por Plaza

| Propiedad ELI | Aplicada a | Obligatoria para Demo | Obligatoria para producción | Notas |
|---|---|---|---|---|
| `eli:jurisdiction` | LegalResource | Sí | Sí | Valor: SKOS concept con `skos:notation "CR"` ([ISO 3166-1](https://www.iso.org/obp/ui/#iso:code:3166:CR)). |
| `eli:type_document` | LegalResource | Sí | Sí | SKOS concept del scheme `plazav:tipo-norma`. |
| `eli:passed_by` | LegalResource | Recomendada | Sí | En Plaza v0 debe apuntar a emisor institucional, no a persona física. Puede ser SKOS mientras no exista capa institucional ORG. |
| `eli:number` | LegalResource | Sí | Sí | Literal string, no numérico; preserva ceros, sufijos, bis, ter, prefijos y signos oficiales. |
| `eli:date_document` | LegalResource | Sí | Sí | Fecha de emisión/adopción/firma de la norma. No es fecha de publicación ni de vigencia. |
| `eli:first_date_entry_in_force` | LegalResource o LegalExpression | Recomendada | Sí | Fecha verificable de entrada en vigencia. Si Plaza usa `/version/{fecha}` como fecha de vigencia, esta propiedad debe aparecer en la `LegalExpression`. |
| `eli:date_no_longer_in_force` | LegalResource o LegalExpression | No (Demo) | Recomendada | Solo si hay evidencia de derogación, expiración o pérdida de vigencia. No inferir. |
| `eli:date_publication` | LegalResource / Format / evento de publicación | No (Demo) | Recomendada | Fecha de publicación. No sustituye `first_date_entry_in_force` ni `version_date`. |
| `eli:date_applicability` | LegalResource o LegalExpression | No | Opcional | Útil cuando una norma entra en vigor en una fecha pero aplica desde otra. |
| `eli:version` | LegalExpression | Recomendada | Sí | Etiqueta o tipo de versión: original, consolidada, revisada, etc. Puede usar SKOS. |
| `eli:version_date` | LegalExpression | No (Demo) | Recomendada | Fecha de versión/consolidación o point-in-time. No equivale automáticamente a entrada en vigencia. |
| `eli:in_force` | LegalResource o LegalExpression | Sí | Sí | SKOS concept local mapeado a la tabla ELI de vigencia cuando aplique. |
| `eli:title` | LegalExpression | Sí | Sí | Literal con `@es`. |
| `eli:title_short` | LegalExpression | Recomendada | Recomendada | Opcional. |
| `eli:title_alternative` | LegalExpression | Opcional | Opcional | Para denominaciones alternativas o populares, sin interpretación jurídica. |
| `eli:language` | LegalExpression | Sí | Sí | Preferir URI/SKOS de idioma con notación `spa`; literal `"es"` solo como fallback de Demo. |
| `eli:realizes` / `eli:is_realized_by` | Resource ↔ Expression | Sí | Sí | Backbone FRBR. |
| `eli:embodies` / `eli:is_embodied_by` | Expression ↔ Format | No (Demo) | Sí cuando se modelen formatos | Diferido si Demo no modela archivos como `eli:Format`. |
| `eli:has_part` / `eli:is_part_of` | LegalResource ↔ Subdivision | No (Demo) | Sí para artículos/transitorios/anexos | Relación preferente para inclusión estructural norma → artículo/transitorio/anexo. |
| `eli:has_member` / `eli:is_member_of` | Resource ↔ miembro conceptual/temporal | No (Demo) | Opcional | No usar automáticamente para artículos. Reservar para membresía conceptual/temporal cuando la semántica lo justifique. |
| `eli:type_subdivision` | LegalResourceSubdivision | No (Demo) | Sí para subdivisiones | Propiedad ELI primaria para artículo, transitorio, anexo, inciso, etc. `plaza:tipoSubdivision` no debe reemplazarla. |
| `eli:has_annex` / `eli:is_annex_of` | LegalResource ↔ anexo | No | Opcional | Útil cuando el anexo requiera relación específica. |
| `eli:cites` / `eli:cited_by` | LegalResource o Expression | Recomendada | Sí | Cita directa. No usar para concordancia temática débil. |
| `eli:refers_to` / `eli:is_referred_to_by` | LegalResource o Expression | No | Recomendada | Referencia general más débil que `cites`; útil para concordancias no normativas o referencias no resueltas. |
| `eli:amends` / `eli:amended_by` | LegalResource o Subdivision | Recomendada | Sí | Reforma/modificación con efecto jurídico. Cuidar dirección. |
| `eli:repeals` / `eli:repealed_by` | LegalResource o Subdivision | Recomendada | Sí | Derogación total o parcial; para parcial, preferir nivel de subdivisión si hay evidencia. |
| `eli:changes` / `eli:changed_by` | LegalResource o Subdivision | Opcional | Recomendada | Fallback para afectaciones SCIJ ambiguas cuando no se pueda elegir `amends`, `repeals` o `corrects`. |
| `eli:corrects` / `eli:corrected_by` | LegalResource | Opcional | Sí | Fe de erratas/correcciones sin afirmar cambio jurídico material. |
| `eli:based_on` / `eli:basis_for` | LegalResource | Sí para relación ley–decreto Demo si hay evidencia | Sí | Relación preferente para decreto/reglamento fundado en ley habilitante o desarrollada. Sustituye el uso default incorrecto de `eli:applies`. |
| `eli:applies` / `eli:applied_by` | LegalResource | No por defecto | Opcional | Relación informativa/de conformidad. No usar como relación primaria ley–decreto salvo evidencia específica. |
| `eli:commences` / `eli:commenced_by` | LegalResource | No | Opcional | Para norma que pone en vigencia otra, si la fuente lo afirma. |
| `eli:consolidates` / `eli:consolidated_by` | LegalResource | No (Demo) | Recomendada | Para modelar consolidaciones editoriales/oficiales cuando se incorpore esa capa. |
| `eli:published_in` | LegalResource / Format | No (Demo) | Recomendada post-Gaceta | No fijar como único modelo de publicación hasta decidir si La Gaceta se modela como literal, `Format`, `SourceArtifact` o evento de publicación. |
| `eli:published_in_format` | Format | No | Opcional post-Gaceta | Candidato si la edición de La Gaceta tiene URI propia. |
| `eli:media_type` | Format | No | Recomendada para formatos publicados | MIME/IANA técnico: `text/turtle`, `application/ld+json`, PDF, Akoma XML. |
| `eli:legal_value` | Format | No | Recomendada | Distingue valor jurídico/documental de formatos: oficial, no oficial, consolidado, informativo, etc. |
| `eli:id_local` | LegalResource o Expression | No | Opcional restringida | No usar para `nValor` SCIJ. Los IDs técnicos de fuente viven en `plaza:SourceArtifact`. Si se usa, debe ser identificador jurídico local normalizado, no ID operacional. |

### 3.3 Mapeo de tipos costarricenses a ELI (ilustrativo)

| Tipo costarricense | `eli:type_document` (SKOS notation) | Emisor típico | Comentario |
|---|---|---|---|
| Constitución Política | `constitucion` | Asamblea Nacional Constituyente | Una sola, expresiones consolidadas múltiples |
| Ley ordinaria | `ley` | Asamblea Legislativa | — |
| Ley orgánica (si Plaza decide diferenciarla) | `ley_organica` | Asamblea Legislativa | **Pregunta abierta:** ¿Plaza distingue `ley_organica` o sigue al SCIJ? |
| Decreto ejecutivo | `decreto_ejecutivo` | Poder Ejecutivo | — |
| Reglamento | `reglamento` | Poder Ejecutivo / órgano | Si desarrolla o se funda en una ley, usar `eli:based_on` hacia la ley y `eli:basis_for` como inverso. `eli:applies` queda solo para conformidad informativa. |
| Norma municipal | `reglamento_municipal` o `acuerdo_municipal` | Concejo Municipal | El `agent` en URI puede capturar la municipalidad |
| Acuerdo / resolución | `acuerdo` / `resolucion` | Variable | Caso por caso |
| Transitorio | (no es tipo, es subdivisión) | — | `eli:LegalResourceSubdivision` con `eli:type_subdivision = plazav:tipo-subdivision/transitorio` |
| Anexo | (subdivisión) | — | `eli:LegalResourceSubdivision` con `eli:type_subdivision = plazav:tipo-subdivision/anexo` |

### 3.4 Cómo modelar cada caso

- **Ley ordinaria:** un `eli:LegalResource` con `eli:type_document = plazav:tipo-norma/ley`; una o varias `eli:LegalExpression` para versiones originales, vigentes o consolidadas.
- **Versión de la norma:** cada `eli:LegalExpression` representa una versión textual/temporal. Si la fecha en la URI `/version/{fecha}` representa entrada en vigencia, debe expresarse con `eli:first_date_entry_in_force`. `eli:version_date` puede usarse como fecha de versión/consolidación, pero no debe confundirse con publicación ni vigencia.
- **Publicación:** `eli:date_publication` y, post-Demo, `eli:published_in` / `eli:published_in_format` se reservan para eventos o formatos de publicación, especialmente La Gaceta. SCIJ puede aportar `publication_hint`, pero no publicación oficial verificada por sí solo.
- **Artículo:** `eli:LegalResourceSubdivision` enlazado estructuralmente al recurso padre mediante `eli:has_part` / `eli:is_part_of`, con `eli:type_subdivision` apuntando al concepto SKOS `plazav:tipo-subdivision/articulo`.
- **Versión de artículo:** una versión de artículo puede ser una `eli:LegalExpression` que `eli:realizes` la `eli:LegalResourceSubdivision`. La clase `plaza:ArticleVersion` es opcional como convenience class para validación, no requisito semántico.
- **Transitorio / anexo:** `eli:LegalResourceSubdivision` con `eli:type_subdivision`. Para anexos, evaluar `eli:has_annex` / `eli:is_annex_of` cuando se necesite semántica específica.
- **Derogación:** `:normaA eli:repeals :normaB`.
- **Modificación:** `:normaA eli:amends :normaB`; usar `eli:changes` solo cuando la afectación sea real pero su tipo específico no esté resuelto.
- **Corrección/errata:** `:normaA eli:corrects :normaB`.
- **Cita directa:** `:normaA eli:cites :normaB`.
- **Referencia débil / concordancia no resuelta:** `:normaA eli:refers_to :normaB` o una extensión `plaza:` documentada si la relación no alcanza cita directa.
- **Decreto o reglamento fundado en una ley:** `:decreto eli:based_on :ley`; inverso opcional `:ley eli:basis_for :decreto`.
- **Conformidad informativa:** `eli:applies` puede usarse solo cuando la fuente o el caso indiquen una relación informativa/de aplicación, no como default para toda reglamentación.

### 3.5 Regla maestra: **ELI identifica; Akoma Ntoso serializa**

ELI gobierna la URI canónica, los metadatos y las relaciones normativas, y se expresa en RDF (Turtle/JSON-LD/RDFa). Akoma Ntoso ([OASIS Standard 1.0](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html)) es un esquema XML para representar la *estructura interna* del texto legal (artículos, párrafos, citas inline). En Plaza, AKN se genera a posteriori desde el grafo canónico cuando exista necesidad de intercambio; nunca al revés. Esto evita el riesgo —observado en otras jurisdicciones— de que el ciclo editorial XML termine dictando la identidad pública.

---

## 4. URI and identity profile

### 4.1 Patrón de URI público (decisión Plaza)

```
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/version/{fecha}
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/articulo/{articulo}
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/articulo/{articulo}/version/{fecha}
```

### 4.2 Evaluación frente al template ELI de referencia

ELI define [una plantilla recomendada](https://eur-lex.europa.eu/eli-register/about.html) (RFC 6570): `/eli/{jurisdiction}/{agent}/{sub-agent}/{year}/{month}/{day}/{type}/{natural identifier}/{level 1…}/{point in time}/{version}/{language}`. **Todos los componentes son opcionales y el orden no está pre-fijado** ([ELI Wikipedia](https://en.wikipedia.org/wiki/European_Legislation_Identifier), [BOE-Spain implementation](https://www.boe.es/legislacion/eli.php?lang=en)). Cada Estado define su URI propia y la documenta vía URI Template.

| Componente Plaza | Componente ELI | Conformidad |
|---|---|---|
| `cr` | `{jurisdiction}` (ISO 3166-1 alpha-2 minúscula) | ✅ Conforme. Ej. España usa `es`, EU usa `eu` |
| `{emisor}` | `{agent}` | ✅ Conforme. Equivalente a `agent` (ej. `bce` para BCE en Italia) |
| `{año}` | `{year}` | ✅ Conforme |
| `{tipo}` | `{type}` | ✅ Conforme |
| `{número}` | `{natural identifier}` | ✅ Conforme |
| `version/{fecha}` | `{point in time}` | ✅ Conforme. ELI permite la fecha como point-in-time |
| `articulo/{articulo}` | `{level 1…}` (subdivisión) | ✅ Conforme. EUR-Lex usa `art_2`; Plaza usa `articulo/2`, también válido |
| `articulo/{articulo}/version/{fecha}` | combinación level + point in time | ✅ Conforme |
| Sin `{language}` ni `{format}` | Componentes opcionales | ⚠️ **Recomendación**: Plaza puede añadirlos en el futuro (`/es`, `/turtle`) cuando exista contenido multilingüe o multiformato |

**Recomendación del autor:** el patrón Plaza es sólido y ELI-conforme. **No se requiere modificación.** Sí se recomienda:

1. **Documentar el URI Template formalmente** (RFC 6570) en `ontology/uri-template.md` para satisfacer Pillar 1 de ELI.
2. **Reservar** el slot `/{idioma}` y `/{formato}` para el momento en que Plaza necesite expresiones multilingües o serializaciones múltiples por URI.
3. **No** introducir el componente `{day}/{month}` separados; mantener `{año}` como unidad y la fecha completa solo en `/version/{fecha}` para legibilidad.
4. **Trailing slash:** prohibirlo. Las URIs Plaza son sin slash final.

### 4.3 URIs de Demo

Para Demo se usa el subdominio resoluble `https://demo.plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}[...]`. Estas URIs:

- Pueden ser inspeccionables por herramientas RDF/HTTP, pero **no son URIs públicas canónicas de producción**.
- Deben ser **mecánicamente convertibles** a `https://plaza.cr/eli/...` mediante una función pura `demoToPublic(u)` documentada que sustituye host `demo.plaza.cr` por `plaza.cr`.
- Mantienen exactamente la misma jerarquía y semántica que las públicas (un Demo válido debe poder migrarse renombrando el host).

### 4.4 Identidad operativa vs. identidad canónica

La identidad operativa SCIJ (`nValor1:nValor2:nValor3`, ver [PGR/SCIJ](http://www.pgrweb.go.cr/scij/busqueda/normativa/normas/nrm_texto_completo.aspx?nvalor1=1&nvalor2=95992&nvalor3=128325)) **nunca** debe usarse como sujeto de tripletas canónicas Plaza. Se modela como **evidencia** vía `prov:Entity` con `dcterms:identifier` y un literal `plaza:scijLocalId "1:95992:128325"`. Esto es un anti-patrón crítico (ver §16 R-01).

---

## 5. Minimal RDF/Turtle profile

### 5.1 Prefijos canónicos

```turtle
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms:<http://purl.org/dc/terms/> .
@prefix prov:   <http://www.w3.org/ns/prov#> .
@prefix sh:     <http://www.w3.org/ns/shacl#> .
@prefix dcat:   <http://www.w3.org/ns/dcat#> .
@prefix spdx:   <http://spdx.org/rdf/terms#> .
@prefix schema: <https://schema.org/> .
@prefix eli:    <http://data.europa.eu/eli/ontology#> .
@prefix plaza:  <https://plaza.cr/ontology#> .
@prefix plazav: <https://plaza.cr/vocab/> .
```

### 5.2 Clases nucleares

| Clase | Tipo | Uso |
|---|---|---|
| `eli:LegalResource` | reutilizada | Norma abstracta |
| `eli:LegalExpression` | reutilizada | Versión idiomática-temporal de la norma |
| `eli:Format` | reutilizada | Encarnación |
| `eli:LegalResourceSubdivision` | reutilizada | Artículo, transitorio, anexo |
| `plaza:ArticleVersion` ⊑ `eli:LegalExpression` | extensión Plaza opcional | Convenience class para validar versiones de artículos. No es requisito semántico: basta una `eli:LegalExpression` que realiza una `eli:LegalResourceSubdivision`. |
| `plaza:Snapshot` ⊑ `dcat:Dataset` | extensión Plaza | Foto del corpus en un instante |
| `plaza:SourceArtifact` ⊑ `prov:Entity` | extensión Plaza | Evidencia preservada (HTML, PDF, blob SCIJ) |
| `plaza:AcquisitionActivity` ⊑ `prov:Activity` | extensión Plaza | Captura desde fuente |
| `plaza:RefinementActivity` ⊑ `prov:Activity` | extensión Plaza | Limpieza/normalización |
| `plaza:CanonicalizationActivity` ⊑ `prov:Activity` | extensión Plaza | Producción del Turtle canónico |
| `plaza:NormativeRelation` ⊑ `prov:Entity` | extensión Plaza (opcional) | Reificación de relación cuando se necesita confianza/evidencia |
| `plaza:DemoStatusMarker` | extensión Plaza | Marca de limitación Demo |

### 5.3 Propiedades Plaza propias (mínimas)

| Propiedad | Dominio | Rango | Uso |
|---|---|---|---|
| `plaza:scijLocalId` | `plaza:SourceArtifact` | `xsd:string` | Identificador operacional SCIJ `nValor1:nValor2:nValor3`; nunca sujeto ni identificador canónico Plaza. |
| `plaza:demoOnly` | cualquier sujeto | `xsd:boolean` | Marca contenido Demo |
| `plaza:demoLimitations` | sujeto Demo | `xsd:string` (multi-valued, `@es`) | Texto legible |
| `plaza:relationConfidence` | `plaza:NormativeRelation` | `skos:Concept` | `alta`, `media`, `requiere_revision` |
| `plaza:ontologyVersion` | grafo (vía `dcat:Dataset`) | `xsd:string` | SemVer de la ontología que produjo el grafo |

### 5.4 Obligatorias / opcionales / prohibidas (Demo/MVP)

**Obligatorias en cada `eli:LegalResource`:**
`rdf:type`, `eli:jurisdiction`, `eli:type_document`, `eli:number`, `eli:date_document`, `eli:in_force`, `eli:is_realized_by` (al menos una), `prov:wasGeneratedBy`, `prov:wasDerivedFrom`.

**Obligatorias en cada `eli:LegalExpression`:**
`rdf:type`, `eli:realizes`, `eli:language`, `eli:title`, `prov:wasGeneratedBy`.

**Opcionales útiles desde Demo:**
`eli:title_short`, `eli:passed_by`, `eli:first_date_entry_in_force`, `eli:cites`, `eli:refers_to`, `eli:amends`, `eli:repeals`, `eli:based_on`, `eli:basis_for`.

**Prohibidas en Demo (scope):** `foaf:*`, `schema:author` con persona física, `org:*`, propiedades que requieran modelado de personas u oficios, propiedades de licencia ejecutable (ODRL).

**Prohibidas siempre en Plaza:** propiedades que afirmen interpretación jurídica (`plaza:significa`, `plaza:contradice`); el proyecto explícitamente no hace interpretación.

---

## 6. Minimal JSON-LD profile

Aunque Demo solo persiste Turtle, el perfil JSON-LD se diseña ahora para que clientes futuros puedan consumir el grafo sin cambios estructurales. Base normativa: [JSON-LD 1.1, W3C REC 2020-07-16](https://www.w3.org/TR/json-ld11/).

### 6.1 Diseño del `@context`

- **Un único contexto público** servido en `https://plaza.cr/context/v1.jsonld`, versionado vía SemVer.
- Mapeos: `eli`, `prov`, `skos`, `dcat`, `dcterms`, `schema`, `plaza`.
- No usar términos sin prefijo que oculten origen (ej. `"author"` sin URI).
- `@type` siempre explícito; `@id` siempre URI completa o expandible.
- `@language: "es"` por defecto.

### 6.2 Compacto vs expandido

- **Salida pública por defecto:** compactada con el contexto Plaza, optimizada para legibilidad.
- **Salida diagnóstica:** expandida (`@expanded`), para depuración y verificación.
- Cualquier consumidor puede expandir/compactar con [JSON-LD API 1.1](https://www.w3.org/TR/json-ld11-api/).

### 6.3 Qué NO ocultar en JSON-LD

- URIs canónicas: nunca reemplazar por strings. Siempre `@id`.
- Procedencia: incluir al menos `prov:wasGeneratedBy` con URI a la activity.
- Estado de vigencia: nunca colapsar a booleano simple sin enlace al `skos:Concept`.
- Estado Demo: si el grafo es Demo, `plaza:demoOnly` debe estar presente y visible.
- Confianza en relaciones: si una relación viene reificada (`plaza:NormativeRelation`), debe aparecer también la confianza.

### 6.4 Riesgos (R-09)

JSON simplificado puede ocultar incertidumbre: un cliente podría leer `"inForce": true` sin notar que la afirmación es Demo o tiene baja confianza. Por eso el contexto Plaza nunca colapsa `eli:in_force` a un booleano: siempre referencia un `skos:Concept` con etiqueta legible.

---

## 7. PROV-O provenance profile

Base normativa: [PROV-O W3C Recommendation 2013-04-30](https://www.w3.org/TR/prov-o/).

### 7.1 Patrón canónico

Plaza distingue tres tipos de actividades, todas subclase de `prov:Activity`:

```
prov:Entity (artefacto fuente, e.g. blob SCIJ)
        ↓ prov:wasGeneratedBy
plaza:AcquisitionActivity (captura)
        ↓ produce → plaza:RefinedArtifact (prov:Entity)
        ↓ prov:wasGeneratedBy
plaza:RefinementActivity (limpieza)
        ↓ produce → plaza:CanonicalizationActivity input
        ↓ prov:wasGeneratedBy
eli:LegalResource / eli:LegalExpression (entidad canónica)
```

### 7.2 Triple obligatorio por entidad canónica

Toda `eli:LegalResource`, `eli:LegalExpression`, `eli:LegalResourceSubdivision` y toda relación normativa importante (`eli:amends`, `eli:repeals`, `eli:cites`) debe tener:

```turtle
:entidadCanonica
    prov:wasGeneratedBy :actividadCanonicalizacion ;
    prov:wasDerivedFrom :artefactoFuente .

:actividadCanonicalizacion a plaza:CanonicalizationActivity ;
    prov:used :artefactoFuente ;
    prov:startedAtTime "2026-04-20T14:30:00-06:00"^^xsd:dateTime ;
    prov:endedAtTime   "2026-04-20T14:30:12-06:00"^^xsd:dateTime ;
    prov:wasAssociatedWith :pipelinePlaza .

:artefactoFuente a plaza:SourceArtifact, prov:Entity ;
    plaza:sourceUrl <http://www.pgrweb.go.cr/...> ;
    plaza:scijLocalId "1:95992:128325" ;
    plaza:capturedAt "2026-04-20T14:29:55-06:00"^^xsd:dateTime ;
    plaza:contentHash "sha256:abc...def" ;
    plaza:sourceSystem "SCIJ" ;
    plaza:parserVersion "plaza-scij-parser/0.3.1" .
```

### 7.3 Qué afirmación apunta a qué evidencia

| Afirmación | Evidencia mínima |
|---|---|
| `:norma rdf:type eli:LegalResource` | Artefacto fuente que demuestra existencia de la norma |
| `:norma eli:in_force <plazav:vigencia/vigente>` | Artefacto fuente que afirme vigencia (página SCIJ con campo "vigencia"); en Demo, sin reconciliación con La Gaceta, `plaza:relationConfidence = media` |
| `:norma eli:amends :otra` | Texto fuente con cláusula modificatoria; relación reificada cuando la afirmación viene de inferencia parcial |
| `:expresion eli:title "..."@es` | Captura HTML/PDF con el título visible |
| Subdivisión (artículo) | Anclaje al artefacto fuente que contiene el artículo |

### 7.4 Identidad fuente (SCIJ) como evidencia

El triple `nValor1:nValor2:nValor3` se almacena como **literal** en `plaza:scijLocalId`, no como URI. Esto preserva la trazabilidad sin elevar SCIJ a identidad pública (riesgo R-01).

---

## 8. SKOS vocabulary profile

Base normativa: [SKOS Reference, W3C REC 2009](https://www.w3.org/TR/skos-reference/).

### 8.1 Schemes mínimos

| Scheme | URI | Conceptos iniciales (sugeridos) | Uso |
|---|---|---|---|
| `plazav:tipoNorma` | `https://plaza.cr/vocab/tipo-norma/` | `constitucion`, `ley`, `decreto_ejecutivo`, `reglamento`, `reglamento_municipal`, `acuerdo`, `resolucion`, `tratado` | Valor de `eli:type_document` |
| `plazav:emisor` | `https://plaza.cr/vocab/emisor/` | `asamblea_legislativa`, `poder_ejecutivo`, `cgr`, `bccr`, `municipalidad_san_jose`, ... | Valor de `eli:passed_by` |
| `plazav:vigencia` | `https://plaza.cr/vocab/vigencia/` | `vigente`, `derogada`, `parcialmente_vigente`, `desconocida` | Valor de `eli:in_force` |
| `plazav:tipoSubdivision` | `https://plaza.cr/vocab/tipo-subdivision/` | `articulo`, `inciso`, `parrafo`, `transitorio`, `anexo`, `capitulo`, `titulo` | Valor de `eli:type_subdivision` |
| `plazav:confianzaRelacion` | `https://plaza.cr/vocab/confianza/` | `alta`, `media`, `requiere_revision` | Valor de `plaza:relationConfidence` |
| `plazav:demoEstado` | `https://plaza.cr/vocab/demo/` | `demo_completo`, `demo_parcial`, `pendiente_reconciliacion` | Marcadores Demo |

### 8.2 Cuándo usar SKOS y no literal

- Cualquier eje cerrado o semi-cerrado (estado, tipo, emisor) → SKOS.
- Texto libre auténtico (título, descripción) → literal con `@es`.
- Identificadores externos (NOR francés, SCIJ-id) → literal `dcterms:identifier` o `skos:notation`.

### 8.3 Valores faltantes / desconocidos

Plaza define explícitamente conceptos `..._desconocida` (ej. `vigencia/desconocida`) en lugar de omitir la propiedad. La omisión sugiere "no aplicable"; el concepto explícito sugiere "no sabemos pero es una pregunta válida". Esto se alinea con la guía ELI sobre `eli:in_force` ([ELI Technical Guide §3.4.6](https://op.europa.eu/documents/2050822/2138819/ELI+-+A+Technical+Implementation+Guide.pdf/)).

### 8.4 Versionado de vocabularios

- Cada `skos:ConceptScheme` lleva `owl:versionInfo "1.0.0"` (SemVer).
- Adición de concepto = MINOR.
- Renombrado o cambio semántico = MAJOR.
- Corrección de label = PATCH.
- Conceptos deprecados se marcan `owl:deprecated true` y `skos:historyNote`, **nunca se eliminan**.

### 8.5 Disciplina anti-inflación

**Recomendación del autor:** prohibir crear conceptos `plaza:` sin justificación documentada. Antes de añadir, comprobar:

1. ¿Existe en el vocabulario ELI o EurLex MDR?
2. ¿Existe en SKOS Core o DCMI?
3. Si no, ¿es necesario para Plaza, o solo para una norma específica?

Plaza apunta a un orden de magnitud de **decenas** de conceptos, no centenas.

---

## 9. SHACL validation profile

Base normativa: [SHACL Core W3C REC 2017](https://www.w3.org/TR/shacl/). Plaza usa SHACL Core 2017 como contrato de validación para Demo/MVP. SHACL 1.2 se monitorea, pero no se usa como base obligatoria.

### 9.1 Principio de separación

> SHACL valida **estructura del grafo**, no **verdad jurídica**. Una norma puede pasar todos los `sh:Violation` y aun así ser legalmente errónea. SHACL no infiere derogaciones, no detecta contradicciones normativas, no determina vigencia.

Esto es crítico (riesgo R-06).

### 9.2 Shapes mínimas

| Shape | Target | Validez (Demo) | Validez (post-Demo) |
|---|---|---|---|
| `plaza:LegalResourceShape` | `eli:LegalResource` | Sí | Sí |
| `plaza:LegalExpressionShape` | `eli:LegalExpression` | Sí | Sí |
| `plaza:LegalResourceSubdivisionShape` | `eli:LegalResourceSubdivision` | No (Demo) | Sí |
| `plaza:ProvenanceShape` | toda entidad canónica | Sí | Sí |
| `plaza:ArtifactShape` | `plaza:SourceArtifact` | Sí | Sí |
| `plaza:NormativeRelationShape` | reificaciones de relación | Si se usan | Sí |
| `plaza:DemoStatusShape` | grafo Demo | Sí | n/a en producción |
| `plaza:VocabularyShape` | `skos:ConceptScheme` Plaza | Sí | Sí |

### 9.3 Detalle de cada shape

**`plaza:LegalResourceShape`**

| Constraint | Severity |
|---|---|
| `sh:targetClass eli:LegalResource` | — |
| `eli:jurisdiction` `sh:minCount 1`, `sh:maxCount 1` | Violation |
| `eli:type_document` `sh:minCount 1`, `sh:class skos:Concept` | Violation |
| `eli:number` `sh:datatype xsd:string`, `sh:minCount 1` | Violation |
| `eli:date_document` `sh:datatype xsd:date`, `sh:minCount 1` | Violation |
| `eli:in_force` `sh:class skos:Concept`, `sh:minCount 1` | Violation |
| `eli:is_realized_by` `sh:minCount 1`, `sh:class eli:LegalExpression` | Violation |
| `prov:wasGeneratedBy` `sh:minCount 1` | Violation |
| URI matches `sh:pattern "^(https://plaza\\.cr|https://demo.plaza.cr/)/eli/cr/.+"` | Warning |

**`plaza:LegalExpressionShape`**

- `eli:realizes` `sh:minCount 1`, `sh:class eli:LegalResource` (Violation).
- `eli:language` `sh:minCount 1`, `sh:datatype xsd:language` o `sh:class skos:Concept` (Violation).
- `eli:title` con `sh:datatype rdf:langString` y `sh:languageIn ("es")` (Violation).
- `prov:wasGeneratedBy` (Violation).

**`plaza:ProvenanceShape`**

- Cualquier `eli:LegalResource` o `eli:LegalExpression` debe tener `prov:wasGeneratedBy` apuntando a `prov:Activity` cuya `prov:used` enlace a `plaza:SourceArtifact`. Sin esa cadena, Violation.

**`plaza:ArtifactShape`**

- `plaza:sourceUrl` `sh:datatype xsd:anyURI` (Violation).
- `plaza:capturedAt` `sh:datatype xsd:dateTime` (Violation).
- `plaza:contentHash` `sh:pattern "^sha256:[a-f0-9]{64}$"` (Violation).
- `plaza:sourceSystem` `sh:in ("SCIJ" "Gaceta" "OtraFuente")` (Warning si valor desconocido).

**`plaza:NormativeRelationShape`** (post-Demo, cuando se reifica)

- Subject and object deben ser `eli:LegalResource` o `eli:LegalExpression` (Violation).
- `plaza:relationConfidence` `sh:minCount 1`, `sh:class skos:Concept` (Warning).

**`plaza:DemoStatusShape`**

- En grafo Demo, `dcat:Dataset` debe llevar `plaza:demoOnly true` (Violation).
- Cualquier triple sin `prov:wasGeneratedBy` en grafo Demo → Warning.

**`plaza:VocabularyShape`**

- Cada `skos:Concept` Plaza debe tener `skos:prefLabel` con `@es` y al menos un `skos:inScheme`.
- Cada scheme debe tener `owl:versionInfo` (Violation).

### 9.4 Lo que SHACL NO puede validar (declarado explícitamente)

- Que una derogación sea legalmente correcta.
- Que el texto del artículo sea fiel al texto oficial.
- Que el emisor sea competente.
- Que la fecha de vigencia sea la real.
- Que la relación `eli:based_on`, `eli:basis_for` o `eli:applies` corresponda a la realidad jurídica/reglamentaria.

Plaza reporta esto en cada release: SHACL pass ≠ corrección jurídica.

---

## 10. DCAT publication/catalog profile

Base normativa: [DCAT 3, W3C REC 22 August 2024](https://www.w3.org/TR/vocab-dcat-3/). Demo no publica catálogo DCAT; este perfil define el patrón para producción.

### 10.1 Modelado

| Entidad Plaza | Clase DCAT | Notas |
|---|---|---|
| Snapshot del corpus en `2026-Q2` | `dcat:Dataset` (subclase `plaza:Snapshot`) | Cada snapshot tiene `dcat:version`, `dcat:previousVersion` ([DCAT 3 Change History](https://www.w3.org/TR/vocab-dcat-3/)) |
| Turtle export | `dcat:Distribution` | `dcat:mediaType "text/turtle"`, `spdx:checksum` con `spdx:Checksum` (algoritmo + valor) |
| JSON-LD export | `dcat:Distribution` | `dcat:mediaType "application/ld+json"` |
| SQLite export | `dcat:Distribution` | `dcat:mediaType "application/vnd.sqlite3"` |
| AKN export | `dcat:Distribution` | `dcat:mediaType "application/akn+xml"` ([Akoma Ntoso Media Type](https://docs.oasis-open.org/legaldocml/akn-media/v1.0/akn-media-v1.0.html)) |
| API REST | `dcat:DataService` | `dcat:endpointURL`, `dcat:endpointDescription` (OpenAPI) |
| MCP server | `dcat:DataService` | `dcat:endpointURL`, `dcterms:conformsTo <https://modelcontextprotocol.io/...>` |

### 10.2 Propiedades obligatorias por snapshot

- `dcterms:title`, `dcterms:description` (`@es`)
- `dcterms:issued`, `dcterms:modified` (`xsd:dateTime`, ISO 8601)
- `dcat:version` (calendar id, e.g. `"2026Q2"`)
- `dcat:previousVersion` (URI del snapshot anterior)
- `plaza:ontologyVersion`, `plaza:shapesVersion` (SemVer)
- `dcterms:publisher`
- `dcat:contactPoint`
- `dcterms:license` (incluso si "uso académico/no oficial")
- `prov:wasGeneratedBy` (apunta a la actividad que produjo el snapshot)
- `spdx:checksum` por distribución (SHA-256, ver [DCAT 3 §spdx:Checksum](https://www.w3.org/TR/vocab-dcat-3/) y [DCAT-AP 3.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/))

### 10.3 Limitaciones de publicabilidad

- Si una distribución contiene contenido Demo, **debe** llevar `plaza:demoOnly true` y `plaza:demoLimitations`.
- Si el catálogo describe un endpoint que aún no existe en producción, no se publica. Riesgo R-11.

---

## 11. Akoma Ntoso export profile

Base normativa: [Akoma Ntoso 1.0, OASIS Standard 2018](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html), Part 1 (Vocabulary) y Part 2 (Specifications).

### 11.1 Cuándo Plaza genera AKN

- A demanda, post-MVP, cuando un consumidor solicite intercambio AKN.
- Como **export derivado** del grafo canónico.
- **Nunca** en Demo/MVP (no bloquea ningún criterio de aceptación).

### 11.2 Mapeo limpio

| Entidad Plaza/ELI | Equivalente AKN | Notas |
|---|---|---|
| `eli:LegalResource` | `akn:act` (FRBR Work) | AKN tiene su propia jerarquía FRBR-like dentro del IRI/FRBRWork |
| `eli:LegalExpression` | `akn:act` con `<FRBRExpression>` | — |
| `eli:Format` | `<FRBRManifestation>` | — |
| `eli:LegalResourceSubdivision` (artículo) | `akn:article` | — |
| Transitorio | `akn:transitional` (o equivalente del esquema) | — |
| Anexo | `akn:attachment` / `akn:component` | — |
| `eli:cites` / `eli:amends` | refs internos AKN o atributos `eId`/`refersTo` | Las relaciones inter-acto se preservan en metadatos AKN |

### 11.3 Lo que permanece gobernado por ELI

- URI canónica.
- Versión y point-in-time.
- Estado de vigencia.
- Relaciones entre actos.
- Procedencia.

AKN puede transportar estos metadatos como atributos, pero la fuente de verdad sigue siendo el grafo Plaza.

### 11.4 Vinculación AKN ↔ ELI

Cada documento AKN exportado lleva en su `<FRBRWork>` un `<FRBRuri value="https://plaza.cr/eli/cr/..."/>` apuntando a la URI ELI Plaza. Cada `eId` de subdivisión se vincula a la URI Plaza correspondiente vía `<FRBRalias>` o atributo `refersTo`.

### 11.5 Validación

OASIS provee XML Schemas oficiales en [docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part2-specs/schemas/](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part2-specs.html). Plaza ejecuta `xmllint --schema` o equivalente antes de publicar AKN.

### 11.6 Por qué AKN no bloquea Demo

- Su esquema XML es voluminoso (>500 entidades en v3.x según [Akoma Ntoso Wikipedia](https://en.wikipedia.org/wiki/Akoma_Ntoso)).
- Convertir Turtle → AKN es lineal una vez la canonicalización está estable; convertir AKN → Turtle es ambiguo.
- Demo solo necesita demostrar que el grafo canónico es estable; AKN es valor añadido posterior.

---

## 12. schema.org/Legislation profile

Base normativa: [schema.org/Legislation](https://schema.org/Legislation), [Guía ELI para schema.org](https://eur-lex.europa.eu/eli-register/legis_schema_org.html). El tipo está marcado como `pending`/derivado de ELI.

### 12.1 Cuándo Plaza genera schema.org

- En páginas HTML públicas (futuro), embebido como JSON-LD `<script>`.
- **Solo** complementario; nunca canónico.

### 12.2 Propiedades útiles

| Propiedad schema.org | Equivalente ELI | Comentario |
|---|---|---|
| `schema:legislationIdentifier` | `eli:number` o `dcterms:identifier` | Útil |
| `schema:legislationType` | `eli:type_document` | Útil; `equivalentProperty` declarado en ELI |
| `schema:legislationDate` | `eli:date_document` | Útil |
| `schema:legislationDateOfApplicability` | `eli:date_applicability` | Útil |
| `schema:legislationLegalForce` | `eli:in_force` | Útil; rangos `InForce` / `NotInForce` |
| `schema:legislationLegalValue` | `eli:legal_value` | Útil para Format |
| `schema:legislationPassedBy` | `eli:passed_by` | Útil |
| `schema:jurisdiction` | `eli:jurisdiction` | Útil |
| `schema:legislationApplies` | `eli:applies` | Útil solo para relaciones informativas/de aplicación. No usar como sustituto de `eli:based_on` / `eli:basis_for` en relación ley–decreto. |
| `schema:legislationAmends` | `eli:amends` | Útil |
| `schema:legislationRepeals` | `eli:repeals` | Útil |
| `schema:LegislationObject` | `eli:Format` | Útil para descargas |

### 12.3 Lo que NO duplicar

- No re-declarar `eli:title` y `schema:name` con valores diferentes; usar el mismo literal.
- No emitir `schema.org` sin emitir el grafo ELI subyacente.
- No permitir que el marcado SEO se convierta en el modelo canónico (riesgo R-10).

### 12.4 Recomendación

Plaza genera el JSON-LD schema.org **derivado del grafo Plaza**, mediante una transformación documentada (estilo del [conversor que Publications Office ofrece](https://eur-lex.europa.eu/eli-register/legis_schema_org.html)). Si Plaza descontinúa su HTML público, el schema.org desaparece sin afectar el grafo canónico.

---

## 13. Versioning profile

Base normativa: [SemVer 2.0.0](https://semver.org/), [DCAT 3 versioning properties](https://www.w3.org/TR/vocab-dcat-3/), [ISO 8601-1:2019](https://www.iso.org/iso-8601-date-and-time-format.html).

### 13.1 Reglas Plaza

| Artefacto | Esquema | Cuándo cambia |
|---|---|---|
| `ontology/plaza.ttl` | SemVer (e.g. `0.4.2`) | Adición de propiedad/clase = MINOR; cambio incompatible (renombrado, dominio/rango más estricto) = MAJOR; corrección de label/comentario = PATCH |
| `ontology/shapes.ttl` | SemVer | Endurecimiento que invalida grafos antes válidos = MAJOR; nuevos shapes = MINOR; corrección = PATCH |
| `vocab/*.ttl` (SKOS) | SemVer (por scheme) | Adición de concepto = MINOR; deprecación = MINOR (con `owl:deprecated`); cambio semántico = MAJOR |
| Snapshots (`data/snapshot/*`) | Calendar ID `YYYY-Qn` o `YYYY-MM-DD` | Cada release del corpus |
| URIs de la ontología | Sufijo opcional `/v1`, `/v2` solo en MAJOR | Plaza prefiere URIs estables sin versión, con `owl:versionInfo` interno |
| Contexto JSON-LD | Path `/context/v1.jsonld` | Cambio incompatible = nueva URL `/v2.jsonld` |

### 13.2 Pre-1.0

Mientras Plaza esté en `0.y.z`, todo es inestable; los consumidores deben fijar la versión exacta (regla SemVer §4: "Anything MAY change at any time").

### 13.3 Etiquetado de snapshots

Cada snapshot lleva:

```turtle
:snapshot-2026Q2
    a plaza:Snapshot, dcat:Dataset ;
    dcat:version "2026Q2" ;
    dcat:previousVersion :snapshot-2026Q1 ;
    plaza:ontologyVersion "0.4.0" ;
    plaza:shapesVersion   "0.3.1" ;
    plaza:vocabVersion    "0.2.0" ;
    dcterms:issued "2026-04-15"^^xsd:date .
```

---

## 14. Demo/MVP minimum viable standards subset

### 14.1 Subset Demo (binding por decisión Plaza)

| Estándar | Demo (sí/no) | Por qué |
|---|---|---|
| RDF 1.1 | Sí | Modelo |
| Turtle 1.1 | Sí | Único formato Demo |
| ELI ontología (subset §3.2) | Sí | Identidad |
| PROV-O subset (`prov:Activity`, `prov:Entity`, `prov:wasGeneratedBy`, `prov:used`, `prov:wasDerivedFrom`) | Sí | Procedencia |
| SKOS subset (`Concept`, `ConceptScheme`, `prefLabel`, `notation`, `inScheme`) | Sí | Vocabularios mínimos |
| SHACL Core (8 shapes mínimas, §9.2) | Sí | Validación pre-publicación |
| ISO 3166-1, ISO 639-1, ISO 8601 | Sí | Códigos |
| SemVer | Sí | Versionado de ontología/shapes |
| JSON-LD 1.1 | No (definido pero no emitido) | Diferido |
| DCAT 3 | No (definido pero no emitido) | Diferido |
| Akoma Ntoso | No | Diferido |
| schema.org/Legislation | No | Diferido |
| Dublin Core Terms | Mínimo (`dcterms:title` solo cuando ELI no aplique, `dcterms:identifier` para SCIJ) | Auxiliar |
| RDFa | No | No hay HTML público |
| SPARQL endpoint público | No | Decisión Plaza |

### 14.2 Acceso Demo

MCP es la única superficie. Demo no expone HTTP, ni SPARQL, ni descarga abierta. El grafo Turtle está en disco y se accede vía herramientas MCP que cargan/consultan el grafo localmente.

---

## 15. Deferred or rejected standards

### 15.1 Diferidos (post-MVP, planeados)

- **JSON-LD 1.1** salida pública con contexto versionado.
- **DCAT 3** catálogo de snapshots y servicios.
- **Akoma Ntoso 1.0** export.
- **schema.org/Legislation** marcado HTML.
- **RDFa** si Plaza publica HTML jurídico.
- **ELI Pillar 4** (sitemap/Atom feed) cuando exista corpus público estable ([ELI Pillar 4](https://op.europa.eu/en/web/eu-vocabularies/eli)).

### 15.2 Rechazados (no en hoja de ruta actual)

- **FOAF / schema.org/Person / W3C ORG** — fuera de scope (no person modeling).
- **LKIF** — implica razonamiento jurídico, fuera de scope.
- **ODRL** — no se modelan licencias ejecutables sobre normas.
- **OWL DL razonamiento** — no se requieren inferencias.
- **SPARQL endpoint público** — coste/riesgo.
- **Akoma-native ingestion** — rompería la regla "ELI identifica".
- **ELI-DL** (draft legislation) — Plaza no modela proyectos de ley en alcance actual ([ELI-DL](https://interoperable-europe.ec.europa.eu/collection/eli-european-legislation-identifier/solution/eli-ontology-draft-legislation-eli-dl)).
- **ELI-I** (impacto de actos) — no necesario hasta consolidación post-MVP ([ELI-I](https://en.wikipedia.org/wiki/European_Legislation_Identifier)).

---

## 16. Implementation risk register

| # | Riesgo | Severidad | Disparador típico | Mitigación | Estándar/doc relacionado |
|---|---|---|---|---|---|
| R-01 | Tratar `nValor1:nValor2:nValor3` como URI canónica | **Crítica** | Atajo en pipeline de ingesta | URIs canónicas siempre `https://plaza.cr/eli/...` o `https://demo.plaza.cr/eli/...`; SCIJ id solo en `plaza:SourceArtifact` vía `plaza:scijLocalId` / `dcterms:identifier` | ELI Pillar 1, §4.4 |
| R-02 | Usar Akoma Ntoso como fuente de identidad | **Crítica** | Adopción acrítica de pipeline AKN-first | Regla maestra: ELI identifica, AKN serializa; AKN solo como export | §11.5 |
| R-03 | Exponer SPARQL público antes de tener throttling/SLA | Alta | Demanda externa | No SPARQL en Demo/MVP; revisar tras estabilización | DCAT 3 `dcat:DataService` |
| R-04 | Procedencia incompleta (afirmaciones sin `prov:wasGeneratedBy`) | Alta | Performance shortcuts | SHACL `plaza:ProvenanceShape` lo bloquea | PROV-O |
| R-05 | Inversión de dirección en relaciones (`amends` vs `amended_by`, `based_on` vs `basis_for`) | Alta | Confusión `subject/object` | Pruebas unitarias por cada par; preferir la propiedad directa y generar inversa solo cuando sea mecánica y verificada | ELI ontología |
| R-06 | SHACL pass interpretado como verdad jurídica | Alta | Comunicación pública | Disclaimer en README, en `dcterms:description` del snapshot, en MCP responses | SHACL §9 |
| R-07 | Drift de vocabulario controlado (creación ad-hoc de SKOS concepts) | Media | Falta de proceso | PR review obligatorio; `owl:versionInfo` en cada scheme | SKOS Reference |
| R-08 | Modelado oculto de personas (vía `dcterms:creator` con literal "Juan Pérez") | Media | Importación automática | SHACL prohíbe `foaf:Person`; `dcterms:creator` solo con organización | DCMI Terms |
| R-09 | JSON simplificado oculta incertidumbre | Media | UX optimization | Contexto JSON-LD prohíbe colapso a primitivos; `eli:in_force` siempre URI | JSON-LD 1.1 |
| R-10 | schema.org/Legislation domina y desplaza ELI | Media | Presión SEO | schema.org siempre derivado; nunca fuente | schema.org/Legislation guide |
| R-11 | DCAT promete servicios que no existen | Media | Marketing del catálogo | Solo publicar `dcat:DataService` con endpoint operativo verificado | DCAT 3 |
| R-12 | Confundir Turtle 1.2 features (triple terms, base direction) con base instalable | Media | Adopción prematura | Plaza usa Turtle 1.1 (REC); 1.2 es Working Draft | RDF 1.2 Turtle WD |
| R-13 | URIs con trailing slash, casing inconsistente o mezcla Demo/producción | Media | Reescrituras manuales | Función pura `canonicalize(uri)`; CI valida host, path y absence of trailing slash | RFC 3986 / ELI URI |
| R-14 | Mezcla de `xsd:date` y `xsd:dateTime` para fechas legales | Baja | Heterogeneidad de fuentes | SHACL fija datatype por propiedad; ISO 8601 estricto | ISO 8601-1:2019 |
| R-15 | Snapshots sin `dcat:previousVersion` rompen trazabilidad temporal | Baja | Primera publicación | SHACL para `plaza:Snapshot` exige el enlace desde el segundo en adelante | DCAT 3 |
| R-16 | ELI ontology version drift (Plaza fija 1.x; aparece 2.x) | Baja | Actualización upstream | `plaza:eliOntologyVersion` literal; revisar cada release | ELI ontology version history |
| R-17 | Confusión Format vs Distribution (ELI vs DCAT) | Baja | Mapeo descuidado | `eli:Format` describe la encarnación legal; `dcat:Distribution` describe el archivo descargable; pueden coexistir | ELI ↔ DCAT |
| R-18 | Adopción de SHACL Rules antes de tiempo | Baja | Tentación de inferencia | Plaza usa solo SHACL Core; SHACL Rules ([WD](https://www.w3.org/TR/shacl12-rules/)) está fuera de alcance | SHACL 1.2 Rules |

---

## 17. Open questions requiring project decision

1. **¿Plaza diferencia `ley` de `ley_organica` en `plazav:tipoNorma`?** El SCIJ no siempre distingue. Decisión necesaria antes de fijar el vocabulario v1.0.
2. **¿`eli:passed_by` se modela como SKOS concept del scheme `plazav:emisor` o como URI directa a una entidad institucional?** SKOS-only es más simple; URI directa permite enriquecer después.
3. **¿La Constitución se modela como un `eli:LegalResource` con muchas `eli:LegalExpression` (por reforma) o como múltiples `LegalResource` consolidados enlazados?** Ver discusión en [ELI Technical Guide §4.1.1](https://op.europa.eu/documents/2050822/2138819/ELI+-+A+Technical+Implementation+Guide.pdf/).
4. **¿`eli:ontology` se importa o solo se referencia por prefijo?** Importar (`owl:imports`) facilita validación; solo referenciar reduce dependencias.
5. **¿Plaza define un scheme `plazav:idioma` propio o usa `xsd:language` directo?** ELI permite ambos.
6. **¿Hash canónico de un `plaza:SourceArtifact`: SHA-256 del archivo crudo o de su normalización?** Recomendación: del crudo, para verificabilidad estricta; cualquier normalización es nueva entidad PROV.
7. **¿Demo usa `https://demo.plaza.cr/eli/...` o `plaza-demo://`?** Decisión actual: `https://demo.plaza.cr/eli/...`, porque es resoluble e inspeccionable por herramientas RDF/HTTP. Debe llevar `canonical_public_uri_issued=false` y `plaza:demoOnly true` para no confundirse con producción.
8. **¿Versionado del contexto JSON-LD: por path (`/v1`) o por ContentNegotiation?** Por path es más simple.
9. **¿Cómo se fija `plaza:eliOntologyVersion`?** Decisión actual: apuntar a ELI Ontology V1.5 LATEST, pero el build debe descargar y validar el OWL/RDF oficial de Publications Office antes de emitir `ontology/plaza.ttl`.
10. **¿Cómo se modelan normas con número alfanumérico (e.g. directrices con prefijo de departamento)?** ELI permite `{natural_identifier}` literal; mantener string.
11. **¿El componente `{emisor}` en URI Plaza acepta espacios/acentos o se normaliza a snake_case ASCII?** Recomendación: snake_case ASCII (e.g. `municipalidad_san_jose`).
12. **¿Plaza emite `dcat:Catalog` o solo `dcat:Dataset` aislados en MVP?** `dcat:Catalog` es opcional inicialmente.

---

## 18. Appendix A — Example Turtle

Ejemplo **ilustrativo** (no afirmación jurídica). Muestra: LegalResource, LegalExpression, Format, SourceArtifact (PROV-O), Activity, relación normativa, SKOS concept y marcador Demo.

```turtle
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms:<http://purl.org/dc/terms/> .
@prefix prov:   <http://www.w3.org/ns/prov#> .
@prefix eli:    <http://data.europa.eu/eli/ontology#> .
@prefix plaza:  <https://plaza.cr/ontology#> .
@prefix plazav: <https://plaza.cr/vocab/> .

# (1) LegalResource
<https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849>
    a eli:LegalResource ;
    eli:jurisdiction      <plazav:jurisdiccion/cr> ;
    eli:type_document     <plazav:tipo-norma/ley> ;
    eli:passed_by         <plazav:emisor/asamblea_legislativa> ;
    eli:number            "9849" ;
    eli:date_document     "2020-05-25"^^xsd:date ;
    eli:first_date_entry_in_force "2020-06-09"^^xsd:date ;
    eli:in_force          <plazav:vigencia/vigente> ;
    eli:is_realized_by
        <https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849/version/2020-05-25> ;
    plaza:demoOnly        true ;
    plaza:demoLimitations "Sin reconciliación con La Gaceta; vigencia inferida solo del SCIJ."@es ;
    prov:wasGeneratedBy   <https://demo.plaza.cr/activity/canon/2026-04-20T14:30:00Z/9849> ;
    prov:wasDerivedFrom   <https://demo.plaza.cr/artifact/scij/1-95992-128325> .

# (2) LegalExpression
<https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849/version/2020-05-25>
    a eli:LegalExpression ;
    eli:realizes  <https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849> ;
    eli:language  "es" ;
    eli:title     "Ley de fortalecimiento de las finanzas públicas (ejemplo ilustrativo)"@es ;
    prov:wasGeneratedBy <https://demo.plaza.cr/activity/canon/2026-04-20T14:30:00Z/9849> .

# (3) SourceArtifact (PROV-O Entity)
<https://demo.plaza.cr/artifact/scij/1-95992-128325>
    a plaza:SourceArtifact, prov:Entity ;
    plaza:sourceUrl     <http://www.pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?nValor1=1&nValor2=95992&nValor3=128325> ;
    plaza:scijLocalId   "1:95992:128325" ;
    plaza:capturedAt    "2026-04-20T14:29:55-06:00"^^xsd:dateTime ;
    plaza:contentHash   "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08" ;
    plaza:sourceSystem  "SCIJ" ;
    plaza:parserVersion "plaza-scij-parser/0.3.1" .

# (4) Canonicalization Activity
<https://demo.plaza.cr/activity/canon/2026-04-20T14:30:00Z/9849>
    a plaza:CanonicalizationActivity, prov:Activity ;
    prov:used           <https://demo.plaza.cr/artifact/scij/1-95992-128325> ;
    prov:startedAtTime  "2026-04-20T14:30:00-06:00"^^xsd:dateTime ;
    prov:endedAtTime    "2026-04-20T14:30:12-06:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <https://demo.plaza.cr/agent/pipeline/v0.4.0> .

# (5) Normative relation (eli:based_on)
<https://demo.plaza.cr/eli/cr/poder_ejecutivo/2021/decreto_ejecutivo/43000>
    a eli:LegalResource ;
    eli:based_on <https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849> ;
    prov:wasGeneratedBy <https://demo.plaza.cr/activity/canon/2026-04-20T14:35:00Z/43000> .

# (6) SKOS concept
<plazav:tipo-norma/ley>
    a skos:Concept ;
    skos:inScheme  <plazav:tipo-norma> ;
    skos:prefLabel "Ley"@es ;
    skos:notation  "ley" .

<plazav:tipo-norma>
    a skos:ConceptScheme ;
    skos:prefLabel  "Tipos de norma costarricense"@es ;
    <http://www.w3.org/2002/07/owl#versionInfo> "0.2.0" .

# (7) Demo marker on the dataset
<https://demo.plaza.cr/snapshot/2026Q2>
    a plaza:Snapshot ;
    plaza:demoOnly true ;
    plaza:demoLimitations "Demo limitada a 4 recursos; sin DCAT publicado; sin reconciliación Gaceta."@es .
```

---

## 19. Appendix B — Example JSON-LD

Compactado con un contexto Plaza. Solo ilustra la forma futura; Demo no lo emite.

```json
{
  "@context": "https://plaza.cr/context/v1.jsonld",
  "@id": "https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849",
  "@type": "eli:LegalResource",
  "jurisdiction": { "@id": "plazav:jurisdiccion/cr" },
  "type_document": { "@id": "plazav:tipo-norma/ley", "prefLabel": "Ley" },
  "passed_by":     { "@id": "plazav:emisor/asamblea_legislativa" },
  "number": "9849",
  "date_document": "2020-05-25",
  "first_date_entry_in_force": "2020-06-09",
  "in_force": { "@id": "plazav:vigencia/vigente", "prefLabel": "Vigente" },
  "is_realized_by": {
    "@id": "https://demo.plaza.cr/eli/cr/asamblea_legislativa/2020/ley/9849/version/2020-05-25",
    "@type": "eli:LegalExpression",
    "language": "es",
    "title": { "@value": "Ley de fortalecimiento de las finanzas públicas (ejemplo ilustrativo)", "@language": "es" }
  },
  "wasGeneratedBy": {
    "@id": "https://demo.plaza.cr/activity/canon/2026-04-20T14:30:00Z/9849",
    "@type": "plaza:CanonicalizationActivity",
    "used": "https://demo.plaza.cr/artifact/scij/1-95992-128325"
  },
  "demoOnly": true,
  "demoLimitations": "Sin reconciliación con La Gaceta."
}
```

Notas sobre el contexto: `in_force` se mantiene como objeto con `@id` (nunca booleano); `wasGeneratedBy` siempre presente; `demoOnly` no se omite si es `true`.

---

## 20. Appendix C — Example SHACL shapes

Subset de `ontology/shapes.ttl` (ilustrativo, SHACL Core).

```turtle
@prefix sh:     <http://www.w3.org/ns/shacl#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix prov:   <http://www.w3.org/ns/prov#> .
@prefix eli:    <http://data.europa.eu/eli/ontology#> .
@prefix plaza:  <https://plaza.cr/ontology#> .

plaza:LegalResourceShape
    a sh:NodeShape ;
    sh:targetClass eli:LegalResource ;
    sh:property [
        sh:path eli:jurisdiction ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class skos:Concept ;
        sh:severity sh:Violation ;
        sh:message "Toda LegalResource debe declarar exactamente una eli:jurisdiction (skos:Concept)."@es
    ] ;
    sh:property [
        sh:path eli:type_document ;
        sh:minCount 1 ;
        sh:class skos:Concept ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path eli:number ;
        sh:datatype xsd:string ;
        sh:minCount 1 ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path eli:date_document ;
        sh:datatype xsd:date ;
        sh:minCount 1 ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path eli:in_force ;
        sh:class skos:Concept ;
        sh:minCount 1 ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path eli:is_realized_by ;
        sh:minCount 1 ;
        sh:class eli:LegalExpression ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path prov:wasGeneratedBy ;
        sh:minCount 1 ;
        sh:severity sh:Violation ;
        sh:message "Falta procedencia (prov:wasGeneratedBy)."@es
    ] .

plaza:LegalExpressionShape
    a sh:NodeShape ;
    sh:targetClass eli:LegalExpression ;
    sh:property [
        sh:path eli:realizes ;
        sh:minCount 1 ;
        sh:class eli:LegalResource ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path eli:language ;
        sh:minCount 1 ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path eli:title ;
        sh:minCount 1 ;
        sh:datatype <http://www.w3.org/1999/02/22-rdf-syntax-ns#langString> ;
        sh:languageIn ( "es" ) ;
        sh:severity sh:Violation
    ] .

plaza:ArtifactShape
    a sh:NodeShape ;
    sh:targetClass plaza:SourceArtifact ;
    sh:property [
        sh:path plaza:sourceUrl ;
        sh:minCount 1 ;
        sh:datatype xsd:anyURI ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path plaza:capturedAt ;
        sh:minCount 1 ;
        sh:datatype xsd:dateTime ;
        sh:severity sh:Violation
    ] ;
    sh:property [
        sh:path plaza:contentHash ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
        sh:pattern "^sha256:[a-f0-9]{64}$" ;
        sh:severity sh:Violation
    ] .

plaza:DemoStatusShape
    a sh:NodeShape ;
    sh:targetClass plaza:Snapshot ;
    sh:property [
        sh:path plaza:demoOnly ;
        sh:minCount 1 ;
        sh:datatype xsd:boolean ;
        sh:severity sh:Violation ;
        sh:message "Snapshot debe declarar plaza:demoOnly explícitamente."@es
    ] .
```

---

## 21. Appendix D — Source links

**ELI:**
- ELI Register / EUR-Lex: https://eur-lex.europa.eu/eli-register/about.html
- ELI Pillars / what is ELI: https://eur-lex.europa.eu/eli-register/what_is_eli.html
- ELI vocabularies (Publications Office): https://op.europa.eu/en/web/eu-vocabularies/eli
- ELI ontology OWL: https://data.europa.eu/eli/ontology
- ELI Technical Implementation Guide: https://op.europa.eu/documents/2050822/2138819/ELI+-+A+Technical+Implementation+Guide.pdf/
- How to implement ELI: https://eur-lex.europa.eu/eli-register/implementing_eli.html
- EUR-Lex 52012XG1026 (Council conclusions establishing ELI): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52012XG1026(01)
- Spain ELI implementation: https://www.boe.es/legislacion/eli.php?lang=en
- Irish Statute Book ELI URI scheme (PDF): https://www.irishstatutebook.ie/pdf/ELI_URI_schema.pdf
- ELI-DL (draft legislation): https://interoperable-europe.ec.europa.eu/collection/eli-european-legislation-identifier/solution/eli-ontology-draft-legislation-eli-dl
- ELI Wikipedia: https://en.wikipedia.org/wiki/European_Legislation_Identifier

**W3C standards:**
- RDF 1.1 Turtle (REC 2014): https://www.w3.org/TR/turtle/
- RDF 1.2 Turtle (Working Draft): https://www.w3.org/TR/rdf12-turtle/
- JSON-LD 1.1 (REC 2020): https://www.w3.org/TR/json-ld11/
- JSON-LD 1.1 Framing: https://www.w3.org/TR/json-ld11-framing/
- PROV-O (REC 2013): https://www.w3.org/TR/prov-o/
- PROV-Overview: https://www.w3.org/TR/prov-overview/
- SKOS Reference (REC 2009): https://www.w3.org/TR/skos-reference/
- SKOS Primer: https://www.w3.org/TR/skos-primer/
- SHACL Core (REC 2017): https://www.w3.org/TR/shacl/
- SHACL 1.2 Core: https://www.w3.org/TR/shacl12-core/
- SHACL 1.2 Overview: https://w3c.github.io/data-shapes/shacl12-overview/
- SHACL 1.2 Rules: https://www.w3.org/TR/shacl12-rules/
- DCAT 3 (REC 22 August 2024): https://www.w3.org/TR/vocab-dcat-3/
- DCAT-AP 3.0: https://semiceu.github.io/DCAT-AP/releases/3.0.0/
- W3C date/time profile of ISO 8601: https://www.w3.org/TR/NOTE-datetime

**OASIS Akoma Ntoso:**
- OASIS standard page: https://www.oasis-open.org/standard/akn-v1-0/
- Part 1 (XML Vocabulary): https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html
- Part 2 (Specifications): https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part2-specs.html
- Akoma Ntoso Media Type: https://docs.oasis-open.org/legaldocml/akn-media/v1.0/akn-media-v1.0.html
- Akoma Ntoso (general site): http://akomantoso.info/
- Akoma Ntoso Wikipedia: https://en.wikipedia.org/wiki/Akoma_Ntoso

**schema.org:**
- Legislation: https://schema.org/Legislation
- LegislationObject: https://schema.org/LegislationObject
- legislationType: https://schema.org/legislationType
- legislationApplies: https://schema.org/legislationApplies
- legislationLegalValue: https://schema.org/legislationLegalValue
- legislationDateOfApplicability: https://schema.org/legislationDateOfApplicability
- ELI guide for schema.org Legislation: https://eur-lex.europa.eu/eli-register/legis_schema_org.html
- Sparna how-to: https://sparna-git.github.io/legislation-schema.org-howto/

**DCMI:**
- DCMI Metadata Terms: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- DCMI Specifications index: https://www.dublincore.org/specifications/
- DCMI Namespace Policy: https://www.dublincore.org/specifications/dublin-core/dcmi-namespace/
- RFC 5013 (Dublin Core Metadata): https://www.ietf.org/rfc/rfc5013.html

**ISO codes:**
- ISO 3166-1 Costa Rica: https://www.iso.org/obp/ui/#iso:code:3166:CR
- ISO 3166-2:CR (Wikipedia): https://en.wikipedia.org/wiki/ISO_3166-2:CR
- ISO 639-3 Spanish (`spa`): https://iso639-3.sil.org/code/spa
- ISO 639 codes (LOC): https://www.loc.gov/standards/iso639-2/php/code_list.php
- ISO 8601 date and time: https://www.iso.org/iso-8601-date-and-time-format.html
- ISO 8601-1:2019 ed-1: https://www.iso.org/obp/ui/#iso:std:iso:8601:-1:ed-1:v1:en

**SemVer:**
- Semantic Versioning 2.0.0: https://semver.org/

**Costa Rica fuentes operativas:**
- SCIJ (PGR): https://pgrweb.go.cr/scij/ayuda/historia.aspx
- SINALEVI: https://www.pgr.go.cr/servicios/sinalevi/
- Globalex Costa Rica research guide: https://www.nyulawglobal.org/globalex/costa_rica1.html

---

*Fin de STANDARDS_IMPLEMENTATION_PROFILE.md.*
