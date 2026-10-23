'''
Step 4: Your basic practice problem
Let's use a different scenario from our previous employee and inventory challenges.
Scenario: Browser History
A browser stores the pages visited during a session.
browser_history = {    "page_1": "Home",    "page_2": "Products",    "page_3": "Offers",    "page_4": "Checkout"}


Requirements
1. Remove the last inserted entry using popitem().
2. Store the returned tuple in a variable.
3. Print the removed entry.
4. Print the updated browser history.
5. Print the number of entries remaining using len().
Rules:
- Use popitem() exactly once.
- Don't use pop(), del, or loops.
- Write the complete program yourself.

'''

browser_history = {
    "page_1": "Home",
    "page_2": "Products",
    "page_3": "Offers",
    "page_4": "Checkout"
}

result = browser_history.popitem()

print(result)

print(browser_history)

print(len(browser_history))