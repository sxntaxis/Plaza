from plaza.cli.doctor import demo_status


def test_doctor_reports_coherent_demo_status():
    status = demo_status()

    assert status["demo_graph_present"]
    assert status["validation_report_present"]
    assert status["validation_conforms"]
    assert status["mcp_startable"]
    assert status["open_blocker_issues_count"] == 0
    assert status["demo_uri_audit"] == "pass"
    assert status["basis_relation_audit"] == "pass"
