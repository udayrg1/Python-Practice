'''
🔄 While Loop — Question 5

Write a Python program that:

Uses a while loop
Starts with number = 1
Counts how many numbers from 1 to 20 are divisible by 4
Prints only the final count

💡 Use the counter pattern we practiced with for loops.

You build it. 😎
'''

number = 1

count = 0

while number <= 20:
    if number % 4 == 0:
        count += 1
    number += 1
print(count)