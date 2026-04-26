# Plaza — MCP Implementation Profile

## Implementation status

As of `0.4.0`, this profile is a target contract for the functional Demo. The repository implements only the local validation/fail-closed guard. Tools, resources, structured outputs, and citations are `0.5.0` work.

## 0. Resumen ejecutivo de decisiones

Este documento define el perfil de implementación de un servidor **MCP (Model Context Protocol)** para la fase Demo del proyecto Plaza, sobre el grafo canónico `data/demo/canonical/demo.ttl`. El servidor MCP es **el único canal de exposición** del Demo (no hay API REST, no hay UI, no hay snapshots, no hay Akoma Ntoso). Su función es **presentar datos**: texto, relaciones, metadatos y procedencia, con citación completa y sin interpretación legal.

Las decisiones binarias adoptadas en este perfil son:

- **Versión de protocolo objetivo:** `2025-11-25` (revisión vigente al 25 de abril de 2026), con compatibilidad mínima hacia `2025-06-18`. Fuente: `https://modelcontextprotocol.io/specification/2025-11-25` (cabecera "Version 2025-11-25 (latest)") y `https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/` (confirma que no se ha cortado versión nueva desde noviembre 2025).
- **Transporte primario:** **stdio** para Demo local (compatible con Claude Desktop y con la guía oficial: *"Clients SHOULD support stdio whenever possible"*, `https://modelcontextprotocol.io/specification/2025-11-25/basic/transports`). Streamable HTTP queda diferido a fase post‑Demo.
- **URIs Demo:** las entidades legales del grafo usan `https://demo.plaza.cr/eli/...`. No se usa un esquema URI propio para recursos legales. Estas URIs son resolubles, inspeccionables por herramientas RDF/HTTP y mecánicamente convertibles a `https://plaza.cr/eli/...` sustituyendo el host cuando Plaza emita URIs públicas de producción. En Demo no se emiten URIs canónicas de producción.
- **Primitivas usadas:** `resources`, `resource templates`, `tools`, `logging`. **No** se usan `prompts`, `sampling`, `elicitation`, `roots`, `completions` ni `tasks` en Demo.
- **Modo:** sólo lectura, determinista, local. Todas las herramientas declaran `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: false`.
- **Compuerta de validación:** el servidor **falla cerrado** si `data/demo/validation/validation_report.json` indica `conforms=false` o no existe.
- **SDK recomendado:** Python (`mcp[cli]` ≥ 1.25 en PyPI) sobre `FastMCP`, justificado por el ecosistema RDF/SHACL maduro (`rdflib`, `pyshacl`).
- **Sin interpretación, sin mutación, sin red, sin lectura de archivos arbitrarios.** El servidor expone exclusivamente lo que está en el grafo canónico y en los reportes de procedencia ya construidos.

El resultado es un servidor MCP *small, deterministic, local‑first* alineado con la especificación oficial y con todas las restricciones del Demo.

---

## 1. Fuentes y metodología

Se priorizaron exclusivamente fuentes oficiales y normativas. Las afirmaciones técnicas se contrastaron contra la especificación publicada en `modelcontextprotocol.io`, el repositorio canónico `github.com/modelcontextprotocol/modelcontextprotocol`, los SDKs oficiales (`python-sdk`, `typescript-sdk`) y los blogs oficiales del proyecto. Para cada decisión se distingue:

- **Capacidad oficial MCP** — definida en la especificación.
- **Decisión Plaza** — vinculante para este Demo, no negociable.
- **Recomendación** — derivada del análisis técnico del equipo de investigación; revisable.
- **Pregunta abierta** — requiere decisión explícita del proyecto.

La incertidumbre se marca de forma explícita. Cuando dos fuentes oficiales discrepan, se prefiere la página versionada `2025-11-25`. Las fuentes externas (blogs de terceros, SaaS) se usaron sólo para corroborar fechas de despliegue real, nunca para definir comportamiento normativo.

