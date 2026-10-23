'''
Example scenario
Your current employee records are:

employee_details = {
    "EMP101": "Automation Analyst",
    "EMP102": "Data Analyst",
    "EMP103": "Software Tester"
}

HR sends these updates:
- EMP102 has moved to a Python Developer role.
- EMP104 has joined as a QA Engineer.
You can apply both changes using one update() call.
'''

employee_details = {
    "EMP101": "Automation Analyst",
    "EMP102": "Data Analyst",
    "EMP103": "Software Tester"
}

employee_details.update({
    "EMP102": "Python Developer",
    "EMP105": "QA Engineer"
})

print(employee_details)


