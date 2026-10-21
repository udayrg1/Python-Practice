#page initialization
page = 1  

#product not found so it is false, initialization
found = False

#we have total 5 pages
while page <= 5 and not found: 
    #printing the page no where crawling and scraping is happening
    print(f"\nScraping Page {page}")   

    if page == 2:
        #when we entered into page 2 detected captcha
        print(f"CAPTCHA Detected.") 

        #captch ust detected but not solved so it false, initialization
        captcha_solved = False  

        #we have total 3 attempts to retry the captcha page
        attempt = 1
        while attempt <= 3 and not captcha_solved:
            print(f"Attempt {attempt}...")

            #if captcha is solved stop immediately and jump to next if loop
            if attempt == 3:
                captcha_solved = True
                break
            attempt += 1

        #if captcha solved print if block, if not print else block and stop the loop
        if captcha_solved:
            print(f"CAPTCHA Solved.")
        else:
            print("CAPTCHA Failed.")
            page += 1
            continue

    #product initialization
    product = 1

    #total 6 products per page
    while product <= 6 and not found:

        #page 3, product 2 retruning 404 we need to print and skip
        if page == 3 and product == 2:
            print(f"Product {product} returned 404 Not Found.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        #page 3, product 5 retruning 500 internal server error we need retry, print and move forward with success/failed state
        if page == 3 and product == 5:
            print(f"Product {product} returned 500 Internal Server Error.")

            #retrying the 500 internal server error product 
            retry = 1
            while retry <= 2:
                print(f"Retry {retry}...") #printing retry attempts
                retry += 1 #retry increment
            print(f"Retry Successful!") #printing retry success status
            print(f"Scraping Product {product}")
            product += 1 #moving with next product scraping within the same page
            continue
        #printing the duplicate product status and skipping
        if page == 4 and product == 1:
            print(f"Product {product} already scraped.")
            print(f"Skipping Duplicate.")
            product += 1 #moving with next product scraping within the same page
            continue

        #printing the oos product status and skipping
        if page == 4 and product == 4:
            print(f"Product {product} is Out of Stock.")
            print(f"Skipping Product {product}")
            product += 1
            continue

        #page 5, product 3 retruning 429 error we need retry, print and move forward with success/failed state
        if page == 5 and product == 3:
            print(f"Product {product} returned 429 Too Many Requests.")

            #retrying the 429 error product 
            retry = 1
            while retry <= 2:
                print(f"Retry {retry}...")
                retry += 1
            print(f"Still Rate Limited.")  #429 not fixed printing the message
            print(f"Skipping Product {product}") #skipping the 429 error product url
            product += 1
            continue

        #found the actual target product and used break to stop the loop or come out of the loop
        if page == 5 and product == 6:
            print(f"Target Product Found!")
            print(f"Stopping Scraping...")
            found = True
            break

        #printing the each product scraped in all pages
        print(f"Scraping Product {product}")
        product += 1

    page += 1 #page increment, as mentioned at first we have 5 pages



        









