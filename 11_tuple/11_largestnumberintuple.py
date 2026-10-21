numbers = (12, 7, 4, 9, 16, 3, 8, 11)

largest_num = numbers[0]

for num in numbers:
    if num > largest_num:
        largest_num = num

print(largest_num)