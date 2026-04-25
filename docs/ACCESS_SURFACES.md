# Plaza — Superficies de Acceso

Este documento define las formas en que Plaza pone sus datos a disposición del mundo. Cada superficie es un **contrato público**: establece qué entrega Plaza, qué garantiza, qué no garantiza, y qué espera del consumidor.

Las superficies no son implementaciones, son compromisos. La implementación concreta puede evolucionar; el contrato no. Cuando una implementación se vuelve inviable, se sustituye por otra que honre el mismo contrato — nunca se rompe el contrato para simplificar la implementación.

El Principio 7 (Separación entre dato y aplicación) gobierna todo este documento. Las superficies exponen los datos; las aplicaciones se construyen encima.

---

## Superficies actuales

Plaza expone cuatro superficies principales y dos auxiliares. Todas son públicas, gratuitas, y sin registro requerido para uso razonable. Todas siguen los identificadores definidos en la [Política de URIs](URI_POLICY.md).

### 1. Snapshots descargables

**Contrato**: Plaza publica, a intervalos regulares, exports completos del corpus normativo en formatos estándar. Un snapshot descargado hoy produce exactamente las mismas respuestas si se consulta mañana. Los snapshots son inmutables una vez publicados.

**Formatos ofrecidos**:

- **RDF/Turtle** — serialización canónica para consumo semántico
- **JSON-LD** — serialización amigable para aplicaciones web y APIs
- **Akoma Ntoso XML** — serialización documental derivada para interoperabilidad con sistemas legales internacionales; no es la representación canónica del grafo
- **Volcado SQLite** — serialización operacional para quien prefiera trabajar relacional

RDF/Turtle y JSON-LD son las serializaciones primarias del grafo canónico. Akoma Ntoso XML es una representación documental derivada.

Cada snapshot incluye su propio identificador único, fecha de generación, hash criptográfico del contenido, y referencia al snapshot anterior. Los snapshots son inmutables y verificables. Cuando aplique, cada snapshot debe poder declarar también, por conjunto publicado, su fuente principal, base jurídica o licencia conocida, fecha de revisión del régimen aplicable, y condición de publicabilidad.

**Garantías**:

- Reproducibilidad total: el mismo snapshot produce los mismos datos para siempre.
- Completitud: cada snapshot contiene todo el corpus al momento de su generación — nunca es un subconjunto.
- Autocontención: cada snapshot incluye su propia definición de esquema, vocabularios controlados, y documentación de estructura.
- Accesibilidad sin fricción: los snapshots se descargan por HTTP directo sin autenticación.

**No se garantiza**:

- Frecuencia de actualización comprometida. Plaza publica snapshots cuando hay cambios sustantivos, sin calendario fijo.
- Retención indefinida de snapshots históricos en línea. Los más recientes siempre están disponibles; los muy antiguos pueden moverse a almacenamiento archival con acceso más lento.

**A quién sirve**: investigadores haciendo análisis reproducible, instituciones que integran Plaza en sistemas cerrados, desarrolladores que necesitan una copia local para desarrollo offline, auditores que verifican el estado del corpus en un momento específico.

---

### 2. API REST

**Contrato**: cada recurso identificado por una URI canónica es consultable vía HTTP GET sobre esa URI. El formato de respuesta se negocia por el header `Accept`. La URI es el contrato; el método es siempre GET; el resultado es siempre determinista para un snapshot dado.

**Operaciones soportadas**:

- **Resolución de identidad**: dada una URI canónica, devuelve el recurso correspondiente. La URI canónica es el método de consulta primario.
- **Búsqueda**: consultas por texto libre y por metadatos sobre el corpus, expuestas como recurso propio bajo `/search` con parámetros de consulta. La búsqueda no es una operación sobre una URI canónica — es un recurso distinto que devuelve listas de URIs canónicas.
- **Navegación del grafo**: las relaciones entre normas se expresan como propiedades del recurso en la respuesta (afectaciones, concordancias, reglamentaciones como predicados RDF), no como subpaths de la URI canónica. El consumidor navega siguiendo los enlaces en la respuesta.
- **Resolución temporal**: se expresa mediante URIs con componente de versión, siguiendo estrictamente la [Política de URIs](URI_POLICY.md). La pregunta "qué decía esta norma en esta fecha" se responde construyendo la URI de versión correspondiente, no mediante parámetros de consulta.

