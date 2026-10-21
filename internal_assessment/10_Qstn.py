'''
📝 Section B – Question 5 (Hard)

A competitor website has 4 pages.

Each page contains 5 products.

Write a program that:

Scrapes Page 1 to Page 4
Scrapes Product 1 to Product 5
On Page 3, Product 2 is Out of Stock
Print:
Product 2 is Out of Stock.
Skipping Product 2
Skip only that product.
On Page 4, Product 4 is the Target Product
Print:
Target Product Found!
Stopping Scraping...
Stop the entire program immediately.
Do not scrape any remaining products or pages after the target is found.
Expected Output
Scraping Page 1
Scraping Product 1
Scraping Product 2
Scraping Product 3
Scraping Product 4
Scraping Product 5

Scraping Page 2
Scraping Product 1
Scraping Product 2
Scraping Product 3
Scraping Product 4
Scraping Product 5

Scraping Page 3
Scraping Product 1
Product 2 is Out of Stock.
Skipping Product 2
Scraping Product 3
Scraping Product 4
Scraping Product 5

Scraping Page 4
Scraping Product 1
Scraping Product 2
Scraping Product 3
Target Product Found!
Stopping Scraping...
Rules
✅ Nested while loops
✅ found flag
✅ break
✅ continue
❌ No for loops
❌ No hints
❌ No explanations
❌ No corrections until you submit

Take your time. Once you submit this, we'll evaluate it, and then you can call it a night. 🌙💪

'''


page = 1

found = False

while page <= 4 and not found:
    print(f"\nScraping Page {page}")

    product = 1

    while product <= 5:
        if page == 3 and product == 2:
            print(f"Product {product} is Out of Stock.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 4 and product == 4:
            print(f"Target Product Found!")
            print("Stopping Scraping...")
            found = True
            break

        print(f"Scraping Product {product}")
        product += 1

    page += 1







































