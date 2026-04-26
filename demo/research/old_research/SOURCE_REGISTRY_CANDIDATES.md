# Plaza — Source Registry Candidates

**Estado:** memoria de investigación.
**No es fuente jurídica final.** El régimen habilitante debe verificarse en `LEGAL_BASIS.md` y, cuando corresponda, con research legal actualizado.

---

## Propósito

Este documento destila el mapa legacy de fuentes oficiales costarricenses para evitar research redundante. No incorpora fuentes al scope activo. Solo registra:

- qué fuente existe;
- qué tipo de material puede aportar;
- qué rol potencial tendría en Plaza;
- qué riesgos o restricciones parecen relevantes;
- qué tendría que verificarse antes de usarla.

---

## Estados de incorporación

| Estado | Significado |
|---|---|
| **Core actual** | Fuente central del alcance normativo actual. |
| **Core complementario** | Fuente relevante para evidencia/publicación, pero no necesariamente para ingesta completa. |
| **Futuro condicionado** | Potencialmente útil, pero requiere madurez, convenio, o verificación legal. |
| **Solo referencia** | Útil para orientación o contraste, no para corpus. |
| **Excluida ordinariamente** | No debe incorporarse en flujo público ordinario. |
| **Requiere verificación** | No tomar ninguna decisión sin revisar condiciones actuales. |

---

## Tabla de fuentes candidatas

| Fuente | Institución | Material potencial | Rol para Plaza nueva | Estado | Riesgos / notas | Verificación pendiente |
|---|---|---|---|---:|---|---|
| **SCIJ / SINALEVI** | Procuraduría General de la República | Normativa consolidada, versiones, metadata, afectaciones, concordancias, reglamentaciones, descriptores, hooks a PGR/constitucional. | Fuente operativa principal para corpus normativo consolidado. | Core actual | Es consolidación operativa oficial, no publicación original. Debe conservarse como fuente con autoridad propia, sin presentarla como certificación documental. | Confirmar comportamiento actual de surfaces y términos antes de crawl amplio. |
| **La Gaceta / Diario Oficial** | Imprenta Nacional | Publicación oficial por edición/alcance; leyes, decretos, reglamentos, acuerdos, erratas, avisos, edictos, etc. | Evidencia de publicación oficial y reconciliación temporal. | Core complementario / futuro reconciliación | No todo lo publicado debe convertirse en corpus Plaza. Alto riesgo en edictos/avisos/personas. | Confirmar estructura actual, términos, CC, acceso estable, y marco de publicabilidad. |
| **Asamblea Legislativa** | Asamblea Legislativa | Leyes, expedientes, PDFs, contexto legislativo, posibles certificaciones. | Complemento para textos de ley, trazabilidad legislativa y certificación documental institucional. | Futuro condicionado | Expedientes pueden tener régimen distinto a actos públicos finales. No asumir redistribución plena. | Verificar términos actuales, estructura y valor frente a SCIJ/Gaceta. |
| **TSE — Normativa** | Tribunal Supremo de Elecciones | Normativa electoral, PDFs institucionales, resoluciones/reglamentos electorales. | Fuente sectorial complementaria; posible fuente para normativa electoral oficial. | Futuro condicionado | No mezclar con padrón electoral ni datos sensibles. | Verificar licencia actual, alcance de CC, endpoints, y si el material duplica SCIJ. |
| **Ministerio de Hacienda / Digesto Tributario** | Ministerio de Hacienda | Normativa tributaria, documentos sectoriales, posiblemente digestos y resoluciones. | Fuente sectorial complementaria para normas tributarias y contexto hacendario. | Futuro condicionado | Puede mezclar normativa con documentos administrativos/no normativos. | Verificar portal actual, formatos, régimen, y solapamiento con SCIJ. |
| **Poder Judicial / Nexus / CEIJ** | Poder Judicial | Jurisprudencia, sentencias, votos, boletines, resoluciones constitucionales. | Hooks desde normas; corpus completo solo con convenio. | Excluida ordinariamente / futuro con convenio | Alto riesgo de datos personales. El marco actual exige extrema cautela y posiblemente convenio formal. | No iniciar scraping estructurado público sin respaldo legal específico. |
| **Sala Constitucional** | Poder Judicial | Votos y acciones constitucionales. | Hooks/relaciones que afectan normas; no corpus completo ahora. | Futuro condicionado | Contiene partes/personas y datos incidentales. | Verificar vía oficial y régimen de anonimización/convenio. |
| **PGR — Pronunciamientos** | PGR | Dictámenes, opiniones jurídicas, interpretaciones. | Hooks desde normas; corpus completo en futuro. | Futuro condicionado | No son normativa; valor interpretativo. No confundir con norma. | Verificar disponibilidad procesable y régimen de uso. |
| **CGR / Datos abiertos** | Contraloría General de la República | Datos abiertos, normativa/fiscalización, resoluciones. | Futura capa institucional/control hacienda; no core normativo inicial. | Futuro condicionado | Puede incluir datos de contratación/personas jurídicas/personas físicas. | Verificar CC BY-SA actual y granularidad de datos. |
| **Archivo Nacional** | Archivo Nacional | Material histórico, documentos oficiales, archivos digitalizados. | Fuente futura para corpus histórico o verificación documental. | Futuro condicionado | Digitalización no equivale a estructura normativa usable. | Verificar licencias, APIs, metadata y prioridades. |
| **SINABI / Biblioteca digital** | Sistema Nacional de Bibliotecas | Gacetas históricas digitalizadas, PDFs antiguos. | Apoyo para reconstrucción histórica cuando La Gaceta moderna no cubra. | Solo referencia / futuro histórico | Calidad OCR/PDF puede variar. No usar como sustituto de fuente primaria moderna si existe. | Verificar estado del repositorio, derechos y metadata. |
| **Municipalidades** | Gobiernos locales | Acuerdos municipales, reglamentos locales, avisos. | Potencial futuro para normativa local. | Futuro condicionado | Altísima heterogeneidad; datos personales/avisos. | Requiere estrategia municipal separada y vocabulario de emisores. |
| **Portales institucionales sectoriales** | Ministerios/autónomas | Reglamentos, directrices, resoluciones, PDFs. | Fuente complementaria cuando SCIJ/Gaceta no basten o para validación. | Requiere verificación caso por caso | Términos, formatos y actualización varían. | Crear adapter solo con fuente habilitada. |

