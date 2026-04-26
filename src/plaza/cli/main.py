from __future__ import annotations

import argparse

from .doctor import print_demo_status


def main() -> int:
    parser = argparse.ArgumentParser(prog="plaza")
    subparsers = parser.add_subparsers(dest="command")
    doctor = subparsers.add_parser("doctor")
    doctor.add_argument("target", choices=["demo"])
    args = parser.parse_args()
    if args.command == "doctor" and args.target == "demo":
        print_demo_status()
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
