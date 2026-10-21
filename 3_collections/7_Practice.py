"""
Question 7
Problem

Create the following dictionary:

product = {
    "name": "Laptop",
    "price": 65000,
    "brand": "Dell"
}

Perform the following tasks:

Print the product name using .get().
Print the price using .get().
Print the brand using .get().
Print the stock status using .get().
Since "in_stock" does not exist, display "Not Available" as the default value.
Expected Output
Product Name: Laptop
Price: 65000
Brand: Dell
Stock Status: Not Available

Rules

Use only:

.get()

Do not use:

product["name"]
"""

product = {
    "name": "Dell dark silver Laptop i5 16GB, 536 SSD",
    "price": 69999,
    "brand": "Dell"
}

print(f"Product Name: {product.get('name')}")
print(f"Price: {product.get('price')}")
print(f"Brand: {product.get('brand')}")
print(f"Stock Status: {product.get('in_stock', 'Not Available')}")


