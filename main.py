import requests
from pprint import pprint

url = 'https://dummyjson.com/products?limit=100'
# url = 'https://editor.herowand.com/?ref=jsoncrack'
# url = 'https://media.istockphoto.com/id/1362513839/photo/colorful-garden.jpg?b=1&s=170667a&w=0&k=20&c=q3JOpzxfLtxP_FV_aJQMuJ8fxqUqKycb5-CHbJlXrSA='

response = requests.get(url)
# print(response.status_code)
# print(response.content)
# print(response.text)
# pprint(response.json())

data = response.json()
# pprint(type(data))
products = data['products']
# pprint(products)
# print(type(products))

total_cost = 0
items_count = 0

for product in products:

    if product.get('price', 0) < 1800 and product.get('brand', '').upper() == 'APPLE':
        # pprint(product)
        product_price = product.get('price', 0)
        product_stock = product['stock']
        product_cost = product_stock * product_price

        total_cost += product_cost
        items_count += product_stock

# print(total_cost)
# print(items_count)
# if items_count:
#     print(f'average cost of unit {round(total_cost / items_count, 2)}')

# url_post = 'https://s.znctrack.net/z'
# response = requests.post(url_post)
# print(response.headers)