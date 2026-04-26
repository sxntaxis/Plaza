# Plaza Demo - State And Signals

This is the Demo construction contract for operational state and feedback.

## Artifact Classes

| Class | Meaning | Rule |
|---|---|---|
| Foundational | Project identity, scope, and policy in `docs/` | Not runtime storage |
| Operational | Mutable evidence, source registry, artifacts, issues | Preserved if it affects decisions |
| Canonical | Stable emitted graph, ontology, SHACL, Demo URIs | Published only after gates pass |
| Derived | Reports, caches, indexes, validation output | Rebuildable from operational or canonical inputs |

## Runtime Boundary

`docs/` is not runtime storage. `demo/specs/` contains active Demo contracts, `demo/ops/` contains Demo operation notes, and `demo/research/` contains Demo research. Local runtime state lives under gitignored `var/`.

## Signal Spine

Signals are structured feedback emitted by the pipeline.

`event` records append-only runtime facts. `issue` records durable feedback that can block publication.

Every signal has a `severity` (`debug`, `info`, `warning`, or `blocker`) and a lifecycle `status`. Events are recorded observations. Issues start `open` and may become `resolved`, `superseded`, or `ignored`.

An open issue with `severity=blocker` is a publication blocker for its `entity_ref` or affected artifact. Blockers must be visible to acquisition, refinement, reconciliation, canonicalization, validation, and the MCP guard through the same signal spine.

Minimum API:

```python
emit_event(...)
emit_issue(...)
list_open_blockers(...)
resolve_issue(...)
```

Required fields are defined by `schemas/signal.schema.json`.

Artifact envelopes connect signals to evidence through `artifact_ref`. Raw artifacts are operational state; if content changes, a new artifact envelope is created rather than overwriting the old one.

## Publication Gate

No candidate crosses into `data/demo/canonical/demo.ttl` unless it has a Demo URI under `https://demo.plaza.cr/eli/`, an enabled source, provenance, evidence, required structural relations, and no open blocker issue.

## Validation Gate

MCP consumes `data/demo/canonical/demo.ttl` and `data/demo/validation/validation_report.json`. If the validation report is missing or has `conforms=false`, MCP fails closed.

## Doctor

`plaza doctor demo` reports graph path, validation path, validation status, source enablement, artifact count, open blocker count, canonical resource count, and whether MCP is startable. It never mutates state.
