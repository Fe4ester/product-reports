from __future__ import annotations

from pathlib import Path

import pytest

from src.brand_reports.utils.csv_reader import read_csv_rows


def _write_csv(path: Path, content: str) -> None:
    # helper для записи временных csv
    path.write_text(content, encoding="utf-8")


def test_read_single_file(tmp_path: Path) -> None:
    csv_content = (
        "name,brand,price,rating\n"
        "iphone 15 pro,apple,999,4.9\n"
        "galaxy s23 ultra,samsung,1199,4.8\n"
    )
    file1 = tmp_path / "a.csv"
    _write_csv(file1, csv_content)

    rows = read_csv_rows([file1])

    assert len(rows) == 2
    assert rows[0]["name"] == "iphone 15 pro"
    assert rows[0]["brand"] == "apple"
    assert isinstance(rows[0]["price"], float)
    assert isinstance(rows[0]["rating"], float)
    assert rows[0]["price"] == 999.0
    assert rows[0]["rating"] == 4.9


def test_read_multiple_files(tmp_path: Path) -> None:
    csv_a = (
        "name,brand,price,rating\n"
        "iphone 15 pro,apple,999,4.9\n"
    )
    csv_b = (
        "name,brand,price,rating\n"
        "redmi note 12,xiaomi,199,4.6\n"
        "galaxy s23 ultra,samsung,1199,4.8\n"
    )
    a = tmp_path / "a.csv"
    b = tmp_path / "b.csv"
    _write_csv(a, csv_a)
    _write_csv(b, csv_b)

    rows = read_csv_rows([a, b])

    assert len(rows) == 3
    brands = {r["brand"] for r in rows}
    assert brands == {"apple", "xiaomi", "samsung"}


def test_missing_file_raises(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        read_csv_rows([missing])