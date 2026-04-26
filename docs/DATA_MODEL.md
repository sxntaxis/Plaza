# Plaza — Modelo de Datos

Este documento especifica la estructura del **grafo canónico** de Plaza: qué clases lo componen, qué propiedades las relacionan, a qué estándares internacionales se alinea, y qué extensiones costarricenses definimos.

El modelo de datos es la implementación concreta del Principio 6 (Estándares internacionales como columna). Toda decisión de modelado se resuelve primero consultando los estándares establecidos. Plaza define vocabulario propio únicamente cuando ningún estándar cubre un caso específico del derecho costarricense — y lo hace como extensión documentada, no como sistema paralelo.

Este documento describe el **contrato semántico** del grafo canónico, no su implementación de almacenamiento. La forma en que los datos se guardan (triple store, archivos versionados, base relacional materializada) es decisión de la arquitectura operacional, descrita en `ARCHITECTURE.md`.

---

## Estándares adoptados por capa

Plaza adopta estándares internacionales con responsabilidades separadas. No todos forman parte del grafo canónico de la misma manera: algunos definen clases y propiedades RDF, otros validan el grafo, otros describen superficies de publicación, y otros serializan documentos legales.

El grafo canónico de Plaza es **ELI-first**: ELI gobierna identidad, metadata legal, versionado FRBR y relaciones entre recursos normativos. Los demás estándares se incorporan según su capa específica.

