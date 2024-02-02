import json


def read_file(operations):
    """Читает Json файл и возвращает список"""

    with open(operations, encoding="utf8") as file:
        list_operations = json.load(file)

    return list_operations


def list_oper(list_operations):

    list_1 = []
    for operation in list_operations:
        list_1.append(operation)

    print(list_1.sort(key=operation))





operations = 'operations.json'
list_oper(read_file(operations))