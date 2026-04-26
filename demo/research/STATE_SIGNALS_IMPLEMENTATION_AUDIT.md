# State/Signals Implementation Audit

## Summary

Cleaned and hardened the Demo state/signals scaffold added in the first implementation pass. The scaffold now has gitignore coverage for local runtime and generated Python artifacts, stronger publication checks, MCP fail-closed checks, and focused tests for the state/signals base.

This audit did not inspect, move, or delete `archive/`. It remains outside the scaffold and is ignored by `.gitignore`.

## Files Created Or Modified

Created during the scaffold pass, then relocated to `demo/`:

- `demo/` contracts and preserved research under `demo/research/`
- `registry/sources.yml`
- `schemas/*.json`
- `ontology/*.ttl`
- `data/demo/canonical/demo.ttl`
- `data/demo/validation/validation_report.json`
- `src/plaza/**`
- `tests/**`
- `pyproject.toml`
- `.gitignore`

Hardened during this audit:

- `.gitignore`
- `docs/DATA_MODEL.md`
- `demo/ops/ACCEPTANCE_CHECKLIST.md`
- `demo/specs/STANDARDS_IMPLEMENTATION_PROFILE.md`
- `demo/specs/STATE_AND_SIGNALS.md`
- `src/plaza/core/publication/gate.py`
- `src/plaza/cli/doctor.py`
- `tests/test_publication_gate.py`
- `tests/test_doctor.py`
- `tests/test_unittest_discovery.py`
- `tests/run_tests.py`

## Cleanup Performed

- Removed generated Python cache directories and `.pyc` files outside `archive/`.
- Added `.gitignore` entries for `var/`, `archive/`, Python bytecode, pytest cache, virtualenvs, SQLite, and DB files.
- Confirmed no root-level `research/` or `profiles/` directory remains.
- Confirmed active Demo graph uses `https://demo.plaza.cr/eli/...` legal-resource URIs.
- Confirmed active Demo graph uses `eli:basis_for` and `eli:based_on` for the law-decree relation.
- Patched the foundational data model so reglamentation no longer defaults to `eli:applies`.

## Verification Commands

Commands run during cleanup and verification:

```bash
git status --short
find src -type d -name "__pycache__" -o -name "*.pyc"
grep -R "plaza-demo://eli" -n docs src data ontology schemas --exclude-dir="__pycache__" || true
grep -R "eli:applies" -n docs src data ontology schemas --exclude-dir="__pycache__" || true
grep -R "eli:based_on\|eli:basis_for" -n docs src data ontology schemas --exclude-dir="__pycache__" || true
PYTHONPATH=src python -m plaza.demo.validate_graph
PYTHONPATH=src python -m plaza.cli.main doctor demo
PYTHONPATH=src python -m plaza.mcp.server
python tests/run_tests.py
PYTHONPATH=src python -m unittest discover -s tests
```

MCP fail-closed simulations were run by temporarily removing `data/demo/validation/validation_report.json` and by temporarily setting `conforms=false`. Both cases failed closed, and the conforming report was restored.

## Test Results

- `python tests/run_tests.py`: 15 tests passed.
- `PYTHONPATH=src python -m unittest discover -s tests`: unittest wrapper passed and executed the scaffold test runner.
- `PYTHONPATH=src python -m plaza.demo.validate_graph`: validation conforms.
- `PYTHONPATH=src python -m plaza.cli.main doctor demo`: validation conforms, blockers 0, MCP startable yes.
- `PYTHONPATH=src python -m plaza.mcp.server`: local read-only guard starts only when validation conforms.

## Remaining Gaps

- This is state/signals scaffolding, not a full Plaza Demo implementation.
- The Demo graph is a small committed scaffold graph, not a complete real acquisition/reconciliation output.
- MCP currently has a fail-closed startup guard and placeholder read-only modules; full MCP tools/resources are not implemented.
- The publication gate is a simple candidate-level gate. It checks source enablement, Demo URI, artifact hash reference, provenance, open blockers, optional validation report, and the law-decree relation anti-pattern, but it is not yet a full canonical graph writer.
- Validation is a lightweight scaffold validator over the Demo graph text, not a full SHACL engine integration.

## Commit Readiness

Ready to commit as a Demo state/signals scaffold if the project accepts the remaining gaps above. The full Demo is not ready.
