'''
🐍⚔️ Q17/200 — Count the Digits

Let's make this one genuinely different from Q16.

🎯 Task

Write a Python program that:

Uses a while loop
Takes a positive integer from the user
Counts how many digits the number contains
Prints the digit count
Do not convert the number to a string
Do not use len()
Do not use a for loop
Examples
Enter a number: 58321
Number of digits: 5
Enter a number: 907
Number of digits: 3
Enter a number: 4
Number of digits: 1
💡 New concept

This time you're going to use:

number = number // 10

to keep removing one digit at a time, while maintaining a counter.
'''

number = int(input("Enter a number: "))

count = 0

while number > 0:

    number = number // 10
    count += 1

print(count)