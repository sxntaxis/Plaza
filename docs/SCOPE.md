# Plaza — Alcance

Este documento define qué hace Plaza hoy, qué podría hacer en el futuro, y qué queda explícitamente fuera. A diferencia de los principios, que son evergreen y gobiernan cómo Plaza hace lo que sea que haga, el alcance es temporal: describe el Plaza de esta etapa. Evoluciona cuando las condiciones cambian.

El propósito es doble: proteger al proyecto del scope creep — la tendencia a agregar "solo una cosita más" hasta que nada se termina — y proteger al proyecto del reverso, que es subestimar su norte por timidez. Cuando alguien propone algo, este documento responde si ese algo está adentro, está fuera por ahora pero es parte del norte, o está fuera para siempre.

---

## En alcance actual

Plaza modela el **corpus normativo costarricense** como grafo estructurado, citable y verificable, distribuido como producto híbrido de snapshots descargables y servicios en vivo.

### Entidades canónicas

- **Normas**: leyes, decretos ejecutivos, reglamentos, directrices, resoluciones, acuerdos, y otras clases normativas de aplicación general.
- **Versiones de normas**: cada cambio material produce una versión distinta con identificador propio, fecha de vigencia, y evidencia de cuándo entró en vigor.
- **Artículos**: cada artículo es una entidad canónica con identidad estable a lo largo del tiempo.
- **Versiones de artículos**: cada cambio textual en un artículo produce una versión con texto específico y período de vigencia.

### Relaciones entre normas

- **Afectaciones**: qué norma deroga, modifica, suspende, o altera de otra manera a qué otra, con tipo de operación y modo explícitos.
- **Concordancias**: vínculos temáticos entre normas y artículos.
- **Reglamentaciones**: qué reglamento regula qué ley.
- **Descriptores**: clasificaciones temáticas y materias.

### Referencias externas

- **Pistas de publicación**: referencias a La Gaceta donde una norma fue publicada oficialmente, tal como las expone SCIJ — sin verificación cruzada con el feed oficial de La Gaceta.
- **Hooks a pronunciamientos de la PGR**: referencias a dictámenes que interpretan las normas, sin incluir el corpus completo de pronunciamientos.
- **Hooks a acciones constitucionales**: referencias a votos de la Sala Constitucional que afectan normas, sin incluir el corpus completo de jurisprudencia.
- **Observaciones editoriales**: notas interpretativas que SCIJ asocia a las normas.

### Superficies de acceso

- **Snapshots descargables**: exports periódicos del corpus completo en RDF/Turtle, JSON-LD, y Akoma Ntoso XML.
- **API REST pública**: endpoints deterministas sobre los identificadores canónicos, con URIs estables por norma, versión, artículo, y versión de artículo.
- **Servidor MCP**: interfaz nativa para sistemas de IA que consumen el corpus con retrieval verificable.
- **Catálogo DCAT**: descripción estructurada de los datasets publicados, para federación con otros portales de datos abiertos.

---

## Fuera del alcance actual, parte del norte

Estas áreas son reconocidas como extensiones naturales del proyecto. Su exclusión actual es de secuencia, no de principio. Cada una tiene un criterio explícito para ser incorporada.

### Reconciliación con La Gaceta

Hoy Plaza tiene pistas de publicación capturadas de SCIJ. Lo que no tiene es verificación cruzada con el feed oficial de La Gaceta publicado por la Imprenta Nacional. Esa reconciliación convierte pistas en hechos verificados y habilita la pregunta "¿cuándo entró realmente en vigor esta norma?" con autoridad completa.

**Criterio de incorporación**: acuerdo de acceso con la Imprenta Nacional, o captura estructurada sostenible del archivo público de La Gaceta.

### Capa institucional

El Estado costarricense como grafo de entidades: poderes, ministerios, órganos adscritos, instituciones autónomas. Modelado bajo W3C ORG. Esta capa es la raíz de cualquier análisis institucional serio y es la visión de largo plazo.

**Criterio de incorporación**: corpus normativo estable (cobertura, coherencia, versiones), gobernanza explícita sobre qué cuenta como institución y cómo se verifica, y alineación formal con los identificadores oficiales donde existan.

### Capa de cargos

Las posiciones dentro de las instituciones como entidades abstractas — "Ministro de Hacienda", "Presidente de la CCSS", "Contralor General" — sin identificar quién las ocupa. Modeladas bajo W3C ORG como posts.

**Criterio de incorporación**: capa institucional estable, y fuentes oficiales para la definición de cargos, típicamente las leyes orgánicas que los crean.

### Capa de funcionarios públicos

Identificar a las personas específicas que ocupan cargos públicos, con períodos de ocupación, evidencia de nombramiento, y autoridad que nombró o removió. Requiere el marco de gobernanza más riguroso del proyecto entero.

**Criterio de incorporación**: capa de cargos estable, fuentes oficiales de nombramientos, marco explícito de privacidad y rectificación, justificación jurídica escrita de que la finalidad de transparencia normativa de Plaza es consistente con la finalidad original con la que los datos fueron publicados por la institución correspondiente, y decisión colectiva del proyecto de que el beneficio justifica la sensibilidad. Puede no ocurrir nunca, y eso es legítimo. El respaldo jurídico aplicable está en [`LEGAL_BASIS.md`](LEGAL_BASIS.md).

### Corpus completo de jurisprudencia

El acervo del Poder Judicial — sentencias, votos constitucionales — como corpus estructurado propio con versioning y relaciones internas, no solo como hooks desde normas. Interoperaría con el corpus normativo pero tiene su propia lógica institucional.

