'''
⭐ While Loop Question 1 (Competitor Scraping)
Scenario

You're scraping a competitor website (Nike.com).

Sometimes the request fails due to a timeout.

Your manager says:

"Retry 5 times. If it still fails, stop and print a failure message."

Expected Output
Attempt 1 to scrape Nike.com
Retrying...

Attempt 2 to scrape Nike.com
Retrying...

Attempt 3 to scrape Nike.com
Retrying...

Attempt 4 to scrape Nike.com
Retrying...

Attempt 5 to scrape Nike.com
Retrying...

Failed to scrape Nike.com after 5 attempts.
'''

attempt = 1

while attempt <= 5:
    print(f"Attempt {attempt} to scrape Nike.com")
    print(f"Retrying...")
    attempt += 1

print(f"Failed to scrape Nike.com after 5 attempts.")


