'''
🐍⚔️ Q14/200 — Multiples in Reverse

Write a Python program that:

Uses a while loop
Starts with number = 50
Goes down to 5
Prints numbers that are multiples of 5
Prints each number on a separate line
Decreases the number by 5 each time
Do not use a for loop
Do not use break
Do not use %
Expected output:
50
45
40
35
30
25
20
15
10
5

🔥 New concept: Reverse stepping with -= 5.
'''

number = 50

while number >= 5:
    print(number)
    number -= 5