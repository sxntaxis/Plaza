# Plaza — Auditoría de Correctitud del Pipeline Legacy
**Fecha:** 2026-04-24
**Alcance:** Etapas del pipeline en /mnt/Tokyo/Lab/Git/Plaza/archive/old/
**Inventario de referencia:** /mnt/Tokyo/Lab/Git/Plaza/archive/INVENTORY_REPORT.md

## 1. Resumen ejecutivo

El pipeline legacy no es base directa y segura para canonicalización pública. La evidencia cruda SCIJ y Gaceta es valiosa, y algunas etapas derivadas funcionan bien contra raw en las muestras: `version_evidence` de SCIJ tuvo 0/100 errores observados, `norm_publication_hint` coincidió con ficha SCIJ en 30/30, y la extracción de afectaciones desde `nrm_norma_afectaciones.aspx` tuvo precision 75/75 y recall 75/76 en la muestra. Pero las etapas que fabrican identidad canónica y estructura de artículos tienen errores materiales y sistemáticos.

Los bloqueos principales son identidad y agrupación. En la muestra dirigida de las 521 normas sospechosas, 30/30 eran colapsos de normas distintas bajo un mismo `norm.id`; ejemplos como `reglamento_0`, `acuerdo_0`, `ley_1`, `reglamento_municipal_municipal` agrupan múltiples `nValor2` y títulos jurídicos distintos. En la muestra general fuera de esas 521 también hubo 2/50 falsos agrupamientos. Por tanto, cualquier uso público de `norm.id` o de `article.id` como identidad canónica requiere endurecimiento previo.

La parte aprovechable directamente como evidencia es el raw y sus vínculos; la parte derivada utilizable con caveats son publication hints, version evidence, texto normalizado como traza revisable y afectaciones extraídas desde la superficie correcta. La parte no confiable para publicación directa es identidad canónica, agrupación, segmentación de artículos como conteo completo, clasificación `ambiguous_scij_page`, y segmentación Gaceta.

## 2. Metodología

Se usó el inventario previo solo como contexto agregado, no como fuente de correctitud. El ground truth fue siempre el raw: HTML SCIJ bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/` y PDFs Gaceta bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/`. La DB se abrió en modo read-only con URI `file:/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza_runtime.db?mode=ro&immutable=1`.

Docs y código leídos para entender intención heredada:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/ARCHITECTURE.md`: define adquisición correcta, refinement determinístico y persistencia canónica auditable.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/ID_POLICY.md`: separa identidad SCIJ `nValor1:nValor2[:nValor3]` de `norm.id`; prohíbe perder `nValor3` cuando importa.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/DB_ROLES.md`: `plaza_runtime.db` es DB operacional; `plaza.db` es producto limpio.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/RUNTIME_ARTIFACT_GOVERNANCE.md`: raw, normalized, manifests y reports son runtime artifacts.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/OBSERVABILITY.md`: runtime artifacts y reports no son verdad canónica automática.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/db/repository/README.md`: divide repositorios de canonical, campaign, coverage, surfaces y summary.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/scij/norm_parser.py`: parsea HTML SCIJ a `norm`, `full_text`, `raw_text`, `articles`, `identity`, `version_evidence`, `page_kind`.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/scij/article_parser.py`: detecta encabezados de artículos/transitorios por regex y segmenta.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/scij/extract_scij_version_evidence.py`: extrae banners/version metadata.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/scij/identity_resolver.py`: resuelve `norm_id` desde tipo, número, sufijo y título.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/scij/extract_ficha_metadata.py`: extrae metadata y publication hints de ficha.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/scij/extract_ficha_tabs.py`: extrae afectaciones, concordancias y tabs.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/persist/scij/norm_writer.py`: persiste `norm`, `norm_version`, `article`, `article_version` y normalized JSON.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/persist/scij/surfaces.py`: persiste ficha y tabs SCIJ.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/db/repository/coverage_repo.py`: persiste coverage state.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/domain/scij/outcomes.py`: define `not_attempted`, `surface_present_and_rows_persisted`, etc.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/gaceta/segmenter.py`: segmenta Gaceta por headers/patrones.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/src/pipeline/refinement/gaceta/classifier.py`: clasifica familias documentales.

Definiciones operativas:

- Correcto en texto SCIJ: `raw_text`, `full_text` o `article_version.text` aparece en el HTML raw con cobertura token >= 0,98, permitiendo normalización de espacios y acentos.
- Correcto en identidad de adquisición: el stem `scij_<nValor1>_<nValor2>_<nValor3>_...` y la URL raw coinciden, y el artefacto derivado conserva identidad nativa suficiente para auditar.
- Correcto en agrupación: los artefactos agrupados bajo un `norm.id` describen la misma norma jurídica, no solo el mismo tipo o número genérico.
- Correcto en artículos: el conteo de artículos persistidos de la versión corriente coincide con el contador SCIJ visible `(N artículos)` y los textos spot-checkeados son trazables al raw.
- Correcto en afectaciones: cada fila DB corresponde a una entrada visible en `nrm_norma_afectaciones.aspx`, y cada entrada visible está representada; `operation_type` debe coincidir con `Afectación:`.
- Correcto en pub hints: número de Gaceta, fecha y alcance coinciden con la ficha raw; para post-2006, el PDF local de esa fecha existe y su portada contiene el mismo número.
- Correcto en surface coverage: la categoría declarada corresponde a la presencia o ausencia observable de la superficie raw.
- Correcto en Gaceta segmentation: el segmento corresponde a una unidad documental coherente, su familia/sección es compatible con el texto, y `page_start/page_end` contiene el texto en el PDF raw.

