# Marco jurídico costarricense para la extracción y redistribución de datos gubernamentales

Este documento sistematiza el derecho costarricense aplicable a la extracción automatizada (web scraping), procesamiento y redistribución de datos publicados por instituciones del Estado. Su tesis central es directa: en Costa Rica **scrapear no es per se ilegal, pero tampoco es legalmente neutro**. El marco constitucional favorece el acceso a la información pública; la legislación penal informática, la Ley 8968 de protección de datos y las licencias institucionales imponen, sin embargo, restricciones muy concretas. Un enfoque estructurado — basado en solicitudes formales al amparo de la **Ley 10554 (2024)**, convenios interinstitucionales y respeto a las licencias publicadas — resulta jurídicamente más sólido, reproducible y sostenible que la extracción automatizada indiscriminada. El documento está pensado como referencia técnico-jurídica para investigadores académicos, desarrolladores, periodistas de datos y organizaciones de transparencia.

---

## 1. Fundamento constitucional del acceso a la información pública

La Constitución Política costarricense articula el acceso a datos gubernamentales sobre dos pilares complementarios. El **artículo 27** dispone: *"Se garantiza la libertad de petición, en forma individual o colectiva, ante cualquier funcionario público o entidad oficial, y el derecho a obtener pronta resolución"*. El **artículo 30** añade: *"Se garantiza el libre acceso a los departamentos administrativos con propósitos de información sobre asuntos de interés público. Quedan a salvo los secretos de Estado"*.

La Sala Constitucional, en sentencia **2021-024839** del 5 de noviembre de 2021, clarificó la distinción operativa: el artículo 27 es el vehículo procesal para dirigirse a la Administración, mientras que el artículo 30 regula el derecho sustantivo de acceder a información de interés público. Ambos son exigibles por recurso de amparo bajo los artículos 29 y 48 de la Constitución y la Ley de la Jurisdicción Constitucional 7135.

### Jurisprudencia estructurante de la Sala Constitucional

El desarrollo jurisprudencial ha sido intenso y mayoritariamente garantista. Destacan:

| Voto | Año | Doctrina relevante |
|---|---|---|
| **3074-2002** | 2002 | Consolidó el alcance amplio del derecho de acceso a información administrativa como herramienta de control democrático y transparencia. |
| **4847-1999** | 1999 | Primer voto que reconoce la **autodeterminación informativa** como derecho fundamental derivado del artículo 24 constitucional. |
| **12226-2010** | 2010 | Define qué datos de funcionarios públicos son legítimamente publicables en Internet (nombre, cédula profesional, datos de trabajo) y cuáles no (residencia, correos privados). |
| **13878-2013** | 2013 | La existencia de datos sensibles no autoriza denegar información pública; obliga a **anonimizar antes de publicar**. |
| **6787-2015** | 2015 | Aspirantes a la Presidencia se someten a un umbral superior de transparencia. |
| **15260-2019** | 2019 | El salario base de funcionarios públicos es información irrestricta; el **desglose individualizado** no. |
| **19110-2022** | 2022 | Caso **UPAD**: consagra la autodeterminación informativa como derecho autónomo y fija requisitos estrictos para limitarlo. |
| **2025-17051** | 2025 | Declara inconstitucional la restricción al acceso a la lista de morosos tributarios, reafirmando la primacía de la transparencia fiscal. |

La Procuraduría General de la República mantiene un compendio oficial de esta jurisprudencia en su Procuraduría de la Ética Pública.

### Ley Marco de Acceso a la Información Pública: Ley 10554 (2024)

El **1 de noviembre de 2024** entró en vigor la **Ley 10554**, hito normativo que salda una deuda histórica del país. Sus elementos centrales son: presunción de publicidad de toda información en poder de sujetos obligados (Ejecutivo, Legislativo, Judicial, TSE, administración descentralizada, municipalidades, partidos políticos y privados con fondos o servicios públicos); **plazo de respuesta de 10 días hábiles**, prorrogable con justificación; obligación de publicación proactiva en **formatos abiertos e interoperables**; régimen sancionatorio para funcionarios que nieguen información (amonestaciones orales hasta suspensiones sin goce de sueldo); y protección jurisdiccional mediante amparo. La ley debía ser reglamentada en 6 meses; a abril de 2026 el reglamento ejecutivo aún no había sido publicado.

### Recomendaciones prácticas

Antes de extraer datos masivamente, verifique si la institución los publica proactivamente en cumplimiento del artículo 17 de la Ley 10554. Cuando no los publique o los publique parcialmente, formule una solicitud por escrito invocando los artículos 27 y 30 constitucionales y la Ley 10554: es más rápido que litigar y genera **trazabilidad jurídica** del origen de los datos. Si la institución omite responder o responde con ambigüedad, proceda con recurso de amparo ante la Sala Constitucional, cuya tasa de acogida fue de 459 amparos con lugar en 2024 según datos publicados por *La Nación*.

