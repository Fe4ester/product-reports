from __future__ import annotations

from collections import defaultdict
from typing import Any, DefaultDict, Dict, List

from .base import Report
from .registry import register_report


class AverageRatingReport(Report):
    # считает средний рейтинг по брендам и сортирует по убыванию рейтинга, при равенстве по названию бренда
    def generate(self, rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        sums: DefaultDict[str, float] = defaultdict(float)
        counts: DefaultDict[str, int] = defaultdict(int)

        for r in rows:
            brand = str(r.get("brand", "")).strip()
            if not brand:
                continue
            rating = float(r.get("rating", 0.0))
            sums[brand] += rating
            counts[brand] += 1

        result: List[Dict[str, Any]] = []
        for brand, total in sums.items():
            cnt = counts[brand]
            avg = total / cnt if cnt else 0.0
            result.append({"brand": brand, "average_rating": avg})

        result.sort(key=lambda d: (-d["average_rating"], d["brand"]))
        return result


# регистрация отчета
register_report("average-rating", AverageRatingReport)
