# Plaza — Política de URIs

Este documento define la estructura de identificadores públicos de Plaza. Es, junto con los principios, el compromiso técnico más duradero del proyecto: las URIs que Plaza publica hoy serán las mismas en diez años. Esta política se diseña para no cambiar.

El Principio 2 (Identidad permanente) y el Principio 6 (Estándares internacionales como columna) son los que gobiernan cada decisión en este documento. Donde una conveniencia local contradice al estándar, el estándar gana. Donde una limitación actual tentaría a cambiar el esquema, la limitación se resuelve — no el esquema.

---

## Alineación con ELI

Plaza adopta el **European Legislation Identifier (ELI)** como patrón de URIs. Esta decisión no es arbitraria: ELI es el estándar más adoptado globalmente para identificar legislación, está implementado por la Unión Europea y por varios estados miembros (incluyendo España, Italia, Francia, Irlanda, Polonia), y fue diseñado precisamente para permitir que cada jurisdicción defina su propia convención dentro de un marco común.

Plaza no es un publicador oficial de derecho costarricense. SCIJ/PGR lo es. Pero dado que Costa Rica no ha adoptado oficialmente ELI al momento de redactar esta política, Plaza define una **implementación ELI provisional costarricense**, documentada como tal. Si en el futuro PGR, la Imprenta Nacional, o cualquier otra autoridad oficial adopta ELI con convenciones distintas, Plaza se adaptará — ya sea incorporando las URIs oficiales como alias canónicos, redirigiendo las URIs actuales, o ambas cosas. Plaza nunca mantiene URIs que contradigan una adopción oficial posterior.

Esta adaptación futura no viola el Principio 2. Las URIs actuales seguirán resolviendo al mismo recurso — eventualmente vía redirección a una URI oficial. Lo que no se hace es desaparecerlas.

---

## Estructura general

Todas las URIs canónicas de Plaza siguen este patrón:

```
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}
```

Con extensiones para subdivisiones y versiones:

```
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/version/{versión}
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/articulo/{articulo}
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/articulo/{articulo}/version/{versión}
https://plaza.cr/eli/cr/{emisor}/{año}/{tipo}/{número}/transitorio/{transitorio}
```

Cada componente tiene reglas explícitas. Todas las URIs son case-sensitive y usan exclusivamente minúsculas, guiones bajos y caracteres ASCII alfanuméricos. No hay acentos, no hay eñes, no hay espacios.

---

## Componentes

### `{jurisdicción}` — siempre `cr`

La jurisdicción es Costa Rica, codificada como `cr` siguiendo el estándar ISO 3166-1 alfa-2. No varía, pero se mantiene explícita en la URI por compatibilidad con ELI y para permitir que el esquema eventualmente incluya jurisdicciones subnacionales (municipalidades) sin cambio de estructura.

### `{emisor}` — órgano que emite la norma

El emisor identifica al órgano constitucional o administrativo que emitió la norma. Plaza usa un vocabulario controlado cerrado:

- `asamblea` — Asamblea Legislativa (leyes, decretos legislativos)
- `poder_ejecutivo` — Presidencia con ministerios (decretos ejecutivos, reglamentos ejecutivos)
- `poder_judicial` — Poder Judicial (reglamentos internos, acuerdos de Corte Plena)
- `tse` — Tribunal Supremo de Elecciones
- `cgr` — Contraloría General de la República
- `pgr` — Procuraduría General de la República
- `defensoria` — Defensoría de los Habitantes
- `municipalidad_<codigo>` — municipalidades, con código territorial MIDEPLAN (ej. `municipalidad_101` para San José)
- `institucion_<slug>` — instituciones autónomas, cuando Plaza modele esa capa en el futuro

El vocabulario de emisores es parte de esta política. Agregar un emisor nuevo requiere actualizar este documento; no se inventan emisores ad hoc.

### `{año}` — año de emisión

El año en que la norma fue emitida (no promulgada, no publicada — emitida). Formato de cuatro dígitos: `1988`, `2023`. Para normas anteriores a 1900, el formato es el mismo: `1821`.

### `{tipo}` — tipo normativo

Vocabulario controlado cerrado:

- `ley` — ley ordinaria
- `ley_organica` — ley orgánica
- `decreto_ejecutivo` — decreto del Poder Ejecutivo
- `decreto_legislativo` — decreto legislativo
- `reglamento` — reglamento
- `directriz` — directriz ejecutiva
- `resolucion` — resolución
- `acuerdo` — acuerdo
- `codigo` — código
- `constitucion` — constitución política

Al igual que con los emisores, el vocabulario de tipos es parte de esta política. Nuevos tipos se agregan por modificación documentada.

### `{número}` — identificador natural

