import json
from Classes import Operation


def read_file(operations):
    """Читает Json файл и возвращает список"""

    with open(operations, encoding="utf8") as file:
        list_operations = json.load(file)

    return list_operations


def list_oper(list_operations):
    for operation in list_operations:
        print(f"{Operation(operation)}\n")


operations = 'operations.json'
list_operations = read_file(operations)

list_oper(list_operations)
