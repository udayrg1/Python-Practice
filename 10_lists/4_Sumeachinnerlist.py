'''
Sum each inner list

Input: [[1, 2, 3], [4, 5], [6, 7, 8]]

Expected: [6, 9, 21]

'''
numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]

sum_nums = []

for i in range(len(numbers)):
    total = 0  # Inside outer loop, before inner loop

    for j in range(len(numbers[i])):
        total += numbers[i][j]

    sum_nums.append(total)

print(sum_nums)