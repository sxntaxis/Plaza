# Demo Roadmap - Functional Local MCP Demo

## Goal

The functional Demo work turns the `0.4.0` scaffold into a functional local stdio MCP Demo backed by the minimum useful approved set of real legal resources, preserved source artifacts, SHACL validation, citation-complete read-only tools/resources, and no-interpretation guardrails.

The resource set is intentionally small for the functional Demo, but the architecture should not hardcode smallness. Corpus expansion is a later lane after the controlled Demo path is correct.

## Inputs

- `demo/specs/STANDARDS_IMPLEMENTATION_PROFILE.md`
- `demo/specs/MCP_IMPLEMENTATION_PROFILE.md`
- `demo/specs/STATE_AND_SIGNALS.md`
- `demo/ops/DEMO_PHASE1_SELECTION_SUMMARY.md`
- `demo/research/source_audits/CORRECTNESS_AUDIT_REPORT.md`
- `demo/research/source_audits/INVENTORY_REPORT.md`
- Foundational docs in `docs/`

## Phase 1 - Select the approved legal-resource set

Purpose: choose the exact resources represented by the Demo and freeze their identifiers.

Files likely touched: `demo/ops/DEMO_ACCEPTANCE_CONTRACT.md`, `data/demo/manifest.candidate.json`, `registry/sources.yml`.

Outputs produced: resource list, source IDs, Demo URI candidates, selection rationale.

Tests/verification: every selected legal resource has a `https://demo.plaza.cr/eli/...` URI; no person modeling; no legal interpretation claims.

Blocking decisions: exact law/decree pair, whether constitution stays in the Demo resource set, and what SCIJ evidence is acceptable for each resource.

## Phase 2 - Preserve SCIJ source artifacts

Purpose: store the evidence used to construct the Demo graph without relying on live network access at runtime.

Files likely touched: `var/artifacts/` during local work and the promoted fixture/preserved artifact location selected for commit.

Outputs produced: preserved SCIJ source artifacts and capture metadata.

Tests/verification: artifacts are immutable, hashable, and mapped to source URL or source local ID.

Blocking decisions: where committed Demo evidence lives if it cannot remain in ignored `var/`.

## Phase 3 - Build artifact envelopes

Purpose: wrap every preserved source artifact with source, capture, storage, and hash metadata.

Files likely touched: `src/plaza/core/artifacts/`, selected artifact-envelope records, tests.

Outputs produced: artifact envelopes with `sha256:` hashes and run IDs.

Tests/verification: missing or malformed hash fails; missing source URL/local ID fails; artifact count appears in `doctor demo`.

Blocking decisions: final envelope storage format and whether envelopes are JSON files, manifest entries, or SQLite rows.

## Phase 4 - Implement minimal refinement

Purpose: extract the minimal fields needed for legal resources, expressions, text snippets, source identifiers, and relations.

Files likely touched: `src/plaza/sources/scij/`, `src/plaza/core/reconciliation/`, tests.

Outputs produced: deterministic refined records for the approved resource set.

Tests/verification: refinement is repeatable from preserved artifacts and does not access network at runtime.

Blocking decisions: minimum text granularity and handling of missing/ambiguous SCIJ fields.

## Phase 5 - Generate real Demo RDF graph

Purpose: replace scaffold graph generation with deterministic RDF output from refined records.

Files likely touched: `src/plaza/demo/build_graph.py`, `src/plaza/core/canonicalization/`, `data/demo/canonical/demo.ttl`, tests.

Outputs produced: Turtle graph for the approved real legal resources and their expressions.

Tests/verification: Turtle parses; all legal URIs use Demo host; law-decree relation uses `eli:based_on` / `eli:basis_for`; no active `eli:applies` default relation.

Blocking decisions: URI path conventions for emitter names and expression/version URIs.

## Phase 6 - Add real PROV-O chain

Purpose: connect canonical entities to acquisition, refinement, reconciliation, and canonicalization activities.

Files likely touched: `ontology/plaza.ttl`, `src/plaza/demo/build_graph.py`, `data/demo/canonical/demo.ttl`, tests.

Outputs produced: PROV-O chain from `plaza:SourceArtifact` to canonical Demo entities.

Tests/verification: every canonical entity has provenance to an artifact or preserved evidence.

Blocking decisions: minimum PROV-O activity/entity model for Demo.

## Phase 7 - Implement SHACL Core validation

Purpose: replace scaffold text validation with real SHACL Core validation through `pyshacl` or equivalent.

Files likely touched: `ontology/shapes.ttl`, `src/plaza/demo/validate_graph.py`, `data/demo/validation/validation_report.json`, `pyproject.toml`, tests.

Outputs produced: validation report generated from the SHACL run.

Tests/verification: conforming graph passes; missing required expression/provenance fails; MCP fails closed on missing/nonconforming report.

Blocking decisions: dependency policy for `pyshacl` and report JSON shape.

## Phase 8 - Implement MCP server/tools/resources

Purpose: implement the local stdio MCP surface declared by the active MCP profile.

Files likely touched: `src/plaza/mcp/server.py`, `src/plaza/mcp/tools.py`, `src/plaza/mcp/resources.py`, `src/plaza/mcp/citations.py`, `src/plaza/mcp/guards.py`, tests.

Outputs produced: read-only MCP tools/resources over `data/demo/canonical/demo.ttl` and validation report.

Tests/verification: tools/resources list matches profile; repeated calls are deterministic; no writes, network access, or arbitrary filesystem reads.

Blocking decisions: direct FastMCP dependency and exact tool response schemas.

## Phase 9 - Add citation wrapper and no-interpretation guardrails

Purpose: make every successful response cite evidence and reject legal interpretation requests.

Files likely touched: `src/plaza/mcp/citations.py`, `src/plaza/mcp/tools.py`, `src/plaza/mcp/resources.py`, tests.

Outputs produced: `citations[]` on tool responses and deterministic rejection/redirect behavior.

Tests/verification: responses without citations fail; interpretation-shaped prompts are rejected or redirected to factual queries.

Blocking decisions: exact citation object fields and rejection language.

## Phase 10 - Add acceptance tests and Claude Desktop smoke test

Purpose: prove the local MCP Demo runs end-to-end for a client.

Files likely touched: `tests/`, `demo/ops/LOCAL_RUNBOOK.md`, `demo/ops/ACCEPTANCE_CHECKLIST.md`.

Outputs produced: automated acceptance tests and documented Claude Desktop local stdio smoke test result.

Tests/verification: all acceptance contract checks pass on a clean local checkout.

Blocking decisions: smoke-test host/version and reproducible test fixture setup.

## Out of scope for the functional Demo

- Public HTTP MCP.
- REST API.
- UI.
- SPARQL endpoint.
- Akoma Ntoso export.
- schema.org output.
- Person modeling.
- Legal interpretation.
- Public production URIs or official certification claims.
- Full SCIJ raw collection ingestion.

## Future lane - broader SCIJ corpus expansion

After the functional Demo, Plaza may expand from the approved Demo set toward a broader SCIJ raw-backed corpus. That expansion must reuse the same evidence, provenance, validation, and URI discipline rather than importing unsafe legacy canonical IDs or article structure.

## Release exit criteria

- `demo/ops/DEMO_ACCEPTANCE_CONTRACT.md` passes in full.
- The approved real legal-resource set is represented.
- SHACL report conforms from a real SHACL run.
- MCP tools/resources are implemented and citation-complete.
- Claude Desktop local stdio smoke test passes.
