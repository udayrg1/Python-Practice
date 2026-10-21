'''
🐍⚔️ Q7/200 — Count Positive & Negative Numbers

Write a Python program that:

Uses a while loop
Keeps accepting numbers from the user
Stops when the user enters 0
Counts how many positive numbers were entered
Counts how many negative numbers were entered
Do not count 0
Prints the final positive count and negative count
Don't use a list
Must use break

Example:

Enter number: 10
Enter number: -5
Enter number: 20
Enter number: -8
Enter number: 7
Enter number: 0

Positive: 3
Negative: 2
'''

positive_number = 0
negative_number = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number > 0:
        positive_number += 1

    if number < 0:
        negative_number += 1

print(positive_number)
print(negative_number)

