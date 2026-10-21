'''
Python Challenge: Longest Increasing Streak

Question: Find the length of the longest consecutive increasing sequence.

'''

numbers = [2, 4, 6, 3, 5, 7, 9, 1, 4]

current_streak = 1
longest_streak = 1

for i in range(1, len(numbers)):

    if numbers[i] > numbers[i-1]:
        current_streak += 1
    else:
        current_streak = 1

    if current_streak > longest_streak:
        longest_streak = current_streak

print(longest_streak)