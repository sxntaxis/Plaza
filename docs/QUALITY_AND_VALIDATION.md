# Plaza — Calidad y Validación

Este documento define cómo Plaza decide que un dato está listo para ser publicado, cómo se valida el grafo canónico contra su modelo, y cómo se manejan los casos que no cumplen los criterios.

Es la implementación operativa de varios principios simultáneamente: el Principio 1 (Evidencia antes que inferencia), el Principio 10 (Disciplina reconstructiva), y el Principio 11 (Honestidad operativa). Donde esos principios dicen *qué* hay que hacer, este documento dice *cuándo* y *cómo verificarlo*.

La frontera más importante de la arquitectura de Plaza — la que separa la reconciliación operacional del grafo canónico público — es la frontera que este documento gobierna. Cruzar esa frontera es un acto que compromete a Plaza con el mundo de forma irreversible (Principio 2), y por eso debe estar regido por criterios explícitos, verificables, y aplicados de forma consistente.

---

## Filosofía de calidad

Plaza adopta cuatro posturas sobre calidad que dan forma a todo el resto de este documento.

**Calidad es preferible a completitud.** Publicar 10,000 normas verificadas es mejor que publicar 15,000 normas donde el 30% tiene errores. Los consumidores de Plaza construyen sobre lo publicado; un corpus con errores silenciosos erosiona la confianza de forma difícilmente reversible.

**Incertidumbre declarada es preferible a certeza falsa.** Cuando Plaza no puede verificar algo, lo dice. Una norma marcada como `plaza:provisional` es información útil; una norma marcada como definitiva cuando no lo es, es falsedad.

**Validación es continua, no puntual.** No basta con validar al momento de canonicalizar. El grafo canónico se revalida periódicamente para detectar inconsistencias introducidas por cambios en el modelo, en las fuentes, o en entidades relacionadas.

**Los criterios son públicos, no discrecionales.** Este documento es el criterio. Si una entidad cumple los criterios, se canonicaliza; si no los cumple, no se canonicaliza. No hay excepciones por decisión individual, ni promociones aceleradas para casos de interés particular.

---

## Niveles de verificación

Plaza distingue cuatro niveles de verificación de una afirmación. Cada uno tiene un tratamiento diferente en el grafo canónico.

### Nivel 1 — Directamente evidenciado

La afirmación se lee directamente de un artefacto oficial, sin interpretación. Ejemplos: el texto literal de un artículo tal como aparece en SCIJ; el número de una ley según el documento oficial; la fecha de emisión explícitamente declarada por la fuente.

**Tratamiento**: se canonicaliza sin marcadores especiales.

### Nivel 2 — Inferido con confianza alta

La afirmación resulta de una inferencia sobre múltiples artefactos o una estructura bien conocida. Ejemplos: el tipo de una norma inferido de convenciones de nombre consistentes en SCIJ; la relación `eli:amends` derivada de una entrada de afectación SCIJ cuyo formato está bien documentado.

**Tratamiento**: se canonicaliza sin marcadores especiales, pero la procedencia PROV-O indica la cadena de inferencia mediante `prov:wasDerivedFrom` apuntando a los artefactos base y `prov:wasGeneratedBy` apuntando al parser específico.

### Nivel 3 — Inferido con incertidumbre

La afirmación resulta de inferencia, pero hay evidencia de ambigüedad o la fuente misma presenta el dato con caveats. Ejemplos: una fecha de derogación tácita inferida de cruces entre normas; un tipo de afectación clasificado por heurísticas porque SCIJ no lo etiquetó explícitamente.

**Tratamiento**: se canonicaliza marcada con `plaza:inferred true` y puede llevar una nota `plaza:inference_note` describiendo la incertidumbre. Los consumidores cautelosos pueden filtrar por este marcador.

### Nivel 4 — Conflictivo o irresoluble

Dos o más fuentes dan afirmaciones incompatibles sobre el mismo hecho, y Plaza no tiene criterio definitivo para elegir. Ejemplo: SCIJ declara una fecha de vigencia que no coincide con lo adquirible desde La Gaceta.

**Tratamiento**: no se canonicaliza una afirmación única. En su lugar se crea un `plaza:reconciliation_issue` que registra ambas evidencias, queda asociado a las entidades afectadas, y permanece hasta que se resuelva. La entidad puede canonicalizarse parcialmente — con los datos no conflictivos — y el issue queda como marcador de incompletud.

---

## Criterios de canonicalización

