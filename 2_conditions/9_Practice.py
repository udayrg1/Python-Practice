"""
Question 7: continue
Problem

Given:

products = [
    {
        "title": "Samsung Galaxy S25",
        "in_stock": True
    },
    {
        "title": "iPhone 17 Pro Max",
        "in_stock": False
    },
    {
        "title": "OnePlus 13",
        "in_stock": True
    },
    {
        "title": "Google Pixel 10",
        "in_stock": False
    }
]

Perform the following:
Loop through all the products.
If the product is out of stock (in_stock == False):
Skip that product using continue.
Otherwise print:
Product Title: <title>
Available
Expected Output
Product Title: Samsung Galaxy S25
Available

Product Title: OnePlus 13
Available
"""

products = [

    {
        "title" : "Samsung Galaxy S25",
        "in_stock": True
    },
    {
        "title" : "iPhone 17 Pro Max",
        "in_stock": False
    },
    {
        "title" : "OnePlus 13",
        "in_stock" : True
    },
    {
        "title" : "Google Pixel 10",
        "in_stock" : False
    }
]

for product in products:

    if product["in_stock"] == False:
        continue
    else: 
        print(f"Product Title: {product['title']}")
        print("Available")
    



