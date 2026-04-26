# Plaza — Requirements and Traceability Notes

**Estado:** memoria de investigación.
**No impone compliance IEEE/ISO.** Este documento extrae prácticas útiles sin convertir Plaza en burocracia enterprise.

---

## Tesis destilada

Legacy research sobre IEEE/ISO no debe importarse como obligación formal. Pero sí dejó una práctica valiosa:

> Las decisiones técnicas de Plaza deben poder convertirse en requisitos verificables con acceptance criteria.

Esto ayuda a agentes, tests, audits y demo readiness sin inflar el repo.

---

## Qué conservar

| Práctica | Uso en Plaza |
|---|---|
| Requirement statements | Convertir decisiones en reglas testables. |
| Acceptance criteria | Saber cuándo una tarea está lista. |
| Traceability | Mapear principio/doc → implementación → test → artifact. |
| Viewpoints | Separar vistas: fuente, semántica, publicación, operación. |
| Test plan thinking | No publicar snapshots que no pasen checks. |
| Non-functional requirements | Idempotencia, reproducibilidad, performance, trazabilidad, seguridad. |

---

## Qué no conservar

- SRS largo como documento central.
- Compliance IEEE/ISO como meta del proyecto.
- Lifecycle documentation pesada.
- Diagrams obligatorios para todo.
- Matrices enormes que nadie mantiene.
- Requisitos que duplican docs fundacionales.
- Roadmaps por estándar.

---

## Formato recomendado de requirement ligero

```markdown
### REQ-SCIJ-001 — Rechazo de PagError

**Fuente de autoridad:** `ARCHITECTURE.md`, `QUALITY_AND_VALIDATION.md`, `source_adapters/SCIJ.md`
**Tipo:** adquisición / validación
**Statement:** El adapter SCIJ debe clasificar cualquier respuesta cuya URL final contenga `/utilitarios/PagError.aspx` como `pagerror`, aunque el HTTP status sea 200.
**Acceptance criteria:**
- Fixture con PagError no produce entidad candidata.
- El artefacto raw se preserva con estado `pagerror`.
- El evento no cuenta como cobertura exitosa.
**Tests:** `tests/source_adapters/scij/test_pagerror.py`
**Status:** proposed | implemented | verified
```

---

## Ejemplos de requirements útiles

### Identidad

```markdown
REQ-ID-001: Una entidad no debe recibir URI canónica si faltan componentes obligatorios de `URI_POLICY.md`.
Acceptance: fixture con emisor desconocido queda en reconciliación y no aparece en snapshot público.
```

### Procedencia

```markdown
REQ-PROV-001: Toda entidad canónica debe tener al menos un artefacto fuente preservado con hash.
Acceptance: SHACL/procedural check falla si `prov:wasDerivedFrom` falta.
```

### SCIJ versions

```markdown
REQ-SCIJ-VER-001: El adapter SCIJ debe capturar el banner `Versión de la norma: X de Y` cuando esté presente.
Acceptance: fixture multi-version produce `version_ordinal`, `version_total` y raw evidence.
```

### La Gaceta publication

```markdown
REQ-GACETA-001: El adapter Gaceta debe cruzar fecha de URL con fecha visible en PDF antes de aceptar la edición como válida.
Acceptance: fixture con path/cover mismatch queda `conflict` o `review_needed`.
```

### Relaciones

```markdown
REQ-REL-001: Una relación normativa no debe canonicalizarse si alguno de sus extremos no está canonicalizado.
Acceptance: relación con target unresolved queda candidate relation y no triple canónico.
```

### Publicabilidad

```markdown
REQ-PUB-001: Segmentos clasificados como edictos o avisos personales de La Gaceta no deben entrar al snapshot público del corpus normativo actual.
Acceptance: fixture de edicto se preserva/excluye según política, pero no genera entidad pública.
```

### Honestidad operativa

```markdown
REQ-HONESTY-001: `failed`, `missing`, `unsupported`, `review_needed` y `excluded` deben conservarse como estados distintos.
Acceptance: report de QA desagrega los cinco estados.
```

---

## Traceability mínima

Para tareas importantes, mantener una fila ligera:

| ID | Decisión / requirement | Doc autoridad | Implementación | Test | Estado |
|---|---|---|---|---|---|
| REQ-ID-001 | No URI sin componentes obligatorios. | `URI_POLICY.md` | canonicalization module | unit + fixture | proposed |
| REQ-PROV-001 | Toda entidad canónica tiene fuente. | `QUALITY_AND_VALIDATION.md` | SHACL/procedural validator | snapshot check | proposed |
| REQ-SCIJ-VER-001 | Capturar version banner. | `source_adapters/SCIJ.md` | SCIJ adapter | fixture | proposed |

No crear matriz gigante. Mantener solo para decisiones que cruzan frontera pública, fuente, privacidad o contratos estables.

---

## Viewpoints útiles

| Viewpoint | Pregunta | Docs relevantes |
|---|---|---|
| Fuente | ¿De dónde viene la evidencia y cómo se adquiere? | source adapters, `ARCHITECTURE.md` |
| Semántico | ¿Qué entidades y relaciones existen en el grafo? | `DATA_MODEL.md` |
| Identidad | ¿Qué URI recibe cada recurso? | `URI_POLICY.md` |
| Calidad | ¿Qué cruza a canónico? | `QUALITY_AND_VALIDATION.md` |
| Publicación | ¿Cómo consume el mundo los datos? | `ACCESS_SURFACES.md` |
| Legal/publicabilidad | ¿Puede publicarse? | `LEGAL_BASIS.md`, `SCOPE.md` |
| Operación | ¿Cómo se corre/reconstruye? | futura docs operativa, no fundacional |

---

## Acceptance checks por adapter

Cada source adapter debe tener:

1. positive fixtures;
2. negative fixtures;
3. error wrapper fixtures;
4. publicability/exclusion fixtures;
5. artifact preservation checks;
6. idempotency checks;
7. status distinction checks;
8. raw evidence checks.

---

## Definition of done para documento de research distill

Una nota de research está completa si:

- dice su autoridad y no-authority;
- enumera qué conocimiento conserva;
- enumera qué descarta;
- identifica preguntas que requieren web/legal refresh;
- define no-goals;
- no contiene tareas fechadas legacy;
- no depende de nombres de módulos viejos;
- puede ser usada por un agente sin abrir olddocs.

---

## Resumen

Usar requirements como herramienta quirúrgica, no como jaula. Plaza necesita criterios verificables en las fronteras importantes: identidad, procedencia, fuente, canonicalización, publicación y privacidad. No necesita adoptar una ceremonia IEEE completa para ser rigurosa.
