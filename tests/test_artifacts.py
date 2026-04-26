from plaza.core.artifacts import ArtifactEnvelope


def test_artifact_envelope_hash_required():
    try:
        ArtifactEnvelope(
            artifact_id="artifact_1",
            source_id="scij",
            access_method="preserved_artifact",
            captured_at="2026-04-25T00:00:00Z",
            content_hash="",
            media_type="text/html",
            storage_path="var/artifacts/scij/demo.html",
            run_id="run_1",
            source_local_id="scij_demo",
        )
    except ValueError as exc:
        assert "content_hash" in str(exc)
    else:
        raise AssertionError("ArtifactEnvelope accepted a missing content_hash")
