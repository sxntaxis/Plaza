# Plaza - Respaldo Legal


Este documento identifica el marco jurídico costarricense específico que habilita a Plaza y al cual el proyecto se adhiere. A diferencia del resto de documentos fundacionales — que están redactados en términos de principios y conceptos jurídicos evergreen — este documento cita leyes, artículos, reglamentos y jurisprudencia concreta. Por esa razón, es el único documento fundacional que requiere revisión periódica: cuando la ley cambia, este documento se actualiza; los demás no necesitan tocarse.

El propósito es triple:

1. Servir de **referencia jurídica consultable** para abogados, colaboradores institucionales, auditores y cualquier persona que necesite verificar el respaldo legal del proyecto.
2. **Absorber la carga de especificidad legal** que los demás documentos fundacionales no cargan, preservando su carácter evergreen.
3. **Documentar con precisión** por qué cada decisión arquitectónica de Plaza tiene base jurídica en el derecho costarricense vigente.

**Última revisión:** abril de 2026. Este documento se revisa, como mínimo, una vez al año, y extraordinariamente cuando se producen reformas legislativas relevantes.

---

## Fundamento constitucional

Plaza encuentra su habilitación más profunda en dos disposiciones de la Constitución Política:

El **artículo 27** garantiza *"la libertad de petición, en forma individual o colectiva, ante cualquier funcionario público o entidad oficial, y el derecho a obtener pronta resolución."*

El **artículo 30** establece: *"Se garantiza el libre acceso a los departamentos administrativos con propósitos de información sobre asuntos de interés público. Quedan a salvo los secretos de Estado."*

La Sala Constitucional ha interpretado estos dos artículos como complementarios: el artículo 27 es el vehículo procesal, el artículo 30 es el derecho sustantivo. Ambos son exigibles por recurso de amparo. La sentencia **2021-024839** (5 de noviembre de 2021) consolidó esta distinción.

Entre la jurisprudencia estructurante cabe destacar los votos **3074-2002** (alcance del derecho de acceso como herramienta de control democrático), **4847-1999** (reconocimiento del derecho a la autodeterminación informativa), **12226-2010** (datos publicables de funcionarios públicos), **13878-2013** (obligación de anonimizar antes de publicar), **15260-2019** (salario base de funcionarios como información irrestricta), y **19110-2022** ("caso UPAD", consagrando la autodeterminación informativa como derecho autónomo).

**Consecuencia para Plaza:** el acceso estructurado a la normativa costarricense no solo es lícito — es una extensión técnica del mandato constitucional de publicidad. El proyecto no pide permiso; ejerce un derecho.

---

## Ley Marco de Acceso a la Información Pública (Ley 10554, 2024)

La **Ley 10554**, vigente desde el 1 de noviembre de 2024, saldó una deuda histórica del país al consolidar en un único instrumento las obligaciones de transparencia activa y pasiva.

Sus elementos más relevantes para Plaza:

- **Presunción de publicidad** de toda información en poder de sujetos obligados (Ejecutivo, Legislativo, Judicial, TSE, administración descentralizada, municipalidades, partidos políticos, y privados con fondos o servicios públicos).
- **Obligación de publicación proactiva en formatos abiertos e interoperables** (artículo 17). Esta obligación describe literalmente el tipo de publicación que Plaza facilita: normativa estructurada, citable, verificable, procesable por máquinas.
- **Plazo de 10 días hábiles** para responder solicitudes, prorrogable con justificación.
- **Régimen sancionatorio** para funcionarios que niegan acceso sin fundamento legal.
- **Protección jurisdiccional** mediante recurso de amparo.

El reglamento ejecutivo de la Ley 10554 estaba pendiente de publicación a la fecha de la última revisión de este documento. Plaza seguirá su emisión y se adaptará si es necesario.

**Consecuencia para Plaza:** la Ley 10554 es, en sentido fuerte, la ley que habilita la relación entre Plaza y las instituciones oficiales costarricenses. Cuando Plaza solicite datos formalmente a una institución, lo hará amparado en esta ley.

---

## Régimen de reproducción de actos oficiales (Ley 6683, artículo 75)

El artículo más importante del derecho costarricense para la operación técnica de Plaza es el **artículo 75 de la Ley 6683 de Derechos de Autor y Derechos Conexos** (14 de octubre de 1982):

