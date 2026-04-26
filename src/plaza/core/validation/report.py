from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class ValidationReport:
    conforms: bool
    path: Path
    data: dict


def load_validation_report(path: Path | str = Path("data/demo/validation/validation_report.json")) -> ValidationReport:
    report_path = Path(path)
    if not report_path.exists():
        return ValidationReport(conforms=False, path=report_path, data={"error": "validation_report_missing"})
    data = json.loads(report_path.read_text(encoding="utf-8"))
    return ValidationReport(conforms=bool(data.get("conforms")), path=report_path, data=data)
