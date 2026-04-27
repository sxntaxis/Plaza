from __future__ import annotations

import importlib
import inspect
from pathlib import Path
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))


MODULES = [
    "tests.test_artifacts",
    "tests.test_demo_graph",
    "tests.test_demo_candidate_manifest",
    "tests.test_demo_validation",
    "tests.test_doctor",
    "tests.test_mcp_demo",
    "tests.test_publication_gate",
    "tests.test_signals",
]


def main() -> int:
    total = 0
    for module_name in MODULES:
        module = importlib.import_module(module_name)
        for name, func in inspect.getmembers(module, inspect.isfunction):
            if not name.startswith("test_"):
                continue
            total += 1
            params = inspect.signature(func).parameters
            if "tmp_path" in params:
                with tempfile.TemporaryDirectory() as directory:
                    func(Path(directory))
            else:
                func()
    print(f"{total} tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
