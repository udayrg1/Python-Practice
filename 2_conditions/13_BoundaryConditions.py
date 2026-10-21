'''
Challenge 4 — Boundary Conditions 🎯

A system assigns a performance rating based on an employee's score.
Rules:
- Score below 40 → "Needs Improvement"
- Score from 40 to 69 → "Good"
- Score from 70 to 89 → "Very Good"
- Score from 90 to 100 → "Excellent"
- Any score below 0 or above 100 → "Invalid Score"

Given:
score = 90

Write the code to classify the score correctly. Pay attention to the boundary values: 0, 39, 40, 69, 70, 89, 90, and 100.
'''

score = 2

if score >= 90 and score <= 100:
    print("Excellent")
elif score >= 70 and score <= 89:
    print("Very Good")
elif score >= 40 and score <= 69:
    print("Good")
elif score >= 0 and score < 40:
    print("Needs Improvement")
else:
    print("Invalid Score")
