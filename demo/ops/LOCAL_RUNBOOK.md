# Plaza Demo - Local Runbook

Build the Demo graph:

```bash
python -m plaza.demo.build_graph
```

Run validation:

```bash
python -m plaza.demo.validate_graph
```

Run diagnostics:

```bash
plaza doctor demo
```

Start the local MCP guard:

```bash
python -m plaza.mcp.server
```

Runtime files belong in `var/`, which is gitignored.
