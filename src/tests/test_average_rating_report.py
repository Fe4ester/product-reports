from __future__ import annotations

from brand_reports.reports.average_rating import AverageRatingReport


def test_average_rating_computation_and_sorting():
    rows = [
        {"name": "a1", "brand": "apple", "price": 1000.0, "rating": 4.9},
        {"name": "a2", "brand": "apple", "price": 900.0, "rating": 3.9},
        {"name": "s1", "brand": "samsung", "price": 1200.0, "rating": 4.8},
        {"name": "x1", "brand": "xiaomi", "price": 200.0, "rating": 4.6},
        {"name": "x2", "brand": "xiaomi", "price": 220.0, "rating": 4.6},
    ]

    report = AverageRatingReport()
    out = report.generate(rows)

    # ожидаемые средние: apple=4.4, samsung=4.8, xiaomi=4.6
    expected = {
        "apple": 4.4,
        "samsung": 4.8,
        "xiaomi": 4.6,
    }
    assert {d["brand"]: round(float(d["average_rating"]), 2) for d in out} == expected

    # сортировка по среднему убыванию, при равенстве по бренду
    brands_sorted = [d["brand"] for d in out]
    assert brands_sorted == ["samsung", "xiaomi", "apple"]
