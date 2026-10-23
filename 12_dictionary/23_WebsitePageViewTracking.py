'''
Next: A unique setdefault() challenge
We'll use a different real-world scenario and introduce a new problem-solving requirement rather than repeating the user-preferences exercise.

Scenario: Website Page-View Tracking

A website receives visits to different pages. You need to maintain a dictionary that counts how many visits each page receives.

For example, when a page is visited for the first time, its counter should start at 1. When that page is visited again, its count should increase.

We'll use setdefault() as part of the solution, but you'll write the code yourself. I'll provide the complete requirements next,
without giving away the solution. 💪

page_visits = ["Home", "Products", "Home", "Cart", "Products", "Home"]

Expected result:

{
    "Home": 3,
    "Products": 2,
    "Cart": 1
}
'''

page_visits = ["Home", "Products", "Home", "Cart", "Products", "Home"]

page_views = {}

for view in page_visits:
    if view in page_views:
        page_views[view] += 1
    else:
        page_views.setdefault(view, 1)

print(page_views)