El identificador que la propia norma lleva. Para leyes, el número de ley (`7092`). Para decretos, el número de decreto. Para códigos (que no tienen número), el slug canónico: `civil`, `penal`, `trabajo`, `procesal_civil`, `procesal_penal`.

Para normas sin número claro o con identificadores compuestos, Plaza define un slug documentado que referencia la práctica oficial. Un ejemplo: un reglamento sin número único podría usar un slug derivado de su título canónico en SCIJ.

Cuando un identificador oficial contiene caracteres no-ASCII o puntuación, se normaliza conservando la forma legible más cercana: `ley_8634_bis` (no `ley_8634/bis`), `decreto_ejecutivo_34433_mag_s` (con guiones bajos, nunca espacios ni slashes).

---

## Subdivisiones

### Artículos

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42
```

Los artículos bis, ter, quater, etc. se expresan con guión bajo:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42_bis
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42_ter
```

Los artículos con letras (42A, 42B) siguen la misma convención:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42a
```

### Transitorios

Los transitorios tienen su propio path, no se mezclan con artículos:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/transitorio/i
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/transitorio/segundo
```

Se usa la forma con la que el transitorio se refiere a sí mismo en el texto oficial (romanos si el texto usa romanos, ordinales escritos si es el caso).

### Anexos

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/anexo/1
```

---

## Versiones

Las versiones son ciudadanos de primera clase en las URIs. La pregunta "¿qué decía esta norma en esta fecha?" se responde construyendo la URI correspondiente.

### Versión vigente

La URI sin componente de versión apunta siempre a la **versión actualmente vigente**:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092
```

Esto es un alias semántico: equivale a consultar la versión más reciente con fecha de vigencia menor o igual a hoy.

### Versión en fecha específica

Para anclar una versión en el tiempo, se usa la fecha de inicio de vigencia de esa versión, en formato ISO 8601:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/2023-01-15
```

Esta URI apunta a "la versión de la Ley 7092 que entró en vigor el 15 de enero de 2023." Si no hubo versión que entró en vigor exactamente ese día, la URI no resuelve — no se aproxima, no se redondea. La honestidad operativa (Principio 11) prohíbe inferir versiones.

### Versión original

Un alias específico para la versión originalmente emitida:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/original
```

### Versiones de artículos

