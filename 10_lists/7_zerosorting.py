'''
Question 3: Move all zeros to the end
Write a Python program to move all zeros to the end of the list while preserving the order of the nonzero elements.

numbers = [0, 5, 0, 3, 8, 0, 2]

Expected output:

[5, 3, 8, 2, 0, 0, 0]
'''


numbers = [0, 5, 0, 3, 8, 0, 2]

# Right Sort: Move zeros to the right
right_sorted_nums = [0] * len(numbers)
index = 0

for num in numbers:
    if num != 0:
        right_sorted_nums[index] = num
        index += 1

print("Right Sort:", right_sorted_nums)


# Left Sort: Move zeros to the left
left_sorted_nums = [0] * len(numbers)
zero_count = 0


#33 to 35 is to get the index count or number of zeros count
for num in numbers:
    if num == 0:
        zero_count += 1

index = zero_count #here index = 3

for num in numbers:
    if num != 0:
        left_sorted_nums[index] = num
        index += 1

print("Left Sort:", left_sorted_nums)
