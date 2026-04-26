from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArtifactEnvelope:
    artifact_id: str
    source_id: str
    access_method: str
    captured_at: str
    content_hash: str
    media_type: str
    storage_path: str
    run_id: str
    source_url: str | None = None
    source_local_id: str | None = None

    def __post_init__(self) -> None:
        if not self.content_hash.startswith("sha256:") or len(self.content_hash) != 71:
            raise ValueError("artifact envelope requires a sha256: content_hash")
        if not (self.source_url or self.source_local_id):
            raise ValueError("artifact envelope requires source_url or source_local_id")
