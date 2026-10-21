"""
Question 10: Access Data from a List of Dictionaries

This is one of the most frequently used patterns in web scraping.

Real-Time Scenario

Suppose you've scraped 1000 products.

Your data looks like this:

products = [
    {
        "name": "iPhone 15",
        "brand": "Apple",
        "price": 79999,
        "in_stock": True
    },
    {
        "name": "Galaxy S25",
        "brand": "Samsung",
        "price": 74999,
        "in_stock": False
    },
    {
        "name": "OnePlus 13",
        "brand": "OnePlus",
        "price": 69999,
        "in_stock": True
    }
]

Now your manager asks:

"Can you tell me the brand of the second product?"

or

"Can you print the price of the third product?"

This is exactly what you'll practice.

Problem

Using the same products list from Question 9, print the following:

Name of the first product.
Brand of the second product.
Price of the third product.
Stock status of the first product.
Total number of products.

Expected Output
First Product Name: iPhone 15

Second Product Brand: Samsung

Third Product Price: 69999

First Product Stock: True

Total Products: 3

Rules

Use:

products[0]["name"]

products[1]["brand"]

products[2]["price"]

len(products)

No loops.

No .get().

No .items().

Just indexing.

Big Hint ⭐⭐⭐⭐⭐

This is the first time we're combining List indexing and Dictionary keys.

Think of it in two steps.

Step 1

Select the product from the list.

products[0]

Output:

{
    "name": "iPhone 15",
    "brand": "Apple",
    "price": 79999,
    "in_stock": True
}

Notice that the result is now a dictionary.

Step 2

Access a value from that dictionary.

products[0]["name"]

Output:

iPhone 15
"""


products =[ 
    
{
"name" : "iPhone 15",
"brand" : "Apple",
"price" : 79999,
"in_stock" : True

},
{
"name" : "Galaxy S25",
"brand" : "Samsung",
"price" : 74999,
"in_stock" : False
},
{
"name" : "OnePlus 13",
"brand" : "OnePlus",
"price" : 69999,
"in_stock" : True
}
]

"""
Name of the first product.
Brand of the second product.
Price of the third product.
Stock status of the first product.
Total number of products.

Expected Output
First Product Name: iPhone 15

Second Product Brand: Samsung

Third Product Price: 69999

First Product Stock: True

Total Products: 3
"""

print(f"First Product Name: {products[0]['name']}")
print(f"Second Product Brand: {products[1]['brand']}")
print(f"Third Product Price: {products[2]['price']}")
print(f"First Product Stock: {products[0]['in_stock']}")
print(f"Total Products: {len(products)}")
