# Plaza — Principios

Este documento establece los principios que gobiernan cada decisión técnica, estratégica y de diseño en Plaza. Cuando dos caminos se presentan y no está claro cuál elegir, este documento es el árbitro. Cuando una nueva propuesta entra en conflicto con alguno de estos principios, la propuesta cede — no el principio.

Los principios no son aspiraciones. Son restricciones. Cada uno está redactado para ser aplicable a una decisión concreta y detectable cuando se incumple.


---

## 1. Evidencia antes que inferencia

Plaza publica solo lo que puede respaldar con una fuente oficial identificable. Cuando una afirmación se deriva de inferencia y no de lectura directa de una fuente, se marca como inferida. Cuando hay incertidumbre, se declara. Cuando hay conflicto entre fuentes, se registra sin resolver silenciosamente.

Esto significa que Plaza prefiere decir "no lo sé" a adivinar, y prefiere publicar un corpus más pequeño pero verdadero a uno más grande pero especulativo. La ausencia explícita es información; la ausencia disfrazada de certeza es traición al usuario.

**Cuándo se rompe:** cuando se completan campos faltantes con heurísticas y no se marcan como inferidos.

---

## 2. Identidad permanente

Los identificadores que Plaza publica son contratos. No cambian. Una URI emitida hoy seguirá resolviendo al mismo recurso en diez años, aunque el backend cambie, aunque el equipo cambie, aunque el formato de serialización evolucione.

Esto impone disciplina en el momento de diseñar los identificadores — deben ser pensados como contratos públicos de duración indefinida — y restringe los cambios futuros al terreno de lo interno. Las representaciones pueden evolucionar; las identidades no.

**Cuándo se rompe:** cuando se cambia el esquema de URIs para "hacerlo más limpio" después de haberlo publicado.

---

## 3. Fuentes oficiales como autoridad

Las instituciones del Estado costarricense — la Procuraduría General, la Imprenta Nacional, el Poder Judicial, la Asamblea Legislativa — son las autoridades de los datos que Plaza representa. Plaza no las sustituye ni compite con ellas. Plaza es una representación estructurada de lo que ellas publican, construida con respeto por su autoridad institucional.

Cuando Plaza y una fuente oficial discrepan, la fuente oficial gana — Plaza se corrige. Toda afirmación en Plaza referencia explícitamente la fuente de la cual proviene.

**Cuándo se rompe:** cuando se presenta Plaza como fuente de verdad independiente en lugar de como representación de fuentes oficiales.

---

## 4. Procedencia explícita y completa

Cada afirmación que Plaza publica es trazable hasta su origen: la fuente oficial, la URL específica consultada, la fecha de captura, el artefacto preservado, la versión del proceso que produjo la interpretación.

Esto permite que cualquier usuario — abogado, investigador, sistema de IA, auditor institucional — verifique no solo qué dice Plaza, sino por qué. Permite también que, cuando el procesamiento mejora, las afirmaciones anteriores puedan reevaluarse sin perder historia.

**Cuándo se rompe:** cuando se guarda solo el dato procesado y se descarta el artefacto fuente.

---

## 5. Precisión temporal de primera clase

Todo lo que cambia en el tiempo en Plaza tiene versiones explícitas. Las versiones son objetos de primera clase con identificadores propios y fechas de vigencia — no notas al pie ni historial no consultable. La pregunta "¿qué decía esta entidad en esta fecha?" es una pregunta legítima que Plaza debe poder responder para cualquier cosa que modele.

**Cuándo se rompe:** cuando se expone solo el estado actual y tratar los estados anteriores como historia no estructurada.

---

## 6. Estándares internacionales como columna

Plaza se alinea con los estándares internacionales establecidos para cada dominio que modela: ELI para identificadores de legislación, Akoma Ntoso y schema.org/Legislation para estructura de textos normativos, PROV-O para procedencia, SKOS para vocabularios controlados, W3C ORG para estructuras institucionales, DCAT para catálogos de datos. Estos no son objetivos futuros — son la columna sobre la cual se construye cada capa del modelo.

