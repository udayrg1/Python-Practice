'''
😎 Time to increase the difficulty for real.

No more toy questions.

⭐ Question 4 (Real Interview Level)

You're scraping a competitor website.

There are 10 pages.

Some pages fail due to server issues.

Page	Status
4    	500 Internal Server Error
8	    500 Internal Server Error

Requirement
Scrape pages 1–10.
If a page returns 500:
Retry that page 3 times.
If it still fails after 3 attempts:

Print:

Failed after 3 retries. Skipping Page 4
Continue with the next page.
All other pages should scrape normally.

Expected Output (Partial)

Scraping Competitor Page 1

Scraping Competitor Page 2

Scraping Competitor Page 3

Scraping Competitor Page 4
Retry 1...
Retry 2...
Retry 3...
Failed after 3 retries. Skipping Page 4

Scraping Competitor Page 5

...

Scraping Competitor Page 8
Retry 1...
Retry 2...
Retry 3...
Failed after 3 retries. Skipping Page 8

Scraping Competitor Page 9

Scraping Competitor Page 10

Rules
❌ Don't use for loops.
✅ Use nested while loops.
✅ Use continue where appropriate.
✅ Think about two loop variables:
One for the page number.
One for the retry count.

This is much closer to what you might implement in a real web scraping script.
'''

page = 1

while page <= 10:
    if page in (4,8):
        print(f"Scraping Competitor Page {page}")

        retry = 1
        while retry <= 3:
            print(f"Retry {retry}...")
            retry += 1

        print(f"Failed after {retry - 1} retries. Skipping Page {page}")
        page += 1
        continue

    print(f"Scraping Competitor Page {page}")
    page += 1