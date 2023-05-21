from copy import copy, deepcopy
from typing import Any

import requests
import decimal
import fractions

# url = 'https://script.google.com/macros/s/AKfycbxWyl5bqQDqHeeCqvEnO9zsv2A9qVSNMZDzyMzqinQutjWUoz8NPf_8_Y3vtLXijvCa/exec'
#
# response = requests.get(url=url)
#
# inner_data = response.json()


# def get_json_data():
#     print(6)
#
#
# def is_number():
#     get_json_data()
#
#
# is_number()



# get_json_data()

'jkhjkhkj    '.isalpha()


def increse_number(number_value: int | float, coeficient: int = 1, rounding: int = 2) -> float:
    duplicate = number_value * coeficient
    floated_duplicate = float(duplicate)
    rounded_value = round(floated_duplicate, rounding)
    return rounded_value


def is_number(value: Any) -> bool:
    """
    according to doc #2356 decimal.Decimal and
    fractions.Fraction are valid types
    """
    # if type(value) == int or type(value) == float or type(value) == decimal.Decimal or type(value) == fractions.Fraction:
    #     pass
    if type(value) in (int, float, decimal.Decimal, fractions.Fraction):
        return True
    return False


number = 555
result = increse_number(
    number_value=number,
    rounding=2,
)
#
# # print(result.is_integer())
# # print()
#
# # candidate = decimal.Decimal('55')
# # print(candidate * 2)
# #
# # fract1 = fractions.Fraction('1/22')
# # fract2 = fractions.Fraction('3/2')
# # res = fract2 + fract1
# # print(res)
#
# print(is_number(value='{5}'))

# some weird staff


def add_value_to_given_list(given_list: list, value: Any) -> list:
    given_list = given_list[:]
    # given_list = copy(given_list)
    print(id(given_list))
    given_list.append(value)
    return given_list


my_list = []
print(id(my_list))
processed1 = add_value_to_given_list(given_list=my_list, value=5)
print(processed1)

processed2 = add_value_to_given_list(given_list=my_list, value=6)
print(processed2)

processed3 = add_value_to_given_list(given_list=my_list, value=6)
print(processed3)


def add_char_to_given_string(given_string: str, char: str, some_unused=None) -> str:
    result = given_string + char
    return result


my_string = '123>>>'
processed_str1 = add_char_to_given_string(given_string=my_string, char='5')
print(processed_str1)

processed_str2 = add_char_to_given_string(given_string=my_string, char='6')
print(processed_str2)





url = 'https://script.google.com/macros/s55/AKfycbxWyl5bqQDqHeeCqvEnO9zsv2A9qVSNMZDzyMzqinQutjWUoz8NPf_8_Y3vtLXijvCa/exec'


def get_dictionary_by_url(url: str) -> dict:
    try:
        response = requests.get(url=url)
    except:
        return {}

    if response:
        try:
            inner_data = response.json()
            return inner_data
        except:
            return {}
    return {}


url = 'https://github.com/smartguy-coder/group19042023/blob/dict_requests/practice.py'

data = get_dictionary_by_url(url=url)

for key in data.items():
    print(key)




















