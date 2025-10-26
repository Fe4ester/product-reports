from __future__ import annotations

from pathlib import Path

from brand_reports.cli import main


def test_cli_unknown_report_returns_error_and_prints_help(tmp_path: Path, capsys):
    # создаем валидный пустой csv чтобы пройти валидацию файлов
    f = tmp_path / "a.csv"
    f.write_text("name,brand,price,rating\n", encoding="utf-8")

    code = main(["--files", str(f), "--report", "not-existing"])
    captured = capsys.readouterr()

    assert code == 2
    assert "unknown report" in captured.err
    assert "usage:" in captured.err.lower()
