# Plaza — Versionado

Este documento define cómo Plaza versiona todo lo que versiona. La disciplina de versionado es uno de los mecanismos más importantes para honrar el Principio 2 (Identidad permanente): cuando algo cambia, el versionado es lo que permite que lo anterior siga existiendo sin ambigüedad.

Plaza tiene múltiples cosas que versionar, cada una con lógica propia. Confundir esas lógicas produce sistemas que parecen versionados pero son incoherentes — dos cosas comparten un número de versión sin realmente evolucionar juntas, o dos cosas evolucionan juntas pero tienen números distintos. Este documento establece con precisión qué se versiona, cómo, y cuál es la relación entre versiones de cosas distintas.

---

## Qué se versiona

Plaza versiona **seis clases de artefacto** distintas. Cada una tiene su propia cadencia, su propio formato de versión, y sus propias reglas de compatibilidad.

| Artefacto | Formato | Cadencia | Quién decide el número |
|---|---|---|---|
| Ontología Plaza | Semver (MAJOR.MINOR.PATCH) | Baja (meses/años) | Equipo de modelado |
| Modelo de datos | Semver, atado a ontología | Baja | Equipo de modelado |
| SHACL shapes | Semver, atado a ontología | Baja | Equipo de modelado |
| Snapshots del corpus | Calendario (YYYY-MM-DD + secuencia) | Alta (semanal/mensual) | Automático al publicar |
| Superficies de acceso | Versionado evolutivo compatible | Variable | Equipo de plataforma |
| Políticas públicas (este tipo de documento) | Semver | Muy baja (años) | Equipo de proyecto |

Hay una regla común que atraviesa las seis: **nunca se reutiliza un número de versión**. Una vez que `ontología 0.2.0` se publicó, ese nombre queda asociado para siempre con ese contenido exacto. Si se descubre un error, se publica `0.2.1` — no se reescribe `0.2.0`.

---

## Versionado de la ontología Plaza

### Qué es la ontología Plaza

La ontología Plaza es el archivo OWL (más documentación asociada) que define formalmente:

- Las extensiones `plaza:` documentadas en DATA_MODEL.md (clases y propiedades)
- Los concept schemes SKOS (TipoNorma, EmisorNorma, EstadoVigencia, TipoSubdivision)
- Los enlaces (`skos:exactMatch`, `skos:closeMatch`) hacia vocabularios estándar (ELI, schema.org/Legislation)
- Las declaraciones de equivalencia con ontologías externas

No incluye las ontologías importadas (ELI, PROV-O, etc.) — esas se versionan por sus propios publicadores. La ontología Plaza es exclusivamente el trabajo original de Plaza.

### Formato: Semantic Versioning 2.0.0

