page = 1

found = False

while page <= 6 and not found:
    print(f"\nScraping Page {page}")

    if page == 2:
        print(f"CAPTCHA Detected.")

        captcha_solved = False

        attempt = 1

        while attempt <= 3 and not captcha_solved:
            print(f"Attempt {attempt}...")

            if attempt == 3:
                captcha_solved = True
                break
            attempt += 1

        if captcha_solved:
            print(f"CAPTCHA Solved.")
        else:
            print(f"CAPTCHA Failed.")
            page += 1
            continue

    if page == 5:
        print(f"503 Service Unavailable.")
        print(f"Skipping Entire Page {page}")
        page += 1
        continue

    product = 1

    while product <= 8 and not found:

        if page == 1 and product == 7:
            print(f"Product {product} already scraped.")
            print(f"Skipping Duplicate.")
            product += 1
            continue

        if page == 2 and product == 5:
            print(f"Product {product} returned 500 Internal Server Error.")

            retry = 1
            while retry <= 2:
                print(f"Retry {retry}...")
                retry += 1
            print(f"Retry Successful!")
            print(f"Scraping Product {product}")
            product += 1
            continue

        if page == 3 and product == 2:
            print(f"Product {product} is Out of Stock.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 3 and product == 6:
            print(f"Product {product} returned 404 Not Found.")
            print(f"Skipping Product 6")
            product += 1
            continue

        if page == 4 and product == 3:
            print(f"Product {product} returned 429 Too Many Requests.")

            retry = 1
            while retry <= 2:
                print(f"Retry {retry}...")
                retry += 1
            print(f"Still Rate Limited.")
            print(f"Skipping Product 3")
            product += 1
            continue

        if page == 4 and product == 7:
            print(f"Product {product} returned 403 Forbidden.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 6 and product == 2:
            print(f"Product {product} already scraped.")
            print(f"Skipping Duplicate.")
            product += 1
            continue

        if page == 6 and product == 4:
            print(f"Product {product} returned 500 Internal Server Error.")

            retry = 1
            while retry <= 3:
                print(f"Retry {retry}...")
                retry += 1
            print(f"Retry Successful!")
            print(f"Scraping Product {product}")
            product += 1
            continue

        if page == 6 and product == 8:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            found = True
            break

        print(f"Scraping Product {product}")
        product += 1

    page += 1






