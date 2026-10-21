'''
Next question: Find the missing number
Given a list containing distinct numbers from 1 to n, with one number missing:

numbers = [1, 2, 3, 5, 6, 7]

Expected output: 4

Rules:
- Don't use sum(), set(), or sorting.
- Try solving it using loops and basic arithmetic.
- Don't look up the solution yet.
'''

numbers = [1, 2, 3, 5, 6, 7]

n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = 0

for i in numbers:
    actual_sum += i

missing_number = expected_sum - actual_sum

print("Missing Number:", missing_number)