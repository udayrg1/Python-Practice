products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True},
    {"title": "Asics", "price": 3200, "stock": False},
    {"title": "Fila", "price": 2700, "stock": True}
]

'''
Task

Using a for loop only:

Print only the products that satisfy all of the following:

Price greater than or equal to ₹2000
Stock is True

Expected Output
Nike
Fila
'''

for product in products:
    if product['price'] >= 2000 and product['stock'] == True:
        print(product['title'])