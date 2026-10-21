numbers = [[2, 3], [4, 6], [7, 8]]

even_nums = []
count = 0

for nums in numbers:
    for digit in nums:
        if digit % 2 == 0:
            even_nums.append(digit)
            count += 1

print(even_nums)
print(count)