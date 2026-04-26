# Plaza — Future State Hub Notes

**Estado:** memoria de investigación de largo plazo.
**No forma parte del scope actual.**
**Fuente legacy absorbida:** `Plaza as the Costa Rican State Hub: Vision & Roadmap.md`, partes de `RDF_adoption_roadmap.md`.

---

## Tesis destilada

Legacy imaginaba Plaza como “hub del Estado costarricense”: normas, instituciones, cargos y eventualmente titularidad oficial. Esa visión tiene valor estratégico, pero es peligrosa si se adelanta.

La formulación compatible con Plaza nueva es:

> Plaza puede habilitar en el futuro un grafo institucional del Estado costarricense, pero solo después de estabilizar el corpus normativo y con gobernanza proporcional a la sensibilidad de cada capa.

---

## Capas futuras posibles

| Capa | Descripción | Estándar probable | Estado |
|---|---|---|---|
| Instituciones | Poderes, ministerios, órganos, autónomas, adscritas. | W3C ORG + SKOS + PROV-O | Futuro condicionado. |
| Unidades | Departamentos, direcciones, órganos internos. | W3C ORG | Futuro condicionado. |
| Cargos abstractos | “Ministro de Hacienda”, “Contralor General”, etc. | W3C ORG `org:Post` | Futuro condicionado. |
| Titularidad oficial | Quién ocupó oficialmente un cargo, cuándo y por qué acto. | ORG membership/post + PROV-O | Muy sensible; puede no ocurrir. |
| Personas privadas | Personas fuera de función pública institucional. | Ninguno | Fuera. |
| Perfil biográfico | Datos personales, redes, atributos, trayectoria general. | Ninguno | Fuera. |

---

## Secuencia obligatoria

1. Corpus normativo estable.
2. URI/model/versioning estables.
3. Fuente registry maduro.
4. Capa institucional sin personas.
5. Capa de cargos abstractos sin titulares.
6. Evaluación jurídica y de finalidad para titularidad oficial.
7. Decisión colectiva explícita.
8. Implementación limitada, verificable y reversible.

Nunca saltar directo a personas.

---

## Reglas para capa institucional

La capa institucional sí puede ser compatible con Plaza si:

- se basa en normas que crean/definen instituciones;
- usa W3C ORG/SKOS;
- conserva procedencia;
- no inventa organigramas sin fuente;
- distingue órgano, institución, unidad y cargo;
- versiona cambios institucionales;
- no requiere perfilar personas.

Ejemplos de entidades aceptables en futuro:

- Asamblea Legislativa;
- Poder Ejecutivo;
- Ministerio de Hacienda;
- Tribunal Supremo de Elecciones;
- Contraloría General de la República;
- Procuraduría General de la República;
- órgano adscrito X, si hay base normativa.

---

## Reglas para cargos

La capa de cargos abstractos podría ser válida si:

- el cargo existe por norma o acto oficial;
- se modela como post/office, no como persona;
- tiene URI propia;
- tiene institución contenedora;
- tiene fecha de creación/supresión si se conoce;
- tiene procedencia.

Ejemplo conceptual:

```text
/cargo/ministro_hacienda
  tipo: cargo_publico
  pertenece_a: Ministerio de Hacienda
  creado_por: norma/acto X
```

Esto no dice quién ocupa el cargo.

---

## Titularidad oficial: zona roja

Representar quién ocupó oficialmente un cargo solo podría considerarse si:

1. El cargo abstracto ya está modelado.
2. Hay acto oficial de nombramiento/remoción/sustitución.
3. La finalidad es estrictamente institucional.
4. La representación es necesaria para trazabilidad, continuidad administrativa, responsabilidad pública o control democrático.
5. Existe evaluación explícita de protección de datos/finalidad.
6. Hay mecanismo de rectificación.
7. No se agregan atributos no funcionales.
8. No se modelan relaciones personales.
9. No se hace scoring/perfilado.
10. El proyecto decide colectivamente que vale el riesgo.

Puede no ocurrir nunca. Eso es aceptable.

---

## Qué queda prohibido

- Bases públicas buscables de personas.
- Perfilado de funcionarios.
- Atributos personales no necesarios para el cargo.
- Relaciones familiares/sociales/políticas.
- Inferencias sobre conducta, ideología o afinidades.
- Enriquecimiento con fuentes no oficiales.
- Datos de personas privadas.
- Scraping de biografías.
- Usar FOAF/schema Person en MVP.
- Convertir signatarios en entidad persona por defecto.

---

## Estándares futuros posibles

| Estándar | Uso posible | Restricción |
|---|---|---|
| W3C ORG | Instituciones, unidades, cargos/posts, memberships. | Solo cuando scope institucional se active. |
| SKOS | Tipos de institución, tipos de cargo, poderes del Estado. | Vocabularios curados. |
| PROV-O | Evidencia de creación, modificación, nombramiento. | Obligatorio si se modela. |
| schema.org/Organization | Interoperabilidad web auxiliar. | No sustituye ORG. |
| FOAF/schema Person | Solo si titularidad oficial se aprueba. | No usar temprano. |

---

## Research fresco requerido antes de activar capa institucional

1. Identificadores oficiales de instituciones costarricenses.
2. Estructura actual del Estado y fuentes normativas que crean instituciones.
3. Mejores prácticas W3C ORG para public bodies.
4. Cómo versionar cambios institucionales.
5. Si existe catálogo oficial de instituciones con IDs.
6. Régimen legal aplicable a titulares de cargos públicos.
7. Jurisprudencia costarricense sobre datos de funcionarios públicos.
8. Mecanismo de rectificación y supresión.
9. Política de minimización de datos.
10. Decisión de governance.

---

## Criterio de entrada al roadmap futuro

Una propuesta de state hub solo puede entrar al roadmap si responde:

1. ¿Qué problema actual del corpus normativo resuelve?
2. ¿La capa normativa ya está madura?
3. ¿Qué fuente oficial define la institución/cargo?
4. ¿Qué URI tendrá?
5. ¿Cómo se versiona?
6. ¿Qué datos personales se evitan?
7. ¿Qué estándar se usa?
8. ¿Qué surface pública lo expondrá?
9. ¿Qué riesgos legales activa?
10. ¿Qué queda explícitamente fuera?

---

## Resumen

La visión de Plaza como state hub es útil como norte, pero debe permanecer bajo llave. La Plaza actual debe construir primero el sustrato normativo. La capa institucional puede venir después. La capa de cargos, después. La titularidad oficial, quizá. El perfilado de personas, nunca.
