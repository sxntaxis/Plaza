# Demo Phase 1 Selection Summary

## Status

candidate_pending_human_approval

## Purpose

This is the active Phase 1 selection summary for the functional local MCP Demo. It consolidates the durable resource-selection, relation-discovery, evidence-policy, and expansion-lane decisions so future implementation work does not need to read intermediate planning reports.

## Resource count policy

The Demo uses `minimum_useful_approved_set`: select the smallest approved set that proves the evidence-to-RDF-to-validation-to-MCP path without unnecessary bloat.

The current candidate set happens to contain four concrete resources, but four is not a rule.

## Recommended candidate set

Recommended resources pending human approval:

1. `constitucion_politica` - Constitucion Politica de la Republica de Costa Rica.
2. `ley_7092` - Ley del Impuesto sobre la Renta.
3. `decreto_ejecutivo_43198_h` - Decreto Ejecutivo 43198-H / Reglamento de la Ley del Impuesto sobre la Renta.
4. `ley_10790` - Ley para garantizar la transparencia en la eleccion de la Presidencia del Concejo Municipal.

Alternates:

- `ley_10791` - strong simple-law alternate.
- `ley_10788` - strong simple-law alternate.

The alternates may replace the simple-law slot, but they do not satisfy the required law-decree or law-regulation relation.

## Relation candidate

- Relation partner: Decreto Ejecutivo 43198-H / Reglamento de la Ley del Impuesto sobre la Renta.
- SCIJ source identifier: `1:95992:139872`.
- Relation status: `verified_pending_human_approval`.
- Evidence text: `Ley: 7092; Nombre: Ley del Impuesto sobre la Renta; Afectacion: Reglamentacion; Modo: Expreso`.
- Demo URI candidate: `https://demo.plaza.cr/eli/cr/poder_ejecutivo/2021/decreto_ejecutivo/43198_h`.

Modeling:

- Decreto Ejecutivo 43198-H `eli:based_on` Ley 7092.
- Ley 7092 `eli:basis_for` Decreto Ejecutivo 43198-H.

The relation still needs human approval and fixture preservation before it can be represented in the canonical Demo graph.

## Evidence policy

- SCIJ raw HTML and SCIJ manifests are source evidence once selected and preserved.
- `nValor1:nValor2:nValor3` is source identity and evidence, not Plaza canonical identity.
- Legacy `norm.id` may appear only as diagnostic metadata or in negative warnings.
- Publication hints are bibliographic evidence only.
- Legacy Gaceta segmentation is not canonical document evidence.
- Normalized text may help review, but final claims must cite preserved raw SCIJ evidence and manifest metadata.

## What is explicitly out of scope for the functional Demo

- Fixture preservation before human approval.
- MCP implementation in Phase 1.
- SHACL implementation in Phase 1.
- Parser/refinement implementation in Phase 1.
- Canonical graph replacement in Phase 1.
- Article-level canonicalization.
- Complete historical version claims.
- Gaceta segmentation as canonical evidence.
- Full SCIJ raw collection ingestion.

## Future expansion lane

The Demo starts with a small approved set so the complete path can be proven on controlled evidence. This is not a statement that Plaza should remain small.

After the functional Demo, Plaza may expand toward a broader SCIJ raw-backed corpus. That expansion must reuse the same evidence, provenance, validation, and URI discipline rather than importing unsafe legacy canonical IDs, article counts, or Gaceta segmentation.

## Human decisions required

- Approve or revise the recommended candidate set.
- Approve or reject Decreto Ejecutivo 43198-H as the relation partner for Ley 7092.
- Decide whether `constitucion_politica` stays in the Demo resource set despite historical and publication caveats.
- Decide whether `ley_10790`, `ley_10791`, or `ley_10788` fills the simple-law slot.
- Approve evidence fixture policy and committed fixture location.
- Decide whether any Gaceta PDFs are in scope as bibliographic publication fixtures.

## Phase 2 entry criteria

Phase 2 may start only after:

- Human approval of the selected concrete resources.
- Human approval of Decreto Ejecutivo 43198-H or an explicit replacement path.
- Human approval of evidence fixture policy and fixture location.

Phase 2 is evidence fixture preservation only. It is not MCP implementation, SHACL implementation, parser implementation, or graph replacement.

## Source documents

- `demo/research/source_audits/CORRECTNESS_AUDIT_REPORT.md`
- `demo/research/source_audits/INVENTORY_REPORT.md`
- `data/demo/manifest.candidate.json`
- `demo/ops/DEMO_ACCEPTANCE_CONTRACT.md`
- `demo/ops/DEMO_ROADMAP.md`
