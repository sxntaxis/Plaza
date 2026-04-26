from __future__ import annotations

from datetime import UTC, datetime
import json
from pathlib import Path


def validate_demo_graph(
    graph_path: Path | str = Path("data/demo/canonical/demo.ttl"),
    report_path: Path | str = Path("data/demo/validation/validation_report.json"),
    shapes_path: Path | str = Path("ontology/shapes.ttl"),
) -> dict:
    graph_path = Path(graph_path)
    report_path = Path(report_path)
    text = graph_path.read_text(encoding="utf-8") if graph_path.exists() else ""
    results = []
    if not text:
        results.append({"code": "graph_missing"})
    if "https://demo.plaza.cr/eli/" not in text:
        results.append({"code": "demo_uri_missing"})
    if "eli:based_on" not in text or "eli:basis_for" not in text:
        results.append({"code": "law_decree_relation_missing"})
    if "eli:applies" in text:
        results.append({"code": "eli_applies_used_for_demo_relation"})
    if "prov:wasDerivedFrom" not in text:
        results.append({"code": "provenance_missing"})
    report = {
        "conforms": not results,
        "checked_at": datetime.now(UTC).isoformat(),
        "graph_path": str(graph_path),
        "shapes_path": str(shapes_path),
        "results": results,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main() -> int:
    report = validate_demo_graph()
    print(f"Validation conforms: {'yes' if report['conforms'] else 'no'}")
    return 0 if report["conforms"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
