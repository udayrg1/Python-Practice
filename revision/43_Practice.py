'''
🔄 Q15 — while + accumulator

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 30
Calculates the sum of odd numbers
Prints only the final sum
Don't use a list

Expected output:

225
'''

number = 1
sum = 0

while number <= 30:
    if number % 2 != 0:
        sum = sum + number
    number += 1
print(sum)