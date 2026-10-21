numbers = [10, 20, 30, 40, 50]

count = 0

average = (sum(numbers)/len(numbers))

for i in range(len(numbers)):
    if numbers[i] > average:
        count += 1

print(count)