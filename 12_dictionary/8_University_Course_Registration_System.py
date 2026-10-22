'''
Challenge: University Course Registration System
Dictionary pop() + logic building
Difficulty: Beginner → Intermediate


A university maintains a record of student enrollments for different courses.

Create a dictionary named course_enrollment using these key-value pairs:
Course code	Enrolled students
"CS101"	45
"DB202"	32
"PY303"	28
"QA404"	36
"WD505"	40

Your requirements
1. Remove "DB202" using the pop() method and store the returned value in a variable.
2. Print the removed enrollment count.
3. Calculate and print the total enrollment across all remaining courses.
4. Print the number of courses remaining using len().
5. Check whether "DB202" exists in the dictionary and print the result.

Expected output
32
149
4
False

Rules for this challenge
- Write the entire program from scratch.
- Don't hardcode the expected answers into your calculations.
- Use dictionary operations and appropriate built-in functions.
- I'll review your code after you submit it, and I'll explain any mistakes without jumping ahead to the next topic.
'''

course_enrollment = {

    "CS101" : 45,
    "DB202" : 32,
    "PY303"	: 28,
    "QA404" : 36,
    "WD505"	: 40
}

removed_value = course_enrollment.pop("DB202", None)
#This removes the key if it exists and returns None if it doesn't.

print(removed_value)

#Calculate and print the total enrollment across all remaining courses.
sum_values = 0

for value in course_enrollment.values():
    sum_values += value

print(sum_values)

#Print the number of courses remaining using len().

print(len(course_enrollment))

#5. Check whether "DB202" exists in the dictionary and print the result.
print("DB202" in course_enrollment)
