'''
🔥 Q1/200 — The Sentinel

Write a Python program that:

Uses a while loop
Keeps asking the user to enter a number
Continues accepting numbers until the user enters 0
When 0 is entered, the loop stops
Prints the sum of all numbers entered before 0
Do not include 0 in the sum

Example:

Enter number: 10
Enter number: 25
Enter number: 7
Enter number: 0

Sum: 42
'''
sum = 0
while True:
    number = int(input("Enter a Number: " ))
    
    if number == 0:
        break
    sum = sum + number
print(sum)


