'''
🐍⚔️ Q2/200 — Running Average

Write a Python program that:

Uses a while loop
Keeps accepting numbers from the user
Stops when the user enters -1
Calculates the average of all numbers entered before -1
Do not include -1
Assume at least one valid number is entered
Prints only the final average

Example:

Enter number: 10
Enter number: 20
Enter number: 30
Enter number: -1

Average: 20.0

💡 New concept: You need both a total and a count.
'''
sum = 0
count = 0
average= 0

while True:
    number = int(input("Enter a Number: " ))
    
    if number == -1:
        break
    count += 1
    sum = sum + number
average = (sum/count)
print(average)