products = [
    {"title": "Nike", "price": 2500},
    {"title": "Puma", "price": 900},
    {"title": "Adidas", "price": 1800}
]

#Using one list comprehension only, create a new list containing only the product titles whose price is greater than or equal to 1500.

#Expected Output ['Nike', 'Adidas']

expense_products = [product['title'] for product in products if product['price']>=1500]

print(expense_products)