'''
🐍⚔️ Q8/200 — Sum of Positive Numbers

Write a Python program that:

Uses a while loop
Keeps accepting numbers from the user
Stops when the user enters 0
Calculates the sum of positive numbers only
Negative numbers should be ignored
Do not include 0
Prints only the final sum
Don't use a list
Must use break
Example
Enter a number: 10
Enter a number: -5
Enter a number: 20
Enter a number: -8
Enter a number: 7
Enter a number: 0

Sum: 37
'''

sum = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number >= 1:
        sum = sum + number

print(sum)