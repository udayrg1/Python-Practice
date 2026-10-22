'''
Day 7 — Dictionary pop() practice
Imagine you're managing student records.

Create a dictionary named students using these key-value pairs:
Key	Value
"Rahul"	85
"Priya"	92
"Arjun"	78
"Sneha"	88

Requirements
1. Remove "Arjun" using the pop() method.
2. Print the value returned by pop().
3. Print the updated dictionary.
4. Print the total number of remaining students using len().
Expected output
78
{'Rahul': 85, 'Priya': 92, 'Sneha': 88}

'''

students = {

    "Rahul" : 85,
    "Priya"	: 92,
    "Arjun"	: 78,
    "Sneha"	: 88
}

value = students.pop("Arjun", None) #Remove "Arjun" using the pop() method.
#This removes the key if it exists and returns None if it doesn't.

print(value)  # Print the value returned by pop().

print(students)

print(len(students))