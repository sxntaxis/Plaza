from plaza.core.signals import emit_event, emit_issue, list_open_blockers, resolve_issue


def test_signal_creation_and_blocker_listing(tmp_path):
    store = tmp_path / "signals.jsonl"
    event = emit_event("acquired", "acquisition", "run_1", "Acquired artifact", store_path=store)
    issue = emit_issue(
        "canonicalization_blocker",
        "blocker",
        "canonicalization",
        "run_1",
        "Cannot publish",
        entity_ref="entity_1",
        store_path=store,
    )

    assert event.signal_family == "event"
    assert issue.status == "open"
    assert [signal.signal_id for signal in list_open_blockers("entity_1", store_path=store)] == [issue.signal_id]

    resolve_issue(issue.signal_id, store_path=store)
    assert list_open_blockers("entity_1", store_path=store) == []
