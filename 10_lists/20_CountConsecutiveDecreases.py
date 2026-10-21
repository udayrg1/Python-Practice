numbers = [9, 7, 5, 8, 6, 4, 3, 7]

count = 0

for i in range(1, len(numbers)):

    if numbers[i] < numbers[i-1]:
        count += 1

print(count)