import library


def main():
    number = library.get_user_int_number('Enter number (like 5 6 10) ')
    result = library.is_even(number=number)
    print(result)


main()
