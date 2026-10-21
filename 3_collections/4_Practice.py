"""
Question 4: Product Details Tuple
Problem

Create a tuple containing the following product details:

Phone X
999
True

Store them in this order:

Product Name, Price, In Stock

Perform these tasks:

Print the complete tuple.
Print the product name using indexing.
Print the price using indexing.
Print the stock status using indexing.
Print the total number of items using len().

Expected Output

Product Details: ('Phone X', 999, 999, True)
Product Name: Phone X
Price: 999
Age: 999
In Stock: True
Total Items: 3

This question tests:

Tuple creation → ()
Indexing       → [0], [1], [2]
Length         → len()
"""

product_details = ('Phone X', 999, 999, True)

print(f"Product Details: {product_details}")

print(f"Product Name: {product_details[0]}")

print(f"Price: {product_details[1]}")

print(f"Age: {product_details[2]}")

print(f"In Stock: {product_details[3]}")

print(f"Total Items: {len(product_details)}")

