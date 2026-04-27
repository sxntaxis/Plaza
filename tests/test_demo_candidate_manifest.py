import json
from pathlib import Path


MANIFEST_PATH = Path("data/demo/manifest.candidate.json")
MCP_PROFILE_PATH = Path("demo/specs/MCP_IMPLEMENTATION_PROFILE.md")


def _load_manifest():
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def test_candidate_manifest_exists_and_has_release_metadata():
    assert MANIFEST_PATH.exists()

    manifest = _load_manifest()
    assert manifest["manifest_kind"] == "demo_resource_candidate_manifest"
    assert manifest["target_milestone"] == "functional_demo"
    assert "target_release" not in manifest
    assert manifest["status"] not in {"approved", "ready"}


def test_candidate_manifest_source_documents_exist():
    manifest = _load_manifest()

    assert "demo/ops/DEMO_PHASE1_SELECTION_SUMMARY.md" in manifest["created_from"]
    for source_path in manifest["created_from"]:
        assert Path(source_path).exists()


def test_candidate_manifest_uses_only_demo_eli_uris():
    manifest = _load_manifest()

    for resource in manifest["resources"]:
        demo_uri = resource.get("demo_uri")
        if demo_uri is None:
            assert resource.get("status") == "blocker_pending"
            continue
        assert resource.get("status") != "blocker_pending" or demo_uri.startswith(
            "https://demo.plaza.cr/eli/"
        )
        legacy_scheme = "plaza-demo://" + "eli"
        assert not demo_uri.startswith(legacy_scheme)
        assert demo_uri.startswith("https://demo.plaza.cr/eli/")


def test_candidate_manifest_keeps_legacy_norm_id_diagnostic_only():
    manifest = _load_manifest()

    policy_text = json.dumps(manifest["selection_policy"], sort_keys=True)
    assert "legacy norm.id is diagnostic only" in policy_text

    for resource in manifest["resources"]:
        assert "legacy_diagnostic_label" in resource
        assert "norm.id" not in resource.get("source_identity", {})


def test_candidate_manifest_uses_minimum_useful_count_policy():
    manifest = _load_manifest()
    count_policy = manifest.get("resource_count_policy", {})

    assert count_policy.get("policy") == "minimum_useful_approved_set"
    assert "not fixed at four" in count_policy.get("description", "")

    recommended = [
        resource
        for resource in manifest["resources"]
        if resource.get("status") == "recommended"
    ]

    assert recommended
    assert count_policy.get("current_recommended_count") == len(recommended)


def test_mcp_profile_does_not_hardcode_candidate_resource_count():
    profile_text = MCP_PROFILE_PATH.read_text(encoding="utf-8")

    forbidden_count_phrases = [
        "los " + "4" + " recursos",
        "los " + "cuatro recursos",
        "4 " + "recursos",
        "cuatro recursos " + "legales reales",
        "Lista los " + "4" + " recursos",
        "length == " + "4",
        "4 entries",
        "longitud == " + "4",
    ]
    for phrase in forbidden_count_phrases:
        assert phrase not in profile_text

    assert "minimum_useful_approved_set" in _load_manifest()["resource_count_policy"]["policy"]
    assert "eli:based_on" in profile_text
    assert "eli:basis_for" in profile_text


def test_candidate_manifest_keeps_future_expansion_out_of_scope():
    manifest = _load_manifest()
    expansion_policy = manifest.get("future_expansion_policy")

    assert expansion_policy is not None
    assert expansion_policy.get("status") == "out_of_scope_for_functional_demo"
    assert "broader SCIJ raw-backed corpus" in expansion_policy.get("direction", "")
    assert expansion_policy.get("constraints")


def test_candidate_manifest_has_verified_relation_or_pending_blocker():
    manifest = _load_manifest()
    relation_status = manifest.get("relation_partner_status", {})
    relations = manifest.get("relations", [])

    if relation_status.get("status") == "verified_pending_human_approval":
        assert relations
        relation = relations[0]
        assert relation.get("predicate") == "eli:based_on"
        assert relation.get("inverse_predicate") == "eli:basis_for"
        source_evidence = relation.get("source_evidence", {})
        assert source_evidence.get("related_surface_raw_path")
        assert source_evidence.get("evidence_text")
        assert (
            source_evidence.get("related_surface_manifest_path")
            or source_evidence.get("related_surface_manifest_status")
            == "pending_phase_2_fixture_resolution"
        )
        return

    blocker_resources = [
        resource
        for resource in manifest["resources"]
        if resource.get("status") == "blocker_pending"
    ]
    assert blocker_resources

    for resource in blocker_resources:
        assert resource.get("next_action")
        assert resource.get("known_caveats")
        demo_uri = resource.get("demo_uri")
        assert demo_uri is None or demo_uri.startswith("https://demo.plaza.cr/eli/")

    for blocker in manifest.get("blockers", []):
        if blocker.get("status") == "blocker_pending":
            assert blocker.get("next_action")
            assert blocker.get("resource_candidate_id")


def test_candidate_manifest_not_final_acceptance_ready():
    manifest = _load_manifest()

    serialized = json.dumps(manifest, sort_keys=True).lower()
    assert '"status": "approved"' not in serialized
    assert '"status": "ready"' not in serialized
    assert "final demo acceptance readiness" in serialized
