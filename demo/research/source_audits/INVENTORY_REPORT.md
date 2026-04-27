# Plaza — Inventario del Scrape Histórico
**Fecha:** 2026-04-24
**Alcance auditado:** /mnt/Tokyo/Lab/Git/Plaza/archive/old/

## 1. Resumen ejecutivo

El scrape histórico es una base útil como evidencia y como insumo bruto. La parte más fuerte está en SCIJ: hay 80.222 HTML bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/`, 80.234 manifiestos JSON bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/`, 23.152 normalizaciones JSON bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/`, y una base operacional fuerte en `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza_runtime.db`. Esa DB conserva 79.643 `source_document`, 66.709 `scij_crawl_artifact`, 15.964 normas, 21.872 versiones, 231.948 artículos y 355.810 versiones de artículo.

La porción usable tal cual es la evidencia cruda y su trazabilidad: HTML SCIJ, manifiestos, hashes, URLs con `nValor1:nValor2:nValor3`, PDFs de La Gaceta y reportes operativos. La porción que necesita limpieza antes de considerarse corpus estructurado son las normalizaciones, los conteos de versiones históricas y varias identidades canónicas sospechosas. La DB limpia `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza.db` no es fuente útil de producto: tiene 23 tablas pero 0 filas en `norm`, `norm_version`, `article`, `article_version` y `norm_metadata`.

Con una definición estricta de cobertura completa por norma, usando `plaza_runtime.db`, hay 3.195 normas con ficha + texto + afectaciones HTML + identificador SCIJ; 3.186 de esas además tienen `norm_publication_hint`. Hay 12.769 normas parciales dentro de las 15.964 normas canónicas de `norm`. La mayor brecha estricta es `afectaciones`: 11.093 normas tienen ficha, 11.096 tienen texto, pero solo 3.197 tienen una página HTML de afectaciones capturada con éxito y vinculada a `norm_id`.

La pregunta de versiones históricas no se puede contestar como “sí, completo”. El scrape no captura solo vigente: `norm_version` tiene 21.872 filas y 5.908 no son actuales, y hay muestras con versiones históricas normalizadas. Pero tampoco captura cadenas históricas completas: 4.936 normas tienen menos versiones persistidas que el `version_total` observado en SCIJ, todos los 66.709 `scij_crawl_artifact` declaran `version_harvest_mode='resolved_version_only'` y `version_chain_status='single_version_only'`, y `valid_to` está vacío en todas las versiones. Conclusión operativa: hay evidencia histórica parcial, no corpus histórico completo.

Gaceta es útil como corpus documental y fuente de publicación para el rango cubierto. Hay 5.164 PDFs bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/`, 5.276 manifiestos regulares y 5.150 extracciones paralelas JSON. Los reportes heredados declaran 5.276 issues, 5.002 con secciones, 52.068 secciones normalizadas y 99,855% de cobertura de clasificación de segmentos, pero otro reporte marca problemas de segmentación: 59,108% de contaminación de cuerpo y 31,897% de segmentos largos en una muestra de 8 issues. Por tanto, Gaceta sirve como evidencia y texto extraído, pero sus segmentos derivados no deberían tratarse como verdad final sin QA.

## 2. Trazabilidad heredada

### Estructura observada

| Ruta | Contenido relevante |
|---|---:|
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/` | `README.md`, `CLAUDE.md`, `docs/`, `data/`, `src/`, `scripts/`, `tests/`, `archive/`, `oldplaza_SCIJ.tar.xz` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/` | `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `DB_ROLES.md`, `ID_POLICY.md`, `OBSERVABILITY.md`, `RUNTIME_ARTIFACT_GOVERNANCE.md`, `REPORTING_AND_LOGS_POLICY.md`, `DOC_INVENTORY.md`, `requirements/`, `roadmaps/`, `traceability/`, `research/` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/` | `db/`, `reports/`, `sources/`, `logs/`, `status/`, `debug_scij/`, `pids/` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/` | `scij/`, `gaceta/` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/` | `raw/`, `manifests/`, `normalized/`, `extracted/`, scripts de análisis |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/` | `raw/`, `manifests/`, `extracted_parallel/`, `extracted_reextract/`, `extracted_sample/`, `archive/`, reportes JSON/MD, logs/checkpoints |

### Documentos de autoridad leídos

| Ruta absoluta | Evidencia usada |
|---|---|
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/README.md` | Define Plaza como pipeline “SQLite-first”, “SCIJ-first”, con preservación de raw y normalizados; runtime bajo `data/`; `plaza_runtime.db` como DB activa. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/CLAUDE.md` | Reitera que la misión es corrección y auditabilidad SCIJ; identidad SCIJ `nValor1:nValor2[:nValor3]`; raw evidence authoritative. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/ARCHITECTURE.md` | Declara dos capas durables: source artifacts bajo `data/sources/` y estado relacional en SQLite. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/DB_ROLES.md` | Define roles: `plaza_runtime.db` para adquisición/diagnóstico, `plaza.db` para producto limpio, `plaza_campaigns.db` para campañas. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/ID_POLICY.md` | Define `scij_identifier = nValor1:nValor2:nValor3` cuando hay versión; prohíbe colapsar `nValor3` cuando importa para versión/tab. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/RUNTIME_ARTIFACT_GOVERNANCE.md` | Define ubicación esperada de reportes, manifiestos, raw/normalized/extracted. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/docs/REPORTING_AND_LOGS_POLICY.md` | Confirma que reportes y manifiestos son runtime artifacts, no docs canónicos automáticamente. |

