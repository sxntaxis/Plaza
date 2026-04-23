<div align="center">

# Plaza

### El derecho costarricense como bien común digital.

*Infraestructura cívica abierta, estructurada y verificable para la era digital.*

---

</div>

Plaza estructura el corpus normativo costarricense como un grafo verificable, alineado a estándares internacionales de datos jurídicos, para que cualquier sistema —inteligencia artificial, aplicación web, herramienta de análisis, o persona— pueda consultarlo con trazabilidad completa y citación verificable. Plaza es infraestructura AI-facing: expone datos verificables a sistemas de IA, pero no se presenta como un sistema de IA autónomo que interpreta el derecho.

No es un sitio web. No es una aplicación. No es un buscador.

**Plaza es la capa de datos sobre la cual esas cosas pueden construirse** — por Plaza mismo o por terceros — con la garantía de que lo que construyan descansa sobre información veraz, citable y temporalmente precisa.

---

## El problema

La información jurídica costarricense es pública por mandato constitucional. Pero no es accesible en los términos que el siglo XXI exige.

SCIJ cumple su función histórica como navegador humano del corpus legal. Sus identificadores son estables, pero no son derivables programáticamente ni alineados con estándares internacionales de datos jurídicos. Para consultar la Ley 7092 por su número de ley, un sistema externo necesita primero consultar el propio SCIJ para descubrir sus parámetros internos — lo que rompe la interoperabilidad automática.

Esta brecha tiene un costo concreto:

> Cuando un asistente de IA hoy responde sobre derecho costarricense, usualmente lo hace desde conocimiento memorizado durante su entrenamiento: puede estar desactualizado, puede alucinar un artículo, y su capacidad de citar fuentes depende de si tiene acceso a retrieval sobre un corpus confiable. Ese corpus confiable, estructurado y citable no existe hoy para el derecho costarricense. Plaza es ese corpus.

---

## La propuesta

Plaza no parte de la premisa de que toda fuente pública deba adquirirse automáticamente. Su regla de acceso es jerárquica: primero publicación proactiva, luego solicitud formal, luego convenio cuando corresponde, y solo de forma residual adquisición automatizada respetuosa. Plaza no se define por scraping; se define por acceso y redistribución jurídicamente habilitados.

Plaza transforma el corpus normativo costarricense en un recurso que cualquier sistema puede consultar con **tres compromisos fundamentales**:

<table>
<tr>
<td width="33%" valign="top">

### Verdad con evidencia

Plaza publica solo lo que puede respaldar con una fuente oficial identificable. Cuando hay incertidumbre, la declara. Cuando hay conflicto entre fuentes, lo registra sin resolverlo silenciosamente.

El sistema sabe lo que no sabe.

</td>
<td width="33%" valign="top">

### Identidad permanente

Cada norma, cada versión, cada artículo tiene un identificador único que no cambia nunca. Una URI emitida hoy seguirá resolviendo al mismo recurso en diez años.

Los enlaces no se rompen.

</td>
<td width="33%" valign="top">

### Apertura total

El código bajo AGPL-3.0. Los datos bajo CC BY-SA 4.0. Las decisiones de diseño públicas. Las licencias elegidas precisamente para que nadie pueda cerrar lo que Plaza abre.

La ley es pública; su representación también.

</td>
</tr>
</table>

---

## ¿A quién sirve?

<table>
<tr>
<td width="33%" valign="top">

#### 🏛️ Abogados e instituciones

Verificación de derecho vigente con trazabilidad a publicación oficial. Citación con URIs permanentes. Consulta temporal precisa: *"¿qué decía este artículo el 15 de marzo de 2019?"*

</td>
<td width="33%" valign="top">

#### 🤖 Sistemas de IA

Fuente verificable para asistentes legales, chatbots institucionales, y herramientas de análisis. Servidor MCP nativo. Retrieval determinístico con citas que el usuario final puede verificar.

</td>
<td width="33%" valign="top">

#### 💻 Desarrolladores e investigadores

Snapshots descargables en RDF, JSON-LD y Akoma Ntoso. API REST sobre URIs estables. Catálogo DCAT para federación. Código abierto, datos abiertos, esquemas abiertos.

</td>
</tr>
</table>

---

## Cómo se ve

