"""
Question 9 — List of Dictionaries

This is where real web scraping starts.

Why is this important?

Suppose you have

1000 Product URLs

Every URL returns one product.

Example:

URL 1
↓

{
    "title": "...",
    "brand": "...",
    "price": ...
}
URL 2
↓

{
    "title": "...",
    "brand": "...",
    "price": ...
}
URL 3
↓

{
    "title": "...",
    "brand": "...",
    "price": ...
}

How do we store all of them?

We create a list.

Inside the list, every element is a dictionary.

products = [

    {
        ...
    },

    {
        ...
    },

    {
        ...
    }

]

This is called a List of Dictionaries.

Real Production Example

Suppose you scrape Amazon.

After scraping, your variable may look like this:

products = [

    {
        "asin": "B0D12345",
        "title": "iPhone 15",
        "brand": "Apple",
        "price": 79999,
        "rating": 4.8,
        "availability": True
    },

    {
        "asin": "B0D56789",
        "title": "Galaxy S25",
        "brand": "Samsung",
        "price": 74999,
        "rating": 4.7,
        "availability": False
    }

]

Later you'll simply save:

products

to

JSON
CSV
Database

Interview Definition

A list of dictionaries is a list in which each element is a dictionary. It is commonly used to store multiple records such as products, employees, students, or API responses.
"""
"""
Question 9
Problem

Create a list of dictionaries containing 3 products.

Product 1
name : iPhone 15
Brand : Apple
Price : 79999
In Stock : True

Product 2
name : Galaxy S25
Brand : Samsung
Price : 74999
In Stock : False

Product 3
name : OnePlus 13
Brand : OnePlus
Price : 69999
In Stock : True

Perform the following tasks
Create the list.
Print the complete list.
Print only the first product.
Print only the second product.
Print only the third product.

Expected Output
Products:
[
 {...},
 {...},
 {...}
]

First Product:
{'name': 'iPhone 15', ...}

Second Product:
{'name': 'Galaxy S25', ...}

Third Product:
{'name': 'OnePlus 13', ...}
Rules

For this question, use only:

List
Dictionary
Indexing

❌ Don't use:

products[0]["name"]

One Small Hint

Think of it like this:

List
 │
 ├── Dictionary
 ├── Dictionary
 └── Dictionary
"""

product_1 = {
"name" : "iPhone 15",
"brand" : "Apple",
"price" : 79999,
"in_stock" : True}

product_2 = {
"name" : "Galaxy S25",
"brand" : "Samsung",
"price" : 74999,
"in_stock" : False}


product_3 = {
"name" : "OnePlus 13",
"brand" : "OnePlus",
"price" : 69999,
"in_stock" : True}

products = [product_1,product_2,product_3]

print(f"Products: {products}")

print(f"First Product: {products[0]}")
print(f"Second Product: {products[1]}")
print(f"Third Product: {products[2]}")
