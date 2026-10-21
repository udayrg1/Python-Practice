'''
Next challenge: Find the largest number in each inner list.

Input: [[3, 9, 2], [15, 4, 8], [7, 6]]

Expected output: [9, 15, 7]
'''

numbers = [[3, 9, 2], [15, 4, 8], [7, 6]]

largest_nums = []

for row in numbers:
    largest = row[0]
    for nums in row:
        if nums > largest:
            largest = nums
    largest_nums.append(largest)
print(largest_nums)