'''
Day 8 — Challenge 2: Employee Exit Processing
Let's increase the difficulty a little. This challenge introduces pop() and missing-key handling in a real-world HR scenario.

You have this dictionary:

employee_status = {
    "EMP101": "Active",
    "EMP102": "Resigned",
    "EMP103": "Active",
    "EMP104": "On Notice",
    "EMP105": "Resigned"
}

Your requirements
1. Remove "EMP102" from the dictionary using pop() and store the removed status in a variable.
2. Print the removed employee's status.
3. Attempt to remove "EMP106", which does not exist, using pop() with a default value of "Employee Not Found". Print the result.
4. Remove "EMP105" using pop() and store its status in a separate variable.
5. Print the final employee_status dictionary.
6. Print the total number of employees remaining.
Rules:
- Use pop() for both removals.
- Do not use if or else.
- Do not manually modify the dictionary with del.
- Write the complete program yourself.

'''

employee_status = {
    "EMP101": "Active",
    "EMP102": "Resigned",
    "EMP103": "Active",
    "EMP104": "On Notice",
    "EMP105": "Resigned"
}

resigned_employee = employee_status.pop("EMP102")

print(resigned_employee)

fetch_employee_data = employee_status.pop("EMP106", "Employee Not Found")
print(fetch_employee_data)

remove_employee = employee_status.pop("EMP105")
print(remove_employee)

print(employee_status)

print(len(employee_status))