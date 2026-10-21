'''
⭐ While Loop - Question 3
🎯 Scenario

You're scraping a competitor website.

The competitor has 10 pages.

During scraping:

Page 3 returns 403 Forbidden
Page 7 returns 403 Forbidden

Your manager says:

"Skip the blocked pages and continue scraping the remaining pages."

✅ Expected Output
Scraping Competitor Page 1
Scraping Competitor Page 2
Skipping Competitor Page 3 (403 Forbidden)
Scraping Competitor Page 4
Scraping Competitor Page 5
Scraping Competitor Page 6
Skipping Competitor Page 7 (403 Forbidden)
Scraping Competitor Page 8
Scraping Competitor Page 9
Scraping Competitor Page 10
'''


#method1
page = 1

while page <= 10:
    if page in (3,7):
        print(f"Skipping Competitor Page {page} (403 Forbidden)")
        page += 1
        continue
    print(f"Scraping Competitor Page {page}")
    page += 1


print("                                 ")
print("                                 ")
print("                                 ")

#method2

page = 1

while page <= 10:
    if page == 3 or page == 7:
        print(f"Skipping Competitor Page {page} (403 Forbidden)")
    else:
        print(f"Scraping Competitor Page {page}")

    page += 1