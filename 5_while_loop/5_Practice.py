'''
Ready for Question 2? 🚀

This one is a bit more realistic and introduces break with while.

Scenario

You're scraping a competitor website.

While scraping:

Pages 1 to 10 exist.
On Page 6, you find the product you're searching for.
Once the product is found, stop scraping immediately.

Expected Output
Checking Competitor Page 1
Checking Competitor Page 2
Checking Competitor Page 3
Checking Competitor Page 4
Checking Competitor Page 5
Checking Competitor Page 6
Product Found!
'''

page = 1

while page <=10:
    print(f"Checking Competitor Page {page}")
    if page == 6:
        print(f"Product Found!")
        break
    page += 1



