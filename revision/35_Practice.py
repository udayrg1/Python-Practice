'''
🔄 While Loop — Question 7

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 20
Prints only numbers that are divisible by both 2 and 3
Each number on a separate line

Expected output:

6
12
18

💡 Use % and and.

You build it — no code from me. 😎
'''

number = 1

while number <= 20:
    if number % 2 == 0 and number % 3 == 0:
        print(number)
    number += 1