from typing import Callable

# print(5)
# print(print)
#
# new_print = print
# print(new_print is print)


def my_function(number):
    try:
        result = number / 22
    except (TypeError, ValueError):
        # print('service unavailable')
        # return 0
        raise
    else:
        return result


def my_scrudge_function(func: Callable, *args, **kwargs):
    print(func)
    print(func(*args, **kwargs))
    result = func(*args, **kwargs)
    return result


#
# print(my_function)
#
res = my_scrudge_function(my_function, 5, 6)
# print(res)

print(my_function('100'))
