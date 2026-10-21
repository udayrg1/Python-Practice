numbers = [4, -2, 5, 7, -3, 6, 8, 1]

count = 0

for i in range(1, len(numbers)):
    if numbers[i] > 0 and numbers[i - 1] < 0:
        count += 1

print(count)