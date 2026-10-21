'''
Pattern 1 of 6: Filtering elements
Your challenge: Collect all numbers divisible by 5 into a new list.

Given:

numbers = [12, 7, 25, 8, 30, 11, 45, 14]

Expected result: [25, 30, 45]

'''

numbers = [12, 7, 25, 8, 30, 11, 45, 14]

new_nums = [0] * len(numbers)

index = 0

for i in range(0, len(numbers)):
    if numbers[i] % 5 == 0:
        new_nums[index] = numbers[i]
        index += 1

print(new_nums[:index])