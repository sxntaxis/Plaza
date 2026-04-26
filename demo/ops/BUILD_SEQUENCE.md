# Plaza Demo - Build Sequence

1. Keep foundational docs in `docs/` and Demo contracts in `demo/specs/`.
2. Preserve ungraduated Demo research in `demo/research/`.
3. Enable sources in `registry/sources.yml`.
4. Acquire raw artifacts using an artifact envelope with a `sha256:` hash.
5. Emit events and durable issues through the signal spine.
6. Reconcile candidate legal resources to `https://demo.plaza.cr/eli/...` URIs.
7. Run the publication gate before writing `data/demo/canonical/demo.ttl`.
8. Validate the graph and write `data/demo/validation/validation_report.json`.
9. Start the local stdio MCP server only if validation conforms.
10. Check readiness with `plaza doctor demo`.

Current commands:

```bash
python -m plaza.demo.build_graph
python -m plaza.demo.validate_graph
plaza doctor demo
python -m plaza.mcp.server
```
