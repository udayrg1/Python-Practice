"""
Question 11: Product Name Normalizer
Problem

A product name is stored with extra spaces and uppercase letters:

product_name = "   APPLE IPHONE 15   "

Perform the following tasks:

Remove the extra spaces from the beginning and end using .strip().
Convert the product name to lowercase using .lower().
Store the result in a separate variable.
Print the final product name using an f-string.
Expected Output
Product: apple iphone 15
"""

product_name = "   APPLE IPHONE 15   "

updated_product_name = product_name.strip().capitalize()

print(f"Product: {updated_product_name}")


