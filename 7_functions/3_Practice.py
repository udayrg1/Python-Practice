'''
🎯 Practice #2 — Slightly harder

Now let's increase the difficulty.

Create a function:

calculate_total(price, quantity)

It should:

accept price
accept quantity
calculate the total price
return the total
don't use print() inside the function

Then calculate the total for 3 products.

For example:

Product 1 → price = 500, quantity = 3
Product 2 → price = 1200, quantity = 2
Product 3 → price = 750, quantity = 4

Expected totals:

1500
2400
3000

💡 Think:

price × quantity → total → return
'''

def calculate_total(price,quantity):
    return price * quantity

print(calculate_total(500, 3))
print(calculate_total(1200, 2))
print(calculate_total(750, 4))

print(calculate_total(500, quantity = 3))
print(calculate_total(quantity = 2, price = 1200))
print(calculate_total(price = 750, quantity = 4))

