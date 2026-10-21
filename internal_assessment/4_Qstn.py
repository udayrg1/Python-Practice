products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 2200, "stock": True}
]

'''
Using one list comprehension only, create a new list containing the titles in uppercase where:

Price is greater than or equal to 2000
Stock is True
Expected Output
['NIKE', 'REEBOK']
'''

titles = [product['title'].upper() for product in products if product['price']>=2000 and product['stock'] == True]

print(titles)