Limitaciones:

- No se hizo interpretación jurídica experta. Si una relación requiere juicio jurídico más allá del texto visible SCIJ, se marca como no verificable por el agente.
- Las tasas son estimaciones de muestra; los intervalos reportados son Wilson 95%.
- El chequeo de texto usa equivalencia textual normalizada, no diff legal línea por línea.
- En Gaceta, `pdftotext` puede introducir diferencias de orden de columnas; aun así, los segmentos con contaminación y rangos malos fueron observables por contenido y longitud.

## 3. Refinement (raw → normalized JSON)

Muestra: 100 normalized JSONs bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/`, estratificados por `page_kind` observado: 50 `texto`, 20 sin `page_kind`, 15 `texto_shell`, 10 `ficha`, 3 `tab`, 2 `pronunciamiento`. Tipos normativos en muestra: `resolucion` 14, `decreto_ejecutivo` 13, `reglamento` 12, `ley` 12, `acuerdo` 10, `directriz` 8, `codigo` 7, `reglamento_municipal` 6, `constitucion` 6, `acuerdo_municipal` 5, más categorías menores.

Según código, esta etapa hace `extract_main_text`, normaliza texto SCIJ, extrae metadata estructurada, clasifica tipo normativo, segmenta artículos, detecta version evidence y clasifica `page_kind`. La salida esperada es un JSON revisable con `norm`, `full_text`, `raw_text`, `articles`, `identity`, `version_evidence`, `page_kind`.

### Tasas

| Subcategoría | Correcto | Error observado | IC 95% del error | Veredicto |
|---|---:|---:|---:|---|
| `raw_text` trazable al raw | 99/100 | 1,0% | 0,2-5,4% | Confiable con caveats |
| `full_text` trazable al raw | 98/100 | 2,0% | 0,6-7,0% | Confiable con caveats |
| URL vs stem `nValor*` | 98/100 | 2,0% | 0,6-7,0% | Confiable con caveats |
| `identity` conserva `nValor*` nativo | 0/100 | 100,0% | 96,3-100,0% | Necesita endurecimiento |
| Conteo `articles` vs contador SCIJ | 49/100 | 51,0% | 41,3-60,6% | No confiable para conteo |
| Texto de artículos trazable al raw | 96/100 | 4,0% | 1,6-9,8% | Confiable con caveats |
| `version_evidence` | 100/100 | 0,0% | 0,0-3,7% | Confiable |
| `page_kind` | 62/100 | 38,0% | 29,1-47,8% | Necesita endurecimiento |

### Text fidelity

La fidelidad textual general es buena. `raw_text` y `full_text` casi siempre son trazables al HTML visible; no se observó invención sustantiva. Los errores son de pérdida/normalización o cobertura incompleta, no de texto fabricado.

Ejemplos de pérdida o cobertura baja:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_49429_0_f15abf1851_280dd94fa6b3.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_49429_0_f15abf1851_280dd94fa6b3.html`
- Resultado: `raw_text` cobertura 0,973; `full_text` cobertura 0,961.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_64115_106350_c11019da6c_d94f3c6e324c.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_64115_106350_c11019da6c_d94f3c6e324c.html`
- Resultado: `full_text` cobertura 0,980.

### Identity capture

El stem y la URL raw coinciden casi siempre. Pero el objeto `identity` del normalized no guarda los campos nativos `nValor1`, `nValor2`, `nValor3` ni `scij_identifier`; guarda claves como `bootstrap_expected_id`, `norm_id`, `norm_type`, `resolution_method`, `title`, `warnings`. Esto es una limitación de trazabilidad del artefacto derivado, y para una etapa que debe separar identidad SCIJ de identidad Plaza se debe tratar como bug de diseño de salida.

Ejemplos representativos:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_104603_146228_c02b657f89_601cdbbffe6b.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_104603_146228_c02b657f89_601cdbbffe6b.html`
- URL: `nValor1=1&nValor2=104603&nValor3=146228`
- `identity` no conserva `nValor*`.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_59644_66630_7eb7ef3d66_326af1e781b0.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_59644_66630_7eb7ef3d66_326af1e781b0.html`
- URL: `nValor1=1&nValor2=59644&nValor3=66630`
- `identity` no conserva `nValor*`.

### Article extraction

La segmentación de artículos no es confiable para conteo. El patrón dominante es que el parser toma artículos citados dentro de considerandos, transcripciones o anexos como si fueran artículos top-level de la norma, o no detecta artículos top-level cuando el encabezado es irregular. El texto de cada artículo extraído suele existir en el raw, por eso la fidelidad textual puntual es mucho mejor que el conteo.

Ejemplos:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_95543_128903_8d2b43f1d5_a9e35ef66d13.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_95543_128903_8d2b43f1d5_a9e35ef66d13.html`
- SCIJ declara `(1 artículo)`; JSON contiene 22 artículos, varios son artículos citados/transcritos en el cuerpo.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_81132_126333_a86bc4140e_e3043fcf82c4.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_81132_126333_a86bc4140e_e3043fcf82c4.html`
- SCIJ declara `(8 artículos)`; JSON contiene 8 y textos trazables. Este es un caso correcto.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_81560_104051_62a9c90b59_caee2f5b2e41.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_81560_104051_62a9c90b59_caee2f5b2e41.html`
- SCIJ declara `(1 artículo)`; JSON contiene 0 y `page_kind=texto_shell`.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_1829_76999_82d9dab994_410fdfc18d65.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_1829_76999_82d9dab994_410fdfc18d65.html`
- SCIJ declara 367 artículos; JSON contiene 366.

### Version evidence

`version_evidence` fue la etapa más sólida del refinement. En 100/100 muestras, `has_version_banner`, `banner_is_latest`, `version_ordinal`, `version_total`, `version_date` y `latest_version_url` coincidieron con el banner o metadata visible en raw.

Ejemplos correctos:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_104603_146228_c02b657f89_601cdbbffe6b.json`
- Raw dice `Versión de la norma: 1 de 1 del 05/03/2025`; JSON coincide.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_81132_126333_a86bc4140e_e3043fcf82c4.json`
- Raw dice `Versión de la norma: 3 de 3 del 08/07/2021`; JSON coincide.

### Page kind classification

`page_kind` falla sistemáticamente en textos con artículos no detectados o superficies SCIJ tabulares. En 38/100 muestras la clasificación no coincide con la superficie observable por URL y contenido. Errores típicos: texto completo con artículos clasificado como `texto_shell`, falta de `page_kind` en normalizados antiguos, y tabs clasificados como ambiguos.

Ejemplos:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_81560_104051_62a9c90b59_caee2f5b2e41.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_81560_104051_62a9c90b59_caee2f5b2e41.html`
- Esperado: texto; JSON: `texto_shell`.

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_7069_91997_da5dc71781_318a5078acc5.json`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_7069_91997_da5dc71781_318a5078acc5.html`
- SCIJ declara 30 artículos; JSON: `texto_shell`, 0 artículos.

