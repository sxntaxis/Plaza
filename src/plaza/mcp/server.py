from __future__ import annotations

import sys

from .guards import check_mcp_startable


def main() -> int:
    readiness = check_mcp_startable()
    if not readiness.startable:
        print(f"MCP closed: {readiness.reason}", file=sys.stderr)
        return 1
    print("Plaza Demo MCP local stdio guard ready (read-only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
