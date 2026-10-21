"""
Question 8
Problem

Create the following dictionary:

employee = {
    "name": "Ravi",
    "age": 28,
    "department": "Automation",
    "salary": 45000
}

Perform the following tasks:

Print the complete dictionary.
Print all the keys.
Print all the values.
Print all the key-value pairs using .items().

Expected Output

Employee Details: {'name': 'Ravi', 'age': 28, 'department': 'Automation', 'salary': 45000}

Keys:
dict_keys(['name', 'age', 'department', 'salary'])

Values:
dict_values(['Ravi', 28, 'Automation', 45000])

Items:
dict_items([
('name', 'Ravi'),
('age', 28),
('department', 'Automation'),
('salary', 45000)
])

Concepts Covered
.keys()

.values()

.items()
"""

employee = {

    "name" : "Uday Kumar Ramagiri",
    "Age"  : 29,
    "Department" : "Indian Administrative Services",
    "Salary" : 350000 
}

print(f"Employee Details: {employee}")

print(employee.keys())
print(employee.values())
print(employee.items())