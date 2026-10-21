'''
📝 Section B – Question 1 (Easy)

A competitor website has 5 pages.

Write a program that:

Scrapes pages 1 to 5
Skips page 3 because it returns 404 Not Found
Continues scraping the remaining pages

Expected Output
Scraping Page 1
Scraping Page 2
Page 3 returned 404 Not Found.
Skipping Page 3
Scraping Page 4
Scraping Page 5


Rules
✅ Use a while loop
✅ Use continue
❌ Do not use for loop
'''

page = 1

while page <= 5:

    if page == 3:
        print(f"Page 3 returned 404 Not Found.")
        print(f"Skipping Page 3")
        page += 1
        continue

    print(f"Scraping Page {page}")
    page += 1

