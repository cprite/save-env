import os


"""

KEY STORAGE MANAGEMENT

"""



def add_key(key):

    with open(os.path.join("app/crawler/data", "keys.txt"), "a") as file:
        file.write(f"{key}\n")


def get_keys():

    with open(os.path.join("app/crawler/data", "keys.txt"), "r") as file:
        keys = set(line.strip() for line in file)

        return keys
