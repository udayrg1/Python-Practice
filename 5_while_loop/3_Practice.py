pages = 1

while pages <= 10:

    if pages % 2 == 0:
        pages += 1
        continue

    print(f"Scraping Page: {pages}")
    pages += 1