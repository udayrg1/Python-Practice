'''
🚀 Next challenge: Dictionary Comprehension with Calculations
Let's increase the difficulty slightly.

Imagine you're building an e-commerce application. You have the original prices of several products, and you need to calculate their prices after applying a 10% discount.
Input

product_prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

Requirements
1. Create a new dictionary named discounted_prices.
2. Use dictionary comprehension.
3. Calculate a 10% discount for every product.
4. Store the product names as keys and the discounted prices as values.
5. Round the discounted prices to two decimal places.
6. Print the new dictionary.

Expected output
{
    'Laptop': 49500.0,
    'Mouse': 720.0,
    'Keyboard': 1350.0,
    'Monitor': 10800.0,
    'Headphones': 2250.0
}
'''

product_prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

discounted_prices = {}

#regular approach
for product, price in product_prices.items():
    discounted_prices[product] = round(price - (price * 0.1), 2)

print(discounted_prices)


#dict comprehensions

discounted_prices = {product: round(price -(price * 0.1), 2) for product, price in product_prices.items()}

print(discounted_prices)
