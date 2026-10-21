'''
numbers = [1, 2, 3, 4, 5] 

Without using a normal for loop, write a list comprehension to create a new list where each number is doubled.
'''
numbers = [1, 2, 3, 4, 5] 

doubled_numbers = [number * 2 for number in numbers]

print(doubled_numbers)