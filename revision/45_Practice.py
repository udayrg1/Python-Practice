'''
🔄 Q17 — while + accumulator + multiple conditions

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 50
Calculates the sum of numbers that are:
even
AND divisible by 3
Prints only the final sum
Don't use a list

Expected output:

90
'''

number = 1

sum = 0

while number <= 50:
    if number % 2 == 0 and number % 3 == 0:
        sum = sum + number
    number += 1
print(sum)