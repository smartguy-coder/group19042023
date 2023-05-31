import requests

TOKEN_TELEGRAM = '6082820508:AAH6EmSXk0Sc9s37FOpVWiczH-l3X4wZHFA'
TELEGRAM_CHAT_ID = 942643203


def send_telegram_message(
        message: str,
        my_token: str = TOKEN_TELEGRAM,
        method: str = 'sendMessage',
):
    url = f"https://api.telegram.org/bot{my_token}/{method}"
    response = requests.post(
        url=url,
        data={'chat_id': TELEGRAM_CHAT_ID, 'text': message},
    )

    return response.json()


def operations_with_file(file_name: str, mode='r'):
    # file = open()
    # 1/0
    # file.close()

    # if mode == 'w':
    #     with open(file_name, mode=mode, encoding='utf-8') as file:
    #         file.write('kmfbvdfvjkdfj')

    with open(file_name, mode=mode, encoding='utf-8') as file:
        content = file.read()
        print(content)


operations_with_file('library.py')