### Reportes heredados relevantes

| Ruta absoluta | Resumen |
|---|---|
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/reports/scij_raw_inventory_report.md` | Reporta subset SCIJ raw: 67.786 raw files, 67.798 manifiestos, 67.207 source docs, 0 raw sin manifest, 0 manifests sin raw, 0 raw fuera de DB, 812 grupos URL duplicados con hash estable igual. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/reports/scij_raw_inventory_report.json` | Misma evidencia en JSON; contiene muestras de URLs duplicadas y conteos `raw_hashes`/`stable_hashes`. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/CORPUS_CENSUS_REPORT.md` | Declara 5.276 issues, 5.002 issues con secciones, 52.069 secciones raw, 52.068 secciones normalizadas, años 2006-2026. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/corpus_audit.md` | Declara 5.275 outputs válidos, 0 inválidos, 256.672 segmentos, 371 desconocidos, 99,855% coverage, 29 issues con cero segmentos. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/segmentation_raw_audit.md` | En muestra de 8 issues: 2.646 segmentos, 59,108% body contamination, 31,897% long segment rate, 15,306% multi-item segment rate. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/REAL_CORPUS_ANALYSIS.md` | En muestra de 60 PDFs: 0 errores, 60 con texto, promedio 69,1 páginas/issue y 518.165 caracteres/issue. |

### Bases SQLite encontradas

| DB | Tamaño | Tablas | Conteos clave |
|---|---:|---:|---|
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza_runtime.db` | 1.704.812.544 bytes | 51 | `source_document=79.643`, `scij_crawl_artifact=66.709`, `norm=15.964`, `norm_version=21.872`, `article=231.948`, `article_version=355.810` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza.db` | 671.744 bytes | 23 | `norm=0`, `norm_version=0`, `article=0`, `article_version=0`, `norm_metadata=0` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza_campaigns.db` | 16.556.032 bytes | 23 | `source_document=32`, `scij_crawl_artifact=34`, `norm=10`, `article=4.078` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/scij_full_spider.sqlite` | 255.619.072 bytes | 47 | `source_document=11.596`, `norm=4.824`, `article=71.411` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza.sqlite` | 16.154.624 bytes | 46 | DB legacy: `source_document=418`, `norm=199`, `article=5.678` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/scij_broad_campaign.sqlite` | 18.755.584 bytes | 46 | DB campaña: `source_document=524`, `norm=172`, `article=5.080` |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/scij_live_batch.sqlite` | 11.399.168 bytes | 46 | DB campaña: `source_document=32`, `norm=10`, `article=4.078` |

## 3. Inventario cuantitativo

### Totales filesystem bajo `data/sources/`

Total medido bajo `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/`: 211.169 archivos, 52.232.580.524 bytes, 48,6 GiB. Los `.gitkeep` están incluidos solo donde se indica; los conteos de extensiones relevantes excluyen implícitamente `.gitkeep` por no tener extensión de datos.

| Extensión | Archivos | Tamaño total | Tamaño promedio |
|---|---:|---:|---:|
| `.json` | 125.751 | 22,9 GiB | 195.166,9 bytes |
| `.html` | 80.222 | 8,0 GiB | 106.615,7 bytes |
| `.pdf` | 5.164 | 17,8 GiB | 3.705.634,4 bytes |
| `.log` | 12 | 641,8 KiB | 54.769,6 bytes |
| `.md` | 5 | 17,6 KiB | 3.611,8 bytes |
| `.py` | 3 | 32,3 KiB | 11.020,7 bytes |
| `.jsonl` | 1 | 604,9 KiB | 619.456 bytes |

### Distribución por fuente

| Fuente | Archivos | Tamaño total | Tamaño promedio |
|---|---:|---:|---:|
| `scij` | 183.616 | 9,5 GiB | 55.292,2 bytes |
| `gaceta` | 27.552 | 39,2 GiB | 1.527.295,3 bytes |

### Subdirectorios principales SCIJ

| Subdirectorio | Archivos | Tamaño total | Extensión principal | Observación |
|---|---:|---:|---|---|
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/` | 80.223 | 8,0 GiB | 80.222 `.html` | HTML crudo SCIJ; un `.gitkeep`. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/` | 80.235 | 38,9 MiB | 80.234 `.json` | Manifiestos por raw; 12 manifiestos extra sin raw. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/` | 23.153 | 1,5 GiB | 23.152 `.json` | Normalizaciones derivadas, principalmente texto. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/extracted/` | 1 | 0 bytes | `.gitkeep` | No contiene extracciones útiles. |

### Subdirectorios principales Gaceta

| Subdirectorio | Archivos | Tamaño total | Extensión principal | Observación |
|---|---:|---:|---|---|
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/` | 5.165 | 17,8 GiB | 5.164 `.pdf` | PDFs de La Gaceta; un `.gitkeep`. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/manifests/` | 5.277 | 29,1 MiB | 5.276 `.json` | Manifiestos `gaceta_YYYY-MM-DD_regular.json`. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/extracted_parallel/` | 5.150 | 7,0 GiB | `.json` | Extracciones por issue. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/archive/` | 10.524 | 14,2 GiB | `.json` | Archivo derivado; no inspeccionado exhaustivamente. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/extracted_sample/` | 100 | 117,3 MiB | `.json` | Muestra derivada. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/extracted_reextract/` | 38 | 39,4 MiB | `.json` | Re-extracciones puntuales. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/extracted/` | 1 | 0 bytes | `.gitkeep` | Vacío. |
| `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/normalized/` | 1 | 0 bytes | `.gitkeep` | Vacío. |

