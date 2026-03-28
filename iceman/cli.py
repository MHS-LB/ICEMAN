import argparse
import sys

from iceman import __version__


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="iceman",
        description="ICEMAN CLI tool",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # Placeholder subcommand — replace with real ones
    run_parser = subparsers.add_parser("run", help="Run ICEMAN")
    run_parser.add_argument("args", nargs="*", help="Arguments")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "run":
        print("ICEMAN is running.")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
