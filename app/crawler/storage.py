import os


"""

KEY STORAGE MANAGEMENT

"""


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
KEYS_PATH = os.path.join(DATA_DIR, "keys.txt")


def add_key(key):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(KEYS_PATH, "a") as file:
        file.write(f"{key}\n")


def get_keys():
    if not os.path.exists(KEYS_PATH):
        return set()

    with open(KEYS_PATH, "r") as file:
        return set(line.strip() for line in file if line.strip())
