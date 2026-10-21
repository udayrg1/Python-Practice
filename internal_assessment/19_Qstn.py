products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True},
    {"title": "Asics", "price": 3200, "stock": False},
    {"title": "Fila", "price": 2700, "stock": True},
    {"title": "Skechers", "price": 1500, "stock": False},
    {"title": "New Balance", "price": 4100, "stock": True}
]

'''
Using one for loop only:

Find:

The most expensive product that is in stock.

Print its:
Title
Price

Expected Output
Most Expensive Product

Title : New Balance
Price : 4100
'''

most_expensive = None

for product in products:
    if product["stock"]:
        if most_expensive is None or product["price"] > most_expensive["price"]:
            most_expensive = product

print("Most Expensive Product")
print(f"Title : {most_expensive['title']}")
print(f"Price : {most_expensive['price']}")