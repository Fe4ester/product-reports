from __future__ import annotations

from pathlib import Path

from brand_reports.cli import main


def test_cli_success_prints_table(tmp_path: Path, capsys):
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

    code = main(["--files", str(f1), str(f2), "--report", "average-rating"])
    captured = capsys.readouterr()

    assert code == 0
    assert "brand" in captured.out.lower()
    assert "average_rating" in captured.out
    assert "apple" in captured.out
    assert "samsung" in captured.out
    assert "xiaomi" in captured.out