---

## Reglas de uso del source registry

1. **Una fuente en esta tabla no está habilitada automáticamente.**
2. **La fuente debe pasar el registro de habilitación** descrito por la arquitectura actual: vía de acceso, régimen jurídico/licencia, restricciones, finalidad original, uso previsto, publicabilidad y obligaciones adicionales.
3. **SCIJ y La Gaceta no cumplen el mismo rol.** SCIJ consolida y estructura; La Gaceta publica oficialmente.
4. **No todo lo oficial es publicable por Plaza como dato estructurado.** La finalidad y datos personales importan.
5. **No se scrapea por defecto.** La jerarquía correcta es publicación proactiva, solicitud formal, convenio, adquisición automatizada residual.
6. **Las fuentes con personas o casos judiciales requieren gobernanza adicional.**
7. **Las fuentes sectoriales no deben expandir scope sin criterio explícito.**

---

## Roles de fuente

Una misma fuente puede tener varios roles. Registrar el rol evita sobreafirmar.

| Rol | Definición | Ejemplos |
|---|---|---|
| **Publicación oficial** | Fuente donde el acto fue publicado oficialmente. | La Gaceta. |
| **Consolidación operativa oficial** | Fuente oficial que consolida textos, versiones y relaciones para consulta. | SCIJ/SINALEVI. |
| **Certificación documental institucional** | Constancia o documento emitido por autoridad competente para certificar un hecho/documento. | Eventual Asamblea/PGR/Imprenta según caso. |
| **Fuente sectorial oficial** | Portal de institución que publica normativa o documentos propios. | TSE, Hacienda, CGR. |
| **Fuente histórica/archival** | Repositorio público de documentos históricos digitalizados. | SINABI, Archivo Nacional. |
| **Hook interpretativo** | Fuente que interpreta o afecta una norma, sin ser parte del corpus normativo principal. | Pronunciamientos PGR, votos constitucionales. |

---

## Preguntas pendientes por fuente

Antes de crear un adapter o ingresar material al grafo público:

1. ¿La fuente publica actos públicos, consolidaciones, interpretaciones, expedientes o avisos?
2. ¿Cuál es la vía preferente de acceso?
3. ¿Existe descarga estructurada o solo UI humana?
4. ¿Qué régimen jurídico o licencia aplica?
5. ¿Hay datos personales, sensibles o incidentales?
6. ¿El uso de Plaza conserva la finalidad original?
7. ¿La fuente requiere convenio formal?
8. ¿La fuente ofrece identificadores propios estables?
9. ¿La fuente tiene timestamps, hashes, versiones o metadata de modificación?
10. ¿Qué se debe preservar como artefacto crudo?
11. ¿Qué no debe estructurarse aunque aparezca en el texto?
12. ¿Qué superficie pública Plaza puede exponer sin simular apertura plena?

---

## Prioridad práctica

### Nivel 1 — Core inmediato

- SCIJ/SINALEVI adapter.
- Registro de publication hints SCIJ sin sobreafirmar.
- Primer modelo de fuente habilitada.

### Nivel 2 — Reconciliación prioritaria

- La Gaceta adapter para ediciones/alcances y publicación oficial.
- Matching controlado SCIJ ↔ Gaceta para normas seleccionadas.
- No ingesta general de edictos/avisos.

### Nivel 3 — Complementos selectivos

- Asamblea para leyes/certificación/documentos legislativos relevantes.
- TSE/Hacienda/CGR solo para casos donde aporten valor no cubierto por SCIJ/Gaceta.

### Nivel 4 — Futuro sensible

- Poder Judicial/Nexus.
- Pronunciamientos PGR como corpus completo.
- Capa institucional/cargos.
- Municipalidades.

---

## No-goals del registry

- No es catálogo DCAT.
- No es inventario exhaustivo de todo el Estado.
- No autoriza scraping.
- No decide licencias.
- No cambia el scope actual.
- No sustituye solicitudes formales ni convenios.
- No convierte datos personales visibles en datos estructurados publicables.
