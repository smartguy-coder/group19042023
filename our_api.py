import requests

url = 'https://script.google.com/macros/s/AKfycbwziIJYJw5i3F-K0kftnH8xOl19TfJF_-c31QrW7SnH5BxRG7bTmNFGzjqY2OZRZkWK/exec'

response = requests.get(url)

inner_data = response.json()

clean_data = inner_data['data']

print(clean_data)

for person in clean_data:
    if person['age'] > 50:
        print(person)
