from __future__ import annotations

from typing import Dict, List, Type

from .base import Report

# глобальный реестр отчетов по имени
REPORT_REGISTRY: Dict[str, Type[Report]] = {}


def register_report(name: str, cls: Type[Report]) -> None:
    # регистрация нового отчета
    key = name.strip().lower()
    if not key:
        raise ValueError("report name cannot be empty")
    if key in REPORT_REGISTRY:
        raise ValueError(f"report already registered: {key}")
    REPORT_REGISTRY[key] = cls


def get_report(name: str) -> Report:
    # получить экземпляр отчета по имени
    key = str(name).strip().lower()
    cls = REPORT_REGISTRY.get(key)
    if cls is None:
        raise KeyError(key)
    return cls()


def list_reports() -> List[str]:
    # доступные имена отчетов
    return sorted(REPORT_REGISTRY.keys())