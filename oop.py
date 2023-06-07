import datetime
import uuid


class Person:
    __population = 0
    hobbies = set()

    def __init__(self, name: str, surname: str, hobby: str) -> None:
        self._name = name
        self._surname = surname
        self.hobby = hobby
        self.__birthday = datetime.datetime.now() - datetime.timedelta(weeks=800)
        self.increase_population()
        self.monitor_hobbies(self.hobby)
        self.tin = uuid.uuid4()

    def __str__(self) -> str:
        return f'PERSON: {self._name} {self._surname}, {self.__birthday.year}, {self.age}'

    __repr__ = __str__

    @property
    def birthday(self) -> datetime.datetime:
        return self.__birthday

    @property
    def age(self) -> int:
        my_age = (datetime.datetime.now() - self.__birthday).days // 365
        return my_age

    @staticmethod
    def get_dna() -> str:
        return 'YZX-AAA....'

    @staticmethod
    def sum_two_numbers(number1: int, number2: int) -> int:
        return number1 + number2

    @classmethod
    def increase_population(cls):
        print('New person was born')
        cls.__population += 1

    @classmethod
    def decrease_population(cls, person):
        print(f'{person} has died')
        cls.__population -= 1

    @classmethod
    def monitor_hobbies(cls, hobby: str):
        cls.hobbies.add(hobby)

    def __del__(self):
        self.decrease_population(self)


person1 = Person('Alex', 'Bush', 'reading')
# del person1
person2 = Person('Alexis', 'Obama', 'swimming')
print(person2.sum_two_numbers(5, 6))

del person1.hobby

person1.balance = 0
person1.balance += 100
del person1.balance


# print(person1.__dict__)
# print(id(person1))
# print(id(person2))
# print(person2)
# print(person1 == person2)
person1.hobby = 'soccer'
pass
person1._name = 'Bill'
pass
# person1.__birthday = datetime.datetime.now()
person1.girl = person2
pass
# print(person1.__dict__)
print(person1._name)
print(person1._surname)
print(person1.birthday)
print(person1.get_dna())
print(Person.get_dna())

# number = 10
# people = []
# for i in range(number):
#     people.append(Person('111', '222', '333'))
# print(people)
# print(people[0])
