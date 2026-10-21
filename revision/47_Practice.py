'''
🔄 Q19 — while + counter + multiple conditions

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 100
Counts numbers that are:
divisible by 3
AND not divisible by 5
Prints only the final count
Don't use a list

Expected output:

27

💡 You'll need %, and, and !=.
'''

number = 1

count = 0

while number <= 100:
    if number % 3 ==0 and number % 5 != 0:
        count += 1
    number += 1
print(count)