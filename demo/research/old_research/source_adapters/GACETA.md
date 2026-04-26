# Plaza Source Adapter Note — La Gaceta / Imprenta Nacional

**Estado:** memoria técnica de fuente.
**No es contrato público.**
**Fuente legacy absorbida:** `Gaceta.md`, `Fuentes oficiales...`, `harvest_observations.md`, `harvest_gaceta_roadmap.md`, `extract_gaceta/taxonomy.md`, `extract_gaceta/segmentation_spec.md`, `extract_gaceta/extraction_schema.md`, `FAMILY_COVERAGE_REPORT.md`.

---

## 1. Identidad de fuente

```yaml
source_id: gaceta_imprenta
source_name: Diario Oficial La Gaceta
institution: Imprenta Nacional de Costa Rica
source_role:
  - publication_official
jurisdiction: cr
language: spa
status: core_complementary_future_reconciliation
```

La Gaceta debe modelarse como fuente de **publicación oficial**, no como “otro SCIJ”. Su rol principal para Plaza nueva es:

1. verificar publicación oficial;
2. anclar fecha, número de Gaceta, edición y alcance;
3. reconciliar publicación oficial con consolidación SCIJ;
4. servir como evidencia temporal cuando corresponda.

No debe convertirse en ingesta indiscriminada de todo lo publicado.

---

## 2. Claim discipline

| Plaza puede decir | Condición |
|---|---|
| “Este documento aparece publicado en esta edición/alcance de La Gaceta.” | Si se preservó PDF/HTML y se extrajo fecha/número/alcance. |
| “Esta norma tiene pista de publicación oficial.” | Si existe matching SCIJ ↔ Gaceta con evidencia. |
| “Este texto proviene de la publicación oficial.” | Si el texto se extrajo del PDF/artefacto oficial preservado. |
| “Este acto está vigente.” | No por publicación sola; requiere análisis normativo/consolidación/entrada en vigencia. |
| “Todo lo publicado es publicable como datos estructurados.” | No. Publicación oficial no elimina límites de finalidad/datos personales. |
| “Edictos/avisos/personas son corpus Plaza.” | No en scope actual. |

---

## 3. Identidad de adquisición

La identidad natural de adquisición para La Gaceta es la publicación por fecha/edición/alcance.

Componentes frecuentes:

```yaml
publication_date: YYYY-MM-DD
issue_type: regular | alcance
issue_number: número de Gaceta si aparece
alcance_number: número de alcance si aplica
file_family: COMP | ALCA
source_path: /pub/YYYY/MM/DD/COMP_DD_MM_YYYY.pdf
```

Patrones legacy observados:

```text
/pub/YYYY/MM/DD/COMP_DD_MM_YYYY.pdf
/pub/YYYY/MM/DD/ALCAxx_DD_MM_YYYY.pdf
/ver/pub/YYYY/MM/DD/COMP_DD_MM_YYYY.pdf
```

Reglas:

1. La URL es evidencia de adquisición, no URI canónica de norma.
2. `COMP` representa edición compilada/regular.
3. `ALCA` representa alcance/suplemento.
4. La fecha en path debe cruzarse con fecha visible en PDF/texto.
5. El número de Gaceta/Alcance debe extraerse del artefacto, no inventarse.
6. Si el PDF directo requiere pasar por vista `ver/pub`, preservar ambos contextos.

---

## 4. Artefactos primarios

| Artefacto | Rol | Preservar |
|---|---|---|
| PDF de edición regular (`COMP`) | Artefacto oficial primario de publicación. | archivo completo, URL, timestamp, hash, tamaño, content-type, page count, texto extraído. |
| PDF de alcance (`ALCA`) | Artefacto oficial primario de suplemento. | igual que COMP + número de alcance. |
| HTML “ver en línea” | Vista auxiliar segmentada/navegable. | HTML completo, URL, timestamp, hash, links a PDF. |
| Cover/page image | Auxiliar si metadata no está en texto. | imagen, hash, dimensiones; OCR solo si necesario. |
| Index/histórico | Discovery auxiliar. | HTML/query, timestamp, raw. |

