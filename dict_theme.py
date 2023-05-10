from pprint import pprint

# person = {}
# person = dict()

# person = {
#     'name': 'John',
#     'hobbies': [
#         'tennis',
#         'darts',
#         'swimming',
#         'horse riding',
#     ],
#     'age': 12,
# }

# person = dict(name='John', hobbies=['tennis', 'darts'], age=12)

wish1_list = ['name', 'hobbies', 'age']
wish2_list = ['name', 'IBAN', 'age', 'address']

wish1 = set(wish1_list)
wish2 = set(wish2_list)

person = dict.fromkeys(wish1 | wish2, None)

hobbies = [
    'tennis',
    'darts',
    'swimming',
    'horse riding',
]
name = 'John1'
person['name'] = 'John'
person['age'] = 12
person['hobbies'] = hobbies
person['address'] = 'Baker Street'
person['name'] = 'sherlock Holmes'

pprint(person, width=50)

print(person['name'].title())
print(person['hobbies'][:2])
print(person.get('surname', '').title())
