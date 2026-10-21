"""
Question 1: Your First for Loop
Problem

Given the following list:

products = ["Phone", "Laptop", "Watch", "Tablet"]

Use a for loop to print each product on a separate line.

Expected Output
Phone
Laptop
Watch
Tablet

Hint (Very Important)

A for loop has this structure:

for variable in collection:
    # code

For this question:

variable → one product at a time
collection → products
"""

"""
1
"""
products = ["Phone", "Laptop", "Watch", "Tablet"]

for items in products:
    print(items)

"""
2
"""

products = ["Phone", "Laptop", "Watch", "Tablet"]

for items in products:
    print(f"Product: {items}")