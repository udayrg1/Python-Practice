products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 2200, "stock": True},
    {"title": "Asics", "price": 1500, "stock": False},
    {"title": "Fila", "price": 3200, "stock": True}
]

'''
Task

Using one list comprehension only, create a new list containing the titles in lowercase where:

✅ Price is greater than or equal to 1800
✅ Stock is True
✅ Title length is greater than 4 characters
Expected Output
['adidas', 'reebok']
'''

product_title =  [product['title'].lower() for product in products if product['price'] >= 1800 and product['stock'] == True and len(product['title'])> 4]

print(product_title)