La revisión `2025-11-25` añade sobre `2025-06-18`: descubrimiento OIDC, *icons*, consentimiento incremental de scopes, modo URL para *elicitation*, *tools-in-sampling*, *Tasks* experimental, *JSON Schema 2020-12* como dialecto por defecto y aclaración de que servidores stdio pueden usar stderr para todos los niveles de log (PR #670). **Ninguno de estos cambios obliga a Plaza Demo a adoptar nuevas primitivas**; la línea base del Demo es interoperable con clientes que negocien `2025-06-18`.

---

## 2. Conceptos MCP relevantes para Plaza

MCP describe una arquitectura **host – client – server** sobre **JSON-RPC 2.0**, con sesión con estado y negociación explícita de capacidades. La siguiente tabla resume cada concepto y su tratamiento en Plaza Demo.

| Concepto MCP | ¿Plaza Demo lo usa? | Justificación |
|---|---|---|
| **Server / Client / Host** | Sí — Plaza implementa un *server*; el *host* (Claude Desktop u otro) instancia el *client*. | Es la arquitectura base; no opcional. |
| **JSON-RPC 2.0** | Sí (obligatorio). | *"All messages between MCP clients and servers MUST follow the JSON-RPC 2.0 specification"*. Sin batching (eliminado en `2025-06-18`). |
| **Lifecycle (initialize / initialized / shutdown)** | Sí. | Plaza intercambia `protocolVersion`, declara capacidades, recibe `notifications/initialized`. |
| **Capability negotiation** | Sí, mínima: `resources`, `tools`, `logging`. | Plaza no declara `prompts`, `completions`, `tasks`. |
| **Resources** | Sí — primitiva principal. | El Demo es esencialmente una superficie de datos de sólo lectura. |
| **Resource Templates (RFC 6570)** | Sí — para URIs paramétricas ELI Demo (`https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}`). | Refleja la estructura ELI sin enumerar todo el universo legal. |
| **Tools** | Sí — ocho herramientas determinísticas. | Permiten consultas estructuradas (búsqueda, relaciones, procedencia, explicación) que no encajan en lectura por URI. |
| **Structured tool output (`outputSchema`, `structuredContent`)** | Sí. | Cada herramienta declara `outputSchema` y emite `structuredContent` para validación cliente. Disponible desde `2025-06-18`. |
| **Tool annotations** (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) | Sí — todas las herramientas son *read-only, idempotent, closed-world*. | Hints para el cliente; el spec los marca como **untrusted** salvo servidor confiable, pero comunican intención. |
| **Prompts** | **No.** | Plaza no es un asistente; los prompts son plantillas iniciadas por el usuario. Fuera del alcance. |
| **Sampling** | **No.** | Plaza no necesita pedir completaciones al LLM del cliente. |
| **Elicitation** | **No.** | El servidor no debe pedir datos al usuario en medio de una operación; toda consulta se contesta o se rechaza. |
| **Roots** | **No declarados ni requeridos.** | Plaza opera sobre su propio almacén interno (`data/demo/canonical/demo.ttl`); no necesita límites de filesystem del cliente. |
| **Completions** | **No** en Demo. | Auto-completar argumentos de templates es opcional; se difiere. |
| **Logging** | Sí — capability declarada. | Permite emitir `notifications/message` con niveles RFC 5424. |
| **Tasks (experimental, 2025-11-25)** | **No.** | Es experimental y no se requiere para operaciones síncronas y rápidas. |
| **Authorization (OAuth 2.1, RFC 8707, RFC 9728)** | **No** en Demo (transporte stdio). | El spec dice explícitamente: *"Implementations using an STDIO transport SHOULD NOT follow this specification, and instead retrieve credentials from the environment"*. |

**Modelo de errores:** MCP usa el espacio de códigos JSON-RPC 2.0 estándar (`-32700`, `-32600`, `-32601`, `-32602`, `-32603`, y `-32000..-32099` para errores definidos por la implementación). Adicionalmente: `-32002` está documentado en la spec para *resource not found*. Una **distinción clave de `2025-11-25` (SEP-1303)** es que los errores de validación de input de tools deben devolverse como **Tool Execution Errors** (resultado JSON-RPC exitoso con `isError: true`), no como errores de protocolo, para permitir auto-corrección del modelo. Plaza adopta esta distinción.

---

## 3. Principios de diseño del MCP del Demo Plaza

Los siguientes principios son vinculantes para el diseño y la revisión de cualquier herramienta o recurso del servidor MCP de Plaza.

**Determinismo total.** Para una misma entrada y un mismo grafo, la salida debe ser byte-equivalente módulo timestamps. Esto implica: orden estable de tripletas (canonicalización de prefijos al arrancar, ordenamiento por `(subject, predicate, object)`), serialización determinística de JSON (`sort_keys=True`), ranking de búsqueda definido por una función pura sobre el grafo cargado.

**Sólo lectura.** No hay ninguna herramienta que mute estado, escriba archivos, abra red, ejecute procesos, ni reordene grafos en disco. La carga inicial del Turtle es la única operación de lectura de filesystem permitida; durante la sesión no se vuelve a tocar disco.

**Cita en cada respuesta.** Toda respuesta de herramienta y todo recurso retornado incluye un objeto `citations[]` con al menos: URI Plaza-Demo, sistema fuente (`scij`), URL del artefacto fuente cuando se conoce, identificador local del sistema fuente, ruta/hash del artefacto preservado y tipo de evidencia. Una herramienta que no pueda construir su `citations[]` debe fallar con error explícito, no entregar datos sin atribución.

**Cierre cerrado ante ausencia de validación.** Si al iniciar el servidor no se encuentra `data/demo/validation/validation_report.json`, o el reporte indica `conforms=false`, o el `demo.ttl` no parsea, el servidor **no inicia el modo operativo**: registra el error por stderr y responde a `tools/list`, `resources/list` y `tools/call` con un error de servidor `validation_gate_failed`.

**Sin interpretación legal.** Las descripciones de herramientas, los avisos en respuestas y las explicaciones (`plaza.explain_resource`) son afirmaciones sobre la estructura del grafo, no sobre el ordenamiento jurídico. Ver §8 para el lenguaje exacto.

**Local-first.** El Demo corre localmente como subproceso del host. No expone puertos. No requiere autenticación. La compatibilidad inmediata con Claude Desktop es un objetivo explícito.

**Mínimo cambio de superficie.** Se evitan capacidades que no son estrictamente necesarias para los doce casos de aceptación (§13). Cada nueva primitiva incrementa la superficie de ataque de *prompt injection*, error y mantenimiento.

---

## 4. Recursos, plantillas de recursos y herramientas

La superficie MCP de Plaza Demo se divide en tres planos: **recursos estáticos**, **plantillas de recursos** y **herramientas**. La regla de asignación es:

- Si la consulta es *"dame el contenido identificado por este URI"*, es **resource** o **resource template**.
- Si la consulta requiere **parámetros no-URI** (texto libre, filtros, dirección de relación), es **tool**.
- Cuando una operación tiene ambas formas naturales, se expone como **tool**, y opcionalmente como **resource** sólo si añade valor al cliente (por ejemplo, `plaza.get_graph` también disponible como resource para clientes que no soportan tools).

### 4.1. Recursos estáticos

| URI | MIME | Descripción | Decisión |
|---|---|---|---|
| `https://demo.plaza.cr/mcp/graph/main` | `text/turtle` | Grafo canónico Demo completo, parseable. | Recurso. |
| `https://demo.plaza.cr/mcp/graph/main.jsonld` | `application/ld+json` | Misma información en JSON-LD (derivada al vuelo, no persistida). | Recurso (recomendación; ver §17). |
| `https://demo.plaza.cr/mcp/catalog/resources` | `application/json` | Listado JSON de los 4 recursos legales del Demo (igual al output de `plaza.list_resources`). | Recurso (espejo del tool, para clientes que no llaman tools). |
| `https://demo.plaza.cr/mcp/catalog/validation` | `application/json` | Copia del `validation_report.json`. | Recurso. |
| `https://demo.plaza.cr/mcp/catalog/demo_notice` | `text/markdown` | Texto fijo describiendo el carácter Demo y las limitaciones. | Recurso. |

### 4.2. Plantillas de recursos (RFC 6570)

| `uriTemplate` | MIME por defecto | Descripción |
|---|---|---|
| `https://demo.plaza.cr/eli/cr/asamblea/{año}/constitucion/politica` | `application/json` | Recurso constitucional (en Demo solo año `1949`). |
| `https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}` | `application/json` | Ley de la Asamblea Legislativa. |
| `https://demo.plaza.cr/eli/cr/poder_ejecutivo/{año}/decreto_ejecutivo/{número}` | `application/json` | Decreto ejecutivo. |
| `https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}/text` | `text/plain` | Texto preservado (subset). |
| `https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}/turtle` | `text/turtle` | Subgrafo CBD (Concise Bounded Description) del recurso. |
| `https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}/provenance` | `application/json` | Procedencia PROV-O serializada como JSON. |
| `https://demo.plaza.cr/eli/cr/poder_ejecutivo/{año}/decreto_ejecutivo/{número}/text` | `text/plain` | Texto preservado del decreto. |
| `https://demo.plaza.cr/eli/cr/poder_ejecutivo/{año}/decreto_ejecutivo/{número}/turtle` | `text/turtle` | Subgrafo CBD del decreto. |
| `https://demo.plaza.cr/eli/cr/poder_ejecutivo/{año}/decreto_ejecutivo/{número}/provenance` | `application/json` | Procedencia. |

**Decisión Plaza:** las plantillas con sufijo `/text`, `/turtle`, `/provenance` son la **forma canónica** de obtener representaciones; las herramientas equivalentes (`plaza.get_text`, `plaza.get_graph`, `plaza.get_provenance`) son la superficie *model-controlled* y aceptan exactamente los mismos URIs base.

**Nota oficial:** la spec advierte que `mimeType` en una *resource template* solo debe declararse si **todas** las URIs concretas que la matchean comparten ese tipo (`schema.ts` 2025-11-25). Por eso cada par recurso/representación tiene su propia plantilla con sufijo, y no una única plantilla con `?format=`.

### 4.3. Herramientas

| Nombre | Tipo | `readOnly` | `idempotent` | `openWorld` | Notas |
|---|---|---|---|---|---|
| `plaza.list_resources` | tool | true | true | false | Lista los 4 recursos Demo. |
| `plaza.get_resource` | tool | true | true | false | Metadatos estructurados de un recurso. |
| `plaza.get_text` | tool | true | true | false | Texto preservado SCIJ. |
| `plaza.search` | tool | true | true | false | Búsqueda determinística sobre índice local. |
| `plaza.get_relations` | tool | true | true | false | Relaciones normativas. |
| `plaza.get_provenance` | tool | true | true | false | PROV-O completo de un recurso. |
| `plaza.get_graph` | tool | true | true | false | Subgrafo Turtle parseable. |
| `plaza.explain_resource` | tool | true | true | false | Explicación factual de metadatos y limitaciones. **No** interpretación legal. |

Cada herramienta se complementa con un recurso o plantilla espejo cuando tiene sentido (ver §4.1, §4.2). El servidor declara `tools.listChanged: true` y `resources.listChanged: true` para permitir notificaciones futuras, aunque en Demo el catálogo es estático.

---

## 5. Conjunto de capacidades MCP propuesto

El servidor declara, en la respuesta a `initialize`:

```json
{
  "protocolVersion": "2025-11-25",
  "capabilities": {
    "resources": { "subscribe": false, "listChanged": true },
    "tools":     { "listChanged": true },
    "logging":   {}
  },
  "serverInfo": {
    "name": "plaza-demo-mcp",
    "title": "Plaza — Costa Rican legal-data Demo (MCP)",
    "version": "0.1.0"
  },
  "instructions": "Servidor de datos legales costarricenses en modo Demo. Sólo lectura. Cuatro recursos reales. Una relación normativa real. Citar siempre URIs bajo `https://demo.plaza.cr/eli/...`. No es asistente legal."
}
```

Justificación campo por campo:

- `protocolVersion` se fija a `2025-11-25` porque es la última estable. Si el cliente solicita `2025-06-18`, el servidor responde con `2025-06-18` (la spec exige que el servidor responda con una versión que soporta; ver §1.7 de la spec lifecycle). Plaza implementa ambas.
- `resources.subscribe = false`: el grafo Demo es inmutable durante la sesión; suscripción aporta complejidad sin beneficio.
- `resources.listChanged = true` y `tools.listChanged = true`: permitidos pero efectivamente no se emiten en Demo. Habilitarlos no cuesta nada y mantiene la puerta abierta para post-Demo.
- `logging = {}`: habilitado para emitir `notifications/message` con eventos de carga, validación y errores controlados.
- **No** se declara `prompts`, `completions`, `sampling`, `elicitation`, `tasks`, `experimental`. Esto es decisión Plaza explícita.
- `instructions` es texto fijo que muchos clientes (incluido Claude Desktop) muestran al usuario; aquí se establece la primera línea de defensa contra *misuse* legal.

---

## 6. Esquemas de herramientas y recursos

Las herramientas usan **JSON Schema 2020-12** (dialecto por defecto desde `2025-11-25`, SEP-1613). Todos los `outputSchema` declarados son objeto con propiedades `data`, `citations`, `warnings`, `limitations`, `status`, `generated_from_snapshot_or_graph`, `demo_notice` (ver §7).

### 6.1. `plaza.list_resources`

```json
{
  "name": "plaza.list_resources",
  "title": "Listar recursos legales del Demo",
  "description": "Devuelve los cuatro recursos legales reales que conforman el grafo Demo (Constitución Política, una ley, un decreto ejecutivo, y la cuarta pieza definida en data/demo/canonical/demo.ttl). No incluye el texto completo. Para texto, usar plaza.get_text.",
  "inputSchema": { "type": "object", "additionalProperties": false, "properties": {} },
  "outputSchema": {
    "type": "object",
    "required": ["data", "citations", "status", "demo_notice"],
    "properties": {
      "data": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["uri", "type", "title", "issuer", "demo_status", "available_operations"],
          "properties": {
            "uri":   { "type": "string", "format": "uri" },
            "type":  { "type": "string", "enum": ["constitucion","ley","decreto_ejecutivo"] },
            "title": { "type": "string" },
            "issuer":{ "type": "string" },
            "demo_status": { "type": "string", "enum": ["canonical_demo"] },
            "available_operations": {
              "type": "array",
              "items": { "enum": ["get_resource","get_text","get_graph","get_relations","get_provenance","explain_resource"] }
            }
          }
        }
      },
      "citations":  { "$ref": "#/$defs/citations" },
      "warnings":   { "type": "array", "items": { "type": "string" } },
      "limitations":{ "type": "array", "items": { "type": "string" } },
      "status":     { "type": "string", "enum": ["ok","partial","error"] },
      "generated_from_snapshot_or_graph": { "type": "string", "const": "demo.ttl" },
      "demo_notice": { "type": "string" }
    }
  },
  "annotations": { "readOnlyHint": true, "idempotentHint": true, "destructiveHint": false, "openWorldHint": false }
}
```

### 6.2. `plaza.get_resource`

`inputSchema`:

```json
{ "type":"object", "additionalProperties":false,
  "required":["uri"],
  "properties":{ "uri":{ "type":"string", "pattern":"^https://demo\\.plaza\\.cr/eli/" } } }