Para que una entidad cruce la frontera de reconciliación hacia el grafo canónico, debe cumplir **todos** los criterios aplicables a su clase. Estos criterios son conjuntivos: un solo criterio incumplido impide la canonicalización.

### Criterios jurídico-operacionales previos a la canonicalización

Antes de evaluar una entidad por calidad semántica o estructural, Plaza debe poder responder cuatro preguntas:

1. **¿La fuente está habilitada?**
2. **¿La base jurídica o licencia de acceso y redistribución está determinada?**
3. **¿La publicabilidad del material fue clasificada?**
4. **¿Existen obligaciones adicionales de protección de datos o cumplimiento que deban satisfacerse antes de publicar?**

Una entidad que falle cualquiera de estas preguntas no cruza la frontera hacia el grafo canónico público, aunque su estructura semántica sea técnicamente correcta.

**C0 — Fuente habilitada.** La entidad debe provenir de una fuente cuya vía de acceso fue determinada y aprobada.

**C0.1 — Base jurídica o licencia determinada.** La entidad debe tener un régimen de acceso y redistribución identificado con suficiente claridad.

**C0.2 — Publicabilidad definida.** La entidad o conjunto de datos debe estar clasificado como publicable, publicable con restricciones, solo interno, o excluido.

**C0.3 — Finalidad evaluada.** Cuando existan datos personales o incidentales relevantes, debe constar evaluación de finalidad y tratamiento.

Para texto normativo oficial, metadata normativa y relaciones normativas, la compatibilidad de finalidad se presume positivamente salvo evidencia en contrario. Cuando existan datos personales o incidentales relevantes, la evaluación deja de ser presunta y pasa a ser obligatoria. Si la compatibilidad no es clara, el material no se trata como publicable por defecto: permanece como solo interno, publicable con reducción, o excluido, según corresponda.

**C0.4 — Cumplimiento adicional resuelto.** Cuando la operación active obligaciones adicionales regulatorias o institucionales, estas deben estar satisfechas o la entidad permanece fuera del grafo público.

## Nivel de autoridad documental de la fuente

Plaza no trata todas las fuentes oficiales como equivalentes para todos los fines. Antes de canonicalizar o publicar una afirmación sensible sobre texto, vigencia, trazabilidad normativa o soporte documental, el sistema debe registrar qué tipo de autoridad documental respalda esa afirmación.

Como mínimo, Plaza distingue tres niveles:

- **Publicación oficial**: la afirmación se ancla en la publicación oficial del texto.
- **Consolidación operativa oficial**: la afirmación se apoya en una fuente oficial de consulta y consolidación útil para navegación, relaciones normativas o texto actualizado.
- **Certificación documental institucional**: la afirmación se apoya en una certificación o constancia formal emitida por la autoridad competente.

Estos niveles no compiten entre sí. Cumplen funciones distintas y deben conservarse explícitamente en la procedencia.

**C0.5 — Nivel de autoridad documental registrado.** Toda entidad o afirmación cuya confianza dependa del carácter de la fuente debe registrar si su respaldo corresponde a publicación oficial, consolidación operativa oficial, certificación documental institucional, o combinación explícita de ellas.

**C0.6 — Claims no sobreafirmados.** Plaza no debe presentar una afirmación como certificada, auténtica o formalmente constatada si la procedencia disponible solo respalda publicación oficial o consolidación operativa.

### Criterios universales (aplican a toda entidad)

**C1 — URI asignable.** La entidad debe poder recibir una URI canónica según `URI_POLICY.md`. Si falta alguno de los componentes obligatorios (jurisdicción, año, tipo, número), no hay URI posible y por tanto no hay canonicalización.

**C2 — Procedencia rastreable.** La entidad debe tener al menos un `prov:wasDerivedFrom` apuntando a un artefacto preservado en el almacén de artefactos crudos. Una entidad sin procedencia no existe canónicamente.

**C3 — Tipo determinado.** La entidad debe tener un tipo canónico del vocabulario controlado correspondiente. Una entidad con tipo "desconocido" o inferido con baja confianza permanece en reconciliación.

**C4 — Consistencia referencial.** Toda URI referenciada por la entidad debe existir en el grafo canónico o estar en la misma cohorte de canonicalización. No se permiten referencias a URIs huérfanas.

### Criterios para LegalResource

Además de los universales:

**C5 — Emisor identificable.** El órgano emisor debe estar asignado a un concepto SKOS del vocabulario `plaza:EmisorNorma`. Un emisor desconocido impide canonicalización.

