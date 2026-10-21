'''
🔄 Q20 — while + accumulator + or

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 50
Calculates the sum of numbers that are:
divisible by 4 OR 7
Prints only the final sum
Don't use a list

💡 If a number is divisible by both 4 and 7, add it only once.

Expected output:

532
'''

number = 1
sum = 0

while number <= 50:
    if number % 4 == 0 or number % 7 == 0:
        sum = sum + number
    number += 1
print(sum)