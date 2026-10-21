'''
🐍⚔️ Q11/200 — Countdown Loop

Write a Python program that:

Uses a while loop
Starts with number = 10
Counts backward from 10 to 1
Prints each number on a separate line
After printing 1, the loop should stop
Do not use for loop
Do not use break

Expected output:

10
9
8
7
6
5
4
3
2
1

🔥 New pattern: decreasing a variable using -= and using the while condition itself to control when the loop ends.
'''

number = 10

while number >= 1:
    print(number)
    number -= 1
