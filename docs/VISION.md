# Plaza — Visión

## Qué es Plaza

Plaza es un corpus normativo costarricense estructurado, verificable y alineado a estándares internacionales, diseñado para ser **fuente confiable de derecho vigente para sistemas de inteligencia artificial** y, por extensión, para cualquier sistema o persona que necesite razonar sobre la ley costarricense con trazabilidad.

Plaza no es un sitio web. No es un buscador. No es una aplicación. Plaza es la capa de datos sobre la cual esas cosas pueden construirse — por Plaza mismo o por terceros — con la garantía de que lo que construyan descansa sobre información veraz, citable y temporalmente precisa.

## Por qué Plaza existe

La información jurídica costarricense es pública por mandato constitucional, y existe un marco legal habilitante que obliga al Estado a publicarla en formatos abiertos e interoperables. Aun así, el corpus normativo del país no es accesible en los términos que el siglo XXI exige.

SCIJ — el sistema oficial — cumple su función histórica como navegador humano del corpus legal. Sus identificadores de recursos son estables, pero no son derivables programáticamente ni alineados con los estándares internacionales de datos jurídicos. Para que un sistema externo consulte una norma específica, primero debe descubrir sus parámetros internos — lo que rompe la interoperabilidad automática. No hay API pública documentada. No hay descargas estructuradas. No hay vocabulario común con el ecosistema global de derecho-como-dato.

Esta brecha tiene un costo concreto. Cuando un asistente de inteligencia artificial responde hoy sobre derecho costarricense, usualmente lo hace desde conocimiento memorizado durante su entrenamiento: puede estar desactualizado, puede alucinar un artículo, y su capacidad de citar fuentes verificables depende de si tiene acceso a un corpus confiable sobre el cual hacer retrieval. Ese corpus confiable, estructurado y citable no existe hoy para el derecho costarricense. El usuario no tiene cómo verificar. El abogado no puede citar con trazabilidad. El ciudadano no puede confiar.

Plaza cierra esa brecha. Transforma el corpus normativo costarricense en un recurso que cualquier sistema puede consultar con la garantía de que cada afirmación se ancla en un texto oficial identificable, con versión explícita, con fecha de vigencia, y con enlace directo al artículo correspondiente.

## Qué hace Plaza

Plaza toma la normativa costarricense — leyes, decretos, reglamentos, y sus relaciones entre sí — y la expone como un corpus estructurado con tres compromisos fundamentales:

**Identidad estable.** Cada norma, cada versión, cada artículo tiene un identificador único, permanente y legible que no cambia nunca. Un enlace a un artículo hoy seguirá siendo válido en diez años.

**Provenance explícito.** Cada afirmación en Plaza apunta a su fuente oficial — la página de SCIJ o La Gaceta donde fue originalmente publicada — con fecha de captura y evidencia preservada. Nada es inferido sin marcarse como tal.

**Precisión temporal.** Plaza responde no solo "¿qué dice esta ley?" sino "¿qué decía esta ley en esta fecha?" Las versiones son objetos de primera clase, no notas al pie.

Todo esto se expresa en el vocabulario de los estándares internacionales de datos jurídicos: ELI para la estructura de identificadores, schema.org/Legislation y Akoma Ntoso para la estructura de los textos, PROV-O para la procedencia, SKOS para los vocabularios controlados. Plaza no es un experimento costarricense; es la manera costarricense de participar de una conversación global sobre cómo debe exponerse el derecho en la era de los datos.

## A quién sirve Plaza

El consumidor primario de Plaza en su etapa inicial son los **sistemas de inteligencia artificial** que necesitan responder sobre derecho costarricense con fuentes verificables. Esto incluye asistentes legales, chatbots gubernamentales, herramientas de análisis, motores de búsqueda semántica, y cualquier aplicación que quiera razonar sobre la ley sin inventarla.

Por extensión — y sin requerir trabajo adicional de Plaza — el corpus también sirve a los humanos que consumen esos sistemas: abogados que verifican citas, ciudadanos que consultan asistentes, investigadores que hacen análisis, periodistas que rastrean cambios normativos. Plaza no compite con SCIJ para el lector humano directo; complementa a SCIJ siendo la capa que los sistemas pueden consumir donde SCIJ no alcanza.

## Qué no es Plaza

Plaza no es un sustituto de SCIJ. SCIJ sigue siendo la fuente oficial; Plaza es una representación estructurada de esa fuente, construida con respeto por su autoridad institucional.