---

## 2. Protección de datos personales: Ley 8968 y rol de PRODHAB

La **Ley 8968 del 7 de julio de 2011** (publicada en La Gaceta N° 170 del 5 de septiembre de 2011) y su Reglamento (**Decreto Ejecutivo 37554-JP**, reformado por el 40008-JP de 2016) constituyen el núcleo del régimen. El artículo 1 es de orden público y tutela el derecho a la **autodeterminación informativa**. El artículo 2 se aplica a "toda modalidad de uso posterior" de datos personales — fórmula decisiva para el scraping, porque captura el tratamiento secundario tras la obtención inicial.

### Categorías de datos y sus regímenes

El artículo 3 distingue tres categorías con tratamientos radicalmente distintos:

- **Datos de acceso irrestricto** (art. 3.c): los de bases públicas de acceso general, utilizables "de conformidad con la finalidad para la cual estos datos fueron recabados". La cláusula de finalidad es el principio más subestimado en la práctica del scraping gubernamental.
- **Datos de acceso restringido** (art. 3.d): solo tratables para fines públicos o con consentimiento expreso.
- **Datos sensibles** (art. 3.e): origen racial, opiniones políticas, convicciones, salud, vida sexual, condición socioeconómica; su tratamiento por personas privadas es **falta gravísima** (art. 31.a).

El artículo 9.3 excluye explícitamente de la categoría "irrestricto" a ciertos datos aunque estén visibles: dirección exacta, fotografía, teléfonos privados y análogos. El **voto 15945-2019** de la Sala Constitucional extiende esta lógica: direcciones IP, placas vehiculares y correos electrónicos **no son de uso libre por el mero hecho de estar a la vista**.

### Consentimiento, finalidad y excepciones

El artículo 5 exige consentimiento expreso y escrito, con tres excepciones relevantes para scraping: orden judicial fundamentada, datos obtenidos de fuentes públicas generales, y entrega por disposición constitucional o legal. El artículo 6 fija que los datos deben conservarse máximo **10 años** desde los hechos, salvo disposición especial — fundamento legal del derecho al olvido costarricense. El artículo 14 somete toda **transferencia** a consentimiento expreso, lo que implica que redistribuir datos scrapeados requiere base de legitimación específica.

### Bases de datos y PRODHAB

El artículo 21 obliga a inscribir en PRODHAB toda base administrada con **fines de distribución, difusión o comercialización**. La omisión es falta gravísima (art. 31.e), sancionable con 15 a 30 salarios base y suspensión del fichero por 1 a 6 meses. La **PRODHAB** fue creada como órgano de desconcentración máxima del Ministerio de Justicia y Paz; desde 2013 funciona como procedimiento especializado de protección, desplazando la vía de amparo conforme el **voto 8405-2021**.

Un precedente directamente aplicable es la **Resolución PRODHAB 697-2023** (28 de agosto de 2023): ordenó al BCCR suspender la solicitud a SUGEF de datos crediticios sin anonimizar. La Agencia estableció que **los datos del Sistema Financiero Nacional no pueden ser tomados por otra entidad para convertirlos en parte de otra base si no se respeta la finalidad original**. Esta doctrina aplica análogamente a cualquier scraping-redistribución que cambie la finalidad con la que los datos fueron recabados.

### Datos mezclados: el caso típico del scraping

Sentencias judiciales con nombres de partes, edictos, notificaciones, padrones electorales, resoluciones administrativas con identificadores personales — todos mezclan información pública con datos personales. El **voto 13878-2013** y el **voto 2215-2021** establecen una obligación operativa clara: **anonimizar antes de publicar en Internet**. El Poder Judicial la formalizó en la **Circular 193-2014** y posteriormente en el **Reglamento para el Tratamiento de Datos Personales del Poder Judicial (sesión 33-2024 de Corte Plena)**, que sustituye nombres por "[Nombre 001]", "[Nombre 002]" en el sistema Nexus.

### Recomendaciones prácticas

Antes de redistribuir cualquier conjunto de datos, clasifique cada campo según las tres categorías de la Ley 8968. Si aparecen datos sensibles, **elimínelos**. Si aparecen datos personales incidentales (cédula, teléfono, correo, dirección), **anonimícelos** con técnicas de k-anonimización o pseudonimización irreversible antes de persistir el conjunto. Si su base será distribuida o difundida, **inscríbala ante PRODHAB** y adopte un protocolo de actuación inscrito (art. 12, presunción iuris tantum de cumplimiento). Respete los derechos de acceso, rectificación y supresión del titular en 5 días hábiles (art. 7).

