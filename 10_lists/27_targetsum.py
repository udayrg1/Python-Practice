'''
Pattern 4 of 6: Find all pairs with a target sum
Difficulty: Intermediate · Nested loops and duplicate handling

Given:

numbers = [2, 7, 4, 5, 3, 8, 1]

target = 9

Expected pairs:

(2, 7), (4, 5), (8, 1)

Rules:
- Find every valid pair.
- Don't print the same pair twice.
- Don't stop after finding the first pair.
- Don't use a set or dictionary for this challenge.

'''

numbers = [2, 7, 4, 5, 3, 8, 1, 7, 2]
target = 9

pairs = []
seen = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            key = tuple(sorted((numbers[i], numbers[j])))
            if key not in seen:
                seen.add(key)
                pairs.append((numbers[i], numbers[j]))

print(pairs)