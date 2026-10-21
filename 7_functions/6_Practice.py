'''
🎯 Function Practice #5 — Product Status

This one combines parameters + conditions + Boolean return, but the logic is different from the previous validation question.

Problem

Create a function:

get_stock_status(quantity)

The function should:

Accept quantity as a parameter.
If quantity is greater than 0, return "In Stock".
If quantity is exactly 0, return "Out of Stock".
If quantity is less than 0, return "Invalid Quantity".

Test it with:

25
0
-5
Expected output
In Stock
Out of Stock
Invalid Quantity
🧠 Think before coding
quantity
   ↓
> 0   → "In Stock"
== 0  → "Out of Stock"
< 0   → "Invalid Quantity"

And remember: don't put print() inside the function. Return the result and print it outside.
'''

def get_stock_status(quantity):

    if quantity > 0:
        return "In Stock"
    elif quantity == 0:
        return "Out of Stock"
    else:
        return "Invalid Quantity"

print("Stock Status: ", get_stock_status(25))
print("Stock Status: ", get_stock_status(0))
print("Stock Status: ", get_stock_status(-5))