---

## 3. Propiedad intelectual sobre obras del Estado

La **Ley 6683 de Derechos de Autor y Derechos Conexos** (14 de octubre de 1982, con reformas hasta la Ley 9858 de 2020) regula los derechos sobre obras intelectuales. Su artículo **75** es la piedra angular para el trabajo con información jurídica oficial:

> *"Se permite a todos reproducir, libremente, las constituciones, leyes, decretos, acuerdos municipales, reglamentos y demás actos públicos, bajo la obligación de conformarse estrictamente con la edición oficial. Los particulares también pueden publicar los códigos y colecciones legislativas, con notas y comentarios, y cada autor será dueño de su propio trabajo."*

La consecuencia es directa: **leyes, decretos, reglamentos, acuerdos municipales y sentencias judiciales** son libremente reproducibles bajo la única carga de ajustarse al texto oficial. Esto constituye el fundamento normativo costarricense más favorable al trabajo con datos jurídicos públicos.

El artículo 63 matiza el régimen general: *"El Estado, los consejos municipales y las corporaciones oficiales gozarán de la protección de esta ley, pero, en cuanto a los derechos patrimoniales, los tendrán únicamente por veinticinco años, contados desde la publicación de la obra, salvo tratándose de entidades públicas que tengan por objeto el ejercicio de esos derechos como actividad ordinaria, en cuyo caso la protección será de cincuenta años"*. Es decir: las obras del Estado distintas de los "actos públicos" del artículo 75 **sí gozan de protección patrimonial**, pero limitada.

El artículo 7 permite usar libremente obras en dominio público sin suprimir el nombre del autor conocido ni hacer interpolaciones sin distinción editorial — principio importante al redistribuir textos oficiales adaptados.

### Tratados internacionales integrados al bloque de legalidad

Costa Rica ratificó el **Convenio de Berna** (aprobado por Ley 6083 de 1977), cuyo artículo 2.4 deja a los Estados miembros la potestad de proteger o no los textos oficiales de naturaleza legislativa, administrativa o judicial; el ordenamiento costarricense optó por liberarlos vía artículo 75 de la Ley 6683. Igualmente vinculantes son los **Acuerdos ADPIC/TRIPS** (Ley 7475), el **Tratado OMPI sobre Derecho de Autor WCT** (Ley 7968), y el capítulo 15 del **CAFTA-DR** (Ley 8622), que endureció observancia mediante la Ley 8039 y sus reformas.

### Licencias declaradas por instituciones costarricenses

La práctica institucional es heterogénea. La tabla siguiente resume el panorama con base en la consulta directa a cada portal:

| Institución | Portal | Licencia declarada | Observaciones |
|---|---|---|---|
| **PGR / SCIJ – SINALEVI** | pgrweb.go.cr | Por artículo 75 Ley 6683, textos legales de dominio público reproducible libremente. No hay licencia CC explícita en el portal SCIJ. | Uso referencial sujeto a fidelidad con la edición oficial. |
| **Imprenta Nacional / La Gaceta** | imprentanacional.go.cr | Términos de uso del sitio; los textos publicados (leyes, decretos) operan bajo art. 75 Ley 6683. | El Boletín Judicial fue trasladado al Poder Judicial en 2023. |
| **TSE** | tse.go.cr | **CC BY-SA 4.0 Internacional** (declarada explícitamente en tse.go.cr/cdr.html) | La licencia expresamente no contempla datos sensibles ni el padrón electoral. |
| **INEC** | inec.cr / datosabiertos.inec.cr | CC BY típicamente, bajo política del Sistema Estadístico Nacional (Ley 7839). | Microdatos sujetos a acceso restringido y confidencialidad estadística. |
| **BCCR** | bccr.fi.cr | Datos públicos con API abierta; términos de uso del portal. | Restricciones sobre imágenes de moneda nacional. |
| **CGR** | cgr.go.cr | **CC BY-SA 4.0** explícita en su portal de datos abiertos. | Incluye SIPP y datos de funcionarios públicos (índice salarial). |
| **Archivo Nacional** | archivonacional.go.cr | **CC BY-SA** explícita. | Patrimonio documental histórico. |
| **Poder Judicial / Nexus** | nexuspj.poder-judicial.go.cr | **Reglamento Corte Plena sesión 33-2024** prohíbe expresamente construir bases paralelas con herramientas robotizadas o IA. | Uso estrictamente consultivo; la anonimización es obligatoria. |
| **IMN** | imn.ac.cr | Términos restrictivos, propiedad intelectual reservada; autorización escrita requerida para logo y datos históricos. | Datos preliminares liberados con exención de responsabilidad. |
| **Registro Nacional** | rnpdigital.com | Consultas individuales con registro; sin API masiva pública. | El uso automatizado masivo viola términos. |
| **Ministerio de Hacienda** | hacienda.go.cr | Datos abiertos bajo licencia abierta; secreto tributario (Ley 4755) limita datos de contribuyentes. | Precedente 2025-17051: acceso a lista de morosos es constitucionalmente exigible. |

