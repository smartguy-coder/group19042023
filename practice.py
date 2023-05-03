# side1 = float(input("first"))
# side2 = float(input("second"))
# side3 = float(input("third"))
#
# side1_requirements = side1 < (side2 + side3)
# side2_requirements = side2 < (side1 + side3)
# side3_requirements = side3 < (side1 + side2)
#
#
# if side1_requirements and side2_requirements and side3_requirements:
#     print('It is triangle')
# else:
#     print('negative')


side1 = input("first ")
side2 = input("second ")

if side1.replace('.', '', 1).isdigit() and side2.replace('.', '', 1).isdigit():
    side1 = float(side1)
    side2 = float(side2)

    if side1 <= 0 or side2 <= 0:
        print('incorrect')
    elif side1 == side2:
        print('square')
    else:
        print('not square')

else:
    print('has letters')



