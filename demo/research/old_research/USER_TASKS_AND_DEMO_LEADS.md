# Plaza — User Tasks and Demo Leads

**Estado:** memoria de investigación.
**No define producto consumer-facing.** Plaza sigue siendo capa de datos. Este documento traduce insights de SCIJ/user needs en criterios para probar y demostrar el funcionamiento de la nueva Plaza.

---

## Tesis destilada

Legacy research sobre “SCIJ parity” dejó una idea útil:

> Paridad con SCIJ no significa copiar la interfaz de SCIJ. Significa cubrir los comportamientos jurídicamente importantes que SCIJ habilita.

La nueva Plaza debe demostrar esos comportamientos como data layer:

- identidad estable;
- consulta por norma/artículo;
- versiones temporales;
- relaciones entre normas;
- publicación/fuente;
- procedencia verificable;
- incertidumbre declarada;
- export/consumo por sistemas.

---

## Tareas reales que Plaza debe habilitar

| Tarea de usuario | Traducción Plaza | Qué debe poder probarse |
|---|---|---|
| “Necesito saber qué dice esta ley ahora.” | Resolver URI canónica vigente. | URI sin versión devuelve/identifica versión vigente con metadata. |
| “Necesito saber qué decía el artículo X en una fecha.” | Resolver LegalExpression de artículo con versión temporal. | URI con `/articulo/{n}/version/{date}` o equivalente devuelve texto correcto/evidencia. |
| “Necesito saber qué reformó esta norma.” | Navegar relaciones de afectación. | `eli:amends`, `eli:repeals`, `eli:changes` o issue si no es resoluble. |
| “Necesito saber qué normas reglamentan esta ley.” | Navegar relaciones de reglamentación. | `eli:applies` o relación Plaza documentada con fuente. |
| “Necesito ver concordancias/citas.” | Exponer vínculos con tipo claro. | Diferenciar cita directa, concordancia temática y relación jurídica fuerte. |
| “Necesito confiar en la fuente.” | Mostrar procedencia. | Artefacto fuente, URL, timestamp, hash, parser/activity. |
| “Necesito saber dónde se publicó.” | Publication hint o publication event verificado. | SCIJ hint separado de Gaceta verified event. |
| “Necesito saber si esto es completo.” | Health/coverage metadata. | Conteos, issues, missing/excluded/review states. |
| “Necesito consumir esto en otro sistema.” | Snapshots/API/MCP/DCAT. | JSON-LD/Turtle/snapshot con URIs estables. |
| “Necesito citarlo.” | URI permanente por norma/versión/artículo. | URI citable y dereferenceable. |

---

## Comportamientos SCIJ relevantes

SCIJ aporta valor no por su UI sino por estas capacidades:

1. Norm-centric browsing.
2. Texto completo.
3. Ficha de norma.
4. Version banners.
5. Afectaciones.
6. Normativa que afectó.
7. Concordancias.
8. Reglamentaciones.
9. Descriptores.
10. Pronunciamientos PGR.
11. Acciones constitucionales.
12. Observaciones.
13. Datos de publicación.
14. Búsqueda libre/selectiva/temática.
15. Normas usuales/colecciones.

Plaza no necesita reproducir la interfaz tabular. Necesita conservar los datos, relaciones, procedencia y estados que hacen útiles esas tabs.

---

## Demo behavior set

Para una demo ejemplar de Plaza nueva, usar un set pequeño pero realista que demuestre futuro funcionamiento sin placeholders inútiles.

### Demo 1 — Resolver norma

**Pregunta:** “Dame la Ley X.”

Debe mostrar:

- URI canónica Plaza/ELI;
- tipo de norma;
- número;
- emisor;
- fecha de emisión/vigencia si está verificada;
- estado;
- fuente SCIJ;
- nivel de verificación.

No debe mostrar:

- UI consumer-facing compleja;
- interpretación legal;
- campos inventados.

### Demo 2 — Resolver versión vigente

**Pregunta:** “¿Cuál es la versión vigente?”

Debe mostrar:

- LegalResource permanente;
- LegalExpression vigente;
- marker de versión SCIJ si aplica;
- `is_current` o equivalente con evidencia;
- si la fecha de vigencia está verificada o inferida.

### Demo 3 — Resolver versión histórica

**Pregunta:** “¿Qué decía esta norma/artículo en fecha Y?”

Debe mostrar:

- URI de versión;
- texto de la versión;
- fecha de inicio de vigencia de la expresión;
- fuente del texto;
- estado si no existe una versión exacta.

Regla: no aproximar silenciosamente una fecha si la URI exacta no resuelve.

### Demo 4 — Artículo como entidad

**Pregunta:** “Dame el artículo 42.”

Debe mostrar:

- URI del artículo;
- URI de versión del artículo;
- texto;
- relación con norma contenedora;
- evidencia del texto.

