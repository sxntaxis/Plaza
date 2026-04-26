# Plaza — Research Distill

**Estado:** memoria de investigación, no documentación normativa.
**Fecha de destilación:** 2026-04-25.
**Origen:** `olddocs.tar.xz`, especialmente `docs/research/` y piezas de source behavior en `docs/roadmaps/districts/`.
**Propósito:** capturar todo el contexto reutilizable de los documentos legacy para que la nueva Plaza no tenga que volver a abrirlos.

---

## Regla de autoridad

Este directorio **no gobierna Plaza**.

Si cualquier nota aquí contradice los documentos fundacionales actuales, pierden estas notas. El orden de autoridad es:

1. `VISION.md`
2. `PRINCIPLES.md`
3. `SCOPE.md`
4. `LEGAL_BASIS.md`
5. `ARCHITECTURE.md`
6. `DATA_MODEL.md`
7. `URI_POLICY.md`
8. `QUALITY_AND_VALIDATION.md`
9. `ACCESS_SURFACES.md`
10. `LICENSING.md`
11. `VERSIONING.md`
12. `REFERENCES.md`
13. Este directorio de research distill

Este material sirve para orientar investigación, adapters, fixtures, validaciones y decisiones técnicas futuras. No debe usarse como promesa pública ni como contrato del proyecto.

---

## Qué se destiló

El archivo legacy contenía research útil mezclado con documentación operativa obsoleta, roadmaps ejecutados, prompts de agentes, reportes de campaña y diseño de arquitectura ya reemplazado.

La destilación conserva únicamente:

- contexto de estándares;
- comportamiento de fuentes;
- pistas de extracción;
- criterios de fixtures;
- mapas de fuentes oficiales;
- insight sobre tareas de usuario;
- riesgos y anti-goals que siguen siendo válidos;
- preguntas pendientes que conviene investigar con web antes de implementar.

Se descarta como autoridad:

- nombres de tablas legacy;
- módulos/clases/personajes de la implementación vieja;
- prompts de agentes;
- roadmaps fechados;
- colas de auditoría;
- SQL viejo;
- reportes de cobertura como verdad actual;
- cualquier afirmación legal no absorbida por `LEGAL_BASIS.md`.

---

## Estructura

| Documento | Función |
|---|---|
| `RESEARCH_LEDGER.md` | Registro de qué se extrajo de cada documento legacy y dónde quedó absorbido. |
| `STANDARDS_RESEARCH_NOTES.md` | Mapa de estándares: qué usa Plaza, qué queda reservado, qué no conviene adoptar todavía y qué requiere web refresh. |
| `SOURCE_REGISTRY_CANDIDATES.md` | Mapa de fuentes oficiales candidatas, su posible rol y estado de incorporación. |
| `USER_TASKS_AND_DEMO_LEADS.md` | Tareas de usuario y comportamientos SCIJ relevantes, traducidos a criterios de demo/data-layer. |
| `RAG_AND_MCP_RESEARCH_NOTES.md` | Destilado de IA/RAG: cómo aprovechar Plaza sin convertirla en razonador legal. |
| `FUTURE_STATE_HUB_NOTES.md` | Capa institucional/cargos/personas: contexto de largo plazo bajo restricciones fuertes. |
| `REQUIREMENTS_TRACEABILITY_NOTES.md` | Cómo usar lenguaje de requisitos, acceptance criteria y trazabilidad sin burocratizar Plaza. |
| `source_adapters/SOURCE_ADAPTER_TEMPLATE.md` | Plantilla para describir una fuente. |
| `source_adapters/SCIJ.md` | Adapter note para SCIJ/SINALEVI. |
| `source_adapters/GACETA.md` | Adapter note para La Gaceta/Imprenta Nacional. |

---

## Cómo usar este directorio

### Para diseñar adapters

Empezar por:

1. `source_adapters/SOURCE_ADAPTER_TEMPLATE.md`
2. `source_adapters/SCIJ.md`
3. `source_adapters/GACETA.md`

La idea es que cada adapter tenga conocimiento explícito de la fuente: URLs, superficies, marcadores de integridad, artefactos crudos, riesgos y no-goals. La arquitectura actual ya separa adquisición, refinamiento y reconciliación; estos notes ayudan a poblar esa separación.

### Para research de estándares

Empezar por:

1. `STANDARDS_RESEARCH_NOTES.md`
2. `DATA_MODEL.md`
3. `URI_POLICY.md`
4. `ACCESS_SURFACES.md`

El research legacy dice dónde mirar. No debe usarse para afirmar versiones actuales de estándares sin verificación web.

### Para demo y MVP

Empezar por:

1. `USER_TASKS_AND_DEMO_LEADS.md`
2. `SCOPE.md`
3. `QUALITY_AND_VALIDATION.md`

El valor no es copiar SCIJ. El valor es demostrar comportamientos: identidad estable, versión temporal, relaciones, fuente, evidencia y honestidad sobre incertidumbre.

### Para no volver a olddocs

Consultar `RESEARCH_LEDGER.md`. Si una pregunta aparece cubierta en el ledger, no abrir legacy. Si una pregunta no aparece ahí, primero preguntarse si pertenece a Plaza nueva; si sí, hacer research fresco.

---

## Criterio de cierre

Después de este destilado, `olddocs.tar.xz` debe tratarse como **archivo histórico frío**.

Solo debería reabrirse si hay una disputa específica sobre el origen de una nota de investigación. Para diseño, implementación o roadmap de Plaza nueva, este distill reemplaza el uso de olddocs.
