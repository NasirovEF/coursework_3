from datetime import datetime


class Operation:

    def __init__(self, id_op, date, state, op_am, dscr, fr, to):
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

