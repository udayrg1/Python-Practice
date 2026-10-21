'''
🐍⚔️ Q9/200 — Sum of Negative Numbers

Write a Python program that:

Uses a while loop
Keeps accepting numbers
Stops when the user enters 0
Calculates the sum of negative numbers only
Positive numbers should be ignored
Do not include 0
Prints only the final sum
Don't use a list
Must use break

Example:

Enter a number: 10
Enter a number: -5
Enter a number: 20
Enter a number: -8
Enter a number: -7
Enter a number: 0

Sum: -20
'''
sum_of_neg_num = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number < 0:
        sum_of_neg_num = sum_of_neg_num + number

print(sum_of_neg_num)
