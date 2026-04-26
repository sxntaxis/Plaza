from plaza.core.publication import CandidateEntity, evaluate_candidate
from plaza.core.signals import emit_issue


def test_blocker_issue_prevents_canonicalization(tmp_path):
    signals = tmp_path / "signals.jsonl"
    sources = tmp_path / "sources.yml"
    sources.write_text("sources:\n  scij:\n    demo_enabled: true\n", encoding="utf-8")
    candidate = CandidateEntity(
        entity_ref="entity_1",
        demo_uri="https://demo.plaza.cr/eli/cr/asamblea/1988/ley/7092",
        source_id="scij",
        artifact_ref="sha256:" + "a" * 64,
        provenance={"source": "scij"},
        relations=[],
    )
    emit_issue(
        "canonicalization_blocker",
        "blocker",
        "canonicalization",
        "run_1",
        "Blocked",
        entity_ref="entity_1",
        store_path=signals,
    )

    decision = evaluate_candidate(candidate, sources_path=sources, signal_store_path=signals)

    assert not decision.allowed
    assert "open_blocker_issue" in decision.reasons


def test_demo_uri_validation(tmp_path):
    sources = tmp_path / "sources.yml"
    sources.write_text("sources:\n  scij:\n    demo_enabled: true\n", encoding="utf-8")
    candidate = CandidateEntity(
        entity_ref="entity_1",
        demo_uri="plaza-demo://" + "eli/cr/asamblea/1988/ley/7092",
        source_id="scij",
        artifact_ref="sha256:" + "a" * 64,
        provenance={"source": "scij"},
        relations=[],
    )

    decision = evaluate_candidate(candidate, sources_path=sources, signal_store_path=tmp_path / "signals.jsonl")

    assert not decision.allowed
    assert "invalid_demo_uri" in decision.reasons


def test_demo_uri_accepted_for_legal_resource(tmp_path):
    sources = tmp_path / "sources.yml"
    sources.write_text("sources:\n  scij:\n    demo_enabled: true\n", encoding="utf-8")
    candidate = CandidateEntity(
        entity_ref="entity_1",
        demo_uri="https://demo.plaza.cr/eli/cr/asamblea/1988/ley/7092",
        source_id="scij",
        artifact_ref="sha256:" + "a" * 64,
        provenance={"source": "scij"},
        relations=[("law", "eli:basis_for", "decree"), ("decree", "eli:based_on", "law")],
    )

    decision = evaluate_candidate(candidate, sources_path=sources, signal_store_path=tmp_path / "signals.jsonl")

    assert decision.allowed


def test_publication_blocks_disabled_source_invalid_artifact_and_validation_failure(tmp_path):
    sources = tmp_path / "sources.yml"
    report = tmp_path / "validation_report.json"
    sources.write_text("sources:\n  scij:\n    demo_enabled: false\n", encoding="utf-8")
    report.write_text('{"conforms": false}', encoding="utf-8")
    candidate = CandidateEntity(
        entity_ref="entity_1",
        demo_uri="https://demo.plaza.cr/eli/cr/asamblea/1988/ley/7092",
        source_id="scij",
        artifact_ref="sha256:not-a-real-hash",
        provenance={"source": "scij"},
        relations=[],
    )

    decision = evaluate_candidate(
        candidate,
        sources_path=sources,
        signal_store_path=tmp_path / "signals.jsonl",
        validation_report_path=report,
    )

    assert "source_not_enabled" in decision.reasons
    assert "missing_artifact_ref" in decision.reasons
    assert "validation_not_conforming" in decision.reasons


def test_publication_blocks_applies_as_demo_relation(tmp_path):
    sources = tmp_path / "sources.yml"
    sources.write_text("sources:\n  scij:\n    demo_enabled: true\n", encoding="utf-8")
    candidate = CandidateEntity(
        entity_ref="entity_1",
        demo_uri="https://demo.plaza.cr/eli/cr/asamblea/1988/ley/7092",
        source_id="scij",
        artifact_ref="sha256:" + "a" * 64,
        provenance={"source": "scij"},
        relations=[("decree", "eli:applies", "law")],
    )

    decision = evaluate_candidate(candidate, sources_path=sources, signal_store_path=tmp_path / "signals.jsonl")

    assert "invalid_law_decree_relation" in decision.reasons
