'''
🐍⚔️ Q6/200 — Second Largest

Now we'll make it slightly harder.

Write a Python program that:

Uses a while loop
Keeps accepting positive numbers
Stops when the user enters 0
Finds the second largest number
Prints only the second largest number
Assume at least two different numbers are entered
Don't use a list
Don't use sort() or max()
Must use break

Example:

Enter number: 10
Enter number: 50
Enter number: 30
Enter number: 70
Enter number: 20
Enter number: 0

Second largest: 50
'''

largest = 0
second_largest = None

while True:

    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest:
        second_largest = number

print(second_largest)



