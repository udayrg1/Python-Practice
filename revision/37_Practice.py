'''
🔄 Question 9

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 30
Calculates the sum of numbers divisible by 3
Prints only the final sum

💡 This time use an accumulator (total), not a counter.

Your turn. 😎💪
'''

number = 1

sum = 0

while number <= 30:
    if number % 3 == 0:
        sum += number
    number += 1
print(sum)