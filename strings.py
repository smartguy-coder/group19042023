my_love = 'I love python'

initial_number = 54
number_one = 5
number_two = 4
print(id(number_two))

result = number_two * 10 + number_one

print(number_two, number_one, sep='', end='------')
print(result)

city = 'Kyiv'
country = 'Ukraine'
continent = 'Europe'

city_o = 'Oslo'
country_n = 'Norway'

# bad idea - too many pluses
capital_city = city + ' ' + country + ' ' + continent
print(capital_city)

# good decision
# 1 - f-string - immediately
capital_city_correct = f'{city} {country} {continent}'
print(capital_city_correct)

# 2 - format method
template = '{city} - {country} {continent}'
kyiv_info = template.format(city=city, country=country, continent=continent)
print(kyiv_info)
oslo_info = template.format(city=city_o, country=country_n, continent=continent)
print(oslo_info)

# smiles  utf-8
# Unicode Name	Fire Unicode Number	U+1F525   🔥
fire_1 = 'fire \U0001F525'
fire_2 = 'fire \t\t🔥'
fire_3 = 'fire \N{Fire}'
fire_4 = r'fire \nkjgh\ndkjfghkjfdhkj\N{Fire}🔥'
print(fire_1, fire_2, fire_3, fire_4, end='\n\n\n')

# user_name = input('Введіть ваше імя >>> ').title()  # every first uppercase, rest - lowercase
# user_name = input('Введіть ваше імя >>> ').capitalize()  # first uppercase
# user_name = input('Введіть ваше імя >>> ').upper()  # uppercase
# user_name = input('Введіть ваше імя >>> ').lower().strip()  # lowercase
# user_name = input('Введіть ваше імя >>> ').lower().strip(' 025\t')  # lowercase
# user_name = input('Введіть ваше імя >>> ').lower().rsplit(' 025\t')  # lowercase
# user_name = input('Введіть ваше імя >>> ').lower().lstrip(' 025\t')  # lowercase
# user_name = input('Введіть ваше імя >>> ').casefold()  # 'Straße
# user_name = input('Введіть ваше імя >>> ').swapcase()  # revert
#
# print(user_name)

# replace
street = "Baker Street 125, room 125"
sherlock_address = street.replace('125', '234', 1)
print(sherlock_address)

# a -> e, e -> b   (letter by letter)
# replacer = street.replace('a', 'e')
# replacer = replacer.replace('e', 'b')
# print(replacer)  # no way

translate_map = str.maketrans('ae', 'eb')
trans_result = street.translate(translate_map)
print(trans_result)

street_length = len(trans_result)
print(street_length)