**C6 — Fecha de emisión verificable.** Debe existir una fecha de emisión con nivel de verificación 1 o 2. Una fecha inferida con incertidumbre (nivel 3) no es suficiente para canonicalizar; la norma permanece en reconciliación con issue marcado.

**C7 — Al menos una Expression realizable.** Debe existir al menos una `eli:LegalExpression` que la realice y que a su vez cumpla sus propios criterios de canonicalización. Una LegalResource sin Expression canonicable no aporta valor consultable.

### Criterios para LegalExpression

Además de los universales:

**C8 — Fecha de vigencia verificable.** La fecha de inicio de vigencia de la expresión debe ser verificable a nivel 1 o 2. No se canonicaliza una Expression con fecha de vigencia ambigua.

**C9 — Texto material presente.** La Expression debe tener texto no vacío. Una Expression cuyo texto no fue extraído exitosamente permanece en reconciliación.

**C10 — Integridad del texto.** El texto debe pasar chequeos básicos de integridad: no truncado a media palabra, no con caracteres de control sospechosos, no vacío donde se esperaría contenido. Los criterios específicos se definen en la implementación del validador pero honran este principio general.

**C11 — LegalResource padre canónica.** La LegalResource que esta Expression realiza debe estar canonicalizada. Una Expression no puede canonicalizarse antes que su obra.

### Criterios para LegalResourceSubdivision

Además de los universales:

**C12 — LegalResource contenedora canónica.** La norma a la que la subdivisión pertenece debe estar canonicalizada.

**C13 — Posición estructural clara.** El tipo de subdivisión (artículo, transitorio, anexo) debe estar identificado con certeza. Una subdivisión cuyo rol estructural es ambiguo permanece en reconciliación.

**C14 — Identificador natural estable.** El número o identificador natural de la subdivisión debe estar determinado y ser consistente con el formato documentado en URI_POLICY.

### Criterios para relaciones entre normas

**C15 — Extremos canónicos.** Tanto el sujeto como el objeto de la relación deben estar canonicalizados. No se canonicalizan relaciones que apunten a normas aún en reconciliación.

**C16 — Tipo de relación ELI válido.** La relación debe mapear a una propiedad ELI reconocida (`eli:amends`, `eli:repeals`, `eli:corrects`, `eli:cites`, `eli:applies`, o variantes), o a una extensión `plaza:` documentada.

**C17 — Evidencia de la relación.** La relación debe tener al menos un artefacto fuente que la respalde, referenciado vía PROV-O.

---

## Validación formal con SHACL

Las restricciones del modelo se formalizan como SHACL (Shapes Constraint Language) shapes. Un SHACL shape es un artefacto que un validador puede ejecutar contra cualquier grafo RDF para detectar violaciones.

Plaza publica sus SHACL shapes junto con la ontología. Los shapes son versionados conjuntamente con el modelo de datos.

### Qué valida SHACL

**Estructura del grafo**: que cada `eli:LegalResource` tenga las propiedades obligatorias; que cada `eli:LegalExpression` apunte a su `eli:realizes`; que las subdivisiones estén correctamente enlazadas a sus obras.

**Tipos de datos**: que las fechas sean `xsd:date` válidas; que los literales de idioma tengan tags válidos; que los números sean del tipo correcto.

**Referencias**: que cada URI referenciada resuelva en el grafo o esté marcada como externa; que no haya ciclos inválidos en relaciones que deberían ser acíclicas.

**Vocabularios controlados**: que los tipos de norma sean conceptos del SKOS scheme correspondiente; que los emisores estén dentro del vocabulario oficial.

**Cardinalidades**: que las propiedades funcionales no tengan múltiples valores; que las propiedades obligatorias estén presentes.

### Cuándo se ejecuta

SHACL se ejecuta en tres momentos:

**Pre-canonicalización**: antes de promover entidades del estado reconciliado al grafo canónico. Una entidad que falla SHACL no se canonicaliza, aunque cumpla los criterios C1–C17 operacionales.

**Post-snapshot**: cada snapshot publicado se valida completo. Un snapshot que falla SHACL no se publica; se regenera con las correcciones necesarias o se revierten las promociones problemáticas.

**Periódico**: el grafo canónico se revalida periódicamente (ej. semanalmente) para detectar inconsistencias que pueden haber emergido de cambios en normas relacionadas. Violaciones detectadas se tratan como issues de reconciliación reabiertos.

### Qué no valida SHACL

