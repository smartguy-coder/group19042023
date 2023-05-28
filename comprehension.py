import sys

some_list = [5, 6, 18, 0, -6, 7, 7, 7, 8]

number = 6655

# target_list = []
# for number in some_list:
#     if number > 5:
#         target_list.append(number)
#
# print(target_list)
# print(number)

# comprehension

new_target_list = [number_inner for number_inner in some_list if number_inner > 5]
# print(new_target_list)

# new_target_set = {number_inner for number_inner in some_list if number_inner > 5}
# print(new_target_set)
#
# list_dif_types = [[1], [2, 3], 'abc', 5, 5, '5']
#
# list_comp_double = [element * 2 for element in list_dif_types]
# print(list_comp_double)

# list_comp_double_unique = {element * 2 for element in list_dif_types}
# print(list_comp_double_unique)

# list_comp_double_pairs = {str(element): element * 2 for element in list_dif_types}
# print(list_comp_double_pairs)
#
#
# list_comp_double_numbers = {element: element * 2 for element in some_list}
# print(list_comp_double_numbers)


# print(number_inner) error

# some_string = 'koeghuHIOHIOUHHHIUOHIOHIOUHIUOHIUHiughiuhuh'

# list_lower_case = [char for char in some_string if char.islower()]
# print(list_lower_case)

# list_lower_case_converted_to_upper = [char.upper() for char in some_string if char.islower()]
# print(list_lower_case_converted_to_upper)
#
# list_maybe_int = [5, 6, '565', 56.5, -9, '5.2']
# list_definitely_int = [int(float(number)) for number in list_maybe_int]
# print(list_definitely_int)

list_comp_round_brackets = (number_inner for number_inner in some_list if number_inner > 5)
print(list_comp_round_brackets)

# print(sys.getsizeof(new_target_list))
print(sys.getsizeof(list_comp_round_brackets))

# for element in list_comp_round_brackets:
#     print(element)
#
# for element in list_comp_round_brackets:
#     print(5555555555)
#     print(element)


print(next(list_comp_round_brackets))
print(next(list_comp_round_brackets))
print(next(list_comp_round_brackets))

print(5555555555555555555555)

print(next(list_comp_round_brackets))
some_list.pop()


some_list.append(12)
some_list.append(13)
some_list.append(16)

for rest in list_comp_round_brackets:
    print('>>>>>>>>>', rest)

