products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True},
    {"title": "Asics", "price": 3200, "stock": False},
    {"title": "Fila", "price": 2700, "stock": True},
    {"title": "Skechers", "price": 1500, "stock": False}
]

'''
Using one for loop only:

Print the products that satisfy all of the following conditions:

✅ Price is greater than or equal to ₹1500
✅ Product is In Stock

For every matching product, print:

Title : Nike
Price : 2500

Title : Adidas
Price : 1800

Title : Fila
Price : 2700
'''

for product in products:
    if product['price']>=1500 and product['stock']:
        print(f"\nTitle : {product['title']}")
        print(f"Price : {product['price']}")
