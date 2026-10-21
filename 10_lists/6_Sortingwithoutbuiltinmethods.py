'''
Question 2: Sorting without built-in methods

Write a Python program to sort a list in both ascending and descending order without using sort() or sorted().

numbers = [34, 12, 56, 8, 23, 41]

Ascending: [8, 12, 23, 34, 41, 56]
Descending: [56, 41, 34, 23, 12, 8]

Rules:
- Don't use sort() or sorted().
- Don't use any external libraries.
- Implement the sorting logic yourself.

'''

numbers = [34, 12, 56, 8, 23, 41]

# Ascending order
ascending = numbers.copy()

for i in range(len(ascending) - 1):
    for j in range(i + 1, len(ascending)):
        if ascending[i] > ascending[j]:
            ascending[i], ascending[j] = ascending[j], ascending[i]

print("Ascending:", ascending)

# Descending order
descending = numbers.copy()

for i in range(len(descending) - 1):
    for j in range(i + 1, len(descending)):
        if descending[i] < descending[j]:
            descending[i], descending[j] = descending[j], descending[i]

print("Descending:", descending)