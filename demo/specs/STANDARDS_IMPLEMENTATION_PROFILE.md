# Plaza Demo - Standards Implementation Profile

This document is the Demo standards contract. It replaces research-stage language and uses **Demo** as the only phase term.

## Scope

The functional Demo persists one canonical RDF graph at `data/demo/canonical/demo.ttl`, validates it with SHACL, and exposes it only through the local read-only MCP surface.

The Demo does not implement a REST API, public HTTP MCP, UI, SPARQL endpoint, Akoma Ntoso export, schema.org output, person modeling, or legal interpretation.

## Legal Resource URIs

Every Demo legal resource uses:

```text
https://demo.plaza.cr/eli/...
```

Examples:

```text
https://demo.plaza.cr/eli/cr/asamblea_legislativa/1949/constitucion/politica
https://demo.plaza.cr/eli/cr/asamblea_legislativa/YYYY/ley/NNNN
https://demo.plaza.cr/eli/cr/poder_ejecutivo/YYYY/decreto_ejecutivo/MMMM
```

These are Demo URIs, not public canonical production URIs.

A production candidate URI is mechanically derived by replacing the host with `https://plaza.cr/eli/...`. That candidate must not be treated as issued until Plaza publishes it as canonical production identity.

The legacy non-HTTP Demo URI scheme is not a legal-resource identity scheme.

## RDF And Validation

ELI identifies legal resources. Akoma Ntoso, when introduced later, serializes legal documents; it does not define Plaza identity.

The persisted Demo graph format is RDF/Turtle. The graph uses ELI for legal resources, PROV-O for provenance, SKOS for controlled concepts, and Plaza ontology terms only where the Demo needs local markers such as `plaza:demoOnly`.

The validation contract is `ontology/shapes.ttl`. SHACL validates graph structure and required metadata; it does not certify legal truth. A conforming report is written to `data/demo/validation/validation_report.json` before MCP can serve the graph.

## Law-Decree Relation

The demonstrative law-decree relation uses ELI foundation predicates:

```turtle
:decreto eli:based_on :ley .
:ley eli:basis_for :decreto .
```

The Demo does not use an application predicate as the default law-decree relation.

`eli:applies` is reserved for informative/de conformidad application cases when evidence supports that narrower meaning.

## Publication Requirements

A resource may enter `data/demo/canonical/demo.ttl` only when it has:

1. A valid Demo ELI URI.
2. An enabled source in `registry/sources.yml`.
3. Preserved evidence or an artifact reference.
4. Minimal provenance.
5. No open blocker issue.
6. Passing Demo validation.

## Normative Implementation Requirements for Demo

| Area | Demo requirement |
|---|---|
| URI identity | Legal resources use `https://demo.plaza.cr/eli/...`; each Demo URI is mechanically convertible to the production host without claiming production issuance. |
| ELI | The graph uses `eli:LegalResource` and `eli:LegalExpression`; every legal resource has at least one expression. |
| ELI relation | The law-decree relation uses `eli:based_on` from decree to law and `eli:basis_for` from law to decree. |
| RDF/Turtle | `data/demo/canonical/demo.ttl` must parse as Turtle and remain the persisted Demo graph. |
| PROV-O | Canonical entities derive from preserved `plaza:SourceArtifact` evidence or equivalent preserved source artifact records. |
| SKOS | Controlled values for type, issuer, and in-force status use SKOS where those values are represented. |
| SHACL | Full Demo readiness requires SHACL Core validation through a real validator; current scaffold validation is not enough. |
| Source artifacts | SCIJ artifacts must have hash, source URL or local ID, capture timestamp, access method, and storage reference. |
| Demo limitations | The Demo graph must declare limitations and avoid claims of official certification or production canonical URI issuance. |
| No interpretation | The graph encodes data and provenance, not legal advice, legal reasoning, or certification. |

The current `0.4.0` scaffold may satisfy only a subset of this profile. Full conformance is a functional Demo goal.
