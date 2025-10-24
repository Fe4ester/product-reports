from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brand-report",
    )
    parser.add_argument(
        "--files",
        nargs="+",
    )
    parser.add_argument(
        "--report",
    )
    return parser


def main() -> None:
    parser = build_parser()
    parser.print_help()


if __name__ == "__main__":
    main()
