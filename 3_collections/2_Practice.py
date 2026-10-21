"""
Question 2: Update Product List
Problem

Create this product list:

products = ["Phone", "Laptop", "Watch"]

Perform these tasks:

Add "Tablet" to the list using .append().
Print the updated list.
Remove the last product using .pop().
Store the removed product in a variable called removed_product.
Print the removed product.
Print the final list.
Expected Output
Updated Products: ['Phone', 'Laptop', 'Watch', 'Tablet']
Removed Product: Tablet
Final Products: ['Phone', 'Laptop', 'Watch']

This question tests:

.append() → adds an item to the end of a list
.pop()    → removes and returns an item
"""

products = ["Phone", "Laptop", "Watch"]

#products.append("Tablet")  -- for single element it is .append()

products.extend(["Tablet", "Charger"]) #for multiple products it is .extend()
print(f"Updated Products: {products}")

removed_product = products.pop()
print(f"Removed Product: {removed_product}")

print(f"Final Products: {products}")







