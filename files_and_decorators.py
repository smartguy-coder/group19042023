def make_html(func):
    def wrapper(*args, **kwargs):
        result: str = str(func(*args, **kwargs))

        title = func.__name__
        html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{title}</title>
            </head>
            <body>
                RESULT: <b>{result}</b>
            </body>
            </html>
        """
        with open(f'index_{func.__name__}_{result.replace(" ", "_")}.html', mode='w', encoding='utf-8') as new_file:
            new_file.write(html)

        return result
    return wrapper


def dec_check_str_arguments(func):
    def wrapper(*args, **kwargs):
        arguments = list(args)
        arguments += list(kwargs.values())
        for arg in arguments:
            if not type(arg) == str:
                raise AttributeError

        result = func(*args, **kwargs)
        return result
    return wrapper


@make_html
def some_work() -> str:
    return 'some result'


@make_html
def some_work3() -> int:
    return 5


@make_html
@dec_check_str_arguments
def some_work2(argument: str) -> str:
    return 'some result2 ' + argument


@make_html
@dec_check_str_arguments
def some_work4(argument: str) -> str:
    return 'some result44 ' + argument


res1 = some_work()
res2 = some_work2('jkhfg')
res2 = some_work2(argument='kmdfjgv')
res3 = some_work3()

print(res1)
print(res2)