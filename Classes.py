from datetime import datetime


class Operation:

    def __init__(self, operation):
        self.operation = operation

    def right_date(self):
        """Прописывает дату в формате ДД.ММ.ГГГГ"""

        the_right_date = datetime.fromisoformat(self.operation.get("date").replace("T", " "))

        return f'{the_right_date.day}.{the_right_date.month}.{the_right_date.year}'

    def transfer_amount(self):
        """Возвращает сумму перевода с указанием валюты"""

        operationamount = self.operation.get("operationAmount")
        amount = operationamount.get("amount")
        money = operationamount.get("currency")
        return f"{amount} {money.get("name")}"

    def hide_inform(self, deposit):
        """Маскирует номер карты и номер счета"""

        if "Счет" in deposit:
            return f'Счет **{deposit[-4:]}'
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

    def transfer_message(self):
        """Формирует информацию откуда и на какой
        счет был перевод"""

        if self.operation.get("from"):
            return f"{self.hide_inform(self.operation.get("from"))} -> {self.hide_inform(self.operation.get("to"))}"
        else:
            return self.hide_inform(self.operation["to"])

    def __str__(self):
        return f"{self.right_date()} {self.operation["description"]}\n{self.transfer_message()}\n{self.transfer_amount()}\n"
