numbers = [2, 7, 4, 5, 3, 8, 1, 7, 2]

target = 9

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
                pair = sorted([numbers[i], numbers[j]])
                if pair not in pairs:
                     pairs.append([numbers[i], numbers[j]])
print(pairs)