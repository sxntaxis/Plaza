# Plaza Source Adapter Note — SCIJ / SINALEVI

**Estado:** memoria técnica de fuente.
**No es contrato público.**
**Fuente legacy absorbida:** `SCIJ_Surfaces.md`, `Harvest_Research.md`, `RAG.md`, `SCIJ Field Validation and Campaign Notes.md`, `harvest_observations.md`, roadmaps SCIJ relacionados.

---

## 1. Identidad de fuente

```yaml
source_id: scij_pgr
source_name: Sistema Costarricense de Información Jurídica / SINALEVI
institution: Procuraduría General de la República
source_role:
  - official_operational_consolidation
  - interpretive_hook_source
jurisdiction: cr
language: spa
status: core_current
```

SCIJ/SINALEVI es la fuente operativa principal para normativa costarricense consolidada: texto vigente/consolidado, versiones, metadata, relaciones normativas y surfaces editoriales.

No es idéntica a La Gaceta. SCIJ consolida y estructura; La Gaceta publica oficialmente.

---

## 2. Claim discipline

| Plaza puede decir | Condición |
|---|---|
| “SCIJ expone esta norma con esta metadata.” | Si se preservó el artefacto SCIJ y el campo aparece ahí. |
| “SCIJ indica esta versión como X de Y.” | Si el banner fue capturado. |
| “SCIJ indica que esta norma está en la última versión.” | Si el banner visible lo dice. |
| “SCIJ registra esta afectación/concordancia/reglamentación.” | Si la fila/tab fue preservada con raw text. |
| “Esta es la publicación oficial original.” | No por SCIJ solo; requiere La Gaceta u otra evidencia de publicación oficial. |
| “Esta afirmación está certificada.” | No por SCIJ solo, salvo artefacto formal de certificación separado. |

---

## 3. Identidad de adquisición

SCIJ usa parámetros internos en sus URLs. Para Plaza son **source identity**, no identidad canónica.

Componentes frecuentes:

```yaml
nValor1: tipo/familia interna SCIJ
nValor2: identificador interno de norma/recurso
nValor3: identificador interno de versión/render
param1: tipo de superficie/consulta
strTipM: modo de vista en algunas fichas
```

Ejemplo conceptual:

```text
nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=10969&nValor3=...
```

Reglas:

1. Preservar `nValor1:nValor2:nValor3:param1:strTipM` en evidencia.
2. No usar `nValor` como URI canónica Plaza.
3. No asumir que `nValor3` equivale semánticamente al ordinal `X de Y`.
4. Cruzar `nValor3` con banner visible de versión antes de tratarlo como version evidence.
5. Si URL y banner discrepan, crear issue de reconciliación; no resolver silenciosamente.

---

## 4. Superficies SCIJ conocidas

### 4.1 Texto completo

| Elemento | Descripción |
|---|---|
| Surface | `nrm_texto_completo.aspx` |
| Param típico | `param1=NRTC`, `nValor1`, `nValor2`, `nValor3` |
| Contenido | Texto completo de la norma, artículos, transitorios, título, emisor, fecha de vigencia, banners. |
| Marcadores clave | `Versión de la norma: X de Y del dd/mm/yyyy`, `Usted está en la última versión de la norma`, encabezados de artículos. |
| Salida | LegalExpression candidata, subdivisiones/artículos, texto material, version marker. |
| Riesgo | Texto puede contener nombres de firmantes u otros datos incidentales; preservar como texto oficial, no estructurar personas. |

### 4.2 Ficha de la norma

| Elemento | Descripción |
|---|---|
| Surface | `nrm_norma.aspx` / ficha relacionada |
| Contenido | Datos generales: tipo, número, título, ente emisor, fecha de vigencia, estado, datos de publicación cuando existan. |
| Salida | Metadata fuente, publication hints, tipo/emisor/estado candidatos. |
| Reconciliación | Comparar tipo/emisor/fecha contra texto completo y otras fuentes. |

### 4.3 Normativa afectada

| Elemento | Descripción |
|---|---|
| Surface | `nrm_norma_afectaciones.aspx` o ficha con `param1=NRF` |
| Contenido | Normas que la norma actual afecta: reforma, derogación, modificación, etc. |
| Campos visibles | Artículo afectante, normativa afectada, artículo afectado, afectación, modo, raw row. |
| Salida | Candidate relation con raw evidence. |
| Mapeo futuro | `eli:amends`, `eli:repeals`, `eli:changes`, según evidencia. |
| Regla | No colapsar afectaciones con concordancias o reglamentaciones. |

