'''
🚀 Next: A unique challenge
Now let's make the problem a little more interesting.

Scenario: Employee Training Tracker
An organization is preparing training sessions for employees across three departments.

departments = {
    "QA": ["EMP101", "EMP102", "EMP103"],
    "Automation": ["EMP201", "EMP202"],
    "Data Analysis": ["EMP301", "EMP302", "EMP303", "EMP304"]
}

Requirements
1. Create an empty dictionary called training_progress.
2. Use a loop to process each department.
3. For each department, use fromkeys() to initialize all its employees with the status "Pending".
4. Store those employee records under their respective departments.
5. Print the final dictionary.

Expected structure (simplified):

{
    "QA": {
        "EMP101": "Pending",
        "EMP102": "Pending",
        "EMP103": "Pending"
    },
    "Automation": {
        "EMP201": "Pending",
        "EMP202": "Pending"
    },
    "Data Analysis": {
        "EMP301": "Pending",
        "EMP302": "Pending",
        "EMP303": "Pending",
        "EMP304": "Pending"
    }
}

💡 Hint
You'll need:
- A for loop to access each department and its employees.
- dict.fromkeys() to initialize employee statuses.
- Dictionary assignment to store each department's employee dictionary.

This challenge introduces a useful concept: nested dictionaries.
'''

departments = {
    "QA": ["EMP101", "EMP102", "EMP103"],
    "Automation": ["EMP201", "EMP202"],
    "Data Analysis": ["EMP301", "EMP302", "EMP303", "EMP304"]
}

training_progress = {}

for department_name, employee_id in departments.items():
    training_progress[department_name] = dict.fromkeys(employee_id, "Pending")

print(training_progress)
