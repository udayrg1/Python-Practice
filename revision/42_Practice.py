'''
🔄 Q14 — while + counter

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 50
Counts how many numbers are divisible by 7
Prints only the final count

Expected output:

7
'''
number = 1

count = 0

while number <= 50:
    if number % 7 == 0:
        count += 1
    number += 1
print(count)