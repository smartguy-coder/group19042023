import requests


url = 'https://dummyjson.com/todos/{id}'

for page in range(1, 151):
    response = requests.get(
        url.format(
            id=page,
        )
    )

    data = response.json()
    # {'id': 1,
    # 'todo': 'Do something nice for someone I care about',
    #  'completed': True,
    #  'userId': 26}

    if data['completed']:
        print(data['todo'], data['completed'])
