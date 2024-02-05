from functions import *
from Classes import Operation

operations = "operations.json"


def main():
    """Функция выводит 5 последних успешно выполненных
    операций отсортированных по дате"""

    list_operations = sorted_list(list_time_state(read_file(operations)))
    for operation in list_operations:
        massage = Operation(operation)
        print(massage)


if __name__ == "__main__":
    main()
