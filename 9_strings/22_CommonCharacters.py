'''
Day 5 — Question 1: Common Characters
Your task

Write a Python program to print the common characters in two strings, printing each common character only once.

text1 = "programming"
text2 = "automation"

Expected output:

oamin

Rules
- Don't use sets.
- Don't use built-in shortcuts to find common elements.
- Don't print duplicate characters.
- Preserve the order in which characters appear in text1.
'''

text1 = "programming"
text2 = "automation"

common_char = ""

for char in text1:
    if char in text2:
        if char not in common_char:
            common_char += char
    
print(common_char)