SHACL valida estructura, no veracidad. Puede verificar que una fecha tenga formato válido, pero no que sea la fecha correcta. La veracidad depende de la evidencia de las fuentes y de los criterios de los niveles de verificación descritos arriba.

---

## Reconciliation issues

Cuando una entidad no puede canonicalizarse, o cuando una entidad canonicalizada revela un conflicto, Plaza registra un `plaza:reconciliation_issue` con información estructurada.

### Estructura de un issue

Un issue es una entidad del grafo operacional (no canónico) con al menos las siguientes propiedades:

| Propiedad | Significado |
|---|---|
| `plaza:issue_type` | Tipo del issue (ver vocabulario abajo) |
| `plaza:affected_entity` | URI de la entidad afectada (puede ser provisional) |
| `plaza:evidence_uris` | Lista de URIs de artefactos que respaldan el issue |
| `plaza:detected_at` | Timestamp de detección |
| `plaza:description` | Descripción estructurada del problema |
| `plaza:status` | Estado actual (abierto, en revisión, resuelto, descartado) |
| `plaza:resolution_note` | Nota de resolución cuando el issue se cierra |

### Tipos de issues

- `plaza:issue-missing-field`: un campo obligatorio no pudo extraerse
- `plaza:issue-conflicting-evidence`: dos fuentes dan información incompatible
- `plaza:issue-ambiguous-reference`: una relación apunta a una norma cuya identidad no está clara
- `plaza:issue-invalid-structure`: el artefacto crudo no sigue el formato esperado
- `plaza:issue-orphan-reference`: una entidad referencia una URI que no existe en el corpus
- `plaza:issue-temporal-inconsistency`: fechas que no cuadran (ej. derogación anterior a emisión)
- `plaza:issue-shacl-violation`: la entidad viola el SHACL shape
- `plaza:issue-unapproved-source`: la entidad proviene de una fuente no habilitada para publicación
- `plaza:issue-unknown-redistribution-basis`: no está clara la base jurídica o licencia para redistribuir
- `plaza:issue-purpose-mismatch`: el tratamiento proyectado no es consistente con la finalidad original
- `plaza:issue-compliance-pending`: la operación requiere cumplimiento adicional antes de publicar
- `plaza:issue-publication-restriction`: la entidad o conjunto no puede exponerse como corpus abierto en su forma actual
- `plaza:issue-unknown-source-authority-level`: no está claro qué tipo de autoridad documental respalda la afirmación
- `plaza:issue-overstated-documentary-authority`: la afirmación fue expresada con un nivel de autoridad documental superior al realmente respaldado por su procedencia

### Exposición pública de issues

Los issues **no son parte del grafo canónico público**. Son parte del estado operacional. Sin embargo, Plaza publica estadísticas agregadas de issues como parte de los metadatos del corpus (ej. cuántos issues abiertos de cada tipo, porcentaje del corpus afectado), porque esa información es relevante para que los consumidores entiendan la calidad del corpus sin tener que inspeccionar cada entidad.

Los snapshots incluyen un documento `corpus_health.json` que resume los estados de calidad sin exponer los issues individuales (que pueden contener información operacional sensible, rutas internas, etc.).

Cuando una afirmación se publique hacia terceros, la procedencia debe poder expresar no solo de qué fuente vino, sino qué rol documental cumple esa fuente dentro del ecosistema jurídico correspondiente.

---

## Marcadores en el grafo canónico

Más allá de los issues (que viven en la capa operacional), el grafo canónico usa marcadores explícitos para declarar incertidumbre a los consumidores.

### plaza:provisional

Una entidad marcada `plaza:provisional true` indica que cumple los criterios mínimos de canonicalización pero tiene dimensiones reconocidas como incompletas. Ejemplos:

- Una norma canonicalizada con texto verificado pero pistas de publicación sin confirmar en La Gaceta.
- Un artículo canonicalizado cuyo texto está verificado pero cuya relación con versiones anteriores no está completa.

Los consumidores pueden filtrar por `plaza:provisional false` para obtener solo entidades completamente maduras.

### plaza:inferred

Como se describió en los niveles de verificación, afirmaciones inferidas con incertidumbre (nivel 3) llevan este marcador. Permite al consumidor distinguir entre hechos directamente evidenciados e inferencias.

### plaza:has_open_issue

Una entidad puede tener `plaza:has_open_issue` apuntando a un issue en la capa operacional. Esto NO expone el issue mismo (los issues no son públicos), pero sí expone que **existe** un issue pendiente. El consumidor sabe que algo está siendo investigado, sin acceder a los detalles operacionales.