## 4. Identidad y agrupación

Según docs, Plaza debe mantener identidad SCIJ separada de identidad canónica. Según código, `identity_resolver.py` construye `norm_id` desde tipo, número, sufijo y título; para algunas familias agrega sufijo SCIJ, pero para números genéricos como `0`, `1`, `17`, `reglamento_de`, `reglamento_para` el resultado colapsa muchas normas.

### Las 521 sospechosas

Muestra: 30 de 521 normas con más versiones persistidas que `version_total` observado. Se abrieron 3-5 fichas raw por `norm.id`, prefiriendo `ficha` o `texto` por distintos `nValor2:nValor3`.

Resultado: 30/30 son colapsos de normas distintas bajo el mismo `norm.id`. Tasa de colapso observada: 100,0%; IC 95% 88,6-100,0%. Es un bug sistemático, no aleatorio. Correlaciona con tipos y títulos genéricos: reglamentos, acuerdos, resoluciones, leyes antiguas con números repetidos o `0`, y títulos que empiezan con `Reglamento de`, `Reglamento para`, `Acuerdo 0`, `Ley 1`.

Ejemplos:

- `reglamento_municipal_municipal`: 830 versiones persistidas, `version_total` máximo 10.
- Raw 1: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100922_138647_160ecb807f_6cd6e4548399.html`, `Reglamento para la operación y administración del acueducto municipal`.
- Raw 2: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_101190_139099_02c7a2e499_dcc4e3871410.html`, `Reglamento de organización y funcionamiento del mercado`.
- Raw 3: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105151_147360_bc59c395c4_dc2996346a81.html`, `Reglamento de trabajo de la Comisión Institucional de la Municipalidad de Cartago`.

- `reglamento_0`: 542 versiones persistidas, `version_total` máximo 28.
- Raw 1: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100016_137065_2a07c6f682_09b1b3d39916.html`, `Reglamento de teletrabajo de la Empresa de Servicios Públicos de Heredia S. A.`.
- Raw 2: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100428_137904_a25879e987_cf282a84b885.html`, `Reforma Reglamento de cobro de la Autoridad Reguladora de los Servicios Públicos`.
- Raw 3: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100721_138342_ebcba2a749_0c4456788580.html`, `Reglamento para la elaboración de los acuerdos y convenios de cooperación`.

- `ley_1`: 15 versiones persistidas, `version_total` máximo 2.
- Raw 1: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10414_11149_c62a47901a_65075f979e0c.html`, `Devuelve Presidencia República al general Tomás Guardia`.
- Raw 2: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10461_11204_3889886797_9ba1883b23ad.html`, `Dicta reglas para la conservación del fluido vacuno`.
- Raw 3: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_11741_12603_088bc732f2_298bfca01a88.html`, `Abre Sesiones Ordinarias Congreso`.

- `reglamento_de`: 156 versiones persistidas, `version_total` máximo 41.
- Raw 1: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100357_137780_7fb3fd2bcb_928a7391cf97.html`, `Reglamento de organización y funcionamiento del Consejo Presidencial de Inversión Extranjera Directa...`.
- Raw 2: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_102725_142086_745341ba62_002684109e0d.html`, `Reglamento de funcionamiento de la Autoridad de Contratación Pública`.
- Raw 3: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_104004_145148_6046959eff_d33a4c4dd287.html`, `Reglamento de las tareas y funciones del Ministerio de Relaciones Exteriores y Culto`.

