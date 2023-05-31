# def some_func(value):
#     return str(value)
#
# def some_func2(value):
#     return int(value)
#
# # another = some_func
# #
# # func_list = [another, some_func, lambda x: x]
# # # print(func_list[0])
# #
# #
# # # print(another())
# # # # print(some_func)
# # # # print(print)
# # #
# # def master(function):
# #     result = function()
# #     print(result)
# #     return result
# #
# # master(some_func)
#
#
# def convert_result_to_float(function, value):
#     result = function(value)
#     converted_result = float(result)
#     return converted_result

# print(convert_result_to_float(some_func, '654645'))
# print(convert_result_to_float(some_func2, 5656))

# def some_func(value=5):
#     return str(value)
#
# def convert_result_to_float(function):
#     result = function()
#     converted_result = float(result)
#     return converted_result
#
#
#
# some_func = convert_result_to_float(some_func)
#
# print(some_func)

force_to_float = True


def decorator_no_parameters(func):
    def wrapper(*args, **kwargs):
        # wrapper(value=5555)
        print(args)
        print(kwargs)
        #        some_func(value=5555)
        result = func(*args, **kwargs)
        return float(result)
    return wrapper


def decorator_with_parameters(convert_value=True):
    def wrapper_inner(func):
        def wrapper(*args, **kwargs):
            # wrapper(value=5555)
            # print(args)
            # print(kwargs)
            # #        some_func(value=5555)
            result = func(*args, **kwargs)
            if convert_value:
                result = float(result)

            return result

        return wrapper

    return wrapper_inner


@decorator_with_parameters(force_to_float)
def some_func(value):
    res = str(value)
    return res

# some_func = decorator(some_func)
@decorator_no_parameters
def some_func2():
    res = str(555555555)
    return float(res)



print(some_func(value=5555))
print(some_func)
print(some_func2())