Plaza no es, por ahora, un mapa del Estado costarricense. La visión de más largo plazo — un grafo que conecte leyes con instituciones, cargos y personas — queda explícitamente fuera del alcance actual. Esa ambición requiere que el substrato normativo esté maduro primero. Plaza la habilita, pero no la incluye.

Plaza no es una aplicación para usuarios finales. No tiene interfaz propia. La interfaz — si existe — la construye quien quiera, sobre los contratos públicos que Plaza expone. Esa separación es deliberada: las aplicaciones envejecen, los datos estructurados perduran.

## Cómo se distribuye Plaza

Plaza se distribuye como producto híbrido: snapshots descargables para consumo masivo, análisis reproducible, o incorporación en sistemas cerrados; y API en vivo (REST + MCP) para consultas puntuales, aplicaciones de IA, y cualquier consumidor que necesite datos actualizados sin mantener su propia infraestructura.

Los snapshots garantizan reproducibilidad: el mismo snapshot consultado en cualquier momento produce las mismas respuestas. La API garantiza actualidad: siempre refleja el estado más reciente del corpus normativo.

Ambas superficies comparten los mismos identificadores, los mismos estándares, y el mismo modelo de provenance.

## El compromiso de Plaza

Plaza es un proyecto de código abierto desarrollado con vocación cívica. Su compromiso con quienes lo consumen y con el país es triple:

**Con la verdad.** Plaza publica solo lo que puede respaldar con evidencia. Cuando hay incertidumbre, la declara. Cuando hay conflicto entre fuentes, lo registra. El sistema sabe lo que no sabe y no lo esconde.

**Con la estabilidad.** Los identificadores que Plaza publica hoy seguirán funcionando mañana, el año que viene, y en diez años. Los estándares a los que Plaza se alinea están elegidos precisamente por esa durabilidad.

**Con la apertura.** El código de Plaza, sus datos, sus esquemas, y sus decisiones están publicados bajo licencias que garantizan que nadie pueda cerrar lo que Plaza abre. La ley es pública; su representación también debe serlo.

## Plaza como proyecto abierto

Plaza es, antes que un producto, un bien común. Su código es abierto, sus datos son abiertos, sus decisiones de diseño se discuten en público, y su desarrollo es impulsado por quien quiera sumarse — voluntarios, colaboradores profesionales, instituciones aliadas, o cualquier persona con interés legítimo en que la ley costarricense sea accesible de forma confiable.

Esta apertura no es una postura retórica; es una decisión arquitectónica. Un corpus de derecho costarricense cerrado, aunque técnicamente excelente, traicionaría la naturaleza pública de lo que representa. Las licencias de Plaza — fuertes tanto en código como en datos — están elegidas precisamente para garantizar que nadie pueda privatizar lo que Plaza construye colectivamente.

Plaza no pertenece a quienes lo desarrollan. Pertenece al país.

---

## Relación con otras políticas

Este documento es el punto de entrada a la constitución del proyecto. Los demás documentos operacionalizan la visión aquí planteada:

- [`PRINCIPLES.md`](PRINCIPLES.md) — los principios no-negociables que gobiernan cada decisión y dan forma a todo lo que sigue.
- [`SCOPE.md`](SCOPE.md) — qué hace Plaza hoy, qué forma parte del norte futuro, y qué queda fuera.
- [`URI_POLICY.md`](URI_POLICY.md) — la estructura de identificadores permanentes que Plaza publica.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — cómo el mundo consume Plaza: snapshots, API, MCP, feeds.
- [`LICENSING.md`](LICENSING.md) — los términos bajo los cuales Plaza se publica, se consume y se extiende.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — cómo está estructurado Plaza internamente para cumplir estas promesas.
- [`DATA_MODEL.md`](DATA_MODEL.md) — el modelo semántico del corpus, alineado a estándares internacionales.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — los criterios de calidad que separan trabajo en progreso de contrato público.
- [`VERSIONING.md`](VERSIONING.md) — cómo evoluciona todo lo anterior sin romper los compromisos ya adquiridos.
- [`LEGAL_BASIS.md`](LEGAL_BASIS.md) — el marco jurídico costarricense específico que habilita al proyecto.
- [`REFERENCES.md`](REFERENCES.md) — glosario, estándares adoptados y bibliografía.