```

`outputSchema.data`:

```json
{ "type":"object",
  "required":["uri","production_candidate_uri","canonical_public_uri_issued","type","number_or_slug","issuer","title","status","limitations","source_summary"],
  "properties":{
    "uri":{ "type":"string" },
    "production_candidate_uri":{ "type":["string","null"], "description":"Forma futura de producción obtenida sustituyendo demo.plaza.cr por plaza.cr; no implica emisión canónica pública." },
    "canonical_public_uri_issued":{ "type":"boolean", "const": false },
    "type":{ "enum":["constitucion","ley","decreto_ejecutivo"] },
    "number_or_slug":{ "type":"string" },
    "issuer":{ "type":"string" },
    "title":{ "type":"string" },
    "status":{ "enum":["represented_in_demo_graph"] },
    "limitations":{ "type":"array","items":{"type":"string"} },
    "source_summary":{
      "type":"object",
      "required":["source_system","artifact_id","hash"],
      "properties":{
        "source_system":{ "const":"scij" },
        "source_url":{ "type":["string","null"] },
        "source_local_id":{ "type":["string","null"] },
        "artifact_id":{ "type":"string" },
        "hash":{ "type":"string" }
      }
    } } }
```

### 6.3. `plaza.get_text`

`inputSchema`: `{ uri: string, range?: { start: int, end: int } }`. `range` es opcional para *chunking*; ver §10.

`outputSchema.data`:

```json
{ "type":"object",
  "required":["uri","language","text","source_artifact","hash","limitations","is_truncated"],
  "properties":{
    "uri":{ "type":"string" },
    "language":{ "type":"string", "enum":["es"] },
    "text":{ "type":"string" },
    "source_artifact":{ "type":"string" },
    "hash":{ "type":"string", "description":"Hash SHA-256 del artefacto fuente preservado." },
    "is_truncated":{ "type":"boolean" },
    "byte_range":{ "type":["object","null"] },
    "expression_distinction":{ "type":"string", "description":"Nota factual sobre la distinción ELI resource/expression." },
    "limitations":{ "type":"array","items":{"type":"string"} } } }
```

**Nota Plaza:** `expression_distinction` es siempre el mismo aviso fijo: *"En Demo, esta representación corresponde a una expresión textual derivada de un único artefacto SCIJ; no se modela el ciclo completo ELI work/expression/manifestation."*

### 6.4. `plaza.search`

`inputSchema`:

```json
{ "type":"object", "additionalProperties":false,
  "required":["query"],
  "properties":{
    "query":{ "type":"string", "minLength":2, "maxLength":256 },
    "limit":{ "type":"integer", "minimum":1, "maximum":20, "default":5 } } }
```

`outputSchema.data`:

```json
{ "type":"object",
  "required":["query","results","ranking_method"],
  "properties":{
    "query":{ "type":"string" },
    "ranking_method":{ "type":"string", "const":"deterministic_lexical_score_v1" },
    "results":{
      "type":"array",
      "items":{
        "type":"object",
        "required":["uri","title","snippet","score","is_legal_truth"],
        "properties":{
          "uri":{ "type":"string" },
          "title":{ "type":"string" },
          "snippet":{ "type":"string" },
          "score":{ "type":"number" },
          "is_legal_truth":{ "const": false } } } } } }
```

`is_legal_truth: false` está cableado para forzar al cliente a no tratar el ranking como autoridad.

### 6.5. `plaza.get_relations`

`inputSchema`: `{ uri: string, direction?: "outgoing" | "incoming" | "both" }`.

`outputSchema.data`:

```json
{ "type":"object",
  "required":["subject","direction","relations"],
  "properties":{
    "subject":{ "type":"string" },
    "direction":{ "enum":["outgoing","incoming","both"] },
    "relations":{
      "type":"array",
      "items":{
        "type":"object",
        "required":["subject","predicate","object","direction","status","evidence"],
        "properties":{
          "subject":{ "type":"string" },
          "predicate":{ "type":"string", "description":"IRI completo (e.g. `eli:based_on` o `eli:basis_for`)" },
          "object":{ "type":"string" },
          "direction":{ "enum":["outgoing","incoming"] },
          "status":{ "enum":["canonical","reconciled_for_demo","candidate","review"] },
          "evidence":{
            "type":"object",
            "required":["evidence_type","source_artifact"],
            "properties":{
              "evidence_type":{ "enum":["scij_explicit_reference","scij_metadata_field","scij_text_match","plaza_demo_assertion"] },
              "source_artifact":{ "type":"string" },
              "hash":{ "type":["string","null"] },
              "source_url":{ "type":["string","null"] }
            }
          },
          "limitations":{ "type":"array","items":{"type":"string"} } } } } } }
```

**Decisión Plaza:** en Demo, **una sola** relación tiene `status: canonical` o `reconciled_for_demo`: la relación ley↔decreto: `eli:basis_for` desde la ley hacia el decreto y `eli:based_on` desde el decreto hacia la ley. Las demás relaciones del grafo, si las hubiera, deben aparecer con `status: candidate` o `review` y un aviso explícito en `warnings`.

### 6.6. `plaza.get_provenance`

`outputSchema.data`:

```json
{ "type":"object",
  "required":["uri","prov_chain"],
  "properties":{
    "uri":{ "type":"string" },
    "prov_chain":{
      "type":"array",
      "items":{
        "type":"object",
        "required":["activity","agent","used","generated","at_time"],
        "properties":{
          "activity":{ "enum":["acquisition","refinement","reconciliation","canonicalization"] },
          "agent":{ "type":"string" },
          "used":{ "type":"array","items":{"type":"string"} },
          "generated":{ "type":"array","items":{"type":"string"} },
          "at_time":{ "type":"string", "format":"date-time" },
          "hash_of_input":{ "type":["string","null"] },
          "hash_of_output":{ "type":["string","null"] } } } } } }
```

### 6.7. `plaza.get_graph`

`inputSchema`: `{ uri?: string, format?: "turtle" | "json-ld" }`. Si `uri` está ausente, devuelve el grafo Demo entero. Si presente, devuelve el CBD (Concise Bounded Description) del recurso.

`outputSchema.data`:

```json
{ "type":"object",
  "required":["format","content","triple_count","content_hash"],
  "properties":{
    "format":{ "enum":["turtle","json-ld"] },
    "content":{ "type":"string" },
    "triple_count":{ "type":"integer", "minimum":0 },
    "content_hash":{ "type":"string", "description":"SHA-256 del campo content." } } }
```

El servidor también expone el mismo contenido como **content type nativo** vía `content[]` en la respuesta MCP (`{ type: "resource", resource: { uri, mimeType: "text/turtle", text: "..." } }`), lo que permite al cliente parsearlo sin desempaquetar JSON.

### 6.8. `plaza.explain_resource`

`outputSchema.data`:

```json
{ "type":"object",
  "required":["uri","factual_explanation","scope_warnings"],
  "properties":{
    "uri":{ "type":"string" },
    "factual_explanation":{
      "type":"object",
      "required":["what_this_resource_is","what_demo_represents","what_demo_does_not_represent"],
      "properties":{
        "what_this_resource_is":{ "type":"string" },
        "what_demo_represents":{ "type":"string" },
        "what_demo_does_not_represent":{ "type":"string" } } },
    "scope_warnings":{ "type":"array","items":{"type":"string"} } } }
