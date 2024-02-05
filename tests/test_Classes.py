from Classes import *


def test_right_date():
    x = Operation({"date": "1996-11-11"})
    assert x.right_date() == "11.11.1996"


def test_transfer_amount():
    x = Operation({"operationAmount": {
      "amount": "31987.58",
      "currency": {"name": "руб.", "code": "RUB"}}})
    assert x.transfer_amount() == "31987.58 руб."


def test_hide_inform():
    deposit = "Счет 123456789"
    x = Operation(deposit)
    assert x.hide_inform(deposit) == "Счет **6789"


def test_hide_inform_1():
    deposit = "Мир Классик 1234567891234567"
    x = Operation(deposit)
    assert x.hide_inform(deposit) == "Мир Классик 1234 56** **** 4567"


def test_hide_inform_2():
    deposit = "мир 1234567891234567"
    x = Operation(deposit)
    assert x.hide_inform(deposit) == "мир 1234 56** **** 4567"


def test_transfer_message():
    x = Operation({"from": "Мир Классик 1234567891234567", "to": "мир 1234567891234567"})
    assert x.transfer_message() == "Мир Классик 1234 56** **** 4567 -> мир 1234 56** **** 4567"


def test_transfer_message_1():
    x = Operation({"to": "мир 1234567891234567"})
    assert x.transfer_message() == "мир 1234 56** **** 4567"