### Política Nacional de Datos Abiertos

El ecosistema de datos abiertos descansa en dos decretos ejecutivos de 2017: el **Decreto 40199-MP-MEIC-MC** (Apertura de Datos Públicos, define los datos como completos, primarios, actualizados, accesibles, procesables, no discriminatorios y **con licencia libre de uso y reuso**) y el **Decreto 40200-MP-MEIC-MC** (Transparencia y Acceso a la Información Pública). El portal nacional es **datosabiertos.gob.go.cr**, operado por una Comisión Nacional de Datos Abiertos con participación del MICITT, MIDEPLAN, INEC, Archivo Nacional, CONARE y sociedad civil (Abriendo Datos, Sulabtasú).

### Recomendaciones prácticas

Para obras jurídicas oficiales (leyes, decretos, reglamentos, sentencias), el artículo 75 de la Ley 6683 autoriza la reproducción libre con fidelidad al texto oficial — no se requiere licencia CC, aunque citarla facilita trazabilidad. Al redistribuir datos de instituciones con licencia CC BY-SA (CGR, TSE, Archivo Nacional), **herede la licencia** en la obra derivada. Mantenga atribución visible: fuente institucional, URL original, fecha de extracción, versión. Para Poder Judicial, limite el uso a consulta; para redistribuir jurisprudencia, solicite convenio formal.

---

## 4. Legalidad del web scraping bajo el derecho penal costarricense

Costa Rica **no cuenta con un tipo penal autónomo de "acceso no autorizado a sistemas informáticos"**, a diferencia de lo que prevé el Convenio de Budapest (ratificado por Ley 9452 de 2017) y de lo que proponía el Proyecto de Ley 21.187 (2018), aún no aprobado. Cualquier imputación al scraping debe subsumirse en los tipos específicos de la Sección VIII del Título VII del Código Penal, reformada por la **Ley 9048** del 10 de julio de 2012 y modificada por la **Ley 9135** del 24 de abril de 2013.

### Tipos penales aplicables al scraping

El **artículo 196 bis** (Violación de datos personales) es el tipo más peligroso para el scraping masivo. Sanciona con prisión de 1 a 3 años a quien, en beneficio propio o de un tercero, con peligro o daño para la intimidad y sin autorización del titular, "se apodere, modifique, interfiera, **acceda, copie, transmita, publique, difunda, recopile**, inutilice, intercepte, retenga, venda, compre, **desvíe para un fin distinto para el que fueron recolectados** o dé un tratamiento no autorizado" a datos personales. La pena se eleva a 2–4 años si los datos están en **bases de datos públicas** (inciso b) — agravante directamente aplicable al scraping gubernamental. Los verbos rectores describen casi literalmente la actividad del scraping.

El **artículo 231** (Espionaje informático) impone prisión de 3 a 6 años a quien "sin autorización del titular o responsable, valiéndose de cualquier manipulación informática o tecnológica, se apodere, transmita, copie, modifique, destruya, utilice, bloquee o recicle **información de valor para el tráfico económico de la industria y el comercio**". Es el tipo más aplicable al scraping con fines competitivos sobre datos de valor económico, aun si están publicados abiertamente.

El **artículo 229 bis** (Daño informático) y el **229 ter** (Sabotaje informático) son relevantes cuando el scraping degrada el servicio. El 229 ter penaliza con 3 a 6 años a quien "destruya, altere, **entorpezca o inutilice** la información contenida en una base de datos, o bien, impida, altere, obstaculice o modifique sin autorización el funcionamiento de un sistema". La agravante del inciso c) (sistemas públicos) eleva la pena a 4–8 años. Un scraping con tasa excesiva que sature servidores gubernamentales y **entorpezca el acceso lícito de usuarios autorizados** puede encuadrar aquí.

El **artículo 217 bis** (Estafa informática) requiere manipulación del procesamiento con beneficio patrimonial; raramente aplicable al scraping pasivo. El **artículo 230** (Suplantación de identidad) aplica si se suplanta marca comercial o entidad jurídica en medios electrónicos. El **artículo 232** (Programas maliciosos) no cubre crawlers comunes, pero sí servicios agresivos que generen denegación de servicio.

### Robots.txt, términos de uso y captchas