```

**Restricción dura:** `factual_explanation.*` se construye sólo a partir de plantillas fijas y datos del grafo. Está prohibido por diseño que esta herramienta produzca texto generativo.

---

## 7. Envoltorio de respuesta y modelo de citación

Toda respuesta exitosa de cualquier herramienta y de los recursos JSON usa el siguiente envoltorio canónico, que se publica como esquema reutilizable y se referencia desde cada `outputSchema`:

```json
{
  "ok": true,
  "data": { /* específico de la operación */ },
  "citations": [
    {
      "plaza_uri": "https://demo.plaza.cr/eli/cr/asamblea/1949/constitucion/politica",
      "source_system": "scij",
      "source_url": "https://...",
      "source_local_id": "scij:doc:N",
      "artifact_id": "scij/raw/2024-XX-XX/N.html",
      "hash": "sha256:...",
      "evidence_type": "scij_canonical_artifact",
      "timestamp": "2026-04-01T12:00:00Z"
    }
  ],
  "warnings":    ["..."],
  "limitations": ["No incluye reconciliación con La Gaceta.", "Demo: no representa la totalidad del ordenamiento jurídico costarricense."],
  "status": "ok",
  "generated_from_snapshot_or_graph": "demo.ttl",
  "demo_notice": "Demo Plaza. Las URIs https://demo.plaza.cr/eli/... no son URIs canónicas públicas de producción y no implican certificación oficial.",
  "errors": []
}
```

En errores, `ok = false`, `data = null`, `errors[]` se llena (ver §9), y `citations[]` puede estar vacío.

**Modelo de citación.** Una `citation` distingue cuatro categorías mediante `evidence_type`:

| `evidence_type` | Significado | Uso típico |
|---|---|---|
| `plaza_demo_resource_uri` | El URI del recurso Plaza-Demo que se está citando. | Siempre presente. |
| `scij_canonical_artifact` | Artefacto SCIJ preservado bit-exacto en almacenamiento Plaza. | `get_text`, `get_resource`. |
| `scij_local_identity` | Identificador interno del sistema fuente (e.g. `scij:doc:N`). | Trazabilidad cruzada. |
| `graph_triple_evidence` | Tripleta(s) que respaldan una relación. | `get_relations`. |

**Regla:** cada `citation` con `evidence_type ≠ plaza_demo_resource_uri` debe incluir `hash` cuando el artefacto fuente esté preservado localmente. Si no hay hash disponible, el campo `hash` debe ser `null` y `warnings[]` debe incluir `"citation_hash_missing"`.

---

## 8. Guardarraíles de no-interpretación

Los guardarraíles operan en **tres capas**: (a) descripciones de las tools, (b) plantillas fijas de texto en respuestas, (c) lista negra de campos generativos.

**Capa A — descripciones de tools (texto literal a usar):**

> *"plaza.get_text — Devuelve texto legal preservado del artefacto SCIJ asociado a un URI Plaza-Demo. **No interpreta**, **no resume**, **no actualiza** vigencia. El texto puede no corresponder a la versión vigente del recurso."*

> *"plaza.get_relations — Devuelve relaciones normativas representadas en el grafo Demo, con su evidencia. **No constituye certificación legal** ni prueba de aplicabilidad jurídica. El estado `candidate` o `review` indica relaciones no verificadas."*

> *"plaza.search — Búsqueda léxica determinística sobre el grafo Demo. **El ranking no expresa importancia jurídica**. Los snippets son extractos textuales sin interpretación."*

> *"plaza.explain_resource — Explica de forma factual qué representa un recurso en el grafo Demo y qué no representa. **No emite juicio jurídico**, no aconseja, no aplica la norma a casos."*

**Capa B — frases permitidas en respuestas (plantillas):**

| Permitido | Prohibido |
|---|---|
| "Este recurso está representado en el grafo Demo." | "Este recurso es legalmente correcto." |
| "Texto extraído de evidencia SCIJ preservada." | "Este es el texto vigente." |
| "Relación representada como `eli:basis_for` desde la ley hacia el decreto, o `eli:based_on` desde el decreto hacia la ley, con evidencia `scij_explicit_reference`." | "Este decreto reglamenta válidamente esta ley." |
| "URI `https://demo.plaza.cr/eli/...` — no es URI canónica pública de producción." | "URI oficial Plaza." |
| "Demo: una relación normativa real, cuatro recursos legales, sin reconciliación con La Gaceta." | "Cobertura completa del derecho costarricense." |
| "Estado de la relación: `candidate`. Requiere revisión." | "Esta relación prueba responsabilidad legal." |

**Capa C — lista negra absoluta.** Las siguientes acciones son rechazadas con error `legal_interpretation_request_rejected` (ver §9):

- Cualquier llamada cuyo `query` o argumento de texto contenga frases-trigger (lista mantenible) como *"¿es legal…?"*, *"qué debo hacer si…"*, *"¿se aplica esto a mi caso?"*, *"interpreta…"*, *"opina sobre…"*. La detección es heurística y conservadora.
- Toda construcción de texto con *templating dinámico libre* sobre datos del grafo. Las plantillas usadas en `explain_resource` son strings fijos con sustitución de campos atómicos (`{title}`, `{number}`, `{issuer}`).

**Decisión Plaza:** la heurística de la Capa C se documenta como configurable y **conservadora**: ante duda, el servidor responde con redirección a `plaza.explain_resource` y un `warnings[]` que indica *"consulta con apariencia de solicitud interpretativa; reformule en términos de datos del grafo"*. Este es el único caso en que el servidor "modera" entradas, y lo hace sin generar texto interpretativo.

---

## 9. Modelo de errores

Plaza adopta el espacio JSON-RPC 2.0 estándar más una región implementación-definida en `-32000..-32099`. Los errores de validación de input se devuelven como **Tool Execution Errors** (resultado JSON-RPC ok con `isError: true`) por alineamiento con SEP-1303 (`2025-11-25`). Los errores de protocolo (URI inválido a nivel de transporte, método desconocido) sí usan el espacio JSON-RPC.

| Código Plaza | Categoría | JSON-RPC | Como Tool Exec Error | Mensaje al usuario | Reintentable | Indica |
|---|---|---|---|---|---|---|
| `invalid_uri` | input | -32602 | sí | "URI Plaza-Demo inválido o mal formado." | no | error del cliente |
| `resource_not_found` | input | -32002 | sí | "Recurso no presente en grafo Demo." | no | error del cliente |
| `graph_not_loaded` | server | -32603 | no | "Grafo Demo no cargado en el servidor." | sí | error del servidor / arranque |
| `validation_report_missing` | server | -32603 | no | "Reporte SHACL ausente; servidor en modo cerrado." | no | error de despliegue |
| `validation_gate_failed` | server | -32603 | no | "Validación SHACL no conforme; servidor en modo cerrado." | no | error de datos |
| `unsupported_operation` | input | -32601 | no | "Operación no soportada en Demo." | no | error del cliente |
| `relation_not_found` | data | — | sí | "Sin relaciones registradas para el sujeto." | no | dato vacío |
| `provenance_missing` | data | — | sí | "Procedencia no disponible para el recurso indicado." | no | brecha de datos |
| `text_missing` | data | — | sí | "Texto preservado no disponible para el recurso." | no | brecha de datos |
| `source_artifact_unavailable` | data | — | sí | "Artefacto SCIJ no preservado o inaccesible." | no | brecha de datos |
| `demo_limitation` | scope | — | sí | "Operación fuera del alcance Demo." | no | scope |
| `internal_parse_error` | server | -32603 | no | "Error interno al parsear contenido." | sí | bug |
| `query_too_broad` | input | — | sí | "Consulta excesivamente amplia; afine los términos." | no | input |
| `result_truncated` | warning | — | resultado ok con `warnings[]` | "Resultado truncado por tamaño." | no | informativo |
| `non_deterministic_request_rejected` | input | — | sí | "Petición incompatible con determinismo del Demo." | no | scope |
| `legal_interpretation_request_rejected` | scope | — | sí | "Plaza no entrega interpretación legal. Consulte plaza.explain_resource." | no | scope |

Cada error incluye en `error.data` los campos `code` (string Plaza), `category` (string), `retryable` (bool) y, cuando aplica, `hint` (string sugerencia accionable factual no-interpretativa).

---

## 10. Arquitectura de runtime

El runtime es un único proceso que monta el siguiente *pipeline* en su `lifespan` de inicio:

1. **Carga de configuración.** Lee variable `PLAZA_DEMO_DIR` o por defecto `data/demo/`. Resuelve rutas absolutas a `canonical/demo.ttl`, `validation/validation_report.json`, opcionalmente `search/search_index.sqlite`.
2. **Lectura de la compuerta de validación.** Lee `validation_report.json`. Si no existe → error `validation_report_missing`, servidor inicia en *closed mode* (responde sólo errores de servidor a cualquier request operativo). Si `conforms == false` → `validation_gate_failed`, mismo *closed mode*. El estado se publica como recurso MCP `https://demo.plaza.cr/mcp/catalog/validation`.
3. **Parseo del Turtle.** Usa `rdflib.Graph().parse("canonical/demo.ttl", format="turtle")`. Falla → `internal_parse_error`, *closed mode*. Tras parseo:
   - Se *bind*-ean prefijos en orden alfabético determinístico (`eli`, `plaza`, `plazav`, `prov`, `skos`).
   - Se calcula `triple_count` y un `graph_hash` (SHA-256 sobre la serialización canónica `nquads` ordenada).
