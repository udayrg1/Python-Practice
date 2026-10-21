"""
if condition sample program using for loop
"""

product = {

    "title" : "Iphone 17 pro max ice blue 532 GB global variant unlocked version",
    "price" : 159999
}


"""
1
"""
if product["price"] > 100000:
    print("Premium mobile")
else:
    print("Budget mobile")

"""
2
"""

for attrib in product:
    if product["price"] > 100000 and attrib == "title":
        print(f"Product Title: {product['title']}")

        