### Patrones de nombres SCIJ

Los 80.222 HTML SCIJ calzan con el patrón `scij_<nValor1>_<nValor2>_<nValor3>_<hash>_<hash>.html`.

| Métrica | Valor |
|---|---:|
| HTML raw SCIJ vistos | 80.222 |
| Archivos que calzan patrón | 80.222 |
| `nValor1` | 80.222 con `1` |
| `nValor2` distintos | 26.818 |
| pares `nValor2:nValor3` distintos | 30.735 |
| archivos con `nValor3` en nombre | 80.222 |
| raw SCIJ sin manifest por stem | 0 |
| manifest SCIJ sin raw por stem | 12, todos con stem tipo `scij_sin_identificador_...` |
| normalized SCIJ con raw correspondiente | 23.152 |
| raw SCIJ sin normalized | 57.070 |

La diferencia entre el reporte heredado de 67.786 raw y el filesystem actual de 80.222 HTML se explica por la DB: `scij_raw_capture` tiene 67.786 capturas con `surface=null` y 12.436 capturas adicionales etiquetadas como `ficha`, `texto` o `descriptores`.

### Patrones de nombres Gaceta

Los PDFs Gaceta calzan con `gaceta_YYYY-MM-DD.pdf`.

| Métrica | Valor |
|---|---:|
| PDFs raw Gaceta | 5.164 |
| PDFs que calzan patrón | 5.164 |
| Manifiestos regulares | 5.276 |
| Fechas PDF con manifiesto regular | 5.164 |
| PDFs sin manifiesto regular | 0 |
| Manifiestos sin PDF | 112 |
| PDFs con extracción en `extracted_parallel/` | 5.149 |
| PDFs sin extracción en `extracted_parallel/` | 15 |

Los 112 manifiestos Gaceta sin PDF tienen `harvest_status='transport_failure'`, `qa_status='pending'` y `pdf_available=false`. Los 15 PDFs sin extracción paralela tienen manifiesto y `page_count=1`; son fechas feriadas o publicaciones mínimas como `2006-04-14`, `2014-12-25`, `2015-01-01`.

### Tipo de norma en `plaza_runtime.db`

| Tipo | Normas |
|---|---:|
| `decreto_ejecutivo` | 5.457 |
| `reglamento` | 4.924 |
| `ley` | 2.469 |
| `resolucion` | 1.457 |
| `acuerdo` | 1.162 |
| `directriz` | 483 |
| `reglamento_municipal` | 6 |
| `acuerdo_municipal` | 4 |
| `constitucion` | 1 |
| `circular` | 1 |

## 4. Inventario cualitativo

### SCIJ raw HTML

Muestra dirigida: 18 HTML, 2 por superficie principal cuando existía muestra exitosa. Superficies muestreadas: `ficha`, `texto`, `afectaciones`, `concordancias`, `descriptores`, `observaciones`, `pronunciamientos_pgr`, `acciones_constitucionales`, `reglamentaciones`.

| Aspecto | Evidencia |
|---|---|
| Estructura general | HTML ASP.NET de `Sistema Costarricense de Información Jurídica`, con `<form>`, `__VIEWSTATE`, tablas y navegación interna. |
| Identificadores | Las URLs y nombres de archivo conservan `nValor1`, `nValor2`, `nValor3`, `param1`, `strTipM`. Ejemplo: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100004_138235_3b03ecfcf9_555a84e22195.html`. |
| Encoding | En los 18 HTML dirigidos: decodificación `utf-8-sig`, 0 caracteres de reemplazo. En muestra aleatoria adicional de 100 HTML: 0 fallos UTF-8 y 0 caracteres de reemplazo. |
| Charset declarado | Mezclado: fichas y tabs laterales suelen declarar `ISO-8859-1`; textos completos suelen declarar `UTF-8`; los bytes se leyeron limpiamente como UTF-8 con BOM. |
| Tabs visibles | En las 18 muestras aparecen labels de Ficha, Texto Completo, Afectaciones, Concordancias, Reglamentaciones, Descriptores, Observaciones, Pronunciamientos y Acciones de inconstitucionalidad. |
| Contenido de ficha | Breadcrumb tipo `Normativa >> Decreto Ejecutivo 44137 >> Fecha 07/07/2023`, metadata de norma, enlaces a tabs. |
| Contenido de texto | Página `Texto Completo`, con texto legal y banner/version evidence en normalizado cuando existe. |
| Contenido de afectaciones/concordancias | Páginas tabulares o wrappers SCIJ; DB las clasifica como `ambiguous_scij_page` aunque son capturas exitosas. |

Ejemplos muestreados:

| Superficie | Ruta absoluta | Identificador |
|---|---|---|
| ficha | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100004_138235_869fb405bd_955d2bd3c289.html` | `1:100004:138235` |
| texto | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100004_138235_3b03ecfcf9_555a84e22195.html` | `1:100004:138235` |
| afectaciones | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100004_138235_de9f2bd56d_c39470089b74.html` | `1:100004:138235` |
| concordancias | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100001_137041_d7a0678bff_36a2080e7757.html` | `1:100001:137041` |
| descriptores | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100001_137041_0468eaa69b_0963ac7bb087.html` | `1:100001:137041` |
| observaciones | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100715_138333_9a0bf09c48_05e560a72402.html` | `1:100715:138333` |
| pronunciamientos PGR | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_100715_138333_0dcd92b7f6_389ef74bf260.html` | `1:100715:138333` |
| acciones constitucionales | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_104039_146214_a1fcd749dd_63a254e87177.html` | `1:104039:146214` |
| reglamentaciones | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_11208_142854_02ad901ff4_3d0e6e2a8d3c.html` | `1:11208:142854` |