| Estándar | Prefijo / formato | Capa | Rol en Plaza |
|---|---|---|---|
| [ELI](https://data.europa.eu/eli/ontology) | `eli` | Grafo canónico | Identidad de legislación, modelo FRBR, metadata legal, relaciones entre normas y versiones |
| [schema.org/Legislation](https://schema.org/Legislation) | `schema` | Grafo canónico / web | Tipo adicional para interoperabilidad con motores de búsqueda y herramientas web generales |
| [PROV-O](https://www.w3.org/TR/prov-o/) | `prov` | Grafo canónico | Procedencia de entidades, afirmaciones, actividades de procesamiento y artefactos fuente |
| [SKOS](https://www.w3.org/TR/skos-reference/) | `skos` | Grafo canónico | Vocabularios controlados: tipos de norma, emisores, estados de vigencia y tipos de subdivisión |
| [Dublin Core Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | `dcterms` | Grafo canónico auxiliar | Metadata bibliográfica genérica cuando ELI no cubre suficientemente el caso |
| [W3C ORG](https://www.w3.org/TR/vocab-org/) | `org` | Futuro | Reservada para capa institucional futura; no activa en esta versión del modelo |
| Plaza extensions | `plaza` | Grafo canónico | Extensiones costarricenses mínimas, documentadas explícitamente |
| [Akoma Ntoso](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/) | `application/akoma-ntoso+xml` | Serialización documental | Export XML derivado para representar la estructura interna de textos legales; no gobierna la identidad canónica |
| [SHACL](https://www.w3.org/TR/shacl/) | `.ttl` shapes | Validación | Shapes versionadas que validan el grafo RDF antes de publicación |
| [DCAT](https://www.w3.org/TR/vocab-dcat-3/) | `dcat` | Catálogo | Descripción de snapshots, distribuciones, servicios y metadata de publicación |

El prefijo `plaza:` corresponde al namespace `https://plaza.cr/ontology#`. Las extensiones bajo este prefijo están documentadas en la sección correspondiente de este documento.

## Relación entre ELI y Akoma Ntoso

ELI y Akoma Ntoso se traslapan en que ambos pueden representar recursos legislativos, versiones y subdivisiones. Plaza resuelve ese traslape asignándoles responsabilidades distintas.

**ELI gobierna la identidad pública.** Toda norma, versión, artículo, transitorio o anexo que Plaza publique recibe una URI canónica definida por `URI_POLICY.md` y expresada en el grafo como recurso ELI.

**Akoma Ntoso gobierna la representación documental XML.** Cuando Plaza exporta una norma como Akoma Ntoso, el XML preserva la estructura interna del texto legal — títulos, capítulos, artículos, incisos, transitorios, anexos — pero no introduce identidades públicas alternativas. Los identificadores internos de Akoma, cuando existan, deben enlazar o corresponder a las URIs canónicas ELI/Plaza.

La regla operativa es simple: **ELI identifica; Akoma serializa.**

Por tanto, Akoma Ntoso no es requisito para canonicalizar una entidad. Una norma puede entrar al grafo canónico si satisface las reglas ELI, PROV-O, SKOS y SHACL aplicables. La representación Akoma Ntoso puede generarse después como superficie derivada de publicación.

---

## Modelo FRBR: las tres capas de identidad

ELI adopta la tri-jerarquía FRBR (Functional Requirements for Bibliographic Records). Plaza la adopta también, sin modificación. Entenderla es prerequisito para entender cualquier cosa en el grafo.

```
┌────────────────────────────────────────────────────────────────┐
│ eli:LegalResource — la obra intelectual abstracta              │
│ "La Ley del Impuesto sobre la Renta de Costa Rica"             │
│                                                                │
│ Tiene:                                                         │
│   - identidad permanente                                       │
│   - número oficial, emisor, jurisdicción                       │
│   - relaciones con otras obras (deroga, modifica, cita)        │
│                                                                │
│ NO tiene:                                                      │
│   - texto literal (eso vive en Expression)                     │
│   - formato de archivo (eso vive en Format)                    │
└────────────────────────────────────────────────────────────────┘
                              │ eli:is_realized_by
                              ▼
┌────────────────────────────────────────────────────────────────┐
│ eli:LegalExpression — realización concreta en tiempo/idioma    │
│ "La versión vigente al 2023-01-15 en español"                  │
│                                                                │
│ Tiene:                                                         │
│   - texto literal                                              │
│   - fecha de vigencia                                          │
│   - idioma                                                     │
│   - referencias a artículos y sus versiones                    │
│                                                                │
│ Múltiples por LegalResource (una por versión histórica)        │
└────────────────────────────────────────────────────────────────┘
                              │ eli:is_embodied_by
                              ▼
┌────────────────────────────────────────────────────────────────┐
│ eli:Format — manifestación en un formato específico            │
│ "Esta LegalExpression serializada en Akoma Ntoso XML"          │
│                                                                │
│ Plaza maneja Formats como resultado de content negotiation     │
│ sobre la URI de la Expression. Las Formats son efímeras        │
│ en el grafo canónico; se generan bajo demanda.                 │
└────────────────────────────────────────────────────────────────┘
```

**Por qué esto importa:** colapsar Resource y Expression en una sola entidad ("la Ley 7092" como si fuera una cosa con texto) parece conveniente pero oscurece la pregunta "¿qué decía esta ley el 15 de marzo de 2019?" — que requiere distinguir entre la obra (permanente) y sus realizaciones temporales. FRBR da vocabulario preciso para esa distinción, y Plaza lo adopta sin compromiso.

En Plaza:

- **Un LegalResource por norma.** La Ley 7092 tiene un único LegalResource, con URI permanente. Esta entidad representa "la Ley 7092 como obra intelectual" y nunca cambia de URI.
- **Un LegalExpression por cada versión histórica.** Cada vez que la Ley 7092 cambia su texto material, se crea un nuevo LegalExpression con URI propia que incluye la fecha de vigencia. Las Expressions históricas se preservan.
- **Format no se materializa en el grafo.** Se genera por content negotiation cuando un consumidor solicita una URI de Expression con un Accept header específico.

Esta decisión fija la relación con Akoma Ntoso: una exportación Akoma corresponde al nivel de `eli:Format` o a una representación serializada derivada de una `eli:LegalExpression`. No reemplaza la `LegalExpression`, no define la URI pública y no es la fuente de verdad del grafo canónico.

---

## Clases principales

### eli:LegalResource (plus schema:Legislation)

**Rol**: la norma como obra intelectual. Permanente, única por norma.

**URI**: la URI canónica sin componente de versión. Ejemplo: `https://plaza.cr/eli/cr/asamblea/1988/ley/7092`.

**Propiedades típicas**:

| Propiedad | Significado | Rango |
|---|---|---|
| `eli:id_local` | Identificador interno operacional (ej. `ley_7092`) | Literal |
| `eli:type_document` | Tipo normativo | SKOS concept (ver vocabulario controlado) |
| `eli:jurisdiction` | Jurisdicción de aplicación | SKOS concept |
| `eli:passed_by` | Órgano emisor | URI de organización (futuro) o literal |
| `eli:date_document` | Fecha de emisión | xsd:date |
| `eli:number` | Número oficial | Literal |
| `eli:first_date_entry_in_force` | Primera fecha de entrada en vigencia | xsd:date |
| `eli:date_no_longer_in_force` | Fecha de derogación total, si aplica | xsd:date |
| `eli:in_force` | Estado de vigencia actual | SKOS concept |
| `eli:is_realized_by` | Enlaces a sus LegalExpressions | URI(s) |
| `eli:amends`, `eli:amended_by` | Relaciones de modificación con otras LegalResources | URI(s) |
| `eli:repeals`, `eli:repealed_by` | Relaciones de derogación | URI(s) |
| `eli:cites`, `eli:cited_by` | Relaciones de cita | URI(s) |
| `prov:wasDerivedFrom` | Artefactos fuente de los que deriva esta entidad | URI(s) |

**También es** `schema:Legislation` por equivalencia declarada en la ontología ELI, lo cual facilita que motores de búsqueda y herramientas web genéricas entiendan el recurso sin necesidad de conocer ELI.

---

### eli:LegalExpression

**Rol**: una versión específica de la norma, con texto material en un idioma y vigente en un período.

**URI**: la URI canónica con componente de versión. Ejemplo: `https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/2023-01-15`.

**Propiedades típicas**:

| Propiedad | Significado | Rango |
|---|---|---|
| `eli:realizes` | La LegalResource que esta Expression realiza | URI |
| `eli:language` | Idioma de la expresión | SKOS concept (ISO 639-2) |
| `eli:version` | Identificador de versión | Literal |
| `eli:version_date` | Fecha de vigencia inicio de esta versión | xsd:date |
| `eli:title` | Título oficial | Literal con tag de idioma |
| `eli:title_short` | Título corto | Literal con tag de idioma |
| `eli:has_member` | Enlaces a subdivisiones (artículos) | URI(s) |
| `dcterms:description` | Descripción | Literal |
| `prov:wasDerivedFrom` | Artefactos fuente | URI(s) |

---

### eli:LegalResourceSubdivision

**Rol**: una subdivisión estructural de una LegalResource — típicamente un artículo, un transitorio, un anexo, o eventualmente un capítulo/título si la norma lo justifica.

**URI**: construida según URI_POLICY. Ejemplos:

- `https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42`
- `https://plaza.cr/eli/cr/asamblea/1988/ley/7092/transitorio/i`

Como LegalResource, una Subdivision es una obra intelectual abstracta. Tiene sus propias Expressions (versiones históricas del artículo a través del tiempo).

**Propiedades típicas**:

| Propiedad | Significado | Rango |
|---|---|---|
| `eli:is_member_of` | LegalResource a la que pertenece | URI |
| `plaza:subdivision_type` | Tipo de subdivisión (articulo, transitorio, anexo) | SKOS concept |
| `plaza:subdivision_number` | Identificador natural de la subdivisión | Literal |
| `eli:is_realized_by` | Expressions históricas de esta subdivisión | URI(s) |
| `eli:amends`, `eli:repeals` | Relaciones con otras subdivisiones | URI(s) |

Nota: `plaza:subdivision_type` y `plaza:subdivision_number` son extensiones costarricenses. ELI no distingue formalmente entre artículos y transitorios porque los sistemas jurídicos europeos no siempre tienen esa figura. El derecho costarricense sí, y Plaza lo codifica explícitamente.

Estas propiedades no intentan replicar todo el modelo estructural de Akoma Ntoso dentro del grafo RDF. Representan únicamente la estructura mínima necesaria para identidad, versionado, navegación y citación. La estructura documental completa puede expresarse en exportaciones Akoma Ntoso cuando exista suficiente estructura refinada para generarlas.

---

### Subdivisiones y Expressions de subdivisiones

Así como una LegalResource tiene LegalExpressions, una LegalResourceSubdivision tiene Expressions propias. Esto permite preguntas como "¿qué decía el artículo 42 de la Ley 7092 el 15 de marzo de 2019?"

La Expression de un artículo es también una LegalExpression en términos de ELI, pero referencia a la subdivisión correspondiente:

- URI: `https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42/version/2023-01-15`
- `eli:realizes`: la URI del artículo como Subdivision
- Tiene texto literal, fecha de vigencia, y procedencia propia

**Relación entre versiones de norma y versiones de artículos**: las versiones no están atadas. Una nueva versión de la norma puede resultar de cambios en uno o varios artículos; un artículo puede mantener la misma Expression a través de varias versiones de la norma si su texto no cambió. El grafo modela esto explícitamente vía `eli:has_member` en cada Expression de norma apuntando a las Expressions de artículos vigentes en esa versión.

---

## Estructura textual mínima vs estructura documental completa

El grafo canónico de Plaza modela únicamente la estructura textual necesaria para cumplir sus contratos públicos: identidad, citación, versionado, navegación y trazabilidad.

En el alcance actual, las unidades estructurales canónicas mínimas son:

- norma;
- versión de norma;
- artículo;
- versión de artículo;
- transitorio;
- anexo cuando sea necesario.

Plaza no está obligado a canonicalizar toda la microestructura documental de una norma — capítulos, títulos, secciones, párrafos, incisos, numerales — salvo cuando esa estructura sea necesaria para una URI pública, una relación jurídica, una cita verificable o una validación de integridad.

Akoma Ntoso es el formato preferente para representar esa estructura documental completa cuando Plaza la exporte como XML. El grafo RDF conserva las entidades jurídicas citables; Akoma conserva la forma documental.

---

## Relaciones entre normas

ELI provee un vocabulario rico para modelar relaciones. Plaza lo adopta tal cual, sin reinvención.

### Relaciones de modificación

| Propiedad ELI | Significado | Inverso |
|---|---|---|
| `eli:amends` | Modifica a | `eli:amended_by` |
| `eli:repeals` | Deroga a | `eli:repealed_by` |
| `eli:corrects` | Corrige (sin cambio legal) a | `eli:corrected_by` |
| `eli:changes` | Cambia (genérico; amends/repeals son subpropiedades) | `eli:changed_by` |

**Mapeo desde SCIJ**: las "afectaciones" de SCIJ se mapean a estas propiedades según el tipo de operación:

- "Deroga" → `eli:repeals`
- "Deroga parcialmente", "Reforma" → `eli:amends`
- "Corrige errata" → `eli:corrects`
- Tipos ambiguos o sin clasificación clara → `eli:changes` (propiedad genérica)

El tipo específico capturado por SCIJ se preserva como propiedad adicional cuando agrega información:

```
plaza:scij_affectation_type  "Reforma parcial"  (literal, si la clasificación de SCIJ es más específica de lo que ELI captura)
```

### Relaciones de cita

| Propiedad ELI | Significado |
|---|---|
| `eli:cites` | Esta norma cita textualmente o por referencia a otra |
| `eli:cited_by` | Esta norma es citada por otra (inverso) |

Las "concordancias" de SCIJ típicamente se mapean a `eli:cites` cuando son referencias directas entre normas, o a `plaza:concordancia_tematica` cuando son vínculos temáticos que no alcanzan la calidad de cita directa.

### Relaciones de fundamento reglamentario

| Propiedad ELI | Significado |
|---|---|
| `eli:based_on` | Esta norma se funda en otra |
| `eli:basis_for` | Esta norma es fundamento de otra (inverso) |
| `eli:applies` | Esta norma aplica a otra en sentido informativo/de conformidad, cuando la evidencia lo justifica |

Las "reglamentaciones" de SCIJ (donde un reglamento se funda en una ley) se mapean por defecto a `eli:based_on` del reglamento hacia la ley y, cuando se emite inverso, a `eli:basis_for` de la ley hacia el reglamento. `eli:applies` queda reservado para relaciones informativas/de conformidad cuando la fuente y el caso lo justifiquen; no es la relación primaria de reglamentación de la Demo.

### Relaciones de vigencia

| Propiedad ELI | Significado |
|---|---|
| `eli:commences` | Esta norma pone en vigencia a otra |
| `eli:commenced_by` | Esta norma entra en vigencia por otra (inverso) |

---

## Procedencia: PROV-O

Cada entidad en el grafo canónico carga su cadena de procedencia. La implementación sigue el patrón estándar PROV-O.

### Entidades PROV-O en Plaza

| Clase PROV | Rol en Plaza |
|---|---|
| `prov:Entity` | Toda entidad del grafo canónico (LegalResource, Expression, etc.) es también una prov:Entity |
| `prov:Activity` | Las ejecuciones de los parsers, canonicalizadores, y reconciliadores |
| `prov:Agent` | Plaza misma, cada parser identificado por versión, y las fuentes oficiales |

### Propiedades típicas de procedencia

Para cada entidad del grafo:

```turtle
<https://plaza.cr/eli/cr/asamblea/1988/ley/7092> 
    prov:wasDerivedFrom <https://plaza.cr/artifact/scij/abc123def456> ;
    prov:wasGeneratedBy <https://plaza.cr/activity/canonicalize/2026-04-20T10:15:00Z> ;
    prov:wasAttributedTo <https://plaza.cr/agent/plaza-canonicalizer-v0.1.0> .

<https://plaza.cr/activity/canonicalize/2026-04-20T10:15:00Z>
    a prov:Activity ;
    prov:startedAtTime "2026-04-20T10:15:00Z"^^xsd:dateTime ;
    prov:used <https://plaza.cr/artifact/scij/abc123def456> ;
    prov:wasAssociatedWith <https://plaza.cr/agent/plaza-canonicalizer-v0.1.0> .

<https://plaza.cr/artifact/scij/abc123def456>
    a prov:Entity ;
    prov:wasAttributedTo <https://plaza.cr/agent/source/scij-pgr> ;
    plaza:source_url "https://pgrweb.go.cr/scij/..." ;
    plaza:captured_at "2026-04-15T03:22:00Z"^^xsd:dateTime ;
    plaza:content_hash "sha256:..." .
```

Esto permite responder, para cualquier afirmación en el grafo: de qué artefacto viene, cuándo fue capturado, qué parser lo interpretó, qué versión del parser, cuándo se canonicalizó. Operacionaliza el Principio 4 (Procedencia explícita y completa).

---

## Vocabularios controlados (SKOS)

Donde ELI define tablas de valores controlados, Plaza define el equivalente costarricense como SKOS concept scheme.

### plaza:TipoNorma

Concept scheme para tipos normativos costarricenses. Concepto raíz: `plaza:TipoNorma`.

Conceptos principales (no exhaustivo; ver URI_POLICY para la lista canónica):

- `plaza:tipo-ley` (con label "Ley ordinaria" en español)
- `plaza:tipo-ley-organica`
- `plaza:tipo-decreto-ejecutivo`
- `plaza:tipo-decreto-legislativo`
- `plaza:tipo-reglamento`
- `plaza:tipo-directriz`
- `plaza:tipo-resolucion`
- `plaza:tipo-acuerdo`
- `plaza:tipo-codigo`
- `plaza:tipo-constitucion`

Cada concepto tiene equivalencia `skos:exactMatch` o `skos:closeMatch` con conceptos ELI donde existan equivalentes razonables.

### plaza:EmisorNorma

Concept scheme para órganos emisores. Concepto raíz: `plaza:EmisorNorma`.

- `plaza:emisor-asamblea`
- `plaza:emisor-poder-ejecutivo`
- `plaza:emisor-poder-judicial`
- `plaza:emisor-tse`
- `plaza:emisor-cgr`
- etc.

Esta capa está mínimamente poblada en la versión actual y se extenderá cuando la capa institucional se incorpore formalmente.

### plaza:EstadoVigencia

Concept scheme para el estado de vigencia de una norma.

- `plaza:vigente`
- `plaza:derogada`
- `plaza:suspendida`
- `plaza:anulada`
- `plaza:en-revision` (para casos donde Plaza no pudo determinar con certeza)

### plaza:TipoSubdivision

Concept scheme para tipos de subdivisiones estructurales.

- `plaza:subdivision-articulo`
- `plaza:subdivision-transitorio`
- `plaza:subdivision-anexo`
- `plaza:subdivision-capitulo` (si se modela en el futuro)
- `plaza:subdivision-titulo` (si se modela en el futuro)

---

## Extensiones costarricenses

Estas son las clases y propiedades que Plaza define bajo el prefijo `plaza:` porque ningún estándar internacional las cubre adecuadamente. Cada una está documentada con su rationale.

### plaza:subdivision_type

**Rationale**: ELI no distingue formalmente entre artículos, transitorios, anexos. El derecho costarricense sí, y esa distinción tiene consecuencias legales (un transitorio tiene régimen de vigencia diferente a un artículo permanente).

### plaza:subdivision_number

**Rationale**: el identificador natural de la subdivisión como aparece en el texto oficial (ej. "42 bis", "primero", "III").

### plaza:scij_affectation_type

**Rationale**: cuando SCIJ clasifica una afectación con un tipo más específico que lo que ELI captura (ej. "Reforma parcial con vigencia diferida"), preservamos la clasificación original para no perder información.

### plaza:concordancia_tematica

**Rationale**: las "concordancias" de SCIJ no siempre son citas directas; a veces son vínculos temáticos curados por el cuerpo editorial de SCIJ. ELI no tiene una propiedad equivalente clara, por lo que Plaza define esta propiedad explícitamente.

### plaza:content_hash

**Rationale**: hash criptográfico del contenido de una entidad, útil para verificación de integridad y detección de cambios. No hay equivalente directo en PROV-O (que maneja procedencia pero no integridad criptográfica).

### plaza:source_url, plaza:captured_at

**Rationale**: metadata básica de captura que excede lo que PROV-O modela directamente. Se usan en artefactos crudos.

### plaza:reconciliation_issue

**Rationale**: cuando Plaza detecta un conflicto entre fuentes que no puede resolver automáticamente, lo registra como `plaza:reconciliation_issue` enlazado a las entidades en conflicto. Esto operacionaliza el Principio 1 (evidencia antes que inferencia) — los conflictos quedan visibles en el grafo canónico hasta que se resuelvan.

### plaza:provisional

**Rationale**: marca una entidad como provisional, cuando se publicó con datos suficientes para ser útil pero con alguna dimensión conocida como incompleta. Permite consumidores cautelosos filtrar por entidades no-provisionales.

Toda extensión `plaza:` está formalizada en una ontología OWL publicada junto con el proyecto, con definiciones precisas de domain, range, y relaciones a vocabularios estándar.

---

## Ejemplo completo: la Ley 7092

Para ilustrar cómo el modelo opera en conjunto, este es un fragmento del grafo canónico para la Ley del Impuesto sobre la Renta (Ley 7092 de 1988):

```turtle
@prefix eli: <http://data.europa.eu/eli/ontology#> .
@prefix schema: <https://schema.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix plaza: <https://plaza.cr/ontology#> .

# LegalResource (la obra intelectual)
<https://plaza.cr/eli/cr/asamblea/1988/ley/7092>
    a eli:LegalResource, schema:Legislation ;
    eli:id_local "ley_7092" ;
    eli:type_document plaza:tipo-ley ;
    eli:jurisdiction "CRI" ;
    eli:passed_by plaza:emisor-asamblea ;
    eli:date_document "1988-04-21"^^xsd:date ;
    eli:number "7092" ;
    eli:first_date_entry_in_force "1988-05-24"^^xsd:date ;
    eli:in_force plaza:vigente ;
    eli:is_realized_by <https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/original>,
                       <https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/2023-01-15> ;
    eli:amended_by <https://plaza.cr/eli/cr/asamblea/2018/ley/9635> ;
    prov:wasDerivedFrom <https://plaza.cr/artifact/scij/norm_7092_metadata_abc123> .

# LegalExpression vigente (la realización actual)
<https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/2023-01-15>
    a eli:LegalExpression ;
    eli:realizes <https://plaza.cr/eli/cr/asamblea/1988/ley/7092> ;
    eli:language "spa" ;
    eli:version_date "2023-01-15"^^xsd:date ;
    eli:title "Ley del Impuesto sobre la Renta"@es ;
    eli:has_member <https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/1/version/2023-01-15>,
                   <https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42/version/2023-01-15> ;
    prov:wasDerivedFrom <https://plaza.cr/artifact/scij/norm_7092_text_def456> .

# Una subdivisión (el artículo 42)
<https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42>
    a eli:LegalResourceSubdivision ;
    eli:is_member_of <https://plaza.cr/eli/cr/asamblea/1988/ley/7092> ;
    plaza:subdivision_type plaza:subdivision-articulo ;
    plaza:subdivision_number "42" ;
    eli:is_realized_by <https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42/version/2023-01-15> .
```

Este fragmento es semánticamente autocontenido: un consumidor que entiende ELI + PROV-O + SKOS puede procesar este grafo sin conocer nada específico de Plaza, excepto las extensiones documentadas explícitamente.

La representación Akoma Ntoso de esta misma norma sería una serialización XML derivada de estas entidades y del texto refinado. No se muestra aquí porque no forma parte del grafo canónico RDF. Sus identificadores internos deben corresponder a las URIs ELI/Plaza cuando representen recursos canónicos.

---

## Reglas de modelado

Cuando se agrega una nueva clase de información al grafo, estas reglas aplican:

**1. Agotar estándares RDF primero.** Antes de crear una propiedad `plaza:`, agotar ELI, schema.org/Legislation, Dublin Core, PROV-O y SKOS. La mayoría de necesidades del grafo canónico están cubiertas por ellos.

**2. No convertir serializaciones en modelo canónico.** Akoma Ntoso se consulta para exportaciones XML y estructura documental, pero no desplaza la identidad ELI ni obliga a duplicar en RDF toda la microestructura documental.

**3. Extensiones `plaza:` requieren documentación.** Toda propiedad nueva bajo el prefijo `plaza:` se documenta en este documento con su rationale. No hay extensiones silenciosas.

**4. Las extensiones preservan compatibilidad.** Un consumidor que conoce solo los estándares debe poder procesar el grafo ignorando las propiedades `plaza:` sin perder las relaciones fundamentales. Nunca una extensión `plaza:` reemplaza una propiedad ELI equivalente — la acompaña.

**5. Los concept schemes SKOS se mapean a estándares cuando sea posible.** Cada concepto `plaza:` que tenga equivalente razonable en un vocabulario estándar (ej. tabla de tipos ELI) se vincula con `skos:exactMatch` o `skos:closeMatch`.

**6. Versionado del modelo.** El modelo de datos se versiona junto con la ontología Plaza. Cambios compatibles (agregar clases, agregar propiedades opcionales, agregar conceptos SKOS) incrementan minor. Cambios incompatibles (retirar clases, cambiar domain/range, redefinir semántica) requieren major y convivencia con la versión anterior.

---

## Relación con otras políticas

- [`PRINCIPLES.md`](PRINCIPLES.md) — Principio 6 (estándares como columna) y Principio 4 (procedencia explícita) gobiernan este documento.
- [`URI_POLICY.md`](URI_POLICY.md) — define las URIs que las entidades de este modelo llevan.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — describe cómo el grafo canónico se produce y se almacena.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — define SHACL shapes que validan conformidad de instancias concretas a este modelo.
- [`VERSIONING.md`](VERSIONING.md) — define cómo se versiona la ontología Plaza misma.
