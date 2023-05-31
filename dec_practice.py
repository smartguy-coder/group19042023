import library

admin = {
    'name': 'Alex',
    'password': '1234',
}


def protection(func):
    def wrapper(*args, **kwargs):
        user = input('Enter your name >>> ')
        password = input('Enter your password >>> ')
        if user == admin['name'] and password == admin['password']:
            result = func(*args, **kwargs)
            return result
        else:
            library.send_telegram_message(f'crack {func.__name__}')
            return {'message': 'access prohibited'}

    return wrapper


def notify_dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        library.send_telegram_message(f'Someone {func.__name__}')
        return result
    return wrapper


def serializer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        final = {
            'count': len(str(result)),
            'result': result,
        }
        return final
    return wrapper


@protection
@serializer
@notify_dec
def mult_two(value):
    return value * 2


@notify_dec
def convert_to_string(value):
    return str(value)

print(mult_two(55))
print(mult_two(value=556565))
print(mult_two(5520))

print(convert_to_string(5656565))
print(type(convert_to_string([5, 6])))