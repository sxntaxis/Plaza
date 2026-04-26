from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from plaza.core.validation import load_validation_report


@dataclass(frozen=True)
class McpReadiness:
    startable: bool
    reason: str | None = None


def check_mcp_startable(
    graph_path: Path | str = Path("data/demo/canonical/demo.ttl"),
    validation_report_path: Path | str = Path("data/demo/validation/validation_report.json"),
) -> McpReadiness:
    if not Path(graph_path).exists():
        return McpReadiness(False, "demo_graph_missing")
    report = load_validation_report(validation_report_path)
    if not report.path.exists():
        return McpReadiness(False, "validation_report_missing")
    if not report.conforms:
        return McpReadiness(False, "validation_gate_failed")
    return McpReadiness(True)
