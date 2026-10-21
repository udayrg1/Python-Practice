'''
🐍⚔️ Q15/200 — Double Step

Write a Python program that:

Uses a while loop
Starts with number = 1
Goes up to 30
Prints every second number: 1, 3, 5, 7...
Each number on a separate line
Do not use a for loop
Do not use break
Do not use %
Do not use an if statement
Expected output:
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29

🔥 New concept: Using += 2 to control which values the while loop visits.
'''

number = 1

while number <= 30:
    print(number)
    number += 2