Regla: el PDF es el artefacto principal. HTML puede ayudar a segmentar, pero no debe sustituir el PDF para evidencia de publicación si el PDF existe.

---

## 5. Discovery strategy

Legacy research encontró que no debe asumirse RSS o sitemap confiable. La estrategia preferente es **date-driven**.

### Flujo recomendado

1. Generar fechas candidatas.
2. Saltar fines de semana y, si existe, feriados conocidos.
3. Intentar edición regular `COMP_DD_MM_YYYY.pdf`.
4. Detectar alcances asociados por HTML/index o patrones `ALCA`.
5. Validar response: status, content-type, PDF header, tamaño razonable, page count.
6. Preservar artefacto crudo.
7. Extraer texto.
8. Validar metadata de portada: fecha, número, año, edición/alcance.
9. Clasificar segmentos si y solo si el material pertenece al scope habilitado.

### Estados

- `published`
- `not_published_day`
- `holiday_or_weekend`
- `not_found`
- `forbidden_direct_pdf`
- `html_gateway_required`
- `pdf_invalid`
- `text_layer_missing`
- `ocr_required`
- `review_needed`

---

## 6. Metadata extraíble

| Campo | Fuente preferente | Notas |
|---|---|---|
| Fecha de publicación | PDF cover/text + URL path | Cruzar path y texto. |
| Número de Gaceta | PDF cover/header | No siempre en HTML metadata. |
| Año institucional / año de publicación | PDF cover | Ej. “Año CXLIV”. |
| Tipo de edición | path + cover | regular/alcance. |
| Número de alcance | filename + cover | Validar contra texto visible. |
| Páginas | PDF metadata/page count | QA. |
| Secciones | HTML headings o PDF headings | Normalizar con raw preserved. |
| IDs internos `(IN...)` | Texto HTML/PDF | Source-local anchors, no identidad canónica. |
| Encabezados de documento | PDF/HTML | Útil para segmentación. |
| Referencias legales | Texto | Mantener raw/unresolved. |
| Firma/signatarios | Texto | Preservar en texto oficial; no estructurar personas por defecto. |

---

## 7. Taxonomía de familias documentales

Legacy identificó familias frecuentes. En Plaza nueva, esta taxonomía sirve para **clasificar y excluir/reducir**, no para ingerir todo.

| Familia | Valor potencial para Plaza | Tratamiento recomendado |
|---|---|---|
| Decretos | Alta relevancia normativa; probable overlap con SCIJ. | Candidato a reconciliación con SCIJ. Extraer como publicación oficial si scope habilitado. |
| Acuerdos | Relevancia normativa/administrativa variable. | Candidato selectivo; requerir tipo/emisor claro. |
| Reglamentos | Alta relevancia normativa. | Candidato a publicación/reconciliación. |
| Fe de Erratas | Alta relevancia para correcciones. | Candidato a relation/correction evidence; requiere linking cuidadoso. |
| Leyes / Poder Legislativo | Relevancia normativa primaria. | Candidato core cuando aparezca; matching con SCIJ/Asamblea. |
| Directrices/resoluciones generales | Relevancia posible. | Requiere clasificación por tipo normativo. |
| Municipalidades | Futuro local; heterogéneo. | Fuera de scope actual salvo caso específico. |
| Edictos | Alto volumen, datos personales/casos. | Excluir del corpus estructurado ordinario. Puede clasificarse para no ingestarlo. |
| Avisos | Muy variable; naturalización y datos personales. | Excluir/reducir; no estructurar personas. |
| Adjudicaciones | Contratación, empresas/personas, montos. | Fuera de corpus normativo actual. |
| Convocatorias | Contratación/procedimientos. | Fuera de corpus normativo actual. |
| TSE/CGR sectorial | Potencial futuro. | Solo con decisión de scope/fuente específica. |

---

## 8. Segmentación

Si se segmenta una edición, la jerarquía conceptual útil es:

```text
Issue / Edition
  Section
    Item / Publication
      Block
      Extracted metadata
```