### Demo 5 — Relación de reforma/derogación

**Pregunta:** “¿Qué normas modifican esta?”

Debe mostrar:

- relación tipada;
- dirección correcta;
- source surface SCIJ;
- raw evidence;
- si ambos extremos son canónicos;
- si la relación está canonicalizada o solo candidata.

### Demo 6 — Publicación oficial / Gaceta

**Pregunta:** “¿Dónde se publicó?”

Debe distinguir:

- `publication_hint` desde SCIJ;
- `publication_event_verified` desde La Gaceta;
- conflicto o ausencia;
- edición/alcance/página si existe.

### Demo 7 — Observación o hook interpretativo

**Pregunta:** “¿Hay pronunciamientos/acciones constitucionales relacionados?”

Debe mostrar:

- hooks como referencias;
- no convertirlos en corpus completo;
- no interpretar su efecto salvo relación explícita.

### Demo 8 — Honestidad operativa

**Pregunta:** “¿Qué falta o está dudoso?”

Debe mostrar:

- issues de reconciliación;
- campos missing;
- relations `review_needed`;
- source not yet habilitated;
- material excluded.

Esta demo es crucial: muestra que Plaza no finge certeza.

---

## Métricas útiles para demo/MVP

| Métrica | Uso |
|---|---|
| Normas canonicalizadas | Tamaño real del corpus publicable. |
| Normas en reconciliación | Trabajo pendiente sin esconder. |
| Version coverage | Capacidad temporal. |
| Article coverage | Granularidad citable. |
| Relationship coverage | Grafo legal útil. |
| Publication hint coverage | Pistas de publicación. |
| Gaceta verified publication coverage | Verificación oficial real. |
| Raw evidence completeness | Trazabilidad. |
| SHACL pass/fail | Validez estructural. |
| Reconciliation issue count | Honestidad de conflictos. |
| Excluded/private-risk items | Cumplimiento y gobernanza. |

---

## Demo fixture strategy

No usar datos sintéticos si el propósito es mostrar funcionamiento futuro. Usar pocos casos reales y bien seleccionados.

| Fixture | Debe demostrar |
|---|---|
| Ley antigua/código | Muchas versiones, artículos, relaciones, observaciones. |
| Ley moderna relevante | Metadata actual, descriptores, publicación. |
| Decreto/reglamento | Tipo distinto, emisor distinto, relación `applies`. |
| Norma derogada | Estado y relación de derogación. |
| Artículo reformado | Versionado granular. |
| Norma con publication hint | SCIJ → Gaceta reconciliation. |
| Norma con conflicto o ausencia | Honestidad operativa. |
| Negative fixture PagError/wrapper | Calidad de adquisición. |

---

## Lo que queda fuera de la demo

- UI final para ciudadanos.
- Chatbot jurídico que interpreta.
- Corpus completo de jurisprudencia.
- Corpus completo de pronunciamientos PGR.
- State hub completo.
- Personas/cargos/officeholders.
- Scraping amplio de La Gaceta.
- Edictos/avisos/adjudicaciones.
- SPARQL público.
- Triple store como requisito.

---

## Criterios de calidad para una demo no vergonzosa

1. Cada dato mostrado tiene fuente.
2. Cada URI sigue `URI_POLICY.md`.
3. Cada relación tiene dirección y tipo.
4. Cada versión tiene evidencia temporal o está marcada como incompleta.
5. Los datos de publicación distinguen pista vs verificación.
6. Los errores/wrappers no cuentan como cobertura.
7. No hay placeholders que luego deban reemplazarse por otro modelo.
8. No hay claims de oficialidad que Plaza no puede hacer.
9. No hay extracción estructurada de personas privadas.
10. La demo puede crecer hacia producción sin reescribir su fundamento.

---

## Mensaje conceptual de demo

La demo debe comunicar:

> Plaza convierte derecho costarricense público en datos estructurados, verificables, versionados y citables, sin sustituir a las fuentes oficiales ni interpretar el derecho.

No comunicar:

- “Plaza es un buscador mejor que SCIJ.”
- “Plaza es un abogado IA.”
- “Plaza scrapea todo el Estado.”
- “Plaza tiene una base pública de personas.”

---

## Preguntas pendientes antes de fijar demo scope

1. ¿Qué norma real será el caso principal?
2. ¿Tiene esa norma versiones múltiples?
3. ¿Tiene artículos bien parseables?
4. ¿Tiene relaciones SCIJ útiles?
5. ¿Tiene publication hint en SCIJ?
6. ¿Existe edición Gaceta localizable para verificar publicación?
7. ¿Hay riesgos de datos personales en el texto o tabs?
8. ¿Qué formato público se mostrará primero: JSON-LD, Turtle, HTML mínima, API response o MCP response?
9. ¿Qué criterio define “demo lista”?
10. ¿Qué queda explícitamente fuera sin parecer bug?
