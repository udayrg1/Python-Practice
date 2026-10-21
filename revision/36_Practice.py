'''
🔄 Question 8

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 20
Counts how many numbers are divisible by both 2 and 3
Prints only the final count

💡 Don't print the matching numbers this time. Use a counter.

Your turn. 😎
'''

number = 1
count = 0

while number <= 20:
    if number % 2 == 0 and number % 3== 0:
        count += 1
    number += 1
print(count)