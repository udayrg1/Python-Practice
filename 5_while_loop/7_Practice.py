'''
🎯 Next Question (Slightly Harder)

Imagine a competitor website has 10 pages, but Page 6 contains the product you're searching for.

Task:

Scrape pages one by one.

When you reach Page 6, print:

Product Found on Page 6
Stop scraping immediately using break.

expected output is:

Scraping Competitor Page 1
Scraping Competitor Page 2
Scraping Competitor Page 3
Scraping Competitor Page 4
Scraping Competitor Page 5
Scraping Competitor Page 6
Product Found on Page 6
Stopping further scraping...
🧠 Explanation
Pages 1 to 5 → Scrape normally.
Page 6 → Scrape the page first.
Then you find the product.

Print:

Product Found on Page 6

Then print:

Stopping further scraping...
Finally, use break to stop the loop.
Pages 7, 8, 9, and 10 should not be scraped.

🎯 Your task: Write the code for this scenario. As before, I'll review it line by line instead of giving the solution immediately.
'''

page = 1

while page <= 10:
    print(f"Scraping Competitor Page {page}")
    page += 1

    if page == 6:
        print(f"Product Found on Page {page}")
        print(f"Stopping further scraping...")
        break