### 4.4 Normativa que la afectó

| Elemento | Descripción |
|---|---|
| Surface | `nrm_norma_afectaron_Consulta.aspx` o ficha con `param1=NRR` |
| Contenido | Normas que afectan la norma actual. |
| Salida | Candidate relation inversa, con dirección explícita. |
| Riesgo | Dirección de relación puede invertirse si parser no distingue surface. |

### 4.5 Concordancias

| Elemento | Descripción |
|---|---|
| Surface | `nrm_concordancias.aspx` / `param1=NRC` |
| Contenido | Vínculos de concordancia entre normas/artículos. |
| Semántica | No siempre equivale a cita jurídica directa. Puede ser vínculo temático/editorial. |
| Salida | `eli:cites` solo si hay referencia directa; si no, extensión `plaza:concordancia_tematica` o issue/review. |
| Regla | Preservar raw text y agrupación por artículo. |

### 4.6 Reglamentaciones

| Elemento | Descripción |
|---|---|
| Surface | `nrm_reglamentaciones.aspx` |
| Contenido | Reglamentos, decretos, circulares o acuerdos relacionados con la norma. |
| Semántica | Implementación/aplicación reglamentaria. |
| Mapeo futuro | `eli:applies` del reglamento hacia la ley cuando la evidencia sea suficiente. |
| Regla | No tratar toda reglamentación como reforma. |

### 4.7 Pronunciamientos de la PGR

| Elemento | Descripción |
|---|---|
| Surface | `nrm_norma_dictamen.aspx` / `param1=NRI` |
| Contenido | Dictámenes/opiniones PGR relacionados con la norma o artículos. |
| Scope actual | Hooks, no corpus completo de pronunciamientos. |
| Salida | Referencias/hook con tipo, número, fecha, artículo, raw text. |
| Regla | No presentar dictámenes como norma. |

### 4.8 Acciones y resoluciones constitucionales

| Elemento | Descripción |
|---|---|
| Surface | `nrm_resoluciones.aspx` / `param1=NRU` |
| Contenido | Expediente, clase de asunto, voto, fecha, estado/resultado. |
| Scope actual | Hooks a acciones constitucionales; no corpus completo de jurisprudencia. |
| Riesgo | Alto riesgo si se intenta estructurar partes/personas del Poder Judicial. |

### 4.9 Observaciones

| Elemento | Descripción |
|---|---|
| Surface | `nrm_norma_observaciones.aspx` / `param1=NRO` |
| Contenido | Notas editoriales libres sobre historia, vigencia, renumeraciones, relaciones, aclaraciones. |
| Salida | Artefacto/nota editorial con raw HTML/text, vinculada a la norma. |
| Regla | No convertir automáticamente en relación canónica. Extraer claims solo con validación específica. |

### 4.10 Descriptores

| Elemento | Descripción |
|---|---|
| Surface | `nrm_norma_descriptores.aspx` / `param1=NRE` |
| Contenido | Descriptores por norma/artículo. |
| Salida | Candidatos a SKOS concepts o labels controlados. |
| Regla | Preservar texto original; normalizar solo cuando exista vocabulary policy. |

### 4.11 Búsqueda selectiva

| Elemento | Descripción |
|---|---|
| Tipo | Search surface, no tab por norma. |
| Contenido | Resultados por fecha/tipo/ente u otros filtros. |
| Uso | Discovery, cobertura, fixtures. |
| Regla | Guardar query/parámetros y result raw; no tratar como fuente canónica de metadata sin reconciliación. |

### 4.12 Búsqueda temática

| Elemento | Descripción |
|---|---|
| Tipo | Search surface por tema/descriptor. |
| Uso | Discovery y recuperación temática. |
| Regla | Los resultados temáticos no prueban por sí solos una relación jurídica. |

### 4.13 Normas usuales

| Elemento | Descripción |
|---|---|
| Tipo | Colecciones predefinidas SCIJ. |
| Uso | Discovery/fixtures/cobertura. |
| Regla | No convertir colecciones UI en taxonomía canónica Plaza sin justificación. |

---

## 5. Marcadores de integridad

