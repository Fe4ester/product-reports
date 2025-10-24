from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Report(ABC):
    """
    Базовый интерфейс отчёта
    """

    @abstractmethod
    def generate(self, rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Сформировать данные отчёта из строк csv"""
        raise NotImplementedError