> *"Se permite a todos reproducir, libremente, las constituciones, leyes, decretos, acuerdos municipales, reglamentos y demás actos públicos, bajo la obligación de conformarse estrictamente con la edición oficial. Los particulares también pueden publicar los códigos y colecciones legislativas, con notas y comentarios, y cada autor será dueño de su propio trabajo."*

La consecuencia es directa: **leyes, decretos, reglamentos, acuerdos municipales y sentencias judiciales son libremente reproducibles bajo la única carga de ajustarse al texto oficial.**

Plaza opera íntegramente dentro de este régimen. No necesita licencia CC específica para redistribuir textos normativos — el art. 75 ya los habilita. Lo que Plaza sí licencia bajo CC BY-SA 4.0 es el **corpus como obra derivada**: la estructura, las anotaciones, los vínculos, la metadata PROV-O, los identificadores canónicos, y los textos incorporados fielmente como parte del corpus estructurado.

El **artículo 63** de la misma ley matiza: el Estado y corporaciones oficiales gozan de protección de derechos patrimoniales por 25 años (o 50 si la entidad tiene por objeto ejercer esos derechos), salvo lo dispuesto en el artículo 75. Los "actos públicos" del artículo 75 no están sujetos a plazo.

**Consecuencia para Plaza:** el proyecto puede — y debe — redistribuir los textos normativos oficiales directamente como parte del corpus, con fidelidad al texto oficial y atribución de fuente, sin mendigar permiso a nadie.

### Tratados internacionales ratificados

Costa Rica integra los siguientes instrumentos que refuerzan o complementan el régimen:

- **Convenio de Berna** (Ley 6083 de 1977): el artículo 2.4 deja a los Estados miembros la potestad de proteger o no los textos oficiales; Costa Rica optó por liberarlos vía artículo 75 de la Ley 6683.
- **Acuerdos ADPIC/TRIPS** (Ley 7475).
- **Tratado OMPI sobre Derecho de Autor WCT** (Ley 7968).
- **CAFTA-DR**, capítulo 15 sobre propiedad intelectual (Ley 8622).

---

## Protección de datos personales (Ley 8968, 2011)

La **Ley 8968 de Protección de la Persona Frente al Tratamiento de sus Datos Personales** (7 de julio de 2011), su Reglamento (**Decreto Ejecutivo 37554-JP**, reformado por el 40008-JP), y la Agencia de Protección de Datos de los Habitantes (**PRODHAB**) constituyen el marco que gobierna la dimensión más sensible de cualquier proyecto de datos.

La ley distingue tres categorías de datos personales (artículo 3):

- **Datos de acceso irrestricto** (art. 3.c): los de bases públicas de acceso general, utilizables *"de conformidad con la finalidad para la cual estos datos fueron recabados"*.
- **Datos de acceso restringido** (art. 3.d): solo tratables para fines públicos o con consentimiento expreso.
- **Datos sensibles** (art. 3.e): origen racial, opiniones políticas, convicciones, salud, vida sexual, condición socioeconómica.

El artículo 9.3 excluye de la categoría "irrestricto" a ciertos datos aunque sean visibles: dirección exacta, fotografía, teléfonos privados y análogos. El **voto 15945-2019** de la Sala Constitucional extiende esta lógica a IPs, placas vehiculares y correos electrónicos.

### Cláusula de finalidad

El principio de finalidad (artículo 3.c y art. 5) es el eje jurídico más importante para cualquier tratamiento de datos en Costa Rica. La **Resolución PRODHAB 697-2023** lo aplicó en un caso muy similar al tipo de decisión que Plaza puede enfrentar: estableció que los datos de una entidad no pueden ser tomados por otra para convertirlos en parte de otra base si no se respeta la finalidad original.

**Implicación para Plaza:** si en algún contexto extraordinario resultara estrictamente necesario representar la titularidad oficial de un cargo público a partir de actos oficiales verificables, el proyecto deberá justificar explícitamente — por escrito, antes de implementar — que esa representación funcional y limitada es consistente con la finalidad original con la que los datos fueron publicados por la institución correspondiente. Este requisito está codificado en `SCOPE.md`.

### Test operativo de compatibilidad de finalidad

