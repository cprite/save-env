import csv
import os


"""

GET STAT ON TOTAL AND LAST SCANNING

"""


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
STATS_PATH = os.path.join(DATA_DIR, "statistics.csv")

FIELDS = ["ScanTime", "TotalFound", "LastFound", "TotalCompromised", "LastCompromised"]

DEFAULT_STAT = {
    "ScanTime": "never",
    "TotalFound": 0,
    "LastFound": 0,
    "TotalCompromised": 0,
    "LastCompromised": 0,
}


def get_stat():
    row = DEFAULT_STAT

    if os.path.exists(STATS_PATH):
        with open(STATS_PATH, newline="") as file:
            rows = list(csv.DictReader(file))
            if rows:
                row = rows[0]

    return (
        str(row["ScanTime"]),
        str(row["TotalFound"]),
        str(row["LastFound"]),
        str(row["TotalCompromised"]),
        str(row["LastCompromised"]),
    )


def update_stat(scan_time, total_found, last_found, total_compromised, last_compromised):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(STATS_PATH, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerow({
            "ScanTime": scan_time,
            "TotalFound": total_found,
            "LastFound": last_found,
            "TotalCompromised": total_compromised,
            "LastCompromised": last_compromised,
        })
