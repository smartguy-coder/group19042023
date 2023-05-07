my_text = 'I love\npython'
# print(id(my_text))
# my_text += ' very \t\t\t\tmuch'
# print(id(my_text))
# print(my_text)
# #
# # some_new = my_text.split('v')
# # print(some_new)
# # print(type(some_new))
#
# new_list_of_week_temperature = [1, 5, 3.3, -6]
# print(id(new_list_of_week_temperature))
# new_list_2 = [55_555_555, 0]
# new_list_3 = list()
#
# length_list = len(new_list_of_week_temperature)
#
# # print(bool(new_list))
# # print(bool(new_list_2))
#
# # if new_list:
# #     new_variable = 666666666666
# #     print(new_variable)
# # else:
# #     new_variable = 0
# #
# # print(new_variable)
# # pass
#
# new_list_of_week_temperature.append(10)
# # new_list_of_week_temperature.append(1_000_000)
# print(id(new_list_of_week_temperature))
# print(new_list_of_week_temperature)
# # new_list_of_week_temperature.sort(reverse=True)
# print(new_list_of_week_temperature)
#
# print(new_list_of_week_temperature[0])
# # print(new_list_of_week_temperature[5])
#
# # for temperature_value in new_list_of_week_temperature:
# #     print(temperature_value, end=' >>> ')
# #     if temperature_value > 5:
# #         print('warm')
# #     else:
# #         print('cold')
# #
# # for letter in my_text:
# #     print(type(letter))
#
# print(range(1, 32))
#
# # clear data
# new_list_of_week_temperature.clear()
# # new_list_of_week_temperature = []
# # new_list_of_week_temperature[:] = []
# # print(new_list_of_week_temperature)
#
# MAX_TEMP = 50
# MIN_TEMP = -40
#
# for day in range(1, 5 + 1):
#     temp = float(input(f'day {day}: enter temperature >>> '))
#     if temp < MIN_TEMP or temp > MAX_TEMP:
#         # continue
#         pass
#         break
#     new_list_of_week_temperature.append(temp)
#
# print(new_list_of_week_temperature)
# if new_list_of_week_temperature:
#     print(sum(new_list_of_week_temperature)/len(new_list_of_week_temperature))

ukraine_cities = ['Lviv', 'Odesa', 'Dnipro', 'Donetsk', 'Zaporizja']

city_list_kyiv_style = []
expenses = []
other = []
some_trash_list = ['Lviv', 'Odesa', 1000, True, 5000, 'Dnipro', 'Petrovych 068555656', 2356.52, ['Igor', 'Sasha']]

for value in some_trash_list:
    # if type(value) == str:
    if isinstance(value, str) and value in ukraine_cities:
        city_list_kyiv_style.append(value)
    # if type(value) == int or type(value) == float:
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        expenses.append(value)
    else:
        other.append(value)


print(city_list_kyiv_style)
print(expenses)
print(other)

# print('f' in ukraine_cities)
# print(5 in ukraine_cities)
# print('Dnipro' in ukraine_cities)

odesa_data_destination = ['Dnipro', 'Donetsk', 'Zaporizja', 'Zaporizja']

city_list_kyiv_style.extend(odesa_data_destination)
city_list_kyiv_style.sort()
print(city_list_kyiv_style)

last_city = city_list_kyiv_style.pop()
print(last_city)
city_list_kyiv_style.pop(2)
print(city_list_kyiv_style)

# print(city_list_kyiv_style[:2])
# if city_list_kyiv_style:
#     print('fireshow: ', city_list_kyiv_style[-1])

city_list_kyiv_style.insert(0, 'Izum')
print(city_list_kyiv_style)

city_list_kyiv_style.remove('Odesa')
print('*' * 120)
print(city_list_kyiv_style)

# sorting
city_list_kyiv_style.sort(reverse=True, key=lambda x: len(x))  # [0, 6 , 1]  -> [0, 1 , 6]
print(city_list_kyiv_style)

city_list_kyiv_style.reverse()  # [0, 6 , 1]  -> [1, 6 , 0]
print(city_list_kyiv_style)

new_list = reversed(city_list_kyiv_style)
print(list(new_list))
# import itertools

some_list = [4545, ['foo', [[6, '555']], [6666]], 454, []]
print(some_list[1][1][0][1])
