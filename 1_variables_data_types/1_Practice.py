""" Create three variables:

Product Name = "Laptop"
Price = 55000.75
Stock Available = True

Print them using an f-string.

Also print the datatype of each variable."""

product_name = "Laptop"
price = 55000.75
stock = True

print(f"Product: {product_name}, Price: {price}, Stock: {stock}")

print(type(product_name).__name__)
print(type(price).__name__)
print(type(stock).__name__)

print(type(product_name))
print(type(price))
print(type(stock))