'''
📝 Section B – Question 6 (Hard)

A competitor website has 4 pages.

Each page contains 6 products.

Write a program that:

Page-Level Rule
Page 2 shows a CAPTCHA.
Retry solving the CAPTCHA 2 times.
On the 2nd attempt, the CAPTCHA is solved.
Print:
CAPTCHA Solved.
Continue scraping Page 2 normally.
Product-Level Rules
Page 3 – Product 3
Returns 403 Forbidden
Skip only that product.
Page 4 – Product 2
Is already scraped.
Print:
Product 2 already scraped.
Skipping Duplicate.
Skip only that product.
Page 4 – Product 6
Is the Target Product.
Print:
Target Product Found!
Stopping Scraping...
Stop the entire program immediately.
Expected Output
Scraping Page 1
Scraping Product 1
...
Scraping Product 6

Scraping Page 2
CAPTCHA Detected.
Attempt 1...
Attempt 2...
CAPTCHA Solved.
Scraping Product 1
...
Scraping Product 6

Scraping Page 3
Scraping Product 1
Scraping Product 2
Product 3 returned 403 Forbidden.
Skipping Product 3
Scraping Product 4
Scraping Product 5
Scraping Product 6

Scraping Page 4
Scraping Product 1
Product 2 already scraped.
Skipping Duplicate.
Scraping Product 3
Scraping Product 4
Scraping Product 5
Target Product Found!
Stopping Scraping...
'''

page = 1

found = False

while page <= 4 and not found:
    print(f"\nScraping Page {page}")


    if page == 2:
        print(f"CAPTCHA Detected.")

        captcha_solved = False

        attempt = 1
        while attempt <= 2:
            print(f"Attempt {attempt}...")

            if attempt == 2:
                captcha_solved = True
                break
            attempt += 1

        if captcha_solved:
            print(f"CAPTCHA Solved.")
        else:
            print("CAPTCHA Failed.")
            print("Skipping Page 2")
            page += 1
            continue


    product = 1

    while product <= 6 and not found:

        if page == 3 and product == 3:
            print(f"Product {product} returned 403 Forbidden.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 4 and product == 2:
            print(f"Product {product} already scraped.")
            print(f"Skipping Duplicate.")
            product += 1
            continue

        if page == 4 and product == 6:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            found = True
            break

        print(f"Scraping Product {product}")
        product += 1

    page += 1


