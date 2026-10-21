#list of dictionaries
product = [
    {
        "title": "iPhone 17",
        "price": 159999
    }
]

for attrib in product:
    if attrib["price"] > 100000:
        print(attrib["title"])