### Estrategias

| Estrategia | Uso | Riesgo |
|---|---|---|
| Header-based | Ediciones bien estructuradas con headings claros. | Headers ambiguos o inconsistentes. |
| Content-based | Documentos viejos/mal formateados. | Falsos positivos. |
| Hybrid | General. Header first, validate with content patterns. | Requiere confidence y review queue. |

### Headers útiles

```text
PODER EJECUTIVO
DECRETOS
ACUERDOS
REGLAMENTOS
EDICTOS
AVISOS
FE DE ERRATA
MUNICIPALIDADES
ADJUDICACIONES
CONVOCATORIAS
```

### Patrones de contenido útiles

```text
DECRETO No. ...
ACUERDO No. ...
RESOLUCIÓN No. ...
VISTOS:
CONSIDERANDO:
RESUELVE:
DECRETA:
Dado en...
```

### Metadata de segmento

Cada segmento debería conservar:

```yaml
segment_id:
issue_id:
section:
section_raw:
item_index:
page_start:
page_end:
text_offset_start:
text_offset_end:
confidence:
detection_method: header_based | content_based | hybrid
raw_header:
family_hypothesis:
source_evidence:
```

---

## 9. QA de segmentación

| Check | Regla |
|---|---|
| Completeness | Todo texto no excluido debe estar en algún segmento o en bucket explícito `unsegmented_review`. |
| Overlap | Segmentos no deben solaparse sin explicación. |
| Size | Flag segmentos demasiado pequeños o demasiado grandes. |
| Page boundaries | Items multi-página deben conservar `page_start/page_end`. |
| Header/footer stripping | Remover headers/footers de texto normalizado, pero preservar raw. |
| Continuation | Detectar `(Continúa)` y unir cuando haya evidencia. |
| Confidence | `1.0` clear header + content pattern; `0.5` ambiguous; `0.3` manual review. |
| Evidence | Todo segmento debe apuntar a PDF/page/offset/hash. |

---

## 10. Legal references y candidate relations

Legacy propuso extraer referencias legales y relaciones candidatas sin resolverlas de inmediato. Esa regla sobrevive.

### Legal reference raw

```yaml
reference_raw:
reference_type: law | decreto | acuerdo | reglamento | constitution | other
reference_number:
reference_year:
reference_subject:
evidence:
resolution_status: unresolved
resolution_attempts: []
```

### Candidate relation raw

```yaml
relation_type: amends | implements | repeals | derives_from | cites | supplements | other
target_reference_raw:
evidence:
confidence:
resolution_status: unresolved
```

Reglas:

1. Extract puede detectar raw references.
2. Reconciliation resuelve contra SCIJ/Plaza.
3. Canonicalización solo ocurre con extremos canónicos y evidencia suficiente.
4. Fe de erratas puede sugerir `eli:corrects`, pero requiere matching documental.
5. “Implementa la Ley X” puede sugerir `eli:applies`, no asumir sin validación.

---

## 11. Publicabilidad y exclusiones

La Gaceta contiene actos públicos, pero también material con datos personales o uso incompatible para una base estructurada pública.

### Regla de máxima importancia

> La publicación oficial de un texto no autoriza automáticamente extraer cada persona, parte, dirección, expediente, adjudicatario o dato incidental como entidad estructurada reutilizable.

### Tratamiento por familia

| Familia | Tratamiento público por defecto |
|---|---|
| Leyes, decretos, reglamentos, acuerdos normativos | Publicable si cumple fuente/base/publicabilidad y calidad. |
| Fe de erratas normativas | Publicable como evidencia de corrección si se vincula a acto normativo. |
| Edictos judiciales | Excluir de corpus estructurado ordinario; preservar solo si hay razón legal específica y reducción. |
| Avisos de naturalización u otros avisos personales | Excluir estructuración de personas; no incluir en Plaza actual. |
| Adjudicaciones/convocatorias | Fuera de corpus normativo actual; no estructurar bidders/personas. |
| Municipalidades | Futuro condicionado; alto heterogeneidad. |
| Signatarios de normas | Preservar como texto oficial; no crear entidad persona en scope actual. |

