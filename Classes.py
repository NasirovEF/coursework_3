from datetime import datetime


class Operation:

    def __init__(self, operation):
        self.operation = operation

    def state_operation(self):
        """Определяет статус операции, если операция выполнена
        возвращает True"""

        self.state = self.operation["state"]
        if self.state == "EXECUTED":
            return True
        else:
            return False

    def right_date(self):
        """Прописывает дату в формате ДД.ММ.ГГГГ"""

        self.date = self.operation["date"]
        the_right_date = datetime.fromisoformat(self.date.replace("T", " "))

        return f'{the_right_date.day}.{the_right_date.month}.{the_right_date.year}'

    def transfer_amount(self):
        """Возвращает сумму перевода с указанием валюты"""

        self.op_am = self.operation["operationAmount"]
        return f"{self.op_am["amount"]} {self.op_am["currency"]["name"]}"

    def hide_inform(self, deposit):
        """Маскирует номер карты и номер счета"""

        self.fr = self.operation["from"]
        self.to = self.operation["to"]
        if "Счет" in deposit:
            return f'Счет **{deposit[-4:]}'
        elif len(deposit) == 0:
            return ""
        else:
            share = deposit.split()
            name_card = []
            card_numb = []
            for i in share:
                if i.isdigit():
                    card_numb.append(i)
                else:
                    name_card.append(i)
            return f'{" ".join(name_card)} {card_numb[0][-16:-12]} {card_numb[0][-16:-14]}** **** {card_numb[0][-4:]}'

    def __str__(self):
        return f"{self.right_date()} {self.operation["description"]}\n{self.hide_inform(self.operation["from"])} -> {self.hide_inform(self.operation["to"])}\n{self.transfer_amount()}"

