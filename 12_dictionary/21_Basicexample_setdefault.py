student_progress = {
    "Uday": "Completed",
    "Priya": "In Progress"
}

result = student_progress.setdefault("Arun", "Not Started")

result1 = student_progress.setdefault("Abhinav")

print(result)

print(student_progress)