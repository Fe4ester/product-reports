from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from tabulate import tabulate

# импорт для регистрации отчетов
import brand_reports.reports  # noqa: F401
from src.brand_reports.reports.registry import get_report, list_reports
from src.brand_reports.utils.csv_reader import read_csv_rows


def build_parser() -> argparse.ArgumentParser:
    # базовый cli парсер
    parser = argparse.ArgumentParser(
        prog="brand-report",
        description="generate brand reports from csv files",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        metavar="FILE",
        help="paths to csv files",
    )
    parser.add_argument(
        "--report",
        metavar="NAME",
        help="report name, e.g. average-rating",
    )
    return parser


def _validate_args(args: argparse.Namespace) -> None:
    # валидация наличия параметров
    if not args.files:
        raise ValueError("error: --files is required")
    if not args.report:
        raise ValueError("error: --report is required")
    # проверка существования файлов
    missing = [p for p in args.files if not Path(p).is_file()]
    if missing:
        raise ValueError(f"error: files not found: {', '.join(missing)}")


def main(argv: Sequence[str] | None = None) -> int:
    # точка входа cli
    parser = build_parser()
    args = parser.parse_args(args=argv)

    try:
        _validate_args(args)
    except ValueError as e:
        # печатаем ошибку и help чтобы было удобно исправить ввод
        print(str(e), file=sys.stderr)
        parser.print_help(sys.stderr)
        return 2

    # проверка существования отчета в реестре
    try:
        report = get_report(args.report)
    except KeyError:
        available = list_reports()
        available_str = ", ".join(available) if available else "<none>"
        print(
            f"error: unknown report '{args.report}', available reports: {available_str}",
            file=sys.stderr,
        )
        parser.print_help(sys.stderr)
        return 2

    # чтение данных и генерация отчета
    rows = read_csv_rows(args.files)
    data = report.generate(rows)

    # вывод таблицы
    headers = ["brand", "average_rating"]
    table_rows = [[d["brand"], f"{float(d['average_rating']):.2f}"] for d in data]
    print(tabulate(table_rows, headers=headers, tablefmt="github"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