Estos estándares no fueron elegidos por preferencia estética. Son los que actualmente usa la mayor parte del mundo legal y de datos abiertos — la Unión Europea publica su derecho en ELI, varios parlamentos (Italia, Brasil, Kenya, Cámara de los Comunes británica) publican en Akoma Ntoso, los catálogos de datos abiertos de gobiernos en media docena de países siguen DCAT. Al adoptarlos, Plaza se vuelve interoperable por construcción: los sistemas externos no necesitan aprender el dialecto de Costa Rica, y los desarrolladores costarricenses que trabajan con Plaza aprenden vocabularios que les sirven globalmente.

Cuando un estándar y una conveniencia local entran en conflicto, el estándar gana. Cuando no existe un estándar aplicable, Plaza inventa lo mínimo necesario y lo documenta como extensión costarricense, no como su propio mundo paralelo.

**Cuándo se rompe:** cuando se diseña el modelo de datos de forma cómoda para la implementación y se pospone la alineación a estándares como "refactor futuro".

---

## 7. Separación entre dato y aplicación

Plaza es infraestructura de datos. Las aplicaciones que los consumen — interfaces humanas, asistentes de IA, analíticos, exploradores visuales — son construidas aparte, sobre los contratos públicos que Plaza expone.

Esta separación es deliberada: las aplicaciones envejecen; los datos estructurados bien diseñados perduran. Plaza elige ser la capa duradera.

**Cuándo se rompe:** cuando se agregan features a Plaza que solo tienen sentido para un consumidor específico (ej. "endpoint optimizado para nuestro chatbot").

---

## 8. Ética en el modelado de entidades sensibles

Cada vez que Plaza extiende su scope hacia un nuevo tipo de entidad — instituciones, cargos, funcionarios públicos, relaciones entre ellas — la extensión requiere un marco de gobernanza explícito proporcional a la sensibilidad de esa entidad.

Modelar una ley es distinto a modelar una institución. Modelar una institución es distinto a modelar un cargo. Modelar un cargo es distinto a modelar a un funcionario público que lo ocupa. Cada nivel de cercanía a lo humano requiere mayor rigor en privacidad, en exactitud, en posibilidad de corrección, y en claridad sobre el propósito del modelado. Ninguna extensión hacia entidades más sensibles se hace por conveniencia o por completitud enciclopédica — se hace cuando existe un propósito claro, una fuente oficial que la respalde, y un marco explícito que la gobierne.

**Cuándo se rompe:** cuando se agrega datos sobre personas como efecto secundario de otro objetivo, sin gobernanza explícita.

---

## 9. Apertura por arquitectura

Plaza es abierto en código, en datos, en esquemas, y en decisiones de diseño. Esta apertura está construida en la arquitectura misma y sostenida por un esquema de licenciamiento dual que protege al proyecto de dos fallas opuestas: la captura privada silenciosa y el debilitamiento por sobreuso comercial no retribuido.

El modelo es el siguiente: el código de Plaza se publica bajo una licencia copyleft fuerte (AGPL-3.0 o equivalente), que garantiza que cualquier uso — comunitario, académico, institucional, o empresarial dentro del ecosistema abierto — es gratuito y permanente, siempre que las modificaciones y servicios derivados se publiquen también bajo la misma licencia. Los datos se publican bajo una licencia share-alike (CC BY-SA 4.0 o equivalente), con el mismo efecto para el corpus jurídico.

Quien quiera integrar Plaza en productos cerrados o servicios empresariales sin publicar su código puede hacerlo negociando una licencia comercial paralela con quien detente los derechos del proyecto. Esa vía comercial no reduce la apertura del proyecto — solo la refleja: quien paga, está comprándose el derecho a no compartir; quien no paga, recibe todo bajo copyleft.

Para que este modelo funcione, todas las contribuciones al proyecto se rigen por un Contributor License Agreement (CLA) explícito que otorga al proyecto los derechos necesarios para sostener la vía comercial paralela, sin lo cual el modelo colapsa la primera vez que alguien contribuye código.

No existen versiones "premium" del corpus de Plaza. No existen datos reservados para aliados. No existen APIs privadas accesibles solo a licenciatarios comerciales. Lo comercial es el permiso de no abrir — nunca el acceso privilegiado a lo que Plaza produce.

