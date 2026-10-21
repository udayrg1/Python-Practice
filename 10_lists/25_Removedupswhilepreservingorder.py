'''
Pattern 2 of 6: Remove duplicates while preserving order
Try this one independently, ra.

Given:

numbers = [4, 2, 4, 7, 2, 9, 7, 5]

Expected result: [4, 2, 7, 9, 5]

Your hints:
1. Create an empty result list.
2. Visit each number in the original list.
3. Before adding a number, check whether it already exists in the result list.
4. Add it only if it isn't already present.
Remember: preserve the original order. No set() for this challenge — I want you to practise the membership-checking logic yourself. 💪
'''

numbers = [4, 2, 4, 7, 2, 9, 7, 5]

unique_nums = [0] * len(numbers)

index = 0

for i in range(0, len(numbers)):
    if numbers[i] not in unique_nums[:index]:
        unique_nums[index] = numbers[i]
        index += 1

print(unique_nums[:index])