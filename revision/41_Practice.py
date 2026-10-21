'''
🔄 Q13 — while + accumulator

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 20
Calculates the sum of numbers that are even
Prints only the final sum
Don't use a list

Expected output:

110
'''

number = 1

sum_of_even = 0

while number <= 20:
    if number % 2 == 0:
        sum_of_even = sum_of_even + number
    number += 1

print(sum_of_even)

