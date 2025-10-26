from __future__ import annotations

import pytest

from brand_reports.reports.base import Report
from brand_reports.reports.registry import REPORT_REGISTRY, get_report, list_reports, register_report


class _DummyReport(Report):
    # тестовый отчет для реестра
    def generate(self, rows):
        return []


def test_register_and_get_report_isolated():
    REPORT_REGISTRY.clear()  # изоляция состояния реестра
    register_report("dummy", _DummyReport)
    assert "dummy" in list_reports()
    inst = get_report("dummy")
    assert isinstance(inst, _DummyReport)


def test_register_duplicate_raises():
    REPORT_REGISTRY.clear()
    register_report("dummy", _DummyReport)
    with pytest.raises(ValueError):
        register_report("dummy", _DummyReport)


def test_get_unknown_report_raises():
    REPORT_REGISTRY.clear()
    with pytest.raises(KeyError):
        get_report("missing")
