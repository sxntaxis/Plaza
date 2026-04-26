# Demo Relocation Audit

## Summary

Relocated Demo-specific documentation and research from the former nested Demo docs area into the root `demo/` workspace. Foundational project documents remain in `docs/`. Runtime data remains in `data/demo/`, and local runtime state remains in ignored `var/`.

This was a structure-only relocation. It did not rebuild the Demo, redesign state/signals, or change runtime behavior.

## Files Moved

- `demo/README.md`
- `demo/specs/STANDARDS_IMPLEMENTATION_PROFILE.md`
- `demo/specs/MCP_IMPLEMENTATION_PROFILE.md`
- `demo/specs/STATE_AND_SIGNALS.md`
- `demo/ops/BUILD_SEQUENCE.md`
- `demo/ops/ACCEPTANCE_CHECKLIST.md`
- `demo/ops/LOCAL_RUNBOOK.md`
- `demo/research/**`

The prior state/signals audit report was preserved at `demo/research/STATE_SIGNALS_IMPLEMENTATION_AUDIT.md`.

## References Updated

- Active Demo README now points to `demo/specs/`, `demo/ops/`, and `demo/research/`.
- Active state/signals spec now defines `demo/specs/`, `demo/ops/`, and `demo/research/` as the Demo documentation workspace.
- Active build sequence and acceptance checklist now reference the new root `demo/` layout.
- No live references to the old Demo docs path remain in the checked project tree outside excluded directories.

## Verification

Verification commands run:

```bash
git status --short
find docs -maxdepth 2 -type f | sort
find demo -maxdepth 3 -type f | sort
find src -type d -name "__pycache__" -o -name "*.pyc"
grep -R "docs/demo" -n . --exclude-dir=".git" --exclude-dir="archive" --exclude-dir="var" || true
grep -R "plaza-demo://eli" -n demo docs src data ontology schemas --exclude-dir="__pycache__" || true
grep -R "eli:applies" -n demo docs src data ontology schemas --exclude-dir="__pycache__" || true
grep -R "eli:based_on\|eli:basis_for" -n demo docs src data ontology schemas --exclude-dir="__pycache__" || true
PYTHONPATH=src python -m plaza.demo.validate_graph
PYTHONPATH=src python -m plaza.cli.main doctor demo
PYTHONPATH=src python -m plaza.mcp.server
python tests/run_tests.py
PYTHONPATH=src python -m unittest discover -s tests
```

Expected semantic checks remain intact: active legal-resource URIs use `https://demo.plaza.cr/eli/...`, active graph relation uses `eli:based_on` and `eli:basis_for`, and `eli:applies` appears only in explanatory, preserved research, or anti-pattern contexts.

## Remaining Gaps

- This relocation does not make the full Demo complete.
- MCP tools/resources remain scaffold-level beyond the validation startup guard.
- The Demo graph remains a small scaffold graph, not a complete acquisition/reconciliation output.
- Validation remains lightweight scaffold validation, not a full SHACL engine integration.

## Commit Readiness

Ready to commit as a documentation-structure relocation plus existing state/signals scaffold. The full Demo is not ready.
