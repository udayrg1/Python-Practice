'''
⭐ Python Practice Challenge – Competitor Retry & Target Finder
Scenario

You are writing a Python program to simulate scraping a competitor website.

The website contains:

3 Pages
5 Products on each page
Requirements
1. Scrape Pages and Products

Print the current page and product being scraped.

Example:

Scraping Page 1
Scraping Product 1
2. Retry Logic

On Page 2, Product 4 returns a 500 Internal Server Error.

When this happens:

Print:
Product 4 returned 500 Error.
Retry the product 3 times.

Example:

Retry 1...
Retry 2...
Retry 3...
After the third retry, print:
Failed after 3 retries. Skipping Product 4
Continue scraping from Product 5.
3. Out of Stock Product

On Page 3, Product 1 is Out of Stock.

Print:

Product 1 is Out of Stock. Skipping...

Skip that product and continue with Product 2.

4. Target Product

On Page 3, Product 5 is the target product.

Print:

Target Product Found!
Stopping Scraping...

Immediately stop all scraping.

Page 3 should stop immediately after finding the target product.

Rules
✅ Use only while loops.
✅ Use nested while loops.
✅ Use another while loop for the retry logic.
✅ Use if statements.
✅ Use continue.
✅ Use break.
✅ Use a flag variable (for stopping the outer loop).
❌ Do NOT use for loops.
❌ Do NOT use functions.
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

Product 4 returned 500 Error.
Retry 1...
Retry 2...
Retry 3...
Failed after 3 retries. Skipping Product 4

Scraping Product 5

Scraping Page 3

Product 1 is Out of Stock. Skipping...

Scraping Product 2
Scraping Product 3
Scraping Product 4

Target Product Found!
Stopping Scraping...
'''


page = 1
found = False

while page <= 3 and not found:
        print(f"\nScraping Page {page}")

        product = 1

        while product <= 5:
            if page ==2 and product == 4:
                print(f"Product {product} returned 500 Error.")


                retry = 1
                while retry <=3:
                    print(f"Retry {retry}...")
                    retry += 1
                    
                print(f"Failed after 3 retries. Skipping Product 4")
                product += 1
                continue

            if page == 3 and product == 1:
                print(f"Product {product} is Out of Stock. Skipping...")
                product += 1
                continue

            if page == 3 and product == 5:
                print(f"Target Product Found!")
                print(f"Stopping Scraping...")
                found = True
                break


            print(f"\nScraping Product {product}")
            product += 1
        page += 1


