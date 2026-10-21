'''
📝 Section B – Question 3 (Medium)

A competitor website has 3 pages.

Each page contains 4 products.

Write a program that:

Scrapes Page 1 to Page 3
For Page 2, Product 3 is Out of Stock
    Print the message
    Skip only that product
Continue scraping the remaining products
After all pages are completed, end the program

Expected Output
Scraping Page 1
Scraping Product 1
Scraping Product 2
Scraping Product 3
Scraping Product 4

Scraping Page 2
Scraping Product 1
Scraping Product 2
Product 3 is Out of Stock.
Skipping Product 3
Scraping Product 4

Scraping Page 3
Scraping Product 1
Scraping Product 2
Scraping Product 3
Scraping Product 4

Rules
✅ Use nested while loops
✅ Use continue
❌ No for loops
❌ No hints
❌ No explanations until you submit
'''

page = 1

while page <= 3:
    print(f"\nScraping Page {page}")

    product = 1

    while product <=4:

        if page ==2 and product == 3:
            print(f"Product {product} is Out of Stock.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        print(f"Scraping Product {product}")
        product += 1

    page += 1
