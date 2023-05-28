some_list = [
    ('Leonid', 'Kuchma', 75),
    ('Petro', 'Poroshenko', 50, 'sweets'),
    ('Oleksandr', 'Zelensky', 50),
]


for name, surname, age, *rest in some_list:
    print(name)
    print(surname)
    print(age)
    print(rest)
    print('-------------------')


def my_function(number, *args):
    try:
        result = number / 22
    except (TypeError, ValueError):
        print('service unavailable')
        raise
    else:
        return result


formulas = {
    'square': lambda length, width, *args: length * width,
    'volume': lambda length, width, hight: length * width * hight,
    '1': my_function,
}


parap = (22, 5, 10)

print(formulas['volume'](*parap))
print(formulas['square'](*parap))
print(formulas['1'](*parap))
