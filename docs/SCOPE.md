# Plaza — Alcance

Este documento define qué hace Plaza hoy, qué podría hacer en el futuro, y qué queda explícitamente fuera. A diferencia de los principios, que son evergreen y gobiernan cómo Plaza hace lo que sea que haga, el alcance es temporal: describe el Plaza de esta etapa. Evoluciona cuando las condiciones cambian.

El propósito es doble: proteger al proyecto del scope creep — la tendencia a agregar "solo una cosita más" hasta que nada se termina — y proteger al proyecto del reverso, que es subestimar su norte por timidez. Cuando alguien propone algo, este documento responde si ese algo está adentro, está fuera por ahora pero es parte del norte, o está fuera para siempre.

---

## En alcance actual

Plaza modela el **corpus normativo costarricense** como grafo estructurado, citable y verificable, distribuido como producto híbrido de snapshots descargables y servicios en vivo. La capacidad de adquisición automatizada existe, pero no define la identidad del proyecto: Plaza prioriza publicación proactiva, solicitud formal y convenio antes que automatización residual.

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

- **Registro de habilitación de fuentes**: para cada fuente incorporada, Plaza documenta su vía de acceso, régimen jurídico o licencia, restricciones relevantes, finalidad original o función pública de la fuente, uso previsto por Plaza, juicio de compatibilidad, y condición de publicabilidad.
- **Pistas de publicación**: referencias a La Gaceta donde una norma fue publicada oficialmente, tal como las expone SCIJ — sin verificación cruzada con el feed oficial de La Gaceta.
- **Hooks a pronunciamientos de la PGR**: referencias a dictámenes que interpretan las normas, sin incluir el corpus completo de pronunciamientos.
- **Hooks a acciones constitucionales**: referencias a votos de la Sala Constitucional que afectan normas, sin incluir el corpus completo de jurisprudencia.
- **Observaciones editoriales**: notas interpretativas que SCIJ asocia a las normas.

### Superficies de acceso

- **Snapshots descargables**: exports periódicos del corpus completo en RDF/Turtle y JSON-LD, más Akoma Ntoso XML como serialización documental derivada cuando exista estructura suficiente.
- **API REST pública**: endpoints deterministas sobre los identificadores canónicos, con URIs estables por norma, versión, artículo, y versión de artículo.
- **Servidor MCP**: interfaz nativa para sistemas de IA que consumen el corpus con retrieval verificable.
- **Catálogo DCAT**: descripción estructurada de los datasets publicados, para federación con otros portales de datos abiertos.

---

## Fuera del alcance actual, parte del norte

Estas áreas son reconocidas como extensiones naturales del proyecto. Su exclusión actual es de secuencia, no de principio. Cada una tiene un criterio explícito para ser incorporada.

### Reconciliación con La Gaceta

Hoy Plaza tiene pistas de publicación obtenidas de SCIJ. Lo que no tiene es verificación cruzada con el feed oficial de La Gaceta publicado por la Imprenta Nacional. Esa reconciliación convierte pistas en hechos verificados y habilita la pregunta "¿cuándo entró realmente en vigor esta norma?" con autoridad completa.

**Criterio de incorporación**: acuerdo de acceso con la Imprenta Nacional, acceso estructurado sostenible al archivo público de La Gaceta, o solo subsidiariamente adquisición estructurada del archivo público bajo un régimen jurídicamente compatible.

### Capa institucional

El Estado costarricense como grafo de entidades: poderes, ministerios, órganos adscritos, instituciones autónomas. Modelado bajo W3C ORG. Esta capa es la raíz de cualquier análisis institucional serio y es la visión de largo plazo.

**Criterio de incorporación**: corpus normativo estable (cobertura, coherencia, versiones), gobernanza explícita sobre qué cuenta como institución y cómo se verifica, y alineación formal con los identificadores oficiales donde existan.

### Capa de cargos

Las posiciones dentro de las instituciones como entidades abstractas — "Ministro de Hacienda", "Presidente de la CCSS", "Contralor General" — sin identificar quién las ocupa. Modeladas bajo W3C ORG como posts.

**Criterio de incorporación**: capa institucional estable, y fuentes oficiales para la definición de cargos, típicamente las leyes orgánicas que los crean.

### Titularidad oficial de cargos públicos

Si una capa institucional futura necesitara responder quién ejercía oficialmente un cargo público en una fecha determinada, Plaza solo podría representar la **titularidad oficial del cargo** a partir de actos oficiales de nombramiento, remoción, sustitución o designación.

Esa representación no constituye un perfil de la persona. Su finalidad sería exclusivamente institucional: preservar trazabilidad del ejercicio del cargo, continuidad administrativa, responsabilidad pública y control democrático.

Quedan fuera de esa lógica:
- la construcción de perfiles personales;
- la agregación biográfica general;
- las relaciones personales o sociales;
- atributos no funcionales;
- inferencias sobre conducta, afinidades o motivaciones;
- y cualquier modelado de personas privadas.

**Criterio de incorporación**: capa de cargos estable, actos oficiales verificables, marco explícito de privacidad y rectificación, justificación jurídica escrita de consistencia con la finalidad original de los datos publicados por la institución correspondiente, evaluación explícita del régimen de protección de datos aplicable, y decisión colectiva del proyecto de que la representación es estrictamente necesaria para la trazabilidad institucional. Puede no ocurrir nunca, y eso es legítimo. El respaldo jurídico aplicable está en [`LEGAL_BASIS.md`](LEGAL_BASIS.md).

### Corpus completo de jurisprudencia

El acervo del Poder Judicial — sentencias, votos constitucionales — como corpus estructurado propio con versioning y relaciones internas, no solo como hooks desde normas. Interoperaría con el corpus normativo pero tiene su propia lógica institucional.

**Criterio de incorporación**: corpus normativo maduro, y convenio formal con el Poder Judicial que autorice explícitamente el procesamiento estructurado de jurisprudencia. Mientras ese convenio no exista, la jurisprudencia estructurada del Poder Judicial no forma parte de la operación ordinaria publicable de Plaza. El marco regulatorio actual del Poder Judicial en materia de datos personales prohíbe expresamente la construcción de bases paralelas mediante herramientas automatizadas, por lo que la vía del convenio es la única jurídicamente viable. Ver [`LEGAL_BASIS.md`](LEGAL_BASIS.md) para el respaldo jurídico detallado.

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

Plaza no identifica ni modela personas privadas, ni siquiera cuando aparezcan mencionadas en textos normativos. Los nombres en textos oficiales se preservan como parte del texto — es una cita textual de un documento público — pero nunca se extraen como datos estructurados ni se convierten en entidades del grafo. Plaza no modela personas como parte de su corpus ordinario. En la única zona excepcional reconocible aquí, Plaza solo admitiría la representación estrictamente funcional y verificable de un hecho institucional de titularidad oficial del cargo cuando ello resulte indispensable para la trazabilidad institucional.

### Información no pública

Plaza solo trabaja con información que ya es pública. Si una fuente le ofrece datos reservados bajo acuerdos de confidencialidad, con fines académicos limitados, o con cualquier restricción de redistribución, Plaza los rechaza. La apertura de Plaza es simétrica: lo que entra, sale.

Plaza tampoco reutiliza información pública para fines incompatibles con la finalidad pública con la que fue recabada o publicada. La publicidad del dato no elimina por sí sola los límites sobre su reutilización posterior.

### Scraping indiscriminado como estrategia general de acceso

Plaza no adopta la extracción automatizada indiscriminada como postura de entrada al ecosistema estatal. La automatización existe como capacidad instrumental residual, no como identidad del proyecto.

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

