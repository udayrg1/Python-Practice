'''
📝 Section B – Question 4 (Medium)

A competitor website has 4 pages.

Each page contains 5 products.

Write a program that:

Scrapes Page 1 to Page 4
On Page 2, Product 4 returns a 500 Internal Server Error
Retry that product 2 times
If both retries fail:
Print "Failed after 2 retries."
Skip only Product 4
Continue scraping the remaining products
After all pages are completed, end the program

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
Product 4 returned 500 Internal Server Error.
Retry 1...
Retry 2...
Failed after 2 retries.
Skipping Product 4
Scraping Product 5

Scraping Page 3
Scraping Product 1
Scraping Product 2
Scraping Product 3
Scraping Product 4
Scraping Product 5

Scraping Page 4
Scraping Product 1
Scraping Product 2
Scraping Product 3
Scraping Product 4
Scraping Product 5

Rules
✅ Use nested while loops
✅ Use another nested while for retries
✅ Use continue
❌ No for loops
❌ No hints
❌ No explanations
❌ No corrections until you submit

Good luck. 💪
'''

page = 1

while page <= 4:
    print(f"\nScraping Page {page}")


    product = 1

    while product <= 5:
        if page == 2 and product == 4:
            print(f"Product {product} returned 500 Internal Server Error.")

            retry = 1

            while retry <= 2:
                print(f"Retry {retry}...")
                retry += 1

            print(f"Failed after 2 retries.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        print(f"Scraping Product {product}")
        product += 1

    page += 1
