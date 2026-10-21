'''
Day 5 — Lists Practice: Problem 3
Topic: Remove duplicate values without using list methods

You are given a list of transaction IDs:

transaction_ids = [101, 102, 103, 101, 104, 102, 105, 103]


Your task
Create a new list containing each transaction ID only once, while preserving the original order.

Expected output:

[101, 102, 103, 104, 105]

Rules:
- Don't use set().
- Don't use append(), insert(), or other list methods.
- Don't use list comprehensions.
- Use loops, conditions, indexing, and assignment.
'''

transaction_ids = [101, 102, 103, 101, 104, 102, 105, 103]

unique_transaction_id = [0] * len(transaction_ids)

index = 0

for i in range(0, len(transaction_ids), 1):
    if transaction_ids[i] not in unique_transaction_id[:index]:
        unique_transaction_id[index] = transaction_ids[i]
        index += 1
print(unique_transaction_id[:index])