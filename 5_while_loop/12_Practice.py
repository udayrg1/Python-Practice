page = 1

found = False

while page <= 4 and not found:
    print(f"\nScraping Page {page}")

    if page == 2:
        print(f"\nCAPTCHA Detected.")
        
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

    while product <= 8 and not found:

        if page == 3 and product == 2:
            print(f"Product {product} returned 404 Not Found.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 3 and product == 5:
            print(f"Product {product} 500 Internal Server Error.")
            retry = 1
            while retry <= 2:
                print(f"Retry {retry}...")
                retry += 1
            print(f"Retry Successful!")
            print(f"\nScraping Product {product}")
            product += 1
            continue

        if page == 4 and product == 1:
            print(f"Product {product} already scraped.")
            print(f"Skipping Duplicate.")
            product += 1
            continue

        if page == 4 and product == 3:
            print(f"Product {product} is Out of Stock.")
            print(f"Skipping Product {product}.")
            product += 1
            continue
 
        if page == 4 and product == 6:
            print(f"Product {product} returned 403 Forbidden.")
            retry = 1
            while retry <= 2:
                print(f"Retry {retry}...")
                retry += 1
            print(f"Still Blocked.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 4 and product == 8:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            found = True
            break

        print(f"\nScraping Product {product}")
        product += 1

    page += 1




        


            