### Muestra general

Muestra: 50 normas aleatorias fuera de las 521 sospechosas, con artefactos exitosos. Resultado: 2/50 falsos agrupamientos; tasa 4,0%, IC 95% 1,1-13,5%. El error general existe fuera de la lista sospechosa, pero con menor frecuencia.

Ejemplos:

- `ley_140`
- Raw 1: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_31591_33326_e554c1b10e_bd64e7a63e1d.html`, `Ley Sobre la Adopción (1934)`.
- Raw 2: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_9051_9708_2d61c8860c_2ede3706677c.html`, `Autoriza al Gobierno disponer de rentas y tabacos federales`.

- `resolucion_075`
- Raw 1: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_71826_116866_bffaca069c_5e1a18ee1f4b.html`, autorización genérica Cruz Roja.
- Raw 2: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_87487_123532_539f03fef7_a61950ede267.html`, selección de regímenes y mercancías exentas.
- Raw 3: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_90338_135423_9ed968155a_0ba341e401de.html`, inscripción de personas jurídicas inactivas.

### Source documents huérfanos

Muestra: 20 `source_document` SCIJ no referenciados por `scij_crawl_artifact`. Resultado: 17/20 eran evidencia raw válida no asociada; 3/20 además tenían `normalized_path`, es decir, derivado existente pero sin crawl artifact. No se observó basura en la muestra.

Ejemplos:

- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_45655_0_ea61016958_7b649d935c61.html`: ficha válida, `Reglamento al artículo 84 del Código Municipal Ley N° 7794`, sin artifact asociado.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_52446_0_45250039d0_438077f61d38.html`: texto válido, `Reglamento de viajes al interior del país`, sin artifact asociado.
- `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_46204_0_f4fd9c0f8f_bfe817898555.html`: texto válido y `normalized_path` presente, pero sin artifact asociado.

## 5. Article extraction en DB

Según código, `norm_writer.py` persiste `article` y `article_version` desde `parsed["articles"]`; el `article_id` depende de `norm_id`, número y tipo de artículo. Por eso cualquier error de identidad se propaga a artículos.

Muestra: 50 normas con artículos persistidos. Estratificación efectiva: 25 simples (1-10 artículos), 15 medias (11-50), 10 complejas (>50), incluyendo `constitucion_politica`, `codigo_trabajo`, `ley_7092`.

### Tasas

| Subcategoría | Correcto | Error observado | IC 95% del error | Observación |
|---|---:|---:|---:|---|
| Conteo de artículos DB vs contador SCIJ | 35/50 | 30,0% | 19,1-43,8% | Error material |
| Texto spot-check de 3 artículos por norma | 42/50 | 16,0% | 8,3-28,5% | Mejor que conteo, pero no seguro |
| Versionado sin flags simples de duplicación/current múltiple | 50/50 | 0,0% observado | 0,0-7,1% | Limitado a checks mecánicos |

Patrones de error:

- Complejas: conteos altos desalineados por artículos citados, transitorios, anexos o deduplicación.
- Simples: encabezados pegados o puntuación SCIJ reducen cobertura textual aunque el contenido sea reconocible.
- Múltiples versiones: se observaron normas multi-versionadas, pero el muestreo no prueba completitud histórica; el inventario ya mostró que no es completa.

Ejemplos:

- `constitucion_politica`: correcto en conteo corriente.
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_871_929_757f44c3c6_981ba13ac8a0.html`
- DB: 197 `article_version` corrientes; SCIJ declara 197.

- `codigo_trabajo`: incorrecto en conteo.
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_8045_83262_b416795935_b1eb4ae5c3a0.html`
- DB: 644 `article_version` corrientes; SCIJ declara 627.

- `ley_7092`: incorrecto en conteo.
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10969_118267_c898617860_8160f15da481.html`
- DB: 106 `article_version` corrientes; SCIJ declara 111.

- `codigo_fiscal`: incorrecto en conteo.
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_494_143685_8950a05ab2_50c8b0fea6cf.html`
- DB: 741 `article_version` corrientes; SCIJ declara 747.

- `decreto_ejecutivo_29848`: incorrecto en conteo y texto spot-check.
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_47217_0_d951a53ca6_3ca524b75bd3.html`
- DB: 3 artículos; SCIJ declara 4; coberturas de artículos chequeados 0,967, 0,971 y 0,857.

