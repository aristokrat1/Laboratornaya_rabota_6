import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter = ",", new_line = "\n") -> list[dict]:
    f = open(filename, 'r')  # TODO реализовать конвертер из csv в json
    headers = f.readline()
    headers = headers.replace(new_line,"")
    headers = headers.split(delimiter)
    for row in f:
        row = row.replace(new_line,"")
        row = row.split(delimiter)
        yield dict(zip(headers,row))
    f.close()
with open("output.json", 'w') as output:
    for record in csv_to_list_dict(INPUT_FILE):
        json.dump(record, output, indent = 4)
