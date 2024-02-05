from functions import *


def test_read_file():
    assert read_file("operationstest.json") == [{"id": 441945886}]

def test_list_time_state():
    operation = [{"state": "EXECUTED", "date": "1234566"}]
    operation_1 = []
    operation_2 = [{"state": "EXECUTED"}]
    operation_3 = [{"date": "1234566"}]
    assert list_time_state(operation) == [{"state": "EXECUTED", "date": "1234566"}]
    assert list_time_state(operation_1) == []
    assert list_time_state(operation_2) == []
    assert list_time_state(operation_3) == []


def test_sorted_list():
    x = [{"date": 1}, {"date": 5}, {"date": 3}]
    assert sorted_list(x) == [{"date": 5}, {"date": 3}, {"date": 1}]

def test_sorted_list_1():
    x = [{"date": 1}, {"date": 5}, {"date": 3}, {"date": 4}, {"date": 2}, {"date": 0}]
    assert sorted_list(x) == [{"date": 5}, {"date": 4}, {"date": 3}, {"date": 2}, {"date": 1}]