**Formatos ofrecidos** (vía content negotiation):

- `application/ld+json` — JSON-LD (default para consumidores API)
- `text/turtle` — Turtle
- `application/akoma-ntoso+xml` — Akoma Ntoso XML derivado, disponible cuando el recurso tenga representación documental suficiente
- `text/html` — HTML con RDFa embebido (para inspección humana)
- `application/json` — JSON simplificado sin contexto semántico (para consumidores que no manejan LD)

**Garantías**:

- Estabilidad de URIs: una URI que funciona hoy funcionará en diez años. Las URIs no llevan versión de API en el path — siguen exactamente la estructura definida en la [Política de URIs](URI_POLICY.md).
- Idempotencia: misma URI, mismo snapshot, misma respuesta, siempre.
- Sin autenticación para uso razonable: Plaza es público por construcción.
- Evolución sin ruptura: nuevas capacidades se agregan de forma compatible; cambios genuinamente incompatibles, de ocurrir, se ofrecen como media types nuevos o servicios complementarios, nunca reescribiendo URIs existentes.
- Honestidad de publicabilidad: cuando una entidad o conjunto esté sujeto a restricciones de publicación, la superficie pública no debe simular apertura completa; debe omitirlo, degradarlo a referencia, o exponer solo la metadata permitida.

**No se garantiza**:

- Uptime absoluto. Plaza es un proyecto comunitario; la disponibilidad se busca pero no se compromete contractualmente.
- Ausencia de límites de tasa. Plaza aplica límites razonables por IP/token para prevenir abuso; consumidores de alto volumen deben usar snapshots.

**A quién sirve**: aplicaciones web, sistemas integrados, desarrolladores construyendo sobre Plaza, cualquier consumidor que necesita datos actualizados sin mantener infraestructura local.

---

### 3. Servidor MCP

