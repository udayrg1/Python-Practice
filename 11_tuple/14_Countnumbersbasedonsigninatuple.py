'''
Problem: Count positive numbers, negative numbers, and zeros in a tuple.

Given: temperatures = (-5, 0, 12, -2, 8, 0, 15, -1)

Expected output:

Positive: 3
Negative: 3
Zeros: 2
'''

temperatures = (-5, 0, 12, -2, 8, 0, 15, -1)

positive_count = 0
negative_count = 0
zeros_count = 0

for temp in temperatures:
    if temp > 0:
        positive_count += 1
    elif temp < 0:
        negative_count += 1
    else:
        zeros_count += 1

print("Positive count: ", positive_count)
print("Negative count: ", negative_count)
print("Zeros count: ", zeros_count)