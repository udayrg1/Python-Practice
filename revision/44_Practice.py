'''
🔄 Q16 — while + multiple conditions

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 50
Counts numbers that are:
even
AND divisible by 5
Prints only the final count
Don't use a list

Expected output:

5
'''

number = 1

count = 0

while number <= 50:
    if number % 2 == 0 and number % 5 == 0:
        count += 1
    number += 1
print(count)