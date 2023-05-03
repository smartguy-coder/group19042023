# user_age = int(input('Enter your age (int value) >>> '))
#
# true = True  # True <>0 not empty string    comparison result
# false = False
#
# # print(bool(user_age))
# # print(bool(0))
# # print(bool(1))
# # print(bool(''))
# print(bool('user_age'))
#
#
# if user_age < 1:  # < > <= >=  ==  !=  is not
#     print('incorrect input')
# elif user_age == 10:
#     print('You are in 4-th grade')
# elif user_age >= 18:
#     print('You can buy alcohol')
# else:
#     print('I do not know what to do')
#
#
#
#
#
# # print(user_age)


# user_name = input('Enter your name >> ').title()
# password = input('Password >> ')
#
# # print(chr(95))
# # print(chr(105))
#
# # if user_name != 'John' or True:  # < > <= >=  ==  !=  is not
# if (user_name != 'John') and (password == '1'):  # < > <= >=  ==  !=  is not
#     print(f"Hello, {user_name}")
# else:
#     print('Go away')

true = True
one = 1

print(id(True))
print(id(true))
print(id(False))
print(id(1))

if true == one:
    print(88888888888)



my_string = '5555555jjjjjjj'

if my_string.isdigit():
    print(my_string.isdigit())
    number = int(my_string)
    print(number, end=' *** ')
else:
    print('not for int')
    print(int(my_string.isdigit()))

