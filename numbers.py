# from decimal import Decimal
import math


# first_number = int(input('Enter your number 1 >>> '))
# second_number = int(input('Enter your number 2 >>> '))

MSG_INPUT_NUMBER = 'Enter your number {position} (allowed numbers like 5 3.22) >>> '

# first_number = float(input(MSG_INPUT_NUMBER.format(position=1)))
# second_number = float(input(MSG_INPUT_NUMBER.format(position=2)))

# first_number = 0.2
# second_num = 0.1
#
# summa = first_number + second_num
# print(summa)
#
# multiplication = first_number * second_num * 200
# print(multiplication)
#
# division_result = first_number / second_num
# print(division_result)
#
# # rounding
# print(round(multiplication, 2))
# print(round(2.5, 0))
# print(round(3.5, 0))
# print(round(-3.5, 0))
# print(int(-3.9))
#
# print(abs(-3.555))
# num_to_string = str(multiplication)
# print(type(num_to_string))
# print(type(multiplication))
# print(type(56565656))

# milk_price = 40.35
# milk_quantity = 0.125
#
#
# temp_purchase_result = milk_quantity * milk_price
# purchase = Decimal(str(temp_purchase_result)).quantize(Decimal('0.01'))
# print(purchase)

PI = math.pi
print(PI)

mult_many = math.prod([5, 5, 5, PI])
print(mult_many)

powering_root = 25 ** 0.5
powering_root = math.sqrt(25)
print(powering_root)

round_floor = math.floor(-2.9)
print(round_floor)

round_ceil = math.ceil(2.9)
print(round_ceil)
