'''
Day 7 — Next challenge: Dictionary iteration
Create a dictionary named scores using these key-value pairs:
Key	Value
"Python"	90
"SQL"	85
"TypeScript"	78
"Testing"	88

Requirements
1. Print all the keys using a for loop.
2. Print all the values using a for loop.
3. Print each subject along with its score using a for loop and the items() method.
Rules for this exercise:
- Write the complete program yourself.
- Don't use print() alone to manually display each key or value; use loops.
- I'll give you feedback after you submit your code, without revealing the solution beforehand.

'''

scores = {
    "Python"     : 90,
    "SQL"        : 85,
    "TypeScript" : 78,
    "Testing"    : 88
}


for key in scores:
    print(key)


for value in scores.values():
    print(value)

for key, value in scores.items():
    print(key, ":", value)