### SCIJ manifiestos

Muestra dirigida: 10 JSON de `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/`.

Cada manifiesto muestreado contiene las llaves `id`, `source_type`, `source_url`, `source_identifier`, `retrieval_date`, `content_hash`, `raw_path`, `mime_type`. Los manifiestos son pequeños, alrededor de 505-518 bytes en las muestras, y apuntan al raw correspondiente. Ejemplo: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_100004_138235_3b03ecfcf9_555a84e22195.json`.

### SCIJ normalizados

Muestra dirigida: 10 JSON de `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/`.

Las llaves observadas son `norm`, `full_text`, `raw_text`, `articles`, `identity`, `detected`, `version_evidence`, `page_kind`. En las 10 muestras, `full_text` y `raw_text` están presentes; `articles` varía de 0 a 20 artículos. `version_evidence` incluye campos como `has_version_banner`, `banner_is_latest`, `version_ordinal`, `version_total`, `version_date`, `latest_version_url`.

Ejemplo con evidencia histórica parcial: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_10000_10703_10d3860267_fe27bb77edbc.json` corresponde a `ley_89`, tiene `version_ordinal=1`, `version_total=2`, `banner_is_latest=false` y `latest_version_url` poblado.

### Gaceta PDFs

Muestra de metadata PDF: 6 PDFs. Rutas muestreadas: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2006-01-02.pdf`, `gaceta_2010-02-03.pdf`, `gaceta_2015-02-16.pdf`, `gaceta_2021-01-04.pdf`, `gaceta_2023-01-16.pdf`, `gaceta_2026-03-20.pdf`.

| PDF | Páginas | Metadata útil |
|---|---:|---|
| `gaceta_2006-01-02.pdf` | 24 | Title `GACETA1ndd.indd`, Creator `Adobe InDesign CS (3.0)`, PDF 1.5, no tagged. |
| `gaceta_2010-02-03.pdf` | 44 | Title `GACETA Nº 23 de la fecha 03 02 2010`, tagged yes. |
| `gaceta_2015-02-16.pdf` | 62 | Title `LA GACETA N° 32 de la fecha 16 02 2015`, tagged yes, AcroForm. |
| `gaceta_2021-01-04.pdf` | 12 | Title `LA GACETA N° 1 de la fecha 04 01 2021`, tagged yes. |
| `gaceta_2023-01-16.pdf` | 220 | Title `LA GACETA N° 6 de la fecha 16 01 2023`, tagged yes. |
| `gaceta_2026-03-20.pdf` | 72 | Title `LA GACETA N° 55 de la fecha 20 03 2026`, tagged yes. |

No revalidé OCR porque el contexto lo daba por cierto: los PDFs tienen texto extraíble. La evidencia heredada de `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/REAL_CORPUS_ANALYSIS.md` reporta 60/60 issues con texto y 0 errores.

### Gaceta manifiestos y extracciones JSON

Muestra dirigida: 6 manifiestos y 6 extracciones para fechas 2006-01-02, 2010-02-03, 2015-02-16, 2021-01-04, 2023-01-16, 2026-03-20.

Los manifiestos tienen llaves `issue_id`, `publication_date`, `issue_family`, `issue_number`, `issue_title`, `source_url_pdf`, `source_url_html`, `retrieval_timestamp`, `pdf_path`, `payload_hash_pdf`, `text_hash`, `page_count`, `html_available`, `pdf_available`, `sections_raw`, `sections_normalized`, `harvest_status`, `qa_status`, `supplements`, `metadata`. Ejemplo: `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/manifests/gaceta_2026-03-20_regular.json`.

Las extracciones en `extracted_parallel/` tienen llaves `issue_id`, `publication_date`, `segment_count`, `family_distribution`, `segments`, `extractions`, `source_evidence`, `build_metadata`. Cada segmento muestreado contiene `segment_id`, `issue_id`, `section`, `section_raw`, `item_index`, `page_start`, `page_end`, `family`, `family_confidence`, `text`, `text_normalized`, `detection_method`, `raw_header`.

Ejemplos de segmentación: `gaceta_2026-03-20.json` tiene 52 segmentos y el primer segmento inicia con `DIRECTRIZ N° 056-MIDEPLAN-MTSS`; `gaceta_2023-01-16.json` tiene 94 segmentos y corresponde a un PDF de 220 páginas.

## 5. Cobertura por norma

### Definición usada

Cobertura completa estricta se computó sobre `plaza_runtime.db`, no por inspección manual de archivos. Una norma se cuenta como completa si tiene simultáneamente: `ficha` con `successful_artifact_count>0`, `texto` con `successful_artifact_count>0`, `afectaciones` con `successful_artifact_count>0`, y un `scij_identifier` en `scij_crawl_artifact` vinculado a `interpreted_norm_id`. La referencia a publicación en La Gaceta se computó aparte como `norm_publication_hint`.

### Conteo global

| Métrica | Normas |
|---|---:|
| Normas en `norm` | 15.964 |
| Con ficha SCIJ | 11.093 |
| Con texto SCIJ | 11.096 |
| Con afectaciones HTML SCIJ | 3.197 |
| Con identificador SCIJ resoluble | 11.354 |
| Con `norm_publication_hint` | 15.759 |
| Completas estrictas | 3.195 |
| Completas estrictas + publicación | 3.186 |
| Parciales estrictas | 12.769 |

### Combinaciones principales de faltantes

| Ficha | Texto | Afectaciones | Identificador | Pub hint | Normas |
|---:|---:|---:|---:|---:|---:|
| sí | sí | no | sí | sí | 7.864 |
| no | no | no | no | sí | 4.565 |
| sí | sí | sí | sí | sí | 3.186 |
| no | no | no | sí | sí | 143 |
| no | no | no | sí | no | 113 |
| no | no | no | no | no | 45 |
| sí | sí | no | sí | no | 34 |
| sí | sí | sí | sí | no | 9 |

Nota: `norm_afectada` tiene 70.479 filas para 7.864 normas, pero eso no equivale a la definición estricta de “página de afectaciones HTML capturada”. El conteo completo usa `scij_norm_surface_coverage.surface='afectaciones'` y artefactos exitosos vinculados a `norm_id`.

### Cobertura estricta por tipo normativo

| Tipo | Total | Completas estrictas | Completas + pub hint | Con ficha | Con texto | Con afectaciones |
|---|---:|---:|---:|---:|---:|---:|
| `decreto_ejecutivo` | 5.457 | 733 | 732 | 3.676 | 3.677 | 735 |
| `reglamento` | 4.924 | 941 | 937 | 2.909 | 2.909 | 941 |
| `ley` | 2.469 | 964 | 963 | 1.891 | 1.892 | 964 |
| `resolucion` | 1.457 | 315 | 313 | 1.178 | 1.178 | 315 |
| `acuerdo` | 1.162 | 197 | 196 | 1.034 | 1.034 | 197 |
| `directriz` | 483 | 43 | 43 | 395 | 395 | 43 |
| `constitucion` | 1 | 1 | 1 | 1 | 1 | 1 |

### Huérfanas y trazabilidad de archivos

| Criterio | Resultado |
|---|---:|
| SCIJ raw sin manifest por stem, filesystem actual | 0 |
| SCIJ manifest sin raw por stem, filesystem actual | 12 |
| SCIJ raw sin manifest en reporte heredado de 67.786 raw | 0 |
| SCIJ raw no registrado en DB en reporte heredado | 0 |
| `source_document` sin `raw_path` en `plaza_runtime.db` | 0 |
| `source_document` sin referencia desde `scij_crawl_artifact` | 19.115 |
| Gaceta PDFs sin manifest regular por fecha | 0 |
| Gaceta manifiestos sin PDF | 112 |
| Gaceta PDFs sin extracción paralela | 15 |

Interpretación: no hay evidencia de raw SCIJ huérfano en el sentido fuerte raw-sin-manifest dentro del reporte heredado ni del filesystem actual. Sí hay 19.115 `source_document` SCIJ sin referencia desde `scij_crawl_artifact`, que son huérfanos relativos al modelo de artefacto actual; no necesariamente archivos inútiles.

### Versiones históricas

Respuesta explícita: el scrape captura más que el estado vigente, pero no captura de forma completa las versiones históricas.

Evidencia de que no es solo vigente:

| Evidencia | Conteo |
|---|---:|
| Filas en `norm_version` | 21.872 |
| Normas con versiones | 15.964 |
| Filas `norm_version` no actuales | 5.908 |
| Normas con más de una versión persistida | 1.039 |
| Normalizados con `version_evidence` muestreados | 10/10 |

Evidencia de que no es histórico completo:

| Relación entre versiones persistidas y `version_total` observado | Normas | Version rows |
|---|---:|---:|
| Una versión y `version_total=1` | 10.203 | 10.203 |
| Menos versiones persistidas que `version_total` observado | 4.936 | 5.425 |
| Más versiones persistidas que `version_total` observado, sospechoso | 521 | 5.571 |
| Conteo persistido igual a `version_total` | 299 | 668 |
| `version_total` desconocido | 5 | 5 |

Ejemplos incompletos importantes: `codigo_penal` tiene 1 versión persistida y `version_total=100`; `codigo_trabajo` tiene 2 y `version_total=62`; `ley_7092` tiene 30 y `version_total=83`; `ley_8114` tiene 1 y `version_total=214`. Además, todos los 66.709 `scij_crawl_artifact` consultados tienen `version_harvest_mode='resolved_version_only'` y `version_chain_status='single_version_only'`.

## 6. Muestras representativas

Estas muestras tienen cobertura completa estricta: ficha + texto + afectaciones + identificador SCIJ. Las rutas listadas son los archivos principales que cubren cada muestra. Cuando existe normalizado de texto, se lista también. Cuando existe Gaceta PDF dentro del rango 2006-2026, se lista.

### Simples

| Norma | SCIJ | Año | Evidencia |
|---|---|---:|---|
| `ley_10790` | `1:105797:148607` | 2025 | Ley para garantizar la transparencia en la elección de la Presidencia del Concejo Municipal. 1 versión, 1 artículo, 0 transitorios, 1 fila de afectaciones, 2 concordancias, pub hint Gaceta 226 del 02/12/2025 Alcance 154. |
| `ley_10791` | `1:105798:148608` | 2025 | Ley para favorecer el análisis científico de sustancias psicoactivas. 1 versión, 1 artículo, 0 transitorios, 1 fila de afectaciones, 2 concordancias, pub hint Gaceta 226 del 02/12/2025 Alcance 154. |
| `ley_10788` | `1:105967:148850` | 2025 | Rescate de Vida Silvestre. 1 versión, 1 artículo, 0 transitorios, 1 fila de afectaciones, 2 concordancias, pub hint Gaceta 236 del 16/12/2025 Alcance 161. |

#### `ley_10790`

| Parte | Ruta |
|---|---|
| ficha raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105797_148607_04f7555bf4_6c7034ad54d1.html` |
| ficha manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105797_148607_04f7555bf4_6c7034ad54d1.json` |
| texto raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105797_148607_3abbe7d2ae_dd299449884e.html` |
| texto manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105797_148607_3abbe7d2ae_dd299449884e.json` |
| texto normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_105797_148607_3abbe7d2ae_dd299449884e.json` |
| afectaciones raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105797_148607_12e97b15ec_627bf13bbcd9.html` |
| afectaciones manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105797_148607_12e97b15ec_627bf13bbcd9.json` |
| Gaceta PDF | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2025-12-02.pdf` |
| Gaceta manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/manifests/gaceta_2025-12-02_regular.json` |
| Falta | No se observan faltantes para la definición estricta. No tiene transitorios ni histórico multi-versión. |

