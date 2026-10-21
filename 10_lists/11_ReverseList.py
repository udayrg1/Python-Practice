'''
Reverse List — Practice Problem 1
You are given a list of website response times:

response_times = [120, 95, 210, 85, 175, 110]

Your task is to create a new list with the elements in reverse order, without modifying the original list.

Expected output:

[110, 175, 85, 210, 95, 120]


Rules
- Don't use reverse(), reversed(), or slicing ([::-1]).
- Don't use append() or insert().
- Use a fixed-size list, a loop, and index-based assignment.
- Don't hardcode the output.
Hint: You already know how to create a zero-filled list and assign values using indexes.

Think about:
- Which index should you read from the original list first?
- Which index should you write to in the new list?
- How should those indexes change after each iteration?
'''

response_times = [120, 95, 210, 85, 175, 110]


reversed_times = [0] * len(response_times) 

index = 0

for i in range(5, -1, -1):
    reversed_times[index] = response_times[i]
    index += 1

print(reversed_times)