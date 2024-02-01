import json


def read_file(operations):
    """Читает Json файл и возвращает список"""

    with open(operations, encoding="utf8") as file:
        list_operation = json.load(file)

    return list_operation

operations = 'operations.json'
list_operation = read_file(operations)
print(list_operation)