**Cuándo se rompe:** cuando se aceptan términos de colaboración que restringen la redistribución o publicación de datos derivados, o cuando se deja entrar código al repositorio sin CLA firmado.

---

## 10. Disciplina reconstructiva

Plaza preserva evidencia suficiente para que cualquier conclusión pueda revisarse y regenerarse sin requerir una recaptura completa desde las fuentes. Los artefactos crudos son inmutables. Las interpretaciones son derivadas y revisables. Mezclar estas capas destruye la capacidad de corregir errores futuros.

Si el procesamiento mejora, las capturas anteriores se reprocesan. Si un estándar evoluciona, las exportaciones se regeneran. Si un conflicto se resuelve, las reconciliaciones se reaplican.

**Cuándo se rompe:** cuando se sobrescriben datos crudos con datos "limpios" perdiendo la capacidad de reparsear.

---

## 11. Honestidad operativa

Plaza nunca colapsa estados distintos en uno solo. Ausente no es lo mismo que no capturado. Fallido no es lo mismo que vacío. Inferido no es lo mismo que verificado. Cada estado se registra con precisión y la distinción se preserva hasta la capa pública.

Cuando el sistema no sabe algo, lo dice. Cuando algo falló, lo reporta. La falsa confianza es más peligrosa que la ignorancia declarada.

**Cuándo se rompe:** cuando se reporta "cobertura 100%" cuando significa "procesamos todo lo que encontramos", sin distinguir de lo que no se encontró.

---

## 12. Un hogar canónico por responsabilidad

Cada concepto en Plaza tiene un único lugar donde vive: una sola definición, una sola autoridad, un solo módulo de referencia. Las duplicaciones se colapsan; no se preservan por compatibilidad. Esto aplica al código, a la documentación, y al modelo de datos.

Un sistema con múltiples fuentes de verdad es un sistema en el que ninguna es confiable.

**Cuándo se rompe:** cuando se mantienen versiones legacy activas junto a la canónica para no romper nada.

---

## Orden de prioridad

Cuando dos principios parecen entrar en conflicto, el orden es:

1. **Evidencia antes que inferencia** — no se negocia con la verdad
2. **Identidad permanente** — no se negocia con contratos públicos
3. **Ética en el modelado** — no se negocia con la integridad de las personas
4. **Apertura por arquitectura** — no se negocia con la apertura
5. El resto, evaluados según contexto

Los cuatro principios superiores son los que, si se violan, cambian lo que Plaza es. Los demás tienen margen de interpretación contextual; estos cuatro no.

---

## Uso de este documento

Cuando una propuesta llega — técnica, estratégica, de colaboración, de scope — el procedimiento es identificar qué principios invoca y cuáles pone en riesgo. Si pone en riesgo alguno, la carga de argumentación recae en quien propone.

Este documento no es un obstáculo a la evolución de Plaza. Es la garantía de que la evolución preserve lo que hace a Plaza valioso.

---

## Relación con otras políticas

Este documento es el árbitro conceptual del proyecto. Los demás documentos del corpus fundacional son su implementación operativa en distintos dominios:

- [`VISION.md`](VISION.md) — la visión estratégica que estos principios protegen.
- [`SCOPE.md`](SCOPE.md) — qué hace Plaza hoy dentro de lo que los principios permiten.
- [`URI_POLICY.md`](URI_POLICY.md) — implementación operativa del Principio 2 (Identidad permanente) y del Principio 6 (Estándares como columna).
- [`ACCESS_SURFACES.md`](ACCESS_SURFACES.md) — implementación operativa del Principio 7 (Separación entre dato y aplicación).
- [`LICENSING.md`](LICENSING.md) — implementación operativa del Principio 9 (Apertura por arquitectura).
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — cómo la estructura interna de Plaza materializa los principios.
- [`DATA_MODEL.md`](DATA_MODEL.md) — implementación operativa del Principio 6 aplicado al grafo canónico.
- [`QUALITY_AND_VALIDATION.md`](QUALITY_AND_VALIDATION.md) — implementación operativa de los Principios 1, 10 y 11 en la frontera de canonicalización.
- [`VERSIONING.md`](VERSIONING.md) — implementación operativa del Principio 2 aplicado a la evolución temporal del proyecto.
