'''
Practice Problem 1 — Extract values by index
You are given a list of daily sensor readings:

readings = [18, 25, 32, 41, 56, 63, 74, 89, 92, 105, 99, 75, 66, 34, 21, 44]

Your task: Create a new list containing values at indexes 2, 4, 6, 8, 10, 12, 14.

Expected output:

[32, 56, 74, 92, 99, 66, 21]
'''

readings = [18, 25, 32, 41, 56, 63, 74, 89, 92, 105, 99, 75, 66, 34, 21, 44]
#            0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15

new_readings = [0] * len(readings)

index = 0

for i in range(2, len(readings), 2):
    new_readings[index] = readings[i]
    index += 1

print("New Readings: ", new_readings[:index])