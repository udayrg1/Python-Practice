'''
🔄 Q12 — continue

Now let's practice the other important loop-control statement.

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes from 1 to 10
Skips the number 5
Prints all other numbers
Must use continue
'''

number = 1

while number <= 10:
    print(number)
    number += 1
    
    if number == 5:
        continue