Un artículo en una versión específica:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42/version/2023-01-15
```

Esto responde "¿qué decía el artículo 42 de la Ley 7092 el 15 de enero de 2023?"

---

## Formato de respuesta

La URI canónica identifica al **recurso**, no al formato. La forma concreta de la respuesta — HTML, JSON-LD, Turtle, Akoma Ntoso XML, texto plano — se determina por **content negotiation** usando el header `Accept`:

```
GET https://plaza.cr/eli/cr/asamblea/1988/ley/7092
Accept: application/ld+json
```

No hay URIs distintas para formatos distintos. Esto es requisito del estándar ELI y de los principios de la web semántica. Plaza nunca publica URIs del tipo `/ley/7092.json` o `/ley/7092/html` — esas son preocupaciones de protocolo, no de identidad.

Las representaciones Akoma Ntoso pueden contener identificadores XML internos, pero estos no sustituyen ni compiten con la URI canónica Plaza/ELI.

---

## Casos especiales

### Constitución Política

La Constitución no tiene número ni fecha de emisión en el sentido ordinario. Su URI es:

```
https://plaza.cr/eli/cr/asamblea/1949/constitucion/politica
```

Usando 1949 como año de emisión (fecha de promulgación de la Constitución vigente) y `politica` como slug identificador.

### Códigos

Los códigos no tienen número pero sí fecha de emisión original:

```
https://plaza.cr/eli/cr/asamblea/1886/codigo/civil
https://plaza.cr/eli/cr/asamblea/1970/codigo/penal
```

### Normas derogadas

Las normas derogadas mantienen sus URIs. Una norma derogada no deja de existir — deja de estar vigente. La URI sigue resolviendo al recurso, que incluye metadata sobre su derogación (norma derogadora, fecha efectiva, evidencia).

### Normas con metadata incompleta

Cuando Plaza no puede determinar con certeza alguno de los componentes de la URI (año, emisor, número), la norma no recibe una URI canónica todavía. Se mantiene en el grafo interno con identificador provisional y se emite solo cuando la evidencia es suficiente. Esto aplica estrictamente el Principio 1 (Evidencia antes que inferencia) al nivel de identidad.

---

## Reglas duras

**1. Las URIs no cambian.** Una URI publicada se compromete para siempre. Si la interpretación interna de un campo cambia, se emiten URIs adicionales como alias — nunca se reescribe una URI existente.

**2. No hay URIs alternativas no canónicas.** Cada recurso tiene exactamente una URI canónica. Los alias son aceptables (como los que se introducirán si Costa Rica adopta ELI oficialmente), pero siempre apuntan a la canónica y nunca al revés.

**3. No se colapsan distinciones por conveniencia.** Si dos normas distintas podrían colisionar en una URI (mismo emisor, mismo año, mismo tipo, mismo número), esa colisión es una señal de que la política necesita refinarse, no de que se puede "resolver" fusionando. Esta situación requiere una actualización documentada de esta política.

**4. Los componentes son parte del contrato.** Cambiar el vocabulario de emisores o de tipos es modificar la política pública de URIs, no una decisión interna. Requiere actualización formal de este documento y comunicación pública si ya hay URIs publicadas que se afectan.

**5. Los identificadores internos no contaminan las URIs.** Plaza tiene identificadores internos (slugs como `ley_7092`, `scij_identifier` con `nValor1:nValor2:nValor3`) que son útiles operativamente pero nunca aparecen en las URIs públicas. Las URIs son el contrato con el mundo; los identificadores internos son detalle de implementación.

---

## Relación con identificadores internos

Plaza mantiene tres capas de identidad, claramente separadas:

1. **Identidad de adquisición** — los identificadores de la fuente original (SCIJ `nValor1:nValor2:nValor3`, URLs de La Gaceta, etc.). Viven en el grafo de evidencia y nunca se exponen públicamente como identidad canónica.
2. **Identidad interna de Plaza** — slugs operativos como `ley_7092` que se usan en código, tablas, y logs. Son estables pero no son el contrato público.
3. **URI canónica pública** — lo definido en este documento. Es lo que Plaza le entrega al mundo.

Las tres capas se mapean unidireccionalmente de 1 a 3 vía el proceso de canonicalización. Las reglas de ese proceso están en los principios (1 y 3) y en el modelo de datos (documentado separadamente).

---

## Versionado de esta política

Esta política es versionada. La versión inicial es `0.1.0`, correspondiente al estado pre-lanzamiento del proyecto. El salto a `1.0.0` ocurre con el primer lanzamiento público formal, momento en el cual las reglas de compatibilidad de cambios (descritas abajo) pasan a aplicarse estrictamente.

**Cambios compatibles (incrementan el minor o patch)**: agregar emisores al vocabulario, agregar tipos normativos, agregar subdivisiones nuevas (como `capitulo` si se decide modelar), aclarar ambigüedades del texto.

**Cambios incompatibles (requieren mayor)**: cambiar la estructura general, retirar emisores o tipos, cambiar reglas de resolución. Un cambio mayor requiere decisión pública documentada, período de convivencia con la versión anterior, y estrategia explícita para las URIs emitidas bajo la versión previa.

Como regla práctica, los cambios mayores tienden a cero. Si Plaza descubre que su diseño inicial era incorrecto, la respuesta preferida es extender (agregar un componente opcional, un alias, una regla complementaria) antes que romper.

---

## Cuándo esta política cambia

Tres disparadores legítimos para revisar esta política:

1. **Adopción oficial de ELI en Costa Rica.** Si PGR, la Imprenta Nacional, o cualquier órgano oficial publica un esquema ELI para Costa Rica, Plaza se alinea. Las URIs de Plaza se convierten en alias hacia las oficiales o se redirigen según corresponda.

2. **Expansión de alcance.** Cuando Plaza incorpore nuevas capas de modelado (instituciones, cargos), esta política se extiende con nuevos emisores y tipos — sin tocar lo existente.

3. **Descubrimiento de una ambigüedad o colisión no prevista.** Si dos normas distintas podrían colapsar en la misma URI, la política se refina para distinguirlas, sin reescribir URIs ya publicadas.

Cambios motivados por preferencia estética, simplificación retrospectiva, o conveniencia de implementación **no son disparadores legítimos**. El Principio 2 prohíbe esas motivaciones explícitamente.

---

## Relación con otras políticas

- [`VISION.md`](VISION.md) — la visión estratégica que las URIs permanentes de Plaza concretan.
- [`PRINCIPLES.md`](PRINCIPLES.md) — especialmente los Principios 2 (Identidad permanente) y 6 (Estándares internacionales como columna), de los cuales este documento es implementación operativa.
- [`SCOPE.md`](SCOPE.md) — define qué entidades reciben URIs bajo esta política.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — las superficies por las cuales las URIs definidas aquí son consumibles.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — describe dónde dentro del pipeline las URIs canónicas se asignan.
- [`DATA_MODEL.md`](DATA_MODEL.md) — usa las URIs definidas aquí como identidades de las entidades del grafo canónico.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — define cuándo una entidad puede recibir URI canónica bajo esta política.
- [`LICENSING.md`](LICENSING.md) — establece los términos de redistribución de los recursos identificados por estas URIs.
- [`VERSIONING.md`](VERSIONING.md) — define cómo se versiona esta política misma.
