"""
⭐⭐⭐⭐⭐ Question 5: Product Category using elif
Problem

Given:

product = {
    "title": "iPhone 17 Pro Max Ice Blue 512 GB",
    "price": 159999
}

Perform the following:

If the product price is greater than 100000, print "Premium Mobile".
Else if the product price is greater than 50000, print "Mid-Range Mobile".
Else, print "Budget Mobile".
Also print the product title.
Expected Output
Product Title: iPhone 17 Pro Max Ice Blue 512 GB
Category: Premium Mobile
"""

product = {

    "title" : "iPhone 17 Pro Max Ice Blue 512 GB",
    "price" : 159999
}

print(f"Product Title: {product['title']}")

if product["price"] > 100000:
    print(f"Category: Premium Mobile")
elif product["price"] > 50000:
    print(f"Category: Mid-Range Mobile")
else:
    print(f"Category: Budget Mobile")