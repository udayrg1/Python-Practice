'''
📝 Section B – Question 2 (Easy)

A competitor website has 5 pages.

Write a program that:

Scrapes pages 1 to 5
Page 2 returns a 500 Internal Server Error
Retry 3 times
If all retries fail, skip Page 2
Continue scraping the remaining pages


Expected Output
Scraping Page 1

Page 2 returned 500 Internal Server Error.
Retry 1...
Retry 2...
Retry 3...
Failed after 3 retries.
Skipping Page 2

Scraping Page 3
Scraping Page 4
Scraping Page 5
Rules
✅ Use while
✅ Use a nested while for retries
✅ Use continue
❌ Do not use for
'''

page = 1

while page <= 5:

    if page == 2:
        print(f"Page {page} returned 500 Internal Server Error.")

        retry = 1

        while retry <= 3:
            print(f"Retry {retry}..")
            retry += 1

        print(f"Failed after 3 retries.")
        print(f"Skipping Page 2")
        page += 1
        continue

    print(f"Scraping Page {page}")
    page += 1



    