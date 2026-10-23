'''
Day 7 — pop() practice: HR System
Create a dictionary named HR_System with these key-value pairs:
Key	Value
"E101"	"Karthik"
"E102"	"Meena"
"E103"	"Sanjay"
"E104"	"Divya"

Requirements
1. Remove employee "E102" using pop().
2. Store the returned employee name in a variable and print it.
3. Print the updated HR_System dictionary.
4. Print the total number of remaining employees using len().
Expected output
Meena
{'E101': 'Karthik', 'E103': 'Sanjay', 'E104': 'Divya'}
3

'''

HR_System = {

    "E101" :	"Karthik",
    "E102" :	"Meena",
    "E103" :	"Sanjay",
    "E104" :	"Divya"
}


resigned_employee = HR_System.pop("E102", None)
#This removes the key if it exists and returns None if it doesn't.

print(resigned_employee)

print(HR_System)

print(len(HR_System))