Aunque el archivo **robots.txt no tiene fuerza legal autónoma** en Costa Rica (no es ley ni contrato formalizado), opera como **indicador probatorio relevante** del consentimiento del titular del sitio. Un `Disallow: /` constituye manifestación unilateral de voluntad que, ignorada conocidamente, refuerza el **dolo** y el elemento "sin autorización" de los tipos del Código Penal. Los términos de uso (ToS) vinculan cuando hay aceptación expresa (clickwrap); sin aceptación, su valor probatorio es más débil pero igualmente considerable. La **evasión de captchas, rate-limiting, tokens o autenticación** es, en cambio, un fuerte indicio de dolo y configura el elemento "manipulación informática o tecnológica" del artículo 231.

La distinción práctica fundamental es: **acceder a datos publicados abiertamente ≠ evadir controles técnicos**. El primer escenario es penalmente atípico por regla general; el segundo se acerca a los tipos del 231 y 196 bis.

### Laguna jurisprudencial

Tras búsquedas en Nexus del Poder Judicial, boletines de la Sala Constitucional y prensa costarricense, **no se ha identificado jurisprudencia publicada que resuelva expresamente un caso de scraping**. Los casos reseñados en delitos informáticos se concentran en phishing bancario, suplantación en redes sociales y ataques ransomware (Conti contra CCSS y Hacienda, 2022). Esta laguna obliga al operador jurídico a razonar por analogía con la dogmática aplicable, con cuidado respecto al principio de legalidad penal (art. 39 constitucional).

### Responsabilidad civil

Más allá del régimen penal, el **artículo 1045 del Código Civil** fundamenta responsabilidad extracontractual por dolo, falta, negligencia o imprudencia que cause daño. Una institución pública tiene legitimación activa para reclamar: costos de infraestructura adicional, lucro cesante por indisponibilidad de servicios, y daños por redistribución de datos erróneos. La Ley General de la Administración Pública (Ley 6227) complementa el fundamento. La redistribución de datos con errores puede además configurar injurias (art. 145 CP), calumnia (art. 147 CP) o difamación (art. 146 CP) si se atribuyen hechos falsos deshonrosos, y genera sanciones administrativas de PRODHAB bajo la Ley 8968.

### Recomendaciones prácticas

Si decide scrapear, documente ausencia de dolo: respete `robots.txt` y ToS, configure rate limiting conservador, use un User-Agent identificable, no evada ningún control técnico. Al redistribuir, publique **disclaimers** sobre fuente, fecha, exactitud y mecanismo de rectificación. Consulte un seguro de responsabilidad civil profesional si el proyecto tiene escala. Reconozca que los disclaimers reducen pero no eliminan la exposición bajo el artículo 1045 CC.

---

## 5. Acceso formal, Ley 9097 y Defensoría de los Habitantes

La **Ley 9097 de Regulación del Derecho de Petición** (2013) operativiza el artículo 27 constitucional. Establece formalidades mínimas y plazo de respuesta de **10 días hábiles** para peticiones simples (posteriormente retomado por la Ley 10554 para solicitudes de acceso a información). Si la solicitud requiere procesamiento y análisis —no mera entrega de información preexistente—, opera el régimen del artículo 30 constitucional y el procedimiento administrativo ordinario de la Ley General de la Administración Pública (Ley 6227).

La **Defensoría de los Habitantes** (Ley 7319) puede mediar cuando una institución niega información pública; sus recomendaciones no son vinculantes, pero generan presión reputacional significativa y documentan la denegatoria para efectos de un eventual amparo. Costa Rica Íntegra opera el **Sistema de Orientación Virtual sobre Acceso a la Información (SOVAI)** con cartas modelo y asesoría para solicitudes y recursos.

### Convenios interinstitucionales: la vía preferente

Para proyectos académicos y organizaciones con volumen significativo de datos, los **convenios interinstitucionales** resuelven simultáneamente tres problemas: legitimación jurídica, acceso a microdatos no publicados, y sostenibilidad del flujo. El precedente más citado es el convenio **INEC – Centro Centroamericano de Población (UCR)** vigente desde 2002, que permite cruces avanzados de censos con garantías de confidencialidad estadística. Convenios análogos existen con el Archivo Nacional y la PGR para universidades públicas.

### Recomendaciones prácticas

Prefiera la solicitud formal ante cualquier dato específico, estructurado, de alto valor y no publicado proactivamente. El costo marginal de una solicitud por la Ley 10554 es bajo; el beneficio probatorio y jurídico es alto. Para proyectos recurrentes o que requieran microdatos, **negocie un convenio** — implica más tiempo inicial pero genera capacidad sostenida. Reserve el scraping para datos voluminosos ya publicados bajo licencia abierta.

---