#### `ley_10791`

| Parte | Ruta |
|---|---|
| ficha raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105798_148608_8d358f2ee4_2471c9f8eaba.html` |
| ficha manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105798_148608_8d358f2ee4_2471c9f8eaba.json` |
| texto raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105798_148608_207babb03d_4e3d5c7a5be9.html` |
| texto manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105798_148608_207babb03d_4e3d5c7a5be9.json` |
| texto normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_105798_148608_207babb03d_4e3d5c7a5be9.json` |
| afectaciones raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105798_148608_c625adae00_e509a147f8c5.html` |
| afectaciones manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105798_148608_c625adae00_e509a147f8c5.json` |
| Gaceta PDF | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2025-12-02.pdf` |
| Gaceta manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/manifests/gaceta_2025-12-02_regular.json` |
| Falta | No se observan faltantes para la definición estricta. No tiene transitorios ni histórico multi-versión. |

#### `ley_10788`

| Parte | Ruta |
|---|---|
| ficha raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105967_148850_0a40cb629e_79a1e311efa2.html` |
| ficha manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105967_148850_0a40cb629e_79a1e311efa2.json` |
| texto raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105967_148850_c72596e21e_9579ecda7f56.html` |
| texto manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105967_148850_c72596e21e_9579ecda7f56.json` |
| texto normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_105967_148850_c72596e21e_9579ecda7f56.json` |
| afectaciones raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_105967_148850_f075c2d564_64b079fd4696.html` |
| afectaciones manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_105967_148850_f075c2d564_64b079fd4696.json` |
| Gaceta PDF | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2025-12-16.pdf` |
| Gaceta manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/manifests/gaceta_2025-12-16_regular.json` |
| Falta | No se observan faltantes para la definición estricta. No tiene transitorios ni histórico multi-versión. |

