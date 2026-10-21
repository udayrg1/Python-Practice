'''
🐍⚔️ Q4/200 — Sentinel + Accumulator

Write a Python program that:

Uses a while loop
Keeps asking the user to enter numbers
Stops when the user enters 0
Calculates the largest number entered before 0
Do not include 0
Prints only the largest number
Assume at least one positive number is entered
Must use break

Example:

Enter number: 12
Enter number: 45
Enter number: 23
Enter number: 67
Enter number: 0

Largest: 67

💡 New concept: finding a maximum value while looping.

Don't use max() or a list.
'''

largest = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number > largest:
        largest = number

print(largest)