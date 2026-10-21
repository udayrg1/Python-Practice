'''
Practice Problem 2 — Extract values at odd indexes
You are given a list of website response times (in milliseconds):

response_times = [120, 95, 210, 85, 175, 110, 240, 130, 160, 75, 190]


Your task: Create a new list containing the values at indexes 1, 3, 5, 7, 9.

Expected output:

[95, 85, 110, 130, 75]

Rules
- No append(), insert(), sort(), or sorted().
- Use a fixed-size list, a loop, and index-based assignment.
- Print only the required values in one list, without extra zeros.
- Don't hardcode the output.
'''


response_times = [120, 95, 210, 85, 175, 110, 240, 130, 160, 75, 190]

odd_resp_times = [0] * len(response_times)

index = 0

for i in range(1, len(response_times), 2):
    odd_resp_times[index] = response_times[i]
    index += 1

print(odd_resp_times[:index])