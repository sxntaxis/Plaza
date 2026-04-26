from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from plaza.core.identity import is_demo_eli_uri
from plaza.core.signals import list_open_blockers
from plaza.core.validation import load_validation_report


@dataclass(frozen=True)
class CandidateEntity:
    entity_ref: str
    demo_uri: str
    source_id: str
    artifact_ref: str | None
    provenance: dict | None
    relations: list[tuple[str, str, str]]


@dataclass(frozen=True)
class PublicationDecision:
    allowed: bool
    reasons: list[str]


def evaluate_candidate(
    candidate: CandidateEntity,
    *,
    sources_path: Path | str = Path("registry/sources.yml"),
    signal_store_path: Path | str = Path("var/signals/signals.jsonl"),
    validation_report_path: Path | str | None = None,
) -> PublicationDecision:
    reasons: list[str] = []
    if not is_demo_eli_uri(candidate.demo_uri):
        reasons.append("invalid_demo_uri")
    if not source_enabled(candidate.source_id, Path(sources_path)):
        reasons.append("source_not_enabled")
    if not _valid_artifact_ref(candidate.artifact_ref):
        reasons.append("missing_artifact_ref")
    if not candidate.provenance:
        reasons.append("missing_provenance")
    if _uses_applies_for_demo_relation(candidate.relations):
        reasons.append("invalid_law_decree_relation")
    if list_open_blockers(candidate.entity_ref, store_path=signal_store_path):
        reasons.append("open_blocker_issue")
    if validation_report_path is not None and not load_validation_report(validation_report_path).conforms:
        reasons.append("validation_not_conforming")
    return PublicationDecision(allowed=not reasons, reasons=reasons)


def source_enabled(source_id: str, sources_path: Path) -> bool:
    if not sources_path.exists():
        return False
    lines = sources_path.read_text(encoding="utf-8").splitlines()
    in_source = False
    for line in lines:
        stripped = line.strip()
        if line.startswith("  ") and stripped == f"{source_id}:":
            in_source = True
            continue
        if in_source and line.startswith("  ") and stripped.endswith(":") and stripped != f"{source_id}:":
            return False
        if in_source and stripped == "demo_enabled: true":
            return True
    return False


def _valid_artifact_ref(artifact_ref: str | None) -> bool:
    return bool(artifact_ref and artifact_ref.startswith("sha256:") and len(artifact_ref) == 71)


def _uses_applies_for_demo_relation(relations: list[tuple[str, str, str]]) -> bool:
    for _subject, predicate, _object in relations:
        if predicate in {"eli:applies", "http://data.europa.eu/eli/ontology#applies"}:
            return True
    return False