En Plaza, la finalidad no se evalúa solo cuando aparece una entidad humana sensible. Se evalúa cada vez que el proyecto pretende hacer algo más que reproducir fielmente un acto público normativo. La regla operativa es por clase de fuente y por tipo de transformación, no por ocurrencia aislada.

Por defecto, se presume compatible la **reproducción fiel de textos normativos oficiales**, la **estructuración de metadata normativa**, y la **representación de relaciones normativas** necesarias para trazabilidad, vigencia e interoperabilidad. No se presume compatible, en cambio, la **extracción estructurada de datos personales o incidentales**, ni la **agregación o cruce de información** que cambie materialmente el uso práctico para el cual la fuente fue publicada. Cuando la compatibilidad no sea clara, la salida por defecto no es publicar igual, sino reducir, excluir, o mantener el material fuera del corpus abierto hasta resolver la evaluación.

### Tratamiento aplicable a textos normativos

Los textos normativos oficiales **no son datos personales** en sentido propio. Sin embargo, pueden contener menciones a personas (nombres de firmantes de decretos, diputados proponentes, partes en sentencias, etc.) que sí lo son. Plaza gestiona esta tensión mediante dos mecanismos:

1. **Preservación sin extracción estructurada**: los nombres que aparecen en textos oficiales se preservan como parte del texto (es cita textual de un documento público), pero no se extraen como datos estructurados ni se convierten en entidades del grafo. Esta decisión está codificada en `SCOPE.md` y en el Principio 8 de `PRINCIPLES.md`.

2. **Criterio de incorporación con gobernanza**: cualquier extensión futura hacia la representación funcional de titularidad oficial de cargos públicos requiere gobernanza explícita proporcional a la sensibilidad de los datos, incluida justificación jurídica escrita de consistencia con la finalidad original.

La eventual representación de titularidad oficial de cargos públicos no se entiende en Plaza como perfilado de personas, sino como reconstrucción limitada de un hecho institucional verificable: qué cargo existía, quién lo ejercía oficialmente, en qué período y con base en cuál acto oficial. Su justificación, de existir, sería exclusivamente de trazabilidad institucional, responsabilidad pública y control democrático.

### Autoridad regulatoria

**PRODHAB** tiene competencia para conocer denuncias, ordenar medidas cautelares, y sancionar infracciones con hasta 30 salarios base. Desde el voto **8405-2021**, la vía de PRODHAB desplaza al amparo como procedimiento preferente en materia de protección de datos.

### Triggers operativos para Plaza

Plaza no presume que toda operación active obligaciones registrales o procedimentales ante PRODHAB, pero sí reconoce que ciertas operaciones pueden hacerlo. Cuando Plaza administre bases con datos personales o incidentales relevantes, especialmente con fines de difusión pública, debe evaluarse expresamente, según corresponda:

- la compatibilidad de finalidad;
- la necesidad de anonimización o pseudonimización irreversible;
- la adopción de protocolo de actuación;
- la eventual inscripción de la base o fichero;
- los mecanismos de rectificación, supresión y atención de reclamos.

La presencia de texto público no elimina por sí sola las obligaciones derivadas del tratamiento posterior de datos personales.

---

## Régimen penal informático (Ley 9048, 2012)

Costa Rica tipificó los delitos informáticos mediante la **Ley 9048** (10 de julio de 2012), que reformó la Sección VIII del Título VII del Código Penal, posteriormente ajustada por la **Ley 9135** (24 de abril de 2013).

Los tipos más relevantes para cualquier proyecto de datos son:

- **Artículo 196 bis** (Violación de datos personales): sanciona con prisión de 1 a 3 años a quien se apodere, acceda, copie, transmita, publique, difunda, recopile, o dé tratamiento no autorizado a datos personales. La pena se eleva a 2–4 años si los datos provienen de bases de datos públicas.
- **Artículo 229 ter** (Sabotaje informático): 3 a 6 años a quien entorpezca o inutilice información o impida el funcionamiento de un sistema. Agravado a 4–8 años en sistemas públicos.
- **Artículo 231** (Espionaje informático): 3 a 6 años a quien, mediante manipulación informática, se apodere de información de valor económico.

Costa Rica ratificó el **Convenio de Budapest sobre Ciberdelincuencia** mediante la Ley 9452 (2017).

