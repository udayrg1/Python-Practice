'''
🎯 Task

Using a for loop only:

Count how many products are in stock.
Count how many products are out of stock.
Print the results exactly like this:

Expected Output
In Stock Products : 4
Out of Stock Products : 3
'''

products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True},
    {"title": "Asics", "price": 3200, "stock": False},
    {"title": "Fila", "price": 2700, "stock": True},
    {"title": "Skechers", "price": 1500, "stock": False}
]

instock_counter = 0
oos_counter = 0


for product in products:
    if product['stock']:
        instock_counter += 1
    else:
        oos_counter += 1
print(f"In Stock Products : {instock_counter}")
print(f"Out of Stock Products : {oos_counter}")

