'''
🐍⚔️ Q18/200 — Sum of Digits

Now we're going to combine digit extraction + accumulation.

🎯 Task

Write a Python program that:

Uses a while loop
Takes a positive integer
Calculates the sum of all its digits
Prints the result
Do not convert to a string
Do not use sum()
Do not use a for loop
Examples
Enter a number: 58321
Sum of digits: 19

Because:

5 + 8 + 3 + 2 + 1 = 19

Another:

Enter a number: 907
Sum of digits: 16

Because:

9 + 0 + 7 = 16
'''

number = int(input("Enter a number: "))

total = 0

while number > 0:

    digit = number % 10

    total = total + digit

    number = number // 10
print(total)