**Consecuencia para Plaza:** el proyecto opera íntegramente dentro del espacio no tipificado. Plaza:

- No accede a sistemas sin autorización: opera sobre información publicada abiertamente por instituciones oficiales, o solicita datos mediante vías formales.
- No entorpece ni sabotea sistemas: cualquier adquisición automatizada respeta `robots.txt`, términos de uso, y aplica tasas conservadoras.
- No manipula sistemas con fin económico: el proyecto es de código abierto, sin ánimo de lucro directo.
- No evade controles técnicos: no rompe captchas, no se autentica como otro, no suplanta identidades.

La operación de Plaza es penalmente atípica. Esta postura está reflejada en los principios arquitectónicos y en la disciplina operativa del proyecto.

---

## Licencias declaradas por instituciones costarricenses

Plaza trabaja con datos publicados por instituciones del Estado costarricense bajo los siguientes regímenes específicos:

| Institución | Portal | Régimen aplicable | Observaciones |
|---|---|---|---|
| **PGR – SINALEVI/SCIJ** | pgrweb.go.cr | Art. 75 Ley 6683: reproducción libre con fidelidad al texto oficial. | Fuente primaria de normativa costarricense. |
| **Imprenta Nacional – La Gaceta** | imprentanacional.go.cr | Art. 75 Ley 6683 para los textos publicados. Términos de uso del sitio para elementos editoriales. | Diario oficial de publicación obligatoria. |
| **TSE** | tse.go.cr | CC BY-SA 4.0 Internacional (declarada). | No aplica a padrón electoral ni datos sensibles. |
| **Asamblea Legislativa** | asamblea.go.cr | Art. 75 Ley 6683 para textos de ley; términos de uso para expedientes parlamentarios. | Además de su valor como fuente legislativa primaria, puede ser relevante cuando la cuestión requiere certificación documental institucional y no solo consulta o consolidación. |
| **Poder Judicial – Nexus** | nexuspj.poder-judicial.go.cr | Reglamento Corte Plena sesión 33-2024: prohíbe construir bases paralelas con herramientas robotizadas o IA. | Requiere convenio formal para procesamiento estructurado; no forma parte del flujo ordinario publicable de Plaza. |
| **CGR** | cgr.go.cr | CC BY-SA 4.0 (declarada en portal de datos abiertos). | — |
| **Archivo Nacional** | archivonacional.go.cr | CC BY-SA (declarada). | — |

**Consecuencia para Plaza:** el alcance actual del proyecto se concentra en fuentes cuyo régimen jurídico es compatible con la apertura que Plaza exige (art. 75 Ley 6683 para normativa, CC BY-SA para datos complementarios). La incorporación de jurisprudencia del Poder Judicial requiere, necesariamente, convenio formal — esta restricción está codificada en `SCOPE.md`.

---

## Marco regulatorio de datos abiertos

Complementariamente al marco legal estricto, existe un ecosistema regulatorio y de política pública que facilita la operación de Plaza:

- **Decreto Ejecutivo 40199-MP-MEIC-MC** (Apertura de Datos Públicos, 2017): establece los principios de apertura (completos, primarios, actualizados, accesibles, procesables, no discriminatorios, con licencia libre).
- **Decreto Ejecutivo 40200-MP-MEIC-MC** (Transparencia y Acceso a la Información Pública, 2017).
- **Portal Nacional de Datos Abiertos** (datosabiertos.gob.go.cr), operado por una Comisión Nacional con participación del MICITT, MIDEPLAN, INEC, Archivo Nacional, CONARE y sociedad civil.
- **Compromisos del 5.º Plan de Acción Nacional de Estado Abierto** (Open Government Partnership, 2023–2027).

Plaza es consistente con estos instrumentos y, en esencia, los operacionaliza para el dominio específico de la normativa costarricense.

---

## Vías de acceso: formal vs. automatizado

El derecho costarricense admite cuatro vías de obtención de datos gubernamentales:

1. **Consulta a publicación proactiva**: lo que las instituciones publican por mandato legal (art. 17 Ley 10554, decretos de datos abiertos). Plaza usa esta vía primero.

2. **Solicitud formal al amparo de la Ley 10554**: cuando los datos no están publicados proactivamente. Plazo de 10 días hábiles. Deja trazabilidad jurídica completa y constituye la vía preferente para microdatos o acceso estructurado.

