'''
🐍 Challenge 11 — Reverse a tuple without using [::-1]
Now let's test your indexing and loop logic.

Given: employee_ids = (101, 205, 310, 420, 510)

Expected output: (510, 420, 310, 205, 101)

Rules:
- Don't use [::-1].
- Don't use reversed().
- Store the result in a new tuple.
- Use a loop.
Hint: You can iterate through the tuple's indices in reverse order using range()

'''

employee_ids = (101, 205, 310, 420, 510)

rev_emp_ids = ()

for index in range(4, -1, -1):
    rev_emp_ids += (employee_ids[index],)

print(rev_emp_ids)