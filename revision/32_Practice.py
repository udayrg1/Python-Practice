'''
🔄 While Loop — Question 4

Write a Python program that:

Uses a while loop
Starts with number = 1
Calculates the sum of numbers from 1 to 10
Prints only the final sum

Expected output:

55

You build it. 😎
'''

sum_of_no = 1
total = 0

while sum_of_no <= 10:
    total = total + sum_of_no
    sum_of_no += 1
    
print(total)