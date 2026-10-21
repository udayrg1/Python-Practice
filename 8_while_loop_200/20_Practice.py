'''
Let's reset Q20 completely. 🐍⚔️
🐍⚔️ Q20/200 — Web Scraping: Pagination With Missing Pages

Imagine you're scraping a competitor's product website.

The website has pages:

Page 1
Page 2
Page 3
Page 4
Page 5
Page 6
...

But sometimes a page fails to load.

Your scraper should:

Start from page 1
Attempt to scrape pages sequentially
If a page succeeds → print "Scraped page X"
If a page fails → print "Page X failed" and retry that same page
A page can fail maximum 2 times
After 2 failures, skip that page and move to the next page
Stop after successfully moving beyond page 10
Use a while loop
Do not use for
Do not use a list
Example behavior
Scraped page 1
Scraped page 2
Page 3 failed - retry 1
Scraped page 3
Scraped page 4
Page 5 failed - retry 1
Page 5 failed - retry 2
Skipping page 5
Scraped page 6
...
Scraped page 10
🧠 New concepts

This is not a digit problem.

You'll need to think about:

A page counter
A retry counter
Nested while loops
Resetting a counter for each new page
Deciding when to retry vs move forward

🔥 This is the kind of problem-solving we're going to use from Q20 onward.

And yes — I'll keep the next questions genuinely different rather than giving you number % 10 in 50 different disguises. 😂🐍⚔️
'''

page_number = 1

while page_number <= 10:

    retry = 0

    if page_number == 3 or page_number == 7:

        print(f"Page {page_number} failed - retry 1")

        retry = 1

        while retry <= 1:
            print(f"Scraped page {page_number}")
            retry += 1

    elif page_number == 5 or page_number == 10:

        retry = 1

        while retry <= 2:
            print(f"Page {page_number} failed - retry {retry}")
            retry += 1

        print(f"Skipping page {page_number}")

    else:
        print(f"Scraped page {page_number}")

    page_number += 1