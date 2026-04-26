from __future__ import annotations

import json
from pathlib import Path


DEMO_GRAPH_PATH = Path("data/demo/canonical/demo.ttl")
VALIDATION_REPORT_PATH = Path("data/demo/validation/validation_report.json")
MANIFEST_PATH = Path("data/demo/manifest.json")


def load_manifest(path: Path | str = MANIFEST_PATH) -> dict:
    manifest_path = Path(path)
    if not manifest_path.exists():
        return {"resources": []}
    return json.loads(manifest_path.read_text(encoding="utf-8"))
