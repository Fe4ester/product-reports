from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_cli_e2e_module_run(tmp_path: Path):
    # готовим временные csv
    f1 = tmp_path / "a.csv"
    f2 = tmp_path / "b.csv"
    f1.write_text(
        "name,brand,price,rating\n"
        "iphone 15 pro,apple,999,4.9\n",
        encoding="utf-8",
    )
    f2.write_text(
        "name,brand,price,rating\n"
        "galaxy s23 ultra,samsung,1199,4.8\n"
        "redmi note 12,xiaomi,199,4.6\n",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        "-m",
        "brand_reports.cli",
        "--files",
        str(f1),
        str(f2),
        "--report",
        "average-rating",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0
    out = proc.stdout.lower()
    assert "brand" in out
    assert "average_rating" in out
    assert "apple" in out and "samsung" in out and "xiaomi" in out
