'''
😈 Challenge 2 (Real Web Scraping)

Now let's make it closer to what you'll actually do.

products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True}
]

🎯 Requirements

Using one list comprehension only, create a new list containing only the product titles where:

✅ price >= 1000
✅ stock == True

Expected Output
['Nike', 'Adidas']
'''

products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True}
]

instock_expensitve_products = [product['title'] for product in products if product['price'] >= 1000 and product['stock'] == True]

print(instock_expensitve_products)