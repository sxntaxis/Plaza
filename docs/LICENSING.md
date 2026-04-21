# Plaza — Licenciamiento

Este documento define los términos bajo los cuales Plaza se publica, se consume, y se extiende. Es la implementación operativa del Principio 9 (Apertura por arquitectura) y del Principio 3 (Fuentes oficiales como autoridad).

El licenciamiento de Plaza no es una decisión administrativa reversible — es una decisión arquitectónica que protege al proyecto de dos fallas opuestas: la captura privada silenciosa (que una empresa tome Plaza, lo cierre, y cobre acceso a algo construido colectivamente), y el debilitamiento por sobreuso comercial sin retribución (que el esfuerzo de mantener el proyecto dependa únicamente del voluntariado mientras terceros lucran).

El modelo elegido resuelve ambas fallas. Lo que sigue lo explica con precisión.

---

## Modelo dual en una página

Plaza se publica bajo un **modelo de licenciamiento dual**:

- **Código**: [GNU Affero General Public License v3.0 (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html)
- **Datos**: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

Cualquier persona o entidad — individuo, empresa, institución, organización — puede usar, modificar, redistribuir, y construir sobre Plaza bajo estos términos, gratuitamente y a perpetuidad. A cambio, debe publicar sus modificaciones y servicios derivados bajo las mismas licencias.

Para quienes necesitan integrar Plaza en productos cerrados o servicios comerciales sin cumplir con las obligaciones de copyleft, existe una **vía comercial paralela**: una licencia comercial negociada que levanta las obligaciones de compartir modificaciones. Esa vía no otorga acceso privilegiado a los datos — solo el permiso de no abrir el código derivado.

Todas las contribuciones al proyecto requieren firma de un **Contributor License Agreement (CLA)** que otorga al proyecto los derechos necesarios para sostener la vía comercial, sin comprometer la apertura del código principal.

---

## Licencia de código: AGPL-3.0

### Qué cubre

Todo el código fuente del proyecto Plaza — pipelines de ingesta, modelos de datos, lógica de reconciliación, servidores API y MCP, herramientas operativas, scripts, y cualquier otro artefacto ejecutable o compilable — se distribuye bajo AGPL-3.0.

### Por qué AGPL y no otra licencia

AGPL fue elegida específicamente por una propiedad que licencias más permisivas (MIT, Apache, BSD) no tienen, y que incluso GPL clásica no tiene completamente: cierra la **cláusula de SaaS (Software as a Service)**. 

Bajo licencias permisivas, una empresa puede tomar Plaza, modificarlo, correrlo como servicio hospedado (sin distribuir el binario), y nunca publicar sus cambios. El código se mantiene privado porque técnicamente no hubo "distribución." AGPL elimina ese hueco: si alguien opera Plaza como servicio accesible por red a terceros, está obligado a proveer el código fuente completo — incluidas modificaciones — a esos terceros.

Para un proyecto cuya misión es ser infraestructura cívica abierta, y cuyo consumidor primario son sistemas de IA que frecuentemente se exponen como servicios, esta propiedad es esencial. Sin AGPL, Plaza podría terminar siendo el motor silencioso de productos cerrados que cobran por funcionalidades construidas sobre trabajo comunitario.

### Qué implica para quien usa Plaza

Usar Plaza internamente — ejecutarlo en una computadora, procesar datos con él, integrarlo en flujos privados que no exponen el código como servicio — no requiere ninguna obligación activa. Se puede usar libremente.

Distribuir Plaza — modificado o no — requiere distribuir también el código fuente correspondiente, bajo la misma licencia AGPL.

Operar una versión modificada de Plaza como servicio accesible a terceros (API pública, producto SaaS, cualquier forma en que el software interactúe con usuarios remotos a través de una red) requiere que esos usuarios tengan acceso al código fuente modificado, también bajo AGPL.

### Qué implica para quien contribuye a Plaza

Las contribuciones al repositorio principal de Plaza se aceptan bajo los términos del CLA (ver sección correspondiente). La AGPL aplica al código resultante.

---

## Licencia de datos: CC BY-SA 4.0

### Qué cubre

El **corpus estructurado** publicado por Plaza se distribuye bajo CC BY-SA 4.0. Esto incluye los snapshots en todos sus formatos (RDF, JSON-LD, Akoma Ntoso XML, SQLite), la estructura del grafo, los vocabularios controlados propios del proyecto, las anotaciones interpretativas, la metadata de procedencia, los identificadores canónicos, y los textos normativos incorporados fielmente al corpus como parte integrante del mismo.

### Base jurídica para la redistribución de textos oficiales

Los textos normativos oficiales costarricenses — constituciones, leyes, decretos, reglamentos, acuerdos municipales, sentencias judiciales — son de libre reproducción bajo el régimen costarricense de reproducción de actos oficiales, con la única carga de ajustarse estrictamente a la edición oficial. Plaza opera íntegramente dentro de este régimen: redistribuye los textos con fidelidad y con atribución explícita a las fuentes oficiales (SCIJ/PGR, La Gaceta/Imprenta Nacional, Poder Judicial, etc.), pero no requiere — ni ha requerido nunca — licencia específica de esas instituciones para incorporarlos al corpus.

La licencia CC BY-SA 4.0 se aplica al corpus como **obra derivada estructurada**: la organización, la estructura, las relaciones, los identificadores canónicos, las anotaciones, y el conjunto de los textos incorporados como unidad citable. Un consumidor que descargue un snapshot de Plaza recibe, bajo los términos de CC BY-SA 4.0, tanto el aparato estructural como los textos normativos organizados dentro de él.

Para el respaldo jurídico completo de esta base, incluyendo los artículos específicos del ordenamiento costarricense que la sustentan, ver [`LEGAL_BASIS.md`](LEGAL_BASIS.md).

### Por qué CC BY-SA y no CC BY

CC BY permite usar, modificar y redistribuir con solo atribuir al autor. No exige que las obras derivadas se publiquen bajo la misma licencia. Bajo CC BY, alguien podría tomar el corpus de Plaza, combinarlo con datos privados, y publicar el resultado cerrado.

CC BY-SA (ShareAlike) exige que las obras derivadas se publiquen bajo la misma licencia. Esto significa que cualquier dataset que incorpore sustantivamente el corpus de Plaza queda también abierto bajo CC BY-SA 4.0.

Esta es la propiedad equivalente a la de AGPL para código: cierra el hueco que permite privatización silenciosa.

### Qué implica para quien usa los datos

Consultar, analizar, o citar el corpus — en una tesis, en un artículo, en un reporte, en una aplicación interna — requiere únicamente atribución a Plaza como fuente, con enlace al proyecto.

Redistribuir el corpus, modificado o no, requiere mantener la atribución y publicar el resultado bajo CC BY-SA 4.0.

Combinar el corpus de Plaza con otros datos en un producto derivado sustantivo requiere publicar ese producto bajo CC BY-SA 4.0.

Construir aplicaciones, dashboards, interfaces, o análisis **sobre** el corpus sin redistribuirlo — por ejemplo, consumiendo la API REST o MCP para mostrar resultados en una interfaz propia — no requiere aplicar CC BY-SA a la aplicación en sí. La aplicación puede tener su propia licencia. Lo que se comparte bajo CC BY-SA son los datos, no las aplicaciones que los consultan.

### Compatibilidad con fuentes oficiales

Las fuentes oficiales costarricenses de las que Plaza se alimenta operan bajo regímenes jurídicos compatibles con la apertura que Plaza exige: los textos normativos bajo el régimen de libre reproducción de actos oficiales, y los datos complementarios bajo licencias abiertas explícitamente declaradas por cada institución (típicamente CC BY 4.0 o CC BY-SA 4.0). CC BY-SA 4.0 es compatible con CC BY 4.0 en la dirección de absorción (material CC BY puede incorporarse a obras CC BY-SA), por lo que el modelo de Plaza honra a sus fuentes sin imponer obligaciones incompatibles. Para el detalle del régimen aplicable a cada institución fuente, ver [`LEGAL_BASIS.md`](LEGAL_BASIS.md).

---

## Vía comercial paralela

### Propósito

El licenciamiento copyleft protege la apertura, pero también impone obligaciones que pueden ser incompatibles con ciertos modelos de negocio legítimos. Una empresa que quiere integrar Plaza en un producto con código propietario no puede hacerlo bajo AGPL. Una plataforma que quiere distribuir un derivado del corpus como parte de un producto cerrado no puede hacerlo bajo CC BY-SA.

En lugar de forzar a esos consumidores a construir sus propias alternativas desde cero — duplicando trabajo y fragmentando el ecosistema — Plaza ofrece una vía comercial paralela: una licencia negociada que levanta las obligaciones de copyleft a cambio de una contribución económica al sostenimiento del proyecto.

### Qué otorga

Una licencia comercial de Plaza otorga a su titular el derecho de usar, modificar y distribuir el código y/o los datos de Plaza sin las obligaciones de publicar modificaciones bajo AGPL o CC BY-SA. El titular puede integrar Plaza en productos cerrados, ofrecerlo como parte de servicios comerciales, y distribuir derivados bajo los términos que considere.

### Qué no otorga

Una licencia comercial **nunca** otorga:

- Acceso a datos que no sean públicos en la versión abierta de Plaza. Si algo está en la versión comercial, está también en la versión abierta. Lo comercial es el permiso de no compartir el resultado derivado, no el acceso privilegiado al insumo.
- Exclusividad. Plaza no ofrece licencias comerciales exclusivas. Cualquier licenciatario comercial puede coexistir con otros licenciatarios comerciales y con el ecosistema abierto.
- Derecho a influir sobre la dirección del proyecto. El proyecto abierto es el proyecto; los licenciatarios comerciales son consumidores, no gobernantes.
- Derecho a restringir la versión abierta. La versión AGPL + CC BY-SA sigue siendo la versión canónica y siempre está disponible gratuitamente.

### Cómo se estructura

La estructura operativa de la vía comercial — quién la administra, qué se cobra, cómo se usan los fondos, qué procesos se siguen — se define en un documento operativo separado cuando haya capacidad institucional para ofrecerla. Hasta entonces, el modelo comercial existe como compromiso en esta política pero no como oferta activa.

Los fondos generados por licenciamiento comercial se destinan exclusivamente al sostenimiento del proyecto abierto: infraestructura, compensación de mantenedores, auditorías de calidad, y fondos de resistencia ante posibles disputas legales. Nunca se distribuyen como dividendos.

---

## Contributor License Agreement (CLA)

### Por qué es necesario

El modelo dual solo funciona si el proyecto tiene el derecho de relicenciar el código cuando negocia licencias comerciales. Sin CLA, cada contribución queda bajo los términos bajo los cuales fue hecha (AGPL), y el proyecto no puede ofrecer esa contribución bajo otra licencia — ni siquiera para una vía comercial paralela. El CLA resuelve esto otorgando al proyecto los derechos necesarios, sin que el contribuyente pierda su propio derecho de autor.

### Qué otorga

Al firmar el CLA, cada contribuyente:

1. **Retiene su derecho de autor** sobre el código contribuido. Plaza no le quita la autoría.
2. **Otorga al proyecto una licencia amplia, perpetua, no-exclusiva, y mundial** para usar, modificar, sublicenciar, y distribuir el código contribuido bajo cualquier licencia que el proyecto considere apropiada — incluyendo AGPL, licencias comerciales, o futuras licencias compatibles con la misión del proyecto.
3. **Declara que tiene el derecho de hacer esa contribución**: que el código es suyo, que no infringe derechos de terceros, y que su empleador no tiene un reclamo sobre él (o que el contribuyente tiene permiso explícito del empleador, cuando aplique).

El contribuyente puede, en paralelo, liberar su propio código bajo cualquier otra licencia que desee. El CLA no es exclusivo.

### Proceso

El proceso específico de firma (formulario, sistema de tracking, verificación) se define en un documento operativo separado. Hasta que el proceso esté establecido, Plaza no acepta contribuciones de código externo al equipo inicial — prefiere rechazar ayuda a aceptarla bajo términos ambiguos que invaliden el modelo más tarde.

Las contribuciones pequeñas (correcciones tipográficas, documentación menor) pueden aceptarse bajo un Developer Certificate of Origin (DCO) simplificado, sin CLA completo. La línea entre "contribución menor" y "contribución que requiere CLA" se documenta operativamente.

---

## Dependencias y fuentes externas

### Dependencias de código

Plaza usa bibliotecas y componentes de terceros. Cada dependencia debe tener una licencia compatible con AGPL-3.0 para su inclusión en el proyecto. Las dependencias bajo MIT, BSD, Apache 2.0, LGPL, GPL-compatible, y similares son generalmente aceptables.

No se aceptan dependencias bajo licencias incompatibles con AGPL (ciertos tipos de licencias propietarias, algunas licencias copyleft incompatibles). Cuando se detecta una incompatibilidad, la dependencia se reemplaza o se evita.

El inventario de dependencias con sus licencias se mantiene en un documento operativo separado (típicamente generado automáticamente y verificado en CI).

### Fuentes de datos

Plaza solo incorpora datos de fuentes que permiten redistribución bajo términos compatibles con CC BY-SA 4.0. Las fuentes oficiales costarricenses ya identificadas (PGR, Imprenta Nacional, TSE) cumplen este criterio.

Si en el futuro se considera incorporar una fuente con términos menos compatibles (por ejemplo, CC BY-NC que prohíbe uso comercial, o licencias propietarias), el proyecto analiza caso por caso si esa fuente puede ser representada bajo un régimen diferenciado (por ejemplo, solo como referencia sin redistribución) o si se excluye. La apertura de Plaza es prioritaria sobre la completitud del corpus.

---

## Garantías y limitaciones

### Sin garantía

Plaza se distribuye tal como está, sin garantía de ningún tipo — ni explícita ni implícita. AGPL y CC BY-SA establecen esto formalmente. En la práctica significa que:

- Plaza puede contener errores, imprecisiones, o representaciones incorrectas del derecho costarricense.
- Plaza puede quedar desactualizado respecto a la normativa vigente.
- Plaza puede fallar operacionalmente.

Los usuarios consumen Plaza bajo su propia responsabilidad. Para decisiones jurídicas que requieren certeza absoluta, la fuente autoritativa sigue siendo el SCIJ oficial, La Gaceta, y las instituciones correspondientes. Plaza es una representación, no un sustituto de la consulta oficial.

### Sin responsabilidad

Los mantenedores del proyecto no son responsables por daños directos, indirectos, consecuentes, o incidentales derivados del uso del código o los datos de Plaza. Esta limitación aplica tanto a usuarios gratuitos como a licenciatarios comerciales, modulada en el segundo caso por los términos específicos del acuerdo comercial.

---

## Cambios futuros al modelo

### Qué puede cambiar

La implementación operativa del modelo puede evolucionar: cómo se administra la vía comercial, qué proceso se usa para CLA, cómo se gestionan los fondos, qué entidad jurídica respalda el proyecto.

### Qué no puede cambiar

Los pilares del modelo son irreversibles:

- **Código bajo copyleft fuerte (AGPL-3.0 o licencia estrictamente equivalente en efecto).** Nunca se relaja a permisiva.
- **Datos bajo share-alike (CC BY-SA 4.0 o licencia estrictamente equivalente).** Nunca se relaja a CC BY sin SA.
- **No hay acceso privilegiado a datos.** Lo comercial es el permiso de no abrir el derivado, nunca acceso exclusivo al insumo.
- **Versión abierta siempre disponible.** La versión AGPL + CC BY-SA es la versión canónica y no se retira.

Un cambio que viole cualquiera de estos pilares no es una evolución del modelo — es un proyecto distinto. El Principio 9 lo prohíbe explícitamente, y este documento lo ratifica.

### Proceso de modificación

Cambios al modelo que no violen los pilares anteriores requieren:

1. Discusión pública en el repositorio del proyecto.
2. Actualización de este documento con referencia a la discusión.
3. Período razonable de notificación a consumidores y contribuyentes antes de que el cambio tome efecto.

Cambios que violen los pilares no requieren proceso porque no son permitidos.

---

## Relación con otras políticas

Este documento se lee junto con:

- [`PRINCIPLES.md`](PRINCIPLES.md) — especialmente Principio 9, del cual este documento es implementación operativa.
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — define las superficies sobre las cuales aplica la licencia de datos.
- [`SCOPE.md`](SCOPE.md) — establece qué forma parte del corpus cubierto.
- [`VERSIONING.md`](VERSIONING.md) — define cómo se versionan los snapshots publicados bajo esta licencia.
- [`LEGAL_BASIS.md`](LEGAL_BASIS.md) — el respaldo jurídico concreto del régimen de reproducción de textos oficiales y de la compatibilidad con licencias de instituciones fuente.
- [`REFERENCES.md`](REFERENCES.md) — glosario y bibliografía para los términos jurídicos y de licenciamiento usados en este documento.
