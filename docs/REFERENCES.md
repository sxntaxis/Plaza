# Plaza — Glosario, Estándares y Referencias

Este documento es el punto de entrada para quien llega al corpus fundacional de Plaza sin familiaridad previa con los estándares y conceptos que lo sustentan. Su propósito es operativo: resolver la pregunta "¿qué significa X?" en una línea o dos, con enlace a la fuente autoritativa para quien quiera profundizar.

No pretende ser enciclopédico. Lo que está aquí es lo que aparece en los documentos fundacionales y requiere contexto para un lector no especialista. Cada entrada apunta a la especificación oficial o a la mejor referencia disponible.

---

## Glosario

### Web semántica y datos enlazados

**Grafo canónico** — el conjunto de afirmaciones estructuradas que Plaza publica como verdad oficial del proyecto, expresado como triples RDF. Es inmutable una vez publicado. Plaza lo distingue del almacén operacional interno, que sí es mutable.

**RDF (Resource Description Framework)** — modelo de datos del W3C para representar información como triples (sujeto, predicado, objeto). Es la base de la web semántica. Ver: [w3.org/RDF](https://www.w3.org/RDF/).

**Triple** — la unidad básica de información en RDF: una afirmación con tres partes (sujeto, predicado, objeto). Por ejemplo: *"Ley 7092 — fue modificada por — Ley 9635"*.

**Turtle** — formato de serialización de RDF legible por humanos. Menos verboso que RDF/XML. Es el formato preferido para mostrar ejemplos en la documentación de Plaza. Ver: [w3.org/TR/turtle](https://www.w3.org/TR/turtle/).

**JSON-LD** — formato de serialización de datos enlazados basado en JSON. Es el formato de facto para APIs web semánticas y para embedding de metadata en páginas HTML. Ver: [json-ld.org](https://json-ld.org/).

**Ontología** — descripción formal de un dominio: qué clases de cosas existen, qué propiedades tienen, y cómo se relacionan entre sí. En Plaza, la ontología define qué es una "ley", qué es una "afectación", cómo se relacionan, etc.

**OWL (Web Ontology Language)** — lenguaje del W3C para escribir ontologías. Permite expresar restricciones y relaciones más ricas que RDFS. Ver: [w3.org/OWL](https://www.w3.org/OWL/).

**Triple store** — base de datos diseñada específicamente para almacenar y consultar triples RDF. Plaza puede usarla, aunque también admite almacenar el grafo como archivos Turtle versionados.

**SPARQL** — lenguaje de consulta para grafos RDF. Análogo a SQL pero para datos enlazados. Ver: [w3.org/TR/sparql11-query](https://www.w3.org/TR/sparql11-query/).

**SHACL (Shapes Constraint Language)** — estándar W3C para definir restricciones que un grafo RDF debe cumplir. Plaza publica shapes SHACL que cualquier consumidor puede usar para validar el corpus. Ver: [w3.org/TR/shacl](https://www.w3.org/TR/shacl/).

**FRBR (Functional Requirements for Bibliographic Records)** — modelo conceptual de la IFLA que distingue cuatro niveles en cualquier obra: Work (obra intelectual), Expression (realización específica), Manifestation (forma física), Item (copia individual). ELI adopta los tres primeros. Ver: [IFLA FRBR Report](https://repository.ifla.org/handle/123456789/811).

**Content negotiation** — mecanismo del protocolo HTTP por el cual cliente y servidor acuerdan el formato de respuesta mediante el header `Accept`. Plaza lo usa: la misma URI devuelve HTML, JSON-LD, Turtle o Akoma Ntoso XML según el header enviado.

**Akoma Ntoso** — estándar XML para representar documentos legales estructurados. En Plaza se usa como serialización documental derivada, no como identidad canónica ni como ontología primaria del grafo RDF.

**ELI-first** — decisión de modelado por la cual ELI gobierna identidad, metadata legal, FRBR, versiones y relaciones normativas del grafo canónico.

### Términos jurídicos costarricenses

**SCIJ (Sistema Costarricense de Información Jurídica)** — el sistema oficial operado por la Procuraduría General de la República que expone la legislación costarricense consolidada. Accesible vía web en pgrweb.go.cr/scij.

**SINALEVI** — el módulo de legislación de SCIJ, operado por la PGR. Contiene leyes, decretos, reglamentos, directrices y demás normativa costarricense desde 1821.

**La Gaceta** — el Diario Oficial de Costa Rica, publicado por la Imprenta Nacional. Publicación constitucional donde toda norma debe aparecer para adquirir vigencia. Ver: [imprentanacional.go.cr](https://www.imprentanacional.go.cr/).

**Alcance de La Gaceta** — edición adicional de La Gaceta publicada cuando el volumen diario lo requiere. Una norma puede publicarse en la edición regular o en un alcance específico.

**Ficha** — en SCIJ, la página de metadata estructurada de una norma (emisor, fecha, estado, publicación, versión vigente, etc.). Distinta de la página de texto completo.

**Afectación** — relación jurídica por la cual una norma altera a otra: deroga, reforma, suspende, interpreta auténticamente, etc. SCIJ las registra estructuralmente.

**Concordancia** — vínculo temático entre normas identificado por el personal editorial de SCIJ, sin implicar necesariamente una modificación legal.

**Reglamentación** — relación entre una ley y el reglamento que la desarrolla o implementa.

**Descriptor** — etiqueta temática controlada que SCIJ asigna a normas y artículos para permitir navegación por materia.

**Pronunciamiento de la PGR** — dictamen u opinión jurídica emitida por la Procuraduría General en ejercicio de su función consultiva. Tienen valor interpretativo pero no crean normativa.

**Transitorio** — disposición de vigencia temporal anexa a una norma, típicamente usada para regular el período de transición entre el régimen anterior y el nuevo. En derecho costarricense tiene régimen distinto a un artículo permanente.

**Ente emisor** — órgano del Estado que emite una norma (Asamblea Legislativa, Poder Ejecutivo, Poder Judicial, TSE, etc.).

### Licenciamiento y código abierto

**Copyleft** — familia de licencias de software libre que exigen que las obras derivadas se publiquen bajo la misma licencia. Opuesto a las licencias permisivas (MIT, BSD, Apache) que permiten que las derivaciones sean privativas.

**AGPL-3.0 (GNU Affero General Public License v3.0)** — licencia copyleft fuerte que cierra explícitamente el "SaaS loophole": quien opera software AGPL como servicio accesible por red debe proveer el código fuente modificado a los usuarios del servicio. Ver: [gnu.org/licenses/agpl-3.0](https://www.gnu.org/licenses/agpl-3.0.html).

**SaaS loophole** — hueco en licencias copyleft tradicionales (GPL clásica): correr software modificado como servicio no cuenta técnicamente como "distribución", por lo que no disparaba la obligación de compartir el código. AGPL cierra este hueco.

**CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0)** — licencia para obras no-software (datos, documentación, contenido) que exige atribución y que las obras derivadas se publiquen bajo la misma licencia. Ver: [creativecommons.org/licenses/by-sa/4.0](https://creativecommons.org/licenses/by-sa/4.0/).

**CC BY 4.0 (Creative Commons Attribution 4.0)** — licencia permisiva de Creative Commons que solo exige atribución. Menos restrictiva que BY-SA. Compatible con BY-SA en la dirección de incorporación (BY-SA puede absorber material BY). Ver: [creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0/).

**CLA (Contributor License Agreement)** — acuerdo mediante el cual quien contribuye código a un proyecto otorga al proyecto los derechos necesarios para relicenciarlo bajo otras licencias. Indispensable para proyectos con modelo de licenciamiento dual.

**DCO (Developer Certificate of Origin)** — alternativa ligera al CLA: una declaración que el contribuyente firma en cada commit (`Signed-off-by:`) afirmando que tiene derecho a contribuir el código. Menos robusto que un CLA pero más práctico para contribuciones pequeñas.

### Protocolos y superficies de acceso

**MCP (Model Context Protocol)** — protocolo estandarizado para que sistemas de inteligencia artificial accedan a fuentes de datos y herramientas externas con retrieval verificable. Ver: [modelcontextprotocol.io](https://modelcontextprotocol.io/).

**DCAT (Data Catalog Vocabulary)** — vocabulario del W3C para describir catálogos de datasets y servicios de datos en la web. Permite federación entre portales de datos abiertos. Ver: [w3.org/TR/vocab-dcat-3](https://www.w3.org/TR/vocab-dcat-3/).

**Feed Atom** — formato XML estandarizado para publicar listas de actualizaciones (IETF RFC 4287). Plaza lo usa para notificar cambios en el corpus siguiendo el Pilar 4 de ELI.

### Instituciones costarricenses mencionadas

**PGR (Procuraduría General de la República)** — órgano superior consultivo técnico-jurídico del Estado. Opera SCIJ-SINALEVI. No ejerce representación judicial del Estado (eso le corresponde a otros órganos).

**CGR (Contraloría General de la República)** — órgano constitucional auxiliar de la Asamblea Legislativa en el control de la hacienda pública. Su rol es fiscalizador, no legislativo.

**TSE (Tribunal Supremo de Elecciones)** — cuarto poder del Estado costarricense, con rango constitucional. Rector de la materia electoral y registral.

**Imprenta Nacional** — institución adscrita al Ministerio de Gobernación y Policía. Responsable de publicar La Gaceta y el Boletín Judicial.

**Asamblea Legislativa** — órgano legislativo unicameral de Costa Rica. 57 diputados. Fuente primaria de leyes y decretos legislativos.

**Poder Judicial / CEIJ (Centro Electrónico de Información Jurisprudencial)** — órgano del Poder Judicial responsable de sistematizar y publicar la jurisprudencia. Opera Nexus-PJ.

**Sala Constitucional** — sala especializada de la Corte Suprema de Justicia encargada del control de constitucionalidad.

---

## Estándares adoptados

Plaza se alinea con los siguientes estándares internacionales. Cada uno cumple un rol específico en el modelo de datos o en la infraestructura del proyecto.

| Estándar | Publicador | Versión | Rol en Plaza | Especificación |
|---|---|---|---|---|
| **ELI** (European Legislation Identifier) | Oficina de Publicaciones de la UE | Ontología v1.3 | Estructura de URIs de legislación; metadata bibliográfica FRBR | [data.europa.eu/eli/ontology](https://data.europa.eu/eli/ontology) |
| **Akoma Ntoso** | OASIS LegalDocML TC | v1.0 | Serialización XML documental de textos legales estructurados | [docs.oasis-open.org/legaldocml/akn-core/v1.0](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/) |
| **schema.org/Legislation** | schema.org community | actual | Interoperabilidad con motores de búsqueda y herramientas web generales | [schema.org/Legislation](https://schema.org/Legislation) |
| **PROV-O** | W3C | Recommendation 2013 | Ontología de procedencia: quién afirmó qué, cuándo, basado en qué | [w3.org/TR/prov-o](https://www.w3.org/TR/prov-o/) |
| **SKOS** | W3C | Recommendation 2009 | Vocabularios controlados (tipos de norma, emisores, estados) | [w3.org/TR/skos-reference](https://www.w3.org/TR/skos-reference/) |
| **DCAT** | W3C | v3 (2024) | Catalogación de datasets y servicios de datos | [w3.org/TR/vocab-dcat-3](https://www.w3.org/TR/vocab-dcat-3/) |
| **W3C ORG** | W3C | Recommendation 2014 | Reservado para capa institucional futura (organizaciones, cargos) | [w3.org/TR/vocab-org](https://www.w3.org/TR/vocab-org/) |
| **SHACL** | W3C | Recommendation 2017 | Validación formal del grafo contra el modelo | [w3.org/TR/shacl](https://www.w3.org/TR/shacl/) |
| **FRBR** | IFLA | Informe 1998 (act. 2009) | Modelo conceptual bibliográfico; base teórica de ELI | [repository.ifla.org](https://repository.ifla.org/handle/123456789/811) |
| **Dublin Core Terms** | DCMI | actual | Metadata bibliográfica genérica | [dublincore.org/specifications](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) |
| **ISO 3166-1** | ISO | actual | Códigos de país (`cr` para Costa Rica en URIs) | [iso.org/iso-3166](https://www.iso.org/iso-3166-country-codes.html) |
| **ISO 639** | ISO | actual | Códigos de idioma (`spa` para español) | [iso.org/iso-639](https://www.iso.org/iso-639-language-code) |
| **ISO 8601** | ISO | actual | Formato de fechas y tiempos (`2023-01-15`) | [iso.org/iso-8601](https://www.iso.org/iso-8601-date-and-time-format.html) |
| **SemVer 2.0.0** | Tom Preston-Werner | 2.0.0 | Versionado semántico de ontología, modelo y shapes | [semver.org](https://semver.org/) |
| **RFC 6570** | IETF | 2012 | URI Templates (base formal del patrón ELI) | [rfc-editor.org/rfc/rfc6570](https://www.rfc-editor.org/rfc/rfc6570) |
| **RFC 4287** | IETF | 2005 | Formato Atom para feeds de actualizaciones | [rfc-editor.org/rfc/rfc4287](https://www.rfc-editor.org/rfc/rfc4287) |

---

## Lecturas recomendadas

Bibliografía curada para quien quiera profundizar. No es exhaustiva — es el mínimo suficiente para tener contexto serio sobre cada área.

### Sobre ELI y datos jurídicos abiertos

1. **Publications Office of the EU (2024).** *ELI Implementation Guide: Technical Aspects.* Tercera edición. Guía técnica oficial para implementar ELI. El punto de partida obligatorio para cualquier implementación. [eur-lex.europa.eu/eli-register/implementing_eli.html](https://eur-lex.europa.eu/eli-register/implementing_eli.html)

2. **Hoekstra, R. et al. (2021).** "The linked legal data landscape: linking legal data across different countries." *Artificial Intelligence and Law.* Análisis comparativo de implementaciones ELI en distintas jurisdicciones; útil para entender cómo adaptar el estándar a un contexto nacional específico. [link.springer.com/article/10.1007/s10506-021-09282-8](https://link.springer.com/article/10.1007/s10506-021-09282-8)

3. **Agencia Estatal Boletín Oficial del Estado (España).** *Proyecto ELI en el BOE.* Ejemplo más cercano lingüística y jurídicamente a Costa Rica de una implementación ELI operativa. [boe.es/legislacion/eli.php](https://www.boe.es/legislacion/eli.php)

### Sobre web semántica y datos enlazados

4. **Heath, T. & Bizer, C. (2011).** *Linked Data: Evolving the Web into a Global Data Space.* Morgan & Claypool. Introducción canónica a los principios de linked data. Gratuita en línea. [linkeddatabook.com](http://linkeddatabook.com/editions/1.0/)

5. **W3C (2013).** *Data on the Web Best Practices.* Recomendación sobre buenas prácticas para publicar datos en la web. Fundamento del modelo de publicación de Plaza. [w3.org/TR/dwbp](https://www.w3.org/TR/dwbp/)

### Sobre Akoma Ntoso

6. **Palmirani, M. & Vitali, F. (2011).** "Akoma-Ntoso for Legal Documents." *Legislative XML for the Semantic Web.* Capítulo fundacional del estándar escrito por sus creadores. Contexto teórico sobre modelado XML de textos legales.

7. **OASIS (2018).** *Akoma Ntoso Version 1.0 Part 1: XML Vocabulary.* Especificación oficial. [docs.oasis-open.org/legaldocml/akn-core/v1.0](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/)

### Sobre licenciamiento de software libre

8. **Free Software Foundation (2007).** *GNU Affero General Public License v3.0.* Texto de la licencia. Incluye preámbulo explicativo fundamental. [gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)

9. **Open Source Initiative.** *Frequently Answered Questions — Licenses.* Guía práctica sobre interoperabilidad entre licencias, CLA, y modelos duales. [opensource.org/faq](https://opensource.org/faq)

### Sobre derecho costarricense y acceso a la información pública

10. **Ley 8968 de Protección de la Persona Frente al Tratamiento de sus Datos Personales.** Costa Rica. Marco legal base para el tratamiento de datos en el país. Relevante especialmente para Principio 8 (Ética en el modelado) y el scope sobre modelado de personas.

11. **Constitución Política de Costa Rica, art. 27 y 30.** Derecho de petición y acceso a la información administrativa. Fundamento constitucional de la premisa de Plaza: la información jurídica es pública.

12. **Sala Constitucional, Voto 3074-2002.** Sentencia sobre el derecho de acceso a la información pública. Interpretación autoritativa del art. 30 constitucional.

### Sobre gobierno abierto y datos gubernamentales

13. **OECD (2018).** *Open Government Data Report: Enhancing Policy Maturity for Sustainable Impact.* Panorama comparativo de políticas de datos abiertos. Costa Rica incluida. [oecd.org/gov/digital-government](https://www.oecd.org/gov/digital-government/)

### Sobre knowledge graphs aplicados a gobierno

14. **Hogan, A. et al. (2021).** "Knowledge Graphs." *ACM Computing Surveys.* Panorama técnico comprensivo y accesible del estado del arte en knowledge graphs. Útil para contextualizar la dirección de largo plazo de Plaza. [dl.acm.org/doi/10.1145/3447772](https://dl.acm.org/doi/10.1145/3447772)

---

## Cómo usar este documento

Cuando un término técnico aparezca en los documentos fundacionales y no sea inmediatamente claro, buscar aquí primero. Si no está, es una omisión — vale reportarla para que se agregue.

Cuando alguien del ecosistema FAIR, de la PGR, o cualquier colaborador institucional pida "¿dónde puedo aprender más sobre X?", apuntar a la sección correspondiente. Las lecturas recomendadas están elegidas para dar contexto serio sin abrumar.

Este documento evoluciona con el corpus fundacional. Cuando un nuevo concepto técnico entra al proyecto, su definición entra aquí. Cuando un estándar se adopta o se actualiza, la tabla se actualiza.

---

## Relación con otras políticas

- [`VISION.md`](VISION.md) — la visión que los estándares listados aquí permiten concretar
- [`LEGAL_BASIS.md`](LEGAL_BASIS.md) — el marco jurídico costarricense específico que habilita al proyecto.
- [`PRINCIPLES.md`](PRINCIPLES.md) — especialmente el Principio 6 (Estándares internacionales como columna), del cual este documento es evidencia operativa.
- [`SCOPE.md`](SCOPE.md) — define qué subset del ecosistema de estándares aplica al alcance actual.
- [`URI_POLICY.md`](URI_POLICY.md) — usa ELI como patrón base de identificadores.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — describe cómo MCP, DCAT y feed Atom se exponen como superficies.
- [`LICENSING.md`](LICENSING.md) — operacionaliza las licencias aquí descritas (AGPL-3.0, CC BY-SA 4.0).
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — usa PROV-O como columna de procedencia.
- [`DATA_MODEL.md`](DATA_MODEL.md) — especifica cómo se combinan ELI, schema.org/Legislation, PROV-O, SKOS y las extensiones costarricenses.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — usa SHACL para validación formal.
- [`VERSIONING.md`](VERSIONING.md) — usa SemVer para la ontología, modelo y shapes.
