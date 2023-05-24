from typing import Any


def is_even(number: int | float) -> bool:
    remain_part = number % 2
    n = 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
    result = remain_part == 0
    return result


def force_to_int(value: Any) -> int:
    try:
        result = int(value)
    except (ValueError, TypeError):
        return 0
    else:
        return result


def get_user_int_number(message: str = 'Enter number: ') -> int:
    flag = True
    while flag:
        proceed = input('Proceed? - ')
        if proceed == 'y':
            continue

        raw_number = input(message)
        if raw_number.isdigit():
            int_number = int(raw_number)
            flag = False
            break
            print(55555555555555555)

    return int_number
