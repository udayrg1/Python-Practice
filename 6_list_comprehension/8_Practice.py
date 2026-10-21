'''
⭐ Challenge 5 (Easy)

Given:

numbers = [5, 10, 15, 20, 25, 30]

Create a new list containing only numbers divisible by 10.

Expected Output
[10, 20, 30]
'''
numbers = [5, 10, 15, 20, 25, 30]

div_number = [number for number in numbers if number % 10 == 0]

print(div_number)
