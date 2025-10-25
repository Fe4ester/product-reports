from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Dict, List, Sequence


def _convert_row(raw: Dict[str, str]) -> Dict[str, Any]:
    # приведение типов и нормализация значений
    name = raw.get("name", "").strip()
    brand = raw.get("brand", "").strip()
    price_str = raw.get("price", "").strip()
    rating_str = raw.get("rating", "").strip()

    # csv валидный по условию, поэтому без сложной валидации
    price = float(price_str)
    rating = float(rating_str)

    return {"name": name, "brand": brand, "price": price, "rating": rating}


def read_csv_rows(files: Sequence[str | Path]) -> List[Dict[str, Any]]:
    # читает несколько csv и объединяет строки
    result: List[Dict[str, Any]] = []
    for path_like in files:
        path = Path(path_like)
        # если файла нет, будет FileNotFoundError что ожидаемо для вызывающей стороны
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                result.append(_convert_row(row))
    return result