### Complejas

| Norma | SCIJ principal | Año | Evidencia |
|---|---|---:|---|
| `codigo_trabajo` | `1:8045:83262` | 1943 | Código de Trabajo. 2 versiones persistidas de 62 observadas, 644 artículos, 3 transitorios, 390 filas de afectaciones, 50 concordancias, pub hint Gaceta 192 del 29/08/1943. |
| `constitucion_politica` | texto `1:64115:106350`, ficha `1:52366`, afectaciones `1:871:929` | 1949 | Constitución Política. 6 versiones persistidas de 28 observadas, 199 artículos, 2 transitorios, 191 filas de afectaciones, 53 concordancias. |
| `ley_7092` | ficha `1:10969:148984`, texto `1:10969:11752`, afectaciones `1:10969:11755` | 1988 | Ley del Impuesto sobre la Renta. 30 versiones persistidas de 83 observadas, 110 artículos, 6 transitorios, 1.068 filas de afectaciones, 120 concordancias, pub hint Gaceta 96 del 19/05/1988. |

#### `codigo_trabajo`

| Parte | Ruta |
|---|---|
| ficha raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_8045_83262_60a51be2ec_ee4b5c5b9761.html` |
| ficha manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_8045_83262_60a51be2ec_ee4b5c5b9761.json` |
| texto raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_8045_83262_b416795935_b1eb4ae5c3a0.html` |
| texto manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_8045_83262_b416795935_b1eb4ae5c3a0.json` |
| texto normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_8045_83262_b416795935_b1eb4ae5c3a0.json` |
| afectaciones raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_8045_83262_3fb991cbef_67a67ded00cf.html` |
| afectaciones manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_8045_83262_3fb991cbef_67a67ded00cf.json` |
| concordancias raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_8045_83262_70cebcf4cb_bc1d8bb9dacb.html` |
| Gaceta | No hay PDF/manifiesto porque el corpus Gaceta local empieza en 2006; solo hay `norm_publication_hint` en DB para 1943. |
| Falta | Cadena histórica incompleta: 2 versiones persistidas de 62 observadas. |

