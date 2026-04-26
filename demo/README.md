# Plaza Demo Workspace

## Purpose

This directory contains the Demo-specific workspace. Foundational Plaza documents remain in `docs/`.

The Demo target is a local, deterministic graph at `data/demo/canonical/demo.ttl`, validated into `data/demo/validation/validation_report.json`, and exposed only through a local read-only MCP surface.

## Structure

- `specs/` - active Demo implementation contracts.
- `ops/` - build sequence, runbooks, checklists, release boundaries, and acceptance contracts.
- `research/` - source research, audits, inventories, and preserved background material.

## Current release boundary

`0.4.0` - Demo scaffold baseline.

See `demo/ops/0.4.0_COMMIT_BOUNDARY.md`.

## Next target

`0.5.0` - Functional local MCP Demo.

See `demo/ops/0.5.0_DEMO_ROADMAP.md` and `demo/ops/0.5.0_ACCEPTANCE_CONTRACT.md`.

## Active contracts

- `demo/specs/STANDARDS_IMPLEMENTATION_PROFILE.md`
- `demo/specs/MCP_IMPLEMENTATION_PROFILE.md`
- `demo/specs/STATE_AND_SIGNALS.md`
- `demo/ops/0.4.0_COMMIT_BOUNDARY.md`
- `demo/ops/0.5.0_DEMO_ROADMAP.md`
- `demo/ops/0.5.0_ACCEPTANCE_CONTRACT.md`
