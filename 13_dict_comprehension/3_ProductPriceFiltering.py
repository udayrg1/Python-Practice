'''
4. Your basic challenge 🧠

Scenario: Product Price Filtering

An online store maintains the following product prices:
product_prices = {    "Laptop": 55000,    "Mouse": 800,    "Keyboard": 1500,    "Monitor": 12000,    "USB Cable": 300,    "Headphones": 2500}


Requirements
1. Create a new dictionary named expensive_products.
2. Use a dictionary comprehension to include only products priced above ₹2,000.
3. Keep the product names as keys and their original prices as values.
4. Print the new dictionary.
5. Print the number of products in the new dictionary using len().

Expected output
{    'Laptop': 55000,    'Monitor': 12000,    'Headphones': 2500}
3
'''

product_prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "USB Cable": 300,
    "Headphones": 2500
}

#Regular Approach
expensive_products = {}

for product, price in product_prices.items():
    if price > 2000:
        expensive_products[product] = price
print(expensive_products)


#dict comprehension
expensive_products1 = {products: prices for products, prices in product_prices.items() if prices > 2000}

print(expensive_products1)