4. **Construcción de índices in-memory.**
   - Mapa `uri → metadata` para los 4 recursos Demo.
   - Mapa `uri → list[triple]` para CBD rápido.
   - Mapa `uri → list[relation]` con `predicate`, `object`, `direction`, `status`, `evidence`.
   - Mapa `uri → provenance_chain` derivado de tripletas PROV-O.
5. **Construcción del índice de búsqueda.** Si `search_index.sqlite` existe, se carga; si no, se construye en memoria (FTS5 simple sobre títulos, snippets de texto, e identificadores). El índice es función pura del grafo cargado, por lo que el servidor puede regenerarlo determinísticamente.
6. **Modo operativo.** Sólo entonces el servidor acepta `tools/list`, `resources/list`, `tools/call`, `resources/read`.

**Decisión Plaza:** ningún archivo se escribe durante la sesión. `search_index.sqlite`, si se materializa, se construye fuera del servidor (en una etapa de build) o en un directorio temporal del proceso, nunca dentro de `data/demo/`.

**Determinismo del output del grafo.** El serializador Turtle de `rdflib` no es estrictamente determinístico por defecto. Plaza fuerza determinismo así:
- Prefijos *bound* en orden fijo antes de serializar.
- Serialización a través de un wrapper que itera tripletas ordenadas por `(s, p, o)` y emite Turtle "canónico Plaza" (mismo escape, mismo agrupamiento por sujeto). El hash `content_hash` que reporta `plaza.get_graph` se calcula sobre esta forma canónica.
- Para `json-ld`, idéntica regla: contexto fijo, claves ordenadas, `@id` siempre antes de `@type`.

**Recomendación SDK:** Python con FastMCP. Razones técnicas:
- `rdflib` cubre Turtle, JSON-LD, N-Quads en una sola dependencia; `pyshacl` permite recomputar localmente la validación si se desea reforzar la compuerta. Esto está documentado en la guía oficial del Python SDK (`https://github.com/modelcontextprotocol/python-sdk`).
- FastMCP infiere `outputSchema` de tipos Python y emite `structuredContent` automáticamente para retornos *object-like*, lo que reduce el código boilerplate.
- Compatibilidad inmediata con Claude Desktop usando `uv run mcp run server.py`.
- TypeScript es viable pero el ecosistema RDF en Node es notoriamente más débil; sólo se justifica si Plaza migra a Workers/Deno post-Demo.

---

## 11. Recomendación de transporte

**Decisión Plaza:** transporte **stdio** para Demo. Justificación:

