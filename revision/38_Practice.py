'''
🔄 Question 10 — Final While Loop Challenge

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 50
Counts numbers that are:
divisible by 5
AND greater than 20
Prints only the final count

💡 Expected matching numbers:

25, 30, 35, 40, 45, 50

Expected output:

6

Your turn. 😎
'''

number = 1

count = 0

while number <= 50:
    if number % 5 == 0 and number > 20:
        count += 1
    number += 1
print(count)