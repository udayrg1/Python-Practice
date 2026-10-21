page = 1

found = False


while page <= 4 and not found:
    print(f"\nScraping Page {page}")

    if page == 2:
        print(f"\nCAPTCHA Detected.")

        attempt = 1
        while attempt <= 3:
            print(f"Attempt {attempt}...") 
            attempt += 1

        print(f"CAPTCHA Failed.")               
        print(f"Skipping Page 2")
        page += 1
        continue

    product = 1
    while product <= 6:
        if page == 3 and product == 4:
            print(f"Product {product} returned 403 Forbidden.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        if page == 4 and product == 2:
            print(f"Product {product} already scraped")
            print("Skipping Duplicate.")
            product += 1
            continue

        if page == 4 and product == 6:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            found = True
            break

        print(f"\nScraping Product {product}")
        product += 1
    page += 1


        
