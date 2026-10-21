'''
🐍⚔️ Q5/200 — Find the Smallest

Write a Python program that:

Uses a while loop
Keeps accepting numbers
Stops when the user enters 0
Finds the smallest number entered before 0
Do not include 0
Prints only the smallest number
Assume at least one positive number is entered
Don't use min()
Don't use a list
Must use break

Example:

Enter number: 45
Enter number: 12
Enter number: 67
Enter number: 23
Enter number: 0

Smallest: 12
'''

smallest = None

while True:
    number = int(input("Enter a number: "))

    if number ==  0:
        break

    if smallest is None or number < smallest:
        smallest = number

print(smallest)
