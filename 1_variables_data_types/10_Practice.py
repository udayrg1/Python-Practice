"""
Question 10: Student Record Formatter
Problem

Given:

student = "  Rahul,22,BTech  "

Perform the following steps:

Remove spaces.
Split into a list.
Print using an f-string.

Expected output:

Name : Rahul
Age : 22
Course : BTech
"""

student = "  Rahul,22,BTech  "

clean_student = student.strip()

split_student = clean_student.split(",")

print(f"Name: {split_student[0]}")
print (f"Age: {int(split_student[1])}")
print(f"Course: {split_student[2]}")
