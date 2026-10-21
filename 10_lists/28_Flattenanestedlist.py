'''
Pattern 5: Flatten a nested list
Challenge

Given this list:

numbers = [[1, 2], [3, 4], [5, 6], [7, 8]]

Your expected output is:

[1, 2, 3, 4, 5, 6, 7, 8]
Your task
Write a Python program to convert the nested list into a single flat list.

Rules:
- Don't use sum(), chain(), or any external library.
- Use loops and your own logic.
- No hints unless you ask for them. 😎

'''

numbers = [[1, 2], [3, 4], [5, 6], [7, 8]]

new_list = []

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        new_list.append(numbers[i][j])

print(new_list)