3. **Convenio interinstitucional**: para flujos sostenidos o datos sensibles. Es la única vía viable para jurisprudencia del Poder Judicial.

4. **Adquisición automatizada respetuosa**: reservada para datos voluminosos ya publicados abiertamente bajo régimen compatible (art. 75 Ley 6683 o licencia CC abierta), con respeto estricto a `robots.txt`, términos de uso, tasas razonables, user-agent identificable, y sin evasión de controles técnicos.

Plaza prioriza las vías en ese orden. La adquisición automatizada es complementaria, no central, y no define la identidad del proyecto.

| Tipo de fuente | Régimen principal | Vía preferente | Observación |
|---|---|---|---|
| Textos normativos oficiales | Art. 75 Ley 6683 + acceso público | Reproducción fiel / descarga / solicitud formal si hace falta | No requiere permiso para existir, pero sí fidelidad al texto oficial |
| Datos abiertos con licencia explícita | Licencia publicada por la institución | Descarga directa conforme a licencia | Verificar compatibilidad con redistribución abierta |
| Información pública no publicada proactivamente | Arts. 27 y 30 + Ley 10554 | Solicitud formal | Preferente frente a automatización masiva |
| Jurisprudencia o fuentes con restricción institucional especial | Régimen específico de la institución | Convenio o canal formal | No se trata como scrapeable por defecto |
| Fuentes con datos personales o incidentales | Ley 8968 + reglamento + finalidad | Caso por caso | Requiere evaluación de finalidad, minimización y posible anonimización |

## Roles documentales distintos dentro del ecosistema legislativo

Para efectos de Plaza, no toda fuente oficial cumple la misma función documental, aunque varias sean autoridades públicas legítimas.

En particular, conviene distinguir al menos tres roles:

- **Publicación oficial**: la publicación en el Diario Oficial La Gaceta ancla la existencia pública y la publicación oficial del texto normativo.
- **Consolidación operativa**: sistemas como SCIJ/SINALEVI son especialmente valiosos para consulta, actualización consolidada, relaciones entre normas, afectaciones, concordancias y navegación estructurada.
- **Certificación documental institucional**: cuando la cuestión jurídica exige una certificación o constancia documental formal, Plaza no presume que toda fuente oficial tenga esa competencia. Esa función debe atribuirse al órgano que efectivamente la tenga conforme al régimen institucional aplicable.

La consecuencia práctica es importante: Plaza puede apoyarse en varias fuentes oficiales al mismo tiempo, pero sin colapsar sus funciones. Un texto publicado oficialmente, un texto consolidado operativamente y un documento certificable no son necesariamente la misma cosa ni provienen del mismo órgano.

### Aplicación práctica para leyes

En el caso de las leyes, Plaza distingue entre:

- el **texto publicado oficialmente** en La Gaceta;
- el **texto consolidado** y sus relaciones normativas en SCIJ/SINALEVI;
- la eventual **certificación documental** emitida por la autoridad legislativa competente.

Plaza no usa la palabra **certificado** salvo que exista efectivamente una certificación emitida por la autoridad competente. En ausencia de esa certificación, el proyecto puede afirmar —según corresponda— que un texto fue publicado oficialmente, o que fue obtenido de una fuente oficial de consolidación, pero no que constituye por sí mismo una certificación formal.

---

## Síntesis

Plaza opera con respaldo jurídico sólido. Cada aspecto del proyecto encuentra base legal explícita en el derecho costarricense:

- **Su existencia** se ampara en los artículos 27 y 30 constitucionales y en la Ley 10554.
- **Su redistribución de textos normativos** se ampara en el artículo 75 de la Ley 6683.
- **Su disciplina de datos personales** se adhiere a la Ley 8968 y a la doctrina de PRODHAB.
- **Su licenciamiento** respeta y hereda los regímenes declarados por cada institución fuente.
- **Su operación técnica** queda íntegramente dentro del espacio no tipificado por la Ley 9048.

El espacio jurídico en el que Plaza opera no es un vacío: es un marco delimitado con zonas de riesgo identificables. Donde existe incertidumbre — típicamente en la frontera entre datos públicos y datos personales, o entre acceso permitido y redistribución abierta — Plaza aplica el criterio más garantista: codifica la duda como regla de exclusión, no como licencia de inclusión.

