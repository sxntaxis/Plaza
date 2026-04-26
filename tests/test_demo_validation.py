import json

from plaza.core.validation import load_validation_report
from plaza.demo.validate_graph import validate_demo_graph


def test_validation_report_required_before_mcp_starts(tmp_path):
    missing = tmp_path / "missing.json"

    report = load_validation_report(missing)

    assert not report.conforms
    assert report.data["error"] == "validation_report_missing"


def test_validate_demo_graph_writes_conforming_report(tmp_path):
    graph = tmp_path / "demo.ttl"
    graph.write_text(
        "https://demo.plaza.cr/eli/ eli:based_on eli:basis_for prov:wasDerivedFrom",
        encoding="utf-8",
    )
    report_path = tmp_path / "validation_report.json"

    report = validate_demo_graph(graph, report_path)

    assert report["conforms"]
    assert json.loads(report_path.read_text(encoding="utf-8"))["conforms"]
