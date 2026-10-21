'''
Problem 1 — Find the second-largest distinct number

numbers = [12, 45, 7, 45, 32, 12, 38]

Find the second-largest distinct value without sorting the list.

Expected output: 38

Rules:
- No sort() or sorted()
- No max() or set()
- No list comprehensions
- Use loops and conditions

'''

numbers = [12, 45, 7, 45, 32, 12, 38]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num < largest and (second_largest is None or num > second_largest):
        second_largest = num

print(second_largest)