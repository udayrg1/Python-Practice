'''
List Challenge — Find the Leaders in a List
A number is called a leader if it is greater than every element to its right. The last element is always a leader.

Given:

numbers = [16, 17, 4, 3, 5, 2]

Expected output:

[17, 5, 2]
'''

numbers = [16, 17, 4, 3, 5, 2]

# Create an empty result area using zeros
new_leaders = [0] * len(numbers)
index = 0

# Check each number in the list
for i in range(len(numbers)):

    # Assume the current number is a leader
    is_leader = True

    # Compare the current number with every number to its right
    for j in range(i + 1, len(numbers)):

        # If the current number is smaller than or equal to
        # any number on its right, it is NOT a leader
        if numbers[i] <= numbers[j]:
            is_leader = False
            break  # Stop checking this candidate; it cannot be a leader

        # If the condition is False, continue comparing
        # For example: 4 <= 3 is False, so check 4 <= 5 next

    # If all comparisons are passed, store the current number
    if is_leader:
        new_leaders[index] = numbers[i]
        index += 1

# Print only the positions containing confirmed leaders
print(new_leaders[:index])
