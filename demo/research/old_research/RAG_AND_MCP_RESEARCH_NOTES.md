# Plaza — RAG and MCP Research Notes

**Estado:** memoria de investigación.
**No define un producto de IA.** Plaza expone datos verificables; los sistemas de IA consumen Plaza.

---

## Tesis destilada

El research legacy usaba “RAG” como forma de pensar consumo por IA. La Plaza nueva ya tiene una formulación más limpia:

> Plaza no debe ser un asistente que interpreta derecho. Plaza debe ser una fuente de retrieval verificable para sistemas de IA.

El servidor MCP y cualquier superficie IA deben entregar:

- texto normativo exacto;
- metadata;
- versiones;
- relaciones;
- fuente;
- URI canónica verificable;
- estado de incertidumbre.

No deben entregar interpretación jurídica propia.

---

## Capacidades IA útiles

| Capacidad | Descripción | Riesgo |
|---|---|---|
| Retrieval por URI | Dada una URI Plaza, devolver recurso y metadata. | Bajo. |
| Retrieval por artículo | Dada norma/artículo/fecha, devolver texto exacto. | Medio si hay versionado incompleto. |
| Búsqueda por texto | Buscar normas/artículos relevantes. | Riesgo de ranking opaco; debe citar URIs. |
| Búsqueda por metadata | Tipo, emisor, fecha, estado, descriptor. | Bajo si vocabularios están curados. |
| Navegación de relaciones | Afectaciones, derogaciones, reglamentaciones, concordancias. | Medio: relaciones deben tener tipo y evidencia. |
| Context pack | Paquete de norma + artículos + relaciones + fuente. | Riesgo de demasiado contexto o claims no resueltos. |
| Citation enforcement | Toda respuesta de tool incluye URIs. | Necesario. |
| Issue surfacing | Mostrar conflicts/missing/review_needed. | Necesario para honestidad. |

---

## No capacidades IA de Plaza

Plaza no debe:

- responder “qué debo hacer legalmente”;
- interpretar si una conducta es legal;
- predecir resultado judicial;
- resumir efectos jurídicos como verdad propia;
- resolver conflictos doctrinales;
- ocultar incertidumbre para dar una respuesta más bonita;
- usar LLM para completar campos canónicos sin marca de inferencia;
- convertir observaciones en conclusiones;
- usar RAG como capa para saltarse modelado estructurado.

---

## MCP resource/tool sketch conceptual

Esto no es API spec final. Es mapa de capacidades.

| Capability | Input | Output | Reglas |
|---|---|---|---|
| `get_resource_by_uri` | URI Plaza | JSON-LD/Turtle-ish resource + provenance | No interpretación. |
| `get_text_by_uri` | URI norma/artículo/versión | Texto exacto + source evidence | Si no hay versión exacta, devolver no-resolve. |
| `search_norms` | query + filtros | Lista de URIs + snippets + score | Cada resultado citable. |
| `get_relationships` | URI + relation type optional | Relaciones tipadas + evidence | Distinguir canonical/candidate/review. |
| `get_publication_evidence` | URI | SCIJ hints + Gaceta verified events | Separar hint/verificado. |
| `get_versions` | URI LegalResource | Lista de LegalExpressions | Incluir source marker y coverage. |
| `get_reconciliation_status` | URI | missing/conflict/issues | Mostrar incertidumbre. |
| `get_snapshot_metadata` | snapshot ID | hash, generated_at, ontology/model/shapes version | Reproducibilidad. |

---

## Context pack mínimo para LLM

Cuando un LLM pida contexto sobre una norma, el pack debería incluir:

```yaml
resource_uri:
resource_type:
title:
type_document:
number:
emitter:
in_force_status:
version_uri:
version_date:
text_requested:
relationships_summary:
publication_evidence:
provenance:
  source:
  artifact_uri_or_id:
  source_url:
  captured_at:
  hash:
quality_status:
  verification_level:
  inferred:
  issues:
```

Cada bloque debe distinguir:

- `verified`
- `inferred`
- `candidate`
- `conflict`
- `missing`
- `excluded`

---

## Prompting rules for external LLM consumers

Esto pertenece a documentación futura de consumo, no al core.

Un LLM que consuma Plaza debe recibir reglas como:

1. Usa solo fuentes devueltas por Plaza para afirmaciones sobre derecho costarricense.
2. Cita siempre las URIs Plaza.
3. No trates candidate relations como hechos definitivos.
4. Distingue texto normativo de observaciones/editorial notes.
5. Distingue publicación SCIJ hint de Gaceta verified event.
6. No infieras vigencia si Plaza no la marca.
7. Si falta evidencia, dilo.
8. No extraigas ni perfiles personas privadas desde textos.
9. No conviertas retrieval en asesoría legal.
10. Remite al usuario a profesional legal cuando la pregunta sea de aplicación concreta.

---

## RAG pitfalls extraídos del legacy

| Pitfall | Mitigación |
|---|---|
| RAG sobre texto plano sin estructura | Usar URIs, versiones, artículos y relaciones. |
| LLM mezclando versiones | Incluir version URI y fechas explícitas. |
| LLM confundiendo concordancia con reforma | Relation types claros. |
| LLM sobreafirmando publicación oficial | Separar SCIJ hints y Gaceta events. |
| LLM citando sin fuente | MCP/tools deben devolver URI obligatoria. |
| LLM completando lagunas | Estados missing/review_needed visibles. |
| RAG como sustituto de canonicalización | Nunca; retrieval consume grafo canónico. |
| Context window excesivo | Context packs por tarea, no dump completo. |
| Search ranking como verdad | Resultados son candidatos; usuario/LLM debe verificar URI. |

---

## Fixtures IA/MCP recomendados

| Fixture | Qué prueba |
|---|---|
| URI de norma vigente | Retrieval directo y metadata. |
| URI de artículo específico | Granularidad citable. |
| URI de versión histórica | Precisión temporal. |
| Norma con relaciones canónicas | Navegación graph. |
| Norma con relación candidata | Honestidad de status. |
| Norma con publication hint pero sin Gaceta verified | Distinción de evidencia. |
| Norma con conflict issue | LLM no debe resolver silenciosamente. |
| Search query ambigua | Resultados con ranking y URIs, no respuesta final. |

---

## Research fresco requerido

Antes de implementar MCP:

1. Verificar versión actual del Model Context Protocol.
2. Revisar patrón recomendado de resources/tools/prompts.
3. Definir cómo representar citas obligatorias en tool responses.
4. Definir límites de tamaño/context packs.
5. Definir seguridad: no endpoints mutables, no hidden operational layers.
6. Definir tests contra hallucination-prone scenarios.

---

## Resumen

La IA es consumidor primario, no identidad operacional de Plaza. El valor de Plaza para IA es hacer que el modelo no tenga que “recordar” derecho costarricense, sino recuperar texto, relaciones y procedencia verificables. El servidor MCP debe ser aburrido, determinista y citable.
