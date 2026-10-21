products = [
    "Samsung",
    "iPhone",
    "OnePlus",
    "Nokia",
    "Google Pixel"
]

#Create a new list containing only product names whose length is greater than 6 characters.

len_products = [product for product in products if len(product) > 6]

print(len_products)