- `reglamento_8114`: incorrecto en conteo y texto spot-check.
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_58770_0_7c786afa49_1b715f37e769.html`
- DB: 24 artículos; SCIJ declara 47.

## 6. Affectation extraction

Según código, `extract_afectaciones_from_html` y `_persist_explicit_tab_surface` parsean HTML de `nrm_norma_afectaciones.aspx` y persisten filas en `norm_afectada`. Una salvedad importante: `norm_afectada` también contiene filas provenientes de `nrm_concordancias.aspx`. En la DB observada, `norm_afectada` tiene 57.256 filas con `source_url` `nrm_concordancias.aspx` y 13.223 con `nrm_norma_afectaciones.aspx`. Esta mezcla de semánticas es un bug de modelado/persistencia para la tabla, aunque la extracción de la superficie de afectaciones sea buena.

Muestra: 40 normas con filas `norm_afectada` cuyo `source_url` era `nrm_norma_afectaciones.aspx` y con artifact raw exitoso de `surface='afectaciones'`.

### Tasas sobre `nrm_norma_afectaciones.aspx`

| Métrica | Resultado | IC 95% |
|---|---:|---:|
| Precision | 75/75 = 100,0% | 95,1-100,0% |
| Recall | 75/76 = 98,7% | 92,9-99,8% |
| Tipo de afectación correcto | 74/75 = 98,7% | 92,8-99,8% |
| Páginas completamente correctas | 39/40 | No se generaliza por baja N de errores |

La extracción desde la superficie correcta es confiable con caveats. El error observado fue una relación visible adicional no emparejada y un tipo no coincidente en una página con múltiples operaciones sobre la misma norma afectada.

Ejemplos correctos:

- `decreto_ejecutivo_11693`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_20021_21310_ba8c3df20e_0fec54696715.html`
- DB: `Derogación`, `Modo: Expreso`, afectada `Decreto Ejecutivo 11464`; raw coincide.

- `ley_1679`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_35105_37019_6ade330f59_c457a3678173.html`
- DB: `Ampliación`, afectada `Ley 8`, artículo afectado 9; raw coincide.

- `reglamento_del_scij_1_44092_46457`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_44092_46457_0d500367ec_38401bcab4fe.html`
- DB: 6 filas; raw: 6 entradas; tipos coinciden.

Ejemplo con error:

- `ley_6934`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_7936_114405_be08db094e_6551dcf1c207.html`
- DB: 2 filas; raw: 3 entradas; match DB 2/2, recall raw 2/3, type 1/2.

## 7. Publication hints

Según código, `extract_ficha_metadata.py` extrae `norm_publication_hint` desde la ficha SCIJ: número de Gaceta, fecha de publicación, alcance y campos relacionados. Esta etapa no decide por sí sola que el PDF existe ni que el segmento Gaceta esté bien; solo registra el vínculo bibliográfico visible en SCIJ.

Muestra: 30 normas con `publication_date` y `gaceta_number`, estratificadas en 10 pre-2006, 10 de 2006-2020 y 10 post-2020. El ground truth primario fue la ficha SCIJ raw. Para 2006-2020 y post-2020 también se abrió el PDF local cuando existía.

### Tasas por época

| Estrato | Contra ficha SCIJ | Contra PDF Gaceta local | Veredicto |
|---|---:|---:|---|
| Pre-2006 | 10/10 correcto | No aplica en esta muestra | Confiable contra ficha |
| 2006-2020 | 10/10 correcto | 10/10 correcto | Confiable con caveats |
| Post-2020 | 10/10 correcto | 10/10 correcto | Confiable con caveats |
| Total ficha | 30/30 correcto; IC 95% 88,6-100,0% correcto | No aplica | Confiable con caveats |
| Total PDF aplicable | No aplica | 20/20 correcto; IC 95% 83,9-100,0% correcto | Confiable en muestra |

En la muestra revisada, número de Gaceta, fecha y alcance coincidieron con la ficha. Para los 20 casos post-2006 auditados contra PDF, el archivo local existía y `pdftotext` de la portada contenía el mismo número de Gaceta. Esto valida el hint como referencia bibliográfica; no valida todavía que la segmentación Gaceta de esa edición haya extraído correctamente la norma.

Ejemplo pre-2006 correcto contra ficha:

- `ley_7607`
- Ficha raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_25026_0_5a405dbb2b_0d501b70f286.html`; DB/ficha: `Gaceta 115`, `18/06/1996`.
- PDF local no exigido para este estrato.

Ejemplos 2006-2020 correctos:

- `reglamento_1070`
- Ficha raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_88124_114989_ddcf082574_85982cb12320.html`; DB/ficha: `Gaceta 20`, `29/01/2019`.
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2019-01-29.pdf`, portada: `La Gaceta N° 20`.

- `decreto_ejecutivo_41704`
- DB/ficha: `Gaceta 146`, `06/08/2019`.
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2019-08-06.pdf`, portada: `La Gaceta N° 146`.

- `ley_9436`
- DB/ficha: `Gaceta 211`, `08/11/2017`.
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2017-11-08.pdf`, portada: `La Gaceta N° 211`.

Ejemplos post-2020 correctos:

- `resolucion_1250`
- DB/ficha: `Gaceta 145`, `10/08/2023`.
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2023-08-10.pdf`, portada: `La Gaceta N° 145`.

- `ley_10554`
- DB/ficha: `Gaceta 205`, `01/11/2024`.
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2024-11-01.pdf`, portada: `La Gaceta N° 205`.

