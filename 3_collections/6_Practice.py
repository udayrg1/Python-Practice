"""
Question 6
Problem

Create a dictionary with the following information:

Product Name : Phone X
Price : 999
In Stock : True
Brand : Apple

Then perform the following tasks:

Print the complete dictionary.
Print only the Product Name.
Print only the Price.
Print only the Brand.
Print only the Stock Status.

Expected Output
Product Details: {'name': 'Phone X', 'price': 999, 'in_stock': True, 'brand': 'Apple'}

Product Name: Phone X

Price: 999

Brand: Apple

In Stock: True

Rules

Use only:

Dictionary creation
Dictionary indexing using keys

For example:

product["name"]

Do not use:

.get()
.keys()
.values()
.items()
"""

product = {

    "item_name" : "Phone X",
    "Price" : 999,
    "In Stock" : True,
    "Brand" : "Apple"
}

print(f"Product Details: {product}")
print(f"Product Name: {product['item_name']}")
print(f"Price: {product['Price']}")
print(f"Brand: {product['Brand']}")
print(f"In Stock: {product['In Stock']}")


