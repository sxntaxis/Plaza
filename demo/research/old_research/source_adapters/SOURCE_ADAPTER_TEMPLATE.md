# Plaza — Source Adapter Template

**Estado:** plantilla de investigación técnica.
**No es contrato público.** Cada adapter describe comportamiento de fuente para guiar adquisición/refinamiento/reconciliación.

---

## Cómo usar esta plantilla

Un source adapter note debe responder:

1. ¿Qué fuente es?
2. ¿Qué autoridad la publica?
3. ¿Qué rol cumple para Plaza?
4. ¿Cómo se accede?
5. ¿Qué artefactos crudos deben preservarse?
6. ¿Qué campos se pueden extraer sin inferencia?
7. ¿Qué inferencias son aceptables y cómo se marcan?
8. ¿Qué riesgos de publicabilidad tiene?
9. ¿Qué no debe intentar el adapter?
10. ¿Qué fixtures demuestran que funciona?

---

## 1. Identidad de fuente

```yaml
source_id:
source_name:
institution:
source_role:
  - publication_official
  - official_operational_consolidation
  - institutional_certification
  - sectoral_official_source
  - historical_archive
  - interpretive_hook
jurisdiction: cr
language: spa
status:
  - core_current
  - core_complementary
  - future_conditioned
  - reference_only
  - excluded_ordinary
```

---

## 2. Autoridad y función pública

- ¿Qué institución opera la fuente?
- ¿La fuente es publicación oficial, consolidación oficial, repositorio sectorial, archivo histórico o interpretación?
- ¿Qué función pública cumple?
- ¿Qué claims permite hacer?
- ¿Qué claims no permite hacer?

Ejemplo de distinción:

| Claim | Publicación oficial | Consolidación operativa | Certificación institucional |
|---|---:|---:|---:|
| “Este acto fue publicado en fecha X” | Sí, si se extrae del diario oficial. | Solo como pista. | Sí, si la certificación lo dice. |
| “Este texto es versión consolidada vigente” | No necesariamente. | Sí, si la fuente lo indica. | Depende. |
| “Esta afirmación está certificada” | No, salvo certificación. | No. | Sí. |

---

## 3. Vía preferente de acceso

| Vía | Aplica | Notas |
|---|---:|---|
| Publicación proactiva |  |  |
| Solicitud formal |  |  |
| Convenio |  |  |
| Descarga oficial estructurada |  |  |
| UI pública humana |  |  |
| Adquisición automatizada residual |  |  |

Regla: adquisición automatizada no decide su propia legitimidad. Solo ejecuta una vía previamente habilitada.

---

## 4. Superficies conocidas

| Surface | URL pattern / acceso | Qué contiene | Artefacto crudo | Estado |
|---|---|---|---|---|
|  |  |  |  |  |

Separar:

- páginas HTML;
- PDFs;
- tabs;
- buscadores;
- índices;
- feeds;
- archivos descargables;
- imágenes;
- metadatos embebidos;
- APIs si existen.

---

## 5. Identidad de adquisición

La identidad de adquisición es el identificador propio de la fuente. No es URI canónica Plaza.

Registrar:

```yaml
source_identity_components:
  -
example_source_identity:
canonical_plaza_identity: assigned later by canonicalization
```

Reglas:

- No poner estado transitorio de crawl en URIs Plaza.
- No depender solo de una URL UI si la fuente tiene IDs internos.
- Preservar todos los source IDs como evidencia.
- Si los IDs fuente son ambiguos, no promover a canónico hasta resolver.

---

## 6. Artefactos crudos

| Artefacto | Preservar | Metadata mínima |
|---|---:|---|
| HTML |  | URL final, timestamp, status, headers relevantes, hash, encoding. |
| PDF |  | URL, timestamp, hash, page count, size, content-type. |
| Imagen |  | URL, timestamp, hash, dimensiones. |
| Search result |  | Query, parámetros, timestamp, raw result. |
| Redirect/error wrapper |  | URL inicial/final, status, body hash, clasificación de error. |

Principio: si el refinamiento mejora, se debe poder reprocesar sin volver a la fuente.

---

## 7. Marcadores de integridad

Listar marcadores que permiten validar que el artefacto corresponde a lo esperado.

| Marker | Tipo | Uso | Si falta |
|---|---|---|---|
|  | heading / banner / field / checksum / page count / ID |  | fail / review_needed / unsupported |

Estados recomendados:

- `success`
- `missing`
- `unsupported`
- `review_needed`
- `failed`
- `excluded`
- `conflict`
- `wrapper_like`
- `pagerror`

No colapsar estados. `failed` no es lo mismo que `review_needed`; `missing` no es lo mismo que `unsupported`.

---

## 8. Salida de refinamiento

Describir entidades candidatas y afirmaciones producidas antes de canonicalización.

| Salida | Tipo | Evidencia requerida | Nivel de verificación esperado |
|---|---|---|---|
|  |  |  |  |

Toda salida debe conservar vínculo al artefacto crudo y, cuando sea posible, al span/text offset/página.

---

## 9. Riesgos de publicabilidad

| Riesgo | Presente | Manejo |
|---|---:|---|
| Datos personales incidentales |  | preservar solo como texto oficial / no estructurar / reducir / excluir |
| Datos sensibles |  | excluir o mantener interno salvo base explícita |
| Finalidad incompatible |  | no publicar |
| Restricción institucional |  | convenio / excluir |
| Fuente no habilitada |  | no adquirir |
| Ambigüedad de licencia/base jurídica |  | mantener fuera de grafo público |

---

## 10. No-goals del adapter

Listar explícitamente qué no hace.

Ejemplos:

- no asigna URI canónica;
- no interpreta derecho;
- no decide vigencia si la fuente no lo prueba;
- no resuelve relaciones débiles como hechos;
- no modela personas;
- no publica datos no habilitados;
- no convierte search UI en API pública simulada;
- no hace OCR salvo fallback documentado;
- no usa crawling agresivo.

---

## 11. Fixtures recomendados

| Fixture | Por qué existe | Superficies cubiertas | Resultado esperado |
|---|---|---|---|
|  |  |  |  |

Cada fixture debe poder usarse offline. Guardar raw artifacts, no solo parsed output.

---

## 12. Acceptance checks

Cada adapter debe tener checks concretos.

Ejemplos:

- Dada una URL válida, adquisición preserva artefacto crudo con hash.
- Dado un wrapper/error, no se marca como éxito.
- Dado un artefacto con marcador de versión, refinamiento captura el marker y su evidencia.
- Dada una relación ambigua, se guarda raw text y se marca `review_needed`, no como relación canónica.
- Dado un material excluido, no aparece en snapshot público.

---

## 13. Preguntas pendientes

- ¿Qué debe verificarse en web?
- ¿Qué requiere consulta legal?
- ¿Qué requiere convenio?
- ¿Qué requiere decisión de scope?
- ¿Qué requiere fixture antes de implementar?

---

## 14. Legacy source trace

Indicar qué research legacy alimentó el adapter. No consultar olddocs salvo disputa específica.

```text
Legacy inputs absorbed:
-
-
```
