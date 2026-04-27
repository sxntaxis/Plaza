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

## Next target

Functional local MCP Demo.

See `demo/ops/DEMO_PHASE1_SELECTION_SUMMARY.md`, `demo/ops/DEMO_ROADMAP.md`, and `demo/ops/DEMO_ACCEPTANCE_CONTRACT.md`.

## Active contracts

- `demo/specs/STANDARDS_IMPLEMENTATION_PROFILE.md`
- `demo/specs/MCP_IMPLEMENTATION_PROFILE.md`
- `demo/specs/STATE_AND_SIGNALS.md`
- `demo/ops/DEMO_PHASE1_SELECTION_SUMMARY.md`
- `demo/ops/DEMO_ROADMAP.md`
- `demo/ops/DEMO_ACCEPTANCE_CONTRACT.md`
