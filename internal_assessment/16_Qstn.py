'''
🎯 Task

Using one for loop only:

Calculate the total price of all In Stock products.
Count how many In Stock products are available.
Print the average price of only the In Stock products.
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

'''
Expected Output
Total Price : 7700
In Stock Products : 4
Average Price : 1925.0
'''
total_price = 0
instock_counter = 0

for product in products:
    if product["stock"]:
        total_price += product["price"]
        instock_counter += 1

average_price = total_price / instock_counter

print(f"Total Price : {total_price}")
print(f"In Stock Products : {instock_counter}")
print(f"Average Price : {average_price}")