- `resolucion_00011`
- DB/ficha: `Gaceta 48`, `12/03/2025`.
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2025-03-12.pdf`, portada: `La Gaceta N° 48`.

Limitación: para normas pre-2006 no se exigió PDF local porque el inventario y la cobertura histórica no garantizan disponibilidad homogénea. Se trató como validación contra ficha SCIJ, no contra colección completa Gaceta.

## 8. Surface coverage classification

Según `coverage_repo.py` y `outcomes.py`, `scij_norm_surface_coverage` no es una tabla de verdad jurídica; es estado operacional de intentos de cobertura por superficie. Aun así, se auditó si las categorías observadas reflejan correctamente la presencia/ausencia de raw.

Distribución observada de `outcome_state`:

| Outcome | Conteo |
|---|---:|
| `not_attempted` | 184.490 |
| `surface_present_and_rows_persisted` | 45.779 |
| `surface_absent` | 36.518 |
| `surface_present_and_parsed_no_rows` | 14.540 |
| `fetch_failed` | 180 |
| `surface_present_but_empty` | 22 |

Distribución relevante de `last_page_kind`:

| Page kind | Conteo |
|---|---:|
| `ambiguous_scij_page` | 25.540 |
| `valid_ficha_norm` | 19.254 |
| `shell_with_norm_content` | 19.103 |

### Spot checks

| Categoría auditada | Resultado | IC 95% | Veredicto |
|---|---:|---:|---|
| `surface_present_and_rows_persisted` | 20/20 correctos | 83,9-100,0% correcto | Confiable en muestra |
| `ambiguous_scij_page` | 18/20 falsos negativos | 69,9-97,2% error | No confiable como ausencia |
| `not_attempted` | 18/20 sin raw success; 2/20 stale | 2,8-30,1% stale | Estado operacional, no verdad final |

Hallazgos:

- `surface_present_and_rows_persisted` sí significó raw con marcador y filas parseadas en 20/20 casos revisados.
- `ambiguous_scij_page` no debe interpretarse como ausencia de superficie. En 18/20 casos había marcadores claros de contenido útil, pero la clasificación se quedó en ambigua.
- `not_attempted` normalmente significa que la superficie no fue intentada o no tiene raw exitoso asociado, pero se observaron 2/20 casos stale donde sí existía raw útil.

Ejemplos:

- `scij_cov_954eda1f1362b2dd9ab3`, `surface=concordancias`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_102170_141181_03b5d29946_54c4776b21db.html`
- Observación: el raw contiene superficie tabular clara aunque la clasificación operacional puede quedar como ambigua.

- `scij_cov_0fbd8c42c6debcaa31b2`, `surface=afectaciones`, `norm_id=codigo_familia`
- Raw: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_970_1037_42200057d7_eda358f7fa27.html`
- Observación: ejemplo de superficie presente con filas persistidas.

- `scij_cov_397d6f70c871b933f303`, `surface=descriptores`
- Observación: `surface_absent` sin raw útil observable en el spot check.

Conclusión: coverage sirve para observabilidad operacional, priorización de backfill y trazabilidad de intentos. No debe usarse como verdad canónica de que una superficie existe/no existe salvo para estados positivos con raw verificado.

## 9. Gaceta segmentation

Según `segmenter.py`, la segmentación Gaceta usa headers, patrones textuales y metadatos de edición para dividir PDFs en documentos. Según `classifier.py`, asigna familia/section. La auditoría comparó 20 segmentos de `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/extracted_parallel/` contra PDFs raw en `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/`.

Advertencia de trazabilidad: varios JSON de segmentos tienen `source_evidence.pdf_path` apuntando a `/mnt/Tokyo/Lab/Git/Plaza/data/sources/gaceta/raw/...`, ruta fuera de `archive/old` y stale para esta auditoría. La verificación usó el PDF equivalente bajo `archive/old`.

### Tasas

| Subcategoría | Resultado | Error observado | IC 95% del error | Veredicto |
|---|---:|---:|---:|---|
| Segmento como unidad documental coherente | 5/20 correcto | 75,0% | 53,1-88,8% | No confiable |
| Clasificación family/section compatible | 17/20 correcto | 15,0% | 5,2-36,0% | Mejor, pero dependiente del segmento |
| Rango `page_start/page_end` contiene el texto | 9/20 correcto | 55,0% | 34,2-74,2% | No confiable |

Patrones observados:

- 6/20 segmentos tenían contaminación de cuerpo: furniture, headers, índice o texto ajeno mezclado con la unidad documental.
- 5/20 eran segmentos excesivamente largos que acumulaban múltiples documentos o secciones.
- 1/20 contenía explícitamente más de un item documental dentro del mismo segmento.
- La clasificación de familia suele ser razonable cuando el segmento empieza con un header fuerte, pero puede ser correcta por accidente aunque el segmento esté contaminado.

Comparación con el audit heredado `segmentation_raw_audit.md`: el hallazgo se confirma en magnitud y patrón. La muestra heredada reportaba 59% body contamination y 32% long segment rate en 8 issues; esta muestra observó 6/20 con contaminación explícita de cuerpo y 5/20 segmentos largos, pero la métrica más estricta de unidad documental coherente falló en 15/20. Por tanto, el problema no se atenúa; se confirma que la segmentación legacy no produce documentos limpios de forma suficientemente confiable.

Ejemplos con problemas:

- `gaceta_2008-07-29_seg_000_8b45e8e8`
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2008-07-29.pdf`
- Observación: `page_start=1`, `page_end=3`, longitud 45.350, 10 headers detectados, furniture presente; no es una unidad documental limpia.

- `gaceta_2014-03-27`
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2014-03-27.pdf`
- Observación: segmento con contaminación y rango de páginas insuficientemente confiable.

- `gaceta_2020-01-07`
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2020-01-07.pdf`
- Observación: segmentación no permite afirmar unidad documental final sin revisión adicional.