**Criterio de incorporación**: corpus normativo maduro, y convenio formal con el Poder Judicial que autorice explícitamente el procesamiento estructurado de jurisprudencia. El marco regulatorio actual del Poder Judicial en materia de datos personales prohíbe expresamente la construcción de bases paralelas mediante herramientas automatizadas, por lo que la vía del convenio es la única jurídicamente viable. Ver [`LEGAL_BASIS.md`](LEGAL_BASIS.md) para el respaldo jurídico detallado.

### Corpus completo de pronunciamientos PGR

El acervo completo de dictámenes de la Procuraduría como corpus propio, no solo hooks. Similar al caso de jurisprudencia.

**Criterio de incorporación**: corpus normativo maduro, y acceso a los pronunciamientos en formato procesable.

---

## Explícitamente fuera, posiblemente para siempre

Estas exclusiones no son de secuencia — son de identidad. Si Plaza alguna vez hace estas cosas, será un proyecto distinto.

### Interfaces para usuarios finales

Plaza no construye una web consumer-facing para navegar el derecho costarricense. Si alguien la necesita, la construye sobre los contratos públicos que Plaza expone. Esta exclusión protege la separación entre dato y aplicación, y la durabilidad del proyecto.

### Razonamiento legal automático

Plaza no interpreta, no predice, no razona sobre el derecho. Plaza representa. La interpretación jurídica es trabajo humano o es algo que las aplicaciones construyen sobre Plaza — no algo que Plaza hace en representación de otros. Plaza puede servir de fundamento a sistemas de razonamiento, pero no incorpora ese razonamiento en su corpus.

### Modelado de ciudadanos privados

Plaza no identifica ni modela personas privadas, ni siquiera cuando aparezcan mencionadas en textos normativos. Los nombres en textos oficiales se preservan como parte del texto — es una cita textual de un documento público — pero nunca se extraen como datos estructurados ni se convierten en entidades del grafo. La distinción entre funcionarios públicos (que eventualmente podrían entrar con gobernanza) y ciudadanos privados (que nunca) es dura.

### Información no pública

Plaza solo trabaja con información que ya es pública. Si una fuente le ofrece datos reservados bajo acuerdos de confidencialidad, con fines académicos limitados, o con cualquier restricción de redistribución, Plaza los rechaza. La apertura de Plaza es simétrica: lo que entra, sale.

---

## Criterios para mover algo del norte al presente

Que algo esté listado como futuro no significa que vaya a ocurrir automáticamente. Incorporarlo al alcance activo requiere que se cumplan estos cuatro criterios, conjuntamente:

1. **Madurez del alcance actual.** Extender el alcance antes de que lo que ya existe esté estable compromete ambas cosas.
2. **Fuente oficial disponible.** Nada entra al alcance sin fuente respaldable. La ambición no sustituye a la evidencia.
3. **Gobernanza proporcional a la sensibilidad.** Cuanto más cercana a lo humano la entidad, más explícita la gobernanza requerida. Este criterio es más estricto que un simple check de viabilidad técnica.
4. **Capacidad sostenida de mantenimiento.** Extender el alcance sin capacidad de sostenimiento es peor que no extenderlo. Plaza prefiere hacer menos bien que hacer más mal.

---

## Cómo manejar propuestas nuevas

Cuando alguien propone agregar algo, el procedimiento es:

1. **¿Está en el alcance actual?** Adelante, siguiendo los principios.
2. **¿Está en el norte futuro?** Evaluar si los cuatro criterios de incorporación se cumplen. Si no, registrar la propuesta como señal de interés y posponer.
3. **¿Está explícitamente fuera?** No. La carga de argumentación para reabrir esa discusión es alta y requiere revisar los principios, no el alcance.
4. **¿No está listado?** Es una decisión nueva que este documento debe absorber. Actualizar este documento es parte del proceso de aceptación, no un paso posterior.

---

## Versión del alcance

El alcance descrito en este documento corresponde a Plaza el lunes 20 de abril del 2026. Cuando el proyecto incorpore oficialmente una de las áreas listadas como norte futuro, este documento se actualiza y la versión avanza. Las versiones históricas del alcance se preservan como evidencia de la evolución del proyecto, no como planes vigentes.

---

## Relación con otras políticas

- [`VISION.md`](VISION.md) — la visión estratégica que este alcance sirve.
- [`PRINCIPLES.md`](PRINCIPLES.md) — los principios que gobiernan qué puede entrar al alcance y qué no.
- [`URI_POLICY.md`](URI_POLICY.md) — la política de identidad aplicable a las entidades dentro del alcance actual; se extiende cuando el alcance se extienda.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — las superficies por las cuales el alcance actual se expone.
- [`LICENSING.md`](LICENSING.md) — los términos bajo los cuales el alcance actual se publica.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — cómo la arquitectura interna soporta el alcance actual y admite los elementos del norte futuro.
- [`DATA_MODEL.md`](DATA_MODEL.md) — el modelo semántico de las entidades que el alcance actual incluye.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — los criterios de calidad aplicables a las entidades dentro del alcance.
- [`VERSIONING.md`](VERSIONING.md) — cómo se versiona este documento cuando el alcance evoluciona.
- [`LEGAL_BASIS.md`](LEGAL_BASIS.md) — el respaldo jurídico concreto para los criterios de incorporación que involucran datos sensibles o instituciones con regímenes específicos.
- [`REFERENCES.md`](REFERENCES.md) — glosario, estándares y bibliografía.

