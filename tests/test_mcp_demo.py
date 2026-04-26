import json

from plaza.mcp.guards import check_mcp_startable


def test_mcp_fails_closed_when_validation_report_missing(tmp_path):
    graph = tmp_path / "demo.ttl"
    graph.write_text("@prefix eli: <http://data.europa.eu/eli/ontology#> .", encoding="utf-8")

    readiness = check_mcp_startable(graph, tmp_path / "missing.json")

    assert not readiness.startable
    assert readiness.reason == "validation_report_missing"


def test_mcp_fails_closed_when_validation_report_false(tmp_path):
    graph = tmp_path / "demo.ttl"
    report = tmp_path / "validation_report.json"
    graph.write_text("@prefix eli: <http://data.europa.eu/eli/ontology#> .", encoding="utf-8")
    report.write_text(json.dumps({"conforms": False}), encoding="utf-8")

    readiness = check_mcp_startable(graph, report)

    assert not readiness.startable
    assert readiness.reason == "validation_gate_failed"


def test_mcp_startable_when_validation_conforms(tmp_path):
    graph = tmp_path / "demo.ttl"
    report = tmp_path / "validation_report.json"
    graph.write_text("@prefix eli: <http://data.europa.eu/eli/ontology#> .", encoding="utf-8")
    report.write_text(json.dumps({"conforms": True}), encoding="utf-8")

    assert check_mcp_startable(graph, report).startable
