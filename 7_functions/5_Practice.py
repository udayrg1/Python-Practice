'''
🎯 Q4 — Validation Function

This introduces a new pattern: returning a Boolean (True / False) from a function.

Problem

Create a function:

is_valid_price(price)

Requirements:

Accept price as a parameter.
If the price is greater than 0, return True.
Otherwise, return False.
Don't use print() inside the function.

Test it with:
500
0
-100
Expected output
True
False
False
🧠 Think about it
price
  ↓
Is price > 0?
  ↓
Yes → True
No  → False
'''
'''
def is_valid_price(price):
    return price > 0

print(is_valid_price(500))
print(is_valid_price(0))
print(is_valid_price(-100))
'''

def is_valid_price(price):
    if price > 0:
        return True
    else:
        return False

print(is_valid_price(500))
print(is_valid_price(0))
print(is_valid_price(-100))

