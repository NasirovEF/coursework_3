import json
from Classes import Operation


def read_file(operations):
    """Читает Json файл и возвращает список"""

    with open(operations, encoding="utf8") as file:
        list_operations = json.load(file)

    return list_operations


def list_time_state(list_operations):
    """Из полученного списка выбирает
     операции со статусом EXECUTED и с датой"""

    list_time_state = []
    for operation in list_operations:
        if operation.get("state") == "EXECUTED" and operation.get("date"):
            list_time_state.append(operation)
    return list_time_state


def sorted_list(list_time_state):
    """ Сортирует полученный список по дате
     и выводит первые 5 элементов"""

    sorted_list = sorted(list_time_state, key=lambda list_time_state: list_time_state.get("date"), reverse=True)
    return sorted_list[:5]




