data = [
    {
        'my_hobbies': [[1], 5, 6],
    },
    {},
]


for item in data:
    print(type(item))
    print(item)
    print(type(item.get('my_hobbies', [])))
    print(item.get('my_hobbies', []))
    if item.get('my_hobbies', []):
        print(item.get('my_hobbies', [])[0][0])

    print('*' * 20)


def is_even(number: int | float) -> bool:
    return 6555555555