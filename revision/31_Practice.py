'''
🔄 While Loop — Question 3

Now let's do the odd numbers from 1 to 15.

Write a Python program that:

Uses a while loop
Starts with number = 1
Prints odd numbers from 1 to 15
Each number on a separate line
Don't use a list

Your turn. 😎💪
'''

number = 1

while number <= 15:
    if number % 2 != 0:
        print(number)
    number += 1