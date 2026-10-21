numbers = [4, 5, 1, 2, 1, 4, 5]

unique_numbers = [0] * len(numbers)
index = 0

for i in range(len(numbers)):
    is_unique = True

    # Compare the current number with every element
    for j in range(len(numbers)):

        # Skip comparing the element with itself
        if i != j and numbers[i] == numbers[j]:
            is_unique = False
            break

    # If no duplicate was found, store the number
    if is_unique:
        unique_numbers[index] = numbers[i]
        index += 1

print(unique_numbers[0])