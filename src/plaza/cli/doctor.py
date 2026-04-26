from __future__ import annotations

from pathlib import Path

from plaza.core.publication import source_enabled
from plaza.core.signals import list_open_blockers
from plaza.core.validation import load_validation_report
from plaza.mcp.guards import check_mcp_startable


def demo_status(root: Path = Path(".")) -> dict[str, object]:
    graph_path = root / "data/demo/canonical/demo.ttl"
    validation_path = root / "data/demo/validation/validation_report.json"
    sources_path = root / "registry/sources.yml"
    artifacts_path = root / "var/artifacts"
    signal_store_path = root / "var/signals/signals.jsonl"
    graph_text = graph_path.read_text(encoding="utf-8") if graph_path.exists() else ""
    report = load_validation_report(validation_path)
    readiness = check_mcp_startable(graph_path, validation_path)
    return {
        "demo_graph_path": graph_path,
        "demo_graph_present": graph_path.exists(),
        "validation_report_path": validation_path,
        "validation_report_present": validation_path.exists(),
        "validation_conforms": report.conforms,
        "sources_enabled": source_enabled("scij", sources_path),
        "artifacts_available_count": _artifact_count(artifacts_path),
        "open_blocker_issues_count": len(list_open_blockers(store_path=signal_store_path)),
        "canonical_demo_resources_count": graph_text.count("a eli:LegalResource"),
        "demo_uri_audit": "pass" if _demo_uri_audit_passes(graph_text) else "fail",
        "basis_relation_audit": "pass" if _basis_relation_audit_passes(graph_text) else "fail",
        "mcp_startable": readiness.startable,
    }


def print_demo_status(root: Path = Path(".")) -> None:
    status = demo_status(root)
    print(f"Demo graph path: {status['demo_graph_path']}")
    print(f"Demo graph present: {_yes_no(status['demo_graph_present'])}")
    print(f"Validation report path: {status['validation_report_path']}")
    print(f"Validation report present: {_yes_no(status['validation_report_present'])}")
    print(f"Validation conforms: {_yes_no(status['validation_conforms'])}")
    print(f"Sources enabled: {_yes_no(status['sources_enabled'])}")
    print(f"Artifacts available count: {status['artifacts_available_count']}")
    print(f"Open blocker issues count: {status['open_blocker_issues_count']}")
    print(f"Canonical demo resources count: {status['canonical_demo_resources_count']}")
    print(f"Demo URI audit: {status['demo_uri_audit']}")
    print(f"Basis relation audit: {status['basis_relation_audit']}")
    print(f"MCP startable: {_yes_no(status['mcp_startable'])}")


def _artifact_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for child in path.rglob("*") if child.is_file())


def _yes_no(value: object) -> str:
    return "yes" if value else "no"


def _demo_uri_audit_passes(graph_text: str) -> bool:
    legacy_legal_scheme = "plaza-demo://" + "eli"
    return "https://demo.plaza.cr/eli/" in graph_text and legacy_legal_scheme not in graph_text


def _basis_relation_audit_passes(graph_text: str) -> bool:
    return "eli:based_on" in graph_text and "eli:basis_for" in graph_text and "eli:applies" not in graph_text