## 6. Tipos de datos gubernamentales y su tratamiento diferenciado

No todos los datos gubernamentales merecen el mismo trato. La tabla siguiente sintetiza los regímenes por tipo:

| Tipo de dato | Institución rectora | Régimen jurídico dominante | Vía recomendada |
|---|---|---|---|
| Legislación (leyes, decretos, reglamentos) | PGR (SINALEVI/SCIJ), Imprenta Nacional, Asamblea Legislativa | Art. 75 Ley 6683: reproducción libre con fidelidad al texto oficial | Descarga directa o scraping respetuoso |
| Jurisprudencia judicial | Poder Judicial (Nexus), Sala Constitucional | Reglamento Corte Plena 33-2024: **prohibido construir bases paralelas** con herramientas robotizadas | Consulta web; convenio formal para base derivada |
| Dictámenes PGR y Contraloría | PGR, CGR | Publicación proactiva bajo régimen de transparencia | Descarga directa |
| Datos estadísticos | INEC (Ley 7839), ministerios | Confidencialidad estadística; datos agregados bajo CC BY | Portal de datos abiertos o solicitud formal para microdatos |
| Datos presupuestarios y ejecución | Hacienda, CGR (SIPP) | CC BY-SA 4.0 (CGR); transparencia presupuestaria | Descarga o API |
| Datos tributarios | Hacienda (Tributación) | Secreto tributario Ley 4755; voto 2025-17051 libera lista de morosos | API para consultas puntuales; restricciones para datos individuales |
| Datos ambientales y meteorológicos | MINAE, SINAC, IMN | Principio de máxima divulgación; IMN con términos restrictivos para datos históricos | Solicitud formal al IMN; consulta directa para datos operativos |
| Datos geoespaciales | Registro Inmobiliario, SNIT, IGN | Variable; muchos bajo WMS/WFS abiertos | Servicios OGC cuando estén disponibles |
| Registros de propiedad y personas jurídicas | Registro Nacional | Consulta individual registrada; **sin API masiva** | Consultas atomizadas; certificaciones pagadas |
| Padrón electoral y registro civil | TSE | CC BY-SA 4.0 para portal; padrón bajo finalidad electoral | Uso estricto para la finalidad declarada |
| Datos de funcionarios públicos | Cada institución, CGR | Salario base es público (voto 15260-2019); DJB confidenciales (art. 24 Ley 8422) | Índice Salarial CGR es fuente preferente |
| Datos de ciudadanos privados | Variable | Régimen pleno Ley 8968; consentimiento y finalidad | Evitar salvo base legal expresa |
| Patrimonio documental histórico | Archivo Nacional | CC BY-SA | Descarga directa |

La distinción entre **datos de funcionarios públicos** (sujetos a transparencia reforzada por la jurisprudencia de la Sala Constitucional) y **datos de ciudadanos privados** (plenamente protegidos por la Ley 8968) es estructuralmente central. El funcionario en ejercicio de función pública cede intimidad en proporción al interés público de su cargo; el ciudadano privado mantiene la plenitud de su autodeterminación informativa aunque aparezca en registros públicos por actos procesales o registrales.

### Recomendaciones prácticas

Construya un **inventario clasificatorio** antes de iniciar cualquier proyecto: para cada fuente, anote institución, tipo de dato, régimen jurídico, licencia, vía de acceso y restricciones. Privilegie fuentes con licencia abierta explícita (CC BY, CC BY-SA). Para datos jurídicos, la ruta preferida es **SCIJ/SINALEVI + La Gaceta** por el amparo del artículo 75 de la Ley 6683. Para jurisprudencia voluminosa, el convenio con el Poder Judicial es obligado dada la restricción reglamentaria.

---

## 7. Buenas prácticas integradas

Cuando el scraping sea la vía necesaria, adopte una disciplina que reduzca exposición jurídica y facilite trazabilidad. Los elementos mínimos son:

- Revisar **robots.txt** antes de cualquier extracción y respetar sus directivas, incluido `Crawl-delay`.
- Leer los términos de uso del portal y documentar la fecha de consulta en los metadatos del conjunto extraído.
- Configurar delays razonables (2-5 segundos por petición), uso de caching local y backoff exponencial ante códigos 429/503.
- Identificar el user-agent con nombre de proyecto y correo de contacto.
- Registrar para cada dato: timestamp, URL exacta, hash, licencia aplicable y versión del scraper.
- Anonimizar inmediatamente los datos personales incidentales; **no persistir** el dato crudo si basta el agregado estadístico.
- Heredar licencia y mantener atribución visible en la obra derivada.
- Publicar política de privacidad propia y mecanismo de rectificación si la base se expondrá públicamente.