Cada norma en Plaza tiene una URI permanente siguiendo el estándar europeo [ELI](https://op.europa.eu/en/web/eu-vocabularies/eli):

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092
```

Consultarla en cualquier formato estándar via content negotiation:

```bash
curl -H "Accept: application/ld+json" \
  https://plaza.cr/eli/cr/asamblea/1988/ley/7092
```

Devuelve metadata estructurada con procedencia PROV-O completa:

```turtle
<https://plaza.cr/eli/cr/asamblea/1988/ley/7092>
    a eli:LegalResource, schema:Legislation ;
    eli:type_document plaza:tipo-ley ;
    eli:number "7092" ;
    eli:date_document "1988-04-21"^^xsd:date ;
    eli:first_date_entry_in_force "1988-05-24"^^xsd:date ;
    eli:in_force plaza:vigente ;
    eli:amended_by <https://plaza.cr/eli/cr/asamblea/2018/ley/9635> ;
    prov:wasDerivedFrom <https://plaza.cr/artifact/scij/...> .
```

Para obtener la versión vigente en una fecha específica:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/version/2023-01-15
```

Para navegar directamente al artículo 42 de esa versión:

```
https://plaza.cr/eli/cr/asamblea/1988/ley/7092/articulo/42/version/2023-01-15
```

---

## Estándares

Plaza no inventa su propio dialecto. Adopta los estándares internacionales que usa la mayor parte del mundo legal y de datos abiertos:

| Rol | Estándar | Publicador |
|---|---|---|
| Identificadores de legislación | [**ELI**](https://data.europa.eu/eli/ontology) | Unión Europea |
| Estructura de textos legales | [**Akoma Ntoso**](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/) | OASIS |
| Interoperabilidad web | [**schema.org/Legislation**](https://schema.org/Legislation) | schema.org |
| Procedencia de datos | [**PROV-O**](https://www.w3.org/TR/prov-o/) | W3C |
| Vocabularios controlados | [**SKOS**](https://www.w3.org/TR/skos-reference/) | W3C |
| Catálogos de datasets | [**DCAT**](https://www.w3.org/TR/vocab-dcat-3/) | W3C |
| Validación formal | [**SHACL**](https://www.w3.org/TR/shacl/) | W3C |

Plaza no es un experimento costarricense. Es la manera costarricense de participar de una conversación global sobre cómo debe exponerse el derecho en la era de los datos.

---

## La constitución del proyecto

Plaza se gobierna por doce documentos fundacionales que establecen, con la rigurosidad de una constitución, qué es Plaza, cómo opera, y qué promete.

<table>
<tr>
<td width="33%" valign="top">

**Fundación**

- [**VISION**](docs/VISION.md) — qué es y por qué existe
- [**PRINCIPLES**](docs/PRINCIPLES.md) — las reglas no-negociables
- [**SCOPE**](docs/SCOPE.md) — qué hace y qué no

</td>
<td width="33%" valign="top">

**Contratos públicos**

- [**URI_POLICY**](docs/URI_POLICY.md) — identificadores permanentes
- [**ACCESS_SURFACES**](docs/ACCESS_SURFACES.md) — cómo se consume
- [**LICENSING**](docs/LICENSING.md) — términos de uso
- [**LEGAL_BASIS**](docs/LEGAL_BASIS.md) — marco jurídico habilitante

</td>
<td width="33%" valign="top">

**Arquitectura y evolución**

- [**ARCHITECTURE**](docs/ARCHITECTURE.md) — estructura interna
- [**DATA_MODEL**](docs/DATA_MODEL.md) — el grafo canónico
- [**QUALITY_AND_VALIDATION**](docs/QUALITY_AND_VALIDATION.md) — criterios de publicación
- [**VERSIONING**](docs/VERSIONING.md) — cómo evoluciona
- [**REFERENCES**](docs/REFERENCES.md) — glosario y bibliografía

</td>
</tr>
</table>

> [!TIP]
> Si es tu primera vez acá, leé [`VISION.md`](docs/VISION.md) primero (5 minutos), luego [`PRINCIPLES.md`](docs/PRINCIPLES.md) (10 minutos). Juntos te dan el 80% de lo que necesitás saber sobre el proyecto.

---

## Estado actual

> [!WARNING]
> **Plaza está en estado pre-lanzamiento (`0.x.y`).** El diseño está maduro pero todavía no hay datos publicados ni URIs públicas en producción. Las URIs de ejemplo en este documento son ilustrativas, no operativas.

Lo que existe hoy:

- ✅ Los doce documentos fundacionales, coherentes entre sí.
- ✅ Diseño del modelo semántico alineado a estándares internacionales.
- ✅ Política de URIs permanentes completamente especificada.
- ✅ Modelo de licenciamiento dual con mecanismo de sostenibilidad.

Lo que está en construcción:

- 🔨 Implementación del sistema de habilitación de fuentes, adquisición, refinamiento y canonicalización.
- 🔨 Primer snapshot público del corpus.
- 🔨 Publicación de la ontología Plaza bajo dominio permanente.

Lo que está por venir:

- ⏳ Primer lanzamiento público (`1.0.0`) con URIs operativas.
- ⏳ API REST y servidor MCP accesibles.
- ⏳ Colaboración institucional formal con fuentes oficiales costarricenses.

---

## Cómo involucrarse

Plaza es un proyecto comunitario. Si querés sumarte, hay varias puertas de entrada según lo que puedas aportar.

<details>
<summary><b>Soy abogado o estudio derecho</b></summary>

<br>

Tu conocimiento jurídico es invaluable para validar el modelo de datos, revisar las convenciones de identificación, y asegurar que las decisiones técnicas respetan la realidad jurídica costarricense. Abrí un [issue](../../issues) con tu perspectiva o contactanos directamente.

Áreas donde más necesitamos criterio jurídico:

- Vocabulario de tipos normativos y emisores.
- Tratamiento de relaciones entre normas (afectaciones, concordancias, reglamentaciones).
- Casos especiales: constituciones, códigos, normativa municipal.

</details>

<details>
<summary><b>Soy desarrollador</b></summary>

<br>

El código está en construcción. Antes de contribuir código al repositorio principal, el proyecto requiere formalizar su Contributor License Agreement (CLA) — ver [`LICENSING.md`](docs/LICENSING.md). Mientras tanto, podés contribuir:

- Revisando los documentos técnicos ([`DATA_MODEL.md`](docs/DATA_MODEL.md), [`ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`QUALITY_AND_VALIDATION.md`](docs/QUALITY_AND_VALIDATION.md)) y reportando inconsistencias.
- Proponiendo diseños alternativos donde veas mejoras.
- Experimentando con los estándares adoptados en tu propio sandbox.

</details>

<details>
<summary><b>Represento una institución o comunidad</b></summary>

<br>

Plaza busca colaboración institucional con fuentes oficiales costarricenses y con comunidades técnicas, jurídicas y cívicas interesadas en el acceso abierto a la información pública. El respaldo de organizaciones que comparten estos valores fortalece la viabilidad del proyecto frente a interlocutores institucionales.

Contactanos para explorar formas de colaboración.

</details>

<details>
<summary><b>Soy ciudadano que quiere apoyar</b></summary>

<br>

- **Dale star al repositorio.** Cada star ayuda a que más personas descubran el proyecto.
- **Compartilo.** Plaza solo tiene sentido si la comunidad costarricense lo conoce.
- **Mandanos feedback.** Abrí un issue con preguntas, observaciones, o críticas constructivas.

</details>

---

## Licencia

Plaza adopta un **modelo de licenciamiento dual** diseñado para proteger la apertura del proyecto sin ingenuidad respecto a la sostenibilidad.

- **Código** — [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html). Copyleft fuerte que cierra el hueco de SaaS: quien opere Plaza como servicio debe publicar sus modificaciones.
- **Datos** — [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Share-alike: las obras derivadas del corpus también se publican abiertamente.
- **Vía comercial paralela** — para integraciones en productos cerrados, disponible mediante licenciamiento negociado. Nunca otorga acceso privilegiado a datos, solo el permiso de no compartir las derivaciones.

Ver [`LICENSING.md`](docs/LICENSING.md) para el modelo completo, incluyendo los cuatro pilares irreversibles que ninguna versión futura puede modificar.

> **Plaza no pertenece a quienes lo desarrollan. Pertenece al país.**

---

## Respaldo

Plaza es impulsado por voluntarios costarricenses y cuenta con el interés activo de la [Fundación Costarricense de IA Responsable (FAIR)](https://www.fair.cr/) como comunidad asociada.

Si tu organización comparte estos valores y quiere respaldar formalmente el proyecto, contactanos.

---

<div align="center">

**Construido en Costa Rica, para Costa Rica, bajo estándares globales.**

[Documentación](./docs) · [Issues](../../issues) · [Discusiones](../../discussions)

</div>
