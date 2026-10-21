'''
🐍 Day 6 — Challenge 8: Remove duplicates while preserving order

Given a tuple of product IDs: product_ids = (101, 205, 101, 310, 205, 420, 310, 510)

Create a new tuple containing only unique values, while preserving their original order.

Expected output: (101, 205, 310, 420, 510)

Rules
- Don't use set() or dict.fromkeys().
- Don't use sorted().
- Use loops and conditions.
- Preserve the order in which each value first appears.
- Store the final result in a tuple.

Hints — only if you need them
Think about these questions:
1. How will you store the unique values you discover?
2. How will you check whether the current value has already been added?
3. Since tuples are immutable, how can you build the result?
'''

product_ids = (101, 205, 101, 310, 205, 420, 310, 510)

unique_ids = ()

for id in product_ids:
    if id not in unique_ids:
        unique_ids += (id,)

print(unique_ids)


