'''
Day 6 — Challenge 10: Find common elements between two tuples
Intermediate
You are given two tuples containing product IDs from two different sales reports.

report_a = (101, 205, 310, 420, 205, 510)
report_b = (205, 420, 600, 310, 700, 420)

Your task: Create a new tuple containing the elements that appear in both tuples, without duplicates.

Expected output: (205, 310, 420)

Rules
- Don't use set().
- Don't use dictionaries.
- Don't use intersection() or other shortcuts.
- Preserve the order in which common elements first appear in report_a.
Hints
Think about the logic you've already used:
1. Loop through report_a.
2. Check whether each element exists in report_b.
3. Ensure you don't add the same element twice.
4. Store the result in a tuple.

'''

report_a = (101, 205, 310, 420, 205, 510)
report_b = (205, 420, 600, 310, 700, 420)


report_c = ()

for a in report_a:
    if a in report_b:
        if a not in report_c:
            report_c += (a,)

print(report_c)

