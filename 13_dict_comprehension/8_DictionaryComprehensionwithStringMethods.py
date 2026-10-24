'''
🚀 Next challenge: Dictionary Comprehension with String Methods
Let's move beyond numbers!

Imagine you're processing employee names for an HR system.

Input
employee_names = {    "EMP101": "  uday kumar  ",    "EMP102": "RAHUL",    "EMP103": "  priya sharma",    "EMP104": "Sneha  "}

Requirements

Create a dictionary named cleaned_names using dictionary comprehension.
1. Remove leading and trailing spaces from each name.
2. Convert each name to title case.
3. Preserve the employee IDs as keys.
4. Print the resulting dictionary.

Expected output
{    'EMP101': 'Uday Kumar',    'EMP102': 'Rahul',    'EMP103': 'Priya Sharma',    'EMP104': 'Sneha'}

Hint: You can chain string methods: .strip() and .title().
'''

employee_names = {
    "EMP101": "  uday kumar  ",
    "EMP102": "RAHUL",
    "EMP103": "  priya sharma",
    "EMP104": "Sneha  "
}

cleaned_names = {employee : name.strip().title() for employee, name in employee_names.items()}

print(cleaned_names)