Para proyectos con volumen, complemente con: protocolo de actuación inscrito ante PRODHAB (art. 12 Ley 8968, activa presunción de cumplimiento), inscripción de la base si tiene fines de difusión (art. 21), seguros de responsabilidad civil profesional, y asesoría legal previa al despliegue.

---

## 8. Contexto institucional y casos relevantes

Costa Rica vive una transformación digital articulada en dos estrategias sucesivas conducidas por el MICITT: la **Estrategia de Transformación Digital hacia el Bicentenario 4.0 (2018–2022)** y la **Estrategia de Transformación Digital 2023–2027** (agosto de 2023). El país es miembro de **Open Government Partnership desde 2012**; su 5.º Plan de Acción Nacional de Estado Abierto (2023–2027) es inédito por incluir los tres poderes más el TSE. **Hacienda Digital** (TRIBU-CR, ATENA, CR-TEZA), iniciada en 2020 con el Banco Mundial, cristaliza la modernización tributaria, aduanera y financiera; el ransomware Conti de abril de 2022 aceleró su urgencia.

En el frente de acceso a información, los amparos ante la Sala Constitucional con lugar por negativa de acceso pasaron de **49 en 2020 a 459 en 2024**, una escalada que refleja tanto mayor conocimiento ciudadano del derecho como mayor resistencia administrativa bajo la administración Chaves (2022–2026). Casos emblemáticos incluyen el caso BCR-El Financiero (2016–2017, Excel con claves), la sentencia 20355-2018 sobre datos geológicos, el amparo de Radios UCR contra el Ministerio de Salud (2020) por datos de COVID-19, y el caso MEP 2024-2025 sobre información del sistema educativo.

El ecosistema civil cuenta con organizaciones activas: **Abriendo Datos Costa Rica**, **Costa Rica Íntegra** (capítulo de Transparencia Internacional, operador del SOVAI), **Fundación Acceso**, **Sulabtasú**, **ACCESA**, **Red Ciudadana por Costa Rica Abierta**, y **PROLEDI (UCR)** e **IPLEX** — motores de la aprobación de la Ley 10554. En periodismo de datos destacan **Punto y Aparte**, **La Nación Data**, **Semanario Universidad**, **Delfino.cr** y **CRHoy**.

El **Reglamento de Corte Plena sesión 33-2024 del Poder Judicial** es la mejor ilustración de la tensión no resuelta entre protección de datos y acceso a jurisprudencia: **prohíbe expresamente la construcción de bases paralelas mediante herramientas robotizadas o IA**. El reglamento es coherente con la protección de titulares de datos en expedientes, pero contrasta con la jurisprudencia garantista de la Sala Constitucional. Para trabajar con jurisprudencia sistemáticamente, el convenio con el Poder Judicial es hoy la única vía jurídicamente sólida.

---

## 9. Conclusión: por qué el enfoque estructurado es el correcto

El marco costarricense dibuja un espacio legalmente delimitado, no un vacío. **Scrapear no es ilegal en sí mismo**, pero opera bajo la sombra de tres regímenes concurrentes: la Ley 8968 (finalidad, consentimiento, inscripción, sanciones), el Código Penal reformado por la Ley 9048 (196 bis, 229 ter, 231), y las licencias específicas de cada institución (desde CC BY-SA 4.0 del TSE y CGR hasta la prohibición expresa del Reglamento Corte Plena 33-2024). La ausencia de jurisprudencia específica sobre scraping no reduce el riesgo: lo hace menos predecible.

El **enfoque estructurado** — solicitudes formales al amparo de la Ley 10554, convenios interinstitucionales, respeto a licencias publicadas y anonimización disciplinada — ofrece cuatro ventajas decisivas sobre el scraping masivo. Primero, **certeza jurídica**: la base del dato queda documentada y oponible. Segundo, **calidad**: los microdatos entregados por convenio suelen ser más ricos y limpios que los raspados de HTML público. Tercero, **sostenibilidad**: un flujo institucional es renovable, escalable y no depende de la estabilidad del portal. Cuarto, **legitimidad**: proyectos con base en convenio soportan mejor el escrutinio de PRODHAB, la Sala Constitucional y la opinión pública.

La Ley 10554, el artículo 75 de la Ley 6683 y la infraestructura de datos abiertos del Estado constituyen, en conjunto, herramientas suficientes para casi todo proyecto legítimo de investigación, periodismo o datos abiertos en Costa Rica. El scraping debe reservarse para lo que realmente exige esa vía — datos voluminosos ya publicados bajo licencia abierta, con respeto estricto a `robots.txt`, términos y tasa — y nunca sustituir el diálogo institucional que el derecho costarricense espera y protege.

---

## Referencias normativas y fuentes institucionales

