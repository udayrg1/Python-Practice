'''
Final Boss – List Comprehension
products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True},
    {"title": "Asics", "price": 3200, "stock": True},
    {"title": "New Balance", "price": 1400, "stock": True},
    {"title": "Converse", "price": 1700, "stock": False}
]

Requirements

Using one list comprehension only:

Keep only products whose price is greater than or equal to ₹1500
Product must be in stock
Convert the title to uppercase
Store only the titles
Expected Output
['NIKE', 'ADIDAS', 'ASICS']
'''

products = [
    {"title": "Nike", "price": 2500, "stock": True},
    {"title": "Puma", "price": 900, "stock": False},
    {"title": "Adidas", "price": 1800, "stock": True},
    {"title": "Reebok", "price": 700, "stock": True},
    {"title": "Asics", "price": 3200, "stock": True},
    {"title": "New Balance", "price": 1400, "stock": True},
    {"title": "Converse", "price": 1700, "stock": False}
]

products_title = [product['title'].upper() for product in products if product['price']>=1500 and product['stock'] == True]

print(products_title)