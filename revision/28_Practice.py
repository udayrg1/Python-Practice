'''
Write a Python program that:

Uses a for loop
Uses range()
Goes through numbers 1 to 20
Finds numbers that are both even AND greater than 10
Prints those numbers
Each number on a separate line

No list.
'''

for number in range(1,21):
    if number % 2 == 0 and number > 10:
        print(number)