from datetime import datetime


class Operation:

    def __init__(self, id_op, state, date, op_am, dscr, fr, to):
        self.id = id_op
        self.date = date
        self.state = state
        self.op_am = op_am
        self.dscr = dscr
        self.fr = fr
        self.to = to

    def state_operation(self):
        """Определяет статус операции, если операция выполнена
        возвращает True"""

        if self.state == "EXECUTED":
            return True
        else:
            return False

    def right_date(self):
        """Прописывает дату в формате ДД.ММ.ГГГГ"""

        the_right_date = datetime.fromisoformat(self.date.replace("T", " "))

        return f'{the_right_date.day}.{the_right_date.month}.{the_right_date.year}'

    def transfer_amount(self):
        """Возвращает сумму перевода с указанием валюты"""

        return f"{self.op_am["amount"]} {self.op_am["currency"]["name"]}"

    def hide_inform(self, deposit):
        """Маскирует номер карты и номер счета"""

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
        return f"{self.right_date()} {self.dscr}\n{self.hide_inform(self.fr)} -> {self.hide_inform(self.to)}\n{self.transfer_amount()}"


first = Operation(547682597, "EXECUTED", "2018-12-29T21:45:18.495053", {"amount": "66263.93", "currency": {"name": "руб.", "code": "RUB"}}, "Перевод организации", "Счет 77977573135347241529", "Счет 33062909508148771891")


print(first)