import json
from pprint import pprint
#
data = '{"id":1,"продукти fresh":[{"id":59,"title":"Spring and summershoes","price":20,"quantity":3,"total":60,"discountPercentage":8.71,"discountedPrice":55},{"id":88,"title":"TC Reusable Silicone Magic Washing Gloves","price":29,"quantity":2,"total":58,"discountPercentage":3.19,"discountedPrice":56},{"id":18,"title":"Oil Free Moisturizer 100ml","price":40,"quantity":2,"total":80,"discountPercentage":13.1,"discountedPrice":70},{"id":95,"title":"Wholesale cargo lashing Belt","price":930,"quantity":1,"total":930,"discountPercentage":17.67,"discountedPrice":766},{"id":39,"title":"Women Sweaters Wool","price":600,"quantity":2,"total":1200,"discountPercentage":17.2,"discountedPrice":994}],"total":2328,"discountedTotal":1941,"userId":97,"totalProducts":5,"totalQuantity":10}'

dict_from_json = json.loads(data)

pprint(dict_from_json)
#
# with open('cart.json', mode='w', encoding='utf-8') as new_json_file:
#     json.dump(dict_from_json, new_json_file, indent=4)

# with open('cart.json', mode='r', encoding='utf-8') as new_json_file:
#     data = json.load(new_json_file)
#     pprint(data)


# new_dict = {'name': 'Alex'}
#
# json_from_dict = json.dumps(new_dict)
#
# pprint(json_from_dict)

