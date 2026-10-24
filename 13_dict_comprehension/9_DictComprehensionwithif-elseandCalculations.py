'''
🚀 Next challenge: Dictionary Comprehension with if-else and Calculations
Let's combine what you've learned!

An e-commerce system stores product prices. Apply a 10% discount to products priced at ₹2,000 or above, and leave the other prices unchanged.
Input
product_prices = {    "Laptop": 55000,    "Mouse": 800,    "Keyboard": 1500,    "Monitor": 12000,    "Headphones": 2500,    "USB Cable": 300}


Requirements
1. Create final_prices using dictionary comprehension.
2. If the price is greater than or equal to ₹2,000, apply a 10% discount.
3. Otherwise, keep the original price.
4. Round the resulting prices to two decimal places.
5. Preserve the product names as keys.
6. Print the dictionary.
Expected output
{    'Laptop': 49500.0,    'Mouse': 800,    'Keyboard': 1500,    'Monitor': 10800.0,    'Headphones': 2250.0,    'USB Cable': 300}


Hint: Remember that the conditional expression goes before the for clause:

{key: value_if_true if condition else value_if_false
 for key, value in dictionary.items()}
'''

product_prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500,
    "USB Cable": 300
}

final_prices = {product: round(price - (price * 0.1), 2) if price >= 2000 else price for product, price in product_prices.items()}

print(final_prices)