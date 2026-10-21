'''
🔄 Q18 — while + counter + or

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 50
Counts numbers that are divisible by 4 OR 6
Prints only the final count
Don't use a list

💡 Be careful: if a number satisfies both conditions, it should be counted only once.

Expected output:

17
'''

number = 1

count = 0

while number <= 50:
    if number % 4 == 0 or number % 6 == 0:
        count += 1
    number += 1
print(count)