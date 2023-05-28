def get_presidents():

    presidents = [
        'Кравчук',
        "Кучма",
        'Ющенко',
        'Янукович',
        'Порошенко',
        'Зеленський',
    ]

    for president in presidents:
        print('work before yield')
        yield president


persons = get_presidents()

print(next(persons))
print(next(persons))
print(next(persons))
print(next(persons))
print(next(persons))


def gen_next_numbers(start: int = 1):

    while True:
        yield start
        start += 1
        if start > 100_000:
            break
    print(5555555555555)


gen = gen_next_numbers(-555)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(465465464465465)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)