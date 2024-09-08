import pandas as pd
import os


"""

GET STAT ON TOTAL AND LAST SCANNING

"""

def get_stat():
    data = pd.read_csv(os.path.join("app/crawler/data", "statistics.csv"))

    return str(data['ScanTime'][0]), str(data['TotalFound'][0]), str(data['LastFound'][0]), str(data['TotalCompromised'][0]), str(data['LastCompromised'][0])


def update_stat(scan_time, total_found, last_found, total_compromised, last_compromised):
    data = pd.read_csv(os.path.join("app/crawler/data", "statistics.csv"))

    data['ScanTime'] = scan_time
    data['TotalFound'] = total_found
    data['LastFound'] = last_found
    data['TotalCompromised'] = total_compromised
    data['LastCompromised'] = last_compromised

    data.to_csv(os.path.join("app/crawler/data", "statistics.csv"), index=False)