**Contrato**: Plaza expone un servidor [Model Context Protocol](https://modelcontextprotocol.io/) que permite a sistemas de inteligencia artificial consultar el corpus normativo costarricense directamente, con capacidad de retrieval, búsqueda y citación verificable.

MCP es el protocolo primario de consumo por IA en el momento de publicar esta política. Si el ecosistema de IA converge hacia otro protocolo estándar, Plaza lo adoptará en paralelo — los datos son los mismos, solo cambia la superficie.

**Capacidades expuestas**:

- **Retrieval por URI canónica**: el LLM recibe el texto normativo exacto con su metadata.
- **Búsqueda semántica**: el LLM consulta por concepto y recibe normas relevantes con sus URIs.
- **Navegación contextual**: el LLM solicita relaciones, versiones anteriores, o contexto de vigencia.
- **Citación verificable**: toda respuesta del servidor MCP incluye URIs canónicas que el usuario final puede verificar.

**Garantías**:

- Citación obligatoria: ninguna respuesta del servidor MCP omite las URIs de las fuentes consultadas. Un LLM que use Plaza vía MCP nunca produce afirmaciones sin fuente verificable.
- Separación entre dato y interpretación: el servidor MCP entrega texto normativo, nunca interpretaciones. La interpretación es trabajo del LLM consumidor, no de Plaza.
- Interoperabilidad multi-modelo: el servidor MCP no está atado a un proveedor específico. Cualquier LLM que implemente MCP puede consumir Plaza.

**No se garantiza**:

- Respuestas en lenguaje natural. MCP entrega datos estructurados; la generación de prosa es responsabilidad del LLM consumidor.
- Compatibilidad eterna con versiones anteriores del protocolo MCP. Plaza sigue la evolución del estándar.

**A quién sirve**: asistentes de IA legales, chatbots institucionales, herramientas de análisis automatizado, cualquier sistema de IA que necesite razonar sobre derecho costarricense con trazabilidad.

---

### 4. Catálogo DCAT

**Contrato**: Plaza publica un catálogo [DCAT](https://www.w3.org/TR/vocab-dcat-3/) que describe todos los datasets y servicios que ofrece, en formato procesable por agregadores de datos abiertos.

**Contenido**:

- Descripción de cada snapshot publicado (título, fecha, formato, URL de descarga, hash).
- Descripción de la API REST como `DataService`.
- Descripción del servidor MCP como `DataService`.
- Metadata de licenciamiento, autoría, y contacto.

**Garantías**:

- Conformidad con DCAT 3.
- Federación posible: el catálogo de Plaza puede ser absorbido por portales de datos abiertos (incluyendo `datos.gob` si Costa Rica llega a tener uno, o agregadores internacionales).

**A quién sirve**: portales de datos abiertos, buscadores de datasets, agregadores institucionales que quieren listar Plaza como recurso.

---

### 5. Feed de cambios (auxiliar)

**Contrato**: Plaza publica un feed Atom y un sitemap XML siguiendo el [Pilar 4 de ELI](https://eur-lex.europa.eu/eli-register/implementing_eli.html), que notifica cambios en el corpus.

**Contenido**:

- Normas recién incorporadas al corpus.
- Versiones nuevas de normas existentes.
- Correcciones a metadata de normas previamente publicadas (con motivo explícito).

**Garantías**:

- Formato Atom estándar, consumible por cualquier agregador.
- Cada entrada del feed referencia URIs canónicas de Plaza.
- Sitemap actualizado que lista todas las URIs publicadas.

**A quién sirve**: suscriptores que quieren estar al tanto de cambios normativos, agregadores de legislación, investigadores construyendo observatorios, sistemas que cachean Plaza y necesitan invalidación.

---

### 6. Representación HTML (auxiliar, no producto)

Cuando una URI canónica se solicita con `Accept: text/html`, Plaza responde con una página HTML mínima que muestra la metadata del recurso y enlaces a sus relaciones, con RDFa embebido para procesamiento semántico.

**Esta superficie NO es un producto consumer-facing**. Es la representación por defecto del recurso cuando un navegador lo visita, consistente con las prácticas de ELI. Plaza no agrega funcionalidad de navegación, búsqueda estética, o experiencia de usuario sobre esta representación. Eso es trabajo de aplicaciones construidas sobre Plaza — no de Plaza misma.

El HTML está ahí porque el estándar lo pide y porque facilita inspección y debugging. Nunca se promociona como la forma de consumir Plaza.

Cuando aplique, las superficies públicas deben ofrecer un mecanismo visible de rectificación o contacto para correcciones relacionadas con fuente, exactitud o tratamiento de datos.

---

## Superficies futuras

Estas superficies no están disponibles actualmente, pero están reconocidas como extensiones naturales futuras. Su incorporación sigue los criterios establecidos en [SCOPE.md](SCOPE.md).

### Endpoint SPARQL

Un endpoint SPARQL público permitiría consultas declarativas arbitrarias sobre el grafo semántico de Plaza. Es poderoso, pero también costoso de operar y difícil de proteger contra consultas mal formadas o maliciosas.

**Criterio de incorporación**: estabilidad demostrada del corpus semántico, casos de uso reales que justifiquen el costo operativo, y capacidad para moderar el acceso (posiblemente con tokens para consultas pesadas).

### API de análisis temporal avanzado

Consultas sobre cómo evolucionó el corpus a lo largo del tiempo: "qué leyes se reformaron más entre 2015 y 2020", "qué normas fueron derogadas en cadena." Actualmente computable sobre snapshots, pero podría expuesta como superficie de primera clase.

**Criterio de incorporación**: demanda concreta, definición estable de qué operaciones componen el análisis temporal.

### Webhooks de cambios

Notificaciones push cuando una norma de interés específico cambia, en lugar del pull model del feed Atom.

**Criterio de incorporación**: infraestructura de sostenimiento adecuada, demanda real de consumidores.

---

## Superficies explícitamente fuera

Estas superficies están listadas como fuera del alcance — no como postergación, sino como decisión de identidad de Plaza.

### APIs privadas o premium

Plaza no ofrece APIs con acceso privilegiado, tiers pagos, o endpoints reservados para aliados. Lo que Plaza expone, lo expone para todos. Esta regla no es negociable (ver Principio 9).

### Endpoints personalizados para consumidores específicos

Plaza no construye endpoints optimizados para las necesidades de un consumidor particular (ver Principio 7). Si un consumidor necesita una transformación particular, la aplica sobre las superficies existentes.

### Interfaces consumer-facing

Plaza no construye una aplicación web, móvil, o de escritorio para que usuarios finales naveguen el derecho costarricense. Si alguien necesita esa experiencia, la construye sobre las superficies que Plaza expone. Plaza es infraestructura, no aplicación (ver SCOPE).

---

## Compromisos operativos

### Límites de tasa

Plaza aplica límites de tasa razonables por IP en la API REST y el servidor MCP, calibrados para permitir uso individual y de aplicaciones modestas sin fricción, pero suficientes para prevenir abuso o agotamiento de recursos. Los límites específicos se documentan en un documento operativo separado y pueden ajustarse según el uso real.

Consumidores con volúmenes mayores tienen dos opciones: usar snapshots (que no tienen límites, solo el ancho de banda de descarga), o contactar al proyecto para coordinar el acceso. Esta coordinación nunca implica acceso privilegiado a datos distintos — solo ajuste de cuotas.

### Caché

Las respuestas de la API REST son cacheables siguiendo los headers HTTP estándar (`Cache-Control`, `ETag`). Los snapshots son inmutables por definición. Plaza fomenta el caching agresivo por parte de los consumidores.

### Degradación graciosa

Si alguna superficie no está disponible temporalmente, las demás siguen funcionando en lo posible. En particular, los snapshots son independientes de la disponibilidad de la API: un consumidor que tenga el último snapshot puede seguir operando aunque la API esté caída.

### Sin promesas de uptime contractual

Plaza es un proyecto de código abierto con sostenimiento comunitario. No ofrece SLAs contractuales de disponibilidad. Para consumidores que requieren uptime garantizado, la estrategia correcta es replicar los snapshots localmente — ese es precisamente uno de los propósitos de publicar snapshots.

---

## Versionado de superficies

Cada superficie se versiona independientemente, usando versionado semántico:

- **Snapshots**: cada uno tiene su propio identificador; no se "versiona" sino que se suceden.
- **API REST**: las URIs canónicas no cambian ni se versionan — son el contrato permanente establecido en la [Política de URIs](URI_POLICY.md). La evolución del protocolo de acceso (cambios en formatos de respuesta, nuevas capacidades, parámetros de consulta) se maneja mediante content negotiation y documentación de capacidades, no mediante prefijos de versión en el path. Si alguna vez una evolución de la API fuera genuinamente incompatible, se ofrecería mediante un nuevo media type o mediante un servicio complementario — nunca reescribiendo las URIs canónicas.
- **Servidor MCP**: sigue la versión del protocolo MCP; compatible hacia atrás en tanto el protocolo lo permita.
- **Catálogo DCAT**: sigue la versión de DCAT.
- **Feed Atom / sitemap**: sigue el estándar ELI Pilar 4.

Cambios dentro de una versión mayor son siempre compatibles. Nunca se cambia una superficie de forma que rompa consumidores existentes sin anunciarlo públicamente y mantener la superficie anterior el tiempo necesario.

---

## Relación con otras políticas

Este documento se lee junto con:

- [`PRINCIPLES.md`](PRINCIPLES.md) — los principios que restringen qué superficies son aceptables.
- [`SCOPE.md`](SCOPE.md) — qué está dentro y fuera del alcance, incluyendo ciertas superficies.
- [`URI_POLICY.md`](URI_POLICY.md) — la estructura de identificadores que las superficies exponen.
- [`LICENSING.md`](LICENSING.md) — bajo qué términos los consumidores usan los datos.
- [`VERSIONING.md`](VERSIONING.md) — cómo se versiona el corpus mismo, no solo las superficies.
