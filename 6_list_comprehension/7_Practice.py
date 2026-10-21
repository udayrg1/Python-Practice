'''
🎯 Challenge 4 (Real Automation Example)

This one is closer to the kind of work you'd do in automation.

prices = [499, 999, 1499, 2999, 799, 3999]

Using List Comprehension only, create a new list containing only prices greater than or equal to ₹1000.

Expected Output:

[1499, 2999, 3999]
'''

prices = [499, 999, 1499, 2999, 799, 3999]

huge_prices = [price for price in prices if price >= 1000]

print(huge_prices)