#### `constitucion_politica`

| Parte | Ruta |
|---|---|
| ficha raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_52366_0_6c5f377e02_8bfdbebad02a.html` |
| ficha manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_52366_0_6c5f377e02_8bfdbebad02a.json` |
| texto raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_64115_106350_c11019da6c_d94f3c6e324c.html` |
| texto manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_64115_106350_c11019da6c_d94f3c6e324c.json` |
| texto normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_64115_106350_c11019da6c_d94f3c6e324c.json` |
| afectaciones raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_871_929_d2ad3758e4_4377895c748c.html` |
| afectaciones manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_871_929_d2ad3758e4_4377895c748c.json` |
| concordancias raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_871_928_e71c3e0162_a5da59ee1cdc.html` |
| Gaceta | No hay fecha de publicación normalizada ni PDF/manifiesto local; pub hint es bibliográfico: `Año: 1949 Semestre: 2 Tomo: 2 Página: 724`. |
| Falta | Cadena histórica incompleta: 6 versiones persistidas de 28 observadas; publicación no reconciliada con PDF. |

#### `ley_7092`

| Parte | Ruta |
|---|---|
| ficha raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10969_148984_96dd5ddd61_8e970432d77d.html` |
| ficha manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_10969_148984_96dd5ddd61_8e970432d77d.json` |
| texto raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10969_11752_0ae904242c_be274127940c.html` |
| texto manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_10969_11752_0ae904242c_be274127940c.json` |
| texto normalized | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/normalized/scij_1_10969_11752_0ae904242c_be274127940c.json` |
| afectaciones raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10969_11755_32fb0d198d_80d3f0a8cddb.html` |
| afectaciones manifest | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/manifests/scij_1_10969_11755_32fb0d198d_80d3f0a8cddb.json` |
| concordancias raw | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/scij/raw/scij_1_10969_11754_b2cdd9c96d_190e6c49f1b5.html` |
| Gaceta | No hay PDF/manifiesto local porque la publicación es 1988; sí existe `norm_publication_hint` para Gaceta 96 del 19/05/1988. |
| Falta | Cadena histórica incompleta: 30 versiones persistidas de 83 observadas; no hay PDF local de publicación original. |

Categorías no forzadas: Código Civil tiene cobertura de ficha/texto/afectaciones, pero no tiene `norm_publication_hint` normalizado en la consulta de candidatos y su cadena histórica está incompleta; no se seleccionó como golden principal.

## 7. Riesgos, huecos, desconocidos

