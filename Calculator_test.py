# from calculator import Calculator
#
# cal = Calculator()
#
# # тестируем метод sum
#
# res = cal.sum(4, 6)
# assert res == 10, 'результат не совпал'
#
# res1 = cal.sum(-4, -2)
# assert res1 == -6, 'результат не совпал'
#
# res2 = cal.avg([1,2,3])
# assert res2 == 2, 'результат не совпал'


from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_sum_pos_muns(calculator):
    assert calculator.sum(1, 2) == 3

def test_sum_neg_muns(calculator):
    assert calculator.sum(-1, -2) == -3