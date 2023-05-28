import pytest

import ternary_operator


def test_bonus_up():
    sales = 5
    assert ternary_operator.bonus_calculator(sales) == 15

def test_bonus_up_type_int():
    sales = 5
    assert type(ternary_operator.bonus_calculator(sales)) == int


def test_bonus_up_type_float():
    sales = 5.5
    assert type(ternary_operator.bonus_calculator(sales)) == int

def test_bonus_low():
    sales = 2
    assert ternary_operator.bonus_calculator(sales) == 10


def test_bonus_error2():
    sales = 100000000000
    assert ternary_operator.bonus_calculator(sales) == 15


def test_bonus_error():
    sales = '2'
    with pytest.raises(TypeError):
        ternary_operator.bonus_calculator(sales)
