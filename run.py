"""
save-env — command-line tool that scans public GitHub `.env` files for
exposed OpenAI API keys, verifies them, and warns the affected repositories.

Usage:
    python run.py scan                 # run a single scan and print the results
    python run.py scan -i 3600         # keep scanning every 3600 seconds
    python run.py stats                # print statistics from the last scan
"""

import argparse
import logging
import sys
import time

from app.crawler.statistics import get_stat


def format_stats():
    """Render the current statistics as plain text for stdout."""
    scan_time, total_found, last_found, total_compromised, last_compromised = get_stat()
    return (
        "Scan results:\n"
        f"  Total keys checked:   {total_found}\n"
        f"  New keys checked:     {last_found}\n"
        f"  Total compromised:    {total_compromised}\n"
        f"  New compromised:      {last_compromised}\n"
        f"  Last scan:            {scan_time}"
    )


def cmd_scan(args):
    # Imported lazily so `stats` and `--help` don't require the scraping stack.
    from app.crawler.scanner import start_scan

    if args.interval:
        logging.info("Continuous scan every %ss — press Ctrl+C to stop.", args.interval)
        while True:
            start_scan()
            print(format_stats())
            print(f"\nNext scan in {args.interval}s...\n")
            time.sleep(args.interval)
    else:
        start_scan()
        print(format_stats())


def cmd_stats(args):
    print(format_stats())


def build_parser():
    parser = argparse.ArgumentParser(
        prog="save-env",
        description="Scan public GitHub .env files for exposed OpenAI API keys, "
                    "verify them, and warn the affected repositories.",
    )
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="enable debug logging")

    sub = parser.add_subparsers(dest="command", required=True)

    p_scan = sub.add_parser("scan", help="scan GitHub for exposed keys")
    p_scan.add_argument("-i", "--interval", type=int, metavar="SECONDS",
                        help="repeat the scan every SECONDS "
                             "(default: run once and exit)")
    p_scan.set_defaults(func=cmd_scan)

    p_stats = sub.add_parser("stats", help="print statistics from the last scan")
    p_stats.set_defaults(func=cmd_stats)

    return parser


def main():
    args = build_parser().parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    try:
        args.func(args)
    except KeyboardInterrupt:
        print("\nExit")
        sys.exit(0)


if __name__ == "__main__":
    main()
