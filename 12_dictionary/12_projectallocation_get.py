'''
Challenge 1: Company Project Allocation System
A company maintains a dictionary of employees assigned to projects.

Create a dictionary named project_allocation using these key-value pairs:
Employee ID	Project
"EMP101"	"Automation"
"EMP102"	"Data Analytics"
"EMP103"	"Software Testing"
"EMP104"	"SQL Development"


Your requirements
1. Retrieve the project assigned to "EMP102" using get() and print it.

2. Retrieve the project assigned to "EMP105" using get() and print the result.

3. Retrieve the project assigned to "EMP105" using get(), but return "Not Assigned" if the employee ID doesn't exist. Print the result.

4. Print the original dictionary and verify that these retrieval operations haven't added any new employees.
Expected output
Data Analytics
None
Not Assigned
{'EMP101': 'Automation', 'EMP102': 'Data Analytics', 'EMP103': 'Software Testing', 'EMP104': 'SQL Development'}

Your rules for this exercise
- Write the complete program from scratch.
- Don't use if conditions for these retrievals; practise get() itself.
- Don't hardcode the expected outputs into variables.
- Use different variable names where appropriate.

'''

project_allocation = {
    "EMP101":	"Automation",
    "EMP102":	"Data Analytics",
    "EMP103":	"Software Testing",
    "EMP104":	"SQL Development"
}

assigned_project = project_allocation.get("EMP102")
print(assigned_project)

'''
project_allocation["EMP105"]  -- if we try to fetch directly without using .get() method, 
it will raise a KeyError
'''

assigned_project = project_allocation.get("EMP105")
print(assigned_project)

assigned_project = project_allocation.get("EMP105", "Not Assigned")
print(assigned_project)

print(project_allocation)