---

## Reversiones y correcciones

Cuando Plaza descubre un error en una entidad ya canonicalizada, el manejo depende del tipo de error.

### Errores en procedencia o metadata no-identificatoria

Si el error es en procedencia, en metadata, o en propiedades no-identificatorias (título, descripción, tipo), la corrección se aplica directamente al grafo canónico **preservando la URI**. El cambio queda documentado con PROV-O: una nueva `prov:Activity` de corrección referencia el estado previo.

### Errores en identidad o estructura fundamental

Si el error es en la identidad misma — la URI se emitió incorrectamente, o la entidad representa algo distinto de lo que se asumió — la URI errónea **no se borra**. Se marca como `plaza:deprecated true` con una propiedad `plaza:superseded_by` apuntando a la URI correcta (si existe). La URI errónea sigue resolviendo, ahora a un documento que explica el error y redirige al recurso correcto.

Este manejo honra el Principio 2 (Identidad permanente): la URI errónea no desaparece del mundo, sigue siendo resoluble, pero es claramente identificable como deprecada.

### Reversión de promociones

Cuando un error es tan grave que la entidad nunca debió canonicalizarse, se ejecuta una reversión: la URI se marca como `plaza:deprecated true` y `plaza:never_valid true`. Esto es diferente de una sucesión normal — indica que la promoción misma fue un error.

Las reversiones son excepcionales y requieren documentación explícita. No son el mecanismo ordinario para corregir errores; son un último recurso cuando ninguna otra corrección preserva la integridad del grafo.

---

## Métricas de calidad

Plaza publica métricas de calidad del corpus como parte de cada snapshot y a través del feed Atom. Estas métricas permiten a consumidores evaluar la confiabilidad del corpus sin inspeccionarlo exhaustivamente.

### Métricas por clase

Para cada clase principal (LegalResource, LegalExpression, Subdivision, relaciones):

- Total de entidades canonicalizadas
- Porcentaje marcadas como `plaza:provisional`
- Porcentaje con `plaza:has_open_issue`
- Porcentaje con afirmaciones inferidas (`plaza:inferred`)
- Desglose por nivel de verificación promedio

### Métricas por dimensión

- Cobertura temporal: distribución de fechas de emisión (esperado vs. observado)
- Cobertura por emisor: distribución por órgano emisor
- Cobertura de relaciones: porcentaje de normas con al menos una relación de afectación
- Cobertura de publicación: porcentaje con pistas de publicación verificadas

### Métricas de validación

- Fecha de última validación SHACL completa
- Número de violaciones SHACL en la última validación (debería ser cero en snapshot publicado)
- Número de issues abiertos por tipo

### Exposición

Estas métricas se publican en dos formatos:

- **Máquina**: como documento DCAT enriquecido en el catálogo del snapshot.
- **Humana**: como reporte Markdown en el repositorio del proyecto, actualizado automáticamente.

---

## Evolución de los criterios

Los criterios de calidad de este documento pueden evolucionar. Su evolución está regida por dos reglas:

**Endurecimiento es siempre aceptable.** Plaza puede agregar criterios, elevar umbrales, o exigir más evidencia en cualquier momento. El efecto es que entidades antes canonicalizadas pueden volverse provisionales o regresar a reconciliación. Esto no viola ningún principio — al contrario, honra el Principio 1.

**Relajamiento requiere justificación explícita.** Reducir un criterio, bajar un umbral, o aceptar menos evidencia solo se hace con discusión pública documentada y con una razón articulada que no contradiga los principios. Relajar criterios silenciosamente es incompatible con la honestidad operativa.

**Cambios se comunican.** Cualquier cambio en los criterios se documenta en el changelog de este documento, se asocia con una versión del modelo de datos, y se anuncia en el canal público de comunicación del proyecto.

---

## Relación con otras políticas

- [`PRINCIPLES.md`](PRINCIPLES.md) — Principios 1, 10 y 11 son la base de este documento.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — define las capas entre las que este documento gobierna el cruce.
- [`DATA_MODEL.md`](DATA_MODEL.md) — define las clases y propiedades que SHACL valida.
- [`URI_POLICY.md`](URI_POLICY.md) — define los criterios de URI canónica que C1 exige.
- [`VERSIONING.md`](VERSIONING.md) — define cómo se versionan los SHACL shapes junto con la ontología.
