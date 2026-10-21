'''
Next challenge — Nested List Processing #3
Find the row with the largest sum.

numbers = [[2, 3], [10, 1], [4, 5, 6]]

Expected output:

[4, 5, 6]
'''

numbers = [[2, 3], [10, 1], [4, 5, 6]]

sum_nested_list = []

# Calculate the sum of each row
for row in numbers:
    sum_list = 0
    for num in row:
        sum_list += num
    sum_nested_list.append(sum_list)

print(sum_nested_list)

# Find the index of the highest sum
largest_sum = sum_nested_list[0]
index = 0

for i in range(len(sum_nested_list)):
    if sum_nested_list[i] > largest_sum:
        largest_sum = sum_nested_list[i]
        index = i

print("Highest sum:", largest_sum)
print("Index:", index)

# Retrieve the row corresponding to that index
print("Row with highest sum:", numbers[index])