| Marker | Uso | Manejo si falta |
|---|---|---|
| `Versión de la norma: X de Y del ...` | Version evidence. | `review_needed` si la norma debería tener versión; no inferir. |
| `Usted está en la última versión de la norma` | Current/latest marker SCIJ. | No marcar `current` sin otra evidencia. |
| Tipo de norma en ficha | Tipo fuente. | Comparar con texto y vocabulario; conflict si difiere. |
| Ente emisor | Emisor fuente. | Reconciliar con vocabulario controlado. |
| Datos de publicación / Gaceta / Alcance | Publication hint. | Guardar como hint SCIJ, no publicación oficial verificada. |
| Tab anatomy / headings | Validar que la página no sea wrapper. | `wrapper_like` o `failed`. |
| `/utilitarios/PagError.aspx` | Error wrapper incluso con HTTP 200. | Hard reject como `pagerror`. |
| Article headings | Segmentación de texto. | Si faltan, guardar raw y marcar extracción incompleta. |
| Raw row text en relaciones | Evidencia de relación. | Si no hay raw text, no promover relación canónica. |

---

## 6. Reglas de adquisición

1. Low concurrency.
2. User-agent identificable.
3. Preservar HTML completo de cada surface visitada.
4. Registrar URL inicial, URL final, status, headers relevantes, timestamp y hash.
5. No clasificar como éxito una página wrapper o PagError.
6. Distinguir `not_found`, `pagerror`, `timeout`, `wrapper_like`, `unsupported`, `review_needed`, `success`.
7. Separar fetch budget de extraction completeness: limitar fetch depth no debe truncar filas ya obtenidas.
8. Si un campo de identidad/versionado crítico es malformado, fail closed para esa entidad.
9. No hacer crawl amplio sin fixtures y source habilitation.
10. No usar crawling para saltarse una vía institucional preferente.

---

## 7. Reglas de refinamiento

1. Parser específico por surface; no heurística única para todo SCIJ.
2. Structured rows first; fallback link-based solo como degraded extraction.
3. Preservar raw text cuando una fila no pueda estructurarse.
4. Extraer dirección de relación explícitamente.
5. `operation_type` nunca debe ser nulo; si no se sabe, usar `unknown`/`other` con raw evidence y `review_needed`.
6. No resolver referencia a norma canónica sin evidencia suficiente.
7. No inferir fecha de vigencia desde fecha de publicación salvo regla documentada.
8. No fusionar observaciones con metadata de ficha.
9. No fusionar concordancia, afectación y reglamentación.
10. No convertir pronunciamientos ni acciones constitucionales en corpus completo dentro del scope actual.

---

## 8. Reconciliation checklist SCIJ-only

| Tema | Check |
|---|---|
| Version | `nValor3` ↔ banner `X de Y` ↔ latest marker ↔ Plaza version candidate. |
| Tipo | Ficha tipo ↔ texto header ↔ vocabulario Plaza. |
| Emisor | Ficha emisor ↔ texto header ↔ vocabulario Plaza. |
| Publicación | SCIJ publication hint separado de La Gaceta verified event. |
| Relaciones | Afectación vs concordancia vs reglamentación preservadas como tipos distintos. |
| Observaciones | Mantener como nota editorial/evidencia, no relación canónica automática. |
| Descriptores | Guardar como vocabulario/label candidato, no taxonomía final sin curación. |
| Hooks | PGR/constitucional como referencias, no corpus completo. |
| Errores | PagError/wrapper no cuentan como cobertura. |
| Personas | No estructurar nombres incidentales en textos oficiales. |

---

## 9. Salidas candidatas hacia Plaza

| Salida | Fuente SCIJ | Canonicalización posible |
|---|---|---|
| `LegalResource` candidato | Ficha + texto completo | Sí, si URI asignable, emisor/tipo/fecha verificables y procedencia completa. |
| `LegalExpression` candidato | Texto completo + version marker | Sí, si fecha/version evidence suficiente y texto íntegro. |
| Artículo/subdivisión candidato | Texto completo | Sí, si identificador natural claro y texto presente. |
| Afectación candidata | Tabs de afectaciones | Sí, si extremos canónicos y tipo ELI válido o extensión documentada. |
| Concordancia candidata | Tab concordancias | Solo si semántica clara; si no, temática/editorial. |
| Reglamentación candidata | Tab reglamentaciones | Sí, si extremos canónicos y relación aplicable clara. |
| Publication hint | Ficha SCIJ | No como evento oficial verificado sin La Gaceta. |
| Descriptor | Descriptores | Sí como SKOS candidate tras curación. |
| Pronunciamiento hook | PGR tab | Hook/reference; no corpus completo actual. |
| Acción constitucional hook | NRU tab | Hook/reference; no corpus completo actual. |
| Observación | Observaciones tab | Evidencia editorial; no claim automático. |

---