---

## Referencias normativas

**Constitución y leyes:**

- [Constitución Política de la República de Costa Rica](https://pgrweb.go.cr/scij/busqueda/normativa/normas/nrm_texto_completo.aspx?nValor1=1&nValor2=871)
- [Ley 6683 de Derechos de Autor y Derechos Conexos](https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?nValor1=1&nValor2=3396)
- [Ley 8968 de Protección de la Persona Frente al Tratamiento de sus Datos Personales](https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=70975)
- Ley 9048 (Delitos Informáticos) y Ley 9135 (reforma)
- Ley 9097 de Regulación del Derecho de Petición
- [Ley 10554 Marco de Acceso a la Información Pública (2024)](https://www.archivonacional.go.cr/web/normativa/ley_10554.pdf)
- Ley 6227 General de la Administración Pública
- Ley 8422 contra la Corrupción y el Enriquecimiento Ilícito
- Ley 7839 del Sistema de Estadística Nacional

**Reglamentos y decretos:**

- Decreto Ejecutivo 37554-JP (Reglamento a la Ley 8968), reformado por el 40008-JP
- Decreto Ejecutivo 40199-MP-MEIC-MC (Apertura de Datos Públicos, 2017)
- [Decreto Ejecutivo 40200-MP-MEIC-MC (Transparencia, 2017)](https://www.mcj.go.cr/sites/default/files/2023-08/Decreto%20de%20Acceso%20a%20la%20Informaci%C3%B3n%20P%C3%BAblica%2040200..pdf)
- [Reglamento para el Tratamiento de Datos Personales del Poder Judicial (Corte Plena sesión 33-2024)](https://cij.poder-judicial.go.cr/images/ProteccionDatos/REGLAMENTO_PROTECCIN_DE_DATOS-PODER_JUDICIAL.pdf)

**Jurisprudencia:**

- [Compendio de Jurisprudencia de Sala Constitucional sobre acceso a información (PGR)](https://www.pgr.go.cr/servicios/procuraduria-de-la-etica-publica-pep/temas-de-interes-pep/compendio-jurisprudencia-sala-constitucional-acceso-a-la-informacion-publica-pep/)
- [Revista de Jurisprudencia sobre Protección de Datos, Poder Judicial](https://cij.poder-judicial.go.cr/images/DocumentosInteres/Revista_Jurisprudencia_Proteccion_de_Datos.pdf)

**Tratados internacionales:**

- Convenio de Berna para la Protección de Obras Literarias y Artísticas (Ley 6083)
- Acuerdos ADPIC/TRIPS (Ley 7475)
- Tratado OMPI sobre Derecho de Autor WCT (Ley 7968)
- CAFTA-DR, capítulo 15 (Ley 8622)
- Convenio de Budapest sobre Ciberdelincuencia (Ley 9452)
- Convención Americana sobre Derechos Humanos (art. 13.1)
- Pacto Internacional de Derechos Civiles y Políticos (art. 19)

---

## Relación con otras políticas

- [`VISION.md`](VISION.md) — habla del "marco legal habilitante"; este documento lo especifica.
- [`PRINCIPLES.md`](PRINCIPLES.md) — el Principio 3 (Fuentes oficiales como autoridad) y el Principio 8 (Ética en el modelado) se fundamentan jurídicamente en este documento.
- [`SCOPE.md`](SCOPE.md) — los criterios de incorporación del alcance usan los regímenes legales descritos aquí.
- [`LICENSING.md`](LICENSING.md) — el modelo de licenciamiento dual se ampara en el art. 75 Ley 6683 para textos oficiales y en CC BY-SA 4.0 para la obra derivada.
- [`REFERENCES.md`](REFERENCES.md) — este documento es la versión jurídicamente específica de los términos legales que el glosario define en abstracto.

---

**Nota de mantenimiento:** este documento es el único fundacional que no es evergreen. Se revisa anualmente y cuando se producen reformas legislativas relevantes. Las referencias a leyes específicas con números, artículos y jurisprudencia viven exclusivamente en este documento; los demás documentos fundacionales hablan en términos conceptuales de institutos jurídicos y enlazan aquí para el respaldo concreto.
