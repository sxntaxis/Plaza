# Plaza Demo - Acceptance Checklist

- [ ] Foundational documents remain in `docs/`.
- [ ] Demo contracts live in `demo/specs/`.
- [ ] Demo operation notes live in `demo/ops/`.
- [ ] Demo research lives in `demo/research/`.
- [ ] No root `research/` or `profiles/` directories exist.
- [ ] Legal resources use `https://demo.plaza.cr/eli/...`.
- [ ] Legal resources do not use a legacy non-HTTP Demo URI scheme.
- [ ] The demonstrative law-decree relation uses `eli:based_on` and `eli:basis_for`.
- [ ] `registry/sources.yml` exists and enables SCIJ for Demo.
- [ ] Artifact envelopes require `content_hash`.
- [ ] Open blocker issues prevent canonicalization.
- [ ] `data/demo/canonical/demo.ttl` exists.
- [ ] `data/demo/validation/validation_report.json` exists and says `conforms=true`.
- [ ] MCP fails closed if the validation report is missing or false.
- [ ] `plaza doctor demo` reports readiness without mutating state.
