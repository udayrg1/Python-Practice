'''
🚀 Let's Start

This is your first List Comprehension using a list of dictionaries.

products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True}
]
🎯 Challenge 1

Create a new list containing only the product titles.

Expected Output
['Nike', 'Puma', 'Adidas', 'Reebok']
Rules
✅ Use one list comprehension
❌ No for loop
❌ No append()
'''

products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True}
]


titles = [product['title'] for product in products]

print(titles)