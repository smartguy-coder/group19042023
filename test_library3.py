import pytest

import library


def test_is_even_positive():
    test_number = 2
    assert library.is_even(test_number) is True


def test_is_even_negative():
    test_number = 3
    print('\n', 555555555555555555555, '\n')
    assert library.is_even(test_number) is False


def test_is_even_wrong_type():
    test_value = '5656'
    with pytest.raises(TypeError):
        assert library.is_even(test_value) is True


def test_force_to_int_int_arg():
    test_value = 2
    assert library.force_to_int(test_value) == 2


def test_force_to_int_float_arg():
    test_value = 2.5
    assert library.force_to_int(test_value) == 2


def test_force_to_int_bool_arg():
    test_value = True
    assert library.force_to_int(test_value) == 1


def test_force_to_int_bool_false_arg():
    test_value = False
    assert library.force_to_int(test_value) == 0


def test_force_to_int_str_arg():
    test_value = 'False'
    assert library.force_to_int(test_value) == 0


def test_force_to_int_list_arg():
    test_value = []
    assert library.force_to_int(test_value) == 0


def test_force_to_int_type_check():
    test_value = []
    assert type(library.force_to_int(test_value)) == int
