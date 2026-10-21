'''
🐍⚔️ Q16/200 — Reverse the Number

Write a Python program that:

Uses a while loop
Takes a positive integer from the user
Reverses the number
Prints the reversed number
Do not convert the number to a string
Do not use slicing
Do not use a for loop
Example 1
Enter a number: 58321

Reversed: 12385
Example 2
Enter a number: 12340

Reversed: 4321

💡 New concept: Extracting digits using % 10 and removing digits using // 10.

🔥 This one is significantly different from Q11–Q15. No 4-line += 2 nonsense now. 😂🐍⚔️
'''

number = int(input("Enter a number: "))

reversed_number = 0

while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number = number // 10

print(reversed_number)