| Item | Severidad | Evidencia | Qué lo resolvería |
|---|---|---|---|
| Versiones históricas incompletas | alta | 4.936 normas tienen menos versiones persistidas que `version_total`; `ley_7092` tiene 30/83, `codigo_trabajo` 2/62, `codigo_penal` 1/100. | Comparar cada `nValor2` contra todas las URLs/versiones SCIJ observables y marcar faltantes por `nValor3`. |
| Ventanas temporales incompletas | alta | `norm_version.valid_to` tiene 0 filas pobladas; `valid_from` parece fecha de ingestión en muchos casos, no vigencia jurídica. | Derivar vigencias desde metadata SCIJ/version banners y afectaciones con reglas verificables. |
| Identidad canónica sospechosa en algunas familias | alta | 521 normas tienen más versiones persistidas que `version_total`; ejemplos como `reglamento_municipal_municipal` con 830 versiones y `version_total=10`, `reglamento_0` con 542 y `version_total=28`. | Auditoría de `norm.id` contra `scij_identifier`; separar familias colapsadas. |
| Cobertura estricta baja de afectaciones | media | Solo 3.197 normas con afectaciones HTML exitosas vinculadas, contra 11.093 con ficha y 11.096 con texto. | Revisar si `norm_afectada` cubre parte de la evidencia y distinguir “página capturada” de “relación persistida”. |
| Normalización SCIJ parcial | media | 23.152 normalized JSON contra 80.222 raw HTML; `raw_without_normalized=57.070`. | Ejecutar/refinar normalización por superficie y registrar estados de no aplicable/no intentado. |
| Gaceta segmentation no es confiable como segmentación final | alta | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/segmentation_raw_audit.md`: 59,108% body contamination, 31,897% long segment rate en muestra de 8. | Re-auditar segmentador sobre muestra estratificada y corregir boundaries antes de usar segmentos como unidades legales. |
| Gaceta tiene manifiestos sin PDF | media | 112 manifiestos con `harvest_status='transport_failure'`, `pdf_available=false`. | Reintento de descarga o clasificación explícita como no publicado/no disponible. |
| Gaceta tiene PDFs sin extracción paralela | baja | 15 PDFs raw sin JSON en `extracted_parallel/`; todos con `page_count=1` y `qa_status=pending`. | Confirmar si son días sin publicación o PDFs informativos y registrar estado final. |
| Reconciliación publicación SCIJ-Gaceta no está cerrada | alta | `publication_event=0`; pub hints existen para 15.759 normas, pero PDFs Gaceta cubren 2006-2026 y muchas normas importantes son anteriores. | Construir o revisar una tabla de reconciliación source-backed entre `norm_publication_hint` y Gaceta. |
| `plaza.db` no contiene producto limpio | baja | `/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza.db` tiene 0 normas y 0 artículos. | Usar `plaza_runtime.db` como fuente de auditoría; no tratar `plaza.db` como corpus. |
| Artefactos duplicados por URL | media | `scij_raw_inventory_issue`: 812 `duplicate_url_volatile_only` abiertos; reporte heredado marca 812 grupos con `stable_hashes=1`. | Decidir política de deduplicación por `stable_html_hash` y preservar evidencia raw si se necesita reproducibilidad. |
| Source documents sin artifact | media | 19.115 `source_document` no referenciados por `scij_crawl_artifact`. | Clasificar esos docs por origen (`scij_raw_capture`, legacy import, retry) y decidir si son evidencia válida o residuo operacional. |
| Cobertura real de tabs opcionales es desconocida | media | Muchos `scij_norm_surface_coverage` tienen `not_attempted/excluded_by_policy`, especialmente observaciones, PGR, acciones, reglamentaciones. | No inferir ausencia legal desde “not_attempted”; requiere captura o prueba explícita de ausencia por superficie. |

## 8. Anexos

### Muestras inspeccionadas

| Categoría | Muestras |
|---|---:|
| SCIJ HTML dirigidos por superficie | 18 |
| SCIJ HTML aleatorios para encoding | 100 |
| SCIJ manifiestos JSON | 10 |
| SCIJ normalizados JSON | 10 |
| Gaceta PDFs con metadata `pdfinfo` | 6 |
| Gaceta manifiestos JSON | 6 |
| Gaceta extracciones JSON | 6 |
| Gaceta reportes heredados MD/JSON | 6 |

### Comandos representativos ejecutados

Los comandos se ejecutaron en modo lectura. Las conexiones SQLite usaron URI `mode=ro&immutable=1`.

```bash
python - <<'PY'
import sqlite3
sqlite3.connect('file:/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/db/plaza_runtime.db?mode=ro&immutable=1', uri=True)
PY
```

```bash
python - <<'PY'
from pathlib import Path
for p in Path('/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources').rglob('*'):
    pass
PY
```

```bash
pdfinfo "/mnt/Tokyo/Lab/Git/Plaza/archive/old/data/sources/gaceta/raw/gaceta_2026-03-20.pdf"
```

### Tablas SQLite usadas como ancla

| Tabla | Uso |
|---|---|
| `source_document` | Raw paths, normalized paths, hashes, URL fuente, mime/status. |
| `scij_crawl_artifact` | Superficie SCIJ, status de adquisición, `scij_identifier`, `n_valor1/2/3`, vínculo a `source_document`. |
| `scij_norm_surface_coverage` | Cobertura por superficie y resultado (`surface_present_and_rows_persisted`, `not_attempted`, `surface_absent`, etc.). |
| `norm` | Universo canónico de normas auditadas. |
| `norm_version` | Evidencia de versiones y pregunta histórica. |
| `article`, `article_version` | Conteo de estructura textual persistida. |
| `norm_publication_hint` | Referencias a publicación en La Gaceta. |
| `norm_afectada`, `norm_concordancia`, `norm_reglamentacion`, `norm_observaciones_tab`, `norm_pronunciamiento_pgr`, `norm_accion_constitucional` | Evidencia relacional por tab/superficie persistida. |

### Límites de esta auditoría

No se inspeccionaron manualmente 80.222 HTML ni 5.164 PDFs; los resultados combinan trazabilidad heredada, conteos agregados, consultas SQL y muestreo dirigido. No se validó jurídicamente cada relación ni cada artículo. Cuando el tracking no permite distinguir ausencia legal de no intentado, el resultado se marcó como desconocido o parcial.