La ontología sigue [Semantic Versioning](https://semver.org/) en su variante aplicada a ontologías. La URI de la ontología incluye la versión:

```
https://plaza.cr/ontology/0.1.0
```

La URI sin versión (`https://plaza.cr/ontology`) siempre resuelve a la versión más reciente, con redirección HTTP 303 a la URI versionada. Esto permite consumidores que quieren "lo más nuevo" y consumidores que necesitan estabilidad.

### Estado pre-lanzamiento

Hasta el primer lanzamiento público formal del proyecto, todos los artefactos versionados comienzan con MAJOR en cero (`0.x.y`). Esto sigue [la convención explícita de SemVer 2.0.0](https://semver.org/#spec-item-4): *"Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable."*

El salto a `1.0.0` ocurre cuando el proyecto se declara formalmente lanzado al público, con compromiso de estabilidad de sus interfaces y contratos. A partir de ese punto, las reglas de compatibilidad descritas abajo aplican estrictamente.

Durante el estado `0.x.y`, los cambios que bajo `1.x.y` serían MAJOR incompatibles pueden hacerse bumpeando MINOR, dado que el proyecto no ha establecido compromisos públicos todavía. Esto le permite al proyecto iterar sobre el diseño sin congelar decisiones prematuramente.

### Qué cuenta como PATCH (0.1.0 → 0.1.1, o eventualmente 1.0.0 → 1.0.1)

Cambios que no afectan semántica operativa:

- Correcciones de tipografía en `rdfs:label` o `rdfs:comment`
- Aclaraciones de definiciones sin cambio de intención
- Adición de `skos:altLabel`, `skos:definition`, `skos:example`
- Corrección de enlaces externos rotos
- Mejoras en documentación interna

Consumidores pueden actualizar a una nueva PATCH sin revisar su código.

### Qué cuenta como MINOR (0.1.0 → 0.2.0, o eventualmente 1.0.0 → 1.1.0)

Cambios compatibles hacia atrás que extienden el modelo:

- Adición de nuevas clases o propiedades con `plaza:` prefix
- Adición de nuevos conceptos a concept schemes SKOS existentes
- Adición de nuevos `skos:exactMatch` o `skos:closeMatch` hacia vocabularios externos
- Relajamiento de restricciones (ej. un dominio antes `plaza:ClassA` ahora `plaza:ClassA or plaza:ClassB`)
- Adición de propiedades opcionales

Consumidores pueden actualizar a una nueva MINOR. Su código existente sigue funcionando. El grafo canónico puede empezar a incluir las nuevas propiedades, pero las entidades previas no pierden validez.

### Qué cuenta como MAJOR (eventualmente 1.0.0 → 2.0.0, una vez superado el estado pre-lanzamiento)

Cambios incompatibles:

- Eliminación de clases o propiedades
- Cambio de dominio o rango de una propiedad existente
- Eliminación de conceptos de un SKOS scheme
- Endurecimiento de restricciones (ej. una propiedad antes opcional ahora obligatoria)
- Cambio de semántica de una propiedad existente

Consumidores deben revisar su código antes de actualizar a un MAJOR nuevo. Plaza mantiene la versión MAJOR anterior accesible durante al menos un período de convivencia documentado.

### Períodos de convivencia

Cuando se publica una nueva MAJOR, la anterior:

- Sigue siendo dereferenciable por URI versionada (`https://plaza.cr/ontology/1.2.3`)
- Sigue siendo válida para el corpus ya canonicalizado bajo ella
- No recibe nuevas entidades canonicalizadas pasado un período de transición documentado

El período mínimo de convivencia entre versiones MAJOR es **dos años** calendario. Esto aplica a partir del primer lanzamiento público formal (`1.0.0`). Durante el estado pre-lanzamiento (`0.x.y`), no hay compromiso de convivencia y las MINOR pueden introducir cambios incompatibles.

---

## Versionado del modelo de datos y SHACL

### Relación con la ontología

El modelo de datos documentado en `DATA_MODEL.md` y las SHACL shapes que lo validan **comparten versión con la ontología Plaza**. Un cambio en la ontología que requiere bump MAJOR también bumpea MAJOR el modelo y las shapes, simultáneamente.

Esto evita que tres cosas conceptualmente acopladas se desincronicen. Si la ontología está en `0.2.0`, el modelo de datos es `0.2.0` y las shapes son `0.2.0`. Publicados juntos, versionados juntos.

### SHACL shapes

Las shapes se publican como archivos Turtle en el repositorio de la ontología:

```
https://plaza.cr/ontology/0.2.0/shapes.ttl
```

Plaza garantiza que cualquier entidad canonicalizada bajo la versión X del modelo pasa las shapes de la versión X. Esto es verificable: basta con correr el validador SHACL contra un snapshot y contra las shapes de la misma versión.

Las shapes de versiones anteriores siguen disponibles para que consumidores puedan validar snapshots históricos.

---

## Versionado de snapshots del corpus

### Qué es un snapshot

Un snapshot es una foto del grafo canónico en un momento dado, publicada como artefacto inmutable en los formatos documentados en `ACCESS_SURFACES.md`. Cada snapshot contiene el corpus completo — no hay snapshots diferenciales.

### Formato: calendario con secuencia

Los snapshots se identifican con fecha ISO y número de secuencia diario cuando aplique:

```
plaza-snapshot-2026-04-20
plaza-snapshot-2026-04-20-002  (si hay más de uno en el mismo día)
```

La razón para usar calendario y no semver: los snapshots no representan decisiones de modelado, representan el estado del corpus en un momento. "¿Qué contenía el corpus el 20 de abril de 2026?" es una pregunta que se responde trivialmente con la fecha. Un semver respondería "¿qué versión es esta?" pero no "¿cuándo se tomó?".

### Metadata de cada snapshot

Cada snapshot incluye:

```
snapshot_id: plaza-snapshot-2026-04-20
generated_at: 2026-04-20T14:30:00Z
ontology_version: 0.2.0
model_version: 0.2.0
shapes_version: 0.2.0
previous_snapshot: plaza-snapshot-2026-04-13
content_hash: sha256:a1b2c3...
entity_counts:
  LegalResource: 15964
  LegalExpression: 21872
  Subdivision: 231948
  ...
corpus_health_reference: https://plaza.cr/snapshot/2026-04-20/corpus_health.json
```

El `previous_snapshot` forma una cadena verificable de snapshots: dado el snapshot más reciente, cualquiera puede recorrer hacia atrás hasta el primer snapshot publicado.

### Inmutabilidad

Una vez publicado, un snapshot no se modifica nunca. Si se descubre un error en un snapshot:

- Si el error es en una afirmación dentro del corpus, se publica un **nuevo snapshot** con la corrección. El snapshot erróneo sigue disponible con advertencia.
- Si el error es en el formato del snapshot (un archivo corrupto), se publica una versión rehecha con sufijo: `plaza-snapshot-2026-04-20-rehecha`. El original corrupto se marca explícitamente como tal.

La inmutabilidad es lo que hace que los snapshots cumplan su rol de archivo histórico del corpus.

### Cadencia

Plaza no se compromete a una cadencia fija de snapshots. La política real es:

- Un snapshot se publica cuando hay cambios sustantivos en el corpus desde el snapshot anterior.
- No se publica un snapshot idéntico al anterior.
- En períodos de actividad alta, puede haber snapshots semanales. En períodos estables, pueden pasar meses.
- En cualquier caso, al menos un snapshot por año, como política de continuidad.

La cadencia real se documenta en cada snapshot (tiempo transcurrido desde el previous) y en el catálogo DCAT.

### Retención

Los snapshots más recientes (por ejemplo, los últimos 12 meses) se mantienen en línea con acceso directo. Los más antiguos pueden migrarse a almacenamiento archival más lento pero siguen siendo accesibles por URL permanente. Ningún snapshot publicado se elimina — la cadena histórica se preserva indefinidamente.

---

## Versionado de superficies de acceso

### El desafío

Las superficies (API REST, MCP, feeds, snapshots descargables) evolucionan con necesidades cambiantes de consumidores. Al mismo tiempo, los Principios 2 y 7 exigen que las URIs no cambien y que los consumidores no se vean forzados a reescribir su código constantemente.

La respuesta es **versionado evolutivo sin prefijos de versión en URIs**, como se estableció en `ACCESS_SURFACES.md`.

### Cómo se evoluciona una superficie

**Nuevas capacidades** se agregan de forma aditiva. Un nuevo endpoint, un nuevo formato de respuesta via nuevo media type, un nuevo parámetro opcional — todo esto se agrega sin romper lo existente.

**Deprecación de capacidades** ocurre cuando algo ya no tiene sentido mantener. El proceso es:

1. Anuncio público de deprecación con fecha de retiro.
2. Período de deprecación (mínimo 12 meses).
3. Durante el período, la capacidad sigue funcionando pero las respuestas incluyen header `Deprecation` y `Sunset` con la fecha.
4. Al final del período, la capacidad se retira.

**Cambios incompatibles** en una superficie son, idealmente, imposibles — están prohibidos por el Principio 2 sobre las URIs y por el Principio 7 sobre estabilidad. Si por alguna razón extraordinaria uno se vuelve necesario, el tratamiento es:

1. Se crea un **nuevo media type** que expresa el nuevo formato (ej. `application/ld+json;profile="https://plaza.cr/profile/v2"`)
2. El media type antiguo sigue funcionando indefinidamente
3. Los consumidores negocian via Accept header cuál quieren

Este patrón sigue el estándar HTTP de content negotiation y respeta las URIs canónicas.

### Capacidad versus contrato

La documentación de las superficies distingue explícitamente entre:

- **Contrato**: qué garantiza Plaza. Cambia muy raramente y nunca de forma incompatible.
- **Capacidad**: qué puede hacer hoy. Se expande con el tiempo.

Un consumidor que se apoya en el contrato está a salvo indefinidamente. Un consumidor que se apoya en capacidades específicas sabe qué esperar si esas capacidades evolucionan.

---

## Versionado de políticas públicas

Los documentos que gobiernan Plaza — este documento, VISION, PRINCIPLES, SCOPE, URI_POLICY, ACCESS_SURFACES, LICENSING, LEGAL_BASIS, ARCHITECTURE, DATA_MODEL, QUALITY_AND_VALIDATION, REFERENCES — también se versionan.

### Formato: Semver aplicado a documentos

Cada documento lleva en su encabezado (o en un changelog asociado):

- Versión actual (ej. `0.2.0`)
- Fecha de la versión
- Enlace al changelog completo

### Qué cuenta como cambio

- **PATCH**: correcciones tipográficas, aclaraciones sin cambio de intención, reorganización interna.
- **MINOR**: agregados que no alteran compromisos existentes (nueva sección, nueva aclaración de un caso antes ambiguo, nuevo ejemplo).
- **MAJOR**: cambios de compromiso. Esto es extremadamente raro — los documentos fundamentales están diseñados para no requerir cambios MAJOR. Si uno ocurre, refleja un cambio fundamental en el proyecto y debe ser discutido públicamente antes de publicarse.

### Inmutabilidad histórica

Las versiones anteriores de los documentos se preservan en el repositorio con sus URLs permanentes. Si alguien citó `PRINCIPLES.md` versión 1.0 en 2026 y quiere verificar qué decía exactamente, esa versión sigue accesible.

### Los cuatro principios irreversibles

Recordemos que el Principio 9 (LICENSING.md) establece cuatro pilares irreversibles:

- Código bajo copyleft fuerte
- Datos bajo share-alike
- Sin acceso privilegiado a datos
- Versión abierta siempre disponible

Estos NO son versionables. No hay MAJOR, MINOR, o PATCH que los modifique. Si un cambio contradice alguno, ese cambio está prohibido por definición, no por versión.

Similarmente, el Principio 2 (URIs inmutables) se aplica a sí mismo: el compromiso de URIs estables no se puede bajar por bump de versión. La política de URIs puede extenderse (MINOR) o refinarse (PATCH), pero nunca reducirse (no hay MAJOR válido que retire URIs ya publicadas).

---

## Relación entre versiones

La siguiente matriz muestra cómo interactúan las versiones de artefactos distintos:

| Si cambia... | Bumpea automáticamente... | Puede afectar... |
|---|---|---|
| Ontología (MAJOR) | Modelo de datos, SHACL shapes | Todos los snapshots futuros |
| Ontología (MINOR) | Modelo de datos, SHACL shapes | Snapshots futuros pueden incluir nuevas propiedades |
| Ontología (PATCH) | Modelo de datos, SHACL shapes | Ningún snapshot cambia |
| Snapshot del corpus | — | Nada más; es el artefacto terminal |
| Superficie de acceso (evolutiva) | — | Puede agregar nuevos formatos o endpoints |
| Política pública (MINOR o PATCH) | — | Documentación, no datos |
| Política pública (MAJOR) | Puede requerir revisión de todo | Requiere discusión pública previa |

---

## Registro de versiones

Plaza mantiene un **índice público de versiones** accesible en:

```
https://plaza.cr/versions
```

Este índice lista:

- Todas las versiones publicadas de la ontología, modelo, y shapes, con fechas y enlaces
- Todos los snapshots publicados, con fechas, tamaños, y hashes
- Las versiones de todos los documentos de política, con fechas y changelogs

El índice es generado automáticamente a partir del repositorio; no es mantenido manualmente. Esto previene que se desincronice con la realidad.

El índice es también consumible como catálogo DCAT, para federación con otros portales.

---

## Changelog de este documento

La primera versión publicada de este documento es `0.1.0`, correspondiente al inicio formal de la infraestructura de versionado activa, aún antes del primer lanzamiento público del proyecto.

---

## Relación con otras políticas

- [`PRINCIPLES.md`](PRINCIPLES.md) — especialmente Principio 2 (identidad permanente), que este documento operacionaliza a través de múltiples dimensiones.
- [`URI_POLICY.md`](URI_POLICY.md) — define cómo se versionan las URIs específicamente, complementado aquí.
- [`DATA_MODEL.md`](DATA_MODEL.md) — la ontología que este documento versiona.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — las SHACL shapes que se versionan junto con la ontología.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — las superficies cuyo versionado evolutivo este documento detalla.
- [`LICENSING.md`](LICENSING.md) — los pilares irreversibles que no admiten versionado.
