from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
import json
from pathlib import Path
from uuid import uuid4


DEFAULT_SIGNAL_PATH = Path("var/signals/signals.jsonl")
SEVERITIES = {"debug", "info", "warning", "blocker"}
STAGES = {"acquisition", "refinement", "reconciliation", "canonicalization", "validation", "mcp"}


@dataclass(frozen=True)
class Signal:
    signal_id: str
    signal_family: str
    type: str
    severity: str
    status: str
    stage: str
    source_id: str | None
    run_id: str
    entity_ref: str | None
    artifact_ref: str | None
    message: str
    details: dict = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
    resolved_at: str | None = None


def emit_event(
    type: str,
    stage: str,
    run_id: str,
    message: str,
    *,
    severity: str = "info",
    source_id: str | None = None,
    entity_ref: str | None = None,
    artifact_ref: str | None = None,
    details: dict | None = None,
    store_path: Path | str = DEFAULT_SIGNAL_PATH,
) -> Signal:
    signal = _make_signal(
        signal_family="event",
        type=type,
        severity=severity,
        status="recorded",
        stage=stage,
        source_id=source_id,
        run_id=run_id,
        entity_ref=entity_ref,
        artifact_ref=artifact_ref,
        message=message,
        details=details or {},
    )
    _append(signal, Path(store_path))
    return signal


def emit_issue(
    type: str,
    severity: str,
    stage: str,
    run_id: str,
    message: str,
    *,
    source_id: str | None = None,
    entity_ref: str | None = None,
    artifact_ref: str | None = None,
    details: dict | None = None,
    store_path: Path | str = DEFAULT_SIGNAL_PATH,
) -> Signal:
    signal = _make_signal(
        signal_family="issue",
        type=type,
        severity=severity,
        status="open",
        stage=stage,
        source_id=source_id,
        run_id=run_id,
        entity_ref=entity_ref,
        artifact_ref=artifact_ref,
        message=message,
        details=details or {},
    )
    _append(signal, Path(store_path))
    return signal


def list_open_blockers(entity_ref: str | None = None, *, store_path: Path | str = DEFAULT_SIGNAL_PATH) -> list[Signal]:
    blockers = []
    for signal in _read_all(Path(store_path)):
        if signal.signal_family != "issue" or signal.severity != "blocker" or signal.status != "open":
            continue
        if entity_ref is not None and signal.entity_ref != entity_ref:
            continue
        blockers.append(signal)
    return blockers


def resolve_issue(signal_id: str, *, store_path: Path | str = DEFAULT_SIGNAL_PATH) -> Signal:
    path = Path(store_path)
    signals = _read_all(path)
    resolved: Signal | None = None
    updated = []
    for signal in signals:
        if signal.signal_id == signal_id:
            resolved = Signal(**{**asdict(signal), "status": "resolved", "resolved_at": datetime.now(UTC).isoformat()})
            updated.append(resolved)
        else:
            updated.append(signal)
    if resolved is None:
        raise KeyError(f"issue not found: {signal_id}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(asdict(signal), sort_keys=True) + "\n" for signal in updated), encoding="utf-8")
    return resolved


def _make_signal(**kwargs: object) -> Signal:
    if kwargs["severity"] not in SEVERITIES:
        raise ValueError(f"invalid severity: {kwargs['severity']}")
    if kwargs["stage"] not in STAGES:
        raise ValueError(f"invalid stage: {kwargs['stage']}")
    return Signal(signal_id=f"sig_{uuid4().hex}", **kwargs)  # type: ignore[arg-type]


def _append(signal: Signal, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(asdict(signal), sort_keys=True) + "\n")


def _read_all(path: Path) -> list[Signal]:
    if not path.exists():
        return []
    signals = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            signals.append(Signal(**json.loads(line)))
    return signals
