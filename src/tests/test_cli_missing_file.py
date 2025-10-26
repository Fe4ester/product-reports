from __future__ import annotations

from pathlib import Path

from brand_reports.cli import main


def test_cli_missing_file_returns_error_and_help(tmp_path: Path, capsys):
    exists = tmp_path / "a.csv"
    missing = tmp_path / "missing.csv"
    exists.write_text("name,brand,price,rating\n", encoding="utf-8")

    code = main(["--files", str(exists), str(missing), "--report", "average-rating"])
    captured = capsys.readouterr()

    assert code == 2
    assert "files not found" in captured.err
    assert "usage:" in captured.err.lower()
