'''
🐍 Day 9 — Challenge: Update Nested Dictionaries Using update()

📌 Scenario: Employee Training Management System
A company tracks employee training progress across different departments. The current training status of employees is stored in a nested dictionary.

1. Given dictionary

training_progress = {
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

2. Your requirements
1. Update EMP101's status to "Completed".
2. Update EMP102's status to "In Progress".
3. Use one update() call to update both employees.
4. Print the updated QA department dictionary.
5. Print the complete training_progress dictionary.
Important: Use update() on the inner dictionary belonging to the "QA" department.

3. Expected output
Updated QA department:

{
    'EMP101': 'Completed',
    'EMP102': 'In Progress',
    'EMP103': 'Pending'
}

'''

training_progress = {
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

training_progress["QA"].update({
    "EMP101": "Completed",
    "EMP102": "In Progress",
    "EMP103": "Pending"
})

print(training_progress["QA"])

print(training_progress)