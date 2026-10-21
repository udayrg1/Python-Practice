'''
Next problem — Count occurrences
Given: numbers = [4, 2, 4, 7, 2, 4, 9, 7]

Create a new list containing each unique number and its frequency, preserving the order of first appearance.

Expected output: [4, 3, 2, 2, 7, 2, 9, 1]

The pattern is [number, frequency, number, frequency, ...].

Rules: No count(), set(), append(), dictionaries, or list comprehensions. Use loops and indexing.

'''

numbers = [4, 2, 4, 7, 2, 4, 9, 7]

frequency = []

for i in numbers:
    if i not in frequency:
        count = 0

        for j in numbers:
            if i == j:
                count += 1

        frequency += [i, count]

print(frequency)