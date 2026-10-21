products = [
    {
        "title": "iPhone 17",
        "price": 159999
    },
    {
        "title": "Samsung S25",
        "price": 89999
    },
    {
        "title": "OnePlus 13",
        "price": 69999
    }
]

for product in products:
    if product["price"] > 100000:
        print(product["title"])