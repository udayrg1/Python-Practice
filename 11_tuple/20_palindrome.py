'''
🐍 Day 6 — Challenge 12: Check whether a tuple is a palindrome
A tuple is a palindrome if it reads the same forwards and backwards.

Given: values = (1, 2, 3, 2, 1)

Expected output: Palindrome

'''
values = (1, 2, 3, 2, 1)

rev_values = ()

for index in range(len(values) -1, -1, -1):
    rev_values += (values[index],)

if rev_values == values:
    print("Palindrome")
else:
    print("Not a palindrome")