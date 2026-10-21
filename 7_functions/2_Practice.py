'''
🎯 Function Practice #1 — Employee Greeting

Write a function called:

greet_employee()

Requirements:

It should accept an employee's name as a parameter.
It should return a greeting message.
Don't use print() inside the function.
Call the function for 3 different employees.
Print the returned messages outside the function.

Expected output:

Welcome to the team, Uday!
Welcome to the team, Ravi!
Welcome to the team, Sandeep!
'''

def greet_employee(name):
    return f"Welcome to the Team, {name}!"

print(greet_employee("Uday"))
print(greet_employee("Vinay"))
print(greet_employee("Sandeep"))
