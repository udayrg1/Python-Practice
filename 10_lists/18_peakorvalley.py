numbers = [2, 5, 8, 6, 3, 7, 9, 4]

count = 0

for i in range(1, len(numbers) -1):

    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        count += 1
    elif numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]:
        count += 1

print(count)