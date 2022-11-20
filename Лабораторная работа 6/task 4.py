import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter = ",", new_line = "\n") -> list[dict]:
    f = open(filename, 'r')  # TODO реализовать конвертер из csv в json
    headers, *rows = f.readlines()
    headers = headers.replace("\n","")
    headers = headers.split(delimiter)
    list = []
    for row in rows:
        row = row.replace("\n","")
        row = row.split(delimiter)
        dictionary = [dict(zip([header for header in headers],[column for column in row])) for _ in range(1)]
        list = list + dictionary
    f.close()
    return list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