- La especificación es explícita: *"Clients SHOULD support stdio whenever possible"* (`https://modelcontextprotocol.io/specification/2025-11-25/basic/transports`). stdio es el ciudadano de primera clase para servidores locales.
- Claude Desktop usa stdio nativamente vía `claude_desktop_config.json` con campos `command`, `args`, `env`. No requiere proxy externo.
- Cero superficie de red: no hay puerto, no hay CORS, no hay validación de Origin, no hay autenticación. Esto cierra de facto categorías enteras de vulnerabilidad (DNS rebinding, token passthrough, hijack de sesión).
- El framing es JSON-RPC delimitado por *newline*, sin embebido de saltos de línea. La spec aclara en `2025-11-25` (PR #670) que stderr puede usarse para *cualquier* nivel de log; Plaza usa stderr para logging operacional (`logging.basicConfig(stream=sys.stderr)`).

**Comparación con Streamable HTTP** (transporte de red estándar actual, reemplaza al deprecado HTTP+SSE desde `2025-03-26`):

| Aspecto | stdio (Demo) | Streamable HTTP (post-Demo) |
|---|---|---|
| Topología | subproceso del host | servicio independiente |
| Auth | env vars (sin OAuth) | OAuth 2.1 + RFC 8707 + RFC 9728 |
| Sesión | implícita | `MCP-Session-Id` (UUID seguro) |
| Header obligatorio | n/a | `MCP-Protocol-Version: 2025-11-25` |
| Origin validation | n/a | obligatorio (HTTP 403 si inválido) |
| Bind | n/a | obligatorio `127.0.0.1` si local |

**Camino de evolución (no aplica al Demo).** Si Plaza decide post-Demo exponer MCP públicamente, la migración es: declarar segundo transporte Streamable HTTP, conservar stdio, añadir descubrimiento OAuth 2.1 con Protected Resource Metadata RFC 9728, fijar `resource indicator` RFC 8707, validar `Origin` y emitir 403 ante invalidez. La spec `2025-11-25` añade además OIDC discovery y consent incremental por scopes que se deben adoptar al hacerlo.

**Configuración de Claude Desktop sugerida (decisión recomendada):**

```json
{
  "mcpServers": {
    "plaza-demo": {
      "command": "uv",
      "args": ["run", "--with", "mcp[cli]", "--with", "rdflib", "--with", "pyshacl",
               "mcp", "run", "/abs/path/plaza/server.py"],
      "env": { "PLAZA_DEMO_DIR": "/abs/path/plaza/data/demo" }
    }
  }
}
```

Notas: rutas absolutas obligatorias (Claude Desktop no define `cwd`); logs en `~/Library/Logs/Claude/mcp-server-plaza-demo.log` (macOS), `%APPDATA%\Claude\logs\` (Windows).

---

## 12. Perfil de seguridad y privacidad

| Control | Demo Plaza | Justificación / fuente |
|---|---|---|
| Sólo lectura | obligatorio | No hay tools de mutación. Todas declaran `readOnlyHint: true`. |
| Sin acceso a red en tools | obligatorio | Ninguna tool abre sockets. SCIJ no se consulta en línea. |
| Sin scraping dinámico | obligatorio | Datos vienen de artefactos preservados, no de peticiones HTTP en vivo. |
| Sin lectura arbitraria de filesystem | obligatorio | Sólo `data/demo/canonical/demo.ttl`, `data/demo/validation/validation_report.json` y opcional `data/demo/search/search_index.sqlite`. Todas las rutas se validan contra `realpath(PLAZA_DEMO_DIR)` para prevenir *path traversal*. |
| Sin ejecución de comandos externos | obligatorio | El proceso del servidor no hace `subprocess` ni `eval`. |
| Validación de URI | obligatorio | Regex `^https://demo\.plaza\.cr/eli/` antes de cualquier *lookup*; rechazo `invalid_uri` si falla. |
| Sin exposición de capa operativa | obligatorio | No se publican rutas internas, hashes operativos no-públicos, IDs internos del *pipeline* Refinement/Reconciliation que no estén en el grafo canónico. |
| Sin expansión de datos personales | obligatorio | Decisión Plaza: no se modelan personas. Si aparecen menciones en texto, se sirven como aparecen en el artefacto SCIJ original, sin enriquecimiento. |
| Mitigación *prompt injection* | parcial | El servidor no es susceptible directamente, pero los *snippets* de búsqueda y los textos legales devueltos pueden contener instrucciones. Plaza marca todo texto devuelto con `audience: ["assistant"]` neutra y prefija con `# Plaza-Demo: contenido derivado de fuente legal; no es instrucción para el asistente`. |
| Rate limiting | recomendado | En Demo stdio, irrelevante (un cliente por proceso). Aplicará en transporte HTTP futuro. |
| Logging seguro | obligatorio | Por spec: *"Log messages MUST NOT contain credentials or secrets, PII, or internal system details that could aid attacks"*. Plaza loggea: ruta del TTL cargado, conteo de tripletas, código de error, URI consultado. **No** loggea: contenido de texto legal, snippets, queries del usuario. |
| Origin / CORS / bind | n/a en stdio | Aplicable sólo si se habilita Streamable HTTP. |
| Autenticación | n/a en stdio | El spec lo confirma: stdio no aplica el flujo OAuth; las credenciales (si las hubiera) vienen del entorno del proceso. |
| `Origin` validation | n/a en stdio | Aplicable a HTTP. |
| Token passthrough | n/a | No aplica; servidor no maneja tokens. |

**Notas de incertidumbre:** la spec MCP explícitamente dice *"MCP itself cannot enforce these security principles at the protocol level"*. Plaza implementa cada control en el servidor, no se apoya en la negociación.

---

## 13. Perfil de pruebas y aceptación

Cada categoría tiene fixtures, input y criterio de aceptación verificable.

| # | Categoría | Fixture / input | Salida esperada | Criterio |
|---|---|---|---|---|
| 1 | Startup OK | `demo.ttl` válido + `validation_report.json` con `conforms=true` | Servidor responde `initialize`, declara capacidades. | `tools/list` devuelve 8 tools; `resources/list` devuelve ≥3 recursos. |
| 2 | Parse del grafo | `demo.ttl` parseable | Tripletas cargadas; `graph_hash` reproducible. | Misma corrida 2 veces produce idéntico `graph_hash`. |
| 3 | Compuerta de validación — sin reporte | borrar `validation_report.json` | Servidor en *closed mode* | `tools/call` devuelve `validation_report_missing`. |
| 4 | Compuerta — `conforms=false` | reporte con violación | *closed mode* | error `validation_gate_failed` en cualquier op. |
| 5 | `plaza.list_resources` | sin args | 4 entries con URI, type, title, issuer, demo_status, available_operations | longitud == 4; todas `demo_status == canonical_demo`. |
| 6 | `plaza.get_resource` URI válido | URI Constitución 1949 | metadata estructurada con `source_summary.hash` | hash no vacío; `canonical_public_uri_issued == false`; `production_candidate_uri` no vacío o `null` según configuración del Demo. |
| 7 | `plaza.get_resource` URI inválido | `https://demo.plaza.cr/invalid` | tool exec error `invalid_uri` | `isError: true`, `code == invalid_uri`. |
| 8 | `plaza.get_resource` URI no existe | `https://demo.plaza.cr/eli/cr/asamblea/9999/ley/9999` | tool exec error `resource_not_found` | `code == resource_not_found`. |
| 9 | `plaza.get_text` | URI ley | texto + hash + `expression_distinction` | hash coincide con artefacto SCIJ preservado. |
| 10 | `plaza.search` simple | `query: "constitución"` | resultados deterministas | dos ejecuciones idénticas → mismo orden y scores. |
| 11 | `plaza.search` query muy amplio | `query: "a"` | error `query_too_broad` | `code == query_too_broad`. |
| 12 | `plaza.get_relations` | URI ley con relación a decreto | 1 relación canónica `eli:basis_for` desde la ley hacia el decreto, o `eli:based_on` desde el decreto hacia la ley | `status ∈ {canonical, reconciled_for_demo}`; `evidence.evidence_type == scij_explicit_reference`. |
| 13 | `plaza.get_relations` sin relaciones | URI Constitución | tool exec error `relation_not_found` | `isError: true`. |
| 14 | `plaza.get_provenance` | URI ley | cadena PROV-O con 4 actividades en orden | `prov_chain[*].activity` cubre acquisition→canonicalization. |
| 15 | `plaza.get_provenance` faltante | recurso sin PROV-O | `provenance_missing` | `code == provenance_missing`. |
| 16 | `plaza.get_graph` global | sin args | Turtle parseable | `triple_count > 0`; `rdflib.Graph().parse(data=content, format="turtle")` no lanza. |
| 17 | `plaza.get_graph` recurso | URI ley | CBD Turtle | sólo tripletas con sujeto = URI o blank node alcanzable. |
| 18 | `plaza.explain_resource` | URI ley | factual_explanation con plantilla fija | no contiene tokens prohibidos (lista de Capa B). |
| 19 | No-interpretación | tool call con `query: "¿es legal el aborto en CR?"` | redirección o `legal_interpretation_request_rejected` | no hay generación de texto interpretativo. |
| 20 | Determinismo | misma llamada 2× | byte-equivalent | `data` y `content_hash` idénticos. |
| 21 | Citation completeness | toda respuesta exitosa | `citations[]` no vacío | cada item con `plaza_uri` + al menos uno con `evidence_type != plaza_demo_resource_uri`. |
| 22 | Texto largo / truncado | `range` que pide >límite | `is_truncated: true` + `warnings: ["result_truncated"]` | bytes devueltos == límite. |
| 23 | Path traversal | no hay vector externo | n/a | revisión de código: `realpath` y allowlist. |
| 24 | URI fuera de esquema | `file:///etc/passwd` como URI | `invalid_uri` | rechazo en regex. |

---

## 14. Guía para consumidores AI

El servidor publica para cada cliente LLM tres canales de contrato: (a) el campo `instructions` del `InitializeResult`, (b) las `description` de cada tool, (c) los avisos en cada respuesta (`warnings`, `limitations`, `demo_notice`).

**Texto del `instructions` (primer canal):**

> *"Servidor de datos legales costarricenses en modo Demo. Sólo lectura. Cuatro recursos legales reales y una relación normativa real. Citá siempre las URIs `https://demo.plaza.cr/eli/...`. No es asistente legal. No interpretás, no resumís, no aconsejás. Las relaciones con `status: candidate` o `review` no son verdad jurídica. Si Plaza no provee vigencia, no la inferís. Mostrá las limitaciones del Demo al usuario."*

**Reglas de comportamiento esperadas del cliente LLM (recomendaciones, no obligación protocolar):**

- Tratar todo `data` como **fuente de hecho preservada**, no como afirmación del modelo.
- Citar el `plaza_uri` y el `source_url` (cuando existe) en la respuesta al usuario final.
- **No** afirmar vigencia, derogación o aplicabilidad si Plaza no la entrega explícitamente como atributo.
- **No** convertir resultados de `plaza.search` en jerarquía de autoridad; el campo `is_legal_truth: false` está cableado para impedirlo.
- Mostrar al usuario el `demo_notice` literal en al menos la primera respuesta de la sesión.
- Distinguir `status: canonical` de `status: candidate`/`review` al verbalizar relaciones.

**Sobre los hints de tools (`readOnlyHint`, `idempotentHint`, etc.):** la spec advierte que el cliente **debe** tratarlos como *untrusted* salvo servidor confiable. Esto no afecta el diseño Plaza pero el equipo del cliente debe configurar a Plaza como servidor confiable explícitamente en su política.

---

## 15. Evolución futura post-Demo

Las siguientes capacidades **no** se implementan en Demo y se listan como hoja de ruta:

- Servicio MCP público sobre **Streamable HTTP**, con OAuth 2.1, RFC 8707 *resource indicators*, RFC 9728 *Protected Resource Metadata* y descubrimiento OIDC (todos exigidos por la spec MCP `2025-11-25` para servidores HTTP).
- API REST coexistiendo con MCP — explicitamente **no** en Demo.
- Snapshots versionados expuestos vía DCAT.
- Salida JSON-LD canónica como representación primaria, no derivada al vuelo.
- Reconciliación con La Gaceta como evidencia de publicación oficial.
- Más recursos legales (más leyes, más decretos, normativa secundaria).
- Recursos a nivel de artículo (`https://demo.plaza.cr/eli/.../articulo/12`).
- Expansión de relaciones: `eli:repeals`, `eli:amends`, `eli:cites`, modelo SKOS de jerarquías.
- Autenticación por cliente y *rate limits* per token.
- Despliegue *hosted* en infraestructura Plaza con `MCP-Session-Id` rotativo.
- Adopción de `prompts` MCP para flujos curados de consulta legal.
- Estudio de `tasks` (experimental en `2025-11-25`) para consultas de larga duración cuando Plaza incorpore SPARQL federado.

Cada elemento queda fuera del alcance Demo y es decisión del proyecto.

---

## 16. Registro de riesgos de implementación

| Riesgo | Categoría | Severidad | Mitigación Plaza |
|---|---|---|---|
| Cliente LLM trata `plaza.search` como autoridad legal. | Misuse | alta | `is_legal_truth: false` cableado; `description` y `warnings` lo indican. |
| LLM "rellena" vigencia ausente. | Misuse | alta | `instructions` y `description` prohíben la inferencia; `limitations[]` lo declara. |
| Snippets contienen *prompt injection*. | Seguridad | media | Prefijo neutro a cada snippet; `audience: ["assistant"]` no se usa para inducir comportamiento. |
| `rdflib` cambia el orden de prefijos entre versiones. | Determinismo | media | *Wrapper* de serialización canónica Plaza, hash sobre forma canónica. |
| Validación SHACL ausente en producción local. | Datos | alta | Compuerta cerrada al arrancar. |
| Path traversal vía URI manipulado. | Seguridad | baja | URI validado por regex; rutas físicas resueltas con `realpath` y allowlist. |
| Cambios en spec MCP en próxima revisión. | Compatibilidad | media | Soporte dual `2025-11-25` y `2025-06-18`; versión negociada en `initialize`. |
| Cliente sólo soporta `2024-11-05`. | Compatibilidad | baja | Plaza puede aceptar pero advierte que algunas capacidades (structured output, elicitation) no aplican. |
| Texto legal grande supera límite de contexto del cliente. | UX | media | `range` en `plaza.get_text`, `is_truncated` y `warnings: ["result_truncated"]`; `resource_link` para fetch lazy. |
| Hash del artefacto fuente no preservado. | Datos | media | `hash: null` + `warnings: ["citation_hash_missing"]`. |
| Discrepancia entre `outputSchema` declarado y `structuredContent` emitido. | Conformidad | baja | Tests de conformidad por tool (categoría 21). |
| Cliente reenvía datos de Plaza a servicios externos sin consentimiento. | Privacidad | media | Fuera del control del servidor; `demo_notice` incluye recordatorio. |

---

## 17. Preguntas abiertas que requieren decisión del proyecto

1. **¿`https://demo.plaza.cr/mcp/graph/main.jsonld` se sirve en Demo o se difiere?** Implementar JSON-LD requiere fijar el `@context` Plaza y un orden canónico. Recomendación: incluir en Demo si y solo si el `@context` ya está aprobado en `STANDARDS_IMPLEMENTATION_PROFILE`; de lo contrario, diferir.

2. **¿Se materializa `data/demo/search/search_index.sqlite` en disco o se construye en memoria al arranque?** En memoria simplifica el contrato (índice = función pura del grafo); en disco acelera arranques repetidos. Recomendación: en memoria en Demo.

3. **¿La heurística de detección de "consulta interpretativa" en `plaza.search` se incluye en Demo o se difiere?** Es la única lógica de moderación de input. Recomendación: incluir como lista mínima de triggers y comportamiento conservador; documentar como configurable.

4. **¿Qué cuarta pieza legal compone el set de 4 recursos?** El brief menciona "cuatro recursos legales" pero no los enumera taxativamente. Decisión del equipo de datos.

5. **¿El servidor publica `instructions` literales o también una versión más larga como recurso `https://demo.plaza.cr/mcp/catalog/demo_notice`?** Recomendación: ambos.

6. **¿Se acepta exponer `pyshacl` como dependencia del runtime MCP, o sólo como dependencia de la fase Refinement/Validation?** Recomendación: el runtime MCP **no** valida; sólo lee `validation_report.json`. `pyshacl` no es dependencia del servidor.

7. **¿Plaza fija una política de *content type* para `resources/read` cuando el cliente no envía `Accept`?** La spec no exige negociación de contenido en `resources/read`; cada URI declara su propio `mimeType`. Recomendación: una URI por representación, sin negociación.

8. **¿Se declara `resources.subscribe = true` para futura compatibilidad o se deja en `false`?** Recomendación: `false` en Demo; activarlo cuando exista un caso real de cambio en sesión.

9. **¿Plaza adopta el patrón `resource_link` en respuestas de tools para manejar texto grande?** Recomendación: sí, pero como mecanismo opcional; Demo expone `range` directo en `plaza.get_text`.

10. **¿Soporte de SDK Python `1.25.x` o congelar versión? ¿Qué política de actualización?** Recomendación: congelar minor durante Demo, revisar trimestralmente.

---

## 18. Apéndice A — Ejemplos de respuestas de tools

### A.1. `plaza.list_resources` — respuesta exitosa

```json
{
  "ok": true,
  "data": [
    {
      "uri": "https://demo.plaza.cr/eli/cr/asamblea/1949/constitucion/politica",
      "type": "constitucion",
      "title": "Constitución Política de la República de Costa Rica",
      "issuer": "Asamblea Nacional Constituyente",
      "demo_status": "canonical_demo",
      "available_operations": ["get_resource","get_text","get_graph","get_relations","get_provenance","explain_resource"]
    },
    {
      "uri": "https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN",
      "type": "ley",
      "title": "Ley NNNN de YYYY",
      "issuer": "Asamblea Legislativa",
      "demo_status": "canonical_demo",
      "available_operations": ["get_resource","get_text","get_graph","get_relations","get_provenance","explain_resource"]
    }
    /* ... 2 más ... */
  ],
  "citations": [
    { "plaza_uri":"https://demo.plaza.cr/eli/cr/asamblea/1949/constitucion/politica",
      "source_system":"scij","evidence_type":"plaza_demo_resource_uri" }
    /* una por recurso */
  ],
  "warnings": [],
  "limitations": [
    "Demo: cuatro recursos legales reales; no representa la totalidad del ordenamiento jurídico costarricense.",
    "Las URIs https://demo.plaza.cr/eli/... no son URIs canónicas públicas de producción."
  ],
  "status": "ok",
  "generated_from_snapshot_or_graph": "demo.ttl",
  "demo_notice": "Demo Plaza. Sin reconciliación con La Gaceta. Sin certificación oficial."
}
```

### A.2. `plaza.get_relations` — respuesta exitosa

```json
{
  "ok": true,
  "data": {
    "subject": "https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN",
    "direction": "outgoing",
    "relations": [
      {
        "subject": "https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN",
        "predicate": "http://data.europa.eu/eli/ontology#basis_for",
        "object": "https://demo.plaza.cr/eli/cr/poder_ejecutivo/YYYY/decreto_ejecutivo/MMMM",
        "direction": "outgoing",
        "status": "canonical",
        "evidence": {
          "evidence_type": "scij_explicit_reference",
          "source_artifact": "scij/raw/2026-XX/decree-MMMM.html",
          "hash": "sha256:...",
          "source_url": null
        },
        "limitations": []
      }
    ]
  },
  "citations": [
    { "plaza_uri":"https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN", "source_system":"scij","evidence_type":"plaza_demo_resource_uri" },
    { "plaza_uri":"https://demo.plaza.cr/eli/cr/poder_ejecutivo/YYYY/decreto_ejecutivo/MMMM", "source_system":"scij","evidence_type":"plaza_demo_resource_uri" },
    { "plaza_uri":"https://demo.plaza.cr/eli/cr/poder_ejecutivo/YYYY/decreto_ejecutivo/MMMM",
      "source_system":"scij","artifact_id":"scij/raw/2026-XX/decree-MMMM.html","hash":"sha256:...",
      "evidence_type":"scij_canonical_artifact" }
  ],
  "warnings": [],
  "limitations": ["Una sola relación normativa real en Demo."],
  "status": "ok",
  "generated_from_snapshot_or_graph": "demo.ttl",
  "demo_notice": "Demo Plaza."
}
```

### A.3. `plaza.search` — query genérica

```json
{
  "ok": true,
  "data": {
    "query": "constitución política",
    "ranking_method": "deterministic_lexical_score_v1",
    "results": [
      { "uri":"https://demo.plaza.cr/eli/cr/asamblea/1949/constitucion/politica",
        "title":"Constitución Política de la República de Costa Rica",
        "snippet":"...",
        "score": 0.97,
        "is_legal_truth": false }
    ]
  },
  "citations": [/* ... */],
  "warnings": ["El ranking no expresa autoridad jurídica."],
  "limitations": ["Búsqueda léxica determinística sobre 4 recursos Demo."],
  "status": "ok",
  "generated_from_snapshot_or_graph": "demo.ttl",
  "demo_notice": "Demo Plaza."
}
```

### A.4. Tool execution error — interpretación legal solicitada

Respuesta JSON-RPC 2.0 exitosa con `isError: true`:

```json
{
  "jsonrpc":"2.0","id":42,
  "result":{
    "isError": true,
    "content":[{ "type":"text",
      "text":"{\"ok\":false,\"errors\":[{\"code\":\"legal_interpretation_request_rejected\",\"category\":\"scope\",\"retryable\":false,\"hint\":\"Use plaza.explain_resource o plaza.get_text con una URI https://demo.plaza.cr/eli/... específica.\"}],\"demo_notice\":\"Plaza Demo no entrega interpretación legal.\"}"
    }],
    "structuredContent":{
      "ok": false,
      "data": null,
      "errors": [{
        "code":"legal_interpretation_request_rejected",
        "category":"scope",
        "retryable": false,
        "hint":"Use plaza.explain_resource o plaza.get_text con una URI https://demo.plaza.cr/eli/... específica."
      }],
      "demo_notice":"Plaza Demo no entrega interpretación legal."
    }
  }
}
```

---

## 19. Apéndice B — Ejemplos de representaciones de recursos

### B.1. `resources/read` sobre `https://demo.plaza.cr/mcp/graph/main`

```json
{ "jsonrpc":"2.0","id":7,
  "result":{
    "contents":[
      { "uri":"https://demo.plaza.cr/mcp/graph/main",
        "mimeType":"text/turtle",
        "text":"@prefix plaza: <https://plaza.cr/ontology#> .\n@prefix plazav: <https://plaza.cr/vocab/> .\n@prefix eli: <http://data.europa.eu/eli/ontology#> .\n@prefix prov: <http://www.w3.org/ns/prov#> .\n\n<https://demo.plaza.cr/eli/cr/asamblea/1949/constitucion/politica>\n  a eli:LegalResource ;\n  eli:type_document plazav:constitucion ;\n  eli:passed_by plazav:emisor/asamblea_constituyente ;\n  ... ."
      }
    ] } }
```

### B.2. `resources/read` sobre plantilla expandida `https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN/provenance`

```json
{ "jsonrpc":"2.0","id":8,
  "result":{
    "contents":[
      { "uri":"https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN/provenance",
        "mimeType":"application/json",
        "text":"{\"uri\":\"https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN\",\"prov_chain\":[{\"activity\":\"acquisition\",\"agent\":\"plaza:scij_acquirer\",\"used\":[\"https://...\"],\"generated\":[\"scij/raw/2026-XX/law-NNNN.html\"],\"at_time\":\"2026-04-01T10:00:00Z\",\"hash_of_output\":\"sha256:...\"},{\"activity\":\"refinement\",\"agent\":\"plaza:refiner\",\"used\":[\"scij/raw/...\"],\"generated\":[\"scij/refined/...\"],\"at_time\":\"2026-04-01T10:05:00Z\"},{\"activity\":\"reconciliation\",\"agent\":\"plaza:reconciler\",\"used\":[\"scij/refined/...\"],\"generated\":[\"https://demo.plaza.cr/eli/cr/asamblea/YYYY/ley/NNNN\"],\"at_time\":\"2026-04-01T10:10:00Z\"},{\"activity\":\"canonicalization\",\"agent\":\"plaza:canonicalizer\",\"used\":[\"...\"],\"generated\":[\"data/demo/canonical/demo.ttl\"],\"at_time\":\"2026-04-01T10:15:00Z\"}]}"
      }
    ] } }
```

### B.3. `resources/templates/list`

```json
{ "jsonrpc":"2.0","id":9,
  "result":{
    "resourceTemplates":[
      { "uriTemplate":"https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}",
        "name":"plaza_law", "title":"Ley de la Asamblea Legislativa",
        "description":"Recurso legal de tipo ley emitido por la Asamblea Legislativa de Costa Rica.",
        "mimeType":"application/json" },
      { "uriTemplate":"https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}/text",
        "name":"plaza_law_text", "title":"Texto de una ley",
        "mimeType":"text/plain" },
      { "uriTemplate":"https://demo.plaza.cr/eli/cr/asamblea/{año}/ley/{número}/turtle",
        "name":"plaza_law_turtle", "title":"Subgrafo Turtle de una ley",
        "mimeType":"text/turtle" },
      { "uriTemplate":"https://demo.plaza.cr/eli/cr/poder_ejecutivo/{año}/decreto_ejecutivo/{número}",
        "name":"plaza_decree", "mimeType":"application/json" }
      /* ... */
    ] } }
```

---

## 20. Apéndice C — Ejemplos de consultas de cliente

### C.1. Inicialización (cliente → servidor)

```json
{ "jsonrpc":"2.0","id":1,"method":"initialize",
  "params":{
    "protocolVersion":"2025-11-25",
    "capabilities":{},
    "clientInfo":{ "name":"plaza-demo-client","version":"0.1.0" } } }
```

Respuesta del servidor: ver §5.

Notificación `initialized`: `{"jsonrpc":"2.0","method":"notifications/initialized"}`.

### C.2. Listar tools

```json
{ "jsonrpc":"2.0","id":2,"method":"tools/list" }
```

### C.3. Llamar `plaza.get_resource`

```json
{ "jsonrpc":"2.0","id":3,"method":"tools/call",
  "params":{
    "name":"plaza.get_resource",
    "arguments":{ "uri":"https://demo.plaza.cr/eli/cr/asamblea/1949/constitucion/politica" } } }
```

### C.4. Leer recurso Turtle global

```json
{ "jsonrpc":"2.0","id":4,"method":"resources/read",
  "params":{ "uri":"https://demo.plaza.cr/mcp/graph/main" } }
```

### C.5. Llamar `plaza.search`

```json
{ "jsonrpc":"2.0","id":5,"method":"tools/call",
  "params":{
    "name":"plaza.search",
    "arguments":{ "query":"decreto reglamentario","limit":3 } } }
```

### C.6. Subscribir a `notifications/message` (logging)

```json
{ "jsonrpc":"2.0","id":6,"method":"logging/setLevel","params":{"level":"info"} }
```

### C.7. Llamar `plaza.explain_resource`

```json
{ "jsonrpc":"2.0","id":10,"method":"tools/call",
  "params":{
    "name":"plaza.explain_resource",
    "arguments":{ "uri":"https://demo.plaza.cr/eli/cr/poder_ejecutivo/YYYY/decreto_ejecutivo/MMMM" } } }
```

Respuesta esperada (extracto, `data.factual_explanation`):

```json
{
  "what_this_resource_is": "Decreto ejecutivo número MMMM emitido en YYYY por el Poder Ejecutivo de Costa Rica, representado en el grafo Demo de Plaza.",
  "what_demo_represents": "Metadatos estructurados, texto preservado de evidencia SCIJ, una relación normativa hacia la ley NNNN/YYYY con evidencia explícita, y procedencia PROV-O de las cuatro actividades del pipeline.",
  "what_demo_does_not_represent": "No representa vigencia actual, derogaciones, modificaciones posteriores, ni publicación oficial en La Gaceta. La URI https://demo.plaza.cr/eli/... no es URI canónica pública de producción. Plaza no certifica ni interpreta este recurso."
}
```

---

## 21. Apéndice D — Enlaces fuente

### Especificación oficial

- Spec landing (revisión vigente): `https://modelcontextprotocol.io/specification/2025-11-25`
- Changelog 2025-11-25: `https://modelcontextprotocol.io/specification/2025-11-25/changelog`
- Architecture: `https://modelcontextprotocol.io/specification/2025-11-25/architecture`
- Base / JSON-RPC: `https://modelcontextprotocol.io/specification/2025-11-25/basic`
- Lifecycle: `https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle`
- Transports: `https://modelcontextprotocol.io/specification/2025-11-25/basic/transports`
- Authorization: `https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization`
- Security best practices (revisión 2025-06-18, vigente referencialmente): `https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices`
- Resources: `https://modelcontextprotocol.io/specification/2025-11-25/server/resources`
- Tools: `https://modelcontextprotocol.io/specification/2025-11-25/server/tools`
- Prompts: `https://modelcontextprotocol.io/specification/2025-11-25/server/prompts`
- Pagination: `https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/pagination`
- Logging: `https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/logging`
- Completion: `https://modelcontextprotocol.io/specification/2025-11-25/server/utilities/completion`
- Roots: `https://modelcontextprotocol.io/specification/2025-11-25/client/roots`
- Sampling: `https://modelcontextprotocol.io/specification/2025-11-25/client/sampling`
- Elicitation: `https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation`
- Tasks (experimental): `https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks`
- Schema reference: `https://modelcontextprotocol.io/specification/2025-11-25/schema`
- Esquema TypeScript canónico: `https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.ts`

### Repositorios oficiales y SDKs

- Organización GitHub: `https://github.com/modelcontextprotocol`
- Repositorio canónico de spec/docs: `https://github.com/modelcontextprotocol/modelcontextprotocol`
- Releases de spec: `https://github.com/modelcontextprotocol/modelcontextprotocol/releases`
- Python SDK: `https://github.com/modelcontextprotocol/python-sdk`
- Python SDK docs site: `https://modelcontextprotocol.github.io/python-sdk/`
- Python SDK on PyPI: `https://pypi.org/project/mcp/`
- TypeScript SDK: `https://github.com/modelcontextprotocol/typescript-sdk`
- TypeScript SDK API docs (v1): `https://ts.sdk.modelcontextprotocol.io/`
- TypeScript SDK on npm: `https://www.npmjs.com/package/@modelcontextprotocol/sdk`

### Documentación de hosts / clientes

- Conexión a servidores locales (Claude Desktop): `https://modelcontextprotocol.io/docs/develop/connect-local-servers`
- Claude Code MCP docs: `https://code.claude.com/docs/en/mcp`

### Blog oficial MCP

- Aniversario 2025-11-25: `https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/`
- Roadmap 2026: `https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/`
- Tool annotations: `https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/`

### Estándares normativamente referenciados

- JSON-RPC 2.0: `https://www.jsonrpc.org/specification`
- RFC 3986 (URI): `https://datatracker.ietf.org/doc/html/rfc3986`
- RFC 5424 (syslog severity): `https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1`
- RFC 6570 (URI templates): `https://datatracker.ietf.org/doc/html/rfc6570`
- RFC 7591 (Dynamic Client Registration): `https://datatracker.ietf.org/doc/html/rfc7591`
- RFC 8414 (OAuth 2.0 Authorization Server Metadata): `https://datatracker.ietf.org/doc/html/rfc8414`
- RFC 8707 (Resource Indicators): `https://datatracker.ietf.org/doc/html/rfc8707`
- RFC 9728 (Protected Resource Metadata): `https://datatracker.ietf.org/doc/html/rfc9728`
- OAuth 2.1 (draft-ietf-oauth-v2-1-13): `https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13`
- JSON Schema 2020-12: `https://json-schema.org/specification-links#2020-12`

### Notas de incertidumbre

- La validación cruzada entre la afirmación *"el SDK Python `1.25.x` soporta plenamente la negociación de `protocolVersion: 2025-11-25`"* y el código real del SDK no se realizó línea por línea; se infirió de los release notes de PyPI y del estado paralelo del SDK Java. El equipo Plaza debe verificar contra el `CHANGELOG.md` del Python SDK al congelar versión.
- El subdominio histórico `spec.modelcontextprotocol.io` parece haber sido absorbido en `modelcontextprotocol.io/specification/...`; cualquier enlace residual a `spec.modelcontextprotocol.io` debe redirigir.
- La heurística de Capa C (§8) es decisión Plaza; la spec MCP no la exige.
- El comportamiento de serialización canónica Turtle por encima de `rdflib` es decisión Plaza; no hay un canónico oficial RDF de uso obligatorio en MCP.
