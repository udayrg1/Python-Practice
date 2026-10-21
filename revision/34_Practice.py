'''
Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 20
Skips multiples of 3
Prints every other number
Each number on a separate line

Expected output:
'''

number = 1

while number <= 20:
    if number % 3 != 0:
        print(number)
    number += 1
    
