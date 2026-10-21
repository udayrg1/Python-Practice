"""
Question 1: Product List
Problem

Create a list containing:

Phone
Laptop
Charger
Watch
Tablet

Then:

Print the complete list.
Print the first product.
Print the last product.
Print the total number of products using len().
"""


electronics = [
    "Phone",
    "Laptop",
    "Charger",
    "Watch",
    "Tablet"
]

print(f"I have all electronic devices with me: {electronics}")
print(f"First product: {electronics[0]}")
print(f"Last product: {electronics[-1]}")
print(f"Total number of products: {len(electronics)}")