---

## 12. Reconciliación con SCIJ

La reconciliación Gaceta ↔ SCIJ no es “linking fuerte” del extract inicial. Es capa posterior.

### Inputs

- SCIJ publication hints: número Gaceta, fecha, alcance, página si existe.
- Gaceta issue metadata: fecha, número, alcance, páginas.
- Segment text/header: tipo, número de norma, emisor, título.
- Raw legal references.

### Matching candidate features

| Feature | Peso conceptual |
|---|---|
| Tipo de norma | Alto |
| Número de norma/decreto | Alto |
| Fecha de emisión/publicación | Medio/alto |
| Título/sujeto | Medio |
| Emisor | Medio |
| Gaceta number/alcance | Alto |
| Página | Alto si existe |
| Texto inicial / encabezado | Medio |

### Estados de match

- `matched_verified`
- `matched_probable`
- `ambiguous_multiple_candidates`
- `no_candidate`
- `conflict_scij_gaceta`
- `excluded_family`
- `needs_manual_review`

No promover una publicación como verificada si el match es solo probable.

---

## 13. Fixtures recomendados

| Fixture | Propósito |
|---|---|
| Edición regular reciente (`COMP`) | Validar PDF, fecha, número, headers, page count. |
| Alcance reciente (`ALCA`) | Validar número de alcance y URL patterns. |
| Edición con decreto | Segmentación de decreto y references. |
| Edición con reglamento | Segmentación normativa compleja. |
| Edición con fe de erratas | Corrección y candidate relation. |
| Edición con edictos | Negative/exclusion fixture. |
| Edición con avisos/naturalización | Privacy exclusion fixture. |
| Direct PDF 403 / gateway required | Acquisition fallback. |
| PDF con text layer normal | Baseline extraction. |
| PDF con text extraction broken | OCR fallback/review. |
| SCIJ publication hint matching issue | Reconciliation fixture. |

Cada fixture debe incluir raw PDF, extracted text, optional HTML, metadata manifest y expected classification.

---

## 14. No-goals

La Gaceta adapter no debe:

- copiar SCIJ adapter;
- crawlear sin límites;
- ingerir todo el Diario Oficial como corpus Plaza;
- estructurar personas privadas;
- resolver vigencia por sí solo;
- resolver relaciones normativas fuertes en extraction layer;
- reemplazar SCIJ como consolidación;
- publicar edictos/avisos/adjudicaciones como open corpus;
- asumir que `COMP`/`ALCA` URL existence basta como metadata;
- asumir que una familia legacy P3/P4/P5 define scope actual.

---

## 15. Preguntas pendientes antes de implementación

1. ¿Los patrones `COMP`/`ALCA` actuales siguen vigentes?
2. ¿El portal mantiene CC BY 4.0 y bajo qué términos exactos?
3. ¿Existe robots.txt o política técnica actual?
4. ¿El PDF directo requiere gateway `ver/pub`?
5. ¿Cómo listar alcances de forma confiable por fecha?
6. ¿Qué metadata de portada está disponible en text layer?
7. ¿Qué rango histórico tiene PDFs con text layer usable?
8. ¿Qué secciones deben clasificarse solo para exclusión?
9. ¿Cómo se documentará user-agent/contacto?
10. ¿Cuál es el mínimo de reconciliation con SCIJ para demo?
11. ¿Qué campos activan evaluación de finalidad/protección de datos?
12. ¿Qué familias deben quedar fuera incluso si la extracción técnica funciona?

---

## 16. Resumen operativo

La Gaceta es la fuente para convertir pistas de publicación en evidencia de publicación. El adapter debe ser conservador: adquirir y preservar PDFs, extraer metadata de edición/alcance, segmentar con confianza declarada, extraer referencias raw sin resolver, y excluir por defecto familias con datos personales o fuera del corpus normativo. La reconciliación fuerte con SCIJ es una etapa posterior, no parte del extractor inicial.
