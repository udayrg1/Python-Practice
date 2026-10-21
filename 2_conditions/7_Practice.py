"""
Problem

A list of products has been scraped from a website.

Perform the following:
Loop through all the products.
If the product title is "iPhone 17 Pro Max":
Print the product title.
Print "Product Found".
Stop the loop immediately using break.

Product Title: iPhone 17 Pro Max
Product Found
"""

products = [
    {
        "title": "Samsung Galaxy S25",
        "price": 89999
    },
    {
        "title": "iPhone 17 Pro Max",
        "price": 159999
    },
    {
        "title": "OnePlus 13",
        "price": 69999
    },
    {
        "title": "Google Pixel 10",
        "price": 79999
    }
]

for product in products:

    if product['title'] == "iPhone 17 Pro Max":
        print(f"Product Title: {product['title']}")
        print("Product Found")
        break
    
    