**Constitución y leyes:**
- Constitución Política de la República de Costa Rica (arts. 24, 27, 30, 41, 48): https://pgrweb.go.cr/scij/busqueda/normativa/normas/nrm_texto_completo.aspx?nValor1=1&nValor2=871
- Ley 6683 de Derechos de Autor y Derechos Conexos: https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?nValor1=1&nValor2=3396
- Ley 8968 de Protección de la Persona Frente al Tratamiento de sus Datos Personales: https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=70975
- Ley 9048 (Delitos Informáticos) y Ley 9135 (reforma): https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?nValor1=1&nValor2=73583
- Ley 9097 de Regulación del Derecho de Petición
- Ley 10554 Marco de Acceso a la Información Pública (2024): https://www.archivonacional.go.cr/web/normativa/ley_10554.pdf
- Ley 6227 General de la Administración Pública
- Ley 8422 contra la Corrupción y el Enriquecimiento Ilícito
- Ley 7839 del Sistema de Estadística Nacional

**Reglamentos y decretos:**
- Decreto Ejecutivo 37554-JP (Reglamento a la Ley 8968), reformado por el 40008-JP
- Decreto Ejecutivo 40199-MP-MEIC-MC (Apertura de Datos Públicos, 2017)
- Decreto Ejecutivo 40200-MP-MEIC-MC (Transparencia, 2017): https://www.mcj.go.cr/sites/default/files/2023-08/Decreto%20de%20Acceso%20a%20la%20Informaci%C3%B3n%20P%C3%BAblica%2040200..pdf
- Reglamento para el Tratamiento de Datos Personales del Poder Judicial (Corte Plena sesión 33-2024): https://cij.poder-judicial.go.cr/images/ProteccionDatos/REGLAMENTO_PROTECCIN_DE_DATOS-PODER_JUDICIAL.pdf

**Jurisprudencia:**
- Compendio de Jurisprudencia de Sala Constitucional sobre acceso a información (PGR): https://www.pgr.go.cr/servicios/procuraduria-de-la-etica-publica-pep/temas-de-interes-pep/compendio-jurisprudencia-sala-constitucional-acceso-a-la-informacion-publica-pep/
- Revista de Jurisprudencia sobre Protección de Datos, CIJ Poder Judicial: https://cij.poder-judicial.go.cr/images/DocumentosInteres/Revista_Jurisprudencia_Proteccion_de_Datos.pdf
- Nexus Poder Judicial: https://nexuspj.poder-judicial.go.cr/

**Instituciones y portales:**
- PRODHAB: https://www.prodhab.go.cr/ (resoluciones: https://www.prodhab.go.cr/resoluciones/)
- MICITT: https://www.micitt.go.cr/ (Estrategia 2023-2027)
- Portal Nacional de Datos Abiertos: https://datosabiertos.gob.go.cr/
- SINALEVI/SCIJ: https://www.pgr.go.cr/servicios/sinalevi/ y https://pgrweb.go.cr/scij/
- Imprenta Nacional: https://www.imprentanacional.go.cr/
- Contraloría General de la República: https://www.cgr.go.cr/
- INEC: https://inec.cr/ y datos abiertos: https://datosabiertos.inec.cr/
- BCCR: https://www.bccr.fi.cr/
- Ministerio de Hacienda: https://www.hacienda.go.cr/
- TSE: https://www.tse.go.cr/ (licencia CC BY-SA 4.0: https://www.tse.go.cr/cdr.html)
- Archivo Nacional: https://www.archivonacional.go.cr/
- IMN: https://www.imn.ac.cr/terminos
- Registro Nacional: https://www.rnpdigital.com/
- Defensoría de los Habitantes: https://www.dhr.go.cr/
- Costa Rica Íntegra – SOVAI: https://costaricaintegra.org/sovai/
- Open Government Partnership Costa Rica: https://www.opengovpartnership.org/members/costa-rica/

**Tratados internacionales ratificados:**
- Convenio de Berna para la Protección de Obras Literarias y Artísticas (Ley 6083)
- Acuerdos ADPIC/TRIPS (Ley 7475)
- Tratado OMPI sobre Derecho de Autor WCT (Ley 7968)
- CAFTA-DR, capítulo 15 (Ley 8622)
- Convenio de Budapest sobre Ciberdelincuencia (Ley 9452 de 2017)
- Convención Americana sobre Derechos Humanos (art. 13.1)
- Pacto Internacional de Derechos Civiles y Políticos (art. 19)

---

*Documento de referencia técnico-jurídica. No constituye asesoría legal para casos concretos. Para proyectos con volumen o exposición específica, se recomienda consulta profesional con abogado especializado en derecho informático y protección de datos en Costa Rica.*