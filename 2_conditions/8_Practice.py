products = [
    {
        "title": "Samsung Galaxy S25",
        "price": 89999
    },
    {
        "title": "Apple iPhone 17 Pro Max",
        "price": 159999
    },
    {
        "title": "Apple iPhone 17",
        "price": 149999
    },
    {
        "title": "OnePlus 13",
        "price": 69999
    }
]

for product in products:

    if "iphone" in product["title"].lower():
        print(f"Product Title: {product['title']}")
        print(f"Price: {product['price']}")
        print("Product Found")
        break