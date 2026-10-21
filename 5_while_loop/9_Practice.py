'''
⭐ Challenge Question 5 - Competitor Product Scraper
Scenario

You're scraping a competitor website.

The website has 5 pages.
Each page contains 4 products.

While scraping:

On Page 2, Product 3 is Out of Stock → Skip it.
On Page 4, Product 2 is the target product you're searching for.
Once you find the target product:
Print "Target Product Found!"
Stop all scraping immediately.

Expected Output
Scraping Page 1
    Scraping Product 1
    Scraping Product 2
    Scraping Product 3
    Scraping Product 4

Scraping Page 2
    Scraping Product 1
    Scraping Product 2
    Product 3 is Out of Stock. Skipping...
    Scraping Product 4

Scraping Page 3
    Scraping Product 1
    Scraping Product 2
    Scraping Product 3
    Scraping Product 4

Scraping Page 4
    Scraping Product 1
    Target Product Found!
Stopping Scraping...

Notice:

Page 5 should never be visited.
On Page 4, Products 3 and 4 should never be scraped.
As soon as the target is found, everything stops.


page = 1

while page <= 5:
    print(f"Scraping Page {page}")

    product = 1
    while product <= 4:

        product += 1

        if page == 2 and product == 3:
            print(f"Product {product} is Out of Stock. Skipping...")
            product += 1
            continue

        if page == 4 and product == 2:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            break

        print(f"Scraping Product {product}")
        product += 1
    page += 1
'''

page = 1

found = False

while page <= 5 and not found:
    print(f"\nScraping Page {page}")

    product = 1

    while product <= 4:

        if page == 2 and product == 3:
            print(f"Product {product} is Out of Stock. Skipping...")
            product += 1
            continue

        if page == 4 and product == 2:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            found = True
            break

        print(f"\nScraping Product {product}")
        product += 1
    page += 1    