## 10. Fixtures recomendados

La selección exacta debe verificarse contra la fuente actual antes de implementarse. Legacy propuso familias útiles, no URLs garantizadas.

| Fixture | Por qué existe | Surfaces que debe cubrir |
|---|---|---|
| Código Civil / norma antigua extensa | Muchas versiones, artículos, observaciones, concordancias, afectaciones. | texto, ficha, versiones, observaciones, concordancias, reglamentaciones, PGR, constitucional. |
| Ley del Impuesto sobre la Renta / ley moderna relevante | Descriptores, versiones, uso frecuente. | texto, ficha, descriptores, publicación, relaciones. |
| Decreto Ejecutivo | Tipo distinto a ley; reglamentación y emisor Poder Ejecutivo. | texto, ficha, tipo/emisor, reglamentaciones. |
| Norma derogada/no vigente | Estado de vigencia y relación de derogación. | ficha, afectaciones, version/current marker. |
| Norma con pronunciamientos PGR abundantes | Hook interpretativo. | PGR tab, article references. |
| Norma con acciones constitucionales | Hook de control constitucional. | NRU tab. |
| Norma con observaciones vacías | Empty case. | observaciones missing/unsupported. |
| Búsqueda selectiva | Discovery fixture. | query params, result page. |
| Búsqueda temática/descriptores | Descriptor fixture. | thematic result, descriptor parsing. |
| Normas usuales | Collection fixture. | collection membership. |
| Multi-version chain | Version navigation. | original/anterior/vigente links, `X de Y`. |
| PagError/wrapper | Negative fixture. | error classification. |

Cada fixture debe guardar raw HTML por surface y manifest con razón de inclusión.

---

## 11. Métricas de confianza

| Métrica | Qué mide | Por qué importa |
|---|---|---|
| Coverage de norms | Entidades candidatas vs discoverable SCIJ bajo metodología declarada. | No decir “100%” sin universo definido. |
| Version coverage | Normas con múltiples versiones capturadas cuando SCIJ indica `Y > 1`. | Preguntas temporales dependen de esto. |
| Relationship extraction accuracy | Conteo y spot-check de afectaciones/concordancias/reglamentaciones. | Grafo de cambios. |
| Publication hint coverage | Normas con datos de publicación SCIJ. | Reconciliación futura con Gaceta. |
| Wrapper/error rate | PagError, wrapper-like, timeout, failed. | Salud del crawl. |
| Review queue age | Issues `review_needed` por antigüedad. | Evita basura acumulada. |
| Raw evidence completeness | % de salidas con artifact/hash/span. | Reconstructibilidad. |
| SHACL/canonicalization failures | Entidades que no cruzan frontera pública. | Calidad de grafo. |

---

## 12. No-goals

SCIJ adapter no debe:

- reemplazar La Gaceta como fuente de publicación oficial;
- decidir claims de autenticidad certificada;
- inferir relaciones jurídicas desde observaciones sin validación;
- resolver todas las concordancias como citas directas;
- ingerir corpus completo de jurisprudencia;
- ingerir corpus completo de pronunciamientos PGR en scope actual;
- extraer personas como entidades;
- abrir crawling amplio sin habilitación y límites;
- usar tablas/nombres legacy como modelo actual;
- publicar capas operacionales.

---

## 13. Preguntas pendientes antes de implementación amplia

1. ¿Los URL patterns actuales siguen iguales?
2. ¿Qué surfaces requieren `param1` distinto o wrappers?
3. ¿Cuáles tabs están disponibles para normas sin versión múltiple?
4. ¿Cómo expresa SCIJ hoy `Versión original`, `Versión anterior`, `Ir a última versión`?
5. ¿Qué marcador robusto diferencia ficha válida de shell page?
6. ¿Qué límites de tasa son prudentes?
7. ¿Cómo se documenta user-agent/contacto?
8. ¿Qué campos de ficha se consideran `Nivel 1` vs `Nivel 2` de verificación?
9. ¿Qué descriptors deben mapearse a SKOS y cuáles quedan como literal?
10. ¿Qué surfacing público se permite para hooks PGR/constitucional?

---

## 14. Resumen operativo

SCIJ debe tratarse como **fuente oficial de consolidación operativa**, rica en surfaces semánticas. El adapter debe preservar cada surface, cada raw row y cada marker de versión. La reconciliación decidirá qué cruza al grafo canónico. La publicación pública nunca debe exponer como hecho definitivo algo que SCIJ solo presenta como pista, observación o vínculo editorial.
