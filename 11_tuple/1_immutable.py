numbers = (10, 20, 30, 40, 50)

numbers[0] = 100

print(numbers)  #--> Expected [100, 20, 30, 40, 50]

# But we do get TypeError --> TypeError: 'tuple' object does not support item assignment

'''
interview qstn: You cannot modify an existing element through item assignment. However, 
a tuple can contain a mutable object, such as a list, whose contents may be changed.

'''