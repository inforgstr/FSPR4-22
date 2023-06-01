import csv

def get_csv(file_path: str, delimiter: str) -> list[dict]:
    with open(file_path, "r") as reader:
        return list(csv.DictReader(reader, delimiter=delimiter))

print(get_csv("users.csv", ";")[0].keys()[0])
