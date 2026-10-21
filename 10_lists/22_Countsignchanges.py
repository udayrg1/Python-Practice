numbers = [3, 5, -2, -7, 4, -1, 6]

sign_count = 0

for i in range(1, len(numbers)):
    if numbers[i] > 0 and numbers[i - 1] < 0 or numbers[i] < 0 and numbers[i - 1] > 0:
            sign_count += 1

print(sign_count)


#2nd method

numbers = [3, 5, -2, -7, 4, -1, 6]

sign_count = 0

for i in range(1, len(numbers)):
    if numbers[i] > 0 and numbers[i - 1] < 0:
            sign_count += 1
    elif numbers[i] < 0 and numbers[i - 1] > 0:
            sign_count += 1

print(sign_count)