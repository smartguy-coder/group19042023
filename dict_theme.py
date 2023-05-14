from pprint import pprint

# person = {}
# person = dict()

person = {
    'name': 'John',
    'hobbies': [
        'tennis',
        'swimming',
        'acrobatic',
        'darts',
        'horse riding',
    ],
    'age': 12,
    True: 'yes, cat play the guitar',
    False: 'weird',
}

account_data = {
    'IBAN': 232323246543546546,
    'Bank': 'Raiffaisen',
    'hobbies': True,
    1: 'one',
    1.0: 'float',
    0.0: 'new weird',
    0: 'brand new weird',
}
# person = dict(name='John', hobbies=['tennis', 'darts'], age=12)

# wish1_list = ['name', 'hobbies', 'age']
# wish2_list = ['name', 'IBAN', 'age', 'address']
#
# wish1 = set(wish1_list)
# wish2 = set(wish2_list)
#
# person = dict.fromkeys(wish1 | wish2, None)
#
# hobbies = [
#     'tennis',
#     'darts',
#     'swimming',
#     'horse riding',
# ]
# name = 'John1'
# person['name'] = 'Jack'
# person['age'] = 55
# # person['hobbies'] = hobbies
# person['address'] = 'Baker Street'
# person['name'] = 'sherlock Holmes'

#
# print(person['name'].title())
# print(person['hobbies'][:2])
# print(person.get('surname', '').title())

person['hobbies'].sort()

# get index of the element in the list
index_data = person['hobbies'].index('swimming')
person['hobbies'][index_data] = 'soccer'

pprint(person, width=50)

# for hobby in person['hobbies']:
#     print(hobby)

# person['subjects'] = ['math', 'history']

# for subject in person.get('subjects', {}):
#     print(subject)

# iteration by keys
# for key in person:
#     print(person[key])

# iteration by keys
# print(list(person.keys()))
# print('*' * 50)
# pprint(list(person.values()))
# pprint(list(person.items()))

# iteration by values
# for value in person.values():
#     print(value)

# tuple - immutable
# my_tuple = tuple()
# my_tuple = ()
my_tuple = ('John', 'Watson', 'Backer Street', [])
my_tuple = ('John', 'Watson')

# print(my_tuple)
# print(len(my_tuple))
# print(my_tuple[0])
#
# list_from_tuple = list(my_tuple)
# print(list_from_tuple)

# list_from_tuple = set(my_tuple) # nop
# print(list_from_tuple)

# name = my_tuple[0]
# surname = my_tuple[1]
# my_tuple[0] = 'Jack' # nop

name, surname, *other = my_tuple

# iteration by all data
# for key, value in person.items():
#     # print(key, value, sep=' --**-- ')
#     if key == 'name' and value == 'John':
#         print('John is here')

# union
# total_person_info = {**person, **account_data}
# pprint(total_person_info)

# python 3.9+
total_person_info = person | account_data



# delete data

# key and value pair
# del total_person_info[True]
del total_person_info[False]

# by key but process value data
true_data_value = total_person_info.pop(True)
# print(f'{true_data_value=}')
print(f'true_data_value = {true_data_value}')

# get deleted pair
# items = total_person_info.popitem()
# print(f'{items=}')

total_person_info.clear()

pprint(total_person_info)
