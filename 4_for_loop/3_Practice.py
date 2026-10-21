"""
Question 3
enumerate() ⭐⭐⭐⭐⭐

Suppose you have:

products = ["Phone", "Laptop", "Watch"]

A normal loop gives you:

Phone
Laptop
Watch

But what if your manager asks:

1. Phone
2. Laptop
3. Watch

or

Index 0 → Phone
Index 1 → Laptop
Index 2 → Watch

How do you get both the index and the value together?

That's exactly what enumerate() does.

Question 4

Given:

products = ["Phone", "Laptop", "Watch", "Tablet"]

Using enumerate(), print:

Expected Output
Index: 0  Product: Phone
Index: 1  Product: Laptop
Index: 2  Product: Watch
Index: 3  Product: Tablet
Hint

The syntax is:

for index, product in enumerate(products):
    print(...)
"""
#op1
products = ["Phone", "Laptop", "Watch", "Tablet"]

for index, product in enumerate(products):
    print(f"Index {index} → {product}")

#op2
for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")

#op3
for index, product in enumerate(products):
    print(f"Index: {index} Product: {product}")