- `gaceta_2023-01-16`
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2023-01-16.pdf`
- Observación: rango y coherencia del segmento fallan en el spot check.

- `gaceta_2026-01-15`
- PDF: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2026-01-15.pdf`
- Observación: segmento contaminado o demasiado amplio para publicación como documento individual.

Conclusión: Gaceta raw y el vínculo bibliográfico son útiles; los segmentos legacy no son suficientemente correctos para corpus público sin resegmentación o validación fuerte.

## 10. Veredicto por etapa

| Etapa | Veredicto | Tamaño del problema | Remediación sugerida |
|---|---|---|---|
| Refinement SCIJ raw → normalized JSON | Necesita endurecimiento | Texto mayormente fiel (`raw_text` 99/100, `full_text` 98/100), pero `identity` no conserva `nValor*` en 100/100, conteo de artículos falla en 51/100 y `page_kind` falla en 38/100. | Re-correr refinement preservando identidad nativa explícita, validar `page_kind` por URL/superficie, y marcar artículos como provisionales hasta reconciliar contra contador SCIJ. |
| Version evidence | Confiable | 100/100 correcto contra banner raw; IC 95% de error 0,0-3,7%. | Usable como señal derivada, manteniendo link al raw y sin inferir completitud histórica. |
| Identity clustering (`norm.id`) | No confiable | 30/30 sospechosas eran colapsos; 2/50 falsos agrupamientos en muestra general. | No usar `norm.id` legacy como URI canónica; separar por identidad SCIJ y re-agrupar con reglas auditables antes de publicar identidad estable. |
| `source_document` huérfanos | Necesita endurecimiento | 17/20 huérfanos eran evidencia válida no asociada; 3/20 tenían normalized existente. | Backfill de provenance y asociación; no descartar huérfanos sin revisión porque contienen raw útil. |
| Article extraction en DB | Necesita endurecimiento | Conteo DB vs SCIJ falló en 15/50; texto spot-check falló en 8/50. | Re-extraer o validar artículos contra contador SCIJ y raw; marcar `article.id` como provisional donde dependa de `norm.id` colapsado. |
| Affectation extraction desde `nrm_norma_afectaciones.aspx` | Confiable con caveats | Precision 75/75, recall 75/76, tipo correcto 74/75; pero `norm_afectada` mezcla concordancias y afectaciones. | Separar semánticamente filas por superficie fuente y mantener evidencia raw; revalidar páginas con múltiples operaciones sobre la misma norma afectada. |
| Publication hints | Confiable con caveats | 30/30 correcto contra ficha; 20/20 correcto contra PDF aplicable. | Usar como referencia bibliográfica con fuente raw; no usar como prueba de segmentación Gaceta correcta. |
| Surface coverage classification | Necesita endurecimiento | `surface_present_and_rows_persisted` 20/20 correcto, pero `ambiguous_scij_page` fue falso negativo en 18/20 y `not_attempted` tuvo 2/20 stale. | Tratar coverage como estado operacional; re-clasificar ambiguos antes de usarlos como ausencia de superficie. |
| Gaceta segmentation | No confiable | Solo 5/20 segmentos fueron unidades documentales coherentes; 11/20 rangos de páginas malos; confirma audit heredado. | Re-segmentar o validar fuertemente contra PDF antes de publicar segmentos como documentos normativos. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza.db` | No confiable como corpus | Inventario reportó tablas corpus principales vacías. | No usar como fuente corpus; usar `plaza_runtime.db` solo con las cautelas por tabla indicadas arriba. |

## 11. Riesgos para canonicalización

Bloquean publicación de URIs canónicas:

- `norm.id` legacy no es identidad estable confiable. Los colapsos sistemáticos de normas distintas bajo IDs genéricos invalidan URIs basadas directamente en ese campo.
- La agrupación de versiones bajo `norm.id` no es confiable en las 521 sospechosas y tiene falsos agrupamientos incluso fuera de ellas. Publicar versiones bajo esa agrupación puede mezclar historias normativas distintas.
- `article.id` hereda errores de `norm.id` y además depende de una segmentación de artículos con 30,0% de error de conteo en la muestra DB. Publicar URIs de artículos desde esta tabla puede asignar textos reales a pertenencias incorrectas.
- `identity` del normalized no conserva explícitamente `nValor1`, `nValor2`, `nValor3`, por lo que el artefacto derivado solo no basta para reconstruir identidad SCIJ sin filename, URL o DB.
- Segmentos Gaceta no son documentos normativos limpios en 15/20 casos revisados; no deben ser base directa de URIs documentales.

Gestionable con provisionalidad agresiva:

- `raw_text` y `full_text` SCIJ son útiles como derivado textual revisable, siempre subordinados al HTML raw y no como texto legal certificado.
- `version_evidence` es confiable como lectura del banner raw, pero no como garantía de que todas las versiones históricas fueron capturadas.
- `norm_publication_hint` es confiable como referencia bibliográfica extraída de ficha, pero no certifica que exista un segmento Gaceta correcto.
- Afectaciones extraídas desde `nrm_norma_afectaciones.aspx` son utilizables con caveats si se separan de concordancias y se conserva evidencia raw por fila.
- `surface_present_and_rows_persisted` es confiable como estado positivo en la muestra; `ambiguous_scij_page`, `not_attempted` y `surface_absent` no deben usarse sin raw como prueba negativa fuerte.

No verificable por el agente:

- Equivalencia jurídica fina entre textos consolidados, reformas y derogatorias cuando requiere interpretación legal experta más allá de la fila visible en SCIJ.
- Determinación final de cuál debe ser la identidad canónica pública cuando varias capturas SCIJ representan versiones, textos compilados, fichas y superficies auxiliares de una misma norma.
- Validez jurídica de la publicación Gaceta más allá de que número, fecha y portada del PDF coincidan con la ficha SCIJ.

## 12. Anexos

### Conteos de muestras inspeccionadas por fase

| Fase | Muestra efectiva | Estratificación o foco |
|---|---:|---|
| Refinement SCIJ | 100 normalized JSONs | `texto` 50, sin `page_kind` 20, `texto_shell` 15, `ficha` 10, `tab` 3, `pronunciamiento` 2; tipos normativos mezclados. |
| Identidad sospechosa | 30 normas | Muestra de las 521 con más versiones persistidas que `version_total`. |
| Identidad general | 50 normas | Aleatorias fuera de las 521 sospechosas. |
| `source_document` huérfanos | 20 documentos | SCIJ sin referencia desde `scij_crawl_artifact`. |
| Artículos DB | 50 normas | 25 simples, 15 medias, 10 complejas; incluyó `constitucion_politica`, `codigo_trabajo`, `ley_7092`. |
| Afectaciones | 40 normas/páginas | Normas con filas `norm_afectada` y raw de `nrm_norma_afectaciones.aspx`. |
| Publication hints | 30 normas | 10 pre-2006, 10 2006-2020, 10 post-2020. |
| Surface coverage | 60 filas | 20 `ambiguous_scij_page`, 20 `surface_present_and_rows_persisted`, 20 `not_attempted`. |
| Gaceta segmentation | 20 segmentos | 5 issues distintos, mezcla de años y tamaños. |

### Comandos representativos

- DB read-only usada en scripts Python: `file:/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza_runtime.db?mode=ro&immutable=1`.
- Verificación de portada Gaceta: `pdftotext -f 1 -l 1 /mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_YYYY-MM-DD.pdf -`.
- Verificación final de no modificación tracked bajo archive: `git status --short --untracked-files=no -- "archive/old"`.
- Verificación de marcadores temporales pendientes en `/mnt/Tokyo/Lab/Git/Plaza/CORRECTNESS_AUDIT_REPORT.md`.

### Errores concretos reproducibles

| Categoría | Path o ID | Hallazgo |
|---|---|---|
| Article extraction normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_95543_128903_8d2b43f1d5_a9e35ef66d13.json` | SCIJ declara 1 artículo; JSON contiene 22 por captura de artículos citados/transcritos. |
| Article extraction normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_81560_104051_62a9c90b59_caee2f5b2e41.json` | SCIJ declara 1 artículo; JSON contiene 0 y `page_kind=texto_shell`. |
| Identity clustering | `reglamento_municipal_municipal` | Agrupa raw distintos: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100922_138647_160ecb807f_6cd6e4548399.html`, `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_101190_139099_02c7a2e499_dcc4e3871410.html`, `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105151_147360_bc59c395c4_dc2996346a81.html`. |
| Identity clustering | `reglamento_0` | Agrupa normas distintas bajo número genérico `0`; ejemplos en `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100016_137065_2a07c6f682_09b1b3d39916.html` y `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100428_137904_a25879e987_cf282a84b885.html`. |
| Article extraction DB | `codigo_trabajo` | DB tiene 644 `article_version` corrientes; SCIJ declara 627 en `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_8045_83262_b416795935_b1eb4ae5c3a0.html`. |
| Article extraction DB | `ley_7092` | DB tiene 106 `article_version` corrientes; SCIJ declara 111 en `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10969_118267_c898617860_8160f15da481.html`. |
| Affectation extraction | `ley_6934` | DB tiene 2 filas, raw tiene 3 entradas visibles; raw `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_7936_114405_be08db094e_6551dcf1c207.html`. |
| Publication hint | `ley_7607` | Correcto contra ficha pre-2006; raw `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_25026_0_5a405dbb2b_0d501b70f286.html`, `Gaceta 115`, `18/06/1996`. |
| Surface coverage | `scij_cov_954eda1f1362b2dd9ab3` | Ejemplo de clasificación operacional ambigua pese a raw tabular claro en `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_102170_141181_03b5d29946_54c4776b21db.html`. |
| Gaceta segmentation | `gaceta_2008-07-29_seg_000_8b45e8e8` | Segmento no limpio: longitud 45.350, 10 headers, furniture; PDF `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2008-07-29.pdf`. |

### Limitaciones explícitas

- Los IC son Wilson 95% sobre muestras, no garantías exhaustivas por fila.
- La auditoría textual normaliza espacios y acentos; no sustituye revisión legal línea por línea.
- En Gaceta, `pdftotext` puede alterar orden de columnas; los errores reportados fueron suficientemente grandes para observarse aun con esa limitación.
- No se interpretó derecho sustantivo; relaciones que requieren juicio jurídico quedan como no verificables por el agente.
- `not_attempted` y estados similares se evaluaron